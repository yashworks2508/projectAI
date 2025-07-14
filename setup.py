from setuptools import setup, find_packages



setup(
    name='mcqgenerator',
    version='0.1.0',
    author='Yash Gupta',
    author_email="yashworks2508@gmail.com",
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)   