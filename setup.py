import pip
import logging
import pkg_resources
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution("pip").version
    pip_version = list(map(int, pip_ver.split(".")[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]


try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception:
    logging.warning("Fail load requirements file, so using default ones.")
    install_reqs = []

setup(
    name="T100_Capture",
    version="0.0.1",
    url="https://github.com/zactodd/number_search",
    author="zactodd",
    author_email="zactodd0@gmail.com",
    description="Application of emailing number searches",
    packages=["ns"],
    install_requires=install_reqs,
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
)