import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("5AHET/Luftdruck")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def main():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.connect("projects-et.htl-hl.ac.at", 1883)

    mqttc.loop_forever()

import paho.mqtt.publish as publish
import time
i = 0
while True:
    i+= 7
    if i > 150:
        i=0
    publish.single("5AHET/Luftdruck", f'{i}', hostname = "projects-et.htl-hl.ac.at")
    time.sleep(1)

if __name__ == '__main__':
    main()
