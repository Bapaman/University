import pymorphy2
import string
from translate import Translator

morph = pymorphy2.MorphAnalyzer()
translator = Translator(from_lang='ru', to_lang='en')

with open('dialog.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
    words = text_without_punctuation.split()

    word_counts = {}

    for word in words:
        normalized_word = morph.parse(word)[0].normal_form
        translate_word = translator.translate(normalized_word)  # Переводим нормализованное слово

        if (normalized_word, translate_word) in word_counts:
            word_counts[(normalized_word, translate_word)] += 1
        else:
            word_counts[(normalized_word, translate_word)] = 1

# Сортируем словарь по количеству повторений в обратном порядке
sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

with open('result_table.txt', 'w', encoding='utf-8') as result_file:
    result_file.write("Исходное слово | Перевод | Количество повторений\n")
    for (word, translation), count in sorted_word_counts:
        result_file.write(f"{word} | {translation} | {count}\n")

print("Таблица успешно создана и сохранена в файл 'result_table.txt'")
