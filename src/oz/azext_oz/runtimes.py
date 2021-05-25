from azure.cli.command_modules.appservice.custom import list_runtimes_hardcoded


RUNTIME_GROUPS = [
    "python",
    "ruby",
    "node",
    "dotnet"
]


def get_runtime_versions(runtime):
    # Gives list like ["PYTHON|3.8", "NODE|14"]
    plat_runtimes = list_runtimes_hardcoded(linux=True)
    return [choice.split('|')[1] for choice in plat_runtimes if choice.startswith(runtime.upper())]


def map_version_dict(runtime, version):
    # TODO : Review what is missing.
    if runtime == "python":
        return {"python_version": version}
    elif runtime == "ruby":
        return {"ruby_version": version}
    elif runtime == "dotnet":
        return {"dotnet_version": version}
    elif runtime == "node":
        return {"node_version": version}
    elif runtime == "java":
        return {"java_version": version}
    else:
        return {}
