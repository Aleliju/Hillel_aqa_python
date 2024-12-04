from tracking_page import TrackingPage

def test_tracking_status(driver):
    driver.get("https://tracking.novaposhta.ua/#/uk")
    tracking_page = TrackingPage(driver)
    tracking_page.enter_ttn("59001268685947")
    tracking_page.click_search()
    tracking_page.close_info_popup()
    status_text = tracking_page.get_status()
    assert status_text == 'Отримана'