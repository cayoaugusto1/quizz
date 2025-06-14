print("Quiz iniciado!")
import time
import threading
import sys

# Perguntas do quiz com imagens (usando emojis para simplicidade)
perguntas = [
    {
        "imagem": "🐍",
        "pergunta": "Qual é o nome desta linguagem de programação?",
        "opcoes": ["Java", "Python", "C++"],
        "resposta": 2  # índice começando em 1 para o usuário
    },
    {
        "imagem": "🌍",
        "pergunta": "Qual planeta é conhecido como o Planeta Azul?",
        "opcoes": ["Marte", "Terra", "Júpiter"],
        "resposta": 2
    },
    {
        "imagem": "⚽",
        "pergunta": "Qual esporte é conhecido como 'futebol'?",
        "opcoes": ["Basquete", "Vôlei", "Futebol"],
        "resposta": 3
    }
]

# Temporizador com timeout para resposta
def temporizador(timeout, flag):
    for i in range(timeout):
        time.sleep(1)
        if flag['answered']:
            return
    print("\nTempo esgotado! Você não respondeu a tempo.")
    flag['timeout'] = True

def quiz():
    print("=== Quiz Interativo ===")
    pontos = 0

    for i, pergunta in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: {pergunta['imagem']} {pergunta['pergunta']}")
        for idx, opcao in enumerate(pergunta['opcoes'], 1):
            print(f"{idx}. {opcao}")

        flag = {'answered': False, 'timeout': False}
        t = threading.Thread(target=temporizador, args=(10, flag))
        t.start()

        resposta = None
        while not flag['timeout']:
            try:
                resposta = input("Escolha a opção (1-3): ")
                if resposta in ['1','2','3']:
                    flag['answered'] = True
                    break
                else:
                    print("Digite 1, 2 ou 3.")
            except Exception:
                pass

        t.join()

        if flag['timeout']:
            print(f"A resposta correta era: {pergunta['resposta']}. {pergunta['opcoes'][pergunta['resposta']-1]}")
            continue

        if int(resposta) == pergunta['resposta']:
            print("Resposta certa! 🎉")
            pontos += 1
        else:
            print(f"Resposta errada! 😞 A resposta correta é: {pergunta['resposta']}. {pergunta['opcoes'][pergunta['resposta']-1]}")

    print(f"\nQuiz finalizado! Você acertou {pontos} de {len(perguntas)} perguntas.")

if __name__ == "__main__":
    quiz()