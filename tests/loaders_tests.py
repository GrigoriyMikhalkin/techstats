# import mock

from models.loaders import VacanciesLoader, ResumesLoader, StatsCalculator


class TestVacanciesLoader():

    def setup_method(self, method):
        self.loader = VacanciesLoader()
        self.date_from = None
        self.date_to = None

    def test_load_vacancies(self):
        tech = {}
        vacancies = self.loader.load()

        assert vacancies
