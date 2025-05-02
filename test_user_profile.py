import unittest
from unittest.mock import patch, mock_open
import json
from pathlib import Path

from models.user_profile import UserProfile
from validations import *
from user_input import *


class TestUserProfile(unittest.TestCase):
    @patch("models.user_profile.get_input")
    @patch("models.user_profile.open", new_callable=mock_open)
    @patch("models.user_profile.Path.exists", return_value=False)
    def test_calculate_daily_calories(self, mock_exists, mock_open_file, mock_get_input):
        mock_get_input.side_effect = [
            # First attempt 
            "male", "20", "190", "120", "60", "10",
            # Second attempt 
            "male", "30", "180", "80", "75", "60"  
        ]

        profile = UserProfile()
        calories = profile.get_daily_calories()

        self.assertTrue(500 <= calories <= 4000)

        self.assertTrue(mock_open_file().write.called)

if __name__ == "__main__":
    unittest.main()