from setuptools import setup, find_packages

setup(
    name='PyJPDF',
    version='0.1.3',
    author='Jasson Carvalho',
    description='A simple library to extract text from PDF files.',
    url='https://github.com/LordWaif/PyJPDF',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    py_modules=['pyjpdf','utils'],
    install_requires=[
        'selenium',
        'pyperclip',
        'webdriver-manager'
    ],
)