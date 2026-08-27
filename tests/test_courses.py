from playwright.sync_api import expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
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
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_form.check_visible(title='',
                                                        description='',
                                                        estimated_time='',
                                                        max_score='0',
                                                        min_score='0'
                                                        )
    create_course_page.create_course_exercise_toolbar.check_visible()
    create_course_page.check_visible_exercises_empty_view()

    # Загрузка изображения
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)

    # Заполнение формы курса
    create_course_page.create_course_form.fill(title=course_title,
                                               estimated_time=course_estimated_time,
                                               description=course_description,
                                               max_score=course_max_score,
                                               min_score=course_min_score
                                               )
    create_course_page.create_course_toolbar.click_create_course_button()

    # Проверяем список курсов после создания курса
    courses_list_page.toolbar_view.check_visible()

    # Проверяем, что созданный курс отображается
    courses_list_page.course_view.check_visible(index=0,
                                                title=course_title,
                                                max_score=course_max_score,
                                                min_score=course_min_score,
                                                estimated_time=course_estimated_time
    )


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    # Переходим на страницу с курсами
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем отображение и содержимое Navbar и Sidebar
    courses_list_page.navbar.check_visible(username='username')
    courses_list_page.sidebar.check_visible()

    courses_list_page.toolbar_view.check_visible()

    # Проверяем наличие и содержимое пустого блока с курсами.
    courses_list_page.check_visible_empty_view()


