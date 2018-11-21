from django.http import HttpResponse, HttpResponseRedirect

#Importing basic rendering modules
from django.shortcuts import render_to_response
from django.template import RequestContext

#Importing uploaded data
from das.forms import UploadFile
import csv

#Using transaction to bypass all ORM shit
from django.db import transaction

#Importing our database
from das.models import ChartDb


#importing charts
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot

from datetime import datetime
import time


def index(request):
    context=RequestContext(request)
    message="Hello"
    if request and request.method=='POST':
        form=UploadFile(request.POST, request.FILES)
        if form.is_valid():
            reader=csv.reader(form.cleaned_data['csv_file'])
            with transaction.commit_on_success():
                for row in reader:
                    # Check to ensure DHT is working correctly
                    if row[2] =='0':
                        hum=row[9]
                        temp=row[10]
                    else:
                        hum=None
                        temp=None

                    k=(int(row[3]),
                       int(row[4]),
                       int(row[5]),
                       int(row[6]),
                       int(row[7]),
                       int(row[8])
                    )
                    current_time=datetime(*k[0:6])
                    day_time=datetime.date(current_time)
                    delta_time=int(time.mktime(current_time.timetuple())*1000)
                    #Check to ensure rtc is working properly
                    if row[1] =='0':
                        ChartDb.objects.create(
                        sd=row[0],
                        rtc=row[1],
                        dht=row[2],
                        year=row[3],
                        month=row[4],
                        day=row[5],
                        hour=row[6],
                        min=row[7],
                        sec=row[8],
                        hum=hum,#9
                        temp=temp,#10
                        rain=row[11],
                        soil=row[12],
                        light=row[13],
                        hour_time=datetime(*k[0:6]),
                        day_time=day_time,
                        full_time=delta_time
                        )
            message ="File uploaded sucessfully"
            return HttpResponseRedirect('timer')
        else:
            print form.errors
            print request.FILES
    else:
        form=UploadFile()

    context_dict={'message':message}
    context_dict['form']=form
    return render_to_response('index.html', context_dict, context)





def charter(request):
    sensor_list=("hum","temp","rain","soil","light")
    color_list=("#4cd1ee","#ff9b02","#2a3fe1","#925407","#f5f61d")
    label_list=("Percentage","Degree Celcius", "From 0 to 1023", "From 0 to 1023", "In Lux")
    chart=[]
    opt=[]
    i=0

    for color in color_list:
        opt.append({'title':"Website",
            'xaxis':{'mode':"time",
                     'axisLabel': "<--- Time in \"Hours:Min\" --->"},
            'yaxis':{'axisLabel':label_list[i],
                    'axisLabelUseCanvas': True,
                    'axisLabelFontSizePixels': 18,},

            'lines':{'fill':"false"},
            'colors': [color],
        })
        i=i+1

    if request.GET:
        if 'Day' in request.GET:
            day_q=request.GET['Day']
            query=ChartDb.objects.filter(day_time=datetime.strptime(day_q,"%Y,%m,%d"))
        elif 'All' in request.GET:
            day_q="All The Data in Databse"
            query=ChartDb.objects.all()
    else:
        return HttpResponseRedirect('/timer/')


    i=0
    for sensor in sensor_list:
        data_source=ModelDataSource(query, fields=['full_time',sensor])
        chart.append(flot.LineChart(data_source, options=opt[i]))
        i=i+1

    context=RequestContext(request)
    contect_dict={'charts':chart}
    contect_dict['a']=day_q
    return render_to_response('charter.html',contect_dict,context)


def timer(request):
    query=ChartDb.objects.all()
    a=query.order_by('day_time').distinct('day_time').values('day_time')

    context=RequestContext(request)
    contect_dict={'a':a}
    return render_to_response('timer.html',contect_dict,context)

