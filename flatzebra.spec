Summary:	A Generic Game Engine library for 2D double-buffering animation
Summary(pl):	Ogólny silnik gier z podwójnie buforowan± animacj± 2D
Name:		flatzebra
Version:	0.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www3.sympatico.ca/sarrazip/dev/%{name}-%{version}.tar.gz
# Source0-md5:	c6c2002f9da4d4dca4934ce41c094965
Patch0:		%{name}-link.patch
BuildRequires:	SDL-devel >= 1.2.7
BuildRequires:	SDL_image-devel >= 1.2.3
BuildRequires:	SDL_mixer-devel >= 1.2.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	SDL >= 1.2.7
Requires:	SDL_image >= 1.2.3
Requires:	SDL_mixer >= 1.2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%description -l fr
Moteur de jeu générique utilisé par BurgerSpace, Afternoon Stalker
et Cosmosmash.

%description -l pl
Biblioteka ogólnego silnika gier s³u¿±ca miêdzy innymi dla gier
BurgerSpace, Afternoon Stalker i Cosmosmash.

%package devel
Summary:	C++ header files for FlatZebra library
Summary(fr):	En-têtes C++ pour la librairie FlatZebra
Summary(pl):	Pliki nag³ówkowe C++ biblioteki FlatZebra
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel >= 1.2.4
Requires:	SDL_image-devel >= 1.2.2
Requires:	SDL_mixer-devel >= 1.2.4
Requires:	libstdc++-devel

%description devel
C++ header files for FlatZebra library.

%description devel -l fr
En-têtes C++ pour la librairie FlatZebra.

%description devel -l pl
Pliki nag³ówkowe C++ biblioteki FlatZebra.

%package static
Summary:	Static FlatZebra library
Summary(pl):	Statyczna biblioteka FlatZebra
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static FlatZebra library.

%description static -l pl
Statyczna biblioteka FlatZebra.

%prep
%setup -q
%patch -p1

%build
# supplied libtool is broken (no C++ support)
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
