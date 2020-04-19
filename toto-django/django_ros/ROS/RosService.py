import roslibpy


class RosService:

    @staticmethod
    def is_connected(ros_bridge_url: str) -> bool:
        client = roslibpy.Ros(ros_bridge_url)
        _is_connected = client.run()
        client.close()
        return _is_connected

    @staticmethod
    def get_services(ros_bridge_url: str) -> list:
        client = roslibpy.Ros(ros_bridge_url)
        client.run()
        return client.get_services()

    @staticmethod
    def run_service(rosbridge_url: str, service_name: str, service_type: str):
        client = roslibpy.Ros(rosbridge_url)
        client.run()
        service = roslibpy.Service(client, service_name, service_type)
        request = roslibpy.ServiceRequest()
        _ = service.call(request)
        client.terminate()
