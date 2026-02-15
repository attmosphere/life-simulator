# Life Simulator

Life Simulator é um projeto em Python que criei para revisar meus conhecimentos em Python, em específico programação orientada a objetos. Feito para ser um "simulador de vida", contém classes que representam humanos (`Person` e `Worker`).
O projeto conta com:
- Verificação de morte
- Frases de morte

## Como Funciona?

Existe uma classe principal: `Person`, que se refere a uma pessoa, onde ela tem algumas funções que representam alguns dos processos básicos da vida: envelhecer (`get_older`) e morrer (`die`) (nome curto e grosso, né?).

<img width="391" height="79" alt="image" src="https://github.com/user-attachments/assets/245be6a4-8d5b-40b5-82e8-45bbe89ccc59" />

Essa classe recebe em seu construtor os seguintes parâmetros: `name` (referente ao nome da pessoa) e `age` (idade dela).

Filha dessa classe, existe uma subclasse `Worker`. A classe `Worker`, como o nome já diz, equivale a(o) trabalhador(a). 
Além dos parâmetros básicos que a classe pai toma, essa classe exige em seu construtor os parâmetros adicionais `job` (emprego) e `salary` (salário). 

<img width="383" height="38" alt="image" src="https://github.com/user-attachments/assets/8716ef37-73fa-48c3-ba5e-fbc5fc597074" />


## Conceitos Trabalhados

* Versionamento de Software (usando o **Git**)
* Programação Orientada a Objetos (OOP)
* Herança de Classes

## TODO
* Adicionar chances de morte proporcionais a idade da pessoa 
* Variação em relação a expectativa de vida, diferente para cada pessoa
* Passar do tempo automaticamente, afetando todas as variáveis pessoais (como o estado vida-morte e a idade)





      



