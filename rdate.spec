Summary:     Remote clock reader (and local setter)
Summary(de): Entfernter Uhrenleser (lokaler Einsteller)
Summary(fr): Lecteur d'horloge distante (et configurateur local)
Summary(pl): Program podaj±cy (i ustawiaj±cy) zdalny czas zegara
Summary(tr): Að üzerinden sistem saatini ayarlayan yazýlým
Name:        rdate
%define      versionmajor 0
%define      versionminor 960923
Version:     %{versionmajor}.%{versionminor}
Release:     1
Copyright:   none
Group:       Networking/Utilities
Source:      ftp://sunsite.unc.edu/pub/Linux/system/network/misc/%{name}-%{versionminor}.tar.gz
Buildroot:   /tmp/%{name}-%{release}-root

%description
rdate is a program that can retrieve the time from another machine on your
network.  If run as root, it will also set your local time to that of the
machine you queried.  It is not super accurate; get xntpd if you are really
worried about milliseconds.

%description -l de
rdate ist ein Programm, das die Uhrzeit von einem anderen Netzwerkrechner
lesen kann. Wenn Sie es als root ausführen, stellt es Ihre Ortszeit auf die
des abgefragten Rechners ein. Es ist nicht sehr genau. Wenn Sie auf die
Millisekunde genau sein wollen, besorgen Sie sich xntpd .

%description -l fr
rdate permet de récupérer l'heure d'une autre machine du réseau. s'il est
lancé par root, il configurera aussi votre heure locale avec celle de la
machine que vous avez interrogé. Il n'est pas très précis ; si vous vous
souciez des millisecondes, récupérez xntpd.

%description -l pl
rdate jest programem który odczytujê datê i godzinê z innej maszyny w sieci.
Je¿eli jest uruchamiany jako root mo¿e tak¿e s³u¿yæ do synchronizacji
lokalnego wzglêdem innego komputera w sieci. Nie jest zbyt dok³adny i je¿eli
milisekundy maj± dla ciebie znaczenie u¿yj xntpd.

%description -l tr
rdate ile herhangi baþka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullanýcý tarafýndan çalýþtýrýlýrsa sistem saatini ayarlamak da
mümkündür. Ne var ki bu uygulama çok hassas deðildir.

%prep
%setup -q -n %{name}

%build
make clean
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s rdate $RPM_BUILD_ROOT/usr/bin
install rdate.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/bin/rdate
%attr(644, root,  man) /usr/man/man1/rdate.1

%changelog
* Thu Oct 13 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.960923-6]
- removed patching Makefile (now $RPM_OPT_FLAGS in CFLAGS is passed directly
  in make parameters).

* Sun Oct 11 1998 Marek Obuchowicz <elephant@shadow.eu.org>
- some other modifications of spec file,
- build from non-root account,
- fixed file permissons.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Otto Hammersmith <otto@redhat.com>
- fixed the url to the source

* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
