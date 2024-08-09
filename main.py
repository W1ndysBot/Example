# script/example/main.py
# 示例脚本
# 本脚本写好了基本的函数，直接在函数中编写逻辑即可，必要的时候可以修改函数名

import logging
import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from app.api import *


async def handle_group_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        group_id = msg.get("group_id")
        raw_message = msg.get("raw_message")
        role = msg.get("sender", {}).get("role")
        message_id = msg.get("message_id")

    except Exception as e:
        logging.error(f"处理编解码消息失败: {e}")
        return


async def handle_private_message(websocket, msg):
    try:
        user_id = msg.get("user_id")
        raw_message = msg.get("raw_message")

    except Exception as e:
        logging.error(f"处理编解码消息失败: {e}")
        return
