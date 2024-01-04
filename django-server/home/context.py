from config.settings import BASE_DIR


def context_processor(request):
    dir = BASE_DIR / 'static/common/lifeQuotes.txt'

    with open(dir, 'r', encoding='utf-8') as f:
        lifeQuotes = f.readlines()

    return {
        'phrase_list': lifeQuotes
    }
