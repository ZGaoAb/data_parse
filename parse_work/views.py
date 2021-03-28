from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from parse_work.models import Temperature


def temperatrue(request):
    tempe_datas = Temperature.objects.all().order_by("-year")
    return render(request,'temperature_index.html',{'datas' : tempe_datas})

def show_co2(request,year):
    temperatrue = Temperature.objects.get(pk=year)
    co2_datas = temperatrue.co2_set.all()
    return render(request, 'co2_list.html', {'co2_datas' : co2_datas,'year':year})