""" Translator Function that englishToFrench , frenchToEnglish """
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#languages = language_translator.list_languages().get_result()
#print(json.dumps(languages, indent=2))

def englishToFrench(english_text):
    """ englishToFrench Function that translates English to French """
    if english_text=="":
        french_text=""
    else:
        translation_reponse = language_translator.translate(text=english_text, model_id="en-fr")
        translation = translation_reponse.get_result()
        french_text = translation['translations'][0]['translation']

    return french_text

def frenchToEnglish(french_text):
    """ englishToFrench Function that translates French to English """
    if french_text=="":
        english_text=""
    else:
        translation_reponse = language_translator.translate(text=french_text, model_id="fr-en")
        translation = translation_reponse.get_result()
        english_text = translation['translations'][0]['translation']

    return english_text

#print(englishToFrench("hello"))
#print(frenchToEnglish("Bonjour"))
