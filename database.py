import sqlite3

# создать коннект и назвать игру
bd = sqlite3.connect('2048.sqlite')
# Создать курсор
cur = bd.cursor()

cur.execute('''
create table if not exists RECORDS(
    name text,
    score integer
)''')

# Ссоздали запрос, который групирует по имени, распологает по значению с
# большего к наименьшему и выводит 3 лучших результата

def get_best():
    cur.execute('''
    SELECT name gamer, max(score) score FROM RECORDS
    GROUP by name
    ORDER by score DESC
    LIMIT 3''')
    return cur.fetchall()

# # достать из таблицы все значения
# result = cur.fetchall()
# print(result)
print(get_best())











