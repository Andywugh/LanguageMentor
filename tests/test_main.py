import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
import gradio as gr
from src.main import main

class TestMain(unittest.TestCase):
    @patch('src.main.create_scenario_tab')
    @patch('src.main.create_conversation_tab')
    @patch('src.main.create_vocab_tab')
    @patch('gradio.Blocks')
    def test_main_function(self, mock_blocks, mock_vocab_tab, mock_conversation_tab, mock_scenario_tab):
        mock_app = MagicMock()
        mock_blocks.return_value.__enter__.return_value = mock_app

        main()
        
        # 验证是否调用了所有必要的函数
        mock_scenario_tab.assert_called_once()
        mock_conversation_tab.assert_called_once()
        mock_vocab_tab.assert_called_once()
        
        # 验证 Gradio 应用是否正确启动
        mock_app.launch.assert_called_once_with(share=True, server_name="0.0.0.0")

if __name__ == '__main__':
    unittest.main()
