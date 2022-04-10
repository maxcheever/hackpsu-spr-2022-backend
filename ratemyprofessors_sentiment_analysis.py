from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import ratemyprofessor

names = ['Abutalib Aghayev', 'Mohamed Almekkawy', 'Erin Ammerman', 'Kultegin Aydin', 'Katelen Bair', 'Jesse Barlow', 'Sven Bilén', 'Antonio Blanca Pimentel', 'Megan Bowersox', 'James Breakall', 'Viveck Cadambe', 'Sawyer Campbell', 'Guohong Cao', 'Nilanjan Ray Chaudhuri', 'Kyusun Choi', 'Roger Christman', 'Rongming Chu', 'Amanda Collins',
         'Robert Collins', 'David Cubanski', 'Daniel Cullina', 'Alyshia Dann', 'Chitaranjan Das', 'Debarati Das', 'John Doherty', 'Taylor Doksa', 'John Domico', 'Donald Ebeigbe', 'Aida Ebrahimi', 'Olivia Ewing', 'Tammy Falls', 'Mahfuza Farooque', 'Junichiro Fukuyama', 'Martin Furer', 'Oren Gall', 'Mariah Germello', 'Swaroop Ghosh', 'Chris Giebink']

for name in names:
    professor = ratemyprofessor.get_professor_by_school_and_name(
        ratemyprofessor.get_school_by_name("Penn State University"), name)
    if(professor):
        print(professor.name)
