%define major 4
%define libname %mklibname atasmart %{major}
%define develname %mklibname -d atasmart

Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Name:		libatasmart
Version:	0.17
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
URL:		http://git.0pointer.de/?p=libatasmart.git;a=summary
Source0:	http://0pointer.de/public/libatasmart-%{version}.tar.gz
BuildRequires:	libudev-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Conflicts:	%{_lib}atasmart0 < 0.14

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package -n	%{libname}
Summary:	ATA S.M.A.R.T. Disk Health Monitoring Library
Group:		System/Libraries

%description -n	%{libname}
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package -n	%{develname}
Summary:	Development Files for libatasmart Client Development
Group:		Development/C
Provides:	libatasmart-devel = %version-%release
Requires:	%libname = %version-%release

%description -n	%{develname}
Development files for libatasmart Client Development

%prep

%setup -q

%build
%configure2_5x \
    --disable-static

%make

%install
rm -rf %{buildroot}

%makeinstall_std

find %{buildroot} \( -name *.a -o -name *.la \) -exec rm {} \;

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%doc README LGPL
%{_sbindir}/skdump
%{_sbindir}/sktest

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libatasmart.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc blob-examples/SAMSUNG* blob-examples/ST* blob-examples/Maxtor* blob-examples/WDC* blob-examples/README
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%{_datadir}/vala/vapi/atasmart.vapi
