from os import times
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
import csv

chrome_driver_path = "D:\\Program Files\\chromedriver\\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.coursera.org/")
time.sleep(2)

# search for "machine learning"
driver.find_element(By.XPATH, "//input[@placeholder='What do you want to learn?']").send_keys("machine learning")
time.sleep(2)

# click on "machine learning"
driver.find_element(By.XPATH, "//span[@class='item-name body-1-text' and text()='machine learning']").click()
time.sleep(2)

# wait and click on "Data Science"
WebDriverWait(driver, 50).until(
    EC.element_to_be_clickable((By.XPATH, "//span[text()='Data Science']"))
).click()
time.sleep(2)

# click on "English"
driver.find_element(By.XPATH, "//span[text()='English']").click()
time.sleep(2)

beginner_option = driver.find_element(By.XPATH, "//span[text()='Beginner']")
driver.execute_script("arguments[0].scrollIntoView();", beginner_option)
beginner_option.click()
time.sleep(2)


# scroll down multiple times to load more courses
for _ in range(500):
    driver.execute_script("window.scrollBy(0,500);")
    time.sleep(3)


WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'css-16m4c33')]")))


# find all course elements
courses = driver.find_elements(By.XPATH, "//div[contains(@class,'css-16m4c33')]")
print(f"Total courses found: {len(courses)}")

# CSV header
data = [["Course Name", "Institute Name", "Rating", "Reviews", "Skills", "Level", "Course Type", "Duration"]]

# helper function to get text safely
def get_text(element, xpath):
    try:
        return element.find_element(By.XPATH, xpath).text.strip()
    except:
        return "N/A"

# helper function to get attribute safely
def get_attribute(element, xpath, attribute):
    try:
        return element.find_element(By.XPATH, xpath).get_attribute(attribute)
    except:
        return "N/A"

for course in courses:
    course_name = get_text(course, ".//h3[contains(@class, 'cds-CommonCard-title')]")
    institute_name = get_text(course, ".//p[contains(@class, 'cds-ProductCard-partnerNames')]")
    rating = get_attribute(course, ".//div[@role='meter']", "aria-valuenow")
    reviews = get_text(course, ".//div[contains(@class, 'css-vac8rf')]")
    skills = get_text(course, ".//p[@class='css-vac8rf']")
    details = get_text(course, ".//div[contains(@class, 'cds-CommonCard-metadata')]//p[contains(@class, 'css-vac8rf')]")

    level, course_type, duration = "N/A", "N/A", "N/A"
    
    if details and details != "N/A":
        parts = details.split(" · ")
        level = parts[0] if len(parts) > 0 else "N/A"
        course_type = parts[1] if len(parts) > 1 else "N/A"
        duration = parts[2] if len(parts) > 2 else "N/A"

    if course_name != "N/A":
        data.append([course_name, institute_name, rating, reviews, skills, level, course_type, duration])

# write data to CSV
with open("courses.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file saved successfully!")


# helper functions
def get_text(element, xpath):
    try:
        return element.find_element(By.XPATH, xpath).text.strip()
    except Exception:
        return "N/A"  # return "N/A" if element not found

def get_attribute(element, xpath, attribute):
    try:
        return element.find_element(By.XPATH, xpath).get_attribute(attribute).strip()
    except Exception:
        return "N/A"
    
