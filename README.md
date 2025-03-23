📌 Coursera Course Scraper (Selenium + Python)
A Python scraper using Selenium to extract courses from Coursera and save them to a CSV file.

🚀 Features
Searches for Machine Learning courses (default, but can be modified)
Filters by Data Science and English (more filters can be added)
Extracts course name, institute, rating, reviews, skills, level, type, and duration
Saves data to courses.csv

🛠️ Requirements
Python 3.x
Selenium
Chrome WebDriver

⚙️ Installation
Clone the repository:
git clone https://github.com/raya-rich/Coursera-Course-Scraper.git
cd Coursera-Course-Scraper

Install dependencies:
pip install selenium
pip install webdriver-manager
or
Download and place chromedriver.exe in the project folder

▶️ Usage
Run the script:
python scrape.py

📂 Output
Courses are saved in courses.csv with columns:
Course Name
Institute Name
Rating
Reviews
Skills
Level
Course Type
Duration
