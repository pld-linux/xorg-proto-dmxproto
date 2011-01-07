Summary:	DMX extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia DMX
Name:		xorg-proto-dmxproto
Version:	2.3.1
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dmxproto-%{version}.tar.bz2
# Source0-md5:	4ee175bbd44d05c34d43bb129be5098a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DMX (Distributed Multihead X) extension defines a protocol for clients
to access a front-end proxy X server that controls multiple back-end X
servers making up a large display.

%description -l pl.UTF-8
Rozszerzenie DMX (Distributed Multihead X) definiuje protokół
pozwalający klientom na dostęp do frontendowego serwera proxy X
sterującego wieloma backendowymi serwerami X tworzącymi duży ekran.

%package devel
Summary:	DMX extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia DMX
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DMX (Distributed Multihead X) extension defines a protocol for clients
to access a front-end proxy X server that controls multiple back-end X
servers making up a large display.

%description devel -l pl.UTF-8
Rozszerzenie DMX (Distributed Multihead X) definiuje protokół
pozwalający klientom na dostęp do frontendowego serwera proxy X
sterującego wieloma backendowymi serwerami X tworzącymi duży ekran.

%prep
%setup -q -n dmxproto-%{version}

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

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%{_includedir}/X11/extensions/dmx*.h
%{_pkgconfigdir}/dmxproto.pc
