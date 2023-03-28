## Проект Mobile автотестов для приложения Wikipedia
### Используемые технологии
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jira" src="https://logojinni.com/image/logos/jira-3.svg"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="Appium" src="https://cdn.worldvectorlogo.com/logos/appium.svg"></code>
<code><img width="5%" title="Browserstack" src="https://brandeps.com/logo-download/B/BrowserStack-logo-vector-01.svg"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
<code><img width="5%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"></code>
</p>
<br> 

### Что проверяют тесты
* Навигация по стартовым экранам
* Переход на главную по кнопке Skip
* Проверка не пустого результата поиска
* Текст ошибки для поля "Пользователь" при вводе невалидного значения
* Отображение пустого экрана "Сохраненный"
<br>

### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/asantalov_diplom_mobile/)
##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение на сервере Jenkins.
![Jenkins_run](/images/allure.jpg)

### <img width="3%" title="Browserstack" src="https://brandeps.com/logo-download/B/BrowserStack-logo-vector-01.svg"> Запуск проекта в Browserstack
##### После запуска сборки в Jenkins, тесты начинают проходить удаленно через Browserstack. Где в реальном времени можно следить за прохождением теста через логи.

![Browserstack](images/bs.jpg)

### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> Allure report
##### После прохождения тестов, результаты можно посмотреть в Allure отчете.
![Overview](images/allure2.jpg)

##### Во вкладке Behaviors находятся собранные тест кейсы, у которых описаны шаги. Для api методов реализованы вложения. Для комбинированных тестов по окончанию теста делается скриншот и сохраняется видеозапись теста.
![Behaviors](images/allure1.jpg)

##### Видео теста Текст ошибки для поля "Пользователь" при вводе невалидного значения.
![test](images/error.gif)


### <img width="3%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"> [Интеграция с Allure TestOps](https://allure.autotests.cloud/project/2094/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![Graf](images/optest.jpg)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![tests](images/testops.jpg)


### <img width="3%" title="Jira" src="https://logojinni.com/image/logos/jira-3.svg"> [Интеграция с Jira](https://jira.autotests.cloud/browse/HOMEWORK-630)
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![Jira](images/Jira.jpg)


### <img width="3%" title="Telegram" src="https://cdn.icon-icons.com/icons2/923/PNG/256/telegram_icon-icons.com_72055.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![Telegram](images/telega.jpg)
