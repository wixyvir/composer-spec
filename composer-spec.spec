%define _version 1.0.0-alpha10
%define _ver %(echo %{_version} | cut -d- -f1)
%define _rel %(echo %{_version} | cut -d- -f2 || echo 1)

# Disable automatic dependency processing
# (prevents endless loop if php-composer is already installed on buildsys)
AutoReqProv: no

Name: php-composer
Version: %{_ver}
Release: %{_rel}
Summary: Dependency Manager for PHP
Group: Development/Libraries
License: MIT
URL: http://getcomposer.org/
Source0: https://getcomposer.org/download/%{_version}/composer.phar
BuildArch: noarch

Requires: php-cli
Requires: php-curl
Requires: php-date
Requires: php-hash
Requires: php-iconv
Requires: php-json
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-pcre
Requires: php-reflection
Requires: php-simplexml
Requires: php-spl
Requires: php-tokenizer
Requires: php-xsl
Requires: php-zip
BuildRequires: wget

%description
Composer is a tool for dependency management in PHP. It allows you to declare
the dependent libraries your project needs and it will install them in your
project for you.

%prep
wget https://getcomposer.org/download/%{_version}/composer.phar

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
cp -r composer.phar %{buildroot}/usr/bin/composer

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root)
/usr/bin/composer
