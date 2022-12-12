import webbrowser
from pathlib import Path

# Выбор браузера. Для указания своего необходимо ввести путь.
def browser():
    webbrowser.register('Yandex', None, webbrowser.BackgroundBrowser(str(Path.home() / 'AppData\Local\Yandex\YandexBrowser\Application\\browser.exe')))
    browser = webbrowser.get('Yandex')
    return browser