from googletrans import Translator
from google_trans_new import google_translator


def LanguageConversionGT(content):
    translatorGT = Translator()
    return (translatorGT.translate(content)).text


def LanguageConversionGTN(content):
    translatorGTN = google_translator()
    return translatorGTN.translate(content, lang_tgt='en')


def ArticleConversion(nepali_article):
    array = nepali_article.split(" ।")
    print(array)
    english_article = ""
    for arr in array:
        if len(arr) > 0:
            english_article = english_article + LanguageConversionGTN(arr + "।")
    return english_article

print(ArticleConversion("""मेरो नाम अर्पण हो ।  म नेपाली हु ।"""))