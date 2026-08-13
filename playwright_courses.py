from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    #Сохраняем контекст
    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу с заранее созданным контекстом
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json") # Указываем файл с сохраненным состоянием
    page = context.new_page()

    # Переходим на страницу с курсами
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка “Courses”.
    courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    # Проверяем наличие и текст блока “There is no results”.
    results_empty_section = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(results_empty_section).to_be_visible()
    expect(results_empty_section).to_have_text('There is no results')

    # Проверяем наличие и видимость иконки 
    results_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(results_empty_icon).to_be_visible()

    # Проверяем наличие и текст описания блока: Results from the load test pipeline will be displayed here”
    results_empty_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(results_empty_text).to_be_visible()
    expect(results_empty_text).to_have_text('Results from the load test pipeline will be displayed here')

