Проверка папки по схеме: cmarker_created.schema 
----------
Начата проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> Файл прошел проверку 

----------

Начата проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> Файл прошел проверку 

----------

Начата проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка:** 

```json 
 ["None is not of type 'object'\n\nFailed validating 'type' in schema:\n    {'$schema': 'http://json-schema.org/schema#',\n     'properties': {'cmarkers': {'items': {'properties': {'date': {'type': 'string'},\n                                                          'id': {'type': 'integer'},\n                                                          'slug': {'type': 'string'}},\n                                           'required': ['date',\n                                                        'id',\n                                                        'slug'],\n                                           'type': ['object', 'string']},\n                                 'type': 'array'},\n                    'datetime': {'type': 'string'},\n                    'user_id': {'type': 'integer'}},\n     'type': 'object'}\n\nOn instance:\n    None"] 
``` 

----------

Начата проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> Файл прошел проверку 

----------

Начата проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> Файл прошел проверку 

----------

Начата проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> Файл прошел проверку 

----------

Начата проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> Файл прошел проверку 

----------

Начата проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> Файл прошел проверку 

----------

Начата проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> Файл прошел проверку 

----------

Начата проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> Файл прошел проверку 

----------

Начата проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> Файл прошел проверку 

----------

Начата проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> Файл прошел проверку 

----------

Начата проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> Файл прошел проверку 

----------

Начата проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Найдена ошибка:** 

```json 
 ["None is not of type 'integer'\n\nFailed validating 'type' in schema['properties']['user_id']:\n    {'type': 'integer'}\n\nOn instance['user_id']:\n    None"] 
``` 

----------

Проверка папки по схеме: label_selected.schema 
----------
Начата проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> Файл прошел проверку 

----------

Начата проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> **Найдена ошибка:** 

```json 
 ["'297e4dc6-07d1-420d-a5ae-e4aff3aedc19' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '297e4dc6-07d1-420d-a5ae-e4aff3aedc19'"] 
``` 

----------

Начата проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка:** 

```json 
 ["None is not of type 'object'\n\nFailed validating 'type' in schema:\n    {'$schema': 'http://json-schema.org/schema#',\n     'properties': {'id': {'type': ['null', 'integer']},\n                    'labels': {'items': {'properties': {'category': {'type': ['null',\n                                                                              'string']},\n                                                        'color': {'type': ['null',\n                                                                           'object']},\n                                                        'is_custom_tag': {'type': 'boolean'},\n                                                        'name_en': {'type': 'string'},\n                                                        'name_ru': {'type': 'string'},\n                                                        'property_arousal': {'type': ['string',\n                                                                                      'null']},\n                                                        'property_pleasure': {'type': ['string',\n                                                                                       'null']},\n                                                        'property_stability': {'type': ['string',\n                                                                                        'null']},\n                                                        'property_vitality': {'type': ['string',\n                                                                                       'null']},\n                                                        'property_where': {'type': ['string',\n                                                                                    'null']},\n                                                        'slug': {'type': 'string'},\n                                                        'type': {'type': 'integer'},\n                                                        'type_stress': {'type': 'integer'}},\n                                         'required': ['category',\n                                                      'color',\n                                                      'is_custom_tag',\n                                                      'name_en',\n                                                      'name_ru',\n                                                      'property_arousal',\n                                                      'property_pleasure',\n                                                      'property_stability',\n                                                      'property_vitality',\n                                                      'property_where',\n                                                      'slug',\n                                                      'type',\n                                                      'type_stress'],\n                                         'type': 'object'},\n                               'type': 'array'},\n                    'rr_id': {'type': ['null', 'integer']},\n                    'timestamp': {'type': 'string'},\n                    'unique_id': {'type': 'string'},\n                    'user': {'properties': {'id': {'type': 'integer'}},\n                             'required': ['id'],\n                             'type': 'object'},\n                    'user_id': {'type': 'integer'}},\n     'type': 'object'}\n\nOn instance:\n    None"] 
``` 

----------

Начата проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> **Найдена ошибка:** 

```json 
 ["'2e8ffd3c-dbda-42df-9901-b7a30869511a' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '2e8ffd3c-dbda-42df-9901-b7a30869511a'"] 
``` 

----------

Начата проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> **Найдена ошибка:** 

```json 
 ["'3ade063d-d1b9-453f-85b4-dda7bfda4711' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '3ade063d-d1b9-453f-85b4-dda7bfda4711'"] 
``` 

----------

Начата проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> **Найдена ошибка:** 

```json 
 ["'3b4088ef-7521-4114-ac56-57c68632d431' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '3b4088ef-7521-4114-ac56-57c68632d431'"] 
``` 

----------

Начата проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> **Найдена ошибка:** 

```json 
 ["'1fe93f66-eaa8-11ea-a179-58e81c50ca6b' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '1fe93f66-eaa8-11ea-a179-58e81c50ca6b'"] 
``` 

----------

Начата проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> Файл прошел проверку 

----------

Начата проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> Файл прошел проверку 

----------

Начата проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> **Найдена ошибка:** 

```json 
 ["'bb998113-bc02-4cd1-9410-d9ae94f53eb0' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    'bb998113-bc02-4cd1-9410-d9ae94f53eb0'"] 
``` 

----------

Начата проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> **Найдена ошибка:** 

```json 
 ["'1fec4e4e-f8a6-11ea-a4b2-fc287a5c983c' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    '1fec4e4e-f8a6-11ea-a4b2-fc287a5c983c'"] 
``` 

----------

Начата проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> Файл прошел проверку 

----------

Начата проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> **Найдена ошибка:** 

```json 
 ["'e2d760c3-7e10-4464-ab22-7fda6b5e2562' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    'e2d760c3-7e10-4464-ab22-7fda6b5e2562'"] 
``` 

----------

Начата проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> **Найдена ошибка:** 

```json 
 ["'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953'"] 
``` 

----------

Начата проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> **Найдена ошибка:** 

```json 
 ["'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c'"] 
``` 

----------

Начата проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Найдена ошибка:** 

```json 
 ["'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c' is not of type 'null', 'integer'\n\nFailed validating 'type' in schema['properties']['id']:\n    {'type': ['null', 'integer']}\n\nOn instance['id']:\n    'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c'"] 
``` 

----------

Проверка папки по схеме: sleep_created.schema 
----------
Начата проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> Файл прошел проверку 

----------

Начата проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> Файл прошел проверку 

----------

Начата проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка:** 

```json 
 ["None is not of type 'object'\n\nFailed validating 'type' in schema:\n    {'$schema': 'http://json-schema.org/schema#',\n     'properties': {'activity_type': {'type': 'string'},\n                    'finish_time': {'type': 'string'},\n                    'info': {'items': {'properties': {'type': {'type': 'string'},\n                                                      'value': {'type': 'number'}},\n                                       'required': ['type', 'value'],\n                                       'type': 'object'},\n                             'type': 'array'},\n                    'phases_info': {'items': {'properties': {'duration': {'type': 'number'},\n                                                             'percent': {'type': 'number'},\n                                                             'type': {'type': 'string'}},\n                                              'required': ['duration',\n                                                           'percent',\n                                                           'type'],\n                                              'type': 'object'},\n                                    'type': 'array'},\n                    'points': {'items': {'properties': {'x_date': {'type': 'string'},\n                                                        'y_value': {'type': 'number'}},\n                                         'required': ['x_date', 'y_value'],\n                                         'type': 'object'},\n                               'type': 'array'},\n                    'source': {'type': 'string'},\n                    'time_start': {'type': 'string'},\n                    'timestamp': {'type': 'string'},\n                    'type_ranges': {'items': {'properties': {'date': {'type': 'string'},\n                                                             'type': {'type': 'string'}},\n                                              'required': ['date', 'type'],\n                                              'type': 'object'},\n                                    'type': 'array'},\n                    'unique_id': {'type': 'string'}},\n     'type': 'object'}\n\nOn instance:\n    None"] 
``` 

----------

Начата проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> Файл прошел проверку 

----------

Начата проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> Файл прошел проверку 

----------

Начата проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> Файл прошел проверку 

----------

Начата проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> Файл прошел проверку 

----------

Начата проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> Файл прошел проверку 

----------

Начата проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> Файл прошел проверку 

----------

Начата проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> Файл прошел проверку 

----------

Начата проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> Файл прошел проверку 

----------

Начата проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> Файл прошел проверку 

----------

Начата проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> Файл прошел проверку 

----------

Начата проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> Файл прошел проверку 

----------

Проверка папки по схеме: workout_created.schema 
----------
Начата проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> Файл прошел проверку 

----------

Начата проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> Файл прошел проверку 

----------

Начата проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка:** 

```json 
 ["None is not of type 'object'\n\nFailed validating 'type' in schema:\n    {'$schema': 'http://json-schema.org/schema#',\n     'properties': {'activity_name': {'type': 'string'},\n                    'activity_type': {'type': 'string'},\n                    'calories': {'type': 'integer'},\n                    'calories_active': {'type': 'number'},\n                    'calories_basal': {'type': 'number'},\n                    'distance': {'type': 'integer'},\n                    'duration': {'type': 'number'},\n                    'exercise_time': {'type': 'integer'},\n                    'met': {'type': 'number'},\n                    'pace_avg': {'type': 'number'},\n                    'pulse': {'type': 'integer'},\n                    'pulse_max': {'type': ['null', 'integer']},\n                    'pulse_min': {'type': ['null', 'integer']},\n                    'resting_hr': {'type': 'integer'},\n                    'source': {'type': 'string'},\n                    'speed_avg': {'type': 'number'},\n                    'steps': {'type': 'integer'},\n                    'steps_speed_avg': {'type': 'number'},\n                    'steps_speed_max': {'type': 'number'},\n                    'time_end': {'type': 'string'},\n                    'time_start': {'type': 'string'},\n                    'timestamp': {'type': 'string'},\n                    'type_ranges': {'properties': {'cardio': {'type': 'integer'},\n                                                   'fat_burn': {'type': 'integer'},\n                                                   'hardcore': {'type': 'integer'},\n                                                   'warm_up': {'type': 'integer'}},\n                                    'required': ['cardio',\n                                                 'fat_burn',\n                                                 'hardcore',\n                                                 'warm_up'],\n                                    'type': 'object'},\n                    'unique_id': {'type': 'string'}},\n     'type': 'object'}\n\nOn instance:\n    None"] 
``` 

----------

Начата проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> Файл прошел проверку 

----------

Начата проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> Файл прошел проверку 

----------

Начата проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> Файл прошел проверку 

----------

Начата проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> Файл прошел проверку 

----------

Начата проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> Файл прошел проверку 

----------

Начата проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> Файл прошел проверку 

----------

Начата проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> Файл прошел проверку 

----------

Начата проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> Файл прошел проверку 

----------

Начата проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> Файл прошел проверку 

----------

Начата проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> Файл прошел проверку 

----------

Начата проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> Файл прошел проверку 

----------

Начата проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> Файл прошел проверку 

----------

