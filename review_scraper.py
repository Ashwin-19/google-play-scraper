from google_play_scraper import app, Sort, reviews
from urllib.error import HTTPError

import math
import time
import random
import json
import os.path
from os import path

BATCH_SIZE = 200 # MAX IS 200
PATH = '' #add save path here @Ayushi/Pooja

class App:
    
    def __init__(self, title: str, app_id: int):
        self.title = title
        self.app_id = app_id


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
            self.app_data = app(self.app_id, lang='en', country='us')
            return self.app_data
        except HTTPError as error:
            if error.code == 404:
                return error.code
            else:
                time.sleep(random.randint(1,3))
                return self.get_app_data()
                

    def get_all_reviews(self):
        
        total_reviews = self.app_data["reviews"]
        print("Total Reviews:", total_reviews)
        
        iterations = math.ceil(total_reviews/BATCH_SIZE)
        _continuation_token = None

        review_data = []
        review_ids = []
        batches = 0

        for i in range(iterations):

            try:
                review_batch, _continuation_token = reviews(
                    self.app_id,
                    lang='en',            
                    country='us',         
                    sort=Sort.NEWEST,     
                    count=200,
                    continuation_token=_continuation_token
                )

                old = len(review_ids)
                for rvw in review_batch:
                    review_ids.append(rvw['reviewId'])

                review_data.extend(review_batch)

                review_ids = list(set(review_ids))
                new = len(review_ids)

                if old == new:
                    '''
                        change criteria
                    '''
                    pass

                batches += 1

                if batches%20 == 0:
                    print(f'Completed: {len(review_ids)}/{total_reviews}')
                    print(f'Batch: {batches}/{iterations}')
            
            except Exception as E:
                time.sleep(random.randint(1,3))
        
        print(f'Finished Collection: {len(review_data)}/{total_reviews}')
        
        return review_data


if __name__=='__main__':
    '''
    replace with code to iterate through all apps
    '''
    app_id = 'org.coursera.android'
    title = 'Coursera'

    print(f'Collecting data for {title}')

    application = App(title, app_id)
    app_data = application.get_app_data()
    # if app_data == 404:
    #   continue
    # application.save_app_data()
    review_data = application.get_all_reviews()
    # application.save_review_data()