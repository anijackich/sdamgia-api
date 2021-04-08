#SdamGIA Api

**SdamGIA Api** – Python модуль для взаимодействия с образовательным порталом СДАМ ГИА

## Структура СдамГИА
Чтобы было проще понять, как устроена база заданий СдамГИА, предлагаю воспользоваться следующей схемой:
```
СдамГИА
└── Предмет (subject)
    ├── Каталог заданий (catalog)
    │   └── Задание (topic)
    │       └── Категория (category)
    │           └── Задача (problem)
    └── Тест (test)
        └── Задача (problem)       
```
У каждой задачи, категории или теста есть свой идентификатор. 
Задания тоже имеют номера, которые в свою очередь могут иметь такие значения как "Д1" или "C4". Этим они отличаются от идентификаторов.

## Установка

    $ pip3 install sdamgia-api

### Установка зависимостей
Для поиска задач по тексту на изображении необходимо установить pytesseract:

    $ pip3 install pytesseract

А так же [Tesseract-OCR](https://www.severcart.ru/blog/all/install_tesseract/)


## Использование

### Инициализация
```python
from sdamgia import SdamGIA

sdamgia = SdamGIA()
```

### Поиск задачи по ее идентификатору
```python
subject = 'math'
id = '1001'
sdamgia.get_problem_by_id(subject, id)
```
```shell
{
  'id': '1001',
  'topic': '4',
  'condition': {
    'text': 'На экзамен вынесено 60 вопросов, Андрей не выучил 3 из них. Найдите вероятность того, что ему попадется выученный вопрос.', 
    'images': []
  }, 
  'solution': {
    'text': 'Решение.Андрей выучил 60\xa0–\xa03\xa0=\xa057 вопросов. Поэтому вероятность того, что на экзамене ему попадется выученный вопрос равна\xa0Ответ: 0,95.',
    'images': ['https://ege.sdamgia.ru/formula/svg/9f/9fbf55ab44a507fb47ba8a2666cd7644.svg']
  }, 
  'answer': '0,95', 
  'analogs': ['1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010'], 
  'url': 'https://math-ege.sdamgia.ru/problem?id=1001'
}
```


### Поиск задач по запросу
```python
subject = 'math'
request = 'Найдите количество'
sdamgia.search(subject, request)
```
```shell
['6407', '8795', '8799', '27501', '519508', '519534', '525371', '512436', '6401', '6421', '6427', '7321', '7325', '7801', '7803', '7807', '7809', '8037', '8039', '8045']
```

### Поиск теста по его идентификатору
```python
subject = 'math'
id = '1770'
sdamgia.get_test_by_id(subject, id)
# Возвращает список задач, входящих в тест
```
```shell
['77345', '28765', '77374', '27903', '26675', '27700', '77411', '27506', '27132', '28008', '26703', '99592']
```

### Поиск категории по ее идентификатору
```python
subject = 'math'
id = '1'
sdamgia.get_category_by_id(subject, id)
# Возвращает список задач, входящих в категорию
```
```shell
['77334', '323512', '501201', '509077', '509106']
```

### Получение каталога
```python
subject = 'math'
sdamgia.get_catalog(subject)
```
```shell
[
  {
    'topic_id': '1',
    'topic_name': 'Простейшие текстовые задачи', 
    'categories': [
      {'category_id': '174', 'category_name': 'Вычисления'}, 
      {'category_id': '1', 'category_name': 'Округление с недостатком'}, 
      {'category_id': '2', 'category_name': 'Округление с избытком'},
      {'category_id': '249', 'category_name': 'Проценты'},
      {'category_id': '5', 'category_name': 'Проценты и округление'}
    ]
  },
  {
    ...
  }        
]
```

### Генерация теста
По умолчанию генерируется тест, включающий по одной задаче из каждого задания предмета. <br>
Так же можно вручную указать одинаковое количество задач для каждого из заданий: {'full': <кол-во задач>} <br>
Указать определенные задания с определенным количеством задач для каждого: {<номер задания>: <кол-во задач>, ... }
```python
subject = 'math'
problems = {1: 1, 2: 2, 3: 4}
sdamgia.generate_test(subject, problems)
# Возвращает идентификатор сгенерированного теста
```
```shell
38299510
```
Обратите внимание, что в этом случае идентификатор задания - только науральное число. Т.е. если после задания 15 идет задание Д1, оно должно будет записываться как 16 задание.

### Генерация pdf-версии теста
```python
sdamgia.generate_pdf('math', '38299510', pdf='h')
```
```shell
https://math-ege.sdamgia.ru/pdf/1fe7d7d8408f8d5195fabfd8ab393d63.pdf
```
Список параметров:
```
subject: Наименование предмета
testid: Идентифигатор теста
solution: Пояснение
nums: № заданий
answers: Ответы
key: Ключ
crit: Критерии
instruction: Инструкция
col: Нижний колонтитул
pdf: Версия генерируемого pdf документа
    По умолчанию генерируется стандартная вертикальная версия
    h - горизонтальная версия
    z - версия с крупным шрифтом
    m - версия с большим полем
```

### Поиск задач по изображению

С помощью sdamgia-api вы можете искать задачи по тексту на изображении. Например, на фотографии распечатки.

Для начала, необходимо указать путь к исполняемому файлу Tesseract-OCR:
```python
sdamgia.tesseract_src = "C:/Program Files/Tesseract-OCR/tesseract.exe"
```
Теперь мы можем запустить поиск:
```python
sdamgia.search_by_img('rus', 'Image.jpg')
# Возвращает список найденных задач
```
```shell
['12629', '14062', '2846', '2836', '2837', '2838', '2839', '2845', '2847', '7776', '10242', '874', '864', '865', '866', '867', '873', '2359', '456', '446', '447', '448', '449', '455', '2348', '7815', '691', '863', '14426', '7867', '1262', '1889', '6716', '6706', '6707', '6708', '6709', '6715', '6717', '8899', '8895', '8896', '8897', '8898', '8900', '4194', '4184', '4185', '4186', '4187', '4193', '4195', '30', '28', '29', '31', '37', '38', '2337', '676', '674', '675', '677', '683', '684', '2168', '1094', '1092', '1093', '1095', '1101', '1102', '2365', '6893', '6891', '6892', '6894', '6900', '6901', '6902', '599', '598', '600', '601', '607', '608', '2352', '1710', '1700', '1701', '1702', '1703', '1709', '2381', '3600', '3599', '3601', '3602', '3608', '3609', '3610', '8327', '8323', '8324', '8325', '8326', '8328', '950', '940', '941', '942', '943', '949', '2361', '11087', '11065', '1304', '1299', '1342', '1337', '1474', '1472', '1473', '1475', '1481', '1482', '2375', '105', '104', '106', '107', '113', '114', '2339', '181', '180', '182', '183', '189', '190', '2341', '257', '256', '258', '259', '265', '266', '1321', '2343', '333', '332', '334', '335', '341', '342', '2345', '380', '370', '371', '372', '373', '379', '2346', '532', '522', '523', '524', '525', '531', '2350', '656', '652', '759', '750', '751', '752', '753', '760', '2356', '789', '788', '790', '791', '797', '798', '2357', '844', '842', '988', '978', '979', '980', '981', '987', '2362', '997', '995', '1026', '1016', '1017', '1018', '1019', '1025', '2363', '1254', '1244', '1245', '1246', '1247', '1253', '2369', '1292', '1282', '1283', '1284', '1285', '1291', '2370', '7568']
```
Поиск может занять продолжительное время в зависимости от объема текста и количества найденных задач