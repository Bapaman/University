import re
import urllib.request
import csv
import ssl

# Создаем SSLContext с отключенной проверкой сертификата
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Открываем URL с использованием SSLContext
adr_request = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/", context=ssl_context).read().decode()

pattern = r"(?:class=\"org-widget-header__title-link\">)(?P<name>.+)(?:<)(?:[^+]+)(?:location\">\s+)(?P<adr>.+)(?:[^+]+)(?P<phone>[^<]+)(?:<)(?:[^А-я]+)(?:.+[^А-я]+)(?P<time>.+)(?:<)"

match = re.findall(pattern, adr_request)

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Название", "Адрес", "Телефон", "Часы работы"])

    for i in match:
        writer.writerow(i)
    print("Данные сохранены")
