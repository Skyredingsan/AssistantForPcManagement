from base_function import talk
from links_commands import url, app
import sys
from base_config import browser
from subprocess import call


# Анализирует слова и если есть подходящее, то выполняет.
def makeSomething(quest):
    if quest in url.keys():
        talk("Уже открываю")
        browser().open_new_tab(url[quest])
    elif quest in app.keys():
        talk('Open')
        call(app[quest])
    elif 'стоп' in quest:
        talk("Да, конечно, без проблем")
        sys.exit()
