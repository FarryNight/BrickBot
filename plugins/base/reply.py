from brickbot.session import Bot
from brickbot.message import processChain, GroupMessage, Message, Plain


@GroupMessage
def reply(session: Bot, msg: Message):  # 函数名称随意
    txt = processChain(msg.chain)  # 处理消息链，以获得消息中的纯文本
    if txt == 'test':
        session.sendGroupMessage(msg.getGroupId(), [
            Plain('Hello world!')
        ])  # sendMessage 方法第二个参数都是消息链
