#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-CGI-Compile
Version  : 0.26
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-0.26.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CGI-Compile-0.26.tar.gz
Summary  : 'Compile .cgi scripts to a code reference like ModPerl::Registry'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-CGI-Compile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package perl
Summary: perl components for the perl-CGI-Compile package.
Group: Default
Requires: perl-CGI-Compile = %{version}-%{release}

%description perl
perl components for the perl-CGI-Compile package.


%prep
%setup -q -n CGI-Compile-0.26
cd %{_builddir}/CGI-Compile-0.26
pushd ..
cp -a CGI-Compile-0.26 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/CGI::Compile.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
