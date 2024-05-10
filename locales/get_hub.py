from fluentogram import TranslatorHub, FluentTranslator
from fluent_compiler.bundle import FluentBundle

from os import listdir
from os.path import join


def get_languages(directory: str) -> dict[str, str]:
    """Returns a dict of language codes and paths to the files"""

    return {
        lang.split('.')[0]:
        join(directory, lang)
        for lang in listdir(directory)
    }


def get_translators(languages: dict[str, str]) -> list[FluentBundle]:
    """
    Returns a list of the FluentBundle from a dict value
    where a key is a language code and a value is path to this
    language.ftl file
    """

    translators = []
    for code, path in languages.items():
        translators.append(
            FluentTranslator(code,
                             translator=FluentBundle.from_files(code, [path]))
            )

    return translators


def get_locales_map(languages: dict[str, str],
                    default: str = 'en') -> dict[str, str]:
    """Returns a dict of map locales"""

    return {
        code:
        ((code, default) if code != default else (code,))
        for code in languages.keys()
        }


def get_hub(directory: str, default: str = 'en') -> TranslatorHub:
    """Returns a TranslatorHub object from a directory with locale files"""

    languages = get_languages(directory)
    return TranslatorHub(
        locales_map=get_locales_map(languages, default),
        translators=get_translators(languages),
        root_locale=default
    )
