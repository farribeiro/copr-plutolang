Name:           plutolang
Version:        0.10.4
Release:        1%{?dist}
Summary:        A superset of Lua 5.4 with a focus on general-purpose programming.
License:        MIT
URL:            https://github.com/PlutoLang/Pluto/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc, make, readline-devel
Requires:       glibc, gcc-libs, readline
Provides:       libpluto.so
Conflicts:      pluto

%description
Pluto is a superset of Lua 5.4 with a focus on general-purpose programming.

%prep
%autosetup -n Pluto-%{version}

%build
make -j$(nproc) PLAT=linux-readline

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/include/pluto
mkdir -p %{buildroot}/usr/share/licenses/%{name}

install -m 755 plutolang-%{version}/src/pluto %{buildroot}/usr/bin/pluto
install -m 755 plutolang-%{version}/src/plutoc %{buildroot}/usr/bin/plutoc
install -m 644 plutolang-%{version}/src/libpluto.so %{buildroot}/usr/lib/libpluto.so
install -m 644 plutolang-%{version}/src/lua.h %{buildroot}/usr/include/pluto/lua.h
install -m 644 plutolang-%{version}/src/lua.hpp %{buildroot}/usr/include/pluto/lua.hpp
install -m 644 plutolang-%{version}/src/lualib.h %{buildroot}/usr/include/pluto/lualib.h
install -m 644 plutolang-%{version}/src/lauxlib.h %{buildroot}/usr/include/pluto/lauxlib.h
install -m 644 plutolang-%{version}/src/luaconf.h %{buildroot}/usr/include/pluto/luaconf.h
install -m 644 plutolang-%{version}/LICENSE %{buildroot}/usr/share/licenses/%{name}/LICENSE

%files
/usr/bin/pluto
/usr/bin/plutoc
/usr/lib/libpluto.so
/usr/include/pluto/*
/usr/share/licenses/%{name}/LICENSE

%changelog
* Tue Feb 18 2025 Maintainer <sainan@calamity.gg> - 0.10.4-1
- Initial RPM package
