---
symbol: "HCFC2"
type: "gene"
col: 3271
ensembl_id: "ENSG00000111727"
name: "host cell factor C2"
location: "12q23.3"
module: 5
arm: "-"
pooled_cpm: 26.69
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 15
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# HCFC2

*host cell factor C2* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.46× (z +27.1, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.560× (z -11.4, q 4e-27, down in 30 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.699× (z -7.6, q 5e-12, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DOP1A]] (+0.75, fdr 7e-06), [[ASB8]] (+0.64, fdr 7e-06), [[HCFC1R1]] (+0.62, fdr 1e-05); moves opposite to [[AHSA1]] (-0.66, fdr 7e-06), [[SMG1P6]] (-0.61, fdr 1e-05), [[NPIPB11]] (-0.57, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.46×** | +27.1 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.51×** | +18.8 | 0e+00 | 46/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.38×** | +18.4 | 0e+00 | 42/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +17.9 | 0e+00 | 38/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +17.2 | 0e+00 | 40/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +17.0 | 0e+00 | 39/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +11.1 | 2e-26 | 35/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +7.5 | 3e-12 | 25/48 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 8e-11 | 24/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.0 | 1e-10 | 24/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +5.8 | 4e-07 | 18/48 (PANC-1, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.25×** | +5.0 | 3e-05 | 15/48 (NCI-H23, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +4.8 | 6e-05 | 17/48 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.21×** | +4.8 | 6e-05 | 15/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.8 | 7e-05 | 16/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3271.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.560×** | -11.4 | 4e-27 | 30/41 (A549, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.589×** | -11.2 | 1e-26 | 30/43 (LOX-IMVI, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.581×** | -11.1 | 3e-26 | 29/47 (HOP62, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.699×** | -7.6 | 5e-12 | 25/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.720×** | -6.7 | 2e-09 | 17/33 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -6.5 | 1e-08 | 21/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.767×** | -5.6 | 2e-06 | 21/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -5.5 | 2e-06 | 24/48 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -5.1 | 2e-05 | 2/48 (KATO III, SW48) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.670×** | -4.4 | 5e-04 | 16/48 (BT-474, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.804×** | -4.4 | 6e-04 | 21/48 (Hs 766T, A-172, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.818×** | -4.1 | 0.002 | 18/47 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.842× | -3.6 | 0.011 | 12/47 (H4, HOP62, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.6 | 0.011 | 10/48 (H4, MIA PaCa-2, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.849× | -3.5 | 0.020 | 13/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.861× | -3.2 | 0.050 | 10/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.063 | 10/44 (SNU-423, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.868× | -3.0 | 0.077 | 15/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.824×** | -2.9 | 0.090 | 12/48 (SW 1088, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.0 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +19.9) | [[Selinexor (drug)]] 5 µM 0.535× (z -9.4) ⚠ cell-cycle shift, explains ~70% of this change |
| [[NCI-H2347 (line)]] | alt | 28.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.3) | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 23.0 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +15.1) | — |
| [[A549 (line)]] | wt | 38.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -16.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 8.67 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 49.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -17.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 33.1 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.17× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -15.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.6 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.158× (z -13.5) |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -17.9) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -9.3) |
| [[J82 (line)]] | alt | 23.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.1) | [[Bortezomib (drug)]] 5 µM 0.0952× (z -9.3) ⚠ toxic |
| [[LoVo (line)]] | wt | 18.6 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.21× (z +11.0) | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.96× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 24.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +13.0) | [[Verteporfin (drug)]] 5 µM 0.187× (z -8.7) |
| [[KATO III (line)]] | alt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -16.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 15.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +12.9) | — |
| [[RKO (line)]] | wt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 16.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 18.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.1) | — |
| [[C-33 A (line)]] | alt | 34.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -8.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.280× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +13.7) | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.138× (z -9.3) |
| [[SNU-423 (line)]] | alt | 37.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | +0.75 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ASB8]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[HCFC1R1]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[POLK]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SUCLG1]] | +0.61 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MIER1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[POGZ]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KMT5B]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ILK]] | +0.56 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[WASHC3]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[RAB30]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.56 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.66 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[SMG1P6]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[NPIPB11]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[LRP8]] | -0.56 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[FKBP4]] | -0.55 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.54 | -0.53 / -0.52 | both halves | 1e-05 | pathway: Epigenetic regulation by WDR5-containing histone modifying complexes; STRING 982 |
| [[MRPS25]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[HSPE1]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[MACROD1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[KCNIP2]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[POLR3E]] | -0.53 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[CCDC168]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers HCFC2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[JAZF1]] | B | JAZF1 activity raises HCFC2's level | lines that do not express JAZF1 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without JAZF1 | 0.057 | ⚠ within organs, on part of the lines; also absent: FGD1, CERCAM, MPP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.417). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.0, 2.4); signed map (-17.9, -10.2). **Vector** length 110, 29.1% of its response variance represented; |z| ≥ 3 in 1,126 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +17.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +27.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.1 | +7.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +11.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.9 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.6 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.5 | -4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.4 | -11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.5 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | host cell factor C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:104,064,531-104,106,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCF-2 |
| Reactome | 3 pathways, smallest: Formation of WDR5-containing histone-modifying complexes; Epigenetic regulation by WDR5-containing histone modifying complexes; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

UniProt [Q9Y5Z7](https://www.uniprot.org/uniprotkb/Q9Y5Z7) carries no function annotation.

**Summary**, from NCBI Gene [29915](https://www.ncbi.nlm.nih.gov/gene/29915):

> This gene encodes one of two proteins which interact with VP16, a herpes simplex virus protein that initiates virus infection. Both the encoded protein and the original Herpes host cell factor interact with VP16 through a beta-propeller domain. The original Herpes host cell factor, however, is effective at initiating viral infection while the encoded protein is not. Transcripts of varying length due to alternative polyadenylation signals have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24972) · Entrez [29915](https://www.ncbi.nlm.nih.gov/gene/29915) · UniProt [Q9Y5Z7](https://www.uniprot.org/uniprotkb/Q9Y5Z7) · Ensembl [ENSG00000111727](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111727)

## Data

Gene col 3271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3271); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3271]; `tensor/DDL_lfc|DDL_z.npy` [3271]; `embed/gene_vectors.npy` [3271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3271 or target_col == 3271). Every well: [[HCFC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCFC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
