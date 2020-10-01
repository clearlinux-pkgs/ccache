#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x996DDA075594ADB8 (joel@debian.org)
#
Name     : ccache
Version  : 3.7.12
Release  : 46
URL      : https://github.com/ccache/ccache/releases/download/v3.7.12/ccache-3.7.12.tar.xz
Source0  : https://github.com/ccache/ccache/releases/download/v3.7.12/ccache-3.7.12.tar.xz
Source1  : https://github.com/ccache/ccache/releases/download/v3.7.12/ccache-3.7.12.tar.xz.asc
Source2  : ccache.sh
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+ MIT
Requires: ccache-bin = %{version}-%{release}
Requires: ccache-data = %{version}-%{release}
Requires: ccache-license = %{version}-%{release}
Requires: ccache-man = %{version}-%{release}
BuildRequires : zlib-dev
Patch1: nonfatal.patch

%description
ccache – a fast compiler cache
==============================
[![Build Status](https://travis-ci.org/ccache/ccache.svg?branch=master)](https://travis-ci.org/ccache/ccache)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/ccache/ccache.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ccache/ccache/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/ccache/ccache.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ccache/ccache/alerts)

%package bin
Summary: bin components for the ccache package.
Group: Binaries
Requires: ccache-data = %{version}-%{release}
Requires: ccache-license = %{version}-%{release}

%description bin
bin components for the ccache package.


%package data
Summary: data components for the ccache package.
Group: Data

%description data
data components for the ccache package.


%package license
Summary: license components for the ccache package.
Group: Default

%description license
license components for the ccache package.


%package man
Summary: man components for the ccache package.
Group: Default

%description man
man components for the ccache package.


%prep
%setup -q -n ccache-3.7.12
cd %{_builddir}/ccache-3.7.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601565952
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1601565952
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ccache
cp %{_builddir}/ccache-3.7.12/LICENSE.adoc %{buildroot}/usr/share/package-licenses/ccache/687dc02bd6d110c3f35c56949d4fd99d95e4d220
%make_install
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d
install  %{_sourcedir}/ccache.sh %{buildroot}/usr/share/defaults/etc/profile.d/
## install_append content
mkdir -p %{buildroot}/usr/lib64/ccache/bin
for f in cc c++ cpp \
{x86_64-generic-linux-,}{gcc,g++}{,-8,-9} \
{clang,clang++}{,-8,-9,-10}; do
ln -s ../../../bin/ccache %{buildroot}/usr/lib64/ccache/bin/$f
done
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/ccache/bin/c++
/usr/lib64/ccache/bin/cc
/usr/lib64/ccache/bin/clang
/usr/lib64/ccache/bin/clang++
/usr/lib64/ccache/bin/clang++-10
/usr/lib64/ccache/bin/clang++-8
/usr/lib64/ccache/bin/clang++-9
/usr/lib64/ccache/bin/clang-10
/usr/lib64/ccache/bin/clang-8
/usr/lib64/ccache/bin/clang-9
/usr/lib64/ccache/bin/cpp
/usr/lib64/ccache/bin/g++
/usr/lib64/ccache/bin/g++-8
/usr/lib64/ccache/bin/g++-9
/usr/lib64/ccache/bin/gcc
/usr/lib64/ccache/bin/gcc-8
/usr/lib64/ccache/bin/gcc-9
/usr/lib64/ccache/bin/x86_64-generic-linux-g++
/usr/lib64/ccache/bin/x86_64-generic-linux-g++-8
/usr/lib64/ccache/bin/x86_64-generic-linux-g++-9
/usr/lib64/ccache/bin/x86_64-generic-linux-gcc
/usr/lib64/ccache/bin/x86_64-generic-linux-gcc-8
/usr/lib64/ccache/bin/x86_64-generic-linux-gcc-9

%files bin
%defattr(-,root,root,-)
/usr/bin/ccache

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/ccache.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ccache/687dc02bd6d110c3f35c56949d4fd99d95e4d220

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ccache.1
