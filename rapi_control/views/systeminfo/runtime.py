from django.shortcuts import HttpResponse

def runtime(request):
    try :
        time_file = open('/proc/uptime')
        time = time_file.read()
    except:
        pass