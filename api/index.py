
from midjourney.Midjourney import MidjourneyClient
import pprint


import os
import json

import time
import sys

from flask import Flask, render_template, request, jsonify

def process_message(message):
    pprint.pprint(message)
    sys.stdout.flush()
app = Flask(__name__,  static_url_path='/static', template_folder='./templates')



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


@app.route('/')
def index():
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







