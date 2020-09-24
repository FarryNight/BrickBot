from brickbot.logger import Logger
import json
import threading

logger = Logger(__name__)

Plain = lambda text: {"type": "Plain", "text": text}
At = lambda qq: {'type': 'At', 'target': qq}

groupProcesser = []


class Message():
    def __init__(self, data):
        self.data = data
        self.chain = data['messageChain']

        if 'sender' in data:
            self.sender = self.data['sender']['id']

    def getGroupId(self):
        try:
            return self.data['sender']['group']['id']
        except Exception as e:
            return 0


def processChain(chain):
    dis = []
    for i in chain:
        if type(i) == dict:
            if i['type'] == 'Plain':
                dis.append(i['text'])
    return " ".join(dis)


def GroupMessage(func):
    groupProcesser.append(func)


def process_msg(session, plainText):
    data = json.loads(plainText)
    if data['type'] == 'GroupMessage':
        logger.log(f"{data['sender']['group']['name']} ({data['sender']['group']['id']}) -> "
                   f"{data['sender']['memberName']} ({data['sender']['id']}) : {processChain(data['messageChain'])}")
    if data['type'] == 'GroupMessage':
        for func in groupProcesser:
            thread = threading.Thread(target=func, args=(session, Message(data)))
            logger.log(f'Broadcast message to {func}')
            thread.start()
