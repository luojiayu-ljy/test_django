from django.shortcuts import render,HttpResponse,render_to_response
import datetime
from django.http import Http404
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def home(request):
	return HttpResponse('<h1>CMDB</h1>')

def current_datetime(request):
	current_date = datetime.datetime.now()
	'''
	#Template class
	t = get_template('current_datetime.html')

	#Template reader参数context必须为一个字典
	html = t.render({'current_date':now})

	#html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)
	'''

	#捷径
	#return render_to_response('current_datetime.html',{'current_date':current_date})

	#locals()返回字典，对html局部变量名称和值进行映射
	return render_to_response('current_datetime.html',locals())

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hours,it will be %s.</body></html>" % (offset,dt)
	return HttpResponse(html)