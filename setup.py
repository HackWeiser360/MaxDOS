from distutils.core import setup

setup(
    name="MaxDOS",
    py_modules=["MaxDOS"],
    entry_points={"console_scripts": ["MaxDOS=MaxDOS:main"]},
    version="1.0",
    description="Low bandwidth DoS tool. MaxDOS written in Python.",
    author="MådMâx",
    instagram:="madmax4708",
    twitter="503_madmax",
    keywords=["dos", "http", "MaxDOS"],
    license="GNU",
)
