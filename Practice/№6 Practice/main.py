import re

input_filename = 'journal.txt'
output_filename = 'result.txt'

pattern = r'Рейс (\d+) (прибыл из|отправился в) (\D+) в (\d{2}:\d{2}:\d{2})'

with open(input_filename, 'r', encoding='utf-8') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
    data = infile.read()
    matches = re.findall(pattern, data)
    for match in matches:
        direction = "в" if match[1] == "отправился в" else "из"
        result_line = f'[{match[3]}] - Поезд № {match[0]} {direction} {match[2]}\n'
        outfile.write(result_line)
