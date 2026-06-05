import streamlit as st
from zhipuai import ZhipuAI

client = ZhipuAI(api_key=st.secrets["ZHIPU_API_KEY"])

st.title("👑 谢鹏辉大王")

# 初始化对话历史
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你是一个helpful的助手，回答简洁友好"}
    ]

# 显示历史消息
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 用户输入
user_input = st.chat_input("说点什么...")

if user_input:
    # 添加用户消息
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # AI回复
    with st.chat_message("assistant"):
        with st.spinner("思考中..."):
            response = client.chat.completions.create(
                model="glm-4-flash",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.write(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
