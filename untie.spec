%define git 14b92c7

Summary: Process namespace creator
Name: untie
Version: 0.4
Release: %mkrel 0.1.git%{git}
License: GPL
Group: System/Utilities
URL: http://guichaz.free.fr/untie
Source0: untie-%{version}-%{git}.tar.gz

%description
untie is a tool used to launch commands in new namespaces.

%prep
%setup -q

%build
make


%install
rm -rf
%makeinstall PREFIX=%{buildroot}/%{_prefix}

%clean
rm -rf


%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_sbindir}/*
%doc %{_mandir}/*/*

