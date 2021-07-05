from review_scraper import App
import json


if __name__=='__main__':
    '''
    iterating through Appids from json file
    '''
    f = open('AppIds.json',)
    data = json.load(f)

    for i in range(len(data)):

        app_id = data[i]["mediaId"]
        title = ""

        application = App(title, app_id)
        app_data = application.get_app_data()
        # if app_data == 404:
        #   continue
        application.save_app_data()
