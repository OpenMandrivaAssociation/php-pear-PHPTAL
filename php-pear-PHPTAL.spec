%define upstream_name PHPTAL

Name:		php-pear-%{upstream_name}
Version:	1.0.10
Release:	13
Summary:	Implementation of Zope Page Templates (ZPT) for PHP
License:	PHP License
Group:		Development/PHP
URL:		http://phptal.motion-twin.com/
Source0:	http://phptal.motion-twin.com/files/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-gettext
BuildArch:	noarch
BuildRequires:	php-pear

%description
PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README
%{_datadir}/pear/PHPTAL
%{_datadir}/pear/PHPTAL.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-11mdv2012.0
+ Revision: 742179
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-10
+ Revision: 679558
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-9mdv2011.0
+ Revision: 613751
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-8mdv2010.1
+ Revision: 467957
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.10-7mdv2010.0
+ Revision: 441561
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-6mdv2009.1
+ Revision: 322608
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-5mdv2009.0
+ Revision: 237046
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.10-4mdv2008.1
+ Revision: 171041
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-3mdv2008.0
+ Revision: 90116
- rebuild


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdv2007.0
+ Revision: 82509
- Import php-pear-PHPTAL

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-2mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-8mdk
- initial Mandriva package

