import streamlit as st
import json
import time

st.title("Worker Node")

# Indicador de status (opcional)
status_placeholder = st.empty()
status_placeholder.info("Worker aguardando tarefa...")

def process_task(params):
    """Função de exemplo para processar uma tarefa."""
    time.sleep(2) # Simula um trabalho de processamento
    result = sum(params.get("numbers", []))
    return result

# Endpoint para receber tarefas
task_json = st.text_area("Enviar Tarefa (JSON)", height=150)
run_button = st.button("Executar Tarefa")

if run_button and task_json:
    try:
        task_params = json.loads(task_json)
        status_placeholder.info("Tarefa recebida e em processamento...")
        result = process_task(task_params)
        status_placeholder.success(f"Tarefa concluída! Resultado: {result}")
    except json.JSONDecodeError:
        status_placeholder.error("Erro: JSON inválido.")
    except Exception as e:
        status_placeholder.error(f"Ocorreu um erro: {e}")

# Simples "ping" para manter o app ativo (opcional, mas útil para debug)
st.sidebar.header("Status")
last_ping = st.sidebar.empty()
last_ping.write(f"Último ping: {time.strftime('%H:%M:%S')}")
time.sleep(1) # Pequena pausa para não sobrecarregar em testes locais
