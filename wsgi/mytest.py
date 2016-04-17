import unittest
import requests
import json
#import myflaskapp.py
#def foo():
#	return 400
class MyTest(unittest.TestCase):
    def test_post_userinfo(self):
        #self.assertEqual(400, requests.post('http://localhost:5000/userinfo/',{'sdfsfd':'9945321000'}).status_code)     #phonenumber not sent
        #self.assertEqual(201, requests.post('http://localhost:5000/userinfo/',{'phonenumber':'8495739573'}).status_code)   #record added to db
        #self.assertEqual(409, requests.post('http://localhost:5000/userinfo/',{'phonenumber':'8495739573'}).status_code)   #duplicate record
        #self.assertEqual(400, requests.post('http://localhost:5000/userinfo/',{}).status_code)   #invalid data
        pass
    def test_get_userinfo(self):
        #print(requests.get('http://localhost:5000/userinfo/8495739573').content)     #testing the returned info is correct from db
        #print(requests.get('http://localhost:5000/userinfo/4565654645').content)     #testing the returned info is not present in db
        pass
        
    def test_admin_student_status(self):
        #print( requests.get('http://localhost:5000/admin_student_status.html').text)     #getting data for student status
        pass

    def test_admin_student_status_post(self):
        #self.assertEqual(200,requests.post('http://localhost:5000/admin_student_status.html',{'phonenumber':'9945321000', 'status': 'aproove'}).status_code)     #passing data for student status - success
        #self.assertEqual(200,requests.post('http://localhost:5000/admin_student_status.html',{'status': 'aproove'}).status_code)     #passing data for student status - fails (no condition to check if phonenumber or status is not sent
        pass

    def test_register_token(self):
        #self.assertEqual(200, requests.post('http://localhost:5000/register_token/',{'phonenumber':'9945321000', 'token':'5gfd345'}).status_code)     #passing data for student registration
        #self.assertEqual(200, requests.post('http://localhost:5000/register_token/',{'phonenumber':'9945321000', 'token':'5gfd345'}).status_code)     #passing data for student registration - fails (no condition to check if phonenumber or token is not sent
        pass


    def setUp(self):
        #for common action.. runs everytime before testing
        pass
    def tearDown(self):
        #runs after testing.
        pass
if __name__ == '__main__':
    unittest.main()
