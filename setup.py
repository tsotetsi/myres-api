from setuptools import setup, find_packages

setup(
    name='myres',
    version='0.0.1',
    description='University Residence Administration.',
    author='Textily',
    author_email='info@textily.co.za',
    url='http://myres.textily.co.za/',
    install_requires=[
        'Django',
        'djangorestframework',
        'djangorestframework-jwt',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
