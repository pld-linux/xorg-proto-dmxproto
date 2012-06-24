Summary:	DMX protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu DMX i pomocnicze
Name:		xorg-proto-dmxproto
Version:	2.3
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/dmxproto-%{version}.tar.bz2
# Source0-md5:	880a41720b2937e2660dcdc0d34a8791
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DMX protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu DMX i pomocnicze.

%package devel
Summary:	DMX protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu DMX i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DMX protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu DMX i pomocnicze.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/dmxproto.pc
