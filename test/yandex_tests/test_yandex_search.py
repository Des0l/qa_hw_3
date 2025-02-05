from selene import browser, have
from time import sleep


#todo_unsuccessful yandex search
def test_unsuccesfull_yandex_search():
    query = 'ajsdajlsdlklkdjkdaslkdjasdl'
    sleep(10)  #костыль, тест не роняется, есть время решить капчу, если она появилась
    browser.element('#text').type(query).press_enter()
    browser.element('.EmptySearchResults-Title').should(have.text('Ничего не нашли'))



