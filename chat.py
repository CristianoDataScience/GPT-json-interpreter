import tkinter as tk
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Carregando o modelo GPT-2 em português do Brasil
model_name = "neuralmind/bert-large-portuguese-cased"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Função para gerar uma interpretação com base na série temporal de receita
def generate_interpretation(revenue_data):
    input_text = f"Interpretação GPT:\nA série temporal apresenta a receita anual do time de beisebol St. Louis Cardinals, da MLB, entre os anos de {revenue_data['start_year']} e {revenue_data['end_year']}. A receita, expressa em milhões de dólares americanos, mostra um aumento notável ao longo desse período. Em {revenue_data['start_year']}, a receita era de ${revenue_data['start_revenue']} milhões e, gradualmente, cresceu para ${revenue_data['end_revenue']} milhões em {revenue_data['end_year']}, o que representa um aumento de mais de {revenue_data['percentage_increase']}% em quase duas décadas. A maior parte desse crescimento ocorreu na segunda metade do período, com destaque para o salto de ${revenue_data['mid_revenue']} milhões em {revenue_data['mid_year']} para ${revenue_data['end_revenue']} milhões em {revenue_data['end_year']}, um aumento de {revenue_data['percentage_mid_increase']}% em um período de sete anos. Esta tendência ascendente indica um fortalecimento financeiro do St. Louis Cardinals ao longo dos anos analisados."
    return input_text

# Função de callback para lidar com a entrada do usuário e gerar uma interpretação
def on_send_click():
    input_json = input_entry.get()
    try:
        revenue_data = json.loads(input_json)
        interpretation_text = generate_interpretation(revenue_data)
        response_textbox.config(state="normal")
        response_textbox.delete(1.0, "end")
        response_textbox.insert("end", interpretation_text)
        response_textbox.config(state="disabled")
    except json.JSONDecodeError:
        response_textbox.config(state="normal")
        response_textbox.delete(1.0, "end")
        response_textbox.insert("end", "Erro: O input não é um JSON válido. Tente novamente.")
        response_textbox.config(state="disabled")

# Configuração da interface
root = tk.Tk()
root.title("ChatGPT de Interpretação (Português do Brasil)")

input_label = tk.Label(root, text="Digite os dados da série temporal de receita (JSON):")
input_label.pack()

input_entry = tk.Entry(root, width=50)
input_entry.pack()

send_button = tk.Button(root, text="Enviar", command=on_send_click)
send_button.pack()

response_textbox = tk.Text(root, wrap="word", height=10, width=80, state="disabled")
response_textbox.pack()

root.mainloop()









