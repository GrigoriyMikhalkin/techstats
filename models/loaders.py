import json
import requests


class TechLoader():
    vacancies_api = 'https://api.hh.ru/vacancies'
    resumes_api = ''

    def load_vacancies(self, tech):
        query = {
            'text': '+'.join([tech['name']] + tech['related_techs']),
            'search_field': 'description',
            'start_date': '',
            'end_date': ''
        }

        response = requests.get(
            self.vacancies_api
        )

        vacancies = response
        return vacancies

    def load_resumes(self, tech):
        pass

    def load_data(self, start_date, end_date):
        """
        Loads data from hh.ru
        """
        techs = []
        self.start_date = start_date
        self.end_date = end_date

        for tech in techs:
            self.load_vacancies(tech)
            self.load_resumes(tech)
            # self.load_stats()

    def load_stats(self, period):
        """
        Loads stats calculated from data provided by hh.ru
        """
        pass
