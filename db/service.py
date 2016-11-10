import consul
import sqlite3
import json
from flask import Flask, Response

app = Flask(__name__)

def deregister(service_id):
  c = consul.Consul()
  c.agent.service.deregister(service_id)

def register(host_consul, port_consul):
  c = consul.Consul(host="127.0.0.1", port=8500)
  c.agent.service.register(name="abc1", service_id="abc1", address=host_consul, port=port_consul)
  
@app.route("/service", methods=['POST', 'GET'])
def connectToDB():
  conn = sqlite3.connect("sqlite.db")
  cursor = conn.execute("SELECT * FROM items")
  data_cursor = []
  for i in cursor:
    data_cursor.append(i[0])
  return json.dumps(data_cursor)
  
if __name__ == "__main__":
  register("127.0.0.1", 8080)
  #deregister("abc1")
  print(connectToDB())
  app.run(port=8080)
  
