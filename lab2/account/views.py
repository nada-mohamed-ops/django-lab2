from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *



def account_list(request):
    context = {}
    accountsobj = Account.objects.all() 
    context["accounts"] = accountsobj
    return render(request, "account/list.html", context)


def account_create(request):
    context = {}
    if request.method == "POST":
       
        if (
            len(request.POST["username"]) > 0
            and len(request.POST["username"]) <= 100
            and len(request.POST["password"]) <= 200
            and request.POST["email"]
        ):
            accountobj = Account()
            accountobj.username = request.POST["username"]
            accountobj.email = request.POST["email"]
            accountobj.password = request.POST["password"]
            accountobj.save()
            return redirect("account_list")
        else:
            context["error"] = "Invalid data"

    return render(request, "account/create.html", context)


def account_update(request, id):
    context = {}
    try:
        accountobj = Account.objects.get(id=id)  
        if request.method == "POST":
            if (
                len(request.POST["username"]) > 0
                and len(request.POST["username"]) <= 100
                and len(request.POST["password"]) <= 200
                and request.POST["email"]
            ):
                accountobj.username = request.POST["username"]
                accountobj.email = request.POST["email"]
                accountobj.password = request.POST["password"]
                accountobj.save()
                return redirect("account_list")
            else:
                context["error"] = "Invalid data"
        context["account"] = accountobj
    except Account.DoesNotExist:
        return HttpResponse("Account not found", status=404)

    return render(request, "account/update.html", context)


def account_delete(request, id):
   
    context = {}
    try:
        accountobj = Account.objects.get(id=id) 
        if request.method == "GET":
            accountobj.delete()
            return redirect("account_list")
        context["account"] = accountobj
    except Account.DoesNotExist:
        return HttpResponse("Account not found", status=404)
    return render(request, "account/list.html", context)


def account_details(request, id):
    context = {}
    accountobj = Account.objects.get(id=id)  
    context["account"] = accountobj
    return render(request, "account/details.html", context)
