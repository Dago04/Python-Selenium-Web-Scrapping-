import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

with open("data.json", 'w') as f:
    json.dump([], f)


def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # first we load existing data into  a dict
        file_data = json.load(file)
        # join new_data with file data inside emp_details
        file_data.append(new_data)

        # sets file's current position at offset
        file.seek(0)

        # convert back to json
        json.dump(file_data, file, indent=4)
# Inicializa el controlador de Selenium


driver = webdriver.Chrome()

# Abre la página web

driver.get("https://www.amazon.com/s?k=gtx+3070&i=computers-intl-ship&crid=31CMKU48OPP55&sprefix=gtx+3070%2Ccomputers-intl-ship%2C118&ref=nb_sb_noss_2")

isNextDisabled = False

while not isNextDisabled:
    try:

        waitPagination = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '//div[@data-component-type="s-search-result"]')))

        element = driver.find_element(
            By.CSS_SELECTOR, 'div.s-main-slot.s-result-list.s-search-results.sg-row')

        items = element.find_elements(
            By.XPATH, '//div[@data-component-type="s-search-result"]')

        for item in items:

            # extraer titulo por el nombre de la etiqueta, en este caso sería h2( se le agrega el .text para extraer el texto de la etiqueta)
            titulo = item.find_element(By.TAG_NAME, 'h2').text
            precio = "No tiene precio"
            # extrer imagen por el css-selector y obtenemos el atributo src
            imagen = item.find_element(
                By.CSS_SELECTOR, '.s-image').get_attribute('src')
            # extraer url de la sección mediante el llamado de la clase y le decimos que queremos el href
            url = item.find_element(
                By.CLASS_NAME, 'a-link-normal').get_attribute('href')

            try:
                precio = item.find_element(
                    By.CSS_SELECTOR, '.a-price').text.replace("\n", ".")
            except:
                pass

            print('Titulo : ' + titulo)
            print('Precio : ' + precio)
            print('URL: ' + url)
            print('URL imagen: '+imagen + '\n')

            write_json({"title": titulo,
                       "precio": precio,
                        "imagen": imagen,
                        "url": url
                        })

        next_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 's-pagination-next')))

        next_class = next_btn.get_attribute('class')

        if "disabled" in next_class:
            isNextDisabled = True

        else:
            driver.find_element(By.CLASS_NAME, 's-pagination-next').click()

    except Exception as e:
        print(e, "Main Error")
        isNextDisabled = True

time.sleep(15)

driver.quit()
