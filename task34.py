# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его 
# стихах ритм. Поскольку разобраться в его кричалках не настолько
# просто, насколько легко он их придумывает, Вам стоит написать 
# программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке
glas=('у','е','ы','а','о','э','я','и','ю')
STIX=input('Введите ваше парам: ')
STIX=(STIX.split( ))
a=0
a1=len(list(filter(lambda x: x in glas, STIX[0])))
def Check(STIX):
 for i in range(len(STIX)):
  a=len(list(filter(lambda x: x in glas, STIX[i])))==a1
  if not a:
          print(("Пам парам") )
          break
 else: print("Парам пам-пам")

Check(STIX)      



