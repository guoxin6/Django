from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def login_view(request):
    return render(request,"login.html")

def hello(request):
#   return HttpResponse("hello world")
    result={
        "code":200,
        "message":"success",
        "date":[{"use":"admin1"},
                {"use":"admin2"}
                ]
    }
    return JsonResponse(result)

def test(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        result = {
            "code": 200,
            "message": "success",
            "date": [{"use": "admin1"},
                     {"use": "admin2"}
                     ],
            "token": "xxx"
        }
        return JsonResponse(result)




