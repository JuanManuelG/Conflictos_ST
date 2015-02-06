import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="Conflictos_ST",
    version="0.2",
    author="",
    author_email="",
    description="Conflictos_ST, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="Conflictos_ST geonode django",
    url='https://github.com/Conflictos_ST/Conflictos_ST',
    packages=['Conflictos_ST',],
    include_package_data=True,
    zip_safe=False,
)
