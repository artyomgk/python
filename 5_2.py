# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

# Подсчет строк в файле
with open("text_1.txt", encoding='utf-8') as f_obj:
    count = 0
    for line in f_obj:
        count = count + 1
    print(f"Количество строк в файле: {count}")

# Подсчет слов в файле
file = open("text_1.txt")
data = file.read()
print(f"Количество слов в файле: {len(data.split())}")
file.close()