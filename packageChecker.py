'''
This app checks wich packages are installed
'''
import pkg_resources

installed_packages = list(pkg_resources.working_set)
for package in installed_packages:
    print(package.project_name, package.version)
