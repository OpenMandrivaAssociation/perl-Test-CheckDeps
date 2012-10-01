%define upstream_name    Test-CheckDeps
%define upstream_version 0.002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Check for presence of dependencies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(CPAN::Meta::Check)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Module::Metadata)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module adds a test that assures all dependencies have been installed
properly. If requested, it can bail out all testing on error.

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
%doc INSTALL LICENSE META.json Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

