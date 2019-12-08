# coding: utf-8

"""
 Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

 Licensed under the Apache License, Version 2.0 (the "License").
 You may not use this file except in compliance with the License.
 A copy of the License is located at

     http://www.apache.org/licenses/LICENSE-2.0

 or in the "license" file accompanying this file. This file is distributed
 on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 express or implied. See the License for the specific language governing
 permissions and limitations under the License.
"""

"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from paapi5_python_sdk.refinement_bin import RefinementBin  # noqa: F401,E501


class Refinement(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bins': 'list[RefinementBin]',
        'display_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'bins': 'Bins',
        'display_name': 'DisplayName',
        'id': 'Id'
    }

    def __init__(self, bins=None, display_name=None, id=None):  # noqa: E501
        """Refinement - a model defined in Swagger"""  # noqa: E501

        self._bins = None
        self._display_name = None
        self._id = None
        self.discriminator = None

        if bins is not None:
            self.bins = bins
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id

    @property
    def bins(self):
        """Gets the bins of this Refinement.  # noqa: E501


        :return: The bins of this Refinement.  # noqa: E501
        :rtype: list[RefinementBin]
        """
        return self._bins

    @bins.setter
    def bins(self, bins):
        """Sets the bins of this Refinement.


        :param bins: The bins of this Refinement.  # noqa: E501
        :type: list[RefinementBin]
        """

        self._bins = bins

    @property
    def display_name(self):
        """Gets the display_name of this Refinement.  # noqa: E501


        :return: The display_name of this Refinement.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Refinement.


        :param display_name: The display_name of this Refinement.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this Refinement.  # noqa: E501


        :return: The id of this Refinement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Refinement.


        :param id: The id of this Refinement.  # noqa: E501
        :type: str
        """

        self._id = id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Refinement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Refinement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other