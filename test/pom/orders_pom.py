import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HeaderOrderPom:
    driver = None

    pop_up_agreement_cookies = [By.ID, 'rcc-confirm-button']
    order_button_header = [By.CLASS_NAME, 'Button_Button__ra12g']
    input_name = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/input']
    input_surname = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/input']
    input_address = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[3]/input']
    choose_station_metro = [By.CLASS_NAME, 'select-search__value']
    station_metro = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button']
    input_phone_number = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[5]/input']
    next_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button']
    when_to_bring_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[1]/div/input']
    input_when_to_bring_scooter = [By.XPATH,
                                   '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[6]/div[1]']
    rental_period = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div/div[1]']
    input_rental_period = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/div[2]/div[2]']
    color_of_scooter = [By.XPATH, '//*[@id="black"]']
    order_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']
    yes_button = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]']
    order_processed = [By.CLASS_NAME, 'Order_Modal__YZ-d3']
    order_processed_text = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
    order_button_not_header = [By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button']
    logo_yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    redirect_yandex_ru = 'https://dzen.ru/?yredirect=true'
    dzen_content_div = [By.CLASS_NAME, 'content']

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Принимаем куки')
    def accept_cookie(self):
        self.driver.find_element(*self.pop_up_agreement_cookies).click()

    @allure.step('Жмакаем на кнопку "Заказать" в хедере ')
    def click_order_button_header(self):
        self.driver.find_element(*self.order_button_header).click()

    @allure.step('Жмакнуть на инпут ввода имени')
    def find_element_and_click_input_name(self):
        self.driver.find_element(*self.input_name).click()

    @allure.step('Ввести имя в инпут')
    def input_name_in(self):
        self.driver.find_element(*self.input_name).send_keys("Катрин")

    @allure.step('Жмакнуть на инпут ввода фамилии')
    def find_element_and_click_input_surname(self):
        self.driver.find_element(*self.input_surname).click()

    @allure.step('Ввести фамилию в инпут')
    def input_surname_in(self):
        self.driver.find_element(*self.input_surname).send_keys("Заидова")

    @allure.step('Жмакнуть на инпут ввода адреса')
    def find_element_and_click_input_address(self):
        self.driver.find_element(*self.input_address).click()

    @allure.step('Ввести адрес в инпут')
    def input_address_in(self):
        self.driver.find_element(*self.input_address).send_keys("Стремянный 17")

    @allure.step('Жмакнуть на выбор метро')
    def find_and_click_metro_station(self):
        self.driver.find_element(*self.choose_station_metro).click()

    @allure.step('Подождать отображения списка метро')
    def wait_before_choose_station(self):
        WebDriverWait(self.driver, 2).until(expected_conditions.visibility_of_element_located(self.station_metro))

    @allure.step('Выбрать станцию метро')
    def click_on_metro_station(self):
        self.driver.find_element(*self.station_metro).click()

    @allure.step('Жмакнуть на инпут нмоера телефона')
    def find_and_click_phone_number(self):
        self.driver.find_element(*self.input_phone_number).click()

    @allure.step('Ввести номер телефона')
    def input_phone_number_in(self):
        self.driver.find_element(*self.input_phone_number).send_keys("79180657848")

    @allure.step('Жмакнуть на кнопку "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    @allure.step('Жмакнуть на выбор даты доставки')
    def find_and_click_when_to_bring_scooter(self):
        self.driver.find_element(*self.when_to_bring_scooter).click()

    @allure.step('Выбрать дату доставки')
    def choose_when_to_bring_scooter(self):
        self.driver.find_element(*self.input_when_to_bring_scooter).click()

    @allure.step('Жмакнуть на выбор периода аренды')
    def find_and_click_rental_period(self):
        self.driver.find_element(*self.rental_period).click()

    @allure.step('Выбрать период аренды')
    def choose_rental_period(self):
        self.driver.find_element(*self.input_rental_period).click()

    @allure.step('Выбрать цвет самоката')
    def choose_color_of_scooter(self):
        self.driver.find_element(*self.color_of_scooter).click()

    @allure.step('Жмакнуть на кнопку "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step('Подтвердить заказ')
    def click_yes_button(self):
        self.driver.find_element(*self.yes_button).click()

    @allure.step('Подождать пока появится баннер с успешным заказом')
    def wait_to_proceed_banner(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_processed))

    @allure.step('Жмакнуть на лого Яндекса')
    def click_on_yandex_logo(self):
        self.driver.find_element(*self.logo_yandex).click()

    @allure.step('Жмакнуть на лого Самоката')
    def click_on_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    @allure.step('Получение текста заказа')
    def order_get_text(self):
        return self.driver.find_element(*self.order_processed_text).text

    @allure.step('Жмакнуть на кнопку "Заказать" в теле сайта')
    def click_on_button_order(self):
        self.driver.find_element(*self.order_button_not_header).click()

    @allure.step('Подождать пока увидим страничку дзена')
    def wait_to_open_dzen_window(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.dzen_content_div))

    @allure.step('Получение текущей ссылки')
    def current_url(self):
        return self.driver.current_url

    def order_from_header_button(self):
        self.click_order_button_header()
        self.find_element_and_click_input_name()
        self.input_name_in()
        self.find_element_and_click_input_surname()
        self.input_surname_in()
        self.find_element_and_click_input_address()
        self.input_address_in()
        self.find_and_click_metro_station()
        self.wait_before_choose_station()
        self.click_on_metro_station()
        self.find_and_click_phone_number()
        self.input_phone_number_in()
        self.click_next_button()
        self.find_and_click_when_to_bring_scooter()
        self.choose_when_to_bring_scooter()
        self.find_and_click_rental_period()
        self.choose_rental_period()
        self.choose_color_of_scooter()
        self.click_order_button()
        self.click_yes_button()
        self.wait_to_proceed_banner()

    def order_from_button(self):
        self.click_on_button_order()
        self.find_element_and_click_input_name()
        self.input_name_in()
        self.find_element_and_click_input_surname()
        self.input_surname_in()
        self.find_element_and_click_input_address()
        self.input_address_in()
        self.find_and_click_metro_station()
        self.wait_before_choose_station()
        self.click_on_metro_station()
        self.find_and_click_phone_number()
        self.input_phone_number_in()
        self.click_next_button()
        self.find_and_click_when_to_bring_scooter()
        self.choose_when_to_bring_scooter()
        self.find_and_click_rental_period()
        self.choose_rental_period()
        self.choose_color_of_scooter()
        self.click_order_button()
        self.click_yes_button()
        self.wait_to_proceed_banner()

    def url_from_logo_yandex(self):
        self.click_on_yandex_logo()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_to_open_dzen_window()

    def url_from_logo_scooter(self):
        self.click_on_button_order()
        self.click_on_logo_scooter()
