%define rname PHPTAL

Summary:	Implementation of Zope Page Templates (ZPT) for PHP
Name:		php-pear-%{rname}
Version:	1.0.10
Release:	%mkrel 7
License:	PHP License
Group:		Development/PHP
URL:		http://phptal.motion-twin.com/
Source0:	http://phptal.motion-twin.com/files/%{rname}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-gettext
#Requires:	php-Types
#Requires:	php-Algo_map
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PHPTAL is an implementation of Zope Page Templates (ZPT) for PHP.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/PHPTAL/Attribute/{I18N,TAL,METAL,PHPTAL}
install -d %{buildroot}%{_datadir}/pear/packages

install -m0644 %{rname}-%{version}/PHPTAL/*.php %{buildroot}%{_datadir}/pear/PHPTAL/
install -m0644 %{rname}-%{version}/PHPTAL/Attribute/I18N/*.php %{buildroot}%{_datadir}/pear/PHPTAL/Attribute/I18N/
install -m0644 %{rname}-%{version}/PHPTAL/Attribute/TAL/*.php %{buildroot}%{_datadir}/pear/PHPTAL/Attribute/TAL/
install -m0644 %{rname}-%{version}/PHPTAL/Attribute/METAL/*.php %{buildroot}%{_datadir}/pear/PHPTAL/Attribute/METAL/
install -m0644 %{rname}-%{version}/PHPTAL/Attribute/PHPTAL/*.php %{buildroot}%{_datadir}/pear/PHPTAL/Attribute/PHPTAL/
install -m0644 %{rname}-%{version}/PHPTAL.php %{buildroot}%{_datadir}/pear/
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{rname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{rname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{rname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{rname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{rname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{rname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{rname}
	fi
fi


%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{rname}-%{version}/README
%dir %{_datadir}/pear/PHPTAL
%dir %{_datadir}/pear/PHPTAL/Attribute
%dir %{_datadir}/pear/PHPTAL/Attribute/I18N
%dir %{_datadir}/pear/PHPTAL/Attribute/TAL
%dir %{_datadir}/pear/PHPTAL/Attribute/METAL
%dir %{_datadir}/pear/PHPTAL/Attribute/PHPTAL
%{_datadir}/pear/PHPTAL/*.php
%{_datadir}/pear/PHPTAL/Attribute/I18N/*.php
%{_datadir}/pear/PHPTAL/Attribute/TAL/*.php
%{_datadir}/pear/PHPTAL/Attribute/METAL/*.php
%{_datadir}/pear/PHPTAL/Attribute/PHPTAL/*.php
%{_datadir}/pear/PHPTAL.php
%{_datadir}/pear/packages/%{rname}.xml


