from setuptools import setup, find_packages

setup(
    name="near_ai_agent",
    version="1.0.0",
    author="Joe Spano",
    author_email="community@near.dev",
    description="A Python package to build AI agents on NEAR Protocol.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/joe-rlo/near_ai_agent", 
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)