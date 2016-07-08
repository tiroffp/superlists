from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        # She notices that the title mentions to-do lists, so she
        # knows shes on the right site
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        #She is invited to make a list right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # She types "Buy more artisanal cheeses"
        inputbox.send_keys('Buy more artisanal cheeses')

        # When she hits enter, the page updates, and the page now
        # lists "1: Buy more artisanal cheeses" as an item on a to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy more artisanal cheeses' for row in rows),
                        "New todo item did not appear in table")

        # There is still a textbox inviting here to enter another item
        # she enters "Host a fancy party with fancy cheeses"
        self.fail('Finish the test!')
        # the page updates again, showing both her inputs

        # Mary begins to wonder if the site will remember her list, but the
        # site explains that it has generated a unique URL for her to save

        # She visits the URL -- the list is there!

        # Satisified, she leaves the page

if __name__ == '__main__':
    unittest.main()
