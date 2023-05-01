from setuptools import setup, find_packages

setup(
    name="findproject",
    version="0.1.0",
    author="ihciM (Michael Gail)",
    description="findproject",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3"
    ],
    scripts=[
        "scripts/fp",
        "scripts/fp_tmux"
    ],
)
