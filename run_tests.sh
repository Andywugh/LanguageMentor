#!/bin/bash

# 安装测试依赖
pip install pytest pytest-cov

# 设置 PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd):$(pwd)/src"

# 运行测试并生成覆盖率报告
pytest tests/ --cov=src --cov-report=html -v

# 如果测试失败，退出并返回非零状态码
if [ $? -ne 0 ]; then
    echo "Tests failed!"
    exit 1
fi

echo "All tests passed successfully!"
