# $Rev: 3420 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xsetpointer application
Summary(pl):	Aplikacja xsetpointer
Name:		xorg-app-xsetpointer
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xsetpointer-%{version}.tar.bz2
# Source0-md5:	538b8a73d04777c71b81b9970b6cc161
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xsetpointer-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xsetpointer application.

%description -l pl
Aplikacja xsetpointer.


%prep
%setup -q -n xsetpointer-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
