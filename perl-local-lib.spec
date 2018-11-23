#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-local-lib
Version  : 2.000024
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/local-lib-2.000024.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/local-lib-2.000024.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblocal-lib-perl/liblocal-lib-perl_2.000024-1.debian.tar.xz
Summary  : 'create and use a local lib/ for perl modules with PERL5LIB'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-local-lib-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
local::lib - create and use a local lib/ for perl modules with PERL5LIB
SYNOPSIS
In code -

%package dev
Summary: dev components for the perl-local-lib package.
Group: Development
Provides: perl-local-lib-devel = %{version}-%{release}

%description dev
dev components for the perl-local-lib package.


%package license
Summary: license components for the perl-local-lib package.
Group: Default

%description license
license components for the perl-local-lib package.


%prep
%setup -q -n local-lib-2.000024
cd ..
%setup -q -T -D -n local-lib-2.000024 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/local-lib-2.000024/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-local-lib
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-local-lib/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.0/POD2/DE/local/lib.pod
/usr/lib/perl5/vendor_perl/5.28.0/POD2/PT_BR/local/lib.pod
/usr/lib/perl5/vendor_perl/5.28.0/lib/core/only.pm
/usr/lib/perl5/vendor_perl/5.28.0/local/lib.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POD2::DE::local::lib.3
/usr/share/man/man3/POD2::PT_BR::local::lib.3
/usr/share/man/man3/lib::core::only.3
/usr/share/man/man3/local::lib.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-local-lib/LICENSE
