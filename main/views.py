# coding: utf-8

from django.shortcuts import render

def main (request):
    return render(request, "index.html", locals())

def about (request):
    return render(request, "about.html", locals())

def contact (request):
    return render(request, "contact.html", locals())




