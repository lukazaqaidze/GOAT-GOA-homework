# ```2) კომენტარების სახით ახსენით რა არის boolean მონაცემთა ტიპი, რა მნიშვნელობები შეიძლება შეიძინოს და როდის რომელს ვღებულობთ?

# 3) კომენტარების სახით ახსენით რა არის binary code და როგორ მუშაობს, რას უდრის 1 და 0?

# 4) კომენტარების სახით ახსენით რა არის bool() ფუნქცია და რა შედეგს გვაძლევს?

# 5) შექმენით ორი ცვლადი a და b, მიაწერეთ მათ მნიშვნელობები და დაბეჭდე მათი თანასწორობა (a == b).

# 6) მომხმარებელს შეიყვანენეთ ორი რიცხვი და შეადარეთ, რომელი უფრო დიდია.

# 7) მომხმარებელს შემოაყვანინეთ სიტყვა, შეამოწმეთ მკადრად უდრის თუ არა მომხმარებლის შეყვანილი სიტყვა "Python"-ს.

# 8) მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ მეტია თუ არა იგი 100-ზე.

# 9) მომხმარებელს შემოაყვანინეთ პაროლი, მკაცრად შეამოწმეთ უდრის თუ არა მომხმარებლის შეყვანილი პაროლი "Python123"-ის.

# 10) მომხმარებელს შემოაყვანინეთ ორი რიცხვი -->
# 👉 შეადარეთ თუ პირველი რიცხვი მეტია მეორეზე
# 👉 შეადარეთ თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე
# 👉 შეადარეთ თუ პირველი რიცხვი უდრის მეორე რიცხვს

# 11) მომხმარებელს შემოატანინეთ 5 string ტიპის მნიშვნელობა, შენი დავალებაა მოახდინო მათი კონკატინაცია.

# 12) მომხმარებელს შემოატანინე 4 რიცხვი, შენი დავალებაა გაიგო ამ რიცხვების საშუალო არითმეტიკული.

# 13) შექმენი 4 ცვლადი,ამ ცვლადებში შეინახე 4 განსხვავებული მონაცემთა ტიპის ელემენტები და დაპრინტე მათ ტიპი (გამოიყენეთ შესაბამისი ფუნქცია)

# 14) შექმენი 2 ცვლადი,შეინახე ორივე ცვლადში string ტიპის მნიშვნელობები დაშეადარე ისინი არიან თუ არა ერთნაირები

# 15) შექმენი 4 ცვლადი, სადაც გექნება მოთავსებული რიცხვები ოღონდ სტრინგის სახით მაგ: "40", გადაიყვანე ეს სტრინგი რიცხვები ინტეჯერში(გამოიყენე შესაბამისი ფუნქცია) და გაიგე ამ ოთხი რიცხვის ჯამი.

# 16) შექმენი 3 ცვლადი,ამ ცვლადებში შეინახეთ ინტეჯერ ტიპის მონაცემები, შენი დავალებაა ეს რიცხვები გადაიყვანო integer მონაცემთა ტიპში და გამოიტანო ეს რიცხვები ერთ წინადადებაში. მაგ: 304050
# ```


# boolean არის ერთ ერთი მონაცემთა ტიპი 5 სხვადასხვა ტიპებისგან. მას აქვს მარტო 2 მნიშვნელობა რომლებიც არია-ნ True და False და როდესაც პირობა სრულდება ჩვენ ვღებულობთ True-ს და რუდესაც მოცემული პირობა არ სრულდება ვღებულობთ False-ს

# ბინარული კოდი (ორობითი კოდი) არის ინფორმაციის წარმოდგენის სისტემა, რომელიც იყენებს მხოლოდ ორ ციფრს: 0-ს და 1-ს.სადაც 1 ნიშნავს ჩართულს ხოლო 0 გამორთულს

# bool() aris კონვერტაცია რომელიც სხვა ტიპის მონაცემთა ტიპებს boolean ტიპებად აქცევს

# a = "koko"
# b = "kako"
# print(a == b)

# num1 = int(input("enter your number:"))
# num2 = int(input("enter your number:"))
# if num1 > num2:
#     print(num1)
# elif num2 > num1:
#     print(num2)
# else:
#     print("the numbers are equal == ")

# password = input("enter your pass-word:")
# if password == "python":
#     print(True)
# else:
#     print(False)

# num3 = int(input("enter your number:"))
# if num3 > 100:
#     print(True)
# elif num3 < 100:
#     print(False)
# else:
#     print("the numbers are equal == ")

# password = input("enter your pass-word:")
# if password == "python":
#     print(True)
# else:
#     print(False)

# num1 = int(input("enter your number:"))
# num2 = int(input("enter your number:"))
# if num1 > num2:
#     print("num1 > num2")
# elif num2 > num1:
#     print('num2 > num1')
# else:
#     print("the numbers are equal == ")

# password1 = input("enter your pass-word:")
# password2 = input("enter your pass-word:")
# password3 = input("enter your pass-word:")
# password4 = input("enter your pass-word:")
# password5 = input("enter your pass-word:")

# print(bool(password1))
# print(bool(password2))
# print(bool(password3))
# print(bool(password4))
# print(bool(password4))
# print(bool(password5))


# num1 = int(input("enter your number:"))
# num2 = int(input("enter your number:"))
# num11 = int(input("enter your number:"))
# num22 = int(input("enter your number:"))
# print((num1+num2+num11+num22)//4)

# strr = "index"
# intt = 6
# bulioni = False
# floativi = 4.4

# print(type(strr))
# print(type(intt))
# print(type(bulioni))
# print(type(floativi))


# wrd1 = "gia"
# wrd2 = "bob"
# if wrd1 == wrd2:
#     print(True)
# else:
#     print(False)

# num1 = "1"
# num2 = "2"
# num3 = "3"
# num4 = "4"

# print(int(num1))
# print(int(num2))
# print(int(num3))
# print(int(num4))

# num1 = "1"
# num2 = "2"
# num3 = "3"
#  num4 = "4"
# print(num1+num2+num3+num4)