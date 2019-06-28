import unittest
import main

class MyTest(unittest.TestCase):
   def test_INPUT_1_SHOULD_BE_1(self):
       self.assertEqual(main.shout(1), '1')
   def test_INPUT_3_SHOULD_BE_FooFoo(self):
       self.assertEqual(main.shout(3), 'FooFoo')
   def test_INPUT_5_SHOULD_BE_BarBar(self):
       self.assertEqual(main.shout(5), 'BarBar')
   def test_INPUT_6_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(6), 'Foo')
   def test_INPUT_7_SHOULD_BE_QixQix(self):
       self.assertEqual(main.shout(7), 'QixQix')
   def test_INPUT_9_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(9), 'Foo')
   def test_INPUT_10_SHOULD_BE_Bar(self):
       self.assertEqual(main.shout(10), 'Bar')
   def test_INPUT_13_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(13), 'Foo')
   def test_INPUT_15_SHOULD_BE_FooBarBar(self):
       self.assertEqual(main.shout(15), 'FooBarBar')
   def test_INPUT_21_SHOULD_BE_FooQix(self):
       self.assertEqual(main.shout(21), 'FooQix')
   def test_INPUT_33_SHOULD_BE_FooFooFoo(self):
       self.assertEqual(main.shout(33), 'FooFooFoo')
   def test_INPUT_51_SHOULD_BE_FooBar(self):
       self.assertEqual(main.shout(51), 'FooBar')
   def test_INPUT_53_SHOULD_BE_BarFoo(self):
       self.assertEqual(main.shout(53), 'BarFoo')

if __name__ == '__main__':
   unittest.main()
   