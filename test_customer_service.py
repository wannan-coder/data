#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
智能客服系统测试文件
"""

import sys
import os

# 确保可以导入主模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from smart_customer_service import SmartCustomerService


def test_initialization():
    """测试系统初始化"""
    print("测试 1: 系统初始化...")
    service = SmartCustomerService()
    assert service is not None, "系统初始化失败"
    assert hasattr(service, 'pdf_materials'), "PDF材料列表未初始化"
    assert hasattr(service, 'topic_keywords'), "主题关键词未初始化"
    assert hasattr(service, 'faq'), "FAQ未初始化"
    print("✓ 系统初始化测试通过")
    return service


def test_topic_matching(service):
    """测试主题匹配功能"""
    print("\n测试 2: 主题匹配功能...")
    
    # 测试动态规划
    topics = service._match_topic("我想学习动态规划")
    assert '动态规划' in topics, "动态规划匹配失败"
    print("✓ 动态规划关键词匹配成功")
    
    # 测试数组
    topics = service._match_topic("array学习")
    assert '数组' in topics, "数组匹配失败"
    print("✓ 数组关键词匹配成功")
    
    # 测试二叉树
    topics = service._match_topic("二叉树怎么学")
    assert '二叉树' in topics, "二叉树匹配失败"
    print("✓ 二叉树关键词匹配成功")
    
    print("✓ 主题匹配测试通过")


def test_faq(service):
    """测试FAQ功能"""
    print("\n测试 3: FAQ功能...")
    
    # 测试"如何开始"
    answer = service._check_faq("如何开始学习")
    assert answer != "", "FAQ '如何开始' 匹配失败"
    assert "数组" in answer or "链表" in answer, "FAQ答案内容不正确"
    print("✓ '如何开始'问题匹配成功")
    
    # 测试"学习顺序"
    answer = service._check_faq("推荐的学习顺序")
    assert answer != "", "FAQ '学习顺序' 匹配失败"
    assert "数组" in answer, "FAQ答案内容不正确"
    print("✓ '学习顺序'问题匹配成功")
    
    print("✓ FAQ测试通过")


def test_query_processing(service):
    """测试查询处理功能"""
    print("\n测试 4: 查询处理功能...")
    
    # 测试动态规划查询
    response = service.process_query("我想学习动态规划")
    assert response != "", "查询处理返回空结果"
    assert "动态规划" in response or "资料" in response, "查询响应不相关"
    print("✓ 动态规划查询处理成功")
    
    # 测试资料列表查询
    response = service.process_query("有哪些资料")
    assert response != "", "资料列表查询返回空结果"
    assert "资料" in response or "PDF" in response or "代码随想录" in response, "资料列表响应不正确"
    print("✓ 资料列表查询处理成功")
    
    # 测试FAQ查询
    response = service.process_query("如何开始")
    assert response != "", "FAQ查询返回空结果"
    print("✓ FAQ查询处理成功")
    
    # 测试空输入
    response = service.process_query("")
    assert "请输入" in response, "空输入处理不正确"
    print("✓ 空输入处理成功")
    
    print("✓ 查询处理测试通过")


def test_pdf_scanning(service):
    """测试PDF文件扫描"""
    print("\n测试 5: PDF文件扫描...")
    
    materials = service.pdf_materials
    print(f"  找到 {len(materials)} 个PDF文件")
    
    if materials:
        print(f"  示例: {materials[0]['name']}")
        assert 'filename' in materials[0], "PDF材料缺少filename字段"
        assert 'name' in materials[0], "PDF材料缺少name字段"
        print("✓ PDF文件扫描成功")
    else:
        print("⚠ 未找到PDF文件（这在测试环境中是正常的）")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("开始运行智能客服系统测试")
    print("=" * 50)
    
    try:
        # 测试1: 初始化
        service = test_initialization()
        
        # 测试2: 主题匹配
        test_topic_matching(service)
        
        # 测试3: FAQ
        test_faq(service)
        
        # 测试4: 查询处理
        test_query_processing(service)
        
        # 测试5: PDF扫描
        test_pdf_scanning(service)
        
        print("\n" + "=" * 50)
        print("✓ 所有测试通过！")
        print("=" * 50)
        return True
        
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n✗ 测试出错: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
