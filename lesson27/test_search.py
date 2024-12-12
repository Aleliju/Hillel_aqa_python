from tracking_page import TrackingPage

def test_tracking_status(driver):
    tracking_page = TrackingPage(driver)
    tracking_page.open_page("https://tracking.novaposhta.ua/#/uk")
    status = tracking_page.search_tracking_status("59001268685947")
    assert status == "Отримана"