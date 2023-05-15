from .. import loader, utils
from asyncio import sleep
import random

class GalaxyMod(loader.Module):
    strings = {"name": "GalaxyMod"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
    async def galaxycmd(self, message):
        """[by n3rz4, @n3rz4_bloody_phoenix]🍒  Пример ввода: .galaxy <задержка появления текста в секундах🍓> <шапка> 🦊"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>модуль galaxy завершил свое истребление!!</b>")
            return
        await utils.answer(
            message,
            "<b>модуль начал свое истребление\n\n"
            "Чтобы его остановить, используй <code>.galaxy</code></b>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [   
        "сын шлюхе сасе хуй",
        "епал тебя у магазина",
        "я твою мать ебал у центра",
        "твая мать сасала мне пряма на публике",
        "перерезал тваей матери ей гарлавину",
        "я твоей матери вагину вспорю",
        "ебал тя красива",
        "соси ты мне красиво",
        "я матери твоей анальник ее расхуярил",
        "я тебе щас нахуй ноги сломаю",
        "я гримировал tya хуйом",
        "я тваю маму ебал у поезда",
        "саси паршива",
        "атсоси не жалуясь",
        "пересаси хуй наш",
        "высасе наши хуи",
        "я твою маму ебал в рот",
        "я епал тя у кровати",
        "всасе хуй",
        "наркотиками тебя епал",
        "карявый саси сваим рылам мне",
        "ебал тя у канализации",
        "у твоей матери ебало ее зависит от моего хуя хе-хе",
        "чортава сасе ез ез",
        "правдой тя ебу",
        "тупа сасеш кхе-кхе",
        "тужься пидарас на маем хуе",
        "хыхы ты наши хуи сасал не па детски",
        "епу тя у ваенкамата"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)
			
		
	