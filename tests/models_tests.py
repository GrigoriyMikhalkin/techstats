import pymongo

from models import Techs


connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)


class TestTechsModel():

    def setup_method(self, method):
        self.db = connection.test
        self.techs = Techs(self.db)
        self.record = {
            'name': "test",
            'related_techs': ['test related']
        }
        records = [self.record]
        self.records_ids = self.techs.insert_records(records)

    def teardown_method(self, method):
        connection.drop_database(self.db)

    def test_insert_valid(self):
        assert self.db.techs.count() == 1
        assert self.db.techs.find_one(self.record)

    def test_insert_invalid(self):
        pass

    def test_get_by_methods(self):
        res = self.techs.get_by_name(self.record['name'])
        assert res.count() == 1

        res = self.techs.get_by_related_techs(self.record['related_techs'])
        assert res.count() == 1
