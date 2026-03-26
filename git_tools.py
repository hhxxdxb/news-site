# git_tools.py
import git
import os

def git_add(repo_path, filepath):
    """添加文件到暂存区"""
    repo = git.Repo(repo_path)
    repo.index.add([filepath])

def git_commit(repo_path, message):
    """提交暂存区"""
    repo = git.Repo(repo_path)
    repo.index.commit(message)

def git_push(repo_path):
    """推送到远程仓库"""
    repo = git.Repo(repo_path)
    origin = repo.remote(name='origin')
    origin.push()