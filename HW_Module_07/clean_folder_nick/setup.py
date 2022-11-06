from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder_nick',
    version='0.0.3',
    description='Very useful code for sorting files in directory. This is package which sorting files in any directory. To start sorting use command "clean-folder"',
    author='Mykyta Sherstianykh',
    author_email='n.sher.test@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder=clean_folder_nick.clean:clean_folder']}
)
