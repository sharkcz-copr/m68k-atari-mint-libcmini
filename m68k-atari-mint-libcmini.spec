# we are cross-compiled libraries
%global debug_package %{nil}
%global __strip /bin/true

%global gitdate 20220330
%global commit 9652c2d567757e77e36d812ab1a5bccf25277fc2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           m68k-atari-mint-libcmini
Summary:        Small-footprint C library for the m68k-atari-mint toolchain
Version:        0.54
Release:        1.%{gitdate}git%{shortcommit}%{?dist}
License:        LGPLv2+
URL:            https://github.com/freemint/libcmini
Source0:        %{url}/archive/%{commit}/libcmini-%{shortcommit}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  m68k-atari-mint-gcc
BuildRequires:  m68k-atari-mint-gemlib
Requires:       m68k-atari-mint-gcc
Provides:       m68k-atari-mint-libc
Conflicts:      m68k-atari-mint-mintlib

%description
libcmini aims to be a small-footprint C library for the m68k-atari-mint
(cross) toolchain, similar to the C library Pure-C came with. Many GEM
programs do not need full MiNT support and only a handful of C library
functions.


%prep
%setup -q -n libcmini-%{commit}


%build
make PREFIX=%{mint_prefix} VERBOSE=yes


%install
make install PREFIX=%{buildroot}%{mint_prefix}

# add libc symlinks
pushd %{buildroot}%{mint_libdir}
for d in . ./mshort ./m68020-60 ./m68020-60/mshort ./m5475 ./m5475/mshort; do
 ( cd $d; ln -sf libcmini.a libc.a )
done
popd


%files
%license LICENSE.txt
%doc README.md
%{mint_includedir}/*
%{mint_libdir}/*


%changelog
* Sun Jul 10 2022 Dan Horák <dan[at]danny.cz> - 0.54-1.20220330
- initial Fedora release
