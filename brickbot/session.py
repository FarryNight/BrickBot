from brickbot.logger import Logger
from brickbot.protocols import Protocals
from brickbot.config import version
from brickbot.circle import Circle
from brickbot.message import processChain

logger = Logger(__name__)


class Bot():
    def __init__(self, ip='127.0.0.1', port=8080, authKey=''):
        logger.log(f'Welcome use BrickBot based on mirai, the version is {version}')
        self.ip = ip
        self.port = port
        self.authKey = authKey
        self.rootUrl = f'http://{ip}:{port}'
        self.protocals = Protocals(self.rootUrl, authKey)
        logger.log(f'Start listening on {self.rootUrl}')
        self.miraiVersion = self.protocals.getVersion()
        logger.log(f'Server version is {self.miraiVersion}')
        logger.log(f'Starting authorize...')
        self.session = self.protocals.auth()
        if self.session == 0:
            logger.log('Auth failed, please check your address or authKey!')
            exit(0)
        logger.log(f'Authorize success. Your session is {self.session}')
        self.protocals.setSession(self.session)

    def login(self, qq, passwd=''):
        logger.log(f'Connecting to account {qq}...')
        self.qq = qq
        self.passwd = passwd
        # verify
        # print(self.protocals.login(qq, passwd))
        self.protocals.verify(self.session, qq)  # 重要，在这之后你便可以进行操作
        self.cicle = Circle(self)
        self.cicle.register(self.cicle.heartBeat, (self.protocals.verify, self.session, qq))
        self.cicle.start()

    def registerPlugins(self, plugins):
        for plugin in plugins:
            logger.log(f'Loading plugin [{plugin}]')
            __import__(plugin)

    def loop(self):
        self.cicle.loop(f'{self.ip}:{self.port}', self.session)

    def sendGroupMessage(self, groupId, msgChain):
        res = self.protocals.sendGroupMessage(groupId, msgChain)
        logger.log(f'Sender -> {groupId}: {processChain(msgChain)}')
