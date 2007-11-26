%define name		marst
%define version		2.4
%define release		2mdk

Name:		%{name}
Summary:	Algol-to-C translator
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-automake-texinfo.patch.bz2
URL:		http://www.gnu.org/software/marst/marst.html
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	texinfo autoconf2.5 automake1.8

%description
MARST is an Algol-to-C translator. It automatically translates programs written
in the algorithmic language Algol 60 to the C programming language.

%prep
%setup -q
%patch0 -p1

%build
export FORCE_AUTOCONF_2_5=1
aclocal-1.8
autoconf-2.5x
automake-1.8 --foreign -a
%configure --disable-dependency-tracking
%make
%make info

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root,0755) 
%doc AUTHORS ChangeLog COPYING README examples
%{_libdir}/libalgol.a
%{_includedir}/algol.h
%{_bindir}/macvt
%{_bindir}/marst
%{_infodir}/%{name}.info*

