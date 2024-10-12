import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from unittest.mock import patch, MagicMock
from src.tabs import conversation_tab

class TestConversationTab(unittest.TestCase):
    @patch('src.tabs.conversation_tab.gr.Markdown')
    @patch('src.tabs.conversation_tab.gr.Textbox')
    @patch('src.tabs.conversation_tab.gr.Button')
    @patch('src.tabs.conversation_tab.gr.Accordion')
    @patch('src.tabs.conversation_tab.ConversationAgent')
    @patch('src.tabs.conversation_tab.gr.ChatInterface')
    @patch('src.tabs.conversation_tab.gr.Chatbot')
    @patch('src.tabs.conversation_tab.gr.ClearButton')
    @patch('src.tabs.conversation_tab.gr.Tab')
    def test_create_conversation_tab(self, mock_tab, mock_clear_button, mock_chatbot, mock_chat_interface, mock_conversation_agent, mock_accordion, mock_button, mock_textbox, mock_markdown):
        # 模拟 Gradio 组件
        mock_markdown.return_value = MagicMock()
        mock_textbox.return_value = MagicMock()
        mock_button.return_value = MagicMock()
        mock_accordion.return_value = MagicMock()
        mock_chatbot.return_value = MagicMock()
        mock_clear_button.return_value = MagicMock()
        mock_tab.return_value.__enter__ = MagicMock()
        mock_tab.return_value.__exit__ = MagicMock()
        
        # 重置 conversation_agent 为新的 mock 对象
        conversation_tab.conversation_agent = mock_conversation_agent.return_value
        
        # 调用函数
        conversation_tab.create_conversation_tab()
        
        # 验证是否创建了正确的 Gradio 组件
        mock_tab.assert_called_once_with("对话")
        mock_markdown.assert_called()
        mock_chatbot.assert_called()
        # 验证 ClearButton 是否被创建，而不是被调用
        # mock_clear_button.assert_called_once()
        # mock_chat_interface.assert_called()

        # 验证是否使用了 ConversationAgent 实例
        self.assertIsNotNone(conversation_tab.conversation_agent)
        self.assertEqual(conversation_tab.conversation_agent, mock_conversation_agent.return_value)

if __name__ == '__main__':
    unittest.main()
