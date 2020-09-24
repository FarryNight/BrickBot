# BrickBot Framework on Mirai

> 警告：本框架仅为个人学习使用，功能性不强，而且会有很多 `bug`，生产环境建议使用其他成熟的框架
>
> 目前最新版本为： `Dev 0.2`

`BrickBot`  是一个基于 `mirai-api-http` 的轻量机器人开发框架，使用语言为 `Python`



## 快速开始

`BrickBot` 基于 `mirai-api-http` ，因此你的第一步应该是安装服务端，这里推荐使用 `MiraiOK`。



### 服务端部署

1. 参见 [MiraiOK](https://github.com/LXY1226/MiraiOK) 提供的教程，安装服务端程序，并运行一次生成对应文件
2. 前往 https://github.com/project-mirai/mirai-api-http/releases 下载最新http插件包并放入上一步生成的plugins文件夹
3. 运行一次 `MiraiOK` 并关闭，修改配置文件，实现 `qq` 自动登录并打开 `mirai-api-http` 的 `websocket` 选项



### 你的第一个应用

编写主函数 `main.py`

```python
from brickbot.session import Bot
from private import address, port, authKey, botqq

if __name__ == '__main__':
    bot = Bot(address, port, authKey)  # 创建一个 Bot 实例
    bot.login(botqq)  # 登陆 Bot （注意：需要主程序已登陆对应 qq）

    bot.registerPlugins([
        'plugins.base.reply'
    ])  # 插件注册，规范如上

    bot.loop()  # 开始监听事件循环
```



### 插件规范

在上一步中，我们注册了一个名为 `plugins.base.reply` 的插件，在 `BrickBot` 中，插件以目录的最深层为终点，也就是说明这个插件的路径应该是 `plugins/base/reply.py`，如下便是一个最简单的插件

```python
from brickbot.session import Bot
from brickbot.message import processChain, GroupMessage, Message, Plain


@GroupMessage
def reply(session: Bot, msg: Message):  # 函数名称随意
    txt = processChain(msg.chain)  # 处理消息链，以获得消息中的纯文本
    if txt == 'test':
        session.sendGroupMessage(msg.getGroupId(), [
            Plain('Hello world!')
        ])  # sendMessage 方法第二个参数都是消息链
```



## Hello world

将插件放置到相应的目录，并运行 `main.py` 

![image-20200924104054507](http://jerrita-img.test.upcdn.net/img/20200924104054.png)

可以看到插件已经成功加载，并且机器人回复了你 `Hello world!`



## 鸣谢

- `Mirai` 开源项目 https://github.com/mamoe/mirai
- `mirai-api-http` 提供的接口支持

