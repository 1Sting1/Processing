import unittest
from unittest.mock import patch
from Src.settings_manager import settings_manager


class TestSettingsManager(unittest.TestCase):

    @patch('builtins.open')
    def test_save_settings_manager(self, mock_open):
        mock_file = mock_open()
        manager = settings_manager()
        manager.settings.name = "Test Company"
        manager.settings.inn = "123456789012"
        manager.save()

        mock_file.assert_called_once_with(manager._settings_file_name, "w")