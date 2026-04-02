import asyncio.staggered
from os import replace

s = "Umar Kamalov"
s2 = "строка.метод"
print(s2.upper())
print(s2.lower())
print(s.lower()) #с маленькими
print(s.upper()) #с заглавными. Они не меняют буквы, а по сути возвращают новые объекты, которые уже записаны в памяти яп. Но если мы напишем:
print(s) # ответ будет "Umar" - вернется первый вариант.
print(s.count("a"))
q1 = "metod kount chitaet kolichestvo bukv"
print(q1.count("о", 4)) #метод .count считает все буквы, количество тех или иных букв мы указываем сами
print(q1.count("о", 0, 7))
print(q1.lower().upper().count("О", 0, 45))
print(q1.find("a", 2, 30)) #.find() возвращает индекс (порядковый номер) первого вхождения символа или подстроки, которую ищем.
print(q1.replace("O", "F"))
print(q1.replace(" ", "").isalpha())
q2 = "123456789."
print(q2.replace(".","").isdigit())
q3 = "1234"
q4 = "1234567"
q5 = "1234567891011"
print(q3.rjust(8,"+"))
print(q4.rjust(8,"+"))
print(q5.rjust(8,"+"))
print(q3.ljust(9,"="))
print(q4.ljust(9,"="))
print(q5.ljust(9, "="))

w = "Kamalov- Umar-Mamatsalievich"
name, surname, lastname = w.replace(" ", "").split("-")
print(name)
print(surname)
print(lastname)
w1 = "12 231 // 3213 313213 444 345/ 345=3"
print(w1.replace("//","").replace("/","").replace("=","").replace(" ","").split(","))
w2 = ["str, float, bool"]
print(",".join(w2))
w3 = "      aaa aaaa bvbbbb bb      "
print(w3.strip())
print(w3.rstrip())
print(w3.lstrip())


# s = "Umar Kamalov"
# res = s.count("a") + s.count("r")
# print(res)
# a = "Поdsf sfdfh sld fhsldf sldfh ;s lhd;f ishfsldhif solihdf ;slihd fs;olhdf s; olihdf lskdhdkfls khn"
# print(a.count("s"))
# print(a.count(" "))
# m = "Я изучаю авто на языке программирования п"
# print(m.find("я"))
# x = "Umar Kamalov"
# print(x.replace("m", "i", 2))
# print(x.replace(" ","").isalpha())
# print("UmarKamalov".isalpha())
# e = "1223131"
# print(e.isdigit())
# # o = "2313"
# # p = "31241421"
# # i = "3423545467485"
# # print(o.rjust(13))
# # print(p.rjust(13))
# # print(i.rjust(10))
# o = "2313"
# p = "31241421"
# i = "3423545467485"
# u = len (o)
# print(o.rjust(u)) #rjust и ljust — работают как линейка в текстовом редакторе
# print(p.ljust(u)) #rjust выравнивает элементы справа, а ljust слева.
# print(i.ljust(u))
# y = "Камалов Умар Маматсалиевич"
# name, lastname, sa = y.split(" ")
# print(name)
# print(lastname)
# print(sa)