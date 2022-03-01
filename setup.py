#!/usr/bin/env python3

#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from setuptools import setup, find_packages

setup(
    name='multiepy',
    version='3.0',
    author='Edson Lourenço (Unraveling Code)',
    author_email='edson.lourenco.dev@gmail.com',
    description='MultiePy is the fundamental package for common operations with PySpark Framework.',
    long_description='Micro-framework for Apache Spark and PySpark Framework that helps Spark developers perform fast for common operations.',
    url='N/A',
    project_url={
        'Bug Tracker': 'N/A'
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.7',
)