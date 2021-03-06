import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-merged-inlines',
    version='0.2',
    packages=['merged_inlines'],
    include_package_data=True,
    license='MIT License',
    description='A Django Admin extension that allows you to mix and reorder multiple inline classes together',
    url='https://github.com/MattBroach/Django-Merged-Inlines',
    download_url = 'https://github.com/mattbroach/django-merged-inlines/tarball/0.2',
    author='Matt Broach, Koty Yell',
    author_email='broach@aya.yale.edu',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
