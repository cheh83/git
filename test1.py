import os
from filmsawardsdata import films_awards
## Крок 3
# (Є прихований код) Для кожного фільму створіть новий список, він має зберігати словники з
# ключем award_name та його значенням, ключем award та його значенням, ключем type та його
# значенням. Приклад,

# [{'type': 'Nominee',
# 'award_name': 'Oscar',
# 'award': 'Best Achievement in Makeup'},
# {'type': 'Nominee',
# 'award_name': 'Oscar',
# 'award': 'Best Achievement in Makeup'}
# ]



# найдем название и колличество фильмов
# for i in films_awards:
#     print(i['results'][0]['movie']['title'])
#  Harry Potter and the Deathly Hallows: Part 2
# Harry Potter and the Sorcerer's Stone
# Harry Potter and the Deathly Hallows: Part 1
# Harry Potter and the Prisoner of Azkaban
# Harry Potter and the Half-Blood Prince
# Harry Potter and the Chamber of Secrets
# Harry Potter and the Goblet of Fire
# Harry Potter and the Order of the Phoenix

Harry_Potter_and_the_Deathly_Hallows_Part_2 = []
Harry_Potter_and_the_Sorcerers_Stone = []
Harry_Potter_and_the_Deathly_Hallows_Part1 = []
Harry_Potter_and_the_Prisoner_of_Azkaban = []
Harry_Potter_and_the_Half_Blood_Prince = []
Harry_Potter_and_the_Chamber_of_Secrets = []
Harry_Potter_and_the_Goblet_of_Fire = []
Harry_Potter_and_the_Order_of_the_Phoenix = []

for i in films_awards[0]['results']:
    Harry_Potter_and_the_Deathly_Hallows_Part_2.append(dict([('type', i['type']), ('award_name', i['award_name']), ('award', i['award'])]))
    #print(Harry_Potter_and_the_Deathly_Hallows_Part_2)

for j in films_awards[1]['results']:
    Harry_Potter_and_the_Sorcerers_Stone.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Sorcerers_Stone)

for j in films_awards[2]['results']:
    Harry_Potter_and_the_Deathly_Hallows_Part1.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Deathly_Hallows_Part1)

for j in films_awards[3]['results']:
    Harry_Potter_and_the_Prisoner_of_Azkaban.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Prisoner_of_Azkaban)

for j in films_awards[4]['results']:
    Harry_Potter_and_the_Half_Blood_Prince.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Half_Blood_Prince)

for j in films_awards[5]['results']:
    Harry_Potter_and_the_Chamber_of_Secrets.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Chamber_of_Secrets)

for j in films_awards[6]['results']:
    Harry_Potter_and_the_Goblet_of_Fire.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Goblet_of_Fire)

for j in films_awards[7]['results']:
    Harry_Potter_and_the_Order_of_the_Phoenix.append(dict([('type', j['type']), ('award_name', j['award_name']), ('award', j['award'])]))
    #print(Harry_Potter_and_the_Order_of_the_Phoenix)

#  Крок 4
# Відсортуйте кожен список з нагородами за алфавітом по ключу award_name.
# Використай sorted та lambda функції.

film1_sorted = sorted(Harry_Potter_and_the_Deathly_Hallows_Part_2, key=lambda x: x['award_name'])
print('Harry_Potter_and_the_Deathly_Hallows_Part_2:', film1_sorted)

film2_sorted = sorted(Harry_Potter_and_the_Sorcerers_Stone, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Sorcerers_Stone:', film2_sorted)

film3_sorted = sorted(Harry_Potter_and_the_Deathly_Hallows_Part1, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Deathly_Hallows_Part1:', film3_sorted)

film4_sorted = sorted(Harry_Potter_and_the_Prisoner_of_Azkaban, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Prisoner_of_Azkaban:', film4_sorted)

film5_sorted = sorted(Harry_Potter_and_the_Half_Blood_Prince, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Half_Blood_Prince:', film5_sorted)

film6_sorted = sorted(Harry_Potter_and_the_Chamber_of_Secrets, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Chamber_of_Secrets:', film6_sorted)

film7_sorted = sorted(Harry_Potter_and_the_Goblet_of_Fire, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Goblet_of_Fire:', film7_sorted)

film8_sorted = sorted(Harry_Potter_and_the_Order_of_the_Phoenix, key=lambda x: x['award_name'])
#print('Harry_Potter_and_the_Order_of_the_Phoenix:', film8_sorted)

#  Крок 5
# Для кожного фільму у теках з літерами від A до Z створи txt файл з назвою (ключ award_name)
# нагороди яка починаєтья на відповідну літеру.
# Приклад:
# Дерикторія фільму: Harry Potter and the Order of the Phoenix
# Дерикторія з назвою V
# Файл VES Award
# path1 = r'C:\project new\Harry Potter\Harry Potter and the Chamber of Secrets'
# os.chdir(path1)
# print(os.getcwd())
# for i in film1_sorted:
#     path11 = os.path.join(path1, i['award_name'][0])
#     os.chdir(path11)
#     print(os.getcwd())
#     file1 = open(f'{i["award_name"]}.txt', "w+")
#     file1.close()


# path2 = r'C:\project new\Harry Potter\Harry Potter and the Deathly Hallows  Part 1'
# os.chdir(path2)
# print(os.getcwd())
# for i in film2_sorted:
#     path22 = os.path.join(path2, i['award_name'][0])
#     print(path22)
#     os.chdir(path22)
#     print(os.getcwd())
#     file2 = open(f'{i["award_name"]}.txt', "w+")
#     file2.close()

# path3 = r'C:\project new\Harry Potter\Harry Potter and the Deathly Hallows  Part 2'
# os.chdir(path3)
# print(os.getcwd())
# for i in film3_sorted:
#     path33 = os.path.join(path3, i['award_name'][0])
#     print(path33)
#     os.chdir(path33)
#     print(os.getcwd())
#     file3 = open(f'{i["award_name"]}.txt', "w+")
#     file3.close()

# path4 = r'C:\project new\Harry Potter\Harry Potter and the Goblet of Fire'
# os.chdir(path4)
# print(os.getcwd())
# for i in film4_sorted:
#     path44 = os.path.join(path4, i['award_name'][0])
#     print(path44)
#     os.chdir(path44)
#     print(os.getcwd())
#     file4 = open(f'{i["award_name"]}.txt', "w+")
#     file4.close()

# path5 = r'C:\project new\Harry Potter\Harry Potter and the Half-Blood Prince'
# os.chdir(path5)
# print(os.getcwd())
# for i in film5_sorted:
#     path55 = os.path.join(path5, i['award_name'][0])
#     print(path55)
#     os.chdir(path55)
#     print(os.getcwd())
#     file5 = open(f'{i["award_name"]}.txt', "w+")
#     file5.close()

# path6 = r'C:\project new\Harry Potter\Harry Potter and the Order of the Phoenix'
# os.chdir(path6)
# print(os.getcwd())
# for i in film6_sorted:
#     path66 = os.path.join(path6, i['award_name'][0])
#     print(path66)
#     os.chdir(path66)
#     print(os.getcwd())
#     file6 = open(f'{i["award_name"]}.txt', "w+")
#     file6.close()

# path7 = r'C:\project new\Harry Potter\Harry Potter and the Prisoner of Azkaban'
# os.chdir(path7)
# print(os.getcwd())
# for i in film7_sorted:
#     path77 = os.path.join(path7, i['award_name'][0])
#     print(path77)
#     os.chdir(path77)
#     print(os.getcwd())
#     file7 = open(f'{i["award_name"]}.txt', "w+")
#     file7.close()
#
# path8 = r"C:\project new\Harry Potter\Harry Potter and the Sorcerer's Stone"
# os.chdir(path8)
# print(os.getcwd())
# for i in film8_sorted:
#     path88 = os.path.join(path8, i['award_name'][0])
#     print(path88)
#     os.chdir(path88)
#     print(os.getcwd())
#     file8 = open(f'{i["award_name"]}.txt', "w+")
#     file8.close()

#  Крок 6
# У файл з ім'ям кожної нагороди перенеси всі назви номінацій цієї(award) нагороди. Приклад
# Файл VES Award:
# Outstanding Special Effects in a Motion Picture
# Outstanding Visual Effects in an Effects Driven Motion Picture
# Outstanding Compositing in a Feature Motion Picture

path1 = r'C:\project new\Harry Potter\Harry Potter and the Chamber of Secrets'
os.chdir(path1)
print(os.getcwd())
# for i in film1_sorted:
#     print(i['award'][0])
    # file1 = open(f'{i["award_name"]}.txt', "w+")
    # file1.close()
