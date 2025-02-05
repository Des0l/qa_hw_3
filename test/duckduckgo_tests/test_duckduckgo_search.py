from selene import browser, have


#todo_unsuccessful duckduckgo search
def test_unsuccesfull_duckduckgo_search():
    query = 'ajssdfghhdfsfhhdshfhsdfhdfdhfshsdfhfds'
    browser.element('[role="combobox"]').type(query).press_enter()
    browser.element('.w7syQmNN6Yjvw6guGJuQ').should(have.text(f"По запросу {query} результаты не найдены."))
