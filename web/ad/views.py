from django.shortcuts import render
from django.http import HttpResponse
from .models import Workstation, Printer

def index(request):
    return HttpResponse("<h2>Хехех приветик</h2>")

def workstation_page(request):
    workstations = Workstation.objects.all()
    return render(request, 'ad/workstation.html', {'workstations': workstations})

def printer_page(request):
        printers = Printer.objects.all()
        return render(request, 'ad/printer.html', {'printers': printers})
