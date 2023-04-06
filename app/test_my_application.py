from playwright.sync_api import Playwright, sync_playwright
# from bs4 import BeautifulSoup
import re

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('https://demo.applitools.com/')
        page.locator('[placeholder="Enter your username"]').fill('demo')
        page.locator('[placeholder="Enter your password"]').fill('demo')
        # page.click('button[type=submit]')
        page.locator('text=Sign in').click()
        # page.click('button >> text=Login')
        print(page.is_visible('div.balance-value.danger'))
        # print(type(html))
        # soup = BeautifulSoup(html, 'html.parser')
        # credit_available = soup.find_all(class_="balance-value danger")
        credit_available = page.locator('[class="balance-value danger"]').all_text_contents()
        # print(len(credit_available))
        # print(f'credit_available= {credit_available}')
        for credit in credit_available:
            print("credit_available= ",credit.strip().split(r'\w+'))
            # print(f'credit_available= {credit.prettify()}')
        # due_today = soup.find_all('div', class_="balance-value danger")
        print(page.is_visible('div.balance-value'))
        due_today = page.locator('[class="balance-value"]').all_text_contents()
        print(type(due_today))
        for txt in due_today:
            print("due_today", txt.strip().split("%")[0])
        print("----------------------------------------------------------")
        # print(page.is_visible('td.nowrap'))
        recent_transactions = page.locator('tr').all_inner_texts()
        # print(len(recent_transactions))
        for transaction in recent_transactions:
            # print(transaction)
            col = transaction.split("   ")
            # print(col)
            for i in range(len(col)):
                col[i] = col[i].split('\t')
                # break
            # col = [x for x in col if x != '']
            col = col[0]
            print(col)
        browser.close()

if __name__=="__main__":
    main()