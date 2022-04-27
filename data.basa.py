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

# Group- объеденяет  по имени. Order рапологает в правильном порядке по
# возрастанию и Desc - c большего с меньшему.
# Score 2 раз пишшем ,что бы имя колонки не наз. max(score)
cur.execute('''
SELECT name gamer, max(score) score FROM RECORDS
GROUP by name
ORDER by score DESC
LIMIT 3''')

# достать из таблицы все значения
result = cur.fetchall()
print(result)
cur.close()










