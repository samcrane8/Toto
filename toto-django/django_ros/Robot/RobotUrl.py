from django.urls import path

from . import RobotView

urlpatterns = [
    path('create/', RobotView.create, name='robot create'),
    path('read/', RobotView.read, name='robot read'),
    path('update/', RobotView.update, name='robot update'),
    path('delete/', RobotView.delete, name='robot delete')
]
