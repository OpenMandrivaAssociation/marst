%define name		marst
%define version		2.4
%define release		 %mkrel 6

Name:		%{name}
Summary:	Algol-to-C translator
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-%{version}-automake-texinfo.patch.bz2
URL:		http://www.gnu.org/software/marst/marst.html
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
autoconf
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4-6mdv2011.0
+ Revision: 620295
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.4-5mdv2010.0
+ Revision: 429954
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 2.4-4mdv2009.0
+ Revision: 251884
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.4-2mdv2008.1
+ Revision: 129735
- kill re-definition of %%buildroot on Pixel's request
- fix autoconf-2.5x path
- use %%mkrel
- import marst


* Fri Nov 05 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.4-2mdk
- fix build with current autotools

* Mon Jan 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- from Omer Shenker <marst@omershenker.net> : 
	- Patch to handle texinfo properly with automake
	- Specfile for Mandrake
	- gz to bz2 compression
