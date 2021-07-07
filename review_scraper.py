from google_play_scraper import app, Sort, reviews, reviews_all
from urllib.error import HTTPError

import math
import time
import random
import json
import os.path
from os import path

BATCH_SIZE = 200 # MAX IS 200
METADATA_PATH = './metadata/' #add save path here @Ayushi/Pooja
REVIEWS_PATH = './reviews/' #add save path here @Ayushi/Pooja

languages = [
    ('aa', 'Afar'),
    ('ab', 'Abkhazian'),
    ('af', 'Afrikaans'),
    ('ak', 'Akan'),
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('an', 'Aragonese'),
    ('hy', 'Armenian'),
    ('as', 'Assamese'),
    ('av', 'Avaric'),
    ('ae', 'Avestan'),
    ('ay', 'Aymara'),
    ('az', 'Azerbaijani'),
    ('ba', 'Bashkir'),
    ('bm', 'Bambara'),
    ('eu', 'Basque'),
    ('be', 'Belarusian'),
    ('bn', 'Bengali'),
    ('bh', 'Bihari languages'),
    ('bi', 'Bislama'),
    ('bo', 'Tibetan'),
    ('bs', 'Bosnian'),
    ('br', 'Breton'),
    ('bg', 'Bulgarian'),
    ('my', 'Burmese'),
    ('ca', 'Catalan; Valencian'),
    ('cs', 'Czech'),
    ('ch', 'Chamorro'),
    ('ce', 'Chechen'),
    ('zh', 'Chinese'),
    ('cu', 'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic'),
    ('cv', 'Chuvash'),
    ('kw', 'Cornish'),
    ('co', 'Corsican'),
    ('cr', 'Cree'),
    ('cy', 'Welsh'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('dv', 'Divehi; Dhivehi; Maldivian'),
    ('nl', 'Dutch; Flemish'),
    ('dz', 'Dzongkha'),
    ('el', 'Greek, Modern (1453-)'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('eu', 'Basque'),
    ('ee', 'Ewe'),
    ('fo', 'Faroese'),
    ('fa', 'Persian'),
    ('fj', 'Fijian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('fy', 'Western Frisian'),
    ('ff', 'Fulah'),
    ('Ga', 'Georgian'),
    ('de', 'German'),
    ('gd', 'Gaelic; Scottish Gaelic'),
    ('ga', 'Irish'),
    ('gl', 'Galician'),
    ('gv', 'Manx'),
    ('el', 'Greek, Modern (1453-)'),
    ('gn', 'Guarani'),
    ('gu', 'Gujarati'),
    ('ht', 'Haitian; Haitian Creole'),
    ('ha', 'Hausa'),
    ('he', 'Hebrew'),
    ('hz', 'Herero'),
    ('hi', 'Hindi'),
    ('ho', 'Hiri Motu'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('hy', 'Armenian'),
    ('ig', 'Igbo'),
    ('is', 'Icelandic'),
    ('io', 'Ido'),
    ('ii', 'Sichuan Yi; Nuosu'),
    ('iu', 'Inuktitut'),
    ('ie', 'Interlingue; Occidental'),
    ('ia', 'Interlingua (International Auxiliary Language Association)'),
    ('id', 'Indonesian'),
    ('ik', 'Inupiaq'),
    ('is', 'Icelandic'),
    ('it', 'Italian'),
    ('jv', 'Javanese'),
    ('ja', 'Japanese'),
    ('kl', 'Kalaallisut; Greenlandic'),
    ('kn', 'Kannada'),
    ('ks', 'Kashmiri'),
    ('ka', 'Georgian'),
    ('kr', 'Kanuri'),
    ('kk', 'Kazakh'),
    ('km', 'Central Khmer'),
    ('ki', 'Kikuyu; Gikuyu'),
    ('rw', 'Kinyarwanda'),
    ('ky', 'Kirghiz; Kyrgyz'),
    ('kv', 'Komi'),
    ('kg', 'Kongo'),
    ('ko', 'Korean'),
    ('kj', 'Kuanyama; Kwanyama'),
    ('ku', 'Kurdish'),
    ('lo', 'Lao'),
    ('la', 'Latin'),
    ('lv', 'Latvian'),
    ('li', 'Limburgan; Limburger; Limburgish'),
    ('ln', 'Lingala'),
    ('lt', 'Lithuanian'),
    ('lb', 'Luxembourgish; Letzeburgesch'),
    ('lu', 'Luba-Katanga'),
    ('lg', 'Ganda'),
    ('mk', 'Macedonian'),
    ('mh', 'Marshallese'),
    ('ml', 'Malayalam'),
    ('mi', 'Maori'),
    ('mr', 'Marathi'),
    ('ms', 'Malay'),
    ('Mi', 'Micmac'),
    ('mk', 'Macedonian'),
    ('mg', 'Malagasy'),
    ('mt', 'Maltese'),
    ('mn', 'Mongolian'),
    ('mi', 'Maori'),
    ('ms', 'Malay'),
    ('my', 'Burmese'),
    ('na', 'Nauru'),
    ('nv', 'Navajo; Navaho'),
    ('nr', 'Ndebele, South; South Ndebele'),
    ('nd', 'Ndebele, North; North Ndebele'),
    ('ng', 'Ndonga'),
    ('ne', 'Nepali'),
    ('nl', 'Dutch; Flemish'),
    ('nn', 'Norwegian Nynorsk; Nynorsk, Norwegian'),
    ('nb', 'Bokmål, Norwegian; Norwegian Bokmål'),
    ('no', 'Norwegian'),
    ('oc', 'Occitan (post 1500)'),
    ('oj', 'Ojibwa'),
    ('or', 'Oriya'),
    ('om', 'Oromo'),
    ('os', 'Ossetian; Ossetic'),
    ('pa', 'Panjabi; Punjabi'),
    ('fa', 'Persian'),
    ('pi', 'Pali'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('ps', 'Pushto; Pashto'),
    ('qu', 'Quechua'),
    ('rm', 'Romansh'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('ro', 'Romanian; Moldavian; Moldovan'),
    ('rn', 'Rundi'),
    ('ru', 'Russian'),
    ('sg', 'Sango'),
    ('sa', 'Sanskrit'),
    ('si', 'Sinhala; Sinhalese'),
    ('sk', 'Slovak'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('se', 'Northern Sami'),
    ('sm', 'Samoan'),
    ('sn', 'Shona'),
    ('sd', 'Sindhi'),
    ('so', 'Somali'),
    ('st', 'Sotho, Southern'),
    ('es', 'Spanish; Castilian'),
    ('sq', 'Albanian'),
    ('sc', 'Sardinian'),
    ('sr', 'Serbian'),
    ('ss', 'Swati'),
    ('su', 'Sundanese'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('ty', 'Tahitian'),
    ('ta', 'Tamil'),
    ('tt', 'Tatar'),
    ('te', 'Telugu'),
    ('tg', 'Tajik'),
    ('tl', 'Tagalog'),
    ('th', 'Thai'),
    ('bo', 'Tibetan'),
    ('ti', 'Tigrinya'),
    ('to', 'Tonga (Tonga Islands)'),
    ('tn', 'Tswana'),
    ('ts', 'Tsonga'),
    ('tk', 'Turkmen'),
    ('tr', 'Turkish'),
    ('tw', 'Twi'),
    ('ug', 'Uighur; Uyghur'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('ve', 'Venda'),
    ('vi', 'Vietnamese'),
    ('vo', 'Volapük'),
    ('cy', 'Welsh'),
    ('wa', 'Walloon'),
    ('wo', 'Wolof'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('yo', 'Yoruba'),
    ('za', 'Zhuang; Chuang'),
    ('zh', 'Chinese'),
    ('zu', 'Zulu')
]

class App:
    
    def __init__(self, title: str, app_id: int, language = "en", country = "us"):
        self.title = title
        self.app_id = app_id
        self.language = language
        self.country = country


    def save_reviews(self):
        '''
        add code to save reviews here @Ayushi/Pooja
        '''
        return


    def save_app_data(self):
        '''
        add code to save app data here @Ayushi/Pooja
        '''

        if path.exists('app_meta_details.json'):
            f = open('app_meta_details.json')
            data = json.load(f)
            # print(len(data))
            # print(type(data))
            data.append(self.app_data)

        else:
            data = []
            data.append(self.app_data)

        with open('app_meta_details.json', '+w') as json_file:
            json.dump(data, json_file, indent=2)
        
        return


    def get_app_data(self):
        try:
            self.app_data = app(self.app_id, lang=self.language, country=self.country)
            print("Scraping MetaData from country: " + self.country + " in language: " + self.language)
            return self.app_data
        except HTTPError as error:
            if error.code == 404:
                return error.code
            else:
                time.sleep(random.randint(1,3))
                return self.get_app_data()
                
    def get_all_reviews_at_once(self):

        total_reviews = self.app_data["reviews"]
        print("Total Reviews:", total_reviews)

        results = reviews_all(
            self.app_id,
            sleep_milliseconds=0, # defaults to 0
            lang='en', # defaults to 'en'
            country='us', # defaults to 'us'
            sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
            # filter_score_with=5 # defaults to None(means all score)
        )

        review_data = []
        review_ids = []

        for rvw in results:
            review_ids.append(rvw['reviewId'])
        
        review_ids = list(set(review_ids))

        print(f'Finished Collection: {len(review_ids)}/{total_reviews}')

        return
        

    def get_all_reviews(self,language="all"):
        
        total_reviews = self.app_data["reviews"]
        print("Total Reviews:", total_reviews)
        
        iterations = math.ceil(total_reviews/BATCH_SIZE)

        _continuation_token = None

        review_data = []
        review_ids = []
        batches = 0
        
        if language == "all":
            code_idx = 0
            language = self.language_codes[0]
            num_languages = len(self.language_codes) - 1
            print("Collecting reviews in all languages...")

        else:
            code_idx = 0
            num_languages = 0
            
        print("Collecting reviews in language: " + language)

        for i in range(iterations):

            try:
                review_batch, _continuation_token = reviews(
                    self.app_id,
                    lang=language,            
                    country=self.country,         
                    sort=Sort.NEWEST,     
                    count=BATCH_SIZE,
                    continuation_token=_continuation_token
                )

                old = len(review_ids)

                for rvw in review_batch:
                    review_ids.append(rvw['reviewId'])
                    # sourceFile = open('multilang_reviewids_coursera_2.txt', '+a')
                    # print(rvw['reviewId'], file = sourceFile)
                    # sourceFile.close()
                   
                review_data.extend(review_batch)

                review_ids = list(set(review_ids))
                new = len(review_ids)

                if old == new:
                    if code_idx < num_languages:
                        code_idx+=1
                        language = self.language_codes[code_idx]
                        print("Collecting reviews in language: " + language)
                        _continuation_token = None
                    else: break

                batches += 1

                if batches%20 == 0:
                    print(f'Completed: {len(review_ids)}/{total_reviews}')
                    print(f'Batch: {batches}/{iterations}')
            
            except Exception as E:
                time.sleep(random.randint(1,3))
        
        # print(f'Finished Collection: {len(review_data)}/{total_reviews}')
        print(f'Finished Collection: {len(review_ids)}/{total_reviews}')

        return review_data

    def get_language_codes(self):

        self.language_codes = []
        for i in range(len(languages)): self.language_codes.append(languages[i][0])

        # self.language_codes = ["en","hi","es","zh","pt","ru","ar","ja"]
        print(self.language_codes)

        return

if __name__=='__main__':
    '''
    replace with code to iterate through all apps
    '''
    
    # app_id = 'org.coursera.android'
    # title = 'Coursera'

    app_id = 'com.amazon.dee.app'
    title = 'Alexa'

    # app_id = 'com.instagram.android'
    # title = 'Instagram'

    print(f'Collecting data for {title}')

    application = App(title, app_id)
    application.get_language_codes()

    app_data = application.get_app_data()
    # print(app_data)
    # if app_data == 404:
    #   continue
    application.save_app_data()
    
    review_data = application.get_all_reviews()

    # application.save_review_data()