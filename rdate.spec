Summary:	Remote clock reader (and local setter)
Summary(de):	Entfernter Uhrenleser (lokaler Einsteller)
Summary(es):	Lector de reloj remoto (y ajuste local)
Summary(fr):	Lecteur d'horloge distante (et configurateur local)
Summary(pl):	Program podaj╠cy (i ustawiaj╠cy) zdalny czas zegara
Summary(pt_BR):	Leitor de relСgio remoto (e ajustador local)
Summary(ru):	Программа для чтения удаленных часов и установки по ним местных
Summary(tr):	AП Эzerinden sistem saatini ayarlayan yazЩlЩm
Name:		rdate
Version:	1.3
Release:	8
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.gz
# Source0-md5: 67da8370335ad0ca7c82cdbe1c82976e
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.cron
Patch0:		%{name}-segfault.patch
Patch1:		%{name}-ipv6.patch
Requires(post,postun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	rdate-bsd

%description
rdate is a program that can retrieve the time from another machine on
your network. If run as root, it will also set your local time to that
of the machine you queried. It is not super accurate; get ntpd if you
are really worried about milliseconds.

%description -l de
rdate ist ein Programm, das die Uhrzeit von einem anderen
Netzwerkrechner lesen kann. Wenn Sie es als root ausfЭhren, stellt es
Ihre Ortszeit auf die des abgefragten Rechners ein. Es ist nicht sehr
genau. Wenn Sie auf die Millisekunde genau sein wollen, besorgen Sie
sich ntpd.

%description -l es
Rdate es un programa que puede retornar el tiempo (fecha/hora) de otra
mАquina en tu red. Si le ejecutas como root, tambiИn configurarА el
tiempo local como el de la mАquina solicitada. No es muy riguroso;
coge xntpd, si realmente te preocupa los milisegundos.

%description -l fr
rdate permet de rИcupИrer l'heure d'une autre machine du rИseau. s'il
est lancИ par root, il configurera aussi votre heure locale avec celle
de la machine que vous avez interrogИ. Il n'est pas trХs prИcis ; si
vous vous souciez des millisecondes, rИcupИrez ntpd.

%description -l pl
rdate jest programem ktСry odczytuje datЙ i godzinЙ z innej maszyny w
sieci. Je©eli jest uruchamiany jako root mo©e tak©e sЁu©yФ do
synchronizacji lokalnego czasu wzglЙdem innego komputera w sieci. Nie
jest zbyt dokЁadny i je©eli milisekundy maj╠ dla nas znaczenie nale©y
u©yФ ntpd.

%description -l pt_BR
Rdate И um programa que pode retornar o tempo (data/hora) de outra
mАquina na sua rede. Se rodar como root, ele tambИm irА configurar o
hora local como o da mАquina requisitada. Ele nЦo И super preciso;
pegue xntpd se vocЙ realmente se preocupa com milisegundos.

%description -l ru
Утилита rdate считывает дату и время с другой машины вашей сети
используя протокол описанный в RFC 868. Если вы запускаете rdate от
пользователя root, она также может установить время на локальной
машине в соответствии со временем на удаленной машине. Имейте в виду,
что rdate не отличается особенной точностью; если вы заботитесь о
миллисекундах, установите пакет xntp3, включающий демона xntpd.

%description -l tr
rdate ile herhangi baЧka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullanЩcЩ tarafЩndan ГalЩЧtЩrЩlЩrsa sistem saatini ayarlamak
da mЭmkЭndЭr. Ne var ki bu uygulama Гok hassas deПildir.

%description -l uk
Утил╕та rdate отриму╓ дату та час з ╕ншо╖ машини у ваш╕й мереж╕,
використовуючи протокол описаний в RFC 868. Якщо ви запуска╓те rdate
в╕д користувача root, вона також може встановити час на локальн╕й
машин╕ у в╕дпов╕дност╕ ╕з часом на в╕ддален╕й машин╕. Майте на уваз╕,
що rdate не в╕др╕зня╓ться особливою точн╕стю; якщо ви турбу╓тесь про
м╕л╕секунди, встанов╕ть пакет xntp3, який включа╓ демона xntpd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} clean
%{__make} CFLAGS="-DINET6 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/{cron.daily,rc.d/init.d,sysconfig}}

install rdate $RPM_BUILD_ROOT%{_bindir}
install rdate.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%post
/sbin/chkconfig --add rdate

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del rdate
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdate
%attr(755,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) /etc/cron.daily/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%{_mandir}/man1/*
