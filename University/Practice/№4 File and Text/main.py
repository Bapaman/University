import re

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        unique_words = sorted(set(words))
        return unique_words

def save_file(file_name, words_list):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f'Всего уникальных слов: {len(words_list)}\n')
        file.write(f'='*30)
        for word in words_list:
            file.write('\n' + word)
words = read_file('data.txt')
save_file('count.txt', words)
