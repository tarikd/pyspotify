# encoding: utf-8

from __future__ import unicode_literals

import unittest

import spotify
from spotify import utils


class ToBytesTest(unittest.TestCase):

    def test_unicode_to_bytes_is_encoded_as_utf8(self):
        self.assertEqual(utils.to_bytes('æøå'), 'æøå'.encode('utf-8'))

    def test_bytes_to_bytes_is_passed_through(self):
        self.assertEqual(
            utils.to_bytes('æøå'.encode('utf-8')), 'æøå'.encode('utf-8'))

    def test_anything_else_to_bytes_fails(self):
        self.assertRaises(ValueError, utils.to_bytes, [])
        self.assertRaises(ValueError, utils.to_bytes, 123)


class ToUnicodeTest(unittest.TestCase):

    def test_unicode_to_unicode_is_passed_through(self):
        self.assertEqual(utils.to_unicode('æøå'), 'æøå')

    def test_bytes_to_unicode_is_decoded_as_utf8(self):
        self.assertEqual(utils.to_unicode('æøå'.encode('utf-8')), 'æøå')

    def test_cdata_to_unicode_is_unwrapped_and_decoded_as_utf8(self):
        cdata = spotify.ffi.new('char[]', 'æøå'.encode('utf-8'))
        self.assertEqual(utils.to_unicode(cdata), 'æøå')

    def test_anything_else_to_unicode_fails(self):
        self.assertRaises(ValueError, utils.to_unicode, [])
        self.assertRaises(ValueError, utils.to_unicode, 123)