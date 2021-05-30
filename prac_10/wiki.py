"""
CP1404/CP5632 Practical
Wikipedia API
"""

import wikipedia

page_title = input('Enter page title: ')
while page_title != "":
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    page_title = input('Enter page title: ')
