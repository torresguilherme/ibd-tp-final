-- 2 consultas envolvendo as operações de seleção e projeção;

-- Encontre as distros que tem todas as vogais e nenhum espaço em seu nome.

SELECT nome FROM distro 
	WHERE nome LIKE '%A%' 
	AND nome LIKE '%E%' 
	AND nome LIKE '%I%' 
	AND nome LIKE '%O%' 
	AND nome LIKE '%U%' 
	AND nome NOT LIKE '% %';


-- 3 consultas envolvendo a junção de duas relações;

-- Crie uma lista de usuarios que usam as mesmas distros da usuaria Mirella Moro.
SELECT TRIM(U.nome) & ' ' & TRIM(U.sobrenome) AS nome_usuario , U.foto, U.idade, U.país 
	FROM Usuario U, Usuario-Distro UD 
	WHERE (U.id = UD.userid) 
	AND(nome <> 'Mirella' AND sobrenome <> 'Moro') 
	AND UD.distroid = 
	  (SELECT UD.distroid FROM Usuario-Distro NATURAL JOIN Distro
			WHERE userid =
				(SELECT id FROM Usuario WHERE nome = 'Mirella' AND sobrenome = 'Moro'))	

-- Calcular o valor de todos os mantenedores de distros baseadas nas mesmas distros  
SELECT D.nome, SUM(M.valor) AS mainteiner_valor 
	FROM (distros AS D1 INNER JOIN distros AS D2 ON D1.nome=D2.based_on) AS D, mainteiner AS M 
	WHERE D.mainteiner = M.nome 
	GROUP BY D.nome, 
	ORDER BY SUM(M.valor) DESC;

-- 3 consultas envolvendo a junção de três ou mais relações;

-- Mostre o nome do usuario e da distro onde as primeiras letras de cada são iguais. 	

SELECT nome, nome_usuario FROM Distro 
	NATURAL JOIN (SELECT nome AS nome_usuario FROM Usuario) as U 
	NATURAL JOIN Usuario-Distro
		WHERE LEFT(nome, 1) = LEFT(nome_usuario, 1) 
		XOR nome = nome_usuario;

SELECT D.nome, U.nome FROM Distro D, Usuario U, Usuario-Distro UD
		WHERE  (D.nome = UD.nome AND U.id = UD.userid) AND LEFT(D.nome, 1) = LEFT(U.nome, 1) 
		XOR D.nome = U.nome;
	

-- 2 consultas envolvendo funções de agregação sobre o resultado da junção de pelo menos duas relações
		
-- Selecione a distro com o maior número de usuarios
SELECT D.nome, SUM(U.nome) AS num_usersFROM distro AS D 
	LEFT JOIN (usuario NATURAL JOIN usuario_distro) AS U 
	ON userid = distroid
GROUP BY nome,
ORDER BY num_users

-- Selecionar a média de usuarios linux por país
SELECT país, floor(avg(nome))FROM Usuario 
GROUP BY país;




