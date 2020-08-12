# coding: utf-8

"""
    Gate API v4

    APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class FuturesAccountBook(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {'time': 'float', 'change': 'str', 'balance': 'str', 'type': 'str', 'text': 'str'}

    attribute_map = {'time': 'time', 'change': 'change', 'balance': 'balance', 'type': 'type', 'text': 'text'}

    def __init__(
        self, time=None, change=None, balance=None, type=None, text=None, local_vars_configuration=None
    ):  # noqa: E501
        # type: (float, str, str, str, str, Configuration) -> None
        """FuturesAccountBook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._change = None
        self._balance = None
        self._type = None
        self._text = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if change is not None:
            self.change = change
        if balance is not None:
            self.balance = balance
        if type is not None:
            self.type = type
        if text is not None:
            self.text = text

    @property
    def time(self):
        """Gets the time of this FuturesAccountBook.  # noqa: E501

        Change time  # noqa: E501

        :return: The time of this FuturesAccountBook.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this FuturesAccountBook.

        Change time  # noqa: E501

        :param time: The time of this FuturesAccountBook.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def change(self):
        """Gets the change of this FuturesAccountBook.  # noqa: E501

        Change amount  # noqa: E501

        :return: The change of this FuturesAccountBook.  # noqa: E501
        :rtype: str
        """
        return self._change

    @change.setter
    def change(self, change):
        """Sets the change of this FuturesAccountBook.

        Change amount  # noqa: E501

        :param change: The change of this FuturesAccountBook.  # noqa: E501
        :type: str
        """

        self._change = change

    @property
    def balance(self):
        """Gets the balance of this FuturesAccountBook.  # noqa: E501

        Balance after change  # noqa: E501

        :return: The balance of this FuturesAccountBook.  # noqa: E501
        :rtype: str
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this FuturesAccountBook.

        Balance after change  # noqa: E501

        :param balance: The balance of this FuturesAccountBook.  # noqa: E501
        :type: str
        """

        self._balance = balance

    @property
    def type(self):
        """Gets the type of this FuturesAccountBook.  # noqa: E501

        Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate  # noqa: E501

        :return: The type of this FuturesAccountBook.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FuturesAccountBook.

        Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate  # noqa: E501

        :param type: The type of this FuturesAccountBook.  # noqa: E501
        :type: str
        """
        allowed_values = ["dnw", "pnl", "fee", "refr", "fund", "point_dnw", "point_fee", "point_refr"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(type, allowed_values)  # noqa: E501
            )

        self._type = type

    @property
    def text(self):
        """Gets the text of this FuturesAccountBook.  # noqa: E501

        Comment  # noqa: E501

        :return: The text of this FuturesAccountBook.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FuturesAccountBook.

        Comment  # noqa: E501

        :param text: The text of this FuturesAccountBook.  # noqa: E501
        :type: str
        """

        self._text = text

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FuturesAccountBook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesAccountBook):
            return True

        return self.to_dict() != other.to_dict()
