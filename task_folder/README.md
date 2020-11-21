### Отчет проверки валидности JSON данных 
*Ниже приведен список проверки предоставленных файлов (folder\event)* 

> Файлы прошедшие проверку идут со статусом: **Прошел проверку** :white_check_mark:

> Файлы с ошибками идут под статусом: **Найдена ошибка** :warning: 

**Как читать ошибки:**

В первой строке текста "ошибки" описывается параметр, не прошедший проверку. Например, ошибка **None is not of type "integer"** означает, что в требуемом поле указано **None**, вместо необходимого **integer**. Далее описан перечень параметров, предложенный schema-файлом, где описано правило для данного параметра проверки. В последней строке текста "ошибки" **On instance** указывается какой именно параметр в файле вызвал ошибку. В данном случае вместо требуемого **целого числа** (англ. - **integer**) в файле указан параметр **None** (что означает "ничего"). Для исправления нам необходимо в поле параметра указать **целое число**, либо переписать правило обработки данного параметра в schema-файле. 

 Если вам попался ответ **None** в строке **On instance**, и первый параметр описывает ошибку, как **None is not of type "object"**, в таких случаях файл проверки пуст или в нем указан один единственный параметр - **Null** 

Проверка файла по схеме: *cmarker_created.schema* 
----------
Проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка** :warning: 

```
None is not of type 'object'

Failed validating 'type' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'cmarkers': {'items': {'properties': {'date': {'type': 'string'},
                                                          'id': {'type': 'integer'},
                                                          'slug': {'type': 'string'}},
                                           'required': ['date',
                                                        'id',
                                                        'slug'],
                                           'type': ['object', 'string']},
                                 'type': 'array'},
                    'datetime': {'type': 'string'},
                    'user_id': {'type': 'integer'}},
     'type': 'object'}

On instance:
    None 
``` 

----------

Проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Найдена ошибка** :warning: 

```
None is not of type 'integer'

Failed validating 'type' in schema['properties']['user_id']:
    {'type': 'integer'}

On instance['user_id']:
    None 
``` 

----------

Проверка файла по схеме: *label_selected.schema* 
----------
Проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> **Найдена ошибка** :warning: 

```
'297e4dc6-07d1-420d-a5ae-e4aff3aedc19' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '297e4dc6-07d1-420d-a5ae-e4aff3aedc19' 
``` 

----------

Проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка** :warning: 

```
None is not of type 'object'

Failed validating 'type' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'id': {'type': ['null', 'integer']},
                    'labels': {'items': {'properties': {'category': {'type': ['null',
                                                                              'string']},
                                                        'color': {'type': ['null',
                                                                           'object']},
                                                        'is_custom_tag': {'type': 'boolean'},
                                                        'name_en': {'type': 'string'},
                                                        'name_ru': {'type': 'string'},
                                                        'property_arousal': {'type': ['string',
                                                                                      'null']},
                                                        'property_pleasure': {'type': ['string',
                                                                                       'null']},
                                                        'property_stability': {'type': ['string',
                                                                                        'null']},
                                                        'property_vitality': {'type': ['string',
                                                                                       'null']},
                                                        'property_where': {'type': ['string',
                                                                                    'null']},
                                                        'slug': {'type': 'string'},
                                                        'type': {'type': 'integer'},
                                                        'type_stress': {'type': 'integer'}},
                                         'required': ['category',
                                                      'color',
                                                      'is_custom_tag',
                                                      'name_en',
                                                      'name_ru',
                                                      'property_arousal',
                                                      'property_pleasure',
                                                      'property_stability',
                                                      'property_vitality',
                                                      'property_where',
                                                      'slug',
                                                      'type',
                                                      'type_stress'],
                                         'type': 'object'},
                               'type': 'array'},
                    'rr_id': {'type': ['null', 'integer']},
                    'timestamp': {'type': 'string'},
                    'unique_id': {'type': 'string'},
                    'user': {'properties': {'id': {'type': 'integer'}},
                             'required': ['id'],
                             'type': 'object'},
                    'user_id': {'type': 'integer'}},
     'type': 'object'}

On instance:
    None 
``` 

----------

Проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> **Найдена ошибка** :warning: 

```
'2e8ffd3c-dbda-42df-9901-b7a30869511a' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '2e8ffd3c-dbda-42df-9901-b7a30869511a' 
``` 

----------

Проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> **Найдена ошибка** :warning: 

```
'3ade063d-d1b9-453f-85b4-dda7bfda4711' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '3ade063d-d1b9-453f-85b4-dda7bfda4711' 
``` 

----------

Проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> **Найдена ошибка** :warning: 

```
'3b4088ef-7521-4114-ac56-57c68632d431' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '3b4088ef-7521-4114-ac56-57c68632d431' 
``` 

----------

Проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> **Найдена ошибка** :warning: 

```
'1fe93f66-eaa8-11ea-a179-58e81c50ca6b' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '1fe93f66-eaa8-11ea-a179-58e81c50ca6b' 
``` 

----------

Проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> **Найдена ошибка** :warning: 

```
'bb998113-bc02-4cd1-9410-d9ae94f53eb0' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    'bb998113-bc02-4cd1-9410-d9ae94f53eb0' 
``` 

----------

Проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> **Найдена ошибка** :warning: 

```
'1fec4e4e-f8a6-11ea-a4b2-fc287a5c983c' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    '1fec4e4e-f8a6-11ea-a4b2-fc287a5c983c' 
``` 

----------

Проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> **Найдена ошибка** :warning: 

```
'e2d760c3-7e10-4464-ab22-7fda6b5e2562' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    'e2d760c3-7e10-4464-ab22-7fda6b5e2562' 
``` 

----------

Проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> **Найдена ошибка** :warning: 

```
'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    'f5656ff6-29e1-46b0-8d8a-ff77f9cc0953' 
``` 

----------

Проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> **Найдена ошибка** :warning: 

```
'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    'fb1a0854-9535-404d-9bdd-9ec0abb6cd6c' 
``` 

----------

Проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Найдена ошибка** :warning: 

```
'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c' is not of type 'null', 'integer'

Failed validating 'type' in schema['properties']['id']:
    {'type': ['null', 'integer']}

On instance['id']:
    'ffe6b214-d543-40a8-8da3-deb0dc5bbd8c' 
``` 

----------

Проверка файла по схеме: *sleep_created.schema* 
----------
Проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка** :warning: 

```
None is not of type 'object'

Failed validating 'type' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'activity_type': {'type': 'string'},
                    'finish_time': {'type': 'string'},
                    'info': {'items': {'properties': {'type': {'type': 'string'},
                                                      'value': {'type': 'number'}},
                                       'required': ['type', 'value'],
                                       'type': 'object'},
                             'type': 'array'},
                    'phases_info': {'items': {'properties': {'duration': {'type': 'number'},
                                                             'percent': {'type': 'number'},
                                                             'type': {'type': 'string'}},
                                              'required': ['duration',
                                                           'percent',
                                                           'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'points': {'items': {'properties': {'x_date': {'type': 'string'},
                                                        'y_value': {'type': 'number'}},
                                         'required': ['x_date', 'y_value'],
                                         'type': 'object'},
                               'type': 'array'},
                    'source': {'type': 'string'},
                    'time_start': {'type': 'string'},
                    'timestamp': {'type': 'string'},
                    'type_ranges': {'items': {'properties': {'date': {'type': 'string'},
                                                             'type': {'type': 'string'}},
                                              'required': ['date', 'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'unique_id': {'type': 'string'}},
     'type': 'object'}

On instance:
    None 
``` 

----------

Проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла по схеме: *workout_created.schema* 
----------
Проверка файла: 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json >>> **Найдена ошибка** :warning: 

```
None is not of type 'object'

Failed validating 'type' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'activity_name': {'type': 'string'},
                    'activity_type': {'type': 'string'},
                    'calories': {'type': 'integer'},
                    'calories_active': {'type': 'number'},
                    'calories_basal': {'type': 'number'},
                    'distance': {'type': 'integer'},
                    'duration': {'type': 'number'},
                    'exercise_time': {'type': 'integer'},
                    'met': {'type': 'number'},
                    'pace_avg': {'type': 'number'},
                    'pulse': {'type': 'integer'},
                    'pulse_max': {'type': ['null', 'integer']},
                    'pulse_min': {'type': ['null', 'integer']},
                    'resting_hr': {'type': 'integer'},
                    'source': {'type': 'string'},
                    'speed_avg': {'type': 'number'},
                    'steps': {'type': 'integer'},
                    'steps_speed_avg': {'type': 'number'},
                    'steps_speed_max': {'type': 'number'},
                    'time_end': {'type': 'string'},
                    'time_start': {'type': 'string'},
                    'timestamp': {'type': 'string'},
                    'type_ranges': {'properties': {'cardio': {'type': 'integer'},
                                                   'fat_burn': {'type': 'integer'},
                                                   'hardcore': {'type': 'integer'},
                                                   'warm_up': {'type': 'integer'}},
                                    'required': ['cardio',
                                                 'fat_burn',
                                                 'hardcore',
                                                 'warm_up'],
                                    'type': 'object'},
                    'unique_id': {'type': 'string'}},
     'type': 'object'}

On instance:
    None 
``` 

----------

Проверка файла: 2e8ffd3c-dbda-42df-9901-b7a30869511a.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3ade063d-d1b9-453f-85b4-dda7bfda4711.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 3b4088ef-7521-4114-ac56-57c68632d431.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: 6b1984e5-4092-4279-9dce-bdaa831c7932.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: a95d845c-8d9e-4e07-8948-275167643a40.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ba25151c-914f-4f47-909a-7a65a6339f34.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: bb998113-bc02-4cd1-9410-d9ae94f53eb0.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: c72d21cf-1152-4d8e-b649-e198149d5bbb.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: cc07e442-7986-4714-8fc2-ac2256690a90.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: e2d760c3-7e10-4464-ab22-7fda6b5e2562.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json >>> **Прошел проверку** :white_check_mark: 

----------

Проверка файла: ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json >>> **Прошел проверку** :white_check_mark: 

----------

