#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ccache
Version  : 3.2.5
Release  : 14
URL      : http://samba.org/ftp/ccache/ccache-3.2.5.tar.gz
Source0  : http://samba.org/ftp/ccache/ccache-3.2.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+
Requires: ccache-bin
Requires: ccache-data
Requires: ccache-doc
BuildRequires : zlib-dev

%description
=============
About
-----
ccache is a compiler cache. It speeds up recompilation by caching the result of
previous compilations and detecting when the same compilation is being done
again. Supported languages are C, C++, Objective-C and Objective-C++.

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
%setup -q -n ccache-3.2.5

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
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
