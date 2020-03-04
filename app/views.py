from django.shortcuts import render
from django.http import JsonResponse
from .models import UserRank
# Create your views here.

def addrank(request):

    if request.method == 'GET':
        return JsonResponse({'errcode':1,'errmsg':'请求方式错误'})
    agent = request.POST.get('agent',None)
    score = request.POST.get('score',None)

    if not all(['agent','score']):
        return JsonResponse({'errcode':1,'errmag':'数据不完整'})
    try:
        u = UserRank.objects.filter(agent=agent).first()
    except:
        return JsonResponse({'errcode': 1, 'errmsg': '上传失败'})
    if u:

        u.score = score
        u.save()
        return JsonResponse({'errcode': 0, 'errmsg': '上传成功'})
    try:
       UserRank.objects.create(agent=agent,score=int(score))
    except:
        return JsonResponse({'errcode':1,'errmsg':'上传失败'})
    return JsonResponse({'errcode': 0, 'errmsg': '上传成功'})

def lookrank(request):

    if request.method == 'POST':
        return JsonResponse({'errcode':1,'errmsg':'请求方式错误'})
    ulist = UserRank.objects.all().order_by('-score')
    l = []
    i = 1
    for u in ulist:
        udict = {}
        udict['rank'] = i
        udict['agent'] = u.agent
        udict['score'] = u.score
        l.append(udict)
        i += 1

    return JsonResponse({'errcode':0,'errmsg':l})








