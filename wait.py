from .. import loader, utils

import logging
import datetime
import time
import asyncio
from datetime import*

logger = logging.getLogger(__name__)


def register(cb):
    cb(WAITMod())


@loader.tds
class WAITMod(loader.Module):
    """Provides a message saying that you are unavailable"""
    strings = {"name": "wait"}

    def __init__(self):
        self.name = self.strings["name"]

    def config_complete(self):
        pass

    async def wait5cmd(self, message):
        """Эта команда удаляет сообхение черезе 5 секунд"""
        await utils.answer(message, "Через 5 секунд это сообщение удалится")

        for i in range(4, -1, -1):
            await asyncio.sleep(1)
            await utils.answer(message, "Через " + str(i) + " секунд это сообщение удалится")

        await message.delete()

    async def waitcmd(self, message):
        """Эта команда удаляет сообхение через n секунд, \nписать нужно так: .wait n"""
        args = utils.get_args(message)
        if not args or len(args) > 1:
            await utils.answer(message, "Вы не указали число секунд или указали несколько параметров")
        else:
            try:
                x = int(args[0])
                await utils.answer(message, "Через " + str(x) + " секунд это сообщение удалится")
                
                dd = time.time()

                while time.time() - dd < x:
                    await asyncio.sleep(1)
                    await utils.answer(message, "Через " + str(x - round(time.time() - dd)) + " секунд это сообщение удалится")
                await message.delete()
            except:
                await utils.answer(message, "Вы указали не число!")

    async def tagcmd(self, message):
        """Эта команда для троллинга друзей. \nЕй вы можете тегнуть друга, а сообщение само удалится!"""
        await message.delete()
