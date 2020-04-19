from celery import shared_task
from django_ros.ROS.Service import RosService


@shared_task
def run_service(rosbridge_url: str, service_name: str, service_type: str):
    RosService.run_service(rosbridge_url, service_name, service_type)


@shared_task
def is_connected(ros_bridge_url: str) -> bool:
    RosService.is_connected(ros_bridge_url)

