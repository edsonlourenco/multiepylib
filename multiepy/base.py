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


class SparkSession:
    """ spark session helper.
    """


    @staticmethod
    def get_instance(self, app_name: str):
        """get instance of spark with app name.

        :param app_name: app name
        :type app_name: str
        :return: spark session class
        :rtype: "SparkSession"

        Examples
        --------
        >>> from multiepy.base import SparkSession as spks
        >>> spark = spks.get_instance("my app")
        >>> df    = spark.sql('SELECT * FROM table1')
        >>> df.count()
        10
        """

        return (SparkSession.builder
                            .appName(app_name)
                            .getOrCreate()
               )



class ModelBase:
    """inheritable base class for spark operations.
    """


    def __init__(self) -> None:
        """constructor that gets or creates spark session instance.
        """
        from pyspark.context import SparkContext
        from pyspark.sql.session import SparkSession

        sc = SparkContext.getOrCreate()
        self.spark = SparkSession(sc)