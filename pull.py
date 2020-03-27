from github import Github
import git
import os
import asyncio

user = os.getenv('USER', 'User Not found')
password = os.getenv('PASSWORD', 'Password Not found')
repository = os.getenv('REPO', 'Repo Not found')

async def pull() :
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
				print("Done.")


asyncio.get_event_loop().run_until_complete(pull())