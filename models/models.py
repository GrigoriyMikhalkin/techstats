import datetime

from pymongo.collection import Collection

from db_settings import db
from .exceptions import WrongValueTypeException


class BaseCollection(Collection):
    COLLECTION_NAME = ''
    SCHEMA = {}

    def __init__(self, db=db, create=False):
        super().__init__(
            database=db,
            name=self.COLLECTION_NAME,
            create=create
        )
        self._gen_query_methods()

    def insert_records(self, records):
        # filter valid records
        valid_records = []
        for record in records:
            if all(
                    [
                        record.get(field[0]) and
                        isinstance(record[field[0]], field[1])
                        for field in self.SCHEMA.items()
                    ]
            ):
                valid_records.append(record)
        records_ids = self.insert_many(valid_records)
        return records_ids

    def get_by_id(self, value):
        pass

    def get_by_ids(self, values):
        pass

    def _gen_query_methods(self):
        """
        Dynamically generates query methods for collection
        """
        record_query_name = "get_by_{field}"
        records_query_name = "get_by_{field}s"

        for field in self.SCHEMA.keys():
            error_msg = "Value '{value}' for field '{field}'' has wrong " +\
                        "type: {actual_type} instead of {required_type}"

            def get_by_value(value, field=field):
                try:
                    if not isinstance(value, self.SCHEMA[field]):
                        raise WrongValueTypeException(
                            error_msg.format(
                                value=value,
                                field=field,
                                actual_type=type(value),
                                required_type=self.SCHEMA[field]
                            )
                        )
                    query = {field: value}
                    return self.find(query)
                except Exception:
                    return []

            def get_by_values(values, field=field):
                try:
                    for value in values:
                        if not isinstance(value, self.SCHEMA[field]):
                            raise WrongValueTypeException(
                                error_msg.format(
                                    value=value,
                                    field=field,
                                    actual_type=type(value),
                                    required_type=self.SCHEMA[field]
                                )
                            )
                    query = {field: {'$in': values}}
                    return self.find(query)
                except Exception:
                    return

            setattr(
                self, record_query_name.format(field=field), get_by_value
            )
            setattr(
                self, records_query_name.format(field=field), get_by_values
            )


class Techs(BaseCollection):

    COLLECTION_NAME = 'techs'
    SCHEMA = {
        'name': str,
        'related_techs': list
    }


class TechVacancies(BaseCollection):
    COLLECTION_NAME = 'techvacancies'
    SCHEMA = {
        'techs': list,
        'salary': int,
        'pub_date': datetime.datetime
    }


class TechResumes(BaseCollection):
    COLLECTION_NAME = 'techresumes'
    SCHEMA = {
        'techs': list,
        'salary': int,
        'pub_date': datetime.datetime
    }


class MonthlyTechStats(BaseCollection):
    COLLECTION_NAME = 'monthlytechstats'
    SCHEMA = {
        'year': int,
        'month': int,
        'highest_salary': int,
        'lowest_salary': int,
        'median_salary': int,
        'mean_salary': int
    }
