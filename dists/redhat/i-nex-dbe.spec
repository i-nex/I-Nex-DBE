%define gittag b6105f35
%define gitlong b6105f355842c9fd29f9b5cfe35ff0db9f4eb600
%define gitdate 20161005

Name:           i-nex-dbe
Version:        0.0.3
Release:        %{gitdate}.git%{gittag}%{?dist}
Summary:        I-Nex JSON Database Editor

Group:          System/X11/Utilities
License:        GPL-3.0+
URL:            https://github.com/i-nex/I-Nex-DBE
Source0:        https://github.com/i-nex/I-Nex-DBE/archive/%{gittag}.zip#/I-Nex-DBE-%{gitlong}.zip

BuildRequires:  ImageMagick
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gambas3-devel >= 3.8.4
BuildRequires:  gambas3-gb-desktop >= 3.8.4
BuildRequires:  gambas3-gb-form >= 3.8.4
BuildRequires:  gambas3-gb-form-dialog >= 3.8.4
BuildRequires:  gambas3-gb-form-stock >= 3.8.4
BuildRequires:  gambas3-gb-gtk >= 3.8.4
BuildRequires:  gambas3-gb-gui >= 3.8.4
BuildRequires:  gambas3-gb-image >= 3.8.4
BuildRequires:  gambas3-gb-qt5 >= 3.8.4
BuildRequires:  gambas3-gb-qt5-opengl >= 3.8.4
BuildRequires:  gambas3-gb-qt5-webkit >= 3.8.4
BuildRequires:  gambas3-gb-settings >= 3.8.4
BuildRequires:  gambas3-gb-data >= 3.8.4
BuildRequires:  gambas3-gb-xml >= 3.8.4
BuildRequires:  gambas3-gb-xml-html >= 3.8.4
BuildRequires:  gambas3-gb-util-web >= 3.8.4
BuildRequires:  gambas3-gb-web >= 3.8.4
BuildRequires:  hicolor-icon-theme
Requires:       gambas3-gb-desktop >= 3.8.4
Requires:       gambas3-gb-form >= 3.8.4
Requires:       gambas3-gb-form-dialog >= 3.8.4
Requires:       gambas3-gb-form-stock >= 3.8.4
Requires:       gambas3-gb-gtk >= 3.8.4
Requires:       gambas3-gb-gui >= 3.8.4
Requires:       gambas3-gb-image >= 3.8.4
Requires:       gambas3-gb-qt5 >= 3.8.4
Requires:       gambas3-gb-qt5-opengl >= 3.8.4
Requires:       gambas3-gb-qt5-webkit >= 3.8.4
Requires:       gambas3-gb-settings >= 3.8.4
Requires:       gambas3-gb-data >= 3.8.4
Requires:       gambas3-gb-xml >= 3.8.4
Requires:       gambas3-gb-xml-html >= 3.8.4
Requires:       gambas3-gb-util-web >= 3.8.4
Requires:       gambas3-gb-web >= 3.8.4
Requires:       gambas3-runtime >= 3.8.4

%description
I-Nex JSON Database Editor

%prep
%setup -q -n I-Nex-DBE-%{gitlong}

%build
autoreconf -fiv
%configure
make \
     %{?_smp_mflags} \
     STATIC=false \
     V=1 \
     additional_confflags+="%{optflags}"

%install
make V=1 DESTDIR=%{buildroot} install


%files
%defattr(-,root,root,-)
/usr/bin/I-Nex-DBE.gambas
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog

%changelog
* Sat Oct 1 2016 <GitHub/eloaders/I-Nex/alphastar868>
- New SPEC file for 2016 RedHat RPM distros
