### task_welltory

Тестовое задание на back-end developer

> Необходимо написать скрипт, который сможет найти максимальное количество ошибок структуры и данных

Решение находиться в папке /task_folder

Результат работы автоматические формируется в файл README.md, папки с файлами должны находить в том же месте где 
и файл скрипта. 

При работе с файлами schema был убран первый параметр **"required"** описывающий список ключевых
имен валидации, к сожалению все файлы проверки не содержат точного наименования
данных параметров и при работе с ним, каждый файл проверки был с ошибками *(возможно это ошибка,
но другого решения и объяснения к сожалению найти не удалось)*.

Привожу с официального сайта, описание данного параметра:
https://json-schema.org/learn/getting-started-step-by-step.html

> In JSON Schema terms, we update our schema to add:

> The ``properties`` validation keyword.
The ``productId`` key.
``description`` schema annotation and type validation keyword is noted – we covered both of these in the previous section.
The ``required`` validation keyword listing productId.

