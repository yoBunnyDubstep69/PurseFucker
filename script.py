import re
import urllib.parse
import os
import time
import platform
import subprocess
file_path = ".list.txt"

def find_all_characters_between(row, start_char, end_char):
    """Ищет текст между заданными символами."""
    pattern = re.escape(start_char) + r'(.*?)' + re.escape(end_char)
    return re.findall(pattern, row)

def remove_links(text):
    """Удаляет ссылки из текста."""
    return re.sub(r'http[s]?://\S+|www\.\S+', '', text)

def create_search_query(text):
    """Создает поисковый запрос для Google."""
    base_url = "https://www.google.com/search?q="
    query = urllib.parse.quote(text)  # Кодируем текст для URL
    return f"{base_url}{query}"

def launch_browser(search_query):
	for br in range(3):
		if platform.system() == "Windows":
			subprocess.Popen(['msedge', search_query], creationflags=subprocess.CREATE_NO_WINDOW)
			# Для Edge на Windows
			time.sleep(1)
			# Задержка 1 секунда
		else:
			subprocess.Popen(['firefox', search_query], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			# Для Firefox на Linux
			time.sleep(1)
			# Задержка 1 секунда
			return()

with open(file_path, 'r', encoding='utf-8') as file:
    for row in file:
        row = row.strip()  # Убираем лишние пробелы и символы новой строки
        
        # Ищем текст между '«' и '»'
        results_angle = find_all_characters_between(row, '«', '»')
        if results_angle:  # Если найдены результаты
            for result in results_angle:
                cleaned_result = remove_links(result)  # Удаляем ссылки
                if cleaned_result:  # Проверяем, не пустой ли результат
                    #print(cleaned_result)  # Выводим каждый найденный текст
                    search_query = create_search_query(cleaned_result)  # Создаем поисковый запрос
                    launch_browser(search_query)
                    
        # Ищем текст между '"' и '"'
        results_quotes = find_all_characters_between(row, '"', '"')
        if results_quotes:  # Если найдены результаты
            for result in results_quotes:
                cleaned_result = remove_links(result)  # Удаляем ссылки
                if cleaned_result:  # Проверяем, не пустой ли результат
                    #print(cleaned_result)  # Выводим каждый найденный текст
                    search_query = create_search_query(cleaned_result)  # Создаем поисковый запрос
                    launch_browser(search_query)
