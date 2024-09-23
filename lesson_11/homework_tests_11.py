import logging
import unittest
import os

from homework_11 import log_event


class TestLogEvent(unittest.TestCase):

    def setUp(self):
        self.log_file = 'login_system.log'
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def tearDown(self):
        logging.shutdown()
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_event_success(self):
        log_event("test_user", "success")

        with open(self.log_file, 'r') as log:
            logs = log.read()
            self.assertIn("Login event - Username: test_user, Status: success", logs)

    def test_log_event_expired(self):
        log_event("test_user", "expired")

        with open(self.log_file, 'r') as log:
            logs = log.read()
            self.assertIn("Login event - Username: test_user, Status: expired", logs)

    def test_log_event_failed(self):
        log_event("test_user", "failed")

        with open(self.log_file, 'r') as log:
            logs = log.read()
            self.assertIn("Login event - Username: test_user, Status: failed", logs)


if __name__ == '__main__':
    unittest.main()
