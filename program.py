import random
# print(5)
# print(5+5)
# print("hello")
# print("hello" +       " world")
# создали первую переменную и назвали её number, чтобы хранить введенное число
# name = "Вася"
# print("Hello " + name)



# randint - random integer - случайное целое
secret_number = random.randint(1, 10)

print("Компьютер загадал число. Попробуйте его отгадать.")

attempts = 3

# while - до тех пор пока 
while attempts > 0:
    print("Количество попыток: " + str (attempts))
    number = input("Введите число: ")
    # превращаем строку в число при помощи команды int
    number = int(number)

    if number > secret_number:
        print("Секретное число меньше")
    if number < secret_number:
        print("Секретное число больше")
    if number == secret_number:
        print("Вы угадали")
        break

    attempts = attempts - 1
    if attempts == 0:
        print("Вы проиграли")
        print("Секретное число: " + str(secret_number))
