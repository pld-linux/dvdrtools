# TODO: 
#   * Apply relevant patches from cdrtools

Summary:	A command line CD/DVD-Recorder
Summary(es.UTF-8):	Un programa de grabación de CD/DVD
Summary(pl.UTF-8):	Program do nagrywania płyt CD/DVD
Summary(pt_BR.UTF-8):	Um programa de gravação de CD/DVD
Summary(ru.UTF-8):	Программа для записи CD/DVD, запускаемая из командной строки
Summary(uk.UTF-8):	Програма для запису CD/DVD, яка запускається з командної стрічки
Name:		dvdrtools
Version:	0.3.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://www.arklinux.org/download/%{name}-%{version}.tar.bz2
# Source0-md5:	2eab3999d840910562b98cc83615c31c
Patch0:		%{name}-transcode.patch
URL:		http://www.arklinux.org/projects/dvdrtools
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	cdrecord = 5:2.0
Obsoletes:	cdrtools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dvdrecord allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl.UTF-8
Dvdrecord pozwala tworzyć CD na nagrywarce CD (SCSI/ATAPI). Obsługuje
dyski z danymi, dźwiękiem, mieszane, wielosesyjne, CD+ i inne.

%description -l pt_BR.UTF-8
Dvdrecord permite que você crie CDs em seu gravador de CDs SCSI/ATAPI.
É possível gravar dados, áudio, misturados, multi-seção e CD+.

%description -l ru.UTF-8
Dvdrecord - это программа для создания аудио и цифровых CD. Dvdrecord
работает со многими типами CD-рекордеров разных производителей,
полностью поддерживает multi-session и сообщает об ошибках в формате,
пригодном для чтения человеком.

%description -l uk.UTF-8
Dvdrecord - це програма для створення аудіо та програмних CD. Dvdrecord
працює з багатьма типами CD-рекордерів різних виробників, повністю
підтримує multi-session і повідомляє про помилки у форматі, придатному
для читання людиною.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es.UTF-8):	La biblioteca SCSI libschily
Summary(pl.UTF-8):	Biblioteka dostępu do poziomu SCSI przez użytkownika
Summary(pt_BR.UTF-8):	A biblioteca SCSI libschily
Summary(ru.UTF-8):	SCSI-библиотека libschily
Summary(uk.UTF-8):	SCSI-бібліотека libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel
Obsoletes:	cdrtools-devel

%description devel
The dvdrtools distribution contains a SCSI user level transport
library. The SCSI library is suitable to talk to any SCSI device
without having a special driver for it. Cdrecord may be easily ported
to any system that has a SCSI device driver similar to the scg driver.

%description devel -l pl.UTF-8
Dystrybucja dvdrtools zawiera bibliotekę dostępu do warstwy transportu
w SCSI. Poprzez bibliotekę można komunikować się z dowolnym
urządzeniem SCSI bez potrzeby posiadania specjalnego sterownika do
tego urządzenia.

%description devel -l pt_BR.UTF-8
O dvdrtools contém uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru.UTF-8
Пакет cdrecord-devel содержит транспортные библиотеки
пользовательского уровня для SCSI, которые могут работать с любым
SCSI-устройством без специального драйвера для этого устройства.
Cdrecord может быть легко портирован на любую систему с драйвером
SCSI-устройства, похожим на драйвер scg.

%description devel -l uk.UTF-8
Пакет cdrecord-devel містить транспортні бібліотеки користувацького
рівня для SCSI, які можуть працювати з будь-яким SCSI-пристроєм без
спеціального драйвера для цього пристрою. Cdrecord може бути легко
портований на будь-яку систему з драйвером SCSI-пристроя, схожим на
драйвер scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es.UTF-8):	Crea archivos tipo WAV a partir de CDs de audio
Summary(fr.UTF-8):	convertisseur CD-Audio->.WAV
Summary(pl.UTF-8):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR.UTF-8):	Cria arquivos tipo WAV a partir de CDs de áudio
Summary(ru.UTF-8):	Утилита для получения файлов .WAV с digital audio CD
Summary(uk.UTF-8):	Утиліта для генерації файлів .WAV з digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav = 5:2.0
Obsoletes:	cdrtools-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into WAV or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es.UTF-8
Un utilitario para leer músicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu máquina. Los
datos pueden ser grabados en formato WAV o sun. Existen opciones para
controlar el formato de la grabación (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl.UTF-8
Narzędzie do zczytywania danych z napędów cdrom, które są w stanie
wysyłać strumień audio. Dane mogą zostać zapisane w formacie plików
WAV lub suna.

%description cdda2wav -l pt_BR.UTF-8
Um utilitário para ler músicas em acionadores de cdrom capazes de
transmitir dados de CDs de áudio em forma digital para sua máquina. Os
dados podem ser gravados em formato WAV ou sun. Existem opções para
controlar o formato da gravação (estéreo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru.UTF-8
Cdda2wav - это сэмплер, способный считывать аудиоданные с CD в
цифровой форме и сохранять их на диск в виде звуковых файлов формата
.WAV или .sun. Форматы записи включают стерео/моно, 8/12/16 бит и
различные частоты дискретизации. Cdda2wav также может быть использован
как CD-плейер.

%description cdda2wav -l uk.UTF-8
Cdda2wav - це семплер, здатний зчитувати аудіодані і CD у цифровій
формі та зберігати їх на диск у вигляді звукових файлів формату .WAV
або .sun. Формати запису включають стерео/моно, 8/12/16 біт та різні
частоты дискретизації. Cdda2wav також може бути використаний як
CD-плейєр.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl.UTF-8):	Odczytuje/Zapisuje dane z Płyt Kompaktowych
Group:		Applications/System
Provides:	readcd = 5:2.0
Obsoletes:	cdrtools-readcd

%description readcd
Read/Write data Compact Discs.

%description readcd -l pl.UTF-8
Odczytuje/Zapisuje dane z Płyt Kompaktowych.

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl.UTF-8):	Zrzucanie i weryfikacja obrazów iso9660
Group:		Applications/System
Obsoletes:	cdrtools-utils

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl.UTF-8
Narzędzia do zrzucania i weryfikacji obrazów iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de.UTF-8):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es.UTF-8):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr.UTF-8):	Crée un image système de fichiers ISO9660
Summary(pl.UTF-8):	Tworzy obraz systemu plików ISO9660
Summary(pt_BR.UTF-8):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru.UTF-8):	Создает образ файловой системы ISO9660
Summary(tr.UTF-8):	ISO9660 dosya sistemi kopyası oluşturur
Summary(uk.UTF-8):	Створює образ файлової системи ISO9660
Group:		Applications/System
Provides:	mkisofs = 5:2.0
Provides:	cdrtools-mkisofs
Obsoletes:	cdrtools-mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es.UTF-8
Este es el paquete mkisofs. Se le usa para crear imágenes de sistema
de archivos ISO 9660 en la creación de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl.UTF-8
To jest pakiet mkisofs. Jest on używany do tworzenia obrazów systemów
plików ISO9660 potrzebnych do tworzenia płyt CD-ROM.

%description mkisofs -l pt_BR.UTF-8
Este é o pacote mkisofs. Ele é usado para criar imagens de sistema de
arquivos ISO 9660 para criação de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru.UTF-8
Программа mkisofs используется для подготовки мастер-диска, т.е. она
генерирует файловую систему ISO9660. Mkisofs делает снимок заданного
дерева каталогов и генерирует бинарный образ этого дерева, который
соответствует файловой системе ISO9660, записываемой на блочное
устройство. Mkisofs используется для записи CD-ROM'ов и включает
поддержку создания загружаемых El Torito CD-ROM'ов.

%description mkisofs -l uk.UTF-8
Програма mkisofs використовується для підготовки мастер-диску, вона
генерує файлову систему ISO9660. Mkisofs робить знімок заданого дерева
каталогів та генерує бінарный образ цього дерева, який відповідає
файловій системі ISO9660, записуваній на блочний пристрій. Mkisofs
використовується для запису CD-ROM'ів і має підтримку створення
завантажуваних El Torito CD-ROM'ів.

%package video
Summary:	Tools for mastering video DVDs
Summary(pl.UTF-8):	Narzędzie do tworzenia płyt video DVD
Group:		Applications/Multimedia
Requires:	transcode

%description video
Tools for mastering video DVDs. At the moment, you can write MPEG and
AVI videos to DVD, but you can not (yet) create DVD menus.

%description video -l pl.UTF-8
Narzędzie do tworzenia płyt video DVD. Umożliwia nagrywanie filmów w
formacie MPEG i AVI na płytę DVD, ale (jeszcze) bez tworzenia menu.

%prep
%setup -q 
%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/schily/scg,%{_mandir}/{man1,man8}}

%{__make} install \
	MANDIR=share/man \
	DESTDIR=$RPM_BUILD_ROOT

# fix manual pages
echo '.so isoinfo.8' > $RPM_BUILD_ROOT%{_mandir}/man8/devdump.8
echo '.so isoinfo.8' > $RPM_BUILD_ROOT%{_mandir}/man8/isovfy.8
echo '.so isoinfo.8' > $RPM_BUILD_ROOT%{_mandir}/man8/isodump.8

ln -sf %{_bindir}/dvdrecord \
        $RPM_BUILD_ROOT%{_bindir}/cdrecord
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/cdrecord
%attr(755,root,root) %{_bindir}/dvdrecord
%{_mandir}/man1/dvdrecord.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/schily

%files cdda2wav
%defattr(644,root,root,755)
%doc cdda2wav/Frontends cdda2wav/HOWTOUSE cdda2wav/OtherProgs
%doc cdda2wav/README cdda2wav/THANKS cdda2wav/TODO
%doc cdda2wav/cdda_links cdda2wav/pitchplay
%doc cdda2wav/readmult cdda2wav/tracknames.pl cdda2wav/tracknames.txt
%doc cdda2wav/FAQ
%attr(755,root,root) %{_bindir}/cdda2wav
%attr(755,root,root) %{_bindir}/cdda2mp3
%attr(755,root,root) %{_bindir}/cdda2ogg
%{_mandir}/man1/cdda2wav.1*

%files readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/readcd
%{_mandir}/man1/readcd.1*

%files utils
%defattr(644,root,root,755)
%doc mkisofs/diag/README
%attr(755,root,root) %{_bindir}/devdump
%attr(755,root,root) %{_bindir}/isodump
%attr(755,root,root) %{_bindir}/isoinfo
%attr(755,root,root) %{_bindir}/isovfy
%{_mandir}/man8/devdump.8*
%{_mandir}/man8/isodump.8*
%{_mandir}/man8/isoinfo.8*
%{_mandir}/man8/isovfy.8*

%files mkisofs
%defattr(644,root,root,755)
%doc mkisofs/README.compression mkisofs/README.eltorito mkisofs/README
%doc mkisofs/README.graft_dirs mkisofs/README.hfs_boot mkisofs/README.hfs_magic
%doc mkisofs/README.hide mkisofs/README.joliet
%doc mkisofs/README.prep_boot mkisofs/README.rootinfo mkisofs/README.session
%doc mkisofs/README.sort mkisofs/README.sparcboot
%attr(755,root,root) %{_bindir}/mkisofs
%{_mandir}/man8/mkisofs.8*

%files video
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ifogen
%attr(755,root,root) %{_bindir}/makecd
