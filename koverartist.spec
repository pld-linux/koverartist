Summary:	KoverArtist - program for the fast creation of covers
Summary(pl):	KoverArtist - program do szybkiego tworzenia ok³adek
Name:		koverartist
Version:	0.3.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://members.inode.at/499177/software/koverartist/%{name}-%{version}.tar.bz2
# Source0-md5:	9c29f5b986ae7faf75e3f14e7b2e6760
URL:		http://www.kde-apps.org/content/show.php?content=38195
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libxml2-progs
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KoverArtist is a program for the fast creation of covers for cd/dvd
cases and boxes.

%description -l pl
KoverArtist jest programem do szybkiego tworzenia ok³adek p³yt CD i
DVD.

%prep
%setup -q -n %{name}

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
echo "Categories=Qt;KDE;AudioVideo;DiscBurning;" >> src/koverartist.desktop
echo "# vi: encoding=utf-8" >> src/koverartist.desktop
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/koverartist.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde/

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/hicolor/*x*/apps/*.png
%{_datadir}/apps/koverartist/cases/*.koac
%{_datadir}/apps/koverartist/koverartistui.rc
%{_datadir}/mimelnk/application/x-koverartist.desktop
%{_desktopdir}/kde/*.desktop
