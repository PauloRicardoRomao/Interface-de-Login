/*create database Usuario_basico
use Usuario_basico
*/
create table tb_usuario
(
cod_usuario int identity primary key,
nome_usuario varchar(70) not null,
senha_usuario char(10) not null,
email_usuario varchar(40) null
)

go

create procedure sp_cadastro_usuario
	@nome varchar(70),
	@senha char(10),
	@email varchar(40)
as
begin
	insert into tb_usuario
	values
	(@nome, @senha, @email)
end
go
exec sp_cadastro_usuario 'Paulo', '123456', 'pauloromao.dev2020@gmail.com'
go

select COUNT(*) as total_usuarios from tb_usuario

select*from tb_usuario where nome_usuario like '%Erika%' and senha_usuario like '%987654321%'

select COUNT(*) as total_usuarios from tb_usuario where nome_usuario like '%Erika%' and senha_usuario like '%987654321%'
select COUNT(*) as total_usuarios from tb_usuario where nome_usuario like '%asdasdasd%' and senha_usuario like '%asdasdsad%'

