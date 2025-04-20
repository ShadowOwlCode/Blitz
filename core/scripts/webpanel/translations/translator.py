import os
import json

# TODO: Improve memory usage
__translation_cache = {}

TRANSLATION_DIRECTORY = './translations'
__current_lang = 'en'


def set_language(lang: str):
    global __current_lang
    __current_lang = lang


def get_language() -> str:
    return __current_lang


def load_translations(lang):
    if lang in __translation_cache:
        return __translation_cache[lang]

    file_path = os.path.join(TRANSLATION_DIRECTORY, f'{lang}.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)
            __translation_cache[lang] = translations
            return translations
    except FileNotFoundError:
        raise ValueError(f'Translation file for \'{lang}\' not found.')
    except json.JSONDecodeError:
        raise ValueError(f'Invalid JSON in translation file for \'{lang}\'.')


def translate(key: str, lang: str = __current_lang) -> str:
    translations = load_translations(lang)
    return translations.get(key, f'[missing:{key}]')
