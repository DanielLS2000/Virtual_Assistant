import wikipedia

wikipedia.set_lang('pt')
def wiki_search(search_term):
    search_result = wikipedia.search(search_term, results=1)
    print(search_result)
    print(wikipedia.summary(search_result))

wiki_search("Barack")