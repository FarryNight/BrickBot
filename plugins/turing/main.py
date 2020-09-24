from brickbot.session import Bot
from brickbot.message import processChain, Message, Plain, GroupMessage
from private import turingKey
import requests
import json

url = 'http://openapi.tuling123.com/openapi/api/v2'

data = {
    'reqType': 0,
    'perception': {
        'inputText': {
            'text': 'test'
        }
    },
    'userInfo': {
        'apiKey': turingKey,
        'userId': 'placeholder'
    }
}


def getResponse(sentence, id):
    data['userInfo']['userId'] = id
    data['perception']['inputText']['text'] = sentence
    res = requests.post(url, json.dumps(data))
    return json.loads(res.text)['results'][0]['values']['text']


@GroupMessage
def reply(session: Bot, msg: Message):
    txt = processChain(msg.chain)
    if len(txt) and txt[0] == ' ':
        session.sendGroupMessage(msg.getGroupId(), [Plain(getResponse(txt, msg.sender))])
