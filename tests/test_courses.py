from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage, CheckVisibleCourseCardParams
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage,
                       courses_list_page: CoursesListPage):

    # Переходим на страницу создания нового курса
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    # Параметры для нового курса
    course_title = 'Playwright'
    course_estimated_time = '2 weeks'
    course_description = 'Playwright'
    course_max_score = '100'
    course_min_score = '10'

    # Проверки состояния страницы создания курса при первом открытии
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(title='',
                                                        description='',
                                                        estimated_time='',
                                                        max_score='0',
                                                        min_score='0'
                                                        )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    # Загрузка изображения
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)

    # Заполнение формы курса
    create_course_page.fill_create_course_form(title=course_title,
                                               estimated_time=course_estimated_time,
                                               description=course_description,
                                               max_score=course_max_score,
                                               min_score=course_min_score
                                               )
    create_course_page.click_create_course_button()

    # Проверяем список курсов после создания курса
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()

    # Проверяем, что созданный курс отображается
    params = CheckVisibleCourseCardParams(index=0,
                                          title=course_title,
                                          max_score=course_max_score,
                                          min_score=course_min_score,
                                          estimated_time=course_estimated_time
                                          )
    courses_list_page.check_visible_course_card(params=params)


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
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

