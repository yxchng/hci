
from midjourney.Midjourney import MidjourneyClient
import pprint


import os
import json

import time
import sys
import requests

from flask import Flask, render_template, request, jsonify

def process_message(message):
    pprint.pprint(message)
    sys.stdout.flush()
app = Flask(__name__,  static_url_path='/static', template_folder='./templates')

print("CURRENT WORKING DIR", os.getcwd())


#@app.route('/midjourney1')
#def midjourney1():
#    #content = request.json
#    #prompt = content['prompt']
#    url = request.args.get('url')
#    print(url)
#
#    client = MidjourneyClient(
#        name="test",
#        token="MTAxODY0MjEyMjkzODc5Mzk5NA.Gg_GFR.U7o1hYzWFu1XUJdPuigHRwtxvqjoj0yGR_FK38",  # your discord token
#        application_id="936929561302675456",  # bot application_id
#        guild_id="1114843849496461383",  # your discord server id or None
#        channel_id="1114843849496461386",  # your channel_id
#        message_handler=process_message,
#    )
#    client.run()
#    time.sleep(3)
#    # get info of the Client
#    #client.info()
#    #client.imagine("{:s} children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))
#    client.imagine("https://hci-silk.vercel.app/static/slice1.jpg In front of western hills white egrets fly up and down. children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))
#
#    client.interact(message_id="", label="U1")
#
#    #path = os.path.abspath('static/TEMP.txt')
#    #print(path)
#    ##path = '../static/TEMP.txt'
#    #with open(path, 'w') as f:
#    #    f.write('temp')
#
#    time.sleep(120)
#    #return render_template('index.html')
#    return ('', 204)

@app.route('/midjourney2')
def midjourney2():
    #content = request.json
    #prompt = content['prompt']
    url = request.args.get('url')
    print(url)

    client = MidjourneyClient(
        name="test",
        token="MTAxODY0MjEyMjkzODc5Mzk5NA.Gg_GFR.U7o1hYzWFu1XUJdPuigHRwtxvqjoj0yGR_FK38",  # your discord token
        application_id="936929561302675456",  # bot application_id
        guild_id="1114843849496461383",  # your discord server id or None
        channel_id="1114843849496461386",  # your channel_id
        message_handler=process_message,
    )
    client.run()
    time.sleep(3)
    # get info of the Client
    #client.info()
    #client.imagine("{:s} children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))
    client.imagine("https://hci-silk.vercel.app/static/slice2.jpg In peach-mirrored stream mandarin fish are full grown.children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))

    client.interact(message_id="", label="U1")

    #path = os.path.abspath('static/TEMP.txt')
    #print(path)
    ##path = '../static/TEMP.txt'
    #with open(path, 'w') as f:
    #    f.write('temp')

    time.sleep(120)
    #return render_template('index.html')
    return ('', 204)

@app.route('/midjourney4')
def midjourney4():
    #content = request.json
    #prompt = content['prompt']
    url = request.args.get('url')
    print(url)

    client = MidjourneyClient(
        name="test",
        token="MTAxODY0MjEyMjkzODc5Mzk5NA.Gg_GFR.U7o1hYzWFu1XUJdPuigHRwtxvqjoj0yGR_FK38",  # your discord token
        application_id="936929561302675456",  # bot application_id
        guild_id="1114843849496461383",  # your discord server id or None
        channel_id="1114843849496461386",  # your channel_id
        message_handler=process_message,
    )
    client.run()
    time.sleep(3)
    # get info of the Client
    #client.info()
    #client.imagine("{:s} children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))
    client.imagine("https://hci-silk.vercel.app/static/slice1.jpg In front of western hills white egrets fly up and down. children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))

    client.interact(message_id="", label="U1")

    #path = os.path.abspath('static/TEMP.txt')
    #print(path)
    ##path = '../static/TEMP.txt'
    #with open(path, 'w') as f:
    #    f.write('temp')

    time.sleep(120)
    #return render_template('index.html')
    return ('', 204)

@app.route('/midjourney3')
def midjourney3():
    #content = request.json
    #prompt = content['prompt']
    url = request.args.get('url')
    print(url)

    client = MidjourneyClient(
        name="test",
        token="MTAxODY0MjEyMjkzODc5Mzk5NA.Gg_GFR.U7o1hYzWFu1XUJdPuigHRwtxvqjoj0yGR_FK38",  # your discord token
        application_id="936929561302675456",  # bot application_id
        guild_id="1114843849496461383",  # your discord server id or None
        channel_id="1114843849496461386",  # your channel_id
        message_handler=process_message,
    )
    client.run()
    time.sleep(3)
    # get info of the Client
    #client.info()
    #client.imagine("{:s} children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))
    client.imagine("https://hci-silk.vercel.app/static/slice3.jpg A fisherman in bamboo hat and green straw cloak. Go fishing careless of slanting wind and fine rain.children's book, simple lines, pretty colors, Feng Zikai Chinese Children's Picture book award. 8k,--v 5 --ar 16:9".format(url))

    client.interact(message_id="", label="U1")

    #path = os.path.abspath('static/TEMP.txt')
    #print(path)
    ##path = '../static/TEMP.txt'
    #with open(path, 'w') as f:
    #    f.write('temp')

    time.sleep(120)
    #return render_template('index.html')
    return ('', 204)


@app.route('/getlatest1')
def getlatest1():
    cookies = {
        '__dcfduid': 'd60e94c002b511ee8e449da4e1b2e41d',
        '__sdcfduid': 'd60e94c102b511ee8e449da4e1b2e41dbdb14d46677fd67e56b5395d3a20a5a5692dde4e86b65fc365d30a608ff462fa',
        '__cfruid': 'f260df573349131d8d815a85879be8a4b6005994-1685869049',
        '_gcl_au': '1.1.1910309976.1685938598',
        '_ga_Q149DFWHT7': 'GS1.1.1685938598.1.0.1685938598.0.0.0',
        'locale': 'zh-CN',
        '_gid': 'GA1.2.1860600195.1685987402',
        '_ga': 'GA1.1.1916387607.1685938598',
        'OptanonConsent': 'isIABGlobal=false&datestamp=Tue+Jun+06+2023+01%3A50%3A33+GMT%2B0800+(Singapore+Standard+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
        '_ga_XXP2R74F46': 'GS1.1.1685987416.1.1.1685987437.0.0.0',
        '__cf_bm': '1l0vizD6UeXveqA6dIG5urG.p1HAMYOFbprOUHspWJY-1686022769-0-AadqG8Xl3e1hbOdmjJY3waR/7c40+q6fluxgMxM8zfYZHc8sJQetluGVRNJFswarw9csmNWD00dTzWmklNmRzUnpl53mB6jV0fStCdPpXnzL',
    }

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'MTAxODY0MjEyMjkzODc5Mzk5NA.Gg_GFR.U7o1hYzWFu1XUJdPuigHRwtxvqjoj0yGR_FK38',
        # Requests sorts cookies= alphabetically
        # 'cookie': '__dcfduid=d60e94c002b511ee8e449da4e1b2e41d; __sdcfduid=d60e94c102b511ee8e449da4e1b2e41dbdb14d46677fd67e56b5395d3a20a5a5692dde4e86b65fc365d30a608ff462fa; __cfruid=f260df573349131d8d815a85879be8a4b6005994-1685869049; _gcl_au=1.1.1910309976.1685938598; _ga_Q149DFWHT7=GS1.1.1685938598.1.0.1685938598.0.0.0; locale=zh-CN; _gid=GA1.2.1860600195.1685987402; _ga=GA1.1.1916387607.1685938598; OptanonConsent=isIABGlobal=false&datestamp=Tue+Jun+06+2023+01%3A50%3A33+GMT%2B0800+(Singapore+Standard+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; _ga_XXP2R74F46=GS1.1.1685987416.1.1.1685987437.0.0.0; __cf_bm=1l0vizD6UeXveqA6dIG5urG.p1HAMYOFbprOUHspWJY-1686022769-0-AadqG8Xl3e1hbOdmjJY3waR/7c40+q6fluxgMxM8zfYZHc8sJQetluGVRNJFswarw9csmNWD00dTzWmklNmRzUnpl53mB6jV0fStCdPpXnzL',
        'referer': 'https://discord.com/channels/1114843849496461383/1114843849496461386',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'zh-CN',
        'x-discord-timezone': 'Asia/Singapore',
        'x-super-properties': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMTMuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjExMy4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIwMjgyOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    }

    params = {
        'mentions': '1018642122938793994',
    }

    response = requests.get('https://discord.com/api/v9/guilds/1114843849496461383/messages/search', params=params, cookies=cookies, headers=headers)

    js = json.loads(response.content)
    print(js['total_results'])

    print(js['messages'][0][0]['attachments'])
    attachments = js['messages'][0][0]['attachments']
    if len(attachments) > 0:
         attachment = attachments[0]
         if attachment['content_type'] == 'image/png' and 'white' in attachment['url']:

            return jsonify(url=attachment['url'])
    return jsonify(url="")

@app.route('/')
def index():
    print('folder path', os.getcwd())
    directory_list = list()
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for name in dirs:
            directory_list.append(os.path.join(root, name))
    print(directory_list)
    return render_template('index.html')

@app.route('/page0')
def page0():
    return render_template('page0.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/page3')
def page3():
    return render_template('page3.html')

@app.route('/page4')
def page4():
    return render_template('page4.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')

@app.route('/page6')
def page6():
    return render_template('page6.html')

@app.route('/page7')
def page7():
    return render_template('page7.html')

@app.route('/page8')
def page8():
    return render_template('page8.html')

if __name__ == '__main__':
    app.run(debug=True)







