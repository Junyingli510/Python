import pickle

def add_cookie():
	pickle.dump(self.mainDriver.driver.get_cookies(), open(self.cookies_dir +"mp_cookie.pkl", "wb"))
	

def upload_cookie():
	self.cookies = pickle.load(open(self.cookies_dir + "mp_cookie.pkl", "rb"))
        print('file_cookie_data', self.cookies)
        for cookie in self.cookies:
            print('cookie', cookie)
            self.mainDriver.driver.add_cookie(cookie)
		
# When save cookei have to delay sleep(5)
