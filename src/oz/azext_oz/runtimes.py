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
