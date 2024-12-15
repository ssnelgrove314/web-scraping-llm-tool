import selenium
import requests
import bs4

def identify_site_structure(entry_page_url):
    """
    The entry point for the web scraper.
    Visits the site, takes a few photos, downloads the soup and identifies
    if the site is static or dynamic, requires login, or has bot protection.
    """
    soup = get_site_soup(entry_page_url)
    images = take_photos(entry_page_url)
    has_login = check_for_login(soup, images)
    is_dynamic = check_for_dynamic(soup, images)
    has_bot_protection = check_for_bot_protection(soup, images)
    site_structure = {
        'url': entry_page_url,
        'soup': soup,
        'images': images,
        'has_login': has_login,
        'is_dynamic': is_dynamic,
        'has_bot_protection': has_bot_protection
    }
    return site_structure

def get_site_soup(url):
    """
    Downloads the HTML of the site and returns a BeautifulSoup object.
    """
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

def take_photos(url):
    """
    Takes a few photos of the site and saves them to the database.
    """
    pass

def check_for_login(soup, images):
    """
    Checks if the site requires login.
    """
    pass

def check_for_dynamic(soup, images):
    """
    Checks if the site is dynamic.
    """
    pass

def check_for_bot_protection(soup, images):
    """
    Checks if the site has bot protection.
    """
    pass
    

    