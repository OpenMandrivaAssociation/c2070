Summary:	Lexmark 2070 Printer color driver
Name:		c2070
Version:	0.99
Release:	21
Group:		System/Printing
License:	GPL
URL:		http://www.linuxprinting.org/show_driver.cgi?driver=%{name}
Source0:	ftp://mirror.linuxsoft.cz/pool/5865/%{name}-%{version}.tar.gz
Patch0:		c2070-0.99-looplimits.patch
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This filter allows to color print in a Lexmark 2070 (windows GDI) printer.

%prep

%setup -q
%patch0 -p1 -b .looplimits

%build
%{__cc} %{optflags} %{ldflags} -o c2070 c2070.c

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.99-11mdv2011.0
+ Revision: 663349
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99-10mdv2011.0
+ Revision: 603815
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.99-9mdv2010.1
+ Revision: 522335
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.99-8mdv2010.0
+ Revision: 413212
- rebuild

* Wed Dec 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.99-7mdv2009.1
+ Revision: 318449
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.99-6mdv2009.0
+ Revision: 220497
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.99-5mdv2008.1
+ Revision: 149061
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.99-4mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-4mdv2008.0
+ Revision: 75321
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-3mdv2008.0
+ Revision: 64142
- use the new System/Printing RPM GROUP

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-2mdv2008.0
+ Revision: 61078
- rebuild

* Fri Aug 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-1mdv2008.0
+ Revision: 60971
- Import c2070



* Thu Aug 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.99-1mdv2008.0
- initial Mandriva package

* Tue Jun 01 2004 Marcelo Ricardo Leitner <mrl@conectiva.com.br>
+ 2004-06-01 14:29:49 (62217)
- This driver was seg. faulting and no corrections seems to available.
    I hope this fixes it the right way, since no one can test it.

* Thu Aug 29 2002 Gustavo Niemeyer <niemeyer@conectiva.com>
+ 2002-08-29 17:23:54 (7430)
- Imported package from 8.0.
