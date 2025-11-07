#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能客服系统 (Smart Customer Service System)
为《代码随想录》算法学习资料提供智能问答服务
"""

import os
from typing import List, Dict


class SmartCustomerService:
    """智能客服类，提供智能问答和资料导航服务"""
    
    def __init__(self):
        """初始化智能客服系统"""
        self.pdf_materials = self._scan_pdf_files()
        self.topic_keywords = {
            '数组': ['数组', 'array', '列表', 'list'],
            '链表': ['链表', 'linked', 'list', '节点', 'node'],
            '哈希': ['哈希', 'hash', '映射', 'map', '字典', 'dict'],
            '字符串': ['字符串', 'string', '文本', 'text'],
            '双指针': ['双指针', 'pointer', '指针', '快慢指针'],
            '栈': ['栈', 'stack'],
            '队列': ['队列', 'queue'],
            '二叉树': ['二叉树', 'tree', '树', 'binary'],
            '回溯': ['回溯', 'backtrack', '递归', 'recursion'],
            '贪心': ['贪心', 'greedy', '贪婪'],
            '动态规划': ['动态规划', 'dp', 'dynamic', 'programming'],
            '单调栈': ['单调栈', 'monotonic', 'stack']
        }
        
        self.faq = {
            '如何开始': '您可以从数组和链表开始学习，这是算法学习的基础。推荐先看《代码随想录》数组和链表的PDF。',
            '学习顺序': '建议学习顺序：1.数组 → 2.链表 → 3.哈希表 → 4.字符串 → 5.双指针 → 6.栈与队列 → 7.二叉树 → 8.回溯算法 → 9.贪心算法 → 10.动态规划 → 11.单调栈',
            '难度': '这套资料适合算法初学者到中级学习者，循序渐进，配有详细讲解。',
            '资料特点': '《代码随想录》提供系统化的算法学习路径，包含详细的解题思路和代码实现。',
            '如何提问': '您可以询问关于某个算法主题的资料，例如"我想学习动态规划"或"有没有关于二叉树的资料"。'
        }
    
    def _scan_pdf_files(self) -> List[Dict[str, str]]:
        """扫描目录中的PDF文件"""
        materials = []
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        for filename in os.listdir(current_dir):
            if filename.endswith('.pdf'):
                materials.append({
                    'filename': filename,
                    'name': filename.replace('.pdf', '')
                })
        
        return materials
    
    def _match_topic(self, user_input: str) -> List[str]:
        """根据用户输入匹配相关主题"""
        user_input_lower = user_input.lower()
        matched_topics = []
        
        for topic, keywords in self.topic_keywords.items():
            for keyword in keywords:
                if keyword in user_input_lower:
                    matched_topics.append(topic)
                    break
        
        return matched_topics
    
    def _find_relevant_pdfs(self, topics: List[str]) -> List[Dict[str, str]]:
        """根据主题查找相关的PDF文件"""
        relevant_pdfs = []
        
        for material in self.pdf_materials:
            for topic in topics:
                if topic in material['name']:
                    relevant_pdfs.append(material)
                    break
        
        return relevant_pdfs
    
    def _check_faq(self, user_input: str) -> str:
        """检查是否匹配常见问题"""
        user_input_lower = user_input.lower()
        
        for question, answer in self.faq.items():
            if question in user_input or any(word in user_input_lower for word in question.split()):
                return answer
        
        return ""
    
    def _generate_greeting(self) -> str:
        """生成欢迎语"""
        return """
========================================
欢迎使用《代码随想录》智能客服系统！
========================================

我可以帮您：
1. 查找相关的算法学习资料
2. 回答关于学习路径的问题
3. 提供学习建议

您可以问我：
- "我想学习动态规划"
- "有哪些资料？"
- "如何开始学习？"
- "推荐的学习顺序是什么？"

输入 'exit' 或 'quit' 退出系统
========================================
"""
    
    def process_query(self, user_input: str) -> str:
        """处理用户查询"""
        if not user_input.strip():
            return "请输入您的问题。"
        
        # 检查是否是常见问题
        faq_answer = self._check_faq(user_input)
        if faq_answer:
            return faq_answer
        
        # 检查是否询问资料列表
        if '资料' in user_input or '有哪些' in user_input or 'pdf' in user_input.lower():
            if self.pdf_materials:
                response = "我们有以下学习资料：\n\n"
                for i, material in enumerate(self.pdf_materials, 1):
                    response += f"{i}. {material['name']}\n"
                return response
            else:
                return "暂时没有找到PDF资料。"
        
        # 匹配主题
        matched_topics = self._match_topic(user_input)
        
        if matched_topics:
            relevant_pdfs = self._find_relevant_pdfs(matched_topics)
            
            if relevant_pdfs:
                response = f"根据您的需求，我找到了以下相关资料：\n\n"
                for pdf in relevant_pdfs:
                    response += f"📚 {pdf['name']}\n"
                response += f"\n这些资料涵盖了：{', '.join(matched_topics)}"
                return response
            else:
                return f"抱歉，我理解您想学习{', '.join(matched_topics)}，但暂时没有找到完全匹配的资料。请尝试其他关键词。"
        
        # 默认回复
        return "我不太理解您的问题。您可以尝试询问：\n- 某个具体算法主题（如：动态规划、二叉树）\n- 学习建议（如：如何开始、学习顺序）\n- 查看所有资料"
    
    def run(self):
        """运行客服系统"""
        print(self._generate_greeting())
        
        while True:
            try:
                user_input = input("\n您: ").strip()
                
                if user_input.lower() in ['exit', 'quit', '退出', '再见']:
                    print("\n感谢使用！祝您学习愉快！👋")
                    break
                
                response = self.process_query(user_input)
                print(f"\n客服: {response}")
                
            except KeyboardInterrupt:
                print("\n\n感谢使用！祝您学习愉快！👋")
                break
            except Exception as e:
                print(f"\n抱歉，系统出现了一个错误: {e}")


def main():
    """主函数"""
    service = SmartCustomerService()
    service.run()


if __name__ == "__main__":
    main()
