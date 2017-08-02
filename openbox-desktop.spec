Name: openbox-desktop
Version: 1.0
Release: 1%{?dist}
Summary: configuration files to enable Openbox desktop on Fedora

License: GPLv3
Source: https://github.com/Antique/%{name}/archive/%{version}.tar.gz

BuildArch: noarch

Requires: slim
Requires: tint2

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

mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
ln -s %{_datadir}/applications/tint2.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/tint2.desktop

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/

mkdir -p %{buildroot}%{_datadir}/slim/themes
cp -r fedora-simple %{buildroot}%{_datadir}/slim/themes/

%post
sed -i -e "s/^sessions.*$/sessions\t\topenbox-session/" %{_sysconfdir}/slim.conf
systemctl set-default graphical.target
systemctl --no-reload enable slim.service
sed -i -e "s/^current_theme.*$/current_theme\tfedora-simple/" %{_sysconfdir}/slim.conf

%files
%{_sysconfdir}/pam.d/slimlock
%{_sysconfdir}/sysconfig/desktop
%{_datadir}/slim/themes/fedora-simple/*


%package default-autostart
Summary: enables default autostart applications

Requires: tint2

%description default-autostart
installs autostart for tint2

%files default-autostart
%{_sysconfdir}/xdg/autostart/tint2.desktop


%changelog

