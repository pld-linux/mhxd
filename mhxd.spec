Summary:	HotlineX (hx) serwer
Summary(pl):	Serwer HotlineX (hx)
Name:		mhxd
Version:	0.4.9
Release:	0.2
License:	GPL
Group:		Networking/Utilities
Source0:	http://hx.fortyoz.org/%{name}-%{version}-common.tar.gz
# Source0-md5:	e4723cd569e195649123c87dac2ef9e2
Source1:	http://hx.fortyoz.org/%{name}-%{version}-modules.tar.gz
# Source1-md5:	722cac47b41571894aab78fe57fba4f7
Source2:	http://hx.fortyoz.org/%{name}-%{version}-hxd.tar.gz
# Source2-md5:	99eac28bcccc34fca13fd87c7e82332f
Source3:	http://hx.fortyoz.org/%{name}-%{version}-hxtrackd.tar.gz
# Source3-md5:	6b6d8b7b29c2b1d3df9c1d04b9285b01
Source4:	http://hx.fortyoz.org/%{name}-%{version}-hx.tar.gz
# Source4-md5:	e2ea01a3ea1ba4fcd0d374e3ad6f4fbb
Source5:	http://hx.fortyoz.org/%{name}-%{version}-ghx.tar.gz
# Source5-md5:	cd06200d14b4fc43219f9ea5e5a7533e
Source6:	http://hx.fortyoz.org/%{name}-%{version}-misc.tar.gz
# Source6-md5:	b08c30d236c1bb32222364eed043c390
Patch0:		%{name}-pic.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gtk+-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
URL:		http://hx.fortyoz.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HotlineX (hx) is an implementation of the Hotline protocol for un*x
based systems.

%description -l pl
Jest to pakiet pozwalaj±cy na udostêpnianie zasobów hotline pod
systemami z X w nazwie, BSD te¿ siê licz±.

%package hx
Summary:	HotlineX (hx) client
Summary(pl):	Klient HotlineX (hx)
Group:		Networking/Utilities

%description hx
HotlineX client.

%description hx -l pl
Klient HotlineX.

%package ghx
Summary:	HotlineX (hx) GTK client
Summary(pl):	Klient GTK HotlineX (hx)
Group:		Networking/Utilities

%description ghx
HotlineX GTK client.

%description ghx -l pl
Klient GTK HotlineX.

%prep
%setup -q -b1 -b2 -b3 -b4 -b5 -b6
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd libltdl
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd ..

CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--enable-irc \
	--disable-kdx \
	--enable-modules \
	--enable-hx \
	--enable-hxd \
	--enable-htxf-queue \
	--enable-gtk \
	--enable-dulled \
	--enable-translate \
	--enable-acctedit \
	--enable-hope \
	--enable-compress \
	--with-pthreads \
	--enable-idea \
	--enable-cipher \
	--enable-hfs \
	--enable-xmms \
	--enable-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/hxd
%attr(755,root,root) %{_bindir}/acctedit
%attr(755,root,root) %{_bindir}/hxd
%attr(755,root,root) %{_bindir}/genconf
%attr(755,root,root) %{_libdir}/hotline.so.*.*
%attr(755,root,root) %{_libdir}/irc.so.*.*

%files hx
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/hx

%files ghx
%defattr(644,root,root,755)
%doc README.gtk README ChangeLog TODO
%attr(755,root,root) %{_bindir}/ghx
