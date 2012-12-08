%define major 4
%define libname %mklibname atasmart %{major}
%define develname %mklibname -d atasmart

Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Name:		libatasmart
Version:	0.19
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://git.0pointer.de/?p=libatasmart.git;a=summary
Source0:	http://0pointer.de/public/libatasmart-%{version}.tar.xz
BuildRequires:	pkgconfig(udev) >= 186
Conflicts:	%{_lib}atasmart0 < 0.14
Patch0:		libatasmart-0.17-initmem.patch

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package -n %{libname}
Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Group:		System/Libraries

%description -n	%{libname}
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package -n %{develname}
Summary:	Development Files for libatasmart Client Development
Group:		Development/C
Provides:	libatasmart-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
Development files for libatasmart Client Development

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
    --disable-static

%make

%install
%makeinstall_std

%files
%doc README LGPL
%{_sbindir}/skdump
%{_sbindir}/sktest

%files -n %{libname}
%{_libdir}/libatasmart.so.%{major}*

%files -n %{develname}
%doc blob-examples/SAMSUNG* blob-examples/ST* blob-examples/Maxtor* blob-examples/WDC* blob-examples/README
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%{_datadir}/vala/vapi/atasmart.vapi


%changelog
* Sun Jul 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.19-1
+ Revision: 808516
- update to new version 0.19
- rebuild against new udev >= 186
- spec file clean

* Thu Oct 27 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.18-1
+ Revision: 707445
- update to new version 0.18

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Correct use of uninitialized malloc memory

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.17-3
+ Revision: 660217
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.17-2mdv2011.0
+ Revision: 602523
- rebuild

* Fri Nov 06 2009 Oden Eriksson <oeriksson@mandriva.com> 0.17-1mdv2010.1
+ Revision: 461762
- 0.17

* Tue Sep 29 2009 Frederik Himpe <fhimpe@mandriva.org> 0.16-1mdv2010.0
+ Revision: 451058
- update to new version 0.16

* Sat Sep 19 2009 Oden Eriksson <oeriksson@mandriva.com> 0.15-1mdv2010.0
+ Revision: 444637
- fix build
- 0.15

* Fri Aug 07 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.0
+ Revision: 411503
- Update to new version 0.14
- Move libraries and documentation from library package to libatasmart
  so that i586 and x86_64 library package are parallel installable

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.13-3mdv2010.0
+ Revision: 395854
- fix devel provides

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.13-2mdv2010.0
+ Revision: 395848
- fix devel dep

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 0.13-1mdv2010.0
+ Revision: 375315
- 0.13

* Tue Apr 14 2009 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdv2010.0
+ Revision: 366914
- import libatasmart


* Tue Apr 14 2009 Oden Eriksson <oeriksson@mandriva.com> 0.10-1mdv2009.1
- initial fedora import

* Sun Apr 12 2009 Lennart Poettering <lpoetter@redhat.com> 0.9-1
- New upstream release

* Fri Apr 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.8-1
- New upstream release

* Tue Apr 7 2009 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New upstream release

* Sat Apr 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New upstream release

* Fri Apr 3 2009 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New upstream release

* Thu Apr 2 2009 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- New upstream release

* Tue Mar 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.3-1
- New upstream release

* Thu Mar 19 2009 Lennart Poettering <lpoetter@redhat.com> 0.2-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Lennart Poettering <lpoetter@redhat.com> 0.1-1
- Initial version
