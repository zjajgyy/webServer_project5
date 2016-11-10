import consul
import requests
import types

c = consul.Consul()
(service_id, service_content) = c.catalog.service("abc1")
print(service_content)
service_address = service_content[0]['ServiceAddress']
service_port = service_content[0]['ServicePort']
url = "http://"+service_address+":"+str(service_port)+"/service"
r = requests.get(url)
print(r.status_code)
print(r.text)
