from jsonschema import validate, Draft7Validator, SchemaError, ValidationError
import json
import os

list_schema = os.listdir('.' + '\\schema')
list_event = os.listdir('.' + '\\event')

with open('README.md', 'w', encoding='utf-8') as readme:
    readme.write('### Отчет проверки валидности JSON данных \n'
                 '*Ниже приведен список проверки предоставленных файлов (folder\\event)* \n\n'
                 '> Файлы прошедшие проверку идут со статусом: **Прошел проверку** :white_check_mark:\n\n'
                 '> Файлы с ошибками идут под статусом: **Найдена ошибка** :warning: \n\n'
                 '**Как читать ошибки:**\n\n'
                 'В первой строке ошибки описывается тот параметр который не прошел проверку. К примеру ошибка -  '
                 '*None is not of type "integer"* - указывает, что в требуемом поле указано **None**, вместо '
                 'необходимого **integer**. Далее описывается схема параметров предложенной schema-проверки файлов, '
                 'где описано правило для данного параметра. Последней строкой **On instance** указывается какой '
                 'именно параметр в файле указан ошибочно. '
                 'В данном случае, вместе требуемого "целого числа" (перевеод с англ. - integer) в файле указан '
                 'параметр "None", что означает ничего. Для исправления нам нужно в требуемом поле параметра '
                 'указать целое число либо переписать правило обработки данного параметра в файле schema. \n\n '
                 'Если вам попался ответ **None** в строке **On instance** и первый '
                 'параметр описывает ошибку как - **None is not of type "object"** в таких случаях файл проверки '
                 'пуст или в нем указан один единственный параметр - **Null**'
                 ' \n\n')

    for schema in list_schema:
        with open(f'schema\\{schema}', 'r') as schema_file:
            schema_data = schema_file.read()
            schema_data = json.loads(schema_data)
        readme.write(f'Проверка файла по схеме: *{schema}* \n')
        readme.write('-' * 10 + '\n')
        try:
            Draft7Validator.check_schema(schema_data)
        except SchemaError as er:
            readme.write(str(er))

        for event in list_event:
            with open(f'event\\{event}', 'r') as check_file:
                file = check_file.read()
                file = json.loads(file)
            readme.write(f'Проверка файла: {event} >>> ')
            try:
                validate(instance=file, schema=schema_data)
                readme.write(f'**Прошел проверку** :white_check_mark: \n\n')
            except ValidationError as er:
                readme.write(f'**Найдена ошибка** :warning: \n\n')
                readme.write(f'```\n{str(er)} \n``` \n\n')
            readme.write('-' * 10 + '\n')
            readme.write('\n')
