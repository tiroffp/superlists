from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mary has been losing track of all the things she needs to do
        # and sees an ad for a to-do list site. She goes to check out the
        #homepage
        self.browser.get('http://localhost:8000')
        #She notices that the title mentions to-do lists, so she
        # knows shes on the right site
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test!')
        #She is invited to make a list right away

        # She types "Buy more artisanal cheeses"

        # When she hits enter, the page updates, and the page now
        # lists "1: Buy more artisanal cheeses" as an item on a to-do list

        # There is still a textbox inviting here to enter another item
        # she enters "Host a fancy party with fancy cheeses"

        # the page updates again, showing both her inputs

        # Mary begins to wonder if the site will remember her list, but the
        # site explains that it has generated a unique URL for her to save

        # She visits the URL -- the list is there!

        # Satisified, she leaves the page

if __name__ == '__main__':
    unittest.main()
