import random
from asyncio import sleep
import os
from .. import loader, utils


@loader.owner
def register(cb):
    cb(YbMod())


class YbitcMod(loader.Module):
    strings = {"name": "Ybitca"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def kingcmd(self, message):
        '''задержка + шапка'''
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b>фух</b>")
            return
        await utils.answer(
            message,
            "<b>разьебу бошку твоего отца💀\n\n",
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [" мамашу твою ебал сынок шлюхи ты хехе ", " поимел тебя сынка шлюхи ебаного прикинь ",
                 " твою мать в рот ебал",
                 " пососал ты сынок шлюхи ", " ты мне жестко отсосал щас или че хуесаска лалка ",
                 " блять вот у тебя мамаша шлюха ебучая ", " вот твою мамашу ебали а ты даж ниче не сказал лошок ",
                 " пиздец соси ", "усоси", " засоси", " пососи", " соси мне блядина ", " отсоси, сынок шлюхи ",
                 " спермоглист, ебучку втопи ",
                 " пахай на моем члене, раб", " насоси хуйца", " хуй лови ", " яйца на ", " хуй на ",
                 " я тебе свой хуй кинул как фрисби", " пес ебаный ты нахуй отсосал", " лох ебаный ты че потух опять ", " сдавил тя залупой хе"," хуй жри",
                 " слабак че спишь ",
                 " засоси", " обсоси", " сасай шкура", " переломали тебя лошара ебучая",
                 " обхуесосим тебя боребух ебаный", " ты пешка ебучая отсосавшая", " хуйло ты ", " сосал ты ",
                 " обоссал тебя ", " сру тебе в рот "
                                   " отсосешь по полной, макака ", " пососи мне, хуесоска",
                 " пересоси тут, выблядь " " ебал тебя лоха ", " по еблу слови хуйло ",
                 " почему ты хуй сосал ало блять ", " слыш полуфабрикат отсоси мне ",
                 " твоя мать так то по всем статьям шлюха "
             , " отсосешь мне хуесоска ебучая не пытайся даже сопротивление давать ",
                 " пизда я твою мамашу в рот ебал ты в кусре надеюсь ", " я твою мать в комбаине имел бля ",
                 " перехуярим тебе еблище лошара ебучая даже не думай отсосать мне хуеплетка малоразумная ",
                 " обосу тебе ебальник хуесоска ебучая ", " шлюхотень подзаборная не отсоси мне ",
                 " переломаем тебе еблище рваная курва ", "обойму спермы в тебя запустил хуйло ",
                 " обоссали тебя лошара ссаная ", " нассали тебе на патлы хуйло"
             , " насру тебе в гортань сынок шлюхи ", " обосру тебе еблище осел ебаный ", " ебало тебе ломал ",
                 " ебало тебе сломаю",
                 " сынок шлюхи тя хуем тут по ребрам ебарирую", " ну ты внатуре козел ебать я те рога вырвал",
                 " пососал ты моего члена конкретно щас олух ты сук", " ебать ты барсук я тебя в рот ебал ",
                 " в гриву тебя ебал ", " в ротик тебя имею шлюшка ", " поимел тебя под фонк ",
                 " под накротиками тебя имел ", " под пивасом тебя имел ", " под пивандеполой тебя имею ",
                 " под диваном тебя имел ", " под кроваткой тебя имел ", " пол одеялом тебя трахал тайно ",
                 " как ниндзя тебе в очко закидал свой хуесюрикен ", " в отсосе ты остался лошара сук ",
                 " пососи мои яйца щенок ты сук) ", " слыш меня клоун ебал я тебя в нос твой красный ",
                 " слыш блять хуесоска я тебя в рот ебал лалку ", " твою мамашу милфу на секс раскрутил прикинь",
                 " пизду твоей мамаши раскрутил ", " натянул твою мать как стрелу на тетеву нах ",
                 " твою мать натягивал на свой хуй пока не заметил что она уже труп ",
                 " пока твоя мать сосала я пил пиво ", " пахатлива сасешь", " трахнул мать те"," раньше твою мать в три щели ебали теперь она хочет больше не можем отказать этой шалаве и зовем толпы на ее пизду", " членом тебе мамашу ебал",
                 " в бане парился и твою мать ебал там же ",
                 "обоссали тебя щенок ебаный хе-хе ", " че ты мне сосешь дура ебаная ",
                 " обоссал тебя хуйло лошара ебаная ", " сру тебе на рожу чмо ебаное ",
                 " да ты уже в отсосе телочка ебаная", " твяо мать мой хуй любит что пиздец",
                 " твяо мать мою залупу сосет", " гидроцефал ты ",
                 " выебал тя ", " я раскромсал еблище твоей полугнилой матери",
                 " слыш ты шелуха ебаная метнулся отсюда кабанчиком нахуй ",
                 " че говна сожрал выкидыш беременной селёдки",
                 " еще че то скажи сюда сын говна и всю оставшуюся жизнь ты будешь передвигаться рывками",
                 " ле твоесть я твою мать ебал внатуре да ",
                 " ты не понял но я твою мать ебал",
                 " да я тебе в общем то буду давать по ебалу ",
                 " ты типо как пешка мой хуй сосал да ",
                 " твою мать ебал",
                 " сосал ты ",
                 " Я твою мать своим хуем затопил нахуй крысу обордажную",
                 " Я внатуре те щас на ебало на су социоблядина ебаная ару",
                 " Ты мой хуй будешь сосать пока у тебя кровь из носа не пойдет",
                 " Ты внатуре же мой хуй сосал без права на ошибку",
                 " Ты мой хуй на кануне ебал своим ртом",
                 " Я твою мать обоссал конкретно так хе",
                 " Бычкуеш мой хуй лярва ебаная ару",
                 " Сосеш ты мне со слезами на глазах ",
                 " Твою мать членам торжашу",
                 " Сосеш ты мне ответсвенно ",
                 " Я твою мать об свой хуй на залупу бросил ",
                 " Я твою мать ебал со скуки",
                 " От разлуки ты мне хуй сосал же ару",
                 " Твою мать ебал по пути",
                 " Сосеш ты мне как нужный кому то блять ару",
                 " Ты мой хуй сосал приторна ",
                 " Я твою мать ебал за гаражами сука децел ты ебаный ",
                 " Хуй соси мне потом ной блядина сука конченная",
                 " Внатуре те глазенки членам вытащил сука",
                 " Твою мать об свой хуй ударял при каждой встрече",
                 " соси",
                 " твоей мамаше ебало перережу сынок шлюхи ебучий а ну иди сюда по ебалу получать будешь хе-хе",
                 " маманю твою ебал сынок шлюхи хе-хе не поверишь как ебал даже !",
                 " усоси",
                 " засосешь",
                 " Ебал я твою мать так то ты сынок шлюхи хе",
                 " Твою мать на свой хуй посадил внатуре",
                 " Ты блять хуй сосеш ",
                 " твою мать я ебал же",
                 " отососи тут переломок ебаный", " я твою мать здесь ебу безмолвно ",
                 " ебу твою мать она молчит и терпит как губка", " впитываешь мою сперму как губка ебаная",
                 " сосешь мне как будто тебе это надо с рождения", " слыш лошара ебаная ну ты всосе",
                 " ару кончебляд ебаный ты че всасываешь ", " я твою мать здесь подвешу за крюк и выебу ее в пузо",
                 " я твою мать здесь буду трахать до потери пульса",
                 " буду твою мать ебать пока все человечество не вымрет",
                 " буду твою мать ебать до того момента пока время не отматается до эры динозавров ",
                 " ебал твою мать пока ты сосал мои яйца ты абсосок ебаный  бля ",
                 " я твою мать здесь ебу даже когда все смотрят она не стесняется",
                 " ебем твою мать в рот она тут ноет ",
                 " ебу тебя тут в рот как кобылу ебаную", " ебем тебя в рот как ебаного укурка",
                 " ебем тебя в рот бычок ебаный", " ты педик дешевый нахуй всосал мне ",
                 " я рот твоей мамаши на свой хуй натянул как презик и выебал тебя",
                 " ты когда родился я тебя как презик на свой хуй натянул и ебал твою мать ",
                 " когда твоя мать мне хуй сосала она влюбилась в мой пенис",
                 " мой хуй наебал твою мать на секс она его любила", " ебем твою мать во всех позах",
                 " ебу тебя как огузка ебаного", " ебу тебя кабанчиком", " ты здесь разве что мне хуй сосать намерен",
                 " ты тут разве что хуй сосать мне будешь постоянно", " отсосешь ты мне как нибудь по преколу",
                 " ты давай там не умирай я ж твою мать ебал", "слыш курва ебаная ты нахуй сдыхаешь тут",
                 " я твою мать ебал пока ты спал в колыбельной дегенерат сука",
                 " ебу твою мать атрофированную на голову ебанутую мразь", " ебу твою мать под кроватью ",
                 " ебу тебя под лсд", " ебу тебя под трапом", " идешь на мой хуй как овца на убой",
                 " ты на прибой моего хуя идешь телочка ебаная", " ты на мой хуй как корабль на маяк реагируешь",
                 " ты сразу на мой хуй кидаешься как будто на жрачку", " бомжиха не расслабляйся я твою мать ебу",
                 " ебеним тебя в рот такого олигофрена ебаного",
                 " слыш олигофрен ебаный я твою мать ебеню по всем фронтам",
                 " олигофрен я тебя в рот ебал ", " распилил твою мать на доске",
                 " встань на колени сынок шлюхи и соси",
                 " на помойке твою мать на видео ебал когда ей было 12",
                 " я твоей мамаше распятие в жопу засунул она вопила как свинья, а я ее глотку говном заткнул",
                 " в твою дохлую мать я засунул страпон в виде арматуры",
                 " я твою мать здесь заставил подыхать у моих ног",
                 " твоя мать мои ногти лижет как шлюха ебаная", " я твои гниющие кости резал залупой",
                 " я твою мать здесь выебал в ее гнилой таз", " твои губы гноем залепил и хуем прибил",
                 " зубы тебе ломом нахуй вырвал", " ты плебей ебаный я в твоем брюхе червей развожу как блядей",
                 " насилую твою мать шлюху", " твоя семья это толпа ебучих имбицилов",
                 " я твою мать зарыл среди каменных скрежалей",
                 " твоя мать после себя оставила лишь пару капель на кинжале", " я в пизду твоей мамаши нож вставил",
                 " слышишь фрик я твою мать ебал", " под ребром у тебя мой хуй застрял ", " рушу твою мать хуем своим ",
                 " рождай себе подобных чтобы я продолжал эту блядскую бойню инфернального транса",
                 " заставляю твою семью танцевать со мной смертельный танец как будто вы стадо баранов",
                 " голову твоей мамаши уронил на пику", " осквернил твой обглоданный труп",
                 " разложившееся мясо твоей мамаши ебал на крышке гроба твоего отца", " ебу твою мать шлюху в рот",
                 " на костях твоей мамаши построил себе дом",
                 " кости твоей мамаши друг о друга заточил теперь буду резать тебя свинья ебаная",
                 " я подтолкну к тебе солнце и сожгу тебя нахуй", " ебу гниющий труп твоей мамаши",
                 " крики твоей мамаши среди пыточных инструментов заводит мой хуй на убойную атаку в ее ебальник",
                 " изуродованную твою мать ебал", " почерневший скелет твоей мамаши ебал",
                 " выкопал выродка твоей мамаши из ее пизды , отрезал ему голову и засунул ей в пизду",
                 " до отказа забиваю твое горло говном", "выкидываю требуху твоей мамаши тебе в ебало",
                 " ебу твою мать как обычно среди темного покрова", " гниющее ебало твоей мамаши ебал",
                 " твой разум окутал своим членом",
                 " Хуем те зубы нахуй сломал шалаве такой",
                 " Сасеш ты мне в почет",
                 " Сасеш ты мне хуйня безпризорная",
                 " Я твою мать ебирую шалаву хе",
                 " Сосеш ты мне блядина ебаная",
                 " Твою мать хуем тратил",
                 " Сасеш ты мне присядчиво",
                 " Су те в ебало гандону ебаному ару",
                 " Чистично мой хуй сосеш ты сынок шлюхорванки",
                 " Я внатуре те кляп хуем в рот засунул пигмей ты ебаный",
                 " Я твою мать буду ебать пока вечер не наступит блядина сука ",
                 " Я твою мать разпидарасю нахуй блядину же",
                 " Ты мой хуй сосеш примитивно",
                 " Сасеш ты мне как надо",
                 " Ебашу те хуем по кадыку шалаве",
                 " Гримирую тя хуйом ",
                 " За цепил твою мать на своем хуе аж взрыв произашел ару",
                 " Хуйца ты моего соснул и сразу понял что это ахуительный экстази",
                 " Нет вот ты сасеш и все тут",
                 " Я твою мать внатуре хуем динамил",
                 " Ты сосеш мне всяческе когда есть возможность",
                 " Я твою мать натуре хуем нашпигаю фаршимачку ебаную",
                 " Бля твоя мать под моим хуем же щас прогибаеться как ебаная блядина иди нахуй её уберай от моего полового органа кхе",
                 " Твою мать внатуре на хуй натяну ебаный ты гандон сука",
                 " Сасеш ты мне провально",
                 " Сасеш ты мне хорошо же",
                 " Сасеш ты мне как надобно"
                 " Твою мать ебу слыш ты чудак ебаный ару",
                 " Хуйца моего сосни лучше блядина конченая",
                 " Я твою мать ебал опарыш ты ебаный сука ару",
                 " Сосни моего хуйца блядоеб сука",
                 " Внатуре твою мать на своем хуе похороню как и весь твой провальный троллинг мде",
                 " Я в твою мать свой хуй тыкаю так то блять",
                 " Я те залупой нахуй прокручу против часовой стрелки ты блять обоссаная ару",
                 " Ты мой хуй своими губами бороздил моряк ебаный сука ахах",
                 " Хуем те по бороде проводил внатуре ахах",
                 " Сосеш ты мне по бланту блядина ссаная",
                 " Я твою мать на свой хуй насадил как ебаную снасть на удочку кхе",
                 " Ты сасеш как то не правильно",
                 " Я твою мать обоссал же внатуре",
                 " Хуя ты моего сосал приблеженно",
                 " Я твою мать внатуре хуем на арбиту пятьдесят два отправил ",
                 " Хуй ты мой сосал и точка на этом",
                 " Я твою мать внатуре на свой хуй по сажу, будет как ебаный часовой сука в бинокль зырить искать мою залупу кхе",
                 " Хуем тя рашу", " хуем тебя ебарирую отрубень ебаный", " стервятник ебаный тебе клюв сломал хуем",
                 " Падарочна тя ебу", " маман твою ебашировал в пакистане "," сасеш как нравственный"," сасешь на секунды", " ровно по траектории  сасеш",
                 " ебарировал твою семейку своим истребительским хуем ",
                 " Сасешь новогодняя",
                 " Сцу те в кишок",
                 " Хуем тя глаголел",
                 " Абидна сасешь",
                 " Публична тя ебу",
                 " Хуем тя выкурел",
                 " Низка сасешь",
                 " Ебу тя паливна ужи",
                 " Хуем тя давел",
                 " Песду те хуем паметел",
                 " Сасешь спокойна",
                 " Ебу тя в деревущке",
                 " Песту те хуем тушил",
                 " Франтальна тя ебу",
                 " Как в старину сасешь",
                 " Хуем тя атцепил",
                 " Сасешь предурковата",
                 " Велика тя ебу",
                 " Жопоблядский еблигад ты сука", " Гнидомудый глуходрыщ сосни", " Скотожирный кривокрыл хуй слови",
                 " Сракосучий гнидотряс хуем тя убью", " ебу твою мать она мне хуй сосет бля дура ",
                 " а ты мой хуй взаместо соски сосал же ", " помню я как твою мать яйцами придавил",
                 " помню твою мать ебал задротку", " помню твою мать ебал на свалке", " помню твою мать ебал в пезду",
                 " помню твою жирную мать ебал свинью", " помню твою мать ебал блядуху",
                 " помню твою мать ебал еще молодую", " помню твою мать шестерку ебал ",
                 " помню как твою мать шлюху ебал в рот ", " помню твою мать ебал невидимую",
                 " помню твою мать ебал в гробу", " помню тебе в рот срал ", " помню тебе на клык кинул ",
                 " помню ты сосал мне ", " помню как тебя шлюху в туалете клуба ебал",
                 " помню как ебал тебя в рот в уличном туалете ", " помню как в думе тебя ебал ",
                 " помню как ебал тебя у мэрии", " помню как ебал тебя у белого дома",
                 " помню как ебал тебя у амфитеатра ", " помню как ебал тебя у музея ", " помню как ебал тебя у тюрьмы",
                 " помню как ебал тебя у парковки ", " помню как ебал тебя у ЖД вокззала",
                 " помню как ебал тебя на рельсах", "помню как ебал тебя у твоей мамы", " помню как ебал тебя на диване",
                 " помню как ебал тебя у подъезда ", " помню как ебал тебя у самолета",
                 " помню как ебал тебя у душевой кабинки", " помню как ебал тебя тапочками ",
                 " помню как ебал тебя у лесной опушки", "помню как ебал тебя у класса",
                 " помню как ебал тебя у аудитории ", "помню как ебал тебя у учительской",
                 " помню как ебал тебя у деконата ", " помню как ебал тебя у садика ",
                 " помню как ебал тебя у парковки на втором этаже ", "помню как ебал тебя у лифта",
                 " помню как ебал тебя у бара ", " помню как ебал тебя у стойла на диком западе ",
                 " помню ебал тебя у витрины", " помню как ебал тебя у банкомата",
                 " помню как ебал тебя у полицейского участка", " помню как ебал тебя у военной части",
                 " помню как ебал тебя у военкомата", " помню как ебал тебя меж ребер",
                 " помню ебал тебя на силе воли ", " помню ебал тебя через душу ", " помню ебал тебя в душе ",
                 " помню ебал тебя у канавы", " помню ебал тебя безприрывно ",
                 " а ты своим языком мне в колокола бил как в церкви ", " помню твою мать ебал у церкви ",
                 " помню твою мать ебал у посольства ", " помню твою мать освежал хуем ", " помню твою мать рвал хуем ",
                 " помню твою мать ебал по сути ", " помню морально твою мать ебал  ",
                 " помню что твою мать ебал дика ", " помню что твоя мать шлюха ебаная мне сосала каждый день в школе ",
                 " помню твою мать ебал в школьном туалете ", " помню твою мать ебал у курилки ",
                 " помню ебал твою мать у пивнушки ", " помню твою мать ебал за магазом ",
                 " помню твою мать ебал у трубного завода ", " помню твою мать ебал у лестницы ",
                 " помню твою мать ебал у дерева ", " помню твою мать ебал у окна",
                 " помню твою мать ебал постоянно в рот ", " помню твою мать ебал у унитаза ",
                 " помню твою мать ебал у плиты ", " помню твою мать ебал у раковины ",
                 " помню твою мать ебал у ванны ", " помню твою мать ебал у комода ",
                 " помню твою мать ебал у тумбочки ", " помню твою мать ебал у капота",
                 " помню твою мать ебал у вейп-шопа", "помню твою мать ебал у секс-шопа",
                 " помню твою мать ебал у космитического магазина", " помню твою мать ебал перед табачкой",
                 " Ноги те абасцал слехка",
                 " Пабедна тя ебу",
                 " Хуем тя кантузел",
                 " Сасешь с престижам",
                 " В тя сцу",
                 " Найсава сасешь чота",
                 " Сасешь с боку",
                 " Хех песту твою хуем задел",
                 " Сасешь чотна",
                 " Просветлил тя хуем",
                 " Великалепна сасешь",
                 " Хуем тя переставел",
                 " Без чести тя ебу",
                 " Хуем тя закалол",
                 " Сасешь имунитетна",
                 " Хуем тя трогал",
                 " Безработна сасешь",
                 " В вальере тя ебу",
                 " Хуем тя праагрил",
                 " Сцу те в уха", " маман твоя блядина мне сосала прикались",
                 " Павадна тя ебу",
                 " Хуем тя усилел",
                 " Хуем тя выпрямил",
                 " Хуем тя вывез",
                 " Паминутна тя ебу",
                 " Проститутшна сасешь",
                 " Выплатна тя ебу",
                 " Сасешь депазитна",
                 " Перевез тя хуем",
                 " В печенку те сцу",
                 " Хуем тя агрю сча",
                 " Убил тя хуем",
                 " Сасешь пад трап",
                 " Хуем тя выправадил",
                 " Стопудова сасешь",
                 " Хуем тя прапил",
                 " За пачку тя ипу",
                 " Хуем тя кастриравал",
                 " Тонка сасешь",
                 " Ебу тя пад напряжением",
                 " Хуем тя в космас отправел",
                 " Закрутел тя в хуе",
                 " Нинармативна сасешь",
                 " Хуем тя выставел",
                 " Сасешь па степендии",
                 " Ебу тя за деплом",
                 " Вспомнел тя хуем",
                 " На силеволе тя ебу",
                 " Хуем на тя рухнул",
                 " Заебата сасешь",
                 " Хуем тя удобрил",
                 " Дарожна тя ебу",
                 " Па прежнему сасешь",
                 " Ебу тя пад вадой",
                 " Хуем тя убел",
                 " По хую тя водел",
                 " Хуем тя качал",
                 " Специфична сасешь",
                 " Кайфова тя па ебал",
                 " Сильна трахаю тя",
                 " Сасешь пад лсд",
                 " Хуем тя выправадил",
                 " Па навагоднему тя ебу",
                 " Скользка тя ебу",
                 " В ноздре те сцу",
                 " Массова тя хуем ебу",
                 " Как чемпион сасешь",
                 " Мирна тя абасцал",
                 " Легальна тя ебу",
                 " Сасешь как диггер",
                 " Как консомольская сасешь",
                 "  Ебу тя как временную",
                 " Хуем в те путишетсвовал",
                 " Отлична тя ебу",
                 " Саверна сасешь", " я тебе в рот насру хуесосище слабоневрозное ",
                 " я твою мать ебал внатуре хуедлинительная блядушинка",
                 " Хуем тя отпездел", " пиздапёрка ебаная я же твою мамашу в рот ебал пока ты мои яйца хавал ",
                 " хуй лови сынок шлюхи странного семейства олигофренов ",
                 " Сасешь как старпер", " в рот тебя ебал мразота ссаная ты отсоси там шлюшенькая ебунячая",
                 " маман я твою мать пиздаголовая тварь",
                 " Бля буду тя ебу", " ты блять шлюха ебаная ", " клюквосранище свое закрой мразинина ебаная ",
                 " Ебу тя насильна", " хуем тебя аннигилировал шлюха терпиливая отсоси грю",
                 " Буквальна сасешь", " хуем тебя тормошил шлюха ебучая ", " сосни здесь хуеплетище ссаное ебаное хаха ",
                 " а так твоя мать то реально тут мне в яйца прыгала языком "," я тебе на клык дам пидорас", " нахуй ты прячешься свою мать от хуя моего" ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)