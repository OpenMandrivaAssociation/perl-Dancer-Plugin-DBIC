%define upstream_name    Dancer-Plugin-DBIC
%define upstream_version 0.1802

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.1802
Release:	3

Summary:	DBIx::Class interface for Dancer applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dancer/Dancer-Plugin-DBIC-0.1802.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dancer)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(strictures)
BuildArch:	noarch

%description
This plugin provides an easy way to obtain the DBIx::Class::ResultSet
manpage instances via the the function schema(), which it automatically
imports. You just need to point to a dsn in your the Dancer manpage
configuration file. So you no longer have to write boilerplate DBIC setup
code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*
