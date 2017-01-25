from setuptools import setup, find_packages

setup(
    name='myres',
    version='0.0.1',
    description='MyRes.',
    author='Thapelo Tsotetsi',
    author_email='info@myres.co.za',
    url='https://myres.co.za/',
    install_requires=[
        'django',
        'djangorestframework',
        'djangorestframework-jwt',
        'django-rest-auth',
        'django-allauth',
        'django-authtools',
        'django-model-utils',
        'django-enumfields',
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
)
