from django.shortcuts import render, HttpResponse, redirect
from todolistapp.models import *
import datetime
import csv
import json
import os
from django.http import FileResponse
from django.conf import settings


# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("Aboutt")

def contact(request):
    return HttpResponse("Contactt")

def addtask(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        image = request.FILES.get("image")

        if due_date:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
        else:
            due_date = None

        addtaskz = Task(title=title, description=description, due_date=due_date, image=image,)
        addtaskz.save()

    return render(request, 'addtask.html')

def displaytask(request):
    taskadded = Task.objects.all()
    return render(request, 'displaytask.html', {'Taskadded': taskadded})

def deletetask(request, id):
    dele = Task.objects.get(id=id)
    dele.delete()
    return redirect("/modifytask")

def updatetask(request, id):
    data = Task.objects.get(id=id)
    return render(request, 'updatetask.html', {'Data': data})

def do_updatetask(request, id):
    task_id = Task.objects.get(id=id)
    if request.method == "POST":
        task_id.title = request.POST.get("title")
        task_id.description = request.POST.get("description")
        task_id.status = request.POST.get("status")
        task_id.due_date = request.POST.get("due_date")

        if request.FILES.get("image"):
            task_id.image = request.FILES.get("image")
            
        task_id.save()
    return redirect("/modifytask")


def modifytask(request):
    taskadded = Task.objects.all()
    return render(request, 'modify.html', {'Taskadded': taskadded})


# def download_taskss(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "savedata.csv")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", newline='', encoding='utf-8') as f:
        ff = csv.writer(f)
        
        ff.writerow(['ID', 'Title', 'Description', 'Due Date', 'Status'])

        tasks = Task.objects.all()

        for task in tasks:
            ff.writerow([task.id, task.title, task.description, task.due_date, task.status])

    return FileResponse(open(file_path, "rb"), as_attachment=True, filename="savedata.csv")


def download_tasks(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "savetasksdata.json")

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    tasks = Task.objects.all()

    tasks_data = [
        {
            "ID": task.id,
            "Title": task.title,
            "Description": task.description,
            "Due Date": task.due_date.strftime("%Y-%m-%d") if task.due_date else None,
            "Status": task.status,
        }
        for task in tasks
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(tasks_data, f, indent=4)

    return FileResponse(open(file_path, "rb"), as_attachment=True, filename="savetasksdata.json")

