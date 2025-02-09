from setuptools import setup, find_packages

setup(
    name="rtc_sdk",
    version="0.1",
    packages=find_packages(),
    package_data={"rtc_sdk": ["lib/*.so"]},
    include_package_data=True,
)
