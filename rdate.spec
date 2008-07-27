Summary:	Remote clock reader (and local setter)
Summary(de.UTF-8):	Entfernter Uhrenleser (lokaler Einsteller)
Summary(es.UTF-8):	Lector de reloj remoto (y ajuste local)
Summary(fr.UTF-8):	Lecteur d'horloge distante (et configurateur local)
Summary(pl.UTF-8):	Program podający (i ustawiający) zdalny czas zegara
Summary(pt_BR.UTF-8):	Leitor de relógio remoto (e ajustador local)
Summary(ru.UTF-8):	Программа для чтения удаленных часов и установки по ним местных
Summary(tr.UTF-8):	Ağ üzerinden sistem saatini ayarlayan yazılım
Name:		rdate
Version:	1.4
Release:	5
License:	GPL v2
Group:		Networking/Utilities
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.gz
# Source0-md5:	b2e5bbfa10ec480076750fd78fe7f7a5
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.cron
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Obsoletes:	rdate-bsd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdate is a program that can retrieve the time from another machine on
your network. If run as root, it will also set your local time to that
of the machine you queried. It is not super accurate; get ntpd if you
are really worried about milliseconds.

%description -l de.UTF-8
rdate ist ein Programm, das die Uhrzeit von einem anderen
Netzwerkrechner lesen kann. Wenn Sie es als root ausführen, stellt es
Ihre Ortszeit auf die des abgefragten Rechners ein. Es ist nicht sehr
genau. Wenn Sie auf die Millisekunde genau sein wollen, besorgen Sie
sich ntpd.

%description -l es.UTF-8
Rdate es un programa que puede retornar el tiempo (fecha/hora) de otra
máquina en tu red. Si le ejecutas como root, también configurará el
tiempo local como el de la máquina solicitada. No es muy riguroso;
coge xntpd, si realmente te preocupa los milisegundos.

%description -l fr.UTF-8
rdate permet de récupérer l'heure d'une autre machine du réseau. s'il
est lancé par root, il configurera aussi votre heure locale avec celle
de la machine que vous avez interrogé. Il n'est pas très précis ; si
vous vous souciez des millisecondes, récupérez ntpd.

%description -l pl.UTF-8
rdate jest programem który odczytuje datę i godzinę z innej maszyny w
sieci. Jeżeli jest uruchamiany jako root może także służyć do
synchronizacji lokalnego czasu względem innego komputera w sieci. Nie
jest zbyt dokładny i jeżeli milisekundy mają dla nas znaczenie należy
użyć ntpd.

%description -l pt_BR.UTF-8
Rdate é um programa que pode retornar o tempo (data/hora) de outra
máquina na sua rede. Se rodar como root, ele também irá configurar o
hora local como o da máquina requisitada. Ele não é super preciso;
pegue xntpd se você realmente se preocupa com milisegundos.

%description -l ru.UTF-8
Утилита rdate считывает дату и время с другой машины вашей сети
используя протокол описанный в RFC 868. Если вы запускаете rdate от
пользователя root, она также может установить время на локальной
машине в соответствии со временем на удаленной машине. Имейте в виду,
что rdate не отличается особенной точностью; если вы заботитесь о
миллисекундах, установите пакет xntp3, включающий демона xntpd.

%description -l tr.UTF-8
rdate ile herhangi başka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullanıcı tarafından çalıştırılırsa sistem saatini ayarlamak
da mümkündür. Ne var ki bu uygulama çok hassas değildir.

%description -l uk.UTF-8
Утиліта rdate отримує дату та час з іншої машини у вашій мережі,
використовуючи протокол описаний в RFC 868. Якщо ви запускаєте rdate
від користувача root, вона також може встановити час на локальній
машині у відповідності із часом на віддаленій машині. Майте на увазі,
що rdate не відрізняється особливою точністю; якщо ви турбуєтесь про
мілісекунди, встановіть пакет xntp3, який включає демона xntpd.

%prep
%setup -q

%build
%{__make} clean
%{__make} \
	CFLAGS="-DINET6 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/{cron.daily,rc.d/init.d,sysconfig}}

install rdate $RPM_BUILD_ROOT%{_bindir}
install rdate.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add rdate

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del rdate
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdate
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) /etc/cron.daily/%{name}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%{_mandir}/man1/*
