
import pandas as pd
import json
data = '''[{
      "_id": "26",
        "Description": "10 YEAR",
        "TypeLevel1": "INTEREST",
        "Currency": "USD",
        "Operational": true,
        "TypeLevel2": "LONG",
      "Settlement": "90",
          "SCSP": "Rajna",
        "BBT": "CITITYM9",
        "TCK": "ZN",
          "SMCP": "01",
          "SMCP2": "02"
    },
    {
      "_id": "27",
        "Description": "5 YEAR",
        "TypeLevel1": "PRINCIPAL",
        "Currency": "GNP",
        "Operational": false,
        "TypeLevel2": "LONG",
      "Settlement": "40",
          "SCSP": "Paus",
        "BBT": "CITITYM10",
        "TCK": "PY",
          "SMCP": "05",
          "SMCP2": "09"
    }]'''

x=pd.read_json(data)
print( x)