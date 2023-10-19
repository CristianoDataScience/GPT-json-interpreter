import tkinter as tk
from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Carregando o modelo GPT-2 em português do Brasil
model_name = "neuralmind/bert-large-portuguese-cased"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Função para gerar uma interpretação com base na série temporal de receita
def generate_interpretation(revenue_data):
    interpretation_text = f"Interpretação GPT:\nA série temporal apresenta a receita anual do time de beisebol St. Louis Cardinals, da MLB, entre os anos de {revenue_data['start_year']} e {revenue_data['end_year']}.\n"
    interpretation_text += f"A receita, expressa em milhões de dólares americanos, mostra um aumento notável ao longo desse período.\n"
    interpretation_text += f"Em {revenue_data['start_year']}, a receita era de ${revenue_data['start_revenue']} milhões e, gradualmente, cresceu para ${revenue_data['end_revenue']} milhões em {revenue_data['end_year']}, o que representa um aumento de mais de {revenue_data['percentage_increase']}% em quase duas décadas.\n"
    interpretation_text += f"A maior parte desse crescimento ocorreu na segunda metade do período, com destaque para o salto de ${revenue_data['mid_revenue']} milhões em {revenue_data['mid_year']} para ${revenue_data['end_revenue']} milhões em {revenue_data['end_year']}, um aumento de {revenue_data['percentage_mid_increase']}% em um período de sete anos.\n"
    interpretation_text += "Esta tendência ascendente indica um fortalecimento financeiro do St. Louis Cardinals ao longo dos anos analisados."
    return interpretation_text

# Função de callback para lidar com a entrada do usuário e gerar uma interpretação
def on_send_click():
    input_json = input_entry.get()
    try:
        revenue_data = json.loads(input_json)
        interpretation_text = generate_interpretation(revenue_data)
        output_textbox.config(state="normal")
        output_textbox.delete(1.0, "end")
        output_textbox.insert("end", interpretation_text)
        output_textbox.config(state="disabled")
    except json.JSONDecodeError:
        output_textbox.config(state="normal")
        output_textbox.delete(1.0, "end")
        output_textbox.insert("end", "Erro: O input não é um JSON válido. Tente novamente.")
        output_textbox.config(state="disabled")

# Configuração da interface
window = tk.Tk()
window.title("ChatGPT de Interpretação (Português do Brasil)")

input_label = tk.Label(window, text="Digite os dados da série temporal de receita (JSON):")
input_label.pack()

input_entry = tk.Entry(window, width=50)
input_entry.pack()

submit_button = tk.Button(window, text="Enviar", command=on_send_click)
submit_button.pack()

output_label = tk.Label(window, text="Interpretação gerada:")
output_label.pack()

output_textbox = tk.Text(window, wrap="word", height=10, width=50)
output_textbox.pack()

window.mainloop()



