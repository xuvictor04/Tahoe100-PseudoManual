---
symbol: "NME7"
type: "gene"
col: 6685
ensembl_id: "ENSG00000143156"
name: "NME/NM23 family member 7"
location: "1q24.2"
module: 135
arm: "-"
pooled_cpm: 85.28
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# NME7

*NME/NM23 family member 7* — 1q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.45× (z +19.5, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.575× (z -11.5, q 3e-28, down in 37 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.711× (z -10.5, q 2e-23, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIBF1]] (+0.65, fdr 3e-05), [[EFHC1]] (+0.62, fdr 4e-05), [[TMEM67]] (+0.57, fdr 3e-05); moves opposite to [[ANGEL2]] (-0.58, fdr 2e-04), [[FAIM]] (-0.58, fdr 5e-04), [[UBXN2A]] (-0.56, fdr 6e-05).
> It sits in the **-** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[STC1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.45×** | +19.5 | 0e+00 | 46/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +19.1 | 0e+00 | 47/47 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +18.9 | 0e+00 | 46/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +13.0 | 1e-36 | 42/47 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.42×** | +10.0 | 2e-21 | 38/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +8.3 | 1e-14 | 34/47 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +7.2 | 5e-11 | 38/48 (NCI-H460, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 2e-08 | 27/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +6.2 | 5e-08 | 25/47 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +5.3 | 6e-06 | 19/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.5 | 4e-04 | 20/47 (HT-29, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.21×** | +4.1 | 0.002 | 20/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.16× | +3.3 | 0.043 | 11/48 (HT-29, RPMI-7951, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -11.5 | 3e-28 | 37/46 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -11.5 | 3e-28 | 34/44 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -10.5 | 2e-23 | 30/48 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -10.4 | 4e-23 | 29/42 (H4, SW 900, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -10.3 | 1e-22 | 36/47 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.630×** | -9.2 | 2e-18 | 33/48 (SW 900, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.659×** | -9.0 | 1e-17 | 31/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.677×** | -8.1 | 3e-14 | 32/49 (LOX-IMVI, H4, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -7.7 | 1e-12 | 34/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.530×** | -7.2 | 4e-11 | 31/44 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.714×** | -7.0 | 1e-10 | 28/47 (A498, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.723×** | -6.8 | 6e-10 | 27/46 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.789×** | -5.1 | 1e-05 | 22/47 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -4.6 | 1e-04 | 21/47 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.808×** | -4.6 | 1e-04 | 23/47 (A-427, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.814×** | -4.5 | 3e-04 | 24/47 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.811×** | -4.3 | 6e-04 | 25/47 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.822×** | -4.3 | 7e-04 | 20/47 (CHP-212, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.838× | -3.8 | 0.004 | 19/47 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.864× | -3.1 | 0.058 | 18/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.824×** | -3.0 | 0.067 | 14/46 (A-427, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.863× | -3.0 | 0.074 | 11/48 (NCI-H460, RKO, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 83.5 | 5 (1 ⚠) | 12 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.44× (z +17.0) | [[Digitoxin (drug)]] 5 µM 0.325× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -12.5) |
| [[A498 (line)]] | wt | 112 | 3 | 10 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.42× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -14.6) |
| [[CFPAC-1 (line)]] | alt | 136 | 1 | 9 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.28× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -14.7) |
| [[J82 (line)]] | alt | 95.8 | 5 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.00× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.396× (z -9.8) |
| [[SW480 (line)]] | alt | 86.5 | 5 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.06× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.491× (z -9.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.513× (z -8.7) |
| [[HOP62 (line)]] | alt | 134 | 2 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.04× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.372× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 224 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.90× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 106 | 3 | 5 (5 ⚠) | [[Belinostat (drug)]] 5 µM 2.10× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 86.0 | 5 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.34× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -10.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 71.0 | 4 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.60× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.3) |
| [[A549 (line)]] | wt | 99.8 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -13.0) |
| [[COLO 205 (line)]] | alt | 75.3 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -10.6) |
| [[PANC-1 (line)]] | alt | 110 | 6 | 1 | [[Panobinostat (drug)]] 5 µM 2.51× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.8) |
| [[SW 900 (line)]] | alt | 219 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.1) |
| [[H4 (line)]] | wt | 140 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0317× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.0) |
| [[SHP-77 (line)]] | alt | 106 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 102 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.05 µM 2.78× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 95.4 | 4 | 1 | [[Belinostat (drug)]] 5 µM 3.03× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.7) |
| [[C32 (line)]] | wt | 47.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.22× (z +14.2) | — |
| [[HepG2_C3A (line)]] | wt | 45.2 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.96× (z +9.4) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.135× (z -13.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 41.7 | 3 | 2 | [[Panobinostat (drug)]] 5 µM 5.50× (z +13.9) | [[Ixazomib citrate (drug)]] 5 µM 0.280× (z -10.4) |
| [[HS-578T (line)]] | alt | 63.4 | 3 | 1 | [[Belinostat (drug)]] 5 µM 2.82× (z +10.3) | [[Harringtonine (drug)]] 5 µM 0.378× (z -9.4) |
| [[HT-29 (line)]] | alt | 52.9 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +12.8) | — |
| [[LoVo (line)]] | wt | 32.6 | 4 | 0 | [[Belinostat (drug)]] 5 µM 4.74× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 34.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +12.3) | — |
| [[NCI-H23 (line)]] | alt | 65.5 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 54.9 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.99× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 61.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -10.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 36.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.337× (z -8.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[AsPC-1 (line)]] | alt | 77.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.43× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 22.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.4× (z +13.0) | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 60.1 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.48× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 68.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.50× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 98.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.9) |
| [[AN3 CA (line)]] | alt | 78.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -10.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 82.2 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 102 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.93× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -10.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 89.8 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +10.1) | — |
| [[RPMI-7951 (line)]] | alt | 89.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 34.4 | 2 | 0 | [[Belinostat (drug)]] 5 µM 5.85× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 44.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +9.8) | — |
| [[KATO III (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | +0.65 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[EFHC1]] | +0.62 | +0.57 / +0.42 | both halves | 4e-05 | STRING 849 |
| [[TMEM67]] | +0.57 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[RNF213-AS1]] | +0.55 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[DCUN1D3]] | +0.55 | +0.54 / +0.36 | both halves | 9e-05 |  |
| [[DAD1]] | +0.55 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[WDPCP]] | +0.54 | +0.48 / +0.38 | both halves | 7e-05 |  |
| [[GP6-AS1]] | +0.53 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SLC2A3]] | +0.53 | +0.42 / +0.33 | both halves | 1e-04 |  |
| [[BLZF1]] | +0.52 | +0.60 / +0.44 | both halves | 3e-05 | STRING 413; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[VTA1]] | +0.51 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[ARL4C]] | +0.51 | +0.44 / +0.34 | both halves | 1e-04 |  |
| [[DNTTIP1]] | +0.51 | +0.57 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANGEL2]] | -0.58 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[FAIM]] | -0.58 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[UBXN2A]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[GCNT4]] | -0.55 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[ECPAS]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[PRDM2]] | -0.54 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[NCOA2]] | -0.54 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[TMCO4]] | -0.54 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[PHF2]] | -0.54 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[TSTD3]] | -0.54 | -0.45 / -0.22 | both halves | 6e-04 |  |
| [[NACC2]] | -0.52 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[UBTF]] | -0.52 | -0.46 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STC1]] | B | STC1 activity raises NME7's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.93× lower at baseline in the lines without STC1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[GP6-AS1]] | B | GP6-AS1 activity raises NME7's level | lines that do not express GP6-AS1 (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without GP6-AS1 | 0.092 | ⚠ within organs, on part of the lines |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NME7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NME7's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **-** arm (projection on the module's main direction -0.569). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-7.8, 8.6); signed map (-39.4, 14.1). **Vector** length 127, 41.2% of its response variance represented; |z| ≥ 3 in 1,512 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +11.3 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.7 | +19.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.4 | +18.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +19.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.0 | +13.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +7.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +2.1 | +2.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.6 | -10.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -10.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.5 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | NME/NM23 family member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q24.2 — chr1:169,132,531-169,367,948 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ37194, NM23-H7, CFAP67 |
| Gene groups (HGNC) | NME/NM23 family; Cilia and flagella associated |
| Reactome | 9 pathways, smallest: Centrosome maturation; Recruitment of mitotic centrosome proteins and complexes; Recruitment of NuMA to mitotic centrosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5B8](https://www.uniprot.org/uniprotkb/Q9Y5B8) (Nucleoside diphosphate kinase 7):

> Possesses an intrinsic kinase activity. Phosphorylates GSK3B at 'Ser-9', leading to the activation of Wnt/beta-catenin signaling. Additionally, exhibits a 3'-5'-DNA exonuclease activity that removes single nucleotides from the 3' terminus of single-stranded DNA substrates and digests overhanging mismatched 3' termini from double-stranded DNA substrates, possibly participating in DNA nucleolytic processing. In vitro, does not seem to have nucleoside diphosphate kinase activity. Functional …

**Summary**, from NCBI Gene [29922](https://www.ncbi.nlm.nih.gov/gene/29922):

> This gene encodes a member of the non-metastatic expressed family of nucleoside diphosphate kinases. Members of this family are enzymes that catalyzes phosphate transfer from nucleoside triphosphates to nucleoside diphosphates. This protein contains two kinase domains, one of which is involved in autophosphorylation and the other may be inactive. This protein localizes to the centrosome and functions as a component of the gamma-tubulin ring complex which plays a role in microtubule …

**Accessions** — [HGNC:20461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20461) · Entrez [29922](https://www.ncbi.nlm.nih.gov/gene/29922) · UniProt [Q9Y5B8](https://www.uniprot.org/uniprotkb/Q9Y5B8) · Ensembl [ENSG00000143156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143156)

## Data

Gene col 6685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6685); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6685]; `tensor/DDL_lfc|DDL_z.npy` [6685]; `embed/gene_vectors.npy` [6685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6685 or target_col == 6685). Every well: [[NME7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NME7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
