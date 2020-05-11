# How to contribute to Fagrimacs

## Set up working copy of fagrimacs repo in your computer

Firstly, you need a local copy of the project. Press the "fork" button in Github to create a copy of the repository in your own Github account.

Now go ahead and create a local copy, find the "SSH clone URL" at your dashboard in the right hand column of repo you forked and use that to clone locally using the terminal:

```
git clone https://github.com/<username>/fagrimacs.git
```

After cloning the repository, now change into the new project's directory:

```
cd fagrimacs
```

Set up a new remote that points to the original project so that you can grab any changes and bring them into your local copy.

```
git remote add upstream https://github.com/fagrimacs/fagrimacs.git
```

Now you have two remotes for this project:

- _origin_ which points to your Github fork of the project. You can read and write to this remote.
- _upstream_ which point to the main project's Github repository. You can only read from this remote.

You can check them using the command:

```
git remote -v
```

## Get it working on your computer

This project comprise 3 requirements files

- requirements.txt - This file contains the packages that are required both in development and production.
- requirements-dev.txt - This file contains the packages that are required in development.
- requirements-prod.txt - This file contains the packages that are required in production.

To run the project locally..

### Create Virtual environment for the project, activate and install packages

In Windows
```python
virtualenv venv

venv\scripts\activate

pip install -r requirements-dev.txt
```

## Do some work

Pick up an issue, reproduce it on your version. Once you have reproduced it, read the code to work out where the problem is. Once you've found the code problem, you can move on to fixing it.

If it's addition of feature, go on write the code for the particular feature.

> **For each issue/feature you are working on make sure to create a branch for it.**

First, make sure you are in a master branch

```
git checkout master
```
Sync your local copy with the upstream project

```
git pull upstream master
```
Then sync it to your forked Github project

```
git push origin master
```

Now you can create a branch on which you will work on.

```
git checkout -b <branch-name>
```

> **Ensure that you only fix the thing you're working on. Do not be tempted to fix some other things that you see along the way, including formatting issues, as your Pull Request (PR) will probably be rejected.**

Make sure you commit in logical blocks. Each commit message should be sane. Check this [link to commit messages article]().

# Create the Pull Request (PR)

Create a PR by pushing your branch to the _origin_ remote and then press some buttons on Github.

To push new branch:
```
git push -u origin <branch-name>
```

This will create the branch on your Github project.

Swap back to the browser and navigate to your fork of the project `https://github.com/<username>/fagrimacs.git` and you'll see that your new branch is listed at the top with a handy "Compate & pull request button". Get ahead and press the button.

Ensure you provide a good, succint title for your pull request and explain why you have created in the in the description box. Add any relevant issue numbers if you have them.

# Review by the maintainers

For your work to be integrated into the project, the maintainer will review your work and either request changes or merge it.

# What next?

Once your PR has been merged, you can delete your branch. Firstly update your master with the changes from maintainers:

```
git checkout master
git pull upstream master
git push origin master
```

You can now delete your branch:

```
git branch -d <branch-name>
git push origin --delete <branch-name>
```

You now have a latest version of the code, so for your next change you can start again at creating new branch.

```
git checkout master
git pull upstream master
git push origin master
git checkout -b <new-branch-name>
```
and away you go making the changes required.

## Attribution

This guide is adopted from [Rob Allen](https://akrabat.com/the-beginners-guide-to-contributing-to-a-GitHub-project)