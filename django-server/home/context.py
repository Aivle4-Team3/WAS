from config.settings import BASE_DIR
from lecture.models import Lecture


def context_processor(request):
    dir = BASE_DIR / 'static/common/lifeQuotes.txt'

    with open(dir, 'r', encoding='utf-8') as f:
        lifeQuotes = f.readlines()

    reg_subjects = Lecture.objects.values_list('subject', flat=True).distinct()

    return {
        'phrase_list': lifeQuotes,
        'reg_subjects': reg_subjects,
    }
