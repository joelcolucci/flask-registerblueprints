from setuptools import setup


setup(
    name='Flask-RegisterBlueprints',
    version='0.1.0',
    url='https://github.com/joelcolucci/flask-registerblueprints',
    license='MIT',
    author='Joel Colucci',
    author_email='joelcolucci@gmail.com',
    description='Dynamically register Flask blueprints on application object',
    long_description=__doc__,
    packages=['flask_registerblueprints'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)