def kernel_status():
    return "Online"


def builder_status():
    return "Pronto"


def system_status():
    return {"kernel": kernel_status(), "builder": builder_status()}