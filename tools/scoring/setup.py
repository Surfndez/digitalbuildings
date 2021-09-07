# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Setup """

from setuptools import setup, find_packages

setup(
    name='scoring',
    version='0.0.1',
    url='https://github.com/google/digitalbuildings',
    license='Apache License',
    author='',
    author_email='',
    description='',
    packages=find_packages(),
    install_requires=['datetime', 'filehash', 'dirhash'],
    python_requires='>=3.7',
)
