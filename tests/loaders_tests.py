import mock

from models.loaders import TechLoader


class TestTechLoader():

    def setup_method(self, method):
        self.loader = TechLoader()
        self.start_date = ''
        self.end_date = ''

    def test_load_vacancies(self):
        tech = {}
        vacancies = self.loader.load_vacancies(tech)

        assert vacancies
