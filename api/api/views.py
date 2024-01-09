from django.http import JsonResponse

def get_json(request):
    data = [
        {"number": 1, "title": "駐輪場", "url": "www/arukuarupaka/home/tyuurinn"},
        {"number": 2, "title": "通知", "url": "www/arukuarupaka/home/notification"},
    ]
    return JsonResponse(data, safe=False)
