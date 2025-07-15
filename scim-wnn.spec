# TODO: gtk3 patch
Summary:	SCIM IMEngine module for Wnn Japanese input
Summary(pl.UTF-8):	Silnik IM SCIM dla metody wprowadzania znaków japońskich Wnn
Name:		scim-wnn
Version:	1.0.0
Release:	0.1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://osdn.jp/projects/scim-imengine/releases/p3292
Source0:	http://dl.osdn.jp/scim-imengine/19759/%{name}-%{version}.tar.gz
# Source0-md5:	0f1c69149a13663e6bcd3ea037a41cf5
Patch0:		%{name}-no-rpath.patch
#Patch1:		%{name}-gtk3.patch
Patch2:		%{name}-include.patch
URL:		https://osdn.jp/projects/scim-imengine/
BuildRequires:	Wnn7-SDK-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.4
Requires:	Wnn7-SDK
Requires:	scim >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM IMEngine module for Wnn Japanese input.

%description -l pl.UTF-8
Silnik IM SCIM dla metody wprowadzania znaków japońskich Wnn.

%prep
%setup -q
%patch -P0 -p1
#patch1 -p1
%patch -P2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%lang(ja) %doc README.ja
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/wnn.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/wnn-imengine-setup.so
%{_datadir}/scim/icons/scim-wnn.png
%{_datadir}/scim/scim-wnn
