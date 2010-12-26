%define upstream_name    Dancer-Plugin-DBIC
%define upstream_version 0.1504

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    DBIx::Class interface for Dancer applications
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dancer/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Dancer)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DBIx::Class::Schema::Loader)
BuildRequires: perl(SAL::Abstract)
BuildRequires: perl(Test::Exception)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin provides an easy way to obtain the DBIx::Class::ResultSet
manpage instances via the the function schema(), which it automatically
imports. You just need to point to a dsn in your the Dancer manpage
configuration file. So you no longer have to write boilerplate DBIC setup
code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README META.yml LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*

