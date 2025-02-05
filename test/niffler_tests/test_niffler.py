from selene import browser, have, be


#Ввести корректные креды и попасть на главную
def test_succesfull_login():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345')
    browser.element('button[type="submit"]').click()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))

#Авторизоваться с помощью клавиатуры
def test_succesfull_login_with_enter():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))

#Авторизация с некорректными кредами
def test_unsuccesfull_login_with_wrong_credentials():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('123456').press_enter()
    browser.element('[class="form__error"]').should(have.text('Неверные учетные данные пользователя'))

#Проверка имени пользователя в лк (через all)
def test_succesfull_login_check_username_all():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.element('[data-testid="PersonIcon"]').click()
    browser.all('[role="menuitem"]')[0].should(have.text('Profile')).click()
    browser.element('[id="username"]').should(have.value('stas'))

#Проверка имени пользователя в лк (через element)
def test_succesfull_login_check_username_element():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('.link.nav-link').should(have.text('Profile')).click()
    browser.element('[id="username"]').should(have.value('stas'))

    
#Проверка выхода из авторизованной зоны (через all)
def test_succesfull_logout_all():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check logout
    browser.element('[data-testid="PersonIcon"]').click()
    browser.all('[role="menuitem"]')[3].should(have.text('Sign out')).click()
    browser.element('//button[text()="Log out"]').click()
    browser.element('.header').should(be.visible).should(have.text('Log in'))

#Проверка выхода из авторизованной зоны (через element)
def test_succesfull_logout_element():
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check logout
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('ul.MuiList-root.MuiList-padding.MuiMenu-list li:last-child').should(have.text('Sign out')).click()
    browser.element('//button[text()="Log out"]').click()
    browser.element('.header').should(be.visible).should(have.text('Log in'))


