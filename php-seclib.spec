# TODO
# - individual php-pear-XXX packages
#   http://phpseclib.sourceforge.net/pear.htm
#   pear remote-list -c phpseclib
#   this way it won't file-conflict with PEAR packages
# - patch location of CRYPT_RSA_OPENSSL_CONFIG (currently not installed)
%define		pkgname	seclib
%define		php_min_version 5.2.0
Summary:	PHP Secure Communications Library
Name:		php-%{pkgname}
Version:	0.3.5
Release:	3
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/phpseclib/phpseclib%{version}.zip
# Source0-md5:	d4a0692a8c2d5ef919f8f867e3878a74
URL:		http://phpseclib.sourceforge.net/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	unzip
Patch0:		includes.patch
Requires:	php(bcmath)
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(hash)
Requires:	php(openssl)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	php-pear
Obsoletes:	php-pear-Crypt_Blowfish <= 1.1.0-0.RC2.2
Obsoletes:	php-pear-Crypt_RSA <= 1.2.1-3
Obsoletes:	php-pear-Math_BigInteger <= 1.0.3-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure-PHP implementations of an arbitrary-precision integer arithmetic
library, fully PKCS#1 (v2.1) compliant RSA, DES, 3DES, RC4, Rijndael,
AES, SSH-1, SSH-2, and SFTP.

%prep
%setup -qc
%undos -f php
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cp -a . $RPM_BUILD_ROOT%{php_pear_dir}

%{__rm} $RPM_BUILD_ROOT%{php_pear_dir}/openssl.cnf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc openssl.cnf
%{php_pear_dir}/Crypt/AES.php
%{php_pear_dir}/Crypt/Blowfish.php
%{php_pear_dir}/Crypt/DES.php
%{php_pear_dir}/Crypt/Hash.php
%{php_pear_dir}/Crypt/Random.php
%{php_pear_dir}/Crypt/RC4.php
%{php_pear_dir}/Crypt/Rijndael.php
%{php_pear_dir}/Crypt/RSA.php
%{php_pear_dir}/Crypt/TripleDES.php
%{php_pear_dir}/Crypt/Twofish.php
%{php_pear_dir}/File/ANSI.php
%{php_pear_dir}/File/ASN1.php
%{php_pear_dir}/File/X509.php
%{php_pear_dir}/Math/BigInteger.php
%{php_pear_dir}/Net/SCP.php
%{php_pear_dir}/Net/SFTP.php
%dir %{php_pear_dir}/Net/SFTP
%{php_pear_dir}/Net/SFTP/Stream.php
%{php_pear_dir}/Net/SSH1.php
%{php_pear_dir}/Net/SSH2.php
