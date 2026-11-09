---
symbol: "MSANTD3-TMEFF1"
type: "gene"
col: 14758
ensembl_id: "ENSG00000251349"
name: "MSANTD3-TMEFF1 readthrough"
location: "9q31.1"
module: 181
arm: "+"
pooled_cpm: 9.67
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 16
n_dd_up_clean: 19
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/181"]
generated_by: "tahoemap"
---

# MSANTD3-TMEFF1

*MSANTD3-TMEFF1 readthrough* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.20× (z +28.6, q 0e+00, up in 43 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.331× (z -15.6, q 0e+00, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAVIN4]] (+0.86, fdr 7e-06, ⚠ same locus), [[TMEFF1]] (+0.80, fdr 7e-06, ⚠ same locus), [[THAP2]] (+0.73, fdr 1e-05), [[LINC01191]] (+0.72, fdr 7e-06), [[IL34]] (+0.72, fdr 3e-05); moves opposite to [[SLC9A6]] (-0.64, fdr 4e-05), [[L2HGDH]] (-0.63, fdr 1e-05), [[FAM118A]] (-0.63, fdr 3e-04).
> It is in [[Module 181]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[JAM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.20×** | +28.6 | 0e+00 | 43/44 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.12×** | +16.0 | 0e+00 | 37/43 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.80×** | +15.1 | 0e+00 | 38/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +10.4 | 3e-23 | 20/23 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.13×** | +10.2 | 2e-22 | 32/45 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.19×** | +8.5 | 1e-15 | 14/20 (HOP62, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +7.3 | 2e-11 | 22/45 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +6.0 | 2e-07 | 22/46 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.8 | 4e-07 | 21/43 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.6 | 1e-06 | 12/33 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.4 | 3e-06 | 7/20 (A549, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.0 | 2e-05 | 15/41 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.6 | 2e-04 | 13/42 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.39×** | +4.6 | 2e-04 | 14/47 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +4.5 | 3e-04 | 14/39 (HOP62, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.24×** | +4.3 | 7e-04 | 9/46 (SW480, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +4.1 | 0.001 | 12/41 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.002 | 10/46 (A-172, KATO III, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.012 | 8/46 (A-172, RKO, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.331×** | -15.6 | 0e+00 | 41/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.375×** | -13.8 | 4e-41 | 37/46 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.443×** | -11.5 | 3e-28 | 33/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.657×** | -5.9 | 4e-07 | 19/47 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -5.9 | 4e-07 | 21/40 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[NG25 (drug)]] 5 µM |  | **0.514×** | -4.9 | 9e-05 | 17/37 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.521×** | -4.8 | 1e-04 | 15/44 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.715×** | -4.7 | 1e-04 | 18/45 (A549, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.755×** | -4.0 | 0.005 | 11/46 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.772×** | -3.7 | 0.014 | 14/45 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.770×** | -3.5 | 0.020 | 16/45 (NCI-H1573, A549, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.785×** | -3.4 | 0.029 | 9/45 (C-33 A, HOP62, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.796×** | -3.2 | 0.050 | 13/45 (A549, NCI-H2030, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.846× | -3.2 | 0.050 | 7/46 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.803×** | -3.1 | 0.071 | 10/38 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 26.9 | 6 | 3 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +23.8) | [[Panobinostat (drug)]] 5 µM 0.136× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -17.9) |
| [[NCI-H460 (line)]] | wt | 11.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +13.7) | — |
| [[A498 (line)]] | wt | 4.95 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 16.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +15.9) | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -9.7) |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -12.4) |
| [[PANC-1 (line)]] | alt | 7.27 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.76× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.219× (z -9.2) |
| [[A549 (line)]] | wt | 12.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -8.9) |
| [[H4 (line)]] | wt | 25.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0863× (z -11.7) |
| [[J82 (line)]] | alt | 13.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.214× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 15.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +15.8) | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0948× (z -12.6) |
| [[C32 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.154× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 3.38 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0753× (z -9.2) |
| [[COLO 205 (line)]] | alt | 4.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 8.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 19.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0672× (z -12.8) |
| [[KATO III (line)]] | alt | 3.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.88× (z +10.5) | — |
| [[LoVo (line)]] | wt | 3.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 6.43 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.51× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 5.83 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.96× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.98× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.3× (z +20.3) | — |
| [[SW 900 (line)]] | alt | 8.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +9.2) | — |
| [[A-427 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 5 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAVIN4]] | +0.86 | +0.91 / +0.73 | both halves | 7e-06 | STRING 403; ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[TMEFF1]] | +0.80 | +0.83 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[THAP2]] | +0.73 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[LINC01191]] | +0.72 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MSANTD3]] | +0.72 | +0.75 / +0.67 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of MSANTD3 on the same strand (can correlate by spillover, not regulation) |
| [[IL34]] | +0.72 | +0.71 / +0.46 | both halves | 3e-05 |  |
| [[LINC02542]] | +0.72 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[MSH4]] | +0.70 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.70 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[C3orf20]] | +0.70 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.70 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[SLC22A1]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[LINC00486]] | +0.69 | +0.68 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A6]] | -0.64 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.63 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FAM118A]] | -0.63 | -0.61 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[JAM2]] | B | JAM2 activity raises MSANTD3-TMEFF1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without JAM2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[LINC00702]] | B | LINC00702 activity raises MSANTD3-TMEFF1's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without LINC00702 | 0.044 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[LINC00504]] | B | LINC00504 activity raises MSANTD3-TMEFF1's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.64× lower at baseline in the lines without LINC00504 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[LINC01291]] | B | LINC01291 activity raises MSANTD3-TMEFF1's level | lines that do not express LINC01291 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without LINC01291 | 0.055 | ⚠ within organs, on part of the lines; also absent: ANTXR2, ENSG00000230479, PROCR; maybe low, not absent |
| [[AXL]] | B | AXL activity raises MSANTD3-TMEFF1's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without AXL | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[LRIF1]] | B | LRIF1 activity lowers MSANTD3-TMEFF1's level | lines that do not express LRIF1 (5) vs lines expressing it (45) | 1.07× higher at baseline in the lines without LRIF1 | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RAP1GAP2, PPFIA4, AP1S3 |
| [[MSANTD3]] | C | MSANTD3's natural level strengthens MSANTD3-TMEFF1's drug response | MSANTD3's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.50; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ZFHX2-AS1]] | C | ZFHX2-AS1's natural level weakens MSANTD3-TMEFF1's drug response | ZFHX2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.03; direction clear | 0.020 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 181]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.794). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.9, -4.2); signed map (24.7, 8.1). **Vector** length 98.0, 21.3% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.8 | +28.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +16.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +10.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.0 | +10.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -13.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -11.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -15.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.4 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -4.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | MSANTD3-TMEFF1 readthrough |
| Locus type | readthrough (other) |
| Location | 9q31.1 — chr9:100,442,271-100,577,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C9orf30-TMEFF1 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100526694](https://www.ncbi.nlm.nih.gov/gene/100526694):

> This locus represents naturally occurring read-through transcription from the neighboring MSANTD3 (Myb/SANT-like DNA-binding domain containing 3) and TMEFF1 (transmembrane protein with EGF-like and two follistatin-like domains 1) genes. The read-through transcript encodes a fusion protein that shares sequence identity with the products of each individual gene. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:38838](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38838) · Entrez [100526694](https://www.ncbi.nlm.nih.gov/gene/100526694) · Ensembl [ENSG00000251349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251349)

## Data

Gene col 14758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14758); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14758]; `tensor/DDL_lfc|DDL_z.npy` [14758]; `embed/gene_vectors.npy` [14758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14758 or target_col == 14758). Every well: [[MSANTD3-TMEFF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSANTD3-TMEFF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
