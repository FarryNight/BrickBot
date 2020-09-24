from brickbot.logger import Logger
import requests
import json
import time

logger = Logger(__name__)

class Protocals():
    def __init__(self, rootUrl, authKey):
        self.authKey = authKey
        self.rootUrl = rootUrl
        self.authUrl = rootUrl + '/auth'
        self.aboutUrl = rootUrl + '/about'
        self.verUrl = rootUrl + '/verify'
        self.loginUrl = rootUrl + '/command/send'
        self.UrlSendGroup = rootUrl + '/sendGroupMessage'

    def setSession(self, session):
        self.session = session

    def auth(self):
        data = requests.post(self.authUrl, json.dumps({'authKey': self.authKey}))
        response = json.loads(data.text)
        if response['code'] == 0:
            return response['session']
        else:
            logger.log('Error auth key!')
            return 0

    def getVersion(self):
        data = requests.get(self.aboutUrl)
        response = json.loads(data.text)
        return response['data']['version']

    def verify(self, session, qq):
        while True:
            data = requests.post(self.verUrl, json.dumps({'sessionKey':session, 'qq':qq}))
            response = json.loads(data.text)
            if response['code'] == 0:
                logger.log(f'Verify success!')
                return 0
            else:
                logger.log(f'Verify failed because {response["msg"]}, sleep 5s.')
                time.sleep(5)

    def login(self, qq, passwd):
        data = requests.post(self.loginUrl, json.dumps({
            'authKey': self.authKey,
            'name': 'login',
            'args': [str(qq), passwd]
        }))
        response = json.loads(data.text)
        return response

    def sendGroupMessage(self, groupId, msgChain):
        data = requests.post(self.UrlSendGroup, json.dumps({
            'sessionKey': self.session,
            'target': groupId,
            'messageChain': msgChain
        }))
        response = json.loads(data.text)
        return response