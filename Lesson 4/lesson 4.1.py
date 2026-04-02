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
