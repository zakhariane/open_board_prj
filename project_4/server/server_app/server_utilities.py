
import random

from .db_manager import TableManager

# def get_results_of_search(wanted_word):
#
#     table_manager = TableManager()  # create table_manager object
#
#     table_manager.create_connection()
#     table_manager.create_cursor()
#
#     results = table_manager.find_string_usage_in_subtitles(wanted_word)
#
#     table_manager.close_connection()
#
#     # если результатов нет, возвращаем 0 и это обрабатывается графическим интерфейсом
#     if results == None:
#         return 0
#
#     # получаем 5 случайных результатов
#
#     random.shuffle(results)
#
#     num = min(5, len(results))
#
#     results = results[:num]
#
#     rows = []
#     for row in results:
#
#         link = row[1]
#         startTime = str( int(row[5] / 1000) )
#         endTime = str( int(startTime) + int(row[2] / 1000) )
#         frase = row[3]
#
#         rows.append([link, startTime, endTime, frase])
#
#     return rows

logged_addresses = {}
messages = []

def logged_in(address):
    return (address in logged_addresses.keys())

def login(address, public, private):
    # TODO поля не пустые, проверить существует ли такой публичный ключ, если да то правильный ли пароль, если нет до зарегистрировать его . если пароль не правильный то сказать что попутал пароль, если правильный и пароль то войти на его страницу
    logged_addresses[address] = {"public": public, "private": private}
    print(logged_addresses)

def logout(address):
    del logged_addresses[address]

def save_message(address, message):
    messages.append(message)
    print((address, message))

def find_user(address, user_name):
    print((address, user_name))
    if user_name == "tree_for_peace":
        return True
    else:
        return False

def get_username_by_addr(address):
    return logged_addresses[address]["public"]

def get_messages_by_addr(address):
    return messages

def get_messages_by_username(user_name):
    if user_name == "tree_for_peace":
        return ["solnce", "vzoshlos", "skoro", "https://mlcourse.ai/book/topic09/topic9_part1_time_series_python.html", "https://www.sciencedirect.com/science/article/pii/S2352484721001219"]
    else:
        return messages
