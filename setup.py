
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = [line.rstrip('\n') for line in requirements_file]

setup(
    author='Emily Selwood',
    author_email='emily.selwood@sa.catapult.org.uk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description='search osm for tags in bounding box',
    long_description=readme,
    long_description_content_type="text/markdown",
    version='0.1.0',
    keywords='osm, kml, osm',
    name='osm_kml_search',
    license='apache2',
    packages=find_packages(include=['osm_kml_search'], exclude=['venv*', ]),
    install_requires=requirements,
    setup_requires=[],
    test_suite='nose2.collector.collector',
)
