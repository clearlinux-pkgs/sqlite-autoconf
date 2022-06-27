#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : sqlite-autoconf
Version  : 3.39.0
Release  : 112
URL      : https://sqlite.org/2022/sqlite-autoconf-3390000.tar.gz
Source0  : https://sqlite.org/2022/sqlite-autoconf-3390000.tar.gz
Summary  : SQL database engine
Group    : Development/Tools
License  : Public-Domain
Requires: sqlite-autoconf-bin = %{version}-%{release}
Requires: sqlite-autoconf-lib = %{version}-%{release}
Requires: sqlite-autoconf-man = %{version}-%{release}
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
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
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
%setup -q -n sqlite-autoconf-3390000
cd %{_builddir}/sqlite-autoconf-3390000
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a sqlite-autoconf-3390000 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656347580
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used "
%reconfigure  CPPFLAGS="-DSQLITE_ENABLE_DBSTAT_VTAB=1"
make
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure  CPPFLAGS="-DSQLITE_ENABLE_DBSTAT_VTAB=1"  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
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

%install
export SOURCE_DATE_EPOCH=1656347580
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
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
