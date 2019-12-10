Name:           firefox-developer-edition
Version:        72.0b4
Release:        2%{?dist}
Summary:        Firefox Developer Edition
License:        Mozilla Public License, GPL
URL:            https://www.mozilla.org/en-US/firefox/

Source0:        https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source1:        firefox-developer-edition.desktop

%description
Firefox Developer Edition

%install
install -d %{buildroot}/opt/%{name}
tar -xvf %{SOURCE0}
cp -r firefox/* %{buildroot}/opt/%{name}/
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
/opt/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Dec 10 2019 Josh Locash <locashjosh@gmail.com> - 72.0b4-2
- Initial RPM release
