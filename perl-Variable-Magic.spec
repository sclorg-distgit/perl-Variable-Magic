%{?scl:%scl_package perl-Variable-Magic}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Variable_Magic_enables_optional_test
%else
%bcond_with perl_Variable_Magic_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-Variable-Magic
Version:        0.62
Release:        9%{?dist}
Summary:        Associate user-defined magic to variables from Perl
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Variable-Magic
Source0:        https://cpan.metacpan.org/authors/id/V/VP/VPIT/Variable-Magic-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.8
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# Tests
BuildRequires:  %{?scl_prefix}perl(B::Deparse)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(vars)
%if %{with perl_Test_Warnings_enables_optional_test}
# Optional Tests
BuildRequires:  %{?scl_prefix}perl(Hash::Util::FieldHash)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(IO::Select)
BuildRequires:  %{?scl_prefix}perl(IPC::Open3)
BuildRequires:  %{?scl_prefix}perl(Perl::Destruct::Level)
BuildRequires:  %{?scl_prefix}perl(Socket)
BuildRequires:  %{?scl_prefix}perl(Symbol)
BuildRequires:  %{?scl_prefix}perl(threads)
BuildRequires:  %{?scl_prefix}perl(threads::shared)
BuildRequires:  %{?scl_prefix}perl(Tie::Array)
BuildRequires:  %{?scl_prefix}perl(Tie::Hash)
%endif
# Dependencies
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%description
Magic is Perl way of enhancing objects. This mechanism let the user add
extra data to any variable and hook syntactical operations (such as access,
assignation or destruction) that can be applied to it. With this module,
you can add your own magic to any variable without the pain of the C API.

%prep
%setup -q -n Variable-Magic-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}

find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete

%{_fixperms} -c $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Variable*
%{_mandir}/man3/*

%changelog
* Fri Jan 03 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-9
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-4
- Perl 5.28 rebuild

* Wed Feb 21 2018 Paul Howarth <paul@city-fan.org> - 0.62-3
- Specify all dependencies

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.62-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.62-1
- 0.62 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.61-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.61-2
- Perl 5.26 rebuild

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.61-1
- Update to 0.61

* Sat Sep 10 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.60-1
- Update to 0.60

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.59-1
- Update to 0.59

* Thu Jul 23 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.58-1
- Update to 0.58

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.57-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.57-1
- Update to 0.57

* Sun Mar 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.56-1
- Update to 0.56

* Fri Oct 24 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.55-1
- Update to 0.55

* Sat Sep 27 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.54-1
- Update to 0.54

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 08 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 0.53-1
- Update to 0.53
- Fix incorrect dates in changelog

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.52-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov 11 2012 Emmanuel Seyman <emmanuel@seyman.fr> - 0.52-1
- Update to 0.52

* Sun Aug 19 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.51-1
- Update to 0.51

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 0.50-2
- Perl 5.16 rebuild

* Tue Jun 26 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.50-1
- Update to 0.50

* Wed Jun 13 2012 Petr Pisar <ppisar@redhat.com> - 0.49-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.49-1
- Update to 0.49

* Tue Apr 24 2012 Petr Pisar <ppisar@redhat.com> - 0.48-2
- Do not use Test::Kwalitee on RHEL >= 7 (#815750)

* Sat Feb 18 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.48-1
- Update to 0.48

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 30 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.47-1
- Update to 0.47
- Clean up spec file

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.46-3
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 24 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.46-1
- Update to 0.46

* Mon Nov 22 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.45-1
- Update to 0.45

* Wed Sep 29 2010 jkeating - 0.44-2
- Rebuilt for gcc bug 634757

* Fri Sep 24 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.44-1
- Update to 0.44.

* Sat Jun 26 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.43-1
- Update to 0.43.

* Wed May 19 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.42-1
- Update to 0.42.

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.41-2
- Mass rebuild with perl-5.12.0

* Sun Apr 11 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.41-1
- Update to 0.41

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.37-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.37-1
- auto-update to 0.37 (by cpan-spec-update 0.01)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May 16 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.34-1
- update to 0.34 (for B::Hooks::EndOfScope 0.08)
- filter private Perl .so's

* Mon Mar  9 2009 Allisson Azevedo <allisson@gmail.com> - 0.32-1
- Update to 0.32

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Allisson Azevedo <allisson@gmail.com> 0.30-1
- Initial rpm release.
