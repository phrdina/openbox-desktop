Name: openbox-desktop
Version: 1.0
Release: 1%{?dist}
Summary: configuration files to enable openbox desktop on fedora

License: GPLv3
Source: https://github.com/Antique/%{name}/archive/%{name}-%{version}.tar.gz


BuildArch: noarch

Requires: slim

%description
openbox desktop packages to make it work out of box on fedora with slim and tint2

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
install -m 0644 default-desktop %{buildroot}%{_sysconfdir}/sysconfig/desktop
ln -s %{_sysconfdir}/pam.d/slim %{buildroot}%{_sysconfdir}/pam.d/slimlock

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
install -m 0644 colorprompt.sh %{buildroot}%{_sysconfdir}/profile.d/colorprompt.sh

mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
ln -s %{_datadir}/applications/tint2.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/tint2.desktop

mkdir -p %{buildroot}%{_datadir}/slim/themes/fedora-simple
install -m 0644 fedora-simple/* %{buildroot}%{_datadir}/slim/themes/fedora-simple/

%post
sed -i -e "s/^sessions.*$/sessions\t\topenbox-session/" %{_sysconfdir}/slim.conf

%files
%{_sysconfdir}/pam.d/slimlock
%{_sysconfdir}/sysconfig/desktop


%package color-prompt
Summary: gentoo-like color prompt

%description color-prompt
enables color prompt like on gentoo

%files color-prompt
%{_sysconfdir}/profile.d/colorprompt.sh


%package default-autostart
Summary: enables default autostart applications

Requires: tint2

%description default-autostart
installs autostart for tint2

%files default-autostart
%{_sysconfdir}/xdg/autostart/tint2.desktop


%package slim-fedora-simple
Summary: theme for slim and slimlock

%description slim-fedora-simple
install and sets fedora-simple theme for slim

%post slim-fedora-simple
sed -i -e "s/^current_theme.*$/current_theme\tfedora-simple/" %{_sysconfdir}/slim.conf

%files slim-fedora-simple
%{_datadir}/slim/themes/fedora-simple/*


%changelog

