from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Product, Record, Regist, User, Bundle, Button
import json
from django.core.mail import send_mail
from django.core.signals import request_finished
from django.dispatch import receiver
# Create your views here.

'''
def main(request):
    all_product_list = Product.objects.order_by('-product_id')[:5]
    #output = ', '.join([q.product_id for q in all_product_list])
    template = loader.get_template('backend/index.html')
    context = {
        'all_product_list': all_product_list,
    }
    return HttpResponse(template.render(context, request))
'''

def receiveCallback(request):
    if request.method == 'POST':
        print ('we are in POST request')
        received_json_data = json.loads(request.body.decode('utf-8'))
        device_id = received_json_data['device']
        sequence_num = received_json_data['seqNumber']
        q = Regist.objects.get(button_id = device_id)
        record = Record()
        record.button_id = device_id
        record.sequence_num = sequence_num
        record.regist_id = q
        record.save()
        sendConfirmationMail(received_json_data)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

#把regist_id作為參數傳入, 並且抓出其bundle的商品項目
def sendConfirmationMail(received_json_data):
    device_id = received_json_data['device']
    q = Regist.objects.get(button_id = device_id)
    orderProduct = Bundle.objects.filter(regist_id=q)
    user_name = q.cust_id
    mail_body = str(user_name) + '您好, 您訂購的商品為：' + str(orderProduct)
    send_mail('Order Detail', mail_body,'dennytsai8201@gmail.com', ['ohyewei@gmail.com'], fail_silently=False)


'''
#用監聽模式來減少庫存量
@receiver(receiveCallback)
def signal_handler(sender, **kwargs):
    print("Request Finished!!!!")
'''
