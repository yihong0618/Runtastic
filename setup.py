# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = '0.0.5'

setup(name='runtastic',
      version=VERSION,
      description="Download all your Runtastic activities save to gpx",
      keywords='runtastic running',
      author='yihong0618',
      author_email='zouzou0208@gmail.com',
      url='https://github.com/yihong0618/Runtastic',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=["httpx", "gpxpy"],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Software Development :: Libraries",
      ],
      py_modules=["runtastic"],
      entry_points={"console_scripts": ["runtastic = runtastic:main"], }
      )
