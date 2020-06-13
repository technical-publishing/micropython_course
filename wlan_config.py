import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    wlan.connect('DumBoBox', '50978253832944485741')
    while not wlan.isconnected():
        pass
    print("Netzwerkkonfiguration: ", wlan.ifconfig())