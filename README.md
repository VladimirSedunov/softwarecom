<h1 align="center">Проект по тестированию главной страницы сайта<br>"Софт Компани — цифровой системный интегратор."</h1>
> <a target="_blank" href="https://softwarecom.ru/">Ссылка на единый портал</a>

![This is an image](/design/images/main_page.png)

### Список проверок, реализованных в автотестах
- [x] Наличие требуемых заголовков на каждой из страниц, соответствующих пунктам в главном (верхнем) меню
- [x] Наличие текста с копирайтом "Софт Компани — цифровой интегратор © 2023" и текущего года на основной странице
- [x] Наличие сообщения 'Страница_не_найдена' при попытке перехода на несуществующую страницу
- [x] Наличие подпунктов меню главного меню (при наведении курсора мыши) и корректное открытие соответствующих страниц
- [x] Наличие блоков с логотипами организаций внизу страницы в разделе 'Клиенты и партнёры', возможность пролистывания блоков и замена логотипа на содержательную информацию при наведении курсора 
- [x] Для каждой комбинации "Отрасль" + "Услуга" отображаются отфильтрованные блоки с логотипами клиентов
- [x] Отправка сообщения из меню "Обратная Связь" / "Задать вопрос" с корректным и некорректными наборами реквизитов
- [x] Те же проверки при отправке сообщения, но реализованные с помощью параметризации теста
- [x] Отправка сообщения со страницы "О нас", кнопка "Отправить заявку", реализованная с помощью Page Object
- [x] Проверка контактных данных на странице "Контакты" (адрес, email и телефон есть и соответствуют реальным данным)
- [x] Те же проверки для сервиса REST API

## Проект реализован с использованием
Python = Pytest = Selenium = Selene = Selenoid = Allure Report = Jenkins = Telegram = Java

![](/design/icons/Python.png)&emsp;![](/design/icons/Pytest.png)&emsp;![](/design/icons/Selenium.png)&emsp;![](/design/icons/Selene.png)&emsp;![](/design/icons/Selenoid.png)&emsp;![](/design/icons/Allure_Report.png)&emsp;![](/design/icons/Jenkins.png)&emsp;![](/design/icons/Telegram.png)&emsp;![](/design/icons/Java.png)


## Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="http://10.155.56.61:8888/job/Demo test softwarecom/">Ссылка на проект в Jenkins</a>


### Параметры сборки

* SELECT_TESTS (default: tests -m jenkins_ok). Параметр определяет группу тестов или отдельный тест для запуска.
* browser (default: chrome). Браузер chrome или firefox.
* browser_version (default: 96.0). Версия браузера на Selenoid.
* window_size (default: 1920x1080). Размер окна браузера.


### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="http://10.155.56.61:8888/job/Demo test softwarecom/">проект</a>

![This is an image](/design/images/jenkins1.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design/images/jenkins2a.png)

## Локальный запуск автотестов
Пример командной строки:
```bash
gradle clean ui_tests -Dlogin=user1 -Dpassword=1234 -DtestUrl=selenoid.autotests.cloud/wd/hub/
```

Получение отчёта:
```bash
allure serve build/allure-results
```

# Полная статистика по прохождению тестпланов, отчёты и приложения к ним хранятся в Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/804">Сссылка на проект в AllureTestOps</a> (запрос доступа admin@qa.guru)

### Тест-планы проекта
![This is an image](/design/images/testplans.png)
### Кейсы тест-плана выполнения ручного тестирования
![This is an image](/design/images/manual.png)
### Кейсы тест-плана выполнения автотестирования
![This is an image](/design/images/auto.png)
### Общий список всех кейсов, имеющихся в системе (без разделения по тест-планам и виду выполнения тестирования)
![This is an image](/design/images/testcases.png)
### Пример dashboard с общими результатами тестирования
![This is an image](/design/images/dashboard_all.png)
### В том числе сводная статистика запусков
![This is an image](/design/images/dashboard_all2.png)

### Пример отчёта выполнения одного из автотестов
![This is an image](/design/images/onecasereport.png)
#### *После окончания выполнения автотестов по каждому из них в отчёте доступны скриншоты и исходный код страницы, лог консоли браузера и видеозапись выполнения теста.*

### Пример видеозаписи прохождения теста
![This is an image](/design/images/Video.gif)


## По результатам ручного тестирования выявлены дефекты, зафиксированные в соответствующих задачах AllureTestOps
### Тест план выполнения ручного тестирования
![This is an image](/design/images/testplan2.png)
### Сводные результаты ручного тестирования
![This is an image](/design/images/failedresult.png)
### Пример описания дефекта в Allure TestOps
![This is an image](/design/images/testops2.png)
### Список выявленных дефектов, открытых как задачи в Allure TestOps
![This is an image](design/images/defects.png)

# Результаты выполнения тестов и информация о выявленных дефектах интегрированы с Atlassian Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-286">Ссылка на задачу в Jira</a> (запрос доступа admin@qa.guru)

Задачи на выявленные дефекты оформлены как подзадачи к данной. Связаны с соответствующими дефектами в Allure TestOps

![This is an image](/design/images/jira_n.png)

# Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/design/images/bot.png)


:heart: <a target="_blank" href="https://qa.guru">qa.guru</a><br/>
:blue_heart: <a target="_blank" href="https://t.me/qa_automation">t.me/qa_automation</a>
