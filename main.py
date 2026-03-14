from fastapi import FastAPI
from playwright.async_api import async_playwright

app = FastAPI()

@app.get("/get-h2")
async def get_h2():

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        page = await browser.new_page()
        await page.goto("https://www.yr.no/en")

        h2_texts = await page.locator("h2").all_inner_texts()

        await browser.close()

    return {"h2": h2_texts}
