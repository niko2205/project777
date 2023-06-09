from selenium import webdriver

def test_loan_calculator():
    # Запустить приложение
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8501")
    
    # Ввести данные в форму
    age_input = driver.find_element_by_name("Возраст")
    age_input.send_keys("30")
    
    gender_select = driver.find_element_by_name("Пол")
    gender_select.click()
    male_option = gender_select.find_element_by_xpath("//option[text()='Мужской']")
    male_option.click()
    
    citizenship_select = driver.find_element_by_name("Гражданство")
    citizenship_select.click()
    russia_option = citizenship_select.find_element_by_xpath("//option[text()='Россия']")
    russia_option.click()
    
    income_input = driver.find_element_by_name("Зарплата")
    income_input.send_keys("50000")
    
    employment_select = driver.find_element_by_name("Статус занятости")
    employment_select.click()
    employed_option = employment_select.find_element_by_xpath("//option[text()='Работаю']")
    employed_option.click()
    
    marital_select = driver.find_element_by_name("Семейное положение")
    marital_select.click()
    married_option = marital_select.find_element_by_xpath("//option[text()='Женат/Замужем']")
    married_option.click()
    
    children_input = driver.find_element_by_name("Количество детей")
    children_input.send_keys("0")
    
    # Нажать на кнопку "Рассчитать кредит"
    calculate_button = driver.find_element_by_css_selector(".css-18yo9w8")
    calculate_button.click()
    
    # Проверить, что результат выведен на странице
    result_text = driver.find_element_by_css_selector(".css-hi6a2p").text
    assert "Предполагаемая сумма кредита:" in result_text
    
    # Закрыть браузер
    driver.quit()
