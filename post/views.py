from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from post.models import *
from user.models import *
from datetime import datetime
# Create your views here.

@csrf_exempt
def create(request):
	if request.method != 'POST':
		return JsonResponse({'result':0, 'message':'Error'})
	
	id = request.session.get('id', 0)
	if id == 0:
		return JsonResponse({'result':0, 'message':r'请先登录'})
	
	data_json = json.loads(request.body)
	post = Post(
		uid = id,
		title = data_json['title'],
		article = data_json['article'],
		time = datetime.now()
	)
	post.save()
	# 存储新博客文章信息

	user = User.objects.get(id = id)
	user.post += 1
	user.save()
	# 更新发表文章数量

	return JsonResponse({'result':1, 'message':r'发表成功'})


@csrf_exempt
def get_list(request):
	if request.method != 'POST':
		return JsonResponse({'result':0, 'message':'Error'})

	data_json = json.loads(request.body)
	id = int(data_json['id'])
	# 这里是用户id，获取这个用户所发表的所有文章

	posts = [{
		'id': x.id,
		'title': x.title,
		'time': x.time
	} for x in Post.objects.filter(uid = id)]
    # filter 的结果是一个类似列表的可迭代元素
    # 故可以使用 for .. in 去遍历
    # 这其实是一种压行写法
    
	return JsonResponse({'result':1, 'message':r'获取成功', 'posts':posts})

@csrf_exempt
def get_post(request):
	if request.method != 'POST':
		return JsonResponse({'result':0, 'message':'Error'})
	data_json = json.loads(request.body)
	id = int(data_json['id'])
	# 这里是文章id

	post = Post.objects.get(id = id)
	return JsonResponse({'result':1, 'message':r'获取成功', 'post': post.to_dic()})
	# 注意这里使用了to_dic()函数

@csrf_exempt
def delete_post(request):
	if request.method != 'POST':
		return JsonResponse({'result':0, 'message':'Error'})
	data_json = json.loads(request.body)
	id = int(data_json['id'])
	# 这里是文章id

	post = Post.objects.get(id = id)
	user = User.objects.get(id = post.uid)
	user.post -= 1
	user.save()
	# 记得先更新发表文章数量
	post.delete()

	return JsonResponse({'result':1, 'message':r'删除成功'})
