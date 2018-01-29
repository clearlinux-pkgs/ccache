#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x996DDA075594ADB8 (joel@debian.org)
#
Name     : ccache
Version  : 3.3.6
Release  : 26
URL      : http://samba.org/ftp/ccache/ccache-3.3.6.tar.xz
Source0  : http://samba.org/ftp/ccache/ccache-3.3.6.tar.xz
Source99 : http://samba.org/ftp/ccache/ccache-3.3.6.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: ccache-bin
Requires: ccache-data
Requires: ccache-doc
BuildRequires : zlib-dev

%description
ccache
======
[![Build Status](https://travis-ci.org/ccache/ccache.svg?branch=master)](https://travis-ci.org/ccache/ccache)

%package bin
Summary: bin components for the ccache package.
Group: Binaries
Requires: ccache-data

%description bin
bin components for the ccache package.


%package data
Summary: data components for the ccache package.
Group: Data

%description data
data components for the ccache package.


%package doc
Summary: doc components for the ccache package.
Group: Documentation

%description doc
doc components for the ccache package.


%prep
%setup -q -n ccache-3.3.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517184426
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
export SOURCE_DATE_EPOCH=1517184426
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib64/ccache/bin
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/gcc
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/g++
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/cc
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/c++
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/cpp
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/x86_64-generic-linux-gcc
ln -s /usr/bin/ccache %{buildroot}/usr/lib64/ccache/bin/x86_64-generic-linux-c++
mkdir -p %{buildroot}/usr/share/defaults/etc/profile.d
cat > %{buildroot}/usr/share/defaults/etc/profile.d/ccache.sh << "EOF"
case ":${PATH:-}:" in
*:/usr/lib64/ccache/bin:*) ;;
*) PATH="/usr/lib64/ccache/bin${PATH:+:$PATH}" ;;
esac
EOF
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/ccache/bin/c++
/usr/lib64/ccache/bin/cc
/usr/lib64/ccache/bin/cpp
/usr/lib64/ccache/bin/g++
/usr/lib64/ccache/bin/gcc
/usr/lib64/ccache/bin/x86_64-generic-linux-c++
/usr/lib64/ccache/bin/x86_64-generic-linux-gcc

%files bin
%defattr(-,root,root,-)
/usr/bin/ccache

%files data
%defattr(-,root,root,-)
/usr/share/defaults/etc/profile.d/ccache.sh

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
