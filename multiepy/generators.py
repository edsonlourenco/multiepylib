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


from ast import Try
import string
import random
from datetime import datetime as d


class Passwordhelper:
    """helper class for password operations.
    """


    @staticmethod
    def generate_random(self, length: int) -> str:
        """generates random passord.

        :param length: length
        :type length: int
        :return: random password
        :rtype: str

        Examples
        --------
        >>> from multiepy.generators import Passwordhelper
        >>> temp_password = Passwordhelper.generate_random(10)
        >>> print(temp_password)
        ONqpbPjhMO
        """

        letters = string.ascii_letters
        temp_password = ''.join(random.choice(letters) for i in range(length))
        return temp_password



class DateTimeHelper:
    """helper class for date time operations.
    """


    @staticmethod
    def get_instant(self, pattern = '%Y-%m-%d_%H%M%S') -> any:
        """get date and time.

        :param pattern: formatted date and time, defaults to '%Y-%m-%d_%H%M%S'
        :type pattern: str, optional
        :return: date time formatted.
        :rtype: any

        Examples
        --------
        >>> from multiepy.generators import DateTimeHelper
        >>> dt = DateTimeHelper.get_instant()
        >>> print(dt)
        '2022-03-01_164844'
        """
        try:
            return d.now().strftime(pattern)
        except Exception as e:
            return e