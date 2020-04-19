from django.urls import path

from . import RobotView

urlpatterns = [
    path('post/', RobotView.create, name='robot create'),
    path('get/', RobotView.read, name='robot read'),
    path('update/<int:robot_id>', RobotView.update, name='robot update'),
    path('delete/<int:robot_id>', RobotView.delete, name='robot delete')
]
