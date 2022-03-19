import time
import lviv_game

mapp = "\n\
                Оперний театр___!!!КРАКІВСЬКА!!!___Данила Галицького                                                \n\
                /                     |                 \           \n\
               /___Вірменська____площа Ринок_____        \          \n\
              /                 /                 \      академія   \n\
             /                 /                Руська   Друкарства \n\
        проспект свободи      /                     \        \      \n\
              \              /                        Підвальна     \n\
               \            /                              /        \n\
                \          /                              /         \n\
                 пам'ятник  _________ площа _____________/          \n\
            Данилу Галицькому        Соборна                        \n\
                                        |                           \n\
                                     Франка____Зелена               \n\
                                        |     /                     \n\
                                        |   Шота Руставелі          \n\
                                        |  /                        \n\
                                       /\                           \n\
                                      /  \                          \n\
                             Стрийська    Стрийський парк           \n\
                                      \  /                          \n\
                                       \/                           \n\
                                    !!!УКУ!!!"
#generating items
Map = lviv_game.Item("карта")
Fork = lviv_game.Item("срібна виделка")
Rose = lviv_game.Item("троянда")
Gift = lviv_game.Item("презент")

#generating characters
Kavaler = lviv_game.People("кавалер", "дозвольте вас провести кілька хвилин, сьогодні маєте гарний вигляд!")
Filolog= lviv_game.People("філолог", "можете пройти, тільки якщо скажете англійський алфавіт у зворотньому порядку!")
Lotr = lviv_game.Enemy("лотр", "хаха, тепер іди без карти! кожен сам винен, що тут проходить!",Map)
Zbuj = lviv_game.Enemy("збуй", "мені потрібна срібна виделка! якщо не даси, не пропущу!\n\
    як добре, що студент продав виделку, тепер можна пройти далі!", Fork)
Batiar = lviv_game.Friend("батяр", "хай, будь-які питання після прогулянки центром!", Rose)
Lajdak = lviv_game.People("лайдак", "ти тут не пройдеш! ця територія - моє місце для байдикування\n\
    Ой, лайдаки надзвичайно люблять говорити...це на довго, мабуть.")
Student1 =  lviv_game.Friend("студент", \
    "привіт, у мене є карта, вона допоможе тобі проходити квест!", Map)
Student2 = lviv_game.Friend("студент",\
    "раджу вам купити також срібну виделку у мене, пригодиться точно!", Fork)
Security = lviv_game.People("охорона", "я можу видати вам скарб лише за троянду!\n\
    чи маєте ви її?")

friends = [Student1, Student2, Batiar]
enemies = [Lotr, Zbuj]

#generating streets
UCU = lviv_game.Street("уку", {1:"Стрийський парк", 2:"Стрийська вулиця"})
Striyska = lviv_game.Street("Стрийська вулиця", {1:"УКУ", 2:"Шота Руставелі", 3:"вулиця Франка"})
Park = lviv_game.Street("Стрийський парк", {1:"Зелена", 2:"Франка", 3:"УКУ"})
Shota = lviv_game.Street("Шота Руставелі", {1:"Парк", 2:"Стрийська вулиця", 3:"Зелена"})
Zelena = lviv_game.Street("Зелена", {1:"Франка"})
Franka = lviv_game.Street("Франка", {1:"Стрийська вулиця", 2:"Стрийський парк",3:"Зелена", 4:"Соборна"})
Soborna = lviv_game.Street("Соборна площа",{1:"Франка",2:"Підвальна",3:"Пам'ятник Данилу Галицькому"})
Pidvalna = lviv_game.Street("Підвальна",{1:"Соборна", 2:"Руська", 3:"академія Друкарства"})
Memor_Danylo = lviv_game.Street("Пам'ятник Данилу Галицькому",{1:"Соборна", 2:"Галицька", 3:"проспект Свободи"})
Ruska = lviv_game.Street("Руська",{1:"площа Ринок", 2:"Підвальна"})
Drukarska = lviv_game.Street("академія Друкарства",{1:"Підвальна", 2:"Данила Галицького"})
Danyla = lviv_game.Street("Данила Галицького",{1:"академія Друкарства",2:"Краківська"})
Galytska= lviv_game.Street("Галицька",{1:"Пам'ятник Данилу Галицькому", 2:"площа Ринок"})
Svobody = lviv_game.Street("проспект Свободи",{1:"Пам'ятник Данилу Галицькому", 2:"Оперний театр", 3:"Вірменська"})
Virmenska = lviv_game.Street("Вірменська",{1:"площа Ринок", 2:"проспект Свободи"})
Opera = lviv_game.Street("Оперний театр",{1:"проспект Свободи", 2:"Краківська"})
Krakyvska = lviv_game.Street("Краківська",{1:"Оперний театр", 2:"площа Ринок", 3:"Данила Галицького"})
Rynok = lviv_game.Street("Площа Ринок",{1:"Краківська", 2:"Вірменська", 3:"Руська", 4:"Галицька"})

streets = {"УКУ":UCU,
"Стрийський парк":Park, "Стрийська вулиця":Striyska,
"Шота Руставелі":Shota, "Франка":Franka,
"Зелена":Zelena, "Соборна":Soborna,
"Підвальна":Pidvalna, "Пам'ятник Данилу Галицькому":Memor_Danylo,
"Руська":Ruska, "академія Друкарства":Drukarska,
"Данила Галицького":Danyla,"Галицька":Galytska,
"проспект Свободи":Svobody,"Вірменська":Virmenska,
"Оперний театр":Opera,"Краківська":Krakyvska,
"площа Ринок":Rynok
}

#filling streets with characters
UCU.set_character(Student1)
Zelena.set_character(Lajdak)
Drukarska.set_character(Lajdak)
Rynok.set_character(Batiar)
Park.set_character(Kavaler)
Danyla.set_character(Lotr)
Krakyvska.set_character(Student2)


#start game
dead = False
backpack = []
current_street = UCU

#one turn
while dead == False:
    
    print(current_street)
    print(f'вміст рюкзака: {[x.name for x in backpack]}')
    
    #зустріч з персонажами
    if current_street.character:
        print(f"\n---тут є {current_street.character.name}---")
        print(current_street.character)

        if current_street.character == Lajdak:
            for i in range(3):
                print("...\nдооосі говорить!")
                time.sleep(3)
            print("...\nо, він заснув! можна йти далі, але вже тепер тільки назад!")
            
        
        elif current_street.character == Batiar:
            print("oй, тепер доведеться пройтись з цим батярем, \n\
             добре, що він хоч красивий!")
            road = [Memor_Danylo, Svobody, Opera, Rynok]
            for i in range(4):
                print(road[i])
                print("...")
                time.sleep(3)
            print("o, як це мило, ви сподобались батяру, і він дарує вам троянду!")
        
        elif current_street.character == Filolog:
            alpha = ''
            alphabet = 'zyxwvutsrqponmlkjihgfedcba'
            while alpha != alphabet:
                alpha = input('>>> ')
                if alpha !=alphabet:
                    print("спробуйте ще! неосвідчені....понаїхали тут!")
            print("супер, проходьте далі!")
        if current_street.character in friends:
            backpack.append(current_street.character.take_item())
            print(f'вміст рюкзака: {[x.name for x in backpack]}')

        elif current_street.character in enemies:
            if current_street.character.weakness in backpack:
                backpack.remove(current_street.character.weakness)
        current_street.character = None    

    #проміжна точка зі скарбом
    if current_street == Krakyvska:
        if Gift in backpack:
            continue
        print("Ви дійшли до сховку! \n\
            тепер візьміть скарб, який потрібно принести до місця призначення,\n\
            та повертайтесь у колегіум!\n\
але скарб можна отримати лише за троянду, яку дарує батяр тільки найкрасивішим гравцям!")

        if Rose in backpack:
            print("ура, у вас уже є вона!\nзабирйте презент!")
            backpack.remove(Rose)
            backpack.append(Gift)
            Soborna.set_character(Zbuj)
            Rynok.set_character(Kavaler)
            Opera.set_character(Filolog)

        else:
            print("у вас такої ще нема\n\
             спробуйте зустріти батяра на площі Ринок!")

    #кінцева точка - виграш
    elif current_street == UCU and Gift in backpack:
        print("ВІТАЄМО, ВИ ПРОЙШЛИ ВИПРОБУВАННЯ!")
        dead = True
        continue

    print("\nвиберіть наступну вулицю (лише номер)\n\
        або введіть 5 щоб показати карту")
    counter1 = 0


    #карта
    ret = current_street.choose_next()
    if Map in backpack:
        if ret == 5:
            print(mapp)
        else:
            current_street = streets[ret]

    else:
        if ret == 5:
            print("у вас уже нема карти, її викрав лотр на вулиці Данила Галицького!")
        else:
            current_street = streets[ret]
