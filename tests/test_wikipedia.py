import allure
import pytest
from selene.support.conditions import have
from wiki_app.locators.wiki import *


@pytest.fixture()
def skip(app):
    with allure.step('Скип стартовых экранов'):
        app.element(btn_skip).click()


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты Wikipedia')
@allure.title('Навигация по стартовым экраным')
def test_navigation_screens(app):
    with allure.step('Проверка стартового экрана'):
        app.element(text_title).should(have.text('The Free Encyclopedia'))
        app.element(btn_continue).click()
    with allure.step('Проверка перехода к второму экрана'):
        app.element(text_title).should(have.text('New ways to explore'))
        app.element(btn_continue).click()
    with allure.step('Проверка перехода к третьему экрану'):
        app.element(text_title).should(have.exact_text('Reading lists with sync'))
        app.element(btn_continue).click()
    with allure.step('Проверка перехода к четвертому экрана'):
        app.element(text_title).should(have.text('Send anonymous data'))


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты Wikipedia')
@allure.title('Переход на главную по кнопке "skip"')
def test_skip_main_screens(app, skip):
    with allure.step('Проверка отображения главного экрана'):
        app.element(text_main_page).should(have.text('Customize your Explore feed'))


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты Wikipedia')
@allure.title('Результат поиска не пустой')
def test_search(app, skip):
    with allure.step('Переход на экран поиска и ввод искомого значения'):
        app.element(search).click()
        app.element(field_search).type('BrowserStack')
    with allure.step('Проверка результатов поиска'):
        app.all(result_search).should(have.size_greater_than(0))


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты Wikipedia')
@allure.title('Текст ошибки для поля "Пользователь" при вводе невалидного значения')
def test_text_error(app, skip):
    with allure.step('Переход на экран авторизации'):
        app.element(btn_menu).click()
        app.element(menu_item_login).click()
    with allure.step('Ввод невалидного значения в поле "Пользователь"'):
        app.element(field_username).type('***')
    with allure.step('Проверка подсказки при невалидном значении'):
        app.element(text_error).should(
            have.exact_text('The user name "***" is not available. Please choose a different name.'))


@allure.label('owner', 'Александр Санталов')
@allure.feature('Тесты Wikipedia')
@allure.title('Отображение пустого экрана "Сохраненный"')
def test_empty_page(app, skip):
    with allure.step('Переход на экран сохраненные'):
        app.element(widget_saved).click()
        app.element(btn_negative).click()
    with allure.step('Проверка текста при пустом экране'):
        app.element(text_empty).should(have.exact_text('No saved pages yet'))
