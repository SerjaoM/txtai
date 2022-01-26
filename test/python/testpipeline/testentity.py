"""
Entity module tests
"""

import unittest

from txtai.pipeline import Entity


class TestEntity(unittest.TestCase):
    """
    Entity tests.
    """

    @classmethod
    def setUpClass(cls):
        cls.entity = Entity("dslim/bert-base-NER")

    def testEntity(self):
        """
        Test entity
        """

        # Run entity extraction
        entities = self.entity("Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg")
        self.assertEqual([e[0] for e in entities], ["Canada", "Manhattan"])

    def testEntityFlatten(self):
        """
        Test entity with flattened output
        """

        # Run entity extraction
        entities = self.entity("Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg", flatten=True)
        self.assertEqual(entities, ["Canada", "Manhattan"])