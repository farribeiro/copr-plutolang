%global debug_package %{nil}
Name:           pluto
Version:        0.11.3
Release:        1%{?dist}
Summary:        A superset of Lua 5.4 with a focus on general-purpose programming.
License:        MIT
URL:            https://github.com/PlutoLang/Pluto
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz
Provides:       libpluto.so

BuildRequires:  make, gcc-c++, readline-devel
Requires:       readline

%description
Pluto is a superset of Lua 5.4 with a focus on general-purpose programming. While being remarkably compatible with Lua 5.4 source-code & bytecode, it enhances the standard library & adds more than a dozen highly-desired syntaxes such as switch statements, compound operators, classes, class inheritance, string interpolation, type hinting, enums, and so on.

%prep
%autosetup -n Pluto-%{version}

%build
make %{?_smp_mflags} PLAT=linux-readline

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
#mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0755 src/pluto src/plutoc %{buildroot}%{_bindir}
install -p -m 0644 src/lua.h src/luaconf.h src/lualib.h src/lauxlib.h src/lua.hpp %{buildroot}%{_includedir}
install -p -m 0644 src/libpluto.so src/libplutostatic.a %{buildroot}%{_libdir}
#install -p -m 0644 doc/lua.1 doc/luac.1 %{buildroot}%{_mandir}/man1

%files
%{_bindir}/pluto
%{_bindir}/plutoc
%{_includedir}/lua.h
%{_includedir}/luaconf.h
%{_includedir}/lualib.h
%{_includedir}/lauxlib.h
%{_includedir}/lua.hpp
%{_libdir}/libpluto.so
%{_libdir}/libplutostatic.a

%changelog
* Sun May 11 2025 Fábio Rodrigues Ribeiro <farribeiro@gmail.com> - 0.10.5-1
- Initial Fedora packaging.
