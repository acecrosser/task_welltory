### task_welltory

Тестовое задание на back-end developer

> Необходимо написать скрипт, который сможет найти максимальное количество ошибок структуры и данных

Решение находится в папке /task_folder

Результат работы автоматически формируется в файл README.md; папки с файлами проверки должны находиться в том же месте где 
и файл скрипта. 

При работе с schema-файлами был удален первый параметр **"required"**, описывающий список ключевых
имен валидации. К сожалению, абсолютно все файлы проверки не содержат точного наименования
данных параметров, и при работе с ними каждый файл проверки выполняется с ошибкой *(возможно это ошибка,
но другого решения и объяснения найти не удалось)*.

Привожу описание данного параметра с официаильного сайта:
https://json-schema.org/learn/getting-started-step-by-step.html

> In JSON Schema terms, we update our schema to add:

> The ``properties`` validation keyword.
The ``productId`` key.
``description`` schema annotation and type validation keyword is noted – we covered both of these in the previous section.
The ``required`` validation keyword listing productId.

