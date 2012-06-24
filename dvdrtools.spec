# TODO: 
# 	* Package /usr/bin/{cdda2mp3,cdda2ogg,devdump,ifogen,isodump,isovfy,makecd}
#   * Apply relevant patches from cdrtools

Summary:	A command line CD/DVD-Recorder
Summary(es):	Un programa de grabaci�n de CD/DVD
Summary(pl):	Program do nagrywania p�yt CD/DVD
Summary(pt_BR):	Um programa de grava��o de CD/DVD
Summary(ru):	��������� ��� ������ CD/DVD, ����������� �� ��������� ������
Summary(uk):	�������� ��� ������ CD/DVD, ��� ������������ � �������ϧ ��Ҧ���
Name:		dvdrtools
Version:	0.2.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://savannah.nongnu.org/download/dvdrtools/%{name}-%{version}.tar.gz
# Source0-md5:	e82d359137e716e8c0b04d5c73bd3e79
URL:		http://www.nongnu.org/dvdrtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cdrecord allows you to create CD's on a CD-Recorder (SCSI/ATAPI).
Supports data, audio, mixed, multi-session and CD+ discs etc.

%description -l pl
Cdrecord pozwala tworzy� CD na nagrywarce CD (SCSI/ATAPI). Obs�uguje
dyski z danymi, d�wi�kiem, mieszane, wielosesyjne, CD+ i inne.

%description -l pt_BR
Cdrecord permite que voc� crie CDs em seu gravador de CDs SCSI/ATAPI.
� poss�vel gravar dados, �udio, misturados, multi-se��o e CD+.

%description -l ru
Cdrecord - ��� ��������� ��� �������� ����� � �������� CD. Cdrecord
�������� �� ������� ������ CD-���������� ������ ��������������,
��������� ������������ multi-session � �������� �� ������� � �������,
��������� ��� ������ ���������.

%description -l uk
Cdrecord - �� �������� ��� ��������� ��Ħ� �� ���������� CD. Cdrecord
������ � �������� ������ CD-�������Ҧ� Ҧ���� �������˦�, ���Φ���
Ц�����դ multi-session � ��צ����Ѥ ��� ������� � �����Ԧ, ����������
��� ������� �������.

%package devel
Summary:	The libschily SCSI user level transport library
Summary(es):	La biblioteca SCSI libschily
Summary(pl):	Biblioteka dost�pu do poziomu SCSI przez u�ytkownika
Summary(pt_BR):	A biblioteca SCSI libschily
Summary(ru):	SCSI-���������� libschily
Summary(uk):	SCSI-¦�̦����� libschily
Group:		Development/Libraries
Obsoletes:	cdrecord-devel

%description devel
The %{name} distribution contains a SCSI user level transport library.
The SCSI library is suitable to talk to any SCSI device without having
a special driver for it. Cdrecord may be easily ported to any system
that has a SCSI device driver similar to the scg driver.

%description devel -l pl
Dystrybucja %{name} zawiera bibliotek� dost�pu do warstwy transportu w
SCSI. Poprzez bibliotek� mo�na komunikowa� si� z dowolnym urz�dzeniem
SCSI bez potrzeby posiadania specjalnego sterownika do tego
urz�dzenia.

%description devel -l pt_BR
O dvdrtools cont�m uma biblioteca de transporte de dados por SCSI "user
level". A biblioteca SCSI pode ser usada para conversar com qualquer
dispositivo SCSI sem a necessidade de um driver especial.

%description devel -l ru
����� cdrecord-devel �������� ������������ ����������
����������������� ������ ��� SCSI, ������� ����� �������� � �����
SCSI-����������� ��� ������������ �������� ��� ����� ����������.
Cdrecord ����� ���� ����� ���������� �� ����� ������� � ���������
SCSI-����������, ������� �� ������� scg.

%description devel -l uk
����� cdrecord-devel ͦ����� ���������Φ ¦�̦����� ���������������
Ҧ��� ��� SCSI, �˦ ������ ��������� � ����-���� SCSI-������Ϥ� ���
���æ������� �������� ��� ����� ��������. Cdrecord ���� ���� �����
���������� �� ����-��� ������� � ��������� SCSI-��������, ������ ��
������� scg.

%package cdda2wav
Summary:	Get WAV files from digital audio cd's
Summary(es):	Crea archivos tipo WAV a partir de CDs de audio
Summary(fr):	convertisseur CD-Audio->.WAV
Summary(pl):	Uzyskaj pliki WAV z cyfrowego kompaktu audio
Summary(pt_BR):	Cria arquivos tipo WAV a partir de CDs de �udio
Summary(ru):	������� ��� ��������� ������ .WAV � digital audio CD
Summary(uk):	���̦�� ��� ������æ� ���̦� .WAV � digital audio CD
Group:		Applications/Sound
Provides:	cdda2wav
Obsoletes:	cdda2wav
Obsoletes:	cdrecord-cdda2wav

%description cdda2wav
A sampling utility for cdrom drives that are capable of sending audio
cd data in digital form to your host. Data can be dumped into WAV or
sun format sound files. Options control the recording format
(stereo/mono; 8,12,16 bits; different rates).

%description cdda2wav -l es
Un utilitario para leer m�sicas en accionadores de cdrom capaces de
transmitir datos de CDs de audio en forma digital para tu m�quina. Los
datos pueden ser grabados en formato WAV o sun. Existen opciones para
controlar el formato de la grabaci�n (stereo/mono, 8, 12, 16 bits,
tasas diferentes).

%description cdda2wav -l pl
Narz�dzie do zczytywania danych z nap�d�w cdrom, kt�re s� w stanie
wysy�a� strumie� audio. Dane mog� zosta� zapisane w formacie plik�w
WAV lub suna.

%description cdda2wav -l pt_BR
Um utilit�rio para ler m�sicas em acionadores de cdrom capazes de
transmitir dados de CDs de �udio em forma digital para sua m�quina. Os
dados podem ser gravados em formato WAV ou sun. Existem op��es para
controlar o formato da grava��o (est�reo/mono, 8, 12, 16 bits, taxas
diferentes).

%description cdda2wav -l ru
Cdda2wav - ��� �������, ��������� ��������� ����������� � CD �
�������� ����� � ��������� �� �� ���� � ���� �������� ������ �������
.WAV ��� .sun. ������� ������ �������� ������/����, 8/12/16 ��� �
��������� ������� �������������. Cdda2wav ����� ����� ���� �����������
��� CD-������.

%description cdda2wav -l uk
Cdda2wav - �� �������, ������� ��������� ��Ħ���Φ � CD � �����צ�
���ͦ �� ���Ҧ���� �� �� ���� � �����Ħ �������� ���̦� ������� .WAV
��� .sun. ������� ������ ��������� ������/����, 8/12/16 ¦� �� Ҧ�Φ
������� ����������æ�. Cdda2wav ����� ���� ���� ������������ ��
CD-���ʤ�.

%package readcd
Summary:	Read/Write data Compact Discs
Summary(pl):	Odczytuje/Zapisuje dane z P�yt Kompaktowych
Group:		Applications/System
Obsoletes:	cdrecord-readcd

%description readcd
Read/Write data Compact Discs.

%description readcd -l pl
Odczytuje/Zapisuje dane z P�yt Kompaktowych.

%package utils
Summary:	Dumping and verifying iso9660 images
Summary(pl):	Zrzucanie i weryfikacja obraz�w iso9660
Group:		Applications/System

%description utils
Utility programs for dumping and verifying iso9660 images.

%description utils -l pl
Narz�dzia do zrzucania i weryfikacji obraz�w iso9660.

%package mkisofs
Summary:	Creates an ISO9660 filesystem image
Summary(de):	Erstellt ein Dateisystem-Abbild nach ISO9660
Summary(es):	Crea una imagen de un sistema de archivos ISO9660
Summary(fr):	Cr�e un image syst�me de fichiers ISO9660
Summary(pl):	Tworzy obraz systemu plik�w ISO9660
Summary(pt_BR):	Cria uma imagem de um sistema de arquivos ISO9660
Summary(ru):	������� ����� �������� ������� ISO9660
Summary(tr):	ISO9660 dosya sistemi kopyas� olu�turur
Summary(uk):	������� ����� ������ϧ ������� ISO9660
Group:		Applications/System
Provides:	mkisofs
Obsoletes:	mkisofs

%description mkisofs
This is the mkisofs package. It is used to create ISO 9660 file system
images for creating CD-ROMs.

%description mkisofs -l es
Este es el paquete mkisofs. Se le usa para crear im�genes de sistema
de archivos ISO 9660 en la creaci�n de CD-ROMs. Ahora incluye soporte
para hacer CD-ROMs de boot "El Torito".

%description mkisofs -l pl
To jest pakiet mkisofs. Jest on u�ywany do tworzenia obraz�w system�w
plik�w ISO9660 potrzebnych do tworzenia p�yt CD-ROM.

%description mkisofs -l pt_BR
Este � o pacote mkisofs. Ele � usado para criar imagens de sistema de
arquivos ISO 9660 para cria��o de CD-ROMs. Agora inclui suporte para
fazer CD-ROMs de boot "El Torito".

%description mkisofs -l ru
��������� mkisofs ������������ ��� ���������� ������-�����, �.�. ���
���������� �������� ������� ISO9660. Mkisofs ������ ������ ���������
������ ��������� � ���������� �������� ����� ����� ������, �������
������������� �������� ������� ISO9660, ������������ �� �������
����������. Mkisofs ������������ ��� ������ CD-ROM'�� � ��������
��������� �������� ����������� El Torito CD-ROM'��.

%description mkisofs -l uk
�������� mkisofs ����������դ���� ��� Ц�������� ������-�����, ����
�����դ ������� ������� ISO9660. Mkisofs ������ �Φ��� �������� ������
������Ǧ� �� �����դ ¦������ ����� ����� ������, ���� צ���צ���
�����צ� �����ͦ ISO9660, ��������Φ� �� ������� �����Ҧ�. Mkisofs
����������դ���� ��� ������ CD-ROM'�� � ��� Ц������� ���������
�������������� El Torito CD-ROM'��.

%prep
%setup -q 
chmod +w -R *

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/schily/scg,%{_mandir}/{man1,man8}}

%{__make} install \
	MANDIR=share/man \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/cdrecord.ps README
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
%{_mandir}/man1/cdda2wav.1*

%files readcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/readcd
%{_mandir}/man1/readcd.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/isoinfo
%{_mandir}/man8/isoinfo.8*

%files mkisofs
%defattr(644,root,root,755)
%doc mkisofs/README.compression mkisofs/README.eltorito mkisofs/README
%doc mkisofs/README.graft_dirs mkisofs/README.hfs_boot mkisofs/README.hfs_magic
%doc mkisofs/README.hide mkisofs/README.joliet
%doc mkisofs/README.prep_boot mkisofs/README.rootinfo mkisofs/README.session
%doc mkisofs/README.sort mkisofs/README.sparcboot
%attr(755,root,root) %{_bindir}/mkisofs
%{_mandir}/man8/mkisofs.8*
