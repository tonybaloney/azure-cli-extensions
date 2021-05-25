import git
import pathlib


def init_local_folder(scm_url):
    repo = git.Repo.init(pathlib.Path())
    if len(repo.remotes) == 0:
        repo.create_remote("azure", scm_url)
    else:
        has_remote_configured = False
        for remote in repo.remotes:
            if remote.name == "azure":
                remote.set_url(scm_url)
                has_remote_configured = True
        if not has_remote_configured:
            repo.create_remote("azure", scm_url)

    return
