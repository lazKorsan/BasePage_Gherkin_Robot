from pages.DriverManagerPage import DriverManagerPage
from pages.ExitIntentPage import ExitIntentPage


def test_mouse_move():
    driver_manager = DriverManagerPage()
    driver_manager.navigate_heroku_homePage()
    exit_intent_page = ExitIntentPage()
    exit_intent_page.navigate_exit_intent_page()
    exit_intent_page.action_mouse_move_to_out_of_the_viewport()
    exit_intent_page.wait_for_flash_message_to_appear()
    exit_intent_page.push_modal_close_button()
    driver_manager.close_driver()

if __name__ == "__main__":
    test_mouse_move()