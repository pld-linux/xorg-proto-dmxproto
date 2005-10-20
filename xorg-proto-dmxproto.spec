Summary:	DMX protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u DMX i pomocnicze
Name:		xorg-proto-dmxproto
Version:	2.2.1
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/dmxproto-%{version}.tar.bz2
# Source0-md5:	4ad016fe64688c54730b47551e96f7c1
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DMX protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u DMX i pomocnicze.

%package devel
Summary:	DMX protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u DMX i pomocnicze.
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
DMX protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u DMX i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/dmxproto.pc
