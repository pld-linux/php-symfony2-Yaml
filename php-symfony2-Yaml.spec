%define		package	Yaml
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Yaml Component
Name:		php-symfony2-Yaml
Version:	2.7.7
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	a4d1ef400e714e92718bf9b248ce39f2
URL:		http://symfony.com/doc/2.7/components/yaml/introduction.html
BuildRequires:	phpab
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(date)
Requires:	php(json)
Requires:	php(mbstring)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-dirs >= 1.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YAML Component loads and dumps YAML files.

%prep
%setup -q -n yaml-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_data_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_data_dir}/Symfony/Component/Yaml
%{php_data_dir}/Symfony/Component/Yaml/*.php
%{php_data_dir}/Symfony/Component/Yaml/Exception
