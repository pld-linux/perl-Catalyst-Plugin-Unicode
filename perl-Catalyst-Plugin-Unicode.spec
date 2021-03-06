#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Catalyst
%define	pnam	Plugin-Unicode
Summary:	Catalyst::Plugin::Unicode - Unicode aware Catalyst
#Summary(pl.UTF-8):	
Name:		perl-Catalyst-Plugin-Unicode
Version:	0.93
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f362bfa2ec2bb70378717122e2da018d
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Unicode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.70
BuildRequires:	perl-IO-stringy
BuildRequires:	perl-MRO-Compat >= 0.10
BuildRequires:	perl-Test-use-ok
BuildRequires:	perl-Test-WWW-Mechanize-Catalyst >= 0.56
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
On request, decodes all params from UTF-8 octets into a sequence of
logical characters. On response, encodes body into UTF-8 octets.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	--skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
