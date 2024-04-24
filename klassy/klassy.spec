Name: klassy
Version: 6.1.breeze6.0.3
Release: 1%{?dist}
Summary: A highly customizable KDE Plasma Window Decoration

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND MIT
URL: https://github.com/paulmcauley/klassy
Source0: %{url}/archive/%{version}.tar.gz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5FrameworkIntegration)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(KDecoration2)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6FrameworkIntegration)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)

%description
Klassy is a highly customizable binary Window Decoration and Application Style
plugin for recent versions of the KDE Plasma desktop. It provides the Klassy,
Kite, Oxygen/Breeze, and Redmond icon styles.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%make_build

%install
cd build
%make_install

%files
%doc README.md
%{_bindir}/klassy-settings
%{_datadir}/applications/kcm_klassydecoration.desktop
%{_datadir}/applications/klassy-settings.desktop
%{_datadir}/applications/klassystyleconfig.desktop
%{_datadir}/color-schemes/Klassy*
%{_datadir}/icons/hicolor/scalable/apps/klassy-settings.svgz
%{_datadir}/icons/klassy*
%{_datadir}/kstyle/themes/klassy.themerc
%{_datadir}/plasma/desktoptheme/klassy
%{_datadir}/plasma/layout-templates/org.kde.klassy*
%{_datadir}/plasma/look-and-feel/org.kde.klassy*
%{_prefix}/%{_lib}/cmake/Klassy/KlassyConfig.cmake
%{_prefix}/%{_lib}/cmake/Klassy/KlassyConfigVersion.cmake
%{_prefix}/%{_lib}/libklassycommon5.so.%{version}
%{_prefix}/%{_lib}/libklassycommon5.so.6
%{_prefix}/%{_lib}/libklassycommon6.so.%{version}
%{_prefix}/%{_lib}/libklassycommon6.so.6
%{_prefix}/%{_lib}/qt5/plugins/styles/klassy5.so
%{_prefix}/%{_lib}/qt6/plugins/kstyle_config/klassystyleconfig.so
%{_prefix}/%{_lib}/qt6/plugins/org.kde.kdecoration2/org.kde.klassy.so
%{_prefix}/%{_lib}/qt6/plugins/org.kde.kdecoration2.kcm/kcm_klassydecoration.so
%{_prefix}/%{_lib}/qt6/plugins/org.kde.kdecoration2.kcm/klassydecoration/presets/*.klpw
%{_prefix}/%{_lib}/qt6/plugins/styles/klassy6.so

%changelog
* Wed Apr 24 2024 GarciaLnk <alberto@garcialnk.com> - 6.1.breeze6.0.3
- Fix build and include all files from Plasma 6 release.

* Tue Mar 12 2024 ErrorNoInternet <errornointernet@envs.net> - 5.0.breeze5.27.11-3
- Fix build by requiring Qt5Svg.
- Include all files from new release.

* Tue Mar 12 2024 ErrorNoInternet <errornointernet@envs.net> - 5.0.breeze5.27.11-2
- Minor description clean up.
- Fix build by requiring Qt6Gui.

* Fri Jun 30 2023 ErrorNoInternet <errornointernet@envs.net> - 4.3.breeze5.27.5-2
- Add README.md.

* Sat May 06 2023 ErrorNoInternet <errornointernet@envs.net> - 4.1.breeze5.25.80-1
- Initial packaging.
