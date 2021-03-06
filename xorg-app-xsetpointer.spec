Summary:	xsetpointer application
Summary(pl.UTF-8):	Aplikacja xsetpointer
Name:		xorg-app-xsetpointer
Version:	1.0.1
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xsetpointer-%{version}.tar.bz2
# Source0-md5:	9e5bcbeda4aaf02bfa095e41d30baee4
Source1:	xsetpointer.1x.it
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsetpointer application.

%description -l pl.UTF-8
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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/it/man1/xsetpointer.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xsetpointer
%{_mandir}/man1/xsetpointer.1*
%lang(it) %{_mandir}/it/man1/xsetpointer.1*
