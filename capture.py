from github import Github
import git
import os
import asyncio
from pyppeteer import launch

# Setup env variables
host = "http://localhost:8000/pulls/"
user = os.getenv('USER', 'User Not found')
password = os.getenv('PASSWORD', 'Password Not found')
repository = os.getenv('REPO', 'Repo Not found')


async def screenshot(directories,destination):
	"""
	A function that creates screenshots and store to captures/ folder
	"""
	browser = await launch()
	page = await browser.newPage()
	await page.goto(directories)
	await page.screenshot({'path': destination})
	await browser.close()


async def main() :
	"""
	This function will clone forked students submission branches 
	"""

	g = Github(user, password)
	repo = g.get_repo(repository)
	cwd = os.getcwd()

	forks = repo.get_forks()
	for fork in forks:
		sub_repo = g.get_repo(fork.full_name)
		branches = sub_repo.get_branches()
		for branch in branches :
			if(branch.name == 'submission'):
				spllt = fork.full_name
				print("cloning.. " + fork.full_name, branch.name)
				os.mkdir("pulls/"+spllt.split("/")[0])
				repo = git.Repo.clone_from(
				    "git@github.com:"+fork.full_name+".git",
				    "pulls/"+spllt.split("/")[0],
				    branch='submission'
				)
				print("Creating screenshot.."+spllt.split("/")[0])
				storage = 'captures/'+spllt.split("/")[0]+'.png'
				await screenshot(host+spllt.split("/")[0],storage)
				print("Done.")


if __name__ == "__main__":
	asyncio.get_event_loop().run_until_complete(main())