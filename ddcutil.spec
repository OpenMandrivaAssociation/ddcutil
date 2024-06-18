%define libname %mklibname ddcutil
%define devname %mklibname -d ddcutil

Name:       ddcutil
Version:    2.1.4
Release:    1
Summary:    Query and update monitor settings
License:    GPLv2+
URL:        http://www.ddcutil.com
Source0:    https://github.com/rockowitz/ddcutil/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:      pkgconfig(glib-2.0)   >= 2.40
BuildRequires:      pkgconfig(libusb-1.0) >= 1.0.15
BuildRequires:      pkgconfig(systemd)
BuildRequires:      pkgconfig(libudev)
BuildRequires:      pkgconfig(xrandr)
BuildRequires:      pkgconfig(libdrm) >= 2.4.67
BuildRequires:      pkgconfig(libkmod)
BuildRequires:      pkgconfig(jansson) >= 2.0
 
Requires:   hwdata
Requires:   i2c-tools
 
# file that may be used at runtime
Recommends: /usr/bin/lsusb
Recommends: /usr/bin/modprobe
Recommends: pkg-config
Recommends: /usr/bin/lscpu
Recommends: /usr/bin/lsb_release
Recommends: xrandr

BuildSystem: autotools
BuildOption: --enable-lib

%patchlist
ddcutil-2.1.4-compile.patch
ddcutil-2.1.4-slibtool.patch
 
%description
Query and change monitor settings
 
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.  In general, anything that can be controlled using a monitor's
on-screen display can be controlled by this program.  Examples include 
changing a monitor's input source and adjusting its brightness.
 
%package -n %{libname}
Summary:        Shared library to query and update monitor settings
 
%description -n %{libname}
Shared library version of ddcutil, exposing a C API.
 
%package -n %{devname}
Summary:        Development files for libddcutil
# FindDDCUtils.cmake has BSD license header
License:        GPLv2+ and BSD
Requires:       %{libname} = %{EVRD}
 
%description -n %{devname}
Development files for libddcutil
 
%prep -a
NOCONFIGURE=1 ./autogen.sh

%files
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_udevrulesdir}/60-ddcutil-i2c.rules
%{_udevrulesdir}/60-ddcutil-usb.rules
%{_modulesloaddir}/ddcutil.conf
 
%files -n %{libname}
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%{_libdir}/lib%{name}.so.5*
 
%files -n %{devname}
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}*.h
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
