%global kf5_version 5.105.0
Name:           opt-kf5-kquickimageeditor
Version:        0.2.0
Release:        0
Summary:        A set of QtQuick components for image editing
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        %{name}-%{version}.tar.xz

                                                                              
BuildRequires:  opt-extra-cmake-modules >= %{kf5_version}                     
BuildRequires:  opt-kf5-rpm-macros >= %{kf5_version}                          
BuildRequires:  opt-qt5-qtbase-devel                                          
BuildRequires:  opt-qt5-qttools-devel                                         
BuildRequires:  opt-kf5-kconfig-devel               
BuildRequires:  opt-kf5-kwidgetsaddons-devel        
                                          
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}              

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
                                                                        
mkdir -p build                                                          
pushd build                                                             
                                                                        
%_opt_cmake_kf5 ../                                                     
%make_build                                                             
                                                                        
popd                                                                    
                                                                        
%install                                                                
pushd build                                                             
make DESTDIR=%{buildroot} install                                       
popd                                                                    
                                                                        
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
%{_opt_kf5_cmakedir}/KQuickImageEditor/
%{_opt_kf5_mkspecsdir}/qt_KQuickImageEditor.pri

%changelog

