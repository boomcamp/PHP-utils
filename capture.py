import os
import asyncio
from pyppeteer import launch

host = "http://localhost:8000/pulls/"

async def main(hosts,locations):
	"""
	A function that create screenshots and store to captures/ folder
	"""

	browser = await launch()
	page = await browser.newPage()
	await page.goto(hosts)
	await page.screenshot({'path': locations})
	await browser.close()

for directories in os.listdir("pulls"):

	screenshot = 'captures/'+directories+'.png'
	path = host+directories
	print("Creating screenshot.." + screenshot)
	asyncio.get_event_loop().run_until_complete(main(path,
	screenshot))
	print("Done.")

