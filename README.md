# 🚀 Coursera Course Scraper (Selenium + Python)
A Python scraper using Selenium to extract courses from Coursera and save them to a CSV file.

## 🌟 Features
- Searches for **Machine Learning** courses (default, but can be modified).
- Filters by **Data Science** and **English** (more filters can be added).
- Extracts **course name, institute, rating, reviews, skills, level, type, and duration**.
- Saves data to **courses.csv**.

## 🔧 Requirements
- **Python 3.x**
- **Selenium**
- **Chrome WebDriver**

## 📥 Installation
Clone the repository:
```sh
git clone https://github.com/raya-rich/Coursera-Course-Scraper.git
cd Coursera-Course-Scraper

Install dependencies:
```sh
pip install selenium  
pip install webdriver-manager
```
Or download and place chromedriver.exe in the project folder.

## ▶️ Usage
Run the script:
```sh
python scrape.py  
```
## 📂 Output
- Course Name
- Institute Name
- Rating
- Reviews
- Skills
- Level
- Course Type
- Duration
