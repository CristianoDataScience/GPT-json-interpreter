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
    text = ''
    if "prompt" in input_data:
        prompt = input_data["prompt"]
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)
        text = tokenizer.decode(output[0], skip_special_tokens=True)

    return text

if __name__ == "__main__":
    while True:
        json_input = input("Digite o JSON de entrada (ou 'sair' para encerrar): ")
        
        if json_input.lower() == 'sair':
            break

        output_text = interpret_json(json_input)

        print("Texto gerado:")
        print(output_text)
