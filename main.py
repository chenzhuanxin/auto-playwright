from playwright.sync_api import sync_playwright
import datetime
import os

def run():
    print(f"--- 任务开始执行，当前时间: {datetime.datetime.now()} ---")
    
    # 启动无头浏览器
    with sync_playwright() as p:
        # headless=True 表示无界面模式，适合云端运行
        browser = p.chromium.launch(headless=True) 
        page = browser.new_page()
        
        # 访问网页
        page.goto("https://www.baidu.com")
        
        # 获取并打印网页标题
        title = page.title()
        print(f"成功获取网页标题: {title}")
        
        # 截图保存
        page.screenshot(path="baidu_screenshot.png")
        print("截图已保存为 baidu_screenshot.png")
        
        browser.close()
        
    print("--- 任务执行完毕 ---")

if __name__ == "__main__":
    run()
