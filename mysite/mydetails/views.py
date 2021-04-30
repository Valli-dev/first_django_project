from django.http import JsonResponse

# Create your views here.

def index(request):
    
    data = { "Name" : "Vallimayil", "Track": "Backend Python", "Message": "Hello Mentor, you are teaching good"}
    
    return JsonResponse(data)
