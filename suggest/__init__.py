import py_eureka_client.eureka_client as eureka_client
import logging

logging.basicConfig()

your_rest_server_port = 9090
# The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
eureka_client.init(eureka_server="http://34.66.153.219:8761/eureka/",
                   app_name="suggestion_service",
                   instance_port=your_rest_server_port,
                   vip_address="http://34.69.92.81/suggest/suggestion_list",
                   port=80,
                   secure_vip_address="https://34.69.92.81/suggest/suggestion_list",
                   secure_port=443)
