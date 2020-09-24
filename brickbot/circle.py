from brickbot.logger import Logger
from brickbot.message import process_msg
import time
import threading
import asyncio
import websockets

logger = Logger(__name__)


class Circle():
    def __init__(self, session):
        self.reg = []
        self.session = session
        logger.log(f'Circle inited.')

    def heartBeat(self, verify, session, qq):
        while True:
            logger.log('Heart beat start.')
            verify(session, qq)
            time.sleep(60)

    def register(self, func, args):
        thread = threading.Thread(target=func, args=args)
        self.reg.append(thread)

    def start(self):
        for thread in self.reg:
            thread.start()

    async def listener(self, addr, session):
        uri = f"ws://{addr}/all?sessionKey={session}"
        async with websockets.connect(uri) as websocket:
            while True:
                msg = await websocket.recv()
                process_msg(self.session, msg)

    def loop(self, addr, session):
        logger.log('Listener starting...')
        asyncio.get_event_loop().run_until_complete(self.listener(addr, session))
