from setuptools import setup, find_packages
from os.path import dirname, abspath, join
from setuptools.command.develop import develop
from setuptools.command.install import install
from snakypy import __author__, __version__


ROOT = dirname(abspath(__file__))


class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        develop.run(self)


class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        install.run(self)


readme_rst = join(ROOT, 'README.rst')
with open(readme_rst) as f:
    long_description = f.read()

requirements = join(ROOT, 'requirements.txt')
with open(requirements) as f:
    install_requires = [i.strip().split('#', 1)[0].strip()
                        for i in f.read().strip().split('\n')]

requirements_dev = join(ROOT, 'requirements-dev.txt')
extras_require = {}
with open(requirements_dev) as f:
    extras_require['dev'] = [i.strip().split('#', 1)[0].strip()
                             for i in f.read().strip().split('\n')]

# Variables setup
license_ = "MIT license",
license_classifiers = "License :: OSI Approved :: MIT License"
name = 'snakypy'
url = 'https://github.com/snakypy/snakypy'
# project_exec = 'snakypy'
# exec_path = 'snakypy.snakypy:Snakypy'
# entry_points = [f' {project_exec} = {exec_path}']

setup(
    name=name,
    version=__version__,
    description='Snakypy is a package that contains code ready to assist in the development of '
                'packages/applications so as not to replicate the code.',
    author=__author__['name'],
    author_email=__author__['email'],
    license=license_,
    maintainer=__author__['name'],
    # Types: text/plain, text/x-rst, text/markdown
    long_description_content_type='text/x-rst',
    long_description=long_description,
    url=url,
    packages=find_packages(include=['snakypy',
                                    'snakypy.*']),
    install_requires=install_requires,
    scripts=[],
    extras_require=extras_require,
    classifiers=['Intended Audience :: Developers',
                 license_classifiers,
                 'Operating System :: POSIX :: Linux',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Unix',
                 'Programming Language :: Python :: 3'],
    python_requires='>= 3.8',
    keywords='snakypy modules library package',
    # entry_points={'console_scripts': entry_points},
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    package_data={
        "": ["LICENSE", "requirements-dev.txt", "CHANGELOG.rst"]}
)
