## 将旧的git贡献者改为新的贡献者

1. 将changename.sh拷贝到本仓库根目录下
2. git pull 保持自己的代码为最新的提交
3. 修改changename.sh中的oldname和newname,newemail等
4. sh changename.sh
5. git push


### COMMITER

如果修改成功提示:Ref 'refs/heads/master' was rewritten.

如果修改失败提示:Ref 'refs/heads/master' is unchanged.这里可能是因为你填写的oldName并没有找到.

如果无差别把所有都改的话去掉if..fi

'''
git filter-branch -f --env-filter "
GIT_AUTHOR_NAME='newName';
GIT_AUTHOR_EMAIL='newEmail';
GIT_COMMITTER_NAME='newName';
GIT_COMMITTER_EMAIL='newEmail'
" HEAD
'''

### CAUTIONS

你这里将你本地git的账户和邮箱重新设置了,但是github并没有那么智能就能判断你是原来你系统默认的用户.

也就是说你新配置的用户和你默认的被github识别成两个用户.

这样你以后操作的时候commit 或者 push的时候有可能产生冲突.

```
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:blurty/algorithms.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

### SOLUTION

	1.使用强制push的方法：

	$ git push -u origin master -f
	这样会使远程修改丢失，一般是不可取的，尤其是多人协作开发的时候。

	我这里只是自己写的博客,所以就直切全部强制覆盖掉了.

	2.push前先将远程repository修改pull下来

	git pull origin master
	git push -u origin master

	3.若不想merge远程和本地修改，可以先创建新的分支：

	git branch [name]
	然后push

	git push -u origin [name]
