Summary:	Remote clock reader (and local setter)
Summary(fr):	Lecteur d'horloge distante (et configurateur local)
Summary(de):	Entfernter Uhrenleser (lokaler Einsteller)
Summary(pl):	Program podaj±cy (i ustawiaj±cy) zdalny czas zegara
Summary(tr):	Að üzerinden sistem saatini ayarlayan yazýlým
Name:		rdate
%define		versionmajor 0
%define		versionminor 990821
Version:	%{versionmajor}.%{versionminor}
Release:	2
License:	none
Group:		Networking/Utilities
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/misc/%{name}-%{versionminor}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdate is a program that can retrieve the time from another machine on
your network. If run as root, it will also set your local time to that
of the machine you queried. It is not super accurate; get ntpd if you
are really worried about milliseconds.

%description -l de
rdate ist ein Programm, das die Uhrzeit von einem anderen
Netzwerkrechner lesen kann. Wenn Sie es als root ausführen, stellt es
Ihre Ortszeit auf die des abgefragten Rechners ein. Es ist nicht sehr
genau. Wenn Sie auf die Millisekunde genau sein wollen, besorgen Sie
sich ntpd.

%description -l fr
rdate permet de récupérer l'heure d'une autre machine du réseau. s'il
est lancé par root, il configurera aussi votre heure locale avec celle
de la machine que vous avez interrogé. Il n'est pas très précis ; si
vous vous souciez des millisecondes, récupérez ntpd.

%description -l pl
rdate jest programem który odczytuje datê i godzinê z innej maszyny w
sieci. Je¿eli jest uruchamiany jako root mo¿e tak¿e s³u¿yæ do
synchronizacji lokalnego czasu wzglêdem innego komputera w sieci. Nie
jest zbyt dok³adny i je¿eli milisekundy maj± dla nas znaczenie nale¿y
u¿yæ ntpd.

%description -l tr
rdate ile herhangi baþka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullanýcý tarafýndan çalýþtýrýlýrsa sistem saatini ayarlamak
da mümkündür. Ne var ki bu uygulama çok hassas deðildir.

%prep
%setup -q -n %{name}-%{versionminor}

%build
%{__make} clean
%{__make} CFLAGS="-DINET6 %{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install rdate $RPM_BUILD_ROOT%{_bindir}
install rdate.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdate
%{_mandir}/man1/*
