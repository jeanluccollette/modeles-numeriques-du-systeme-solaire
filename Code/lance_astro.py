import astro
astro.planetes(Planetes='Planetes.csv')
df = astro.lire_info_csv('Planetes.csv')
print(df)
astro.liste_id()
astro.convert_req_jpl_to_csv(
    Planetes='Planetes.csv', debut='2020-01-01 00:00:00', fin='2040-01-01 00:00:00', pas='8 h')
astro.simu_systsol_save(Planetes='Planetes.csv', methode='rk8')
astro.compare(Astre1_a='Terre', Astre2_a='Lune',
              Astre1_b='Terre_simu', Astre2_b='Lune_simu')
astro.compare(Astre1_a='Soleil', Astre2_a='Mercure',
              Astre1_b='Soleil_simu', Astre2_b='Mercure_simu')
astro.compare(Astre1_a='Soleil', Astre2_a='Terre',
              Astre1_b='Soleil_simu', Astre2_b='Terre_simu')
astro.compare(Astre1_a='Soleil', Astre2_a='Mars',
              Astre1_b='Soleil_simu', Astre2_b='Mars_simu')
astro.orbite_kepler(Astre1='Soleil', Astre2='Mercure', Planetes='Planetes.csv',
                    Astre1_k='Soleil_k', Astre2_k='Mercure_k', Planetes_k='Planetes_sol_mer.csv')
astro.simu_systsol_save(Planetes='Planetes_sol_mer.csv', methode='rk8')
astro.compare(Astre1_a='Soleil_k', Astre2_a='Mercure_k',
              Astre1_b='Soleil_k_simu', Astre2_b='Mercure_k_simu')
astro.orbite_kepler(Astre1='Terre', Astre2='Lune', Planetes='Planetes.csv',
                    Astre1_k='Terre_k', Astre2_k='Lune_k', Planetes_k='Planetes_ter_lun.csv')
astro.simu_systsol_save(Planetes='Planetes_ter_lun.csv', methode='rk8')
astro.compare(Astre1_a='Terre_k', Astre2_a='Lune_k',
              Astre1_b='Terre_k_simu', Astre2_b='Lune_k_simu')
astro.param_orb_comp(Astre1_a='Soleil', Astre2_a='Venus', Astre1_b='Soleil_simu', Astre2_b='Venus_simu',
                     Planetes='Planetes.csv')
astro.param_orb_comp(Astre1_a='Soleil', Astre2_a='Mercure', Astre1_b='Soleil_simu', Astre2_b='Mercure_simu',
                     Planetes='Planetes.csv')
