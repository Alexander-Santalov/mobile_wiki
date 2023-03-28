from appium.webdriver.common.appiumby import AppiumBy


text_title = (AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
btn_continue = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')
btn_skip = (AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')
text_main_page = (AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text')
search = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
field_search = (AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')
result_search = (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
btn_menu = (AppiumBy.ID, 'org.wikipedia.alpha:id/menu_icon')
menu_item_login = (AppiumBy.ID, 'org.wikipedia.alpha:id/main_drawer_login_button')
field_username = (AppiumBy.XPATH, '(//*[@class="android.widget.EditText"])[1]')
text_error = (AppiumBy.ID, 'org.wikipedia.alpha:id/textinput_error')
widget_saved = (AppiumBy.ID, 'org.wikipedia.alpha:id/nav_tab_reading_lists')
btn_negative = (AppiumBy.ID, 'org.wikipedia.alpha:id/negativeButton')
text_empty = (AppiumBy.ID, 'org.wikipedia.alpha:id/empty_title')