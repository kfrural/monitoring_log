import unittest
from unittest.mock import patch
from send_email_alert import send_email_alert

class TestSendEmailAlert(unittest.TestCase):
    
    @patch('send_email_alert.smtplib.SMTP')
    def test_send_email_alert_success(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.sendmail = unittest.mock.MagicMock()

        subject = "Critical Alert"
        message = "CPU usage above 90%"
        recipient = "admin@example.com"
        
        send_email_alert(subject, message, recipient)

        mock_smtp_instance.sendmail.assert_called_once_with(
            "infra.monitor@example.com", 
            recipient, 
            unittest.mock.ANY
        )

    @patch('send_email_alert.smtplib.SMTP')
    def test_send_email_alert_failure(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        mock_smtp_instance.sendmail.side_effect = Exception("SMTP server error")

        subject = "Critical Alert"
        message = "CPU usage above 90%"
        recipient = "admin@example.com"
        
        with self.assertRaises(Exception):
            send_email_alert(subject, message, recipient)

if __name__ == '__main__':
    unittest.main()
