import argparse

from .commands import install_module, list_modules, module_info, remove_module
from .manager import PackageManager


def main():
    parser = argparse.ArgumentParser(prog="gpm")
    parser.add_argument("command", choices=["list", "install", "remove", "info"])
    parser.add_argument("name", nargs="?")
    arguments = parser.parse_args()
    manager = PackageManager(".")
    if arguments.command == "list":
        print(list_modules(manager))
    elif arguments.command == "install":
        print(manager.preview(arguments.name, "install"))
        if input("Confirmar instalação? [s/N] ").strip().lower() == "s":
            print(install_module(manager, arguments.name))
        else:
            print("Operação cancelada.")
    elif arguments.command == "remove":
        print(manager.preview(arguments.name, "remove"))
        if input("Confirmar remoção? [s/N] ").strip().lower() == "s":
            print(remove_module(manager, arguments.name))
        else:
            print("Operação cancelada.")
    else:
        print(module_info(manager, arguments.name))


if __name__ == "__main__":
    main()