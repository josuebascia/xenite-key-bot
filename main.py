from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import requests
import os

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def complete_quests():
    driver = get_driver()
    try:
        print("🌐 Apertura pagina bstlar...")
        driver.get("https://bstlar.com/4GA/xenitemainkey")
        time.sleep(random.uniform(4, 8))
        
        for i in range(4):
            print(f"⚡ Quest {i+1}/4 in esecuzione...")
            time.sleep(random.uniform(12, 28))  # Tempo per ads/quest
            
            try:
                # Clicca su qualsiasi pulsante visibile di continuazione
                buttons = driver.find_elements(By.XPATH, "//button | //a[contains(@class, 'btn') or contains(text(), 'Continue') or contains(text(), 'Next') or contains(text(), 'Claim')]")
                for btn in buttons:
                    if btn.is_displayed() and btn.is_enabled():
                        driver.execute_script("arguments[0].scrollIntoView();", btn)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", btn)
                        break
            except:
                pass
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        
        time.sleep(6)
        # Estrai key (adatta se necessario)
        key = None
        try:
            elements = driver.find_elements(By.XPATH, "//*[contains(text(), '0') and string-length(text()) >= 30]")
            for el in elements:
                text = el.text.strip()
                if len(text) == 32 and all(c in "0123456789abcdefABCDEF" for c in text):
                    key = text
                    break
        except:
            pass
        
        if key:
            print(f"✅ KEY GENERATA: {key}")
            send_notification(key)
            return key
        else:
            print("❌ Key non trovata questa volta")
            return None
    finally:
        driver.quit()

def send_notification(key):
    # Telegram (consigliato)
    token = os.getenv("TELEGRAM_TOKEN", "8995788735:AAFHc2abMiK6DL3P3CE6ZDcOXPOIKRJQpTY")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "7410616401")
    if token and chat_id:
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=Nuova%20Xenite%20Key:%20{key}")
        except:
            pass

if __name__ == "__main__":
    while True:
        complete_quests()
        print("⏳ Prossimo ciclo tra 5.5 ore...")
        time.sleep(19800)  # 5.5 ore
