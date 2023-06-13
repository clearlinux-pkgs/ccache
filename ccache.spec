#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x996DDA075594ADB8 (joel@debian.org)
#
Name     : ccache
Version  : 4.8.2
Release  : 70
URL      : https://github.com/ccache/ccache/releases/download/v4.8.2/ccache-4.8.2.tar.xz
Source0  : https://github.com/ccache/ccache/releases/download/v4.8.2/ccache-4.8.2.tar.xz
Source1  : https://github.com/ccache/ccache/releases/download/v4.8.2/ccache-4.8.2.tar.xz.asc
Source2  : ccache.sh
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+
Requires: ccache-bin = %{version}-%{release}
Requires: ccache-data = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : pkg-config
BuildRequires : zlib-dev
BuildRequires : zstd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains Dockerfiles for building and testing ccache in
different build environments.

%package bin
Summary: bin components for the ccache package.
Group: Binaries
Requires: ccache-data = %{version}-%{release}

%description bin
bin components for the ccache package.


%package data
Summary: data components for the ccache package.
Group: Data

%description data
data components for the ccache package.


%prep
%setup -q -n ccache-4.8.2
cd %{_builddir}/ccache-4.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686666294
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake .. -DREDIS_STORAGE_BACKEND=OFF
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake .. -DREDIS_STORAGE_BACKEND=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :
cd ../clr-build-avx2;
make test || : || :

%install
export SOURCE_DATE_EPOCH=1686666294
rm -rf %{buildroot}
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/bin/ccache
/usr/bin/ccache

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/ccache.sh
