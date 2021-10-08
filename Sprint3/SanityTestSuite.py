import unittest
from Sprint3.TC_Login import class_login
from Sprint3.TC_forgot_pwd import Class_forgot_pwd
from Sprint3.TC_Sign_up import Sign_Up

signup = unittest.TestLoader().loadTestsFromTestCase(Sign_Up)
login = unittest.TestLoader().loadTestsFromTestCase(class_login)
fgtpwd = unittest.TestLoader().loadTestsFromTestCase(Class_forgot_pwd)


test_suite = unittest.TestSuite([login, fgtpwd, signup])

unittest.TextTestRunner().run(test_suite)
