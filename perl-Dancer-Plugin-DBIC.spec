%define upstream_name    Dancer-Plugin-DBIC
%define upstream_version 0.1504

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	DBIx::Class interface for Dancer applications
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dancer/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dancer)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::Schema::Loader)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Module::Find)
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

%changelog
* Sun Apr 24 2011 Funda Wang <fwang@mandriva.org> 0.150.400-3mdv2011.0
+ Revision: 658177
- tweak br
- rebuild for updated spec-helper
- rebuild for updated spec-helper

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - fix build dependencies

* Thu Dec 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.400-1mdv2011.0
+ Revision: 624080
- update to new version 0.1504

* Sun Oct 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.100-1mdv2011.0
+ Revision: 586525
- import perl-Dancer-Plugin-DBIC

