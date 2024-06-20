%global commit      f261e3feec27da5dcbb07db6abdaf0662d5f0db5
%global snapdate    20240619

Name:               xwayland-satellite
Version:            0^%{snapdate}
Release:            2%{?dist}
Summary:            Xwayland outside your Wayland.

License:            MPL-2.0-only
URL:                https://github.com/Supreeeme/xwayland-satellite
Source:             %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:      cargo-rpm-macros >= 24
BuildRequires:      clang
BuildRequires:      pkgconfig(xcb)
BuildRequires:      pkgconfig(xcb-cursor)

Requires:           xorg-x11-server-Xwayland

%description
xwayland-satellite grants rootless Xwayland integration to any Wayland
compositor implementing xdg_wm_base. This is particularly useful for
compositors that (understandably) do not want to go through implementing
support for rootless Xwayland themselves.

%prep
%autosetup -n %{name}-%{commit} -p1
cargo vendor
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/xwayland-satellite

%changelog
%autochangelog