import pytest
from project import validate_personal_information, validate_educational_information, validate_language_information, validate_work_information


def test_validate_personal_information():
    dict1 = {'name': 'XY', 'birthday': 'XY', 'place of birth': 'XY'}
    dict2 = None
    assert validate_personal_information(dict1) == "y"
    assert validate_personal_information(dict2) == "n"

def test_validate_educational_information():
    dict1 = {"degree0": {'Degree': 'XY','Name': 'XY','Timeframe': 'XY'}}
    dict2 = {"degree0": {'Degree': 'Bachelor','Name': 'Harvard','Timeframe': '2010-2015'},
             "degree1": {'Degree': 'Master','Name': 'MIT','Timeframe': '2015-2020'}
             }
    assert validate_educational_information(dict1) == "n"
    assert validate_educational_information(dict2) == "y"

def test_validate_language_information():
    dict1 = {"language0": {'language': 'XY','proficiency': 'native'}}
    dict2 = {"language0": {'language': 'English','proficiency': 'C2'},
             "language1": {'language': 'German','proficiency': 'C1'}
             }
    assert validate_language_information(dict1) == "n"
    assert validate_language_information(dict2) == "y"

def test_validate_work_information():
    dict1 = {"work0": {'job': 'XY','company': 'Company Name', 'time': '20XX-20YY'}}
    dict2 = {"work0": {'job': 'Consultant','company': 'Financial Services Company', 'time': '2010-2015'},
             "work1": {'job': 'Engineer','company': 'Engineering Company', 'time': '2015-2020'}
             }
    assert validate_work_information(dict1) == "n"
    assert validate_work_information(dict2) == "y"