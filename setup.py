from setuptools import setup, find_packages

setup(
    name='olvy',
    version='1.0.0',
    author='Your Company',
    author_email='info@yourcompany.com',
    description='AI-powered cap table management and customer survey tool',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourcompany/olvy',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'sqlalchemy',
        'alembic',
        'flask_sqlalchemy',
        'flask_migrate',
        'flask_jwt_extended',
        'flask_cors',
        'python-dotenv',
        'openai',
        'requests',
        'bcrypt',
        'email_validator',
        'python-jose[cryptography]',
        'gunicorn'
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'pytest-cov',
        ],
    },
    entry_points={
        'console_scripts': [
            'olvy=backend.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)