create table public.nuvens(
	cod int primary key,
	nome varchar(100) not null,
	login varchar(100) not null
);

create table public.foldersync(
	cod int primary key,
	nome varchar(60) not null,
	nuvem int not null,
	hora varchar(10) not null,
	dias varchar(50) not null,
	foreign key(nuvem) references public.nuvens(cod)
);

create table public.notebook(
	cod int primary key,
	diretorio varchar(150) not null,
	nuvem int not null,
	foreign key(nuvem) references public.nuvens(cod)
);

create table public.diretorios(
	cod int primary key,
	diretorio varchar(150) not null,
	nuvem int,
	dvd boolean,
	tamanho float(32),
	foreign key(nuvem) references public.nuvens(cod)
);

create table public.discos(
	cod int primary key,
	descricao varchar(500) not null,
	tipo varchar(5)
);

create table public.arquivo(
	cod int primary key,
	nuvem int,
	disco int,
	descricao varchar(500),
	foreign key(nuvem) references nuvens(cod),
	foreign key(disco) references discos(cod)
);	