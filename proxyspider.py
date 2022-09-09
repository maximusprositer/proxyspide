import os


def MAIN():
    try:
        import requests
        import random
        import datetime
        import sys
        import re
        import time
        import datetime
        import json
        import threading
        from threading import Thread
        from colorama import Fore, Back, Style
        from random import randint
        def Main():
            global phone
            global info
            global proxy
            global proxies

            r = Fore.RED
            g = Fore.GREEN
            y = Fore.YELLOW
            s = Style.RESET_ALL

            def mask(str, maska):
                if len(str) == maska.count('#'):
                    str_list = list(str)
                    for i in str_list:
                        maska = maska.replace("#", i, 1)
                    return maska
                    except:
                        pass
                except:
                    pass

            def clear():
                os.system('cls' if os.name == 'nt' else 'clear')

            def checkver():
                global info
                ver = '90'
                version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
                if int(ver) < int(version):
                    info = Back.RED + "\nВерсия устарела и нуждается в обновлении!" + Style.RESET_ALL
            
            def updateproxy():
                global proxy
                global info
                try:
                    print("Введите proxy в формате ip:port.")
                    print("Пример: " + Fore.GREEN + "123.45.6.78:8080" + Style.RESET_ALL)
                    print("Для отмены нажмите Ctrl+C")
                    proxy = input(Fore.BLUE + "spymer > " + Style.RESET_ALL)
                    if proxy == "":
                        info = Fore.RED + "\nНекорректно введены данные!" + Style.RESET_ALL
                        proxy = "localhost"
                    else:
                        print("Проверяю прокси...")
                        ip = requests.get("http://fsystem88.ru/ip", verify=False, timeout=10).text
                        try:
                            ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(proxy),
                                                                                  'https': "http://{}".format(proxy)},
                                               verify=False, timeout=10).text
                        except:
                            ipx = ip
                        if ip != ipx:
                            info = Fore.GREEN + "Proxy рабочий." + Style.RESET_ALL
                        else:
                            print(Fore.RED + "{} не работает. Введите новый!".format(proxy) + Style.RESET_ALL)
                            updateproxy()
                except:
                    info = Fore.RED + "\nНекорректно введены данные!" + Style.RESET_ALL
                    proxy = "localhost"

            def generateproxy():
                global proxy
                global info

                print(
                    Fore.YELLOW + "Подождите генерируем рабочий прокси.\nОбычно это занимает не больше 30 секунд..." + Style.RESET_ALL)
                url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=RU"
                req = requests.get(url)
                ip = requests.get("http://fsystem88.ru/ip").text
                array = req.text.split()
                open("proxies.txt", "w+").close()
                for prox in array:
                    thread_list = []
                    t = threading.Thread(target=checkproxy, args=(ip, prox))
                    thread_list.append(t)
                    t.start()
                time.sleep(20)
                f = open("proxies.txt")
                proxies = f.read().split()
                proxy = random.choice(proxies)
                info = Fore.GREEN + "Рабочий прокси успешно найден!" + Style.RESET_ALL

            def checkproxy(ip, prox):
                try:
                    ipx = requests.get("http://fsystem88.ru/ip",
                                       proxies={'http': "http://{}".format(prox), 'https': "http://{}".format(prox)},
                                       verify=False, timeout=10).text
                except:
                    ipx = ip
                if ip != ipx:
                    f = open("proxies.txt", "a+")
                    f.write("{}\n".format(prox))
                    f.close()

            def make7phone():
                global phone
                if phone[0] == '+':
                    phone = phone[1:]
                elif phone[0] == '8':
                    phone = '7' + phone[1:]
                elif phone[0] == '9':
                    phone = '7' + phone

            def addparams():
                global name
                global password
                global email
                name = ''
                for x in range(12):
                    name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                    password = name + random.choice(
                        list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
                    email = "{}@gmail.com".format(name)

            def onesend():
                global phone
                global name
                global password
                global email
                global proxy
                global info
                global proxies
                                clear()
                                logo()
                                print(info)
                                if proxy == "localhost":
                                    proxies = None
                                else:
                                    proxies = {'http': "http://{}".format(proxy), 'https': "http://{}".format(proxy)}
                                while iteration < count:
                                    addparams()
                                    sms()
                                    iteration += 1
                                    print("{} круг пройден.".format(iteration))
                                info = Fore.BLUE + "\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone,
                                                                                                      iteration) + Style.RESET_ALL
                        except:
                            info = Fore.RED + "Неверно введено кол-во кругов" + Style.RESET_ALL
                except:
                    info = Fore.RED + "Неверно введен номер телефона" + Style.RESET_ALL
                    
            def n_send(phone, count, proxies):
                global name
                global password
                global email
                global info
                iteration = 0
                while iteration < count:
                    addparams()
                    sms()
                    iteration += 1
                    print(Fore.GREEN + "{}".format(phone) + Style.RESET_ALL + ": круг №{} пройден.".format(iteration))
                print(Fore.GREEN + "\nСпам на {} закончен. Кол-во кругов {}".format(phone, count) + Style.RESET_ALL)
                exit()

            def main():
                global phone
                global info
                global proxy

                global proxies
                proxy = "localhost"
                info = " "
                while True:
                    clear()
                    logo()
                    print(info)
                    checkver()
                    print("Proxy: " + Fore.BLUE + "{}".format(proxy) + Style.RESET_ALL)
                    if proxy == "localhost":
                        print(Fore.YELLOW + "Советую использовать прокси !!!" + Style.RESET_ALL)
                    print("1) Обновить прокси.")
                    input1 = input(Fore.BLUE + "Введите номер пункта: " + Style.RESET_ALL)
                    if input1 == "1":
                        clear()
                        logo()
                        print(info)
                        print("Выберите один вариант:")
                        print("1. Запустить спамер на один номер")
                        print("2. Выгрузить номера из TXT файла ")
                        print("3. Выгрузить номера по токену")
                        input11 = input(Fore.BLUE + "spymer > " + Style.RESET_ALL)
                        if input11 == "1":
                            onesend()

                        elif input11 == "2":
                            filesend()

                        elif input11 == "3":
                            tokensend()
                        else:
                            print("Некорректно")

                    elif input1 == "2":
                        print("1. Удалить прокси")
                        print("2. Ввести свой прокси")
                        print("3. Сгенерировать прокси")
                        input51 = input(Fore.BLUE + "spymer > " + Style.RESET_ALL)
                        if input51 == "1":
                            proxy = "localhost"

                        elif input51 == "2":
                            updateproxy()

                        elif input51 == "3":
                            generateproxy()

                    elif input1 == "3":
                        update()

                    elif input1 == "4":
                        print(Fore.BLUE + "\nДо скорой встречи!)\n" + Style.RESET_ALL)
                        exit()

            main()

        Main()
    except ModuleNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Нажмите Enter чтобы установить недостающие библиотеки...")
        input()
        os.system("python -m pip install requests colorama")

        MAIN()


MAIN()