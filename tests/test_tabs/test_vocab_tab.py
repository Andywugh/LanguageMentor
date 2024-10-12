import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from unittest.mock import patch, MagicMock
from src.tabs import vocab_tab

class TestVocabTab(unittest.TestCase):
    @patch('src.tabs.vocab_tab.gr.Markdown')
    @patch('src.tabs.vocab_tab.gr.Textbox')
    @patch('src.tabs.vocab_tab.gr.Button')
    @patch('src.tabs.vocab_tab.gr.Accordion')
    @patch('src.tabs.vocab_tab.VocabAgent')
    @patch('src.tabs.vocab_tab.gr.ChatInterface')
    @patch('src.tabs.vocab_tab.gr.Chatbot')
    @patch('src.tabs.vocab_tab.gr.ClearButton')
    @patch('src.tabs.vocab_tab.gr.Tab')
    def test_create_vocab_tab(self, mock_tab, mock_clear_button, mock_chatbot, mock_chat_interface, mock_vocab_agent, mock_accordion, mock_button, mock_textbox, mock_markdown):
        # 模拟 Gradio 组件
        mock_markdown.return_value = MagicMock()
        mock_textbox.return_value = MagicMock()
        mock_button.return_value = MagicMock()
        mock_accordion.return_value = MagicMock()
        mock_chatbot.return_value = MagicMock()
        mock_clear_button.return_value = MagicMock()
        mock_tab.return_value.__enter__ = MagicMock()
        mock_tab.return_value.__exit__ = MagicMock()
        
        # 重置 vocab_agent 为新的 mock 对象
        vocab_tab.vocab_agent = mock_vocab_agent.return_value
        
        # 调用函数
        vocab_tab.create_vocab_tab()
        
        # 验证是否创建了正确的 Gradio 组件
        mock_tab.assert_called_once_with("单词")
        mock_markdown.assert_called()
        mock_chatbot.assert_called()
        mock_clear_button.assert_called_once_with(value="下一关")
        mock_chat_interface.assert_called()

        # 验证是否使用了 VocabAgent 实例
        self.assertIsNotNone(vocab_tab.vocab_agent)
        self.assertEqual(vocab_tab.vocab_agent, mock_vocab_agent.return_value)

if __name__ == '__main__':
    unittest.main()
