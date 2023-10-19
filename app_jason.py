import sys
import json
from transformers import GPT2LMHeadModel, GPT2TokenizerFast

# Carregando o modelo GPT-2 pré-treinado
model_name = "gpt2"  # Você pode escolher um modelo diferente se desejar
tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Função para interpretar JSON e gerar texto
def interpret_json(json_input):
    # Analisar o JSON de entrada
    try:
        input_data = json.loads(json_input)
    except json.JSONDecodeError as e:
        return f"Erro ao analisar o JSON de entrada: {str(e)}"

    # Gerar texto com base no JSON interpretado
    text = ""
    if "prompt" in input_data:
        prompt = input_data["prompt"]
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
        text = tokenizer.decode(output[0], skip_special_tokens=True)

    return text

# Função para ler a entrada JSON do arquivo
def read_input_json_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        json_input = file.read()
    return json_input

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: ./arquivo_1.json, arquivo_2.json, arquivo_3.json, arquivo_4.json")
        sys.exit(1)

    input_file = sys.argv[1]
    json_input = read_input_json_file(input_file)
    output_text = interpret_json(json_input)

    print("Texto gerado:")
    print(output_text)



