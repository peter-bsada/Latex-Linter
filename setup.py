import setuptools

setuptools.setup(
    name="Linter",
    version="0.0.1",
    author="Peter Bsada",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    scripts=["latex.py", "replace.json"],
    setup_requires=["wheel"],
    entry_points={
        "console_scripts": [
            "linter-peter = latex:main"
        ]
    }
)
