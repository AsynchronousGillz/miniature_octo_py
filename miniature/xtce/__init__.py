#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
"""
import logging
from xml.etree import ElementTree
from xml.etree.ElementTree import Element


class Xtce:
    """
    Telemetry/Telecommand (TM/TC) definitions across the widest possible range
    of space domain activities. The goal is to allow TM/TC definitions to be
    exchanged between different organizations and systems, often at the
    boundaries of mission phases, without the need for customized import/export,
    re-validation, or even re-implementation of mission databases.
    """

    _XTCE_IGNORED_ELEMENTS = []

    @classmethod
    def load(cls, file_name: str):
        """ Load from a file """
        with open(file_name) as fp:
            source = fp.read()
        return Xtce(source)

    def __init__(self, source: str):
        """
        """
        self.name = ""
        self.root = None
        self._current_packet = None
        self._types = {}
        self._parse(source)

    @property
    def _lookup(self):
        return {
            "SpaceSystem": self._space_systems,
        }

    def _parse(self, source: str) -> None:
        """ TODO """
        try:
            self.root = ElementTree.fromstring(source)
        except ElementTree.ParseError as err:
            raise ValueError("invalid input source") from err
        else:
            self._xtce_validate_root()
        for child in self.root:
            for element in self._xtce_recurse_element(child):
                self._xtce_process_element(element)

    def _xtce_validate_root(self) -> None:
        """ TODO """
        if any(self.root) is False:
            raise ValueError("invalid xtce structure")
        for child in self.root:
            for valid_tag in ["Header", "ServiceSet", "TelemetryMetaData", "CommandMetaData"]:
                if valid_tag == child.tag:
                    break
            else:  # this is a for-else statement; if a break happens it won't run this code
                raise ValueError(f"invalid xtce structure, root child {child.tag}")

    def _xtce_process_element(self, element: Element) -> None:
        """ TODO """
        if element.tag.startswith("{"):
            element.tag = element.tag.split("}", 1)[1]  # strip namespace
        if element.text:
            element.text = element.tag.rstrip()
        if element.tag in self._XTCE_IGNORED_ELEMENTS:
            return
        self._xtce_log(element)
        method = self._lookup.get(element.tag)
        if method is None:
            return
        method(element)

    @staticmethod
    def _xtce_log(element: Element):
        """ TODO """
        ret = [f"- {element.tag}"]
        for k, v in element.attrib.items():
            ret.append(f"{k}:{v}")
        logging.info(", ".join(ret))

    def _xtce_recurse_element(self, element: Element):
        """ TODO """
        if any(element) is False:
            yield element
        for child in element:
            yield from self._xtce_recurse_element(child)

    def _finish_packet(self):
        """ TODO """
        if self._current_packet is None:
            return
        # check bit offset
        # self._check_packet_endianness()
        # check packet type
        # add packet to xtce type dict
        # self._current_packet = None

    def _check_packet_endianness(self):
        """ TODO """
        pass

    def _space_systems(self, element: Element):
        """ TODO """
        self.name = element.attrib.get("name")

    def _telemetry_metadata(self, element: Element):
        """ TODO """
        pass

    def _command_metadata(self, element: Element):
        """ TODO """
        pass

    def _parameter_type(self, element: Element):
        """ TODO """
        pass

    def _argument_type(self, element: Element):
        """ TODO """
        pass
