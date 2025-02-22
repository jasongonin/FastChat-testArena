import subprocess

def uninstall_packages():
    # Get the list of installed packages
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
    packages = result.stdout.decode('utf-8').split('\n')

    for package in packages:
        if package:
            # Uninstall each package
            subprocess.run(['pip', 'uninstall', '-y', package])

if __name__ == "__main__":
    uninstall_packages()
