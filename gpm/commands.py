def list_modules(manager):
    return manager.list()


def install_module(manager, name):
    return manager.install(name)


def remove_module(manager, name):
    return manager.remove(name)


def module_info(manager, name):
    return manager.info(name)