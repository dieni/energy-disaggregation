# energy
A tailored energy saving recommendation web service using disaggregation methods on smartmeter data.

# Introduction
Below are some guidelines for working together on this project and instructions for running the project on your computer.

## Git Guidelines/Procedure for Development
For the first time you will have to clone the git project to your local filesystem by using "git clone git@github.com:dieni/energy.git". If you have done it already just proceed to the next steps. 

1. Use the already created branch for your feature by using "git checkout your_feature_branch_name" HINT: you can see the available branches by clicking on the branch button
2. After you have written your code and tested it do the following: 
  - "git add ." (adds all files to the stage)
  - "git status"(to check if everything has been added)
  - "git commit -m "Description_of_this_commit"
  - "git push origin your_feature_branch_name" (pushes your commit to remote)
3. "git fetch" (updates references to remote changes)
4. Merge your Changes into Master branch by using:
  - "git checkout master"
  - "git merge your_feature_branch_name"
  - "git push origin master"

