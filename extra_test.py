import unittest
import main

class MyTest(unittest.TestCase):
   def test_INPUT_1_SHOULD_BE_1(self):
       self.assertEqual(main.shout(), '1')
   def test_INPUT_3_SHOULD_BE_FooFoo(self):
       self.assertEqual(main.shout(), 'FooFoo')
   def test_INPUT_5_SHOULD_BE_BarBar(self):
       self.assertEqual(main.shout(), 'BarBar')
   def test_INPUT_6_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(), 'Foo')
   def test_INPUT_7_SHOULD_BE_QixQix(self):
       self.assertEqual(main.shout(), 'QixQix')
   def test_INPUT_9_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(), 'Foo')
   def test_INPUT_10_SHOULD_BE_Bar(self):
       self.assertEqual(main.shout(), 'Bar')
   def test_INPUT_13_SHOULD_BE_Foo(self):
       self.assertEqual(main.shout(), 'Foo')
   def test_INPUT_15_SHOULD_BE_FooBarBar(self):
       self.assertEqual(main.shout(), 'FooBarBar')
   def test_INPUT_21_SHOULD_BE_FooQix(self):
       self.assertEqual(main.shout(), 'FooQix')
   def test_INPUT_33_SHOULD_BE_FooFooFoo(self):
       self.assertEqual(main.shout(), 'FooFooFoo')
   def test_INPUT_51_SHOULD_BE_FooBar(self):
       self.assertEqual(main.shout(), 'FooBar')
   def test_INPUT_53_SHOULD_BE_BarFoo(self):
       self.assertEqual(main.shout(), 'BarFoo')
   def test_INPUT_101_SHOULD_BE_1Par1(self):
       self.assertEqual(main.shout(), '1*1')
   def test_INPUT_303_SHOULD_BE_FooFooParFoo(self):
       self.assertEqual(main.shout(), 'FooFoo*Foo')
   def test_INPUT_105_SHOULD_BE_FooBarQixParBar(self):
       self.assertEqual(main.shout(), 'FooBarQix*Bar')
   def test_INPUT_10101_SHOULD_BE_FooQixParPar(self):
       self.assertEqual(main.shout(), 'FooQix**')

if __name__ == '__main__':
   unittest.main()