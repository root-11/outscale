# Maslite setup script created by package.py
build_tag = "899e350a94b131465fd800d2dec5474b21f2b8f046532fb195159d73e7927d1e"
from pathlib import Path
from setuptools import setup


folder = Path(__file__).parent
filename = "readme.md"
readme = folder / filename
assert isinstance(readme, Path)
assert readme.exists(), readme
with open(str(readme), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="MASlite",
    version="2021.5.28.43437",
    url="https://github.com/root-11/maslite",
    license="MIT",
    author="Bjorn Madsen",
    author_email="bjorn.madsen@operationsresearchgroup.com",
    description="A lightweight multi-agent system",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="multi agent system MAS",
    packages=["maslite"],
    include_package_data=True,
    data_files=[(".", ["license.md", "readme.md"])],
    platforms="any",
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
