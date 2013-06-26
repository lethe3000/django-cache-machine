from setuptools import setup

import caching


setup(
    name='django-cache-zoom',
    version=caching.__version__,
    description='Automatic caching and invalidation for Django models '
                'through the ORM.',
    long_description=open('README.rst').read(),
    author='Lethe',
    author_email='lethe30003000@mozilla.com',
    url='https://github.com/lethe3000/django-cache-zoom',
    license='BSD',
    packages=['caching', 'caching.backends'],
    include_package_data=True,
    zip_safe=False,
)
