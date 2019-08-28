#!/bin/bash
git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_NAME" = "fuhongbo" ]
then
export GIT_AUTHOR_NAME="blurty"
export GIT_AUTHOR_EMAIL="fuhongbofhb@163.com"
fi
' HEAD
 
git filter-branch -f --env-filter '
if [ "$GIT_COMMITTER_NAME" = "fuhongbo" ]
then
export GIT_COMMITTER_NAME="fuhongbo"
export GIT_COMMITTER_EMAIL="fuhongbofhb@163.com"
fi
' HEAD
