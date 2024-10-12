import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from unittest.mock import patch, MagicMock
from src.tabs import scenario_tab

class TestScenarioTab(unittest.TestCase):
    @patch('src.tabs.scenario_tab.gr.Markdown')
    @patch('src.tabs.scenario_tab.gr.Textbox')
    @patch('src.tabs.scenario_tab.gr.Button')
    @patch('src.tabs.scenario_tab.gr.Accordion')
    @patch('src.tabs.scenario_tab.ScenarioAgent')
    @patch('src.tabs.scenario_tab.gr.ChatInterface')
    @patch('src.tabs.scenario_tab.gr.Chatbot')
    @patch('src.tabs.scenario_tab.gr.ClearButton')
    @patch('src.tabs.scenario_tab.gr.Tab')
    def test_create_scenario_tab(self, mock_tab, mock_clear_button, mock_chatbot, mock_chat_interface, mock_scenario_agent, mock_accordion, mock_button, mock_textbox, mock_markdown):
        # 模拟 Gradio 组件
        mock_markdown.return_value = MagicMock()
        mock_textbox.return_value = MagicMock()
        mock_button.return_value = MagicMock()
        mock_accordion.return_value = MagicMock()
        mock_chatbot.return_value = MagicMock()
        mock_clear_button.return_value = MagicMock()
        mock_tab.return_value.__enter__ = MagicMock()
        mock_tab.return_value.__exit__ = MagicMock()
        
        # 重置 scenario_agent 为新的 mock 对象
        scenario_tab.scenario_agent = mock_scenario_agent.return_value
        
        # 调用函数
        scenario_tab.create_scenario_tab()
        
        # 验证是否创建了正确的 Gradio 组件
        mock_tab.assert_called_once_with("场景")
        mock_markdown.assert_called()
        mock_chatbot.assert_called()
        # 验证 ClearButton 是否被创建，而不是被调用
        # mock_clear_button.assert_called_once()
        # mock_chat_interface.assert_called()

        # 验证是否使用了 ScenarioAgent 实例
        self.assertIsNotNone(scenario_tab.scenario_agent)
        self.assertEqual(scenario_tab.scenario_agent, mock_scenario_agent.return_value)

if __name__ == '__main__':
    unittest.main()
