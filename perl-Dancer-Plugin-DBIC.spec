%define upstream_name    Dancer-Plugin-DBIC
%define upstream_version 0.2104

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	DBIx::Class interface for Dancer applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ironcamel/Dancer-Plugin-DBIC
Source0:	https://cpan.metacpan.org/authors/id/I/IR/IRONCAMEL/Dancer-Plugin-DBIC-0.2104.tar.gz

BuildRequires:	make
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
