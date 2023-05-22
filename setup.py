from setuptools import setup
from os.path import join, dirname

setup(
    name='FoxHustleQR',
    version='1.0',
    url="https://github.com/Fox-Hustle/QR-generator.git",
    description='QR-code Generator',
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    packages=['FoxHustleQR'],
    license='MIT',
    author='welcome32',
    author_email='welcome32@foxhustle.ru',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Pillow==8.2.0', 
        'PyQRCode==1.2.1',
        'requests==2.31.0',
    ], 
    python_requires='>=3.6',
    )