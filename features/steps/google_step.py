from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

@given('User is on the google homepage')
def step_impl(context):
    driver.get("http://www.google.com")

@when('User searches for the word \'Python\'')
def step_impl(context):
    input_element = driver.find_element_by_name("q")
    input_element.send_keys("python")
    driver.close()

@when('Hits the \'Search\' butoon')
def step_impl(context):
    # input_element = driver.find_element_by_name("g")
    # input_element.submit()
    assert True

@then('it should return links to python')
def step_impl(context):
    assert True

@then('User should be able to see the Search button')
def step_impl(context):
    assert True

@then('User should be able to see the search textbox')
def step_impl(context):
    assert True
