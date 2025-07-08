from setuptools import setup, find_packages

setup(
    name='text_cleaner',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['nltk'],
    author='Your Name',
    author_email='youremail@example.com',
    description='A simple NLP tool to remove punctuation and stopwords.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/text_cleaner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
