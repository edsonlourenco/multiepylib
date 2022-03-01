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


import requests
import json
import pyspark
import pandas as pd
import numpy as np
from base import ModelBase


class SparkHelper(ModelBase):
    """helper class for Spark common operations.

    :param ModelBase: ModelBase class
    :type ModelBase: ModelBase
    """


    def register_udf(self, function, function_udf_name: str) -> None:
        """register python function as udf function.

        :param function: python function
        :type function: function
        :param function_udf_name: udf function name
        :type function_udf_name: str

        Examples
        --------
        >>> from pyspark.sql.functions import col
        >>> from multiepy.helpers import SparkHelper
        >>> def calculate(column_a: float):
                ...
        >>> SparkHelper.register_udf(calculate, 'calculate_udf')
        >>> df_total = df.withColumn('value_calculated', calculate_udf(col('value')))
        """

        self.spark.udf.register(function_udf_name, function)



class DataFrameHelper:
    """helper class for dataframe spark operations.
    """


    def spark_col_to_list(self, df: pyspark.sql.dataframe, col_name: str) -> list:
        """cast dataframe spark column to list.

        :param df: spark dataframe.
        :type df: pyspark.sql.dataframe
        :param col_name: column name
        :type col_name: str
        :return: list
        :rtype: list

        Examples
        --------
        >>> from multiepy.helpers import DataFrameHelper
        >>> values_list = DataFrameHelper.spark_col_to_list(df_spark, 'value')
        >>> print(values_list)
        [1.44, 5.58, 102.6, 777.0, 19.25, 0, 55.7, 250.34, 0.01]
        """
        try:
            temp_list = [row[col_name] for row in df.collect()]
            return temp_list
        except Exception as e:
            raise e


    def split_pandas(df: pd.DataFrame, parts=1) -> list:
        """split dataframe pandas in parts.

        :param df: datafrme pandas
        :type df: pd.DataFrame
        :param parts: parts for spliting, defaults to 1
        :type parts: int, optional
        :return: list of pandas dataframe splitted
        :rtype: list

        Examples
        --------
        >>> from multiepy.helpers import DataFrameHelper
        >>> pd.read_csv('fbi_ufo.csv', sep=';', header=True) #1000 rows
        >>> df_list = DataFrameHelper.split_pandas(df_pandas, 10)
        >>> len(df_list)
        10
        """

        permuted_indices = np.random.permutation(len(df))

        dfs = []
        for i in range(parts):
            dfs.append(df.iloc[permuted_indices[i::parts]])

        return dfs



class ApiHelper:
    """helper class for API http operations.

    :return: http response.
    :rtype: any
    """


    def call_api(url: str, data = '', headers = {'content-type': "application/json"}) -> any:
        """call api http url.

        :param url: url api 
        :type url: str
        :param data: data for request, defaults to ''
        :type data: str, optional
        :param headers: header for request, defaults to {'content-type': "application/json"}
        :type headers: dict, optional
        :return: any
        :rtype: any

        Examples
        --------
        >>> from multiepy.helpers import ApiHelper
        >>> json_response = ApiHelper.call_api(url)
        """

        res = None

        try:
            api_url_tmp   = '{}{}'.format(url, data)
            res = requests.get(api_url_tmp, headers=headers)
        except Exception as e:
            return e

        if res != None and res.status_code == 200:
            return json.loads(res.text)
        return None