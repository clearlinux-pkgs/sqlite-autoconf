#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v3
# autospec commit: c1050fe
#
%define keepstatic 1
Name     : sqlite-autoconf
Version  : 3.45.0
Release  : 130
URL      : https://sqlite.org/2024/sqlite-autoconf-3450000.tar.gz
Source0  : https://sqlite.org/2024/sqlite-autoconf-3450000.tar.gz
Summary  : SQL database engine
Group    : Development/Tools
License  : Public-Domain
Requires: sqlite-autoconf-bin = %{version}-%{release}
Requires: sqlite-autoconf-lib = %{version}-%{release}
Requires: sqlite-autoconf-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : ncurses-dev
BuildRequires : readline-dev
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: flags.patch
Patch2: defaults.patch
Patch3: chunksize.patch
Patch4: defaultwal.patch

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
Requires: sqlite-autoconf-lib = %{version}-%{release}
Requires: sqlite-autoconf-bin = %{version}-%{release}
Provides: sqlite-autoconf-devel = %{version}-%{release}
Requires: sqlite-autoconf = %{version}-%{release}

%description dev
dev components for the sqlite-autoconf package.


%package dev32
Summary: dev32 components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-lib32 = %{version}-%{release}
Requires: sqlite-autoconf-bin = %{version}-%{release}
Requires: sqlite-autoconf-dev = %{version}-%{release}

%description dev32
dev32 components for the sqlite-autoconf package.


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


%package man
Summary: man components for the sqlite-autoconf package.
Group: Default

%description man
man components for the sqlite-autoconf package.


%package staticdev
Summary: staticdev components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-dev = %{version}-%{release}

%description staticdev
staticdev components for the sqlite-autoconf package.


%package staticdev32
Summary: staticdev32 components for the sqlite-autoconf package.
Group: Default
Requires: sqlite-autoconf-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the sqlite-autoconf package.


%prep
%setup -q -n sqlite-autoconf-3450000
cd %{_builddir}/sqlite-autoconf-3450000
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
pushd ..
cp -a sqlite-autoconf-3450000 build32
popd
pushd ..
cp -a sqlite-autoconf-3450000 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705438356
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%reconfigure  CPPFLAGS="-DSQLITE_ENABLE_DBSTAT_VTAB=1  -DSQLITE_ENABLE_JSON=1"
make
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure  CPPFLAGS="-DSQLITE_ENABLE_DBSTAT_VTAB=1  -DSQLITE_ENABLE_JSON=1"  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
%reconfigure  CPPFLAGS="-DSQLITE_ENABLE_DBSTAT_VTAB=1  -DSQLITE_ENABLE_JSON=1"
make
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check
cd ../build32;
make check || :
cd ../buildavx2;
make check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1705438356
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/sqlite3
/usr/bin/sqlite3

%files dev
%defattr(-,root,root,-)
/usr/include/sqlite3.h
/usr/include/sqlite3ext.h
/usr/lib64/libsqlite3.so
/usr/lib64/pkgconfig/sqlite3.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so
/usr/lib32/pkgconfig/32sqlite3.pc
/usr/lib32/pkgconfig/sqlite3.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libsqlite3.so.0.8.6
/usr/lib64/libsqlite3.so.0
/usr/lib64/libsqlite3.so.0.8.6

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.so.0
/usr/lib32/libsqlite3.so.0.8.6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sqlite3.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libsqlite3.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libsqlite3.a
