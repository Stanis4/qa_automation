import platform


def allure_os_properties():
    # Retrieve system information
    os_platform = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    python_version = platform.python_version()

    # Define the properties to be written to the file
    properties = f"""
    os_platform = {os_platform}
    os_release = {os_release}
    os_version = {os_version}
    python_version = {python_version}
    """

    # Write to the environment.properties file
    with open('..\\tests\\allure-results\\environment.properties', 'w') as file:
        file.write(properties)

