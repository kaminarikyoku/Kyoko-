from django.shortcuts import render
from django.http import HttpResponse
import random 
def index(request):
	myname="胖子伯"
	data= [i for i in range(1,43)]
	random.shuffle(data)
	lottl_numbers=data[0:6]
	special_number=data[6]
	return render(request,"index.html", locals())
	


# Create your views here.
