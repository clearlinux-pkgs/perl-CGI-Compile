#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-CGI-Compile
Version  : 0.25
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-0.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-0.25.tar.gz
Summary  : 'Compile .cgi scripts to a code reference like ModPerl::Registry'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-CGI-Compile-license = %{version}-%{release}
Requires: perl-CGI-Compile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
NAME
CGI::Compile - Compile .cgi scripts to a code reference like
ModPerl::Registry

%package dev
Summary: dev components for the perl-CGI-Compile package.
Group: Development
Provides: perl-CGI-Compile-devel = %{version}-%{release}
Requires: perl-CGI-Compile = %{version}-%{release}

%description dev
dev components for the perl-CGI-Compile package.


%package license
Summary: license components for the perl-CGI-Compile package.
Group: Default

%description license
license components for the perl-CGI-Compile package.


%package perl
Summary: perl components for the perl-CGI-Compile package.
Group: Default
Requires: perl-CGI-Compile = %{version}-%{release}

%description perl
perl components for the perl-CGI-Compile package.


%prep
%setup -q -n CGI-Compile-0.25
cd %{_builddir}/CGI-Compile-0.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-CGI-Compile
cp %{_builddir}/CGI-Compile-0.25/LICENSE %{buildroot}/usr/share/package-licenses/perl-CGI-Compile/6eee64e6240eb3496293e0e3a8d568e984e4f1fa
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CGI::Compile.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-CGI-Compile/6eee64e6240eb3496293e0e3a8d568e984e4f1fa

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/CGI/Compile.pm
