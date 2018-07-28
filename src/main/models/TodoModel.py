import datetime


class TodoModel:
    _name = ""
    _data = ""

    def __init__(self, name="No Name", data=""):
        self._name = name
        self._data = "".join([data])
        self._createdon = datetime.datetime
        self._modifiedon = None

    def get_name(self):
        return self._name

    def set_name(self, name=""):
        self._name = name or self._name
        self._modifiedon = datetime.datetime

    def get_data(self):
        return "".join(self._data) or None

    def add_data(self, data = ""):
        self._data = self._data.__add__(data)
        self._modifiedon = datetime.datetime

    def get_created_on(self):
        return self._createdon.day

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Name: {name}, data: {data}, created_on: {createdon}, modified_on: {modified_on}".format(name=self._name, data = self._data, createdon = self._createdon, modified_on=self._modifiedon)

