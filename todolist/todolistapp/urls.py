from django.urls import path, include
from todolistapp import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('addtask', views.addtask, name='addtask'),
    path('displaytask', views.displaytask, name='displaytask'),
    path('updatetask/<int:id>', views.updatetask, name='updatetask'),
    path('do_updatetask/<int:id>', views.do_updatetask, name='do_updatetask'),
    path('deletetask/<int:id>', views.deletetask, name='deletetask'),
    path('modifytask', views.modifytask, name='modifytask'),
    path('download_tasks', views.download_tasks, name='download_tasks')
]