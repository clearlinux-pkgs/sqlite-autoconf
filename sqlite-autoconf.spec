#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sqlite-autoconf
Version  : 3200000
Release  : 52
URL      : http://sqlite.org/2017/sqlite-autoconf-3200000.tar.gz
Source0  : http://sqlite.org/2017/sqlite-autoconf-3200000.tar.gz
Summary  : SQL database engine
Group    : Development/Tools
License  : Public-Domain
Requires: sqlite-autoconf-bin
Requires: sqlite-autoconf-lib
Requires: sqlite-autoconf-doc
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : pkg-config-dev
BuildRequires : readline-dev
Patch1: flags.patch
Patch2: defaults.patch
Patch3: walmode.patch
Patch4: chunksize.patch
Patch5: defaultwal.patch

%description
This is the SQLite extension for Tcl using the Tcl Extension
Architecture (TEA).  For additional information on SQLite see

%package bin
Summary: bin components for the sqlite-autoconf package.
Group: Binaries

%description bin
bin components for the sqlite-autoconf package.


%package dev
Summary: dev components for the sqlite-autoconf package.
Group: Development
Requires: sqlite-autoconf-lib
Requires: sqlite-autoconf-bin
Provides: sqlite-autoconf-devel

%description dev
dev components for the sqlite-autoconf package.


%package dev32
Summary: dev32 components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-lib32
Requires: sqlite-autoconf-bin
Requires: sqlite-autoconf-dev

%description dev32
dev32 components for the sqlite-autoconf package.


%package doc
Summary: doc components for the sqlite-autoconf package.
Group: Documentation

%description doc
doc components for the sqlite-autoconf package.


%package lib
Summary: lib components for the sqlite-autoconf package.
Group: Libraries

%description lib
lib components for the sqlite-autoconf package.


%package lib32
Summary: lib32 components for the sqlite-autoconf package.
Group: Default

%description lib32
lib32 components for the sqlite-autoconf package.


%prep
%setup -q -n sqlite-autoconf-3200000
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a sqlite-autoconf-3200000 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501607740
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%reconfigure --disable-static
make V=1  %{?_smp_mflags} -j1
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags} -j1
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1501607740
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlite3

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libsqlite3.so
/usr/lib64/pkgconfig/sqlite3.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so
/usr/lib32/pkgconfig/32sqlite3.pc
/usr/lib32/pkgconfig/sqlite3.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsqlite3.so.0
/usr/lib64/libsqlite3.so.0.8.6

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so.0
/usr/lib32/libsqlite3.so.0.8.6
