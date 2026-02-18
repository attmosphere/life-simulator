# Life Simulator

Life Simulator é um projeto em Python que criei para revisar meus conhecimentos em Python, em específico programação orientada a objetos. Feito para ser um "simulador de vida", contém classes que representam humanos (`Person` e `Worker`).
O projeto conta com:
- Verificação de morte
- Frases de morte
- Envelhecimento
- Suporte multilinguagem (português e inglês)
- Entrada (input) do usuário, conferindo dinamicidade ao programa

<img width="400" height="200" src="https://github.com/user-attachments/assets/a9c0e018-ef2a-40c9-a762-e582b455a694">


## Como Rodar?

Execute esse comando no seu terminal de preferência, com a pasta do repositório aberta:

`python main.py`

## Como Funciona?

Existe uma classe principal: `Person`, que se refere a uma pessoa, onde ela tem algumas funções que representam alguns dos processos básicos da vida: envelhecer (`get_older`) e morrer (`die`) (nome curto e grosso, né?).

<img width="391" height="79" alt="image" src="https://github.com/user-attachments/assets/245be6a4-8d5b-40b5-82e8-45bbe89ccc59" />

Essa classe recebe em seu construtor os seguintes parâmetros: `name` (referente ao nome da pessoa) e `age` (idade dela).

Filha dessa classe, existe uma subclasse `Worker`. A classe `Worker`, como o nome já diz, equivale a(o) trabalhador(a). 
Além dos parâmetros básicos que a classe pai toma, essa classe exige em seu construtor os parâmetros adicionais `job` (emprego) e `salary` (salário).

<img width="383" height="38" alt="image" src="https://github.com/user-attachments/assets/8716ef37-73fa-48c3-ba5e-fbc5fc597074" />

Seguindo a estrutura da aplicação, temos uma configuração de idioma.

<img width="305" height="52" alt="image" src="https://github.com/user-attachments/assets/dd7bd63f-3012-4f10-a4f4-345ad95c1919" />

A partir da opção selecionada pelo usuário, todos os textos do programa se adaptam ao idioma. 
O usuário então recebe um menu com opções: **criar** alguém, **matar** alguém, ou **mostrar a população** (pessoas criadas).

<img width="321" height="184" alt="menu-pt" src="https://github.com/user-attachments/assets/7925a90b-869e-46e4-b813-0358c0b32fc6" />

<img width="321" height="184" alt="menu-en" src="https://github.com/user-attachments/assets/22cb5ee1-a7dc-4382-a001-281999e57357" />

A configuração de idioma funciona por meio de um dicionário que possui os subdicionários `pt` e `en`. Cada item desses dicionários contém textos, em seu respectivo idiomas, usados pelo programa. Quando o usuário coloca "pt" ou "en", o programa passa a usar o dicionário do mesmo nome.

## Conceitos Trabalhados

* Versionamento de Software (usando o **Git**)
* Programação Orientada a Objetos (**OOP**)
* Herança de Classes 
* **UX** básica
* **Polimorfismo** 

## TODO
* ~~Adicionar chances de morte proporcionais a idade da pessoa~~
* ~~Variação em relação a expectativa de vida, diferente para cada pessoa~~
* ~~Passar do tempo automaticamente, afetando todas as variáveis pessoais (como o estado vida-morte e a idade)~~ (função não implementada; descartada por ser inviável)
* ~~Suporte multilingual~~






      



