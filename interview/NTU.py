# -*- coding: utf-8 -*-
"""
Created on 03/12/2025 14:17

@author: Aidan
@project: leetcode
@filename: NTU
"""
import json

import requests

url = "https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages?updatedFrom=2020-12-31T23:00:00&updatedTo=2021-01-07T22:59:59"
# params = {
#     # e.g. filter by date
#     "updatedFrom": "2025-11-01T00:00:00"
# }
resp = requests.get(url)
data = resp.json()
# print(data)
print(json.dumps(data, indent=2))
# data will be a JSON object containing release packages (i.e. tenders)
