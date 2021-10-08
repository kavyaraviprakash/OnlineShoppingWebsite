import unittest
from Sprint3.TC_product_detail import Class_Product_Detail
from Sprint3.TC_product_category import Class_product_category
from Sprint3.TC_changing_quantity_cart import Class_change_qty
from Sprint3.TC_paymentvalidation_with_userlogin import Class_Payment_validation

productdetail = unittest.TestLoader().loadTestsFromTestCase(Class_Product_Detail)
productcategory = unittest.TestLoader().loadTestsFromTestCase(Class_product_category)
product_change_qty = unittest.TestLoader().loadTestsFromTestCase(Class_change_qty)
payment_validation = unittest.TestLoader().loadTestsFromTestCase(Class_Payment_validation)


test_suite = unittest.TestSuite([productdetail, productcategory, product_change_qty, payment_validation])

unittest.TextTestRunner().run(test_suite)
