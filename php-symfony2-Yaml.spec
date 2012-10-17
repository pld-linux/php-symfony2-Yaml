%define		status		stable
%define		pearname	Yaml
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Symfony2 Yaml Component
Name:		php-symfony2-Yaml
Version:	2.1.2
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	85b7c9272413501386a468cf0dc09a70
URL:		http://pear.symfony.com/package/Yaml/
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Symfony2 Yaml Component

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

# no packaging of tests
rm -r .%{php_pear_dir}/Symfony/Component/Yaml/Tests

# fixups
mv .%{php_pear_dir}/Symfony/Component/Yaml/CHANGELOG.md .
mv .%{php_pear_dir}/Symfony/Component/Yaml/phpunit.xml{.dist,}
mv docs/Yaml/Symfony/Component/Yaml/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
# XXX proper dirs
%dir %{php_pear_dir}/Symfony
%dir %{php_pear_dir}/Symfony/Component
%dir %{php_pear_dir}/Symfony/Component/Yaml
%{php_pear_dir}/Symfony/Component/Yaml/Exception
%{php_pear_dir}/Symfony/Component/Yaml/*.php
%{php_pear_dir}/Symfony/Component/Yaml/phpunit.xml
