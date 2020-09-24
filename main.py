from brickbot.session import Bot
from private import address, port, authKey, botqq

if __name__ == '__main__':
    bot = Bot(address, port, authKey)  # 创建一个 Bot 实例
    bot.login(botqq)  # 登陆 Bot （注意：需要主程序已登陆对应 qq）

    bot.registerPlugins([
        # 'plugins.turing.main',
        'plugins.base.reply'
    ])  # 插件注册，规范如上

    bot.loop()  # 开始监听事件循环
