# movie-rater-project

`Pedro Antônio Silva e Gustavo Lindenberg Pacheco`

https://github.com/gustavolp1/movie-rater-project

## Como instalar e executar

> git clone git@github.com:gustavolp1/cube-rotato.git

(Entre no diretório do repositório)

> pip install -r "requirements.txt"

## Como usar o programa

Abra `demo.ipynb` e rode todas as células. Note que o processo inteiro pode demorar algumas horas.

## Modelo Matemático

As notas reais para cada filme são representadas pela matriz `A`, onde cada linha é um usuário e cada coluna é um filme. Um exemplo de um cenário onde existem 3 usuários e 4 filmes, com notas de 0 a 5:

$$
A =
\begin{bmatrix}
3 & 1.5 & 4 & 5 \\
4 & 5 & 3 & 5 \\
1 & 0 & 4.5 & 2
\end{bmatrix}
$$

O objetivo é, recebendo uma matriz `B`, que é uma cópia de `A` com um ou mais erros, estimar os valores reais contidos em `A`. Este princípio teoricamente pode ser usado para prever um valor de `A` não atribuído a `B`.

Tanto `A` quanto `B` podem ser decompostas como a seguinte multiplicação matricial:

$$
A = XYZ
$$

Onde:

`X` representa os autovetores em uma matriz de usuários por linhas e perfis por coluna.

`Y` mapeia um perfil com outro, em uma matriz quadrada de usuários por linhas e perfis por coluna, que nos permite selecionar valores por um critério.

`Z` representa os autovalores em uma matriz que relaciona perfis com filmes.

- explicar que decompoe

- X sao autovetores

- Y serve pra selecionar os valores q a gnt quer; eh quadrada pq compara o perfil de um usuario com o de outro

- 

# To do

fazer a descrição do modelo/ readme

fazer demo.py

checar com a rubrica