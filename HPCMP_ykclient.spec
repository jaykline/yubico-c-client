#
# YubiKey Project for the HPCMP
#

Name:           HPCMP_ykclient
Version:        2.7
Release:        2%{?dist}
Summary:        Yubikey management library and client with HPCMP changes

Group:          Applications/System
License:        BSD
URL:            https://github.com/Yubico/yubico-c-client
Source0:        https://github.com/Yubico/yubico-c-client/tarball/ykclient-2.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  curl-devel
BuildRequires:  chrpath


%description
- commandline for yubikeys
- development files for ykclient  needed to build applications to
take advantage of yubikey authentication.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
autoreconf --install
%configure --enable-static=no
make %{?_smp_mflags}

%install

%makeinstall
rm %{buildroot}%{_libdir}/*.la
chrpath -d $RPM_BUILD_ROOT%{_bindir}/ykclient

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS NEWS README
%{_bindir}/ykclient
%{_libdir}/libykclient.so.3*
%{_libdir}/libykclient.so
%{_includedir}/ykclient.h
%{_includedir}/ykclient_server_response.h

%changelog
* Wed Jan 11 2012 tom.proue.ctr@hpcmo.hpc.mil
- Upgraded to version 2.7
- Added changes to allow user to choose Certificate Authority directory
* Tue Sep 07 2011 tom.proue.ctr@hpcmo.hpc.mil
- Initial package, version 2.6
