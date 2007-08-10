Summary:	Lexmark 2070 Printer color driver
Name:		c2070
Version:	0.99
Release:	%mkrel 2
Group:		File tools
License:	GPL
URL:		http://www.linuxprinting.org/show_driver.cgi?driver=%{name}
Source0:	ftp://mirror.linuxsoft.cz/pool/5865/%{name}-%{version}.tar.gz
Patch0:		c2070-0.99-looplimits.patch
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This filter allows to color print in a Lexmark 2070 (windows GDI) printer.

%prep

%setup -q

%patch -p1 -b .looplimits

%build
%{__cc} %{optflags} -o c2070 c2070.c

%install
rm -rf %{buildroot}

install -d %{buildroot}/%{_bindir}
install -m0755 c2070 %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc LICENSE README
%attr(0755,root,root) %{_bindir}/c2070
