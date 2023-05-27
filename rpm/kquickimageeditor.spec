%define _kf5_version 5.79.0
%bcond_without  lang
Name:           kquickimageeditor
Version:        0.2.0
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/kquickimageeditor/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/kquickimageeditor/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  cmake >= 3.5
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Quick) >= 5.15.0

%description
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package imports
Summary:        A set of QtQuick components for image editing
Group:          System/GUI/KDE

%description imports
KQuickImageEditor is a set of QtQuick components providing basic image editing
capabilities.

%package devel
Summary:        Development files for KQuickImageEditor
Group:          Development/Libraries/KDE
Requires:       %{name}-imports = %{version}
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Quick)

%description devel
Development files for KQuickImageEditor, a set of QtQuick components providing
basic image editing capabilities.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%files imports
%license LICENSES/*
%doc README*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/kquickimageeditor/

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KQuickImageEditor/
%{_kf5_mkspecsdir}/qt_KQuickImageEditor.pri

%changelog

