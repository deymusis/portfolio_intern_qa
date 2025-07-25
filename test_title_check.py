from playwright.sync_api import sync_playwright

# Ожидаемый заголовок страницы
EXPECTED_TITLE = "Fast and reliable end-to-end testing for modern web apps | Playwright"

def run_test_in_browser(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=True)
        page = browser.new_page()
        page.goto("https://playwright.dev/")
        actual_title = page.title()
        assert actual_title == EXPECTED_TITLE, f"{browser_name}: Заголовок не совпадает"
        print(f"[OK] {browser_name}: Заголовок корректен.")
        browser.close()

def main():
    for browser in ["chromium", "firefox"]:
        run_test_in_browser(browser)

if __name__ == "__main__":
    main()
