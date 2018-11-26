-- 2 consultas envolvendo as operações de seleção e projeção;

-- Encontre as distros que tem todas as vogais e nenhum espaço em seu nome.

SELECT nome FROM distro 
	WHERE nome LIKE '%A%' 
	AND nome LIKE '%E%' 
	AND nome LIKE '%I%' 
	AND nome LIKE '%O%' 
	AND nome LIKE '%U%' 
	AND nome NOT LIKE '% %';

-- Selecione as distros que não são mantidas pela comunidade
SELECT * FROM distro
	WHERE maintainer <> "community"

		
-- 3 consultas envolvendo a junção de duas relações;

-- Crie uma lista de usuarios que usam as mesmas distros da usuaria Mirella Moro.
SELECT TRIM(U.nome) & ' ' & TRIM(U.sobrenome) AS nome_usuario , U.foto, U.idade, U.pais 
	FROM Usuario U, UsuarioDistro UD 
	WHERE (U.idusuario = UD.idusuario) 
	AND(nome <> 'Mirella' AND sobrenome <> 'Moro') 
	AND UD.distro = 
	  (SELECT distro FROM UsuarioDistro JOIN Distro
			WHERE distro = nome 
			AND idusuario =
				(SELECT id FROM Usuario WHERE nome = 'Mirella' AND sobrenome = 'Moro'))	

-- Calcular o valor de todos os mantenedores de distros baseadas nas mesmas distros  
SELECT D.nome, SUM(M.valor) AS maintainer_valor 
	FROM (distro AS D1 INNER JOIN distro AS D2 ON D1.nome=D2.basedOn) AS D, maintainer AS M 
	WHERE D.maintainer = M.nome 
	GROUP BY D.nome, 
	ORDER BY SUM(M.valor) DESC;	

-- Selecione a quantidade de distros que tem como ambiente desktop o GNOME
SELECT D.nome, count(DD.distro) AS quantidade 
	FROM Desktop D, Distro_Desktop AS DD 
	WHERE D.nome = DD.desktop ;
	
 
-- 3 consultas envolvendo a junção de três ou mais relações;

-- Mostre o nome do usuario e da distro onde as primeiras letras de cada são iguais. 	

SELECT nome, nome_usuario FROM Distro 
	NATURAL JOIN (SELECT nome AS nome_usuario FROM Usuario) as U 
	NATURAL JOIN UsuarioDistro
		WHERE LEFT(nome, 1) = LEFT(nome_usuario, 1) 
		XOR nome = nome_usuario;

SELECT D.nome, U.nome FROM Distro D, Usuario U, UsuarioDistro UD
		WHERE  (D.nome = UD.nome AND U.id = UD.userid) AND LEFT(D.nome, 1) = LEFT(U.nome, 1) 
		XOR D.nome = U.nome;

-- Qual a distribuição de Linux mais frequente entre usuários entre 40 e 60 anos de idade?
SELECT D.nome, max(count(*)) AS numero_usuarios FROM Distro D, Usuario U, UsuarioDistro UD
		WHERE  (D.nome = UD.nome AND U.id = UD.idusuario) 
		AND U.idade BETWEEN 40 AND 60; 	
	
-- Qual a porcentagem de usuários casuais que preferem usar distribuições rolling release?
SELECT (count(*) 100 / (SELECT count(*) FROM Usuario WHERE usoProfissional = 0)) AS porcentagem 
FROM Distro D, Usuario U, UsuarioDistro UD
		WHERE  (D.nome = UD.nome AND U.id = UD.idusuario) 
		AND usoProfissional = 0 AND D.tipo = "Rolling";

-- 2 consultas envolvendo funções de agregação sobre o resultado da junção de pelo menos duas relações
		
-- Selecione a distro com o maior número de usuarios

SELECT D.nome, SUM(U.nome) AS num_users FROM distro AS D 
	LEFT JOIN (usuario NATURAL JOIN UsuarioDistro) AS U 
	ON idusuario = distro
GROUP BY nome,
ORDER BY num_users

-- Selecionar a média de usuarios linux por país

SELECT pais, floor(avg(nome))FROM Usuario 
GROUP BY pais;