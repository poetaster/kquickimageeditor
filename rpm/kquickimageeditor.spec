%global kf5_version 5.105.0
%global qt_version 5.15.9

Name:           opt-kf5-kquickimageeditor
Version:        0.3.0
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        %{name}-%{version}.tar.xz

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-kf5-kcoreaddons-devel >= %{kf5_version}
BuildRequires: opt-qt5-qtdeclarative-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires:      opt-qt5-qtbase-gui >= %{qt_version}
Requires:      opt-qt5-qtdeclarative >= %{qt_version}


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

%description devel
Development files for KQuickImageEditor, a set of QtQuick components providing
basic image editing capabilities.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%_opt_cmake_kf5
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files imports
%license LICENSES/*
%doc README*
%dir %{_opt_kf5_qmldir}/org/
%dir %{_opt_kf5_qmldir}/org/kde/
%{_opt_kf5_qmldir}/org/kde/kquickimageeditor/

%files devel
%license LICENSES/*
%{_opt_kf5_libdir}/cmake/KQuickImageEditor/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KQuickImageEditor.pri

%changelog

