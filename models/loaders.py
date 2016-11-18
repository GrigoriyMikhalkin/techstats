import json
import requests


class BaseLoader():
    api = ''
    query = {}

    def get_techs():
        pass

    def load(self, date_from=None, date_to=None):
        search_text = 'python'
        # '+'.join([tech['name']] + tech['related_techs'])
        search_query = self.query.copy()
        search_query['text'] = search_text
        search_query['date_from'] = date_from
        search_query['date_to'] = date_to

        response = requests.get(
            self.api,
            params=search_query
        )

        return response


class VacanciesLoader(BaseLoader):
    api = 'https://api.hh.ru/vacancies'
    query = {
        'text': '',
        'search_field': 'description',
        'date_from': '',
        'date_to': ''
    }


class ResumesLoader(BaseLoader):
    api = 'https://api.hh.ru/resumes'
    query = {}


class StatsCalculator():
    pass
