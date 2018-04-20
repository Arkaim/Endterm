from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from .models import *


@csrf_exempt
def blog(request):
    try:
        if request.method == "GET":
            posts = Post.objects.filter(is_active=True)
            posts_json = [post.to_json() for post in posts]
            return JsonResponse(posts_json, safe=False)

        elif request.method == "POST":
            post = Post()
            post.post_name = request.POST.get('name', '')
            post.post_text = request.POST.get('text', '')
            post.save()

            return JsonResponse(post.to_json(), status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def contact_detail(request, post_id):
    try:
        try:
            contact = Contact.objects.get(pk=contact_id, is_active=True)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        if request.method == "GET":
            return JsonResponse(contact.to_json(), status=200)

        elif request.method == "PUT":
            contact.name = request.POST.get('name', contact.name)
            contact.surname = request.POST.get('surname', contact.surname)
            contact.phone_num = request.POST.get('phone_num', contact.phone_num)
            contact.description = request.POST.get('description', contact.description)
            contact.pub_date = request.POST.get('pub_date', contact.pub_date)
            contact.save()

            return JsonResponse(contact.to_json(), status=200)

        elif request.method == "DELETE":
            contact.is_active = False
            contact.save()
            return JsonResponse(contact.to_json(), status=200)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

