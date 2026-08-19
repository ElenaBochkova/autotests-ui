from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Переходим на страницу с курсами
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка “Courses”.
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверяем наличие и текст блока “There is no results”.
    results_empty_section = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_empty_section).to_be_visible()
    expect(results_empty_section).to_have_text('There is no results')

    # Проверяем наличие и видимость иконки 
    results_empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(results_empty_icon).to_be_visible()

    # Проверяем наличие и текст описания блока: Results from the load test pipeline will be displayed here”
    results_empty_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_empty_text).to_be_visible()
    expect(results_empty_text).to_have_text('Results from the load test pipeline will be displayed here')

