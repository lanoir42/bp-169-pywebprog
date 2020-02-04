from selenium import webdriver
import os


def test_project():
    test_file_dir = os.path.dirname(
        os.path.abspath(__file__)
    )
    proj_dir = os.path.dirname(test_file_dir)
    repo_dir = os.path.dirname(proj_dir)
    driver_path = os.path.join(repo_dir, 'bin', 'chromedriver')
    browser = webdriver.Chrome(
        executable_path=driver_path,
    )
    browser.get("http://localhost:8000")
    assert 'Django' in browser.title
