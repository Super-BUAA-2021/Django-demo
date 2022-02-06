from django.shortcuts import render
import json
from user.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def register(request):
	if request.method == 'POST':
		# 检测 POST 类型的请求
		
		data_json = json.loads(request.body)
		# 此时 data_json 已经转为了字典类型

		username = data_json['username']
		password1 = data_json['password1']
		password2 = data_json['password2']
		email = data_json.get('email', '')
		# 不确定是否有这个参数，使用get

		if password1 != password2:
			return JsonResponse({'result': 0, 'message': '两次密码不一致!'})
		# 虽然密码一致性与合法性检测一般是前端判断
		# 但是后端最好也加上，以防万一
		
		user = User(username=username, password=password1, email=email)
		# id 是自动赋值，不需要指明
		# post 不赋值会使用默认值0
		
		user.save()
		return JsonResponse({'result': 1, 'message': '注册成功!'})
		# 正常结束后需要给一个反馈信息

@csrf_exempt
def login(request):
	if request.method == 'POST':
		id = request.session.get('id', 0)
		# 从 session 中获取信息
		if id != 0:
			return JsonResponse({'result': 0, 'message': '用户已登录!'})
		data_json = json.loads(request.body)
		username = data_json['username']
		password = data_json['password']
		if User.objects.filter(username=username).exists() == True:
			user = User.objects.get(username=username)
		else:
			return JsonResponse({'result': 0, 'message': '用户不存在!'})
		if user.password == password:
			request.session["id"] = user.id
			# 登录成功后就把 id 存进去

			return JsonResponse({'result': 1, 'message': '登录成功!'})
		else:
			return JsonResponse({'result': 0, 'message': '密码错误!'})

@csrf_exempt
def logout(request):
	if request.session.get('id', 0) != 0:
		request.session.flush()
		# 清空所有的信息
		return JsonResponse({'result': 1, 'message': r'已登出!'})
	else:
		return JsonResponse({'result': 0, 'message': r'请先登录!'})
