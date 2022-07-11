# CodeWorks2022_intro_pyton
This repo is home for all of our projects (including the final project)

All junior developers need to create a github account with their CITS email account and fork this repo.
https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository

There are branches for every week containing all the projects and rubric.

## Cheat Sheet

### linux commandes

- **Change Directory**
  - cd [file name] : moves you to the specified Directory
  - cd .. : moves you back to the parent directory

- **Make Directory**
  - mkdir [new file name]: creates a new directory with the name specified

- **Print Working directory**
  - pwd: lets you see the current directory you are in

- **List Files**
  - ls : lists the files in the current directory
  - ls -la : lists all the files (including hidden ones)
  (for windows cmd it is dir)

- **create a new file**
  - touch [new file name]
  - ex: touch mytext.txt

- **remove**
  - rm [file name]: deletes a file
  - rm -r [directory name]: deletes a folder and everything inside of it.

- **cat** [file name]: lets you see the contents of a file

- **Copy**
  - cp file1 file2: lets you copy the connects of file1 into file2

- **Source**
  - source [file name]: lets you use environment variables form a source file


### git commandes

- **Initializing** an empty git repository
  - *git init*

- **Cloning** a repository
  - *git clone [url of repo to be cloned]*

- **Status** of working tree
  - *git status*

- **Branch**
  - *git branch* lets you see which branch in the repo you're in

- **Change Branch (Checkout)**
  - *git checkout [branch name]* lets you change to the specified branch in the repo

- **Staging** files before commit:
  - *git add [file to be staged]* lets you stage a single file
  - *git add .*  lets you stage all the changed files

- **Commit** all staged files:
  - *git commit -m "Commit message"* lets you commit with a message

- **Push** to remote:
  - *git push*

- **Pull** from remote:
  - *git pull*

- **How do I update or sync a forked repository on GitHub?**

  1. Add the remote, call it "upstream":
    ```shell
    git remote add upstream https://github.com/brookCITS/CodeWorks2022_intro_pyton
    ```

  2. Fetch all the branches of that remote into remote-tracking branches (upstream)
    ```shell
    git fetch upstream
    ```

  3. Make sure that you're on your master branch (or the branch you want to sync)
    ```shell
    git checkout [branch]
    ```

  4. Rewrite your master branch so that any commits of yours that aren't already in upstream/master are replayed on top of that other branch:
    ```shell
    git merge upstream/master
    ```


You may need to force the push in order to push it to your own forked repository on GitHub. You'd do that with:
    ```shell
    git push -f origin master
    ```
    You only need to use the -f the first time after you've rebased.
