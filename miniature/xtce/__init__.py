#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""
import os
from xml.etree import ElementTree
from xmlschema import XMLSchema


class Xtce:

    def __init__(self, file_input: str):
        """
        """
        self.source = self._generate_source(file_input)
        # self._validate()
        self._generate_attr()

    @staticmethod
    def _generate_source(file_input: str) -> str:
        with open(file_input, "r") as fp:
            return fp.read()

    def _validate(self):
        """Validate XML to XSD"""
        xsd = os.path.join(os.path.dirname(__file__), "xtce-dtc-18-02-04.xsd")
        self.schema = XMLSchema(xsd)
        self.schema.validate(self.source)

    def _generate_attr(self) -> None:
        ns = {"xtce": "http://www.omg.org/spec/XTCE/20180204"}
        root = ElementTree.fromstring(self.source)
        tlm_metadata = root.find("xtce:TelemetryMetaData", ns)
        print(f"tlm_metadata {tlm_metadata}")

