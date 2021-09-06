from pathlib import Path
import os
import math
import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from .models import MyProduct
from .models import MyOrder
from .models import MyUser
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.contrib.auth.hashers import (make_password, check_password)
from django.contrib.admin.utils import flatten
from django.views.generic import TemplateView
#from django.utils import simplejson
import json

class VueAppView(TemplateView):
    template_name = 'shop/index.html'

# from django.views.generic.base import TemplateView
# class IndexTemplateView(TemplateView):
#     def get_template_names(self):
#         template_name = "index.html"
#         return template_name

# Create your views here.

def build(request):
	# with open(str(Path(__file__).resolve().parent.parent) + os.path.sep + str(os.path.join('shop', 'templates', 'shop') + os.path.sep + 'index.html'), 'r') as f:
	# 	file_data = f.read()
	# 	return HttpResponse(file_data)
	# with open(str(Path(__file__).resolve().parent.parent) + os.path.sep + str(os.path.join('client', 'vue-super-shop', 'dist') + os.path.sep + 'vue.html'), 'r') as f:
	# 	file_data = f.read()
	# 	return HttpResponse(file_data)
	# return JsonResponse({ 'allProducts': "out", 'message': 'success' })
	# return render(request, 'index.html')
	return render(request, template_name='index.html')

def home(request):
	data = serializers.serialize('json', MyProduct.objects.all())
	mailOfUser = request.GET["useremail"]
	# return JsonResponse({ 'allProducts': "out", 'message': 'success' })
	myjson = json.dumps([{'id': o.id, 'name': o.name, 'price': o.price } for o in MyProduct.objects.all()])
	# myjson = json.dumps([{'id': o.id, 'name': o.name, 'price': o.price} for o in MyUser.objects.get(email=request.GET["useremail"]).productsInBucket])
	# myjson = str(myjson)
	# return JsonResponse({ 'allProducts': MyUser.objects.get(email=request.GET["useremail"]).productsInBucket, 'message': 'success' })
	return HttpResponse(myjson, content_type='application/json')

def adminOrders(request):
	data = serializers.serialize('json', MyOrder.objects.all())
	myjson = json.dumps([{'ownername': o.ownername, 'price': o.price} for o in MyOrder.objects.all()])
	# return JsonResponse({ 'allOrders': data })
	# return HttpResponse(data, content_type='application/json') 
	return HttpResponse(myjson, content_type='application/json') 

def adminProductsAdd(request):
	product = MyProduct(name=request.GET["productname"], price=request.GET["productprice"])
	product.save()
	return JsonResponse({'status': 'OK'})

def adminProductsDelete(request):
	MyProduct.objects.filter(name=request.GET["productname"]).delete()
	return JsonResponse({ 'status': 'ok' })

def productByProductID(request, productID):
	print("productID: " + str(productID))
	product = MyProduct.objects.get(id=productID)
	myjson = json.dumps({ 'product': { 'id': product.id, 'name': product.name, 'price': product.price }, 'message': 'success' })
	return HttpResponse(myjson, content_type='application/json')

def usersBucketDelete(request):
	user = MyUser.objects.get(email=request.GET["useremail"])
	productIndex = -1
	for productInBucket in user.productsInBucket:
		productIndex += 1
		strid = str(productInBucket['id'])
		if (strid == request.GET['productid']):
			user.productsInBucket.pop(productIndex)
			user.save()
			return JsonResponse({ "status": "OK", "message": "success" })
	return JsonResponse({ "status": "Error", "message": "failed" })

def usersBucketBuy(request):
	user = MyUser.objects.get(email=request.GET['useremail'])
	commonPrice = 0
	for product in user.productsInBucket:
		if product['price'] is None:
			commonPrice += 0
		else:
			commonPrice += product['price']
	if user.moneys >= commonPrice and commonPrice != 0:
		order = MyOrder(ownername=request.GET["useremail"], price=commonPrice)
		order.save()
		user.moneys -= commonPrice
		user.productsInBucket = []  
		user.save()
		return JsonResponse({'status': 'OK', 'message': 'success'})
	return JsonResponse({'status': 'Error', 'message': 'success'})

def usersAmount(request):
	user = MyUser.objects.get(email=request.GET['useremail'])
	incerementAmountBy = request.GET['amount']
	user.moneys += int(incerementAmountBy)
	user.save()
	return JsonResponse({ "status": "OK", "moneys": user.moneys, "message": "success" })

def usersCheck(request):
	# response = HttpResponse()
	# response["Access-Control-Allow-Origin"] = "*"
	# response["Access-Control-Allow-Headers"] = "*"
	user = MyUser.objects.get(email=request.GET['useremail'])
	passwordCheck = check_password(request.GET['userpassword'], user.password) and request.GET['userpassword'] != ''
	if (passwordCheck and request.GET['useremail'] == user.email):
		data = serializers.serialize('json', [user])
		# return JsonResponse({ "user": data, "status": "OK" })
		# return HttpResponse(data, content_type='application/json') 
		# return response
		myjson = json.dumps({'moneys': user.moneys, 'productsInBucket': user.productsInBucket, 'name': user.name, 'age': user.age, 'password': user.password, 'status': 'OK' })
		response = HttpResponse(myjson, content_type='application/json')
		response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, PATCH, DELETE"
		response["Access-Control-Allow-Credentials"] = True
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Headers"] = "X-Requested-With, X-Access-Token, X-Socket-ID, Accept-Language, Content-Language, Content-Type, Accept"
		return response
	# return JsonResponse({'status': 'Error'})
	# return response
	response = JsonResponse({'status': 'Error'})
	response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, PATCH, DELETE"
	response["Access-Control-Allow-Credentials"] = True
	response["Access-Control-Allow-Origin"] = "*"
	response["Access-Control-Allow-Headers"] = "X-Requested-With, X-Access-Token, X-Socket-ID, Accept-Language, Content-Language, Content-Type, Accept"
	return response

def usersUsercreatesuccess(request):
	userExists = False
	for user in MyUser.objects.all():
		if(user.email in request.GET["useremail"]):
			userExists = True
	if(userExists):
		return JsonResponse({ "message": "Error" })
	else:
		encodedPassword = "#"
		encodedPassword = make_password(request.GET["userpassword"])
		user = MyUser(email=request.GET["useremail"], password=encodedPassword, name=request.GET["username"], age=request.GET["userage"])
		user.save()
		return JsonResponse({'message': 'success'})
	return JsonResponse({'message': 'error'})

def usersBucketAdd(request):
	user = MyUser.objects.get(email=request.GET['useremail'])
	user.productsInBucket=[*user.productsInBucket, {'id': request.GET['productid'], 'idx': math.floor(random.random() * 500), 'name':request.GET['productname'], 'price':int(request.GET['productprice'])}]
	user.save()
	return JsonResponse({'status': 'OK'})

def usersBucket(request):
	allProductsInBucketOfThisUser = MyUser.objects.get(email=request.GET['useremail'])
	queryOfProducts = MyProduct.objects.all()
	products = allProductsInBucketOfThisUser.productsInBucket
	return JsonResponse({ "productsInBucket": products, "message": 'success' })

def otherRoutes(request, **routes):
	# return JsonResponse({ 'name': request.path })
	return redirect(f"/?redirectroute={request.path}")
	