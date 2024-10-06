from playwright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://rco.paas.pr.gov.br/")
        await page.click("text=Central de Segurança")  # Clica no botão pelo texto
        await page.wait_for_selector('#attribute_central')
        # FAZER UM SISTEMA ONDE O USUÁRIO DIGITE O CPF E SENHA
        await page.fill('#attribute_central', "") #CPF 
        await page.wait_for_selector('#password')
        await page.fill('#password', "")  #SENHA
        await page.click("#btn-central-acessar")
      
        await browser.close()

# Loop asyncio
asyncio.run(main())
