Summary:	HotlineX (hx) serwer
Summary(pl):	Serwer HotlineX (hx)
Name:		mhxd
Version:	0.4.9
Release:	0.1
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
URL:		http://hx.fortyoz.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HotlineX (hx) is an implementation of the Hotline protocol for un*x
based systems.

%description -l pl
Jest to pakiet pozwalaj±cy na udostêpnianie zasobów hotline pod
systemami z X w nazwie, BSD te¿ siê licz±.

%prep
%setup -q -b1 -b2 -b3 -b4 -b5 -b6

%build

%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc ChangeLog AUTHORS INSTALL NEWS PROBLEMS README*
#%attr(755,root,root) %{_bindir}/*
