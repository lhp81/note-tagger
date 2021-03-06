from setuptools import setup

long_description = """
This is a web app which attempts to auto-tag your notes
"""

setup(
    name="note_tagger",
    version="0.1-dev",
    description="Auto Tag Notes",
    long_description=long_description,
    # The project URL.
    # url='http://github.com/<yourname>/data-structures',
    # Author details
    author='<Your Name>',
    author_email='<your.email@domain.com',
    # Choose your license
    #   and remember to include the license text in a 'docs' directory.
    # license='MIT',
    packages=['note_tagger'],
    install_requires=['setuptools', ]
)
