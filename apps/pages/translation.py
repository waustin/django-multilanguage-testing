from modeltranslation.translator import translator, TranslationOptions
from .models import Page


class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'head_title', 'meta_description')

translator.register(Page, PageTranslationOptions)
