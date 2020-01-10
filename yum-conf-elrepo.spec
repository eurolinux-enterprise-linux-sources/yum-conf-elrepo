Name:           yum-conf-elrepo       
Version:        6
Release:        1.1
Summary:        ElRepo.org Community Enterprise Linux Repository release file
Group:          System Environment/Base 
License:        GPL 
URL:            http://elrepo.org/
BuildArch:      noarch
Requires:       elrepo-release
Requires:	yum-plugin-fastestmirror

%description
This package pulls in elrepo-release which contains the
yum configuration for the ElRepo.org Community 
Enterprise Linux Repository, as well as the public GPG keys 
used to sign packages.

%files


%changelog
* Tue Dec 6 2011 Pat Riehecky <riehecky@fnal.gov> - 6-1.1
- Added requires yum-plugin-fastest mirror (adding to all non SL yum-conf packages) 

* Thu Jan 13 2011 Troy Dawson <dawson@fnal.gov> - 6-1
- The rpm only pulls in the appropriate release package

