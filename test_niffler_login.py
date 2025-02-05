from selene import browser, have, be


def test_succesfull_login():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345')
    browser.element('button[type="submit"]').click()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_succesfull_login_with_enter():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()

    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    browser.quit()

def test_unsuccesfull_login_with_wrong_credentials():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('123456').press_enter()
    browser.element('[class="form__error"]').should(have.text('Неверные учетные данные пользователя'))
    browser.quit()

def test_succesfull_login_check_username_all():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check username profile
    browser.element('[data-testid="PersonIcon"]').click()
    browser.all('[role="menuitem"]')[0].should(have.text('Profile')).click()
    browser.element('[id="username"]').should(have.value('stas'))
    browser.quit()



def test_succesfull_login_check_username_element():
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check username profile
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('.link.nav-link').should(have.text('Profile')).click()
    browser.element('[id="username"]').should(have.value('stas'))
    browser.quit()
    

def test_succesfull_logout_all():
    browser.config.timeout = 5
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check logout
    browser.element('[data-testid="PersonIcon"]').click()
    browser.all('[role="menuitem"]')[3].should(have.text('Sign out')).click()
    browser.element('//button[text()="Log out"]').click()
    browser.element('.header').should(be.visible).should(have.text('Log in'))
    browser.quit()

def test_succesfull_logout_element():
    browser.config.timeout = 5
    browser.open('https://niffler.qa.guru')
    browser.element('input[name="username"]').type('stas')
    browser.element('input[name="password"]').type('12345').press_enter()
    browser.element('[id="spendings"]').should(have.text('History of Spendings'))
    # todo check logout
    browser.element('[data-testid="PersonIcon"]').click()
    browser.element('ul.MuiList-root.MuiList-padding.MuiMenu-list li:last-child').should(have.text('Sign out')).click()
    browser.element('//button[text()="Log out"]').click()
    browser.element('.header').should(be.visible).should(have.text('Log in'))
    browser.quit()

    # todo unsuccessful yandex search
def test_unsuccessful_yandex_search():
    query = 'adgfoodifgghfdfdoigafdhoidf'
    browser.config.timeout = 5
    browser.open('https://ya.ru ')
    browser.element('#text').type(query).press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))
