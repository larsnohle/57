#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient()
db = client.exercise39of57

result = db.employees.insert_one({"firstName": "John", "lastName": "Johnson", "position": "Manager", "separationDate": "2016-12-31"})
result = db.employees.insert_one({"firstName": "Tou", "lastName": "Xiong", "position": "Softeare Engineer", "separationDate": "2016-10-05"})
result = db.employees.insert_one({"firstName": "Michaela", "lastName": "Michaelson", "position": "District Manager", "separationDate": "2015-12-29"})
result = db.employees.insert_one({"firstName": "Jake", "lastName": "Jacobson", "position": "Programmer", "separationDate": ""})
result = db.employees.insert_one({"firstName": "Jacquelyn", "lastName": "Jackson", "position": "DBA", "separationDate": ""})
result = db.employees.insert_one({"firstName": "Sally", "lastName": "Weber", "position": "Web Developer", "separationDate": "2015-12-18"})

