if platform.system().lower() == "windows":
        libs.pop(1)
    else:
        windows = False