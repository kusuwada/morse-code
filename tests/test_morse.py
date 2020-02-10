#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from morse import Morse

class TestMorse(unittest.TestCase):
		
	def test_normal(self):
		test_patterns = [
				('test', '- . ... -'),
				('hello, world!', '.... . .-.. .-.. --- --..-- \n.-- --- .-. .-.. -.. -.-.--'),
				('This is Letter A.', '- .... .. ... \n.. ... \n.-.. . - - . .-. \n.- .-.-.-')
				]
		morse = Morse()
		for message, expect in test_patterns:
			with self.subTest(message = message, expect = expect):
				endoded = morse.enc(message)
				self.assertEqual(endoded, expect)
				decoded = morse.dec(endoded)
				self.assertEqual(decoded, message.upper())
		
	def test_invalid_message(self):
		test_patterns = [
				('%test', '*%* - . ... -'),
				('i%u', '.. *%* ..-')
				]
		morse = Morse()
		signals = ['-', '.', ' ', '\n']
		for message, expect in test_patterns:
			with self.subTest(message = message, expect = expect):
				endoded = morse.enc(message)
				self.assertEqual(endoded, expect)
	
	def test_invalid_morse(self):
		test_patterns = [
				('._..', '*._..*'),
				('', '**'),
				('_.. -.-', '*_..*K'),
				]
		morse = Morse()
		signals = ['-', '.', ' ', '\n']
		for mor, expect in test_patterns:
			with self.subTest(mor = mor, expect = expect):
				decoded = morse.dec(mor)
				self.assertEqual(decoded, expect)


if __name__ == "__main__":
	unittest.main()