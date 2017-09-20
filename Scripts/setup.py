from setuptools import setup, find_packages


setup(
    name='ml_ecomh9',
    version='1.8.0-SNAPSHOT',
    py_modules=['ecom_h9'],
    author='Kogentix, Inc.',
    packages=find_packages(exclude=['ecom_h9.tests']),
    install_requires=[
        'numpy',
        'pandas',
        'nose',
        'nltk'
        ],
    entry_points={
        'console_scripts': [
            'ml_h9predict=ecom_h9.predict:predict_h9',
        ]
    },
    include_package_data=True,
    # test_suite='nose.collector',
    # tests_require=['nose'],
)

Testing exp3