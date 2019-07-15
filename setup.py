from collections import OrderedDict

from setuptools import setup, find_packages

setup(
    name="rundeck",
    version="0.1.0",
    keywords=("rundeck", "rundeck client", "python"),
    description="rundeck client",
    project_urls=OrderedDict(
        (
            ("Code", "https://github.com/Barnettxxf/rundeck"),
        )
    ),
    license="MIT",
    author="Barnett Xu",
    author_email="15102096586@163.com",
    packages=find_packages("src"),

    package_data={
        'rundeck': ['web/templates/*.html', 'web/static/*/*/*', 'web/static/*/*'],
    },
    include_package_data=True,
    package_dir={"": "src"},
    long_description="""Rundeck Client""",
    platforms="any",
    install_requires=[
        "demjson",
        "requests",
        "pyyaml",
        "beautifulsoup4",
        "flask",
        "crontab",
    ],
    entry_points={
        "console_scripts": ["rdweb = rundeck.server:cli"]}
)
