#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""

from concurrent.futures import ThreadPoolExecutor

import grpc
from pathlib import Path

from miniature.environment import PORT
from miniature.server import miniature_pb2, miniature_pb2_grpc


class Server:

    @staticmethod
    def load_certs():
        """
        :return: (private_key, certificate_chain)
        """
        try:
            private_key = Path("test", "data", "certs", "ca-key.pem").open("rb").read()
            certificate_chain = Path("test", "data", "certs", "ca-cert.pem").open("rb").read()
            return private_key, certificate_chain
        except FileNotFoundError:
            pass

    def grpc_setup(self):
        private_key, certificate_chain = self.load_certs()
        credentials = grpc.ssl_server_credentials([(private_key, certificate_chain)], require_client_auth=True)
        composite_credentials = grpc.composite_channel_credentials(credentials)
        return composite_credentials

    @classmethod
    def main(cls):
        # server = grpc.server(ThreadPoolExecutor(max_workers=5))
        server_instance = cls()
        composite_credentials = server_instance.grpc_setup()
        with grpc.secure_channel("localhost:8080", composite_credentials) as channel:
            # ... create stub and do the call
            pass


