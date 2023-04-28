from django.shortcuts import render

# Create your views here.


def built_in_filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'BF':'haI THis iS vEnky','dt':dt,'c':2}
    return render (request,'built_in_filters.html',d)

    import datetime
    dt=datetime.datetime.now()
    d={'data':'HAI HOw aRe YoU','dt':dt,'c':0}
    return render(request,'built_in_filters.html',d)