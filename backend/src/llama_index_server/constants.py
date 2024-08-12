NEBULA_EDGE_TYPES = ['relationship']
NEBULA_REL_PROP_NAMES = ['relationship']
NEBULA_STORE_TAGS = ['entity']

RAG_QUERY_ENGINE_TOOLS_MAPPING = {
    'asegptkg_rag_war': {
        'name':
        'war_query_engine_tool',
        'description':
        'Useful for answering questions about "China–United States trade war" and its impact on the world'
    },
    'asegptkg_rag_silicon': {
        'name':
        'silicon_query_engine_tool',
        'description':
        'Useful for answering questions about "Silicon Photonics development trend" and its impact on the world'
    },
    'asegptkg_rag_ai': {
        'name':
        'ai_query_engine_tool',
        'description':
        'Useful for answering questions about "Artificial Intelligence(AI)" and "AI Chips development trend" and its impact on the world'
    },
    'asegptkg_rag_semiconductor': {
        'name':
        'semiconductor_query_engine_tool',
        'description':
        'Useful for answering questions about "General Semiconductor development trend" or "Commonsense of Semiconductor".'
    }
}

DEFAULT_SYSTEM_PROMPT = 'You are a helpful assistant. Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.'

SYSTEM_PROMPT_SEMICONDUCTOR_ROLE = '''You are a semiconductor expert. Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request. Your answer is very important to me and will help whole company in decision making. Please help me complete the task and answer any questions. Please answer the questions in Chinese.
你是一位半導體專家。請你提供專業、有邏輯、內容真實且有價值的詳細回覆。你的回答對我非常重要，請幫助我完成任務，與解答任何疑惑。請使用中文回答問題。
'''