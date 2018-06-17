import setuptools


setuptools.setup(
    name = 'DigitToChinese',
    version='0.0.1',
    author='Keyuan Wu',
    author_email='wky0702@gmail.com',
    description='A function that can convert number to Chinese words in proper reading order.',
    url='https://github.com/CapSOSkw/DigitToChinese',
    packages=setuptools.find_packages(include=['DigitToChinese']),
    python_requires='>=2.7',
)