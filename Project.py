import PySimpleGUI as sg
import json
from requests import get

def getIP():
    print('loading..')
    ip = get('https://api.ipify.org').text
    res = get('http://api.ipstack.com/'+ip+'?access_key=d19f6bf9beeb2919b685a14cd49a32a4&format=1').text
    res = json.loads(res)
    print(res)
    return res
layout = [[sg.Text('IP GeoLocation')],
          [sg.Multiline(size=(30, 15), key='textbox')],
          [sg.Button('Ok'), sg.Button('Cancel')]]
# Create the Window
window = sg.Window('IP Locator', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'Ok':
        res = getIP()
        output = "IP address: {} \nIP Type: {}\nContinent: {} \nCountry: {} \nRegion Name: {}".format(res["ip"],res["type"],res["continent_name"],res["country_name"],res["region_name"])
        window['textbox'].update(output)
        window['Ok'].update(disabled=True)
window.close()

