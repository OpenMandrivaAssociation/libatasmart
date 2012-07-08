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

find %{buildroot} \( -name *.a -o -name *.la \) -exec rm {} \;

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
