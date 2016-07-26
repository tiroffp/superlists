from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from functional_tests.base import FunctionalTest


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Mary has been losing track of all the things she needs to do
        # and sees an ad for a to-do list site. She goes to check out the
        # homepage
        self.browser.get(self.live_server_url)

        # She notices that the title mentions to-do lists, so she
        # knows shes on the right site
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # She is invited to make a list right away
        inputbox = self.get_item_input_box
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')

        # She types "Buy more artisanal cheeses"
        inputbox.send_keys('Buy more artisanal cheeses')

        # When she hits enter, the page updates, and the page now
        # lists "1: Buy more artisanal cheeses" as an item on a to-do list
        inputbox.send_keys(Keys.ENTER)
        mary_list_url = self.browser.current_url
        self.assertRegex(mary_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy more artisanal cheeses')

        # There is still a textbox inviting here to enter another item
        # she enters "Host a fancy party with fancy cheeses"
        inputbox = self.get_item_input_box
        inputbox.send_keys('Host a fancy party with fancy cheeses')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, showing both her inputs
        self.check_for_row_in_list_table('1: Buy more artisanal cheeses')
        self.check_for_row_in_list_table('2: Host a fancy party with fancy cheeses')

        # now a new user, Frank, comes along to the site

        # # We use a new browser session to make sure that no information
        # # of Mary's is coming through cookies, etc
        self.browser.refresh()
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Frank visits the home page. There is no sign of Mary's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy more artisanal cheeses', page_text)
        self.assertNotIn('Host a fancy party with fancy cheeses', page_text)

        # Frank starts a new list by entering a new item. He is
        # significantly less creative than Mary
        inputbox = self.get_item_input_box
        inputbox.send_keys('Buy pork chops')
        inputbox.send_keys(Keys.ENTER)

        # Frank gets his own unique URL
        frank_lists_url = self.browser.current_url
        self.assertRegex(frank_lists_url, '/lists/.+')
        self.assertNotEqual(frank_lists_url, mary_list_url)

        # Again, there is no trace of Mary's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy more artisanal cheeses', page_text)
        self.assertIn('Buy pork chops', page_text)

        # Satisified, he leaves the page
