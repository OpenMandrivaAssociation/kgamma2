%define snapshot 20261019
%define commit beaa5f2885a8ffde9546012b7be7cdb6a5dffa58

Name:		kgamma2
Version:	0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Wayland monitor gamma correction
# No upstream release. Snapshot of
# https://invent.kde.org/davidedmundson/kgamma2
# commit beaa5f2885a8ffde9546012b7be7cdb6a5dffa58 (2026-08-07).
Source0:	https://invent.kde.org/davidedmundson/kgamma2/-/archive/%{commit}/%{name}-%{commit}.tar.bz2#/%{name}-%{snapshot}.tar.xz
URL:		https://invent.kde.org/davidedmundson/kgamma2
License:	LGPL-2.1-or-later AND BSD-3-Clause
Group:		Graphical desktop/KDE
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Kirigami)
BuildRequires:	cmake(KF6Screen) >= 6.8
BuildRequires:	pkgconfig(lcms2)
# Kirigami and the desktop style are QML imports, not DT_NEEDED libraries.
# libQt6Qml already pulls Qt Quick Controls.
Requires:	kf6-kirigami
Requires:	qml(org.kde.desktop)
BuildSystem:	cmake
# find_package(ECM) has no version, so ECM defaults to Qt 5 and
# KDEInstallDirs then requires Qt 5 qmake. Cooker aarch64 has no qmake.
BuildOption:	-DBUILD_WITH_QT6:BOOL=ON

%description
Standalone Wayland tool that writes an sRGB ICC profile with a VCGT gamma
ramp and applies it through KScreen. The X11 gamma module stays in the
separate kgamma package.

# Upstream installs only the kgamma_wayland binary.
%install -a
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/org.kde.kgamma2.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=Wayland Gamma
GenericName=Monitor correction
Comment=Adjust display gamma on Wayland
Exec=kgamma_wayland
Icon=preferences-desktop-display-color
Categories=Qt;KDE;Settings;HardwareSettings;
Keywords=gamma;color;icc;calibration;monitor;display;
OnlyShowIn=KDE;
X-KDE-OnlyShowOnQtPlatforms=wayland
Terminal=false
StartupNotify=true
SingleMainWindow=true
EOF

%files
%{_bindir}/kgamma_wayland
%{_datadir}/applications/org.kde.kgamma2.desktop
