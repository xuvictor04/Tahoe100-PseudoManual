---
symbol: "ARHGEF26"
type: "gene"
col: 3589
ensembl_id: "ENSG00000114790"
name: "Rho guanine nucleotide exchange factor 26"
location: "3q25.2"
module: 115
arm: "+"
pooled_cpm: 16.96
n_lines_expressing: 46
n_dd_up: 29
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# ARHGEF26

*Rho guanine nucleotide exchange factor 26* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.23× (z +28.1, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.708× (z -5.9, q 2e-06, down in 16 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.751× (z -4.9, q 2e-04, down in 15 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP44]] (+0.65, fdr 2e-05), [[ZYG11A]] (+0.64, fdr 1e-05), [[LRRC20]] (+0.63, fdr 1e-05); moves opposite to [[LINC00174]] (-0.68, fdr 2e-05), [[CHMP4A]] (-0.64, fdr 1e-05), [[RAB30-DT]] (-0.62, fdr 4e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC01239]] → it (grade B ⚠); 4 go from it, the strongest it → [[TMEM131L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.23×** | +28.1 | 0e+00 | 43/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.39×** | +25.1 | 0e+00 | 43/43 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.15×** | +24.2 | 0e+00 | 42/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +18.9 | 0e+00 | 35/41 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.77×** | +17.3 | 0e+00 | 41/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.08×** | +12.4 | 2e-33 | 36/42 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.97×** | +12.2 | 2e-32 | 38/43 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +11.7 | 1e-29 | 35/43 (SW480, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.76×** | +9.3 | 1e-18 | 26/41 (NCI-H460, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +8.7 | 1e-16 | 26/42 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +7.7 | 6e-13 | 23/33 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.55×** | +7.4 | 7e-12 | 23/43 (HEC-1-A, A498, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.06×** | +6.4 | 6e-09 | 20/40 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.48×** | +6.4 | 8e-09 | 22/43 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +5.8 | 2e-07 | 18/43 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +4.5 | 2e-04 | 13/42 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.2 | 7e-04 | 12/43 (C32, LoVo, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.009 | 7/43 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.015 | 3/42 (LOX-IMVI, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.708×** | -5.9 | 2e-06 | 16/36 (HT-29, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -5.6 | 7e-06 | 17/32 (NCI-H2347, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -4.9 | 2e-04 | 15/43 (AN3 CA, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.758×** | -4.6 | 7e-04 | 13/29 (A-427, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.630×** | -4.1 | 0.004 | 15/43 (NCI-H2347, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.9 | 0.009 | 13/43 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.811×** | -3.6 | 0.028 | 16/43 (RKO, SNU-1, …) | two highest doses | low cells (technical?) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.865× | -3.5 | 0.029 | 9/43 (H4, SNU-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.776× | -3.1 | 0.12 | 6/38 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.68 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 45.2 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.20× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -16.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 33.9 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.16× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -12.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 14.2 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +15.3) | — |
| [[SW480 (line)]] | alt | 6.50 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 9.48× (z +12.9) | — |
| [[A498 (line)]] | wt | 7.89 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 11.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.94× (z +10.6) | — |
| [[HEC-1-A (line)]] | alt | 24.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.33× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 13.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.63× (z +15.9) | — |
| [[A-172 (line)]] | wt | 7.78 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 12.1× (z +10.5) | [[Cilostazol (drug)]] 0.05 µM 0.0530× (z -11.5) |
| [[A-427 (line)]] | wt | 63.0 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -17.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.80× (z +9.5) | — |
| [[LoVo (line)]] | wt | 15.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 11.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.58× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 16.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +13.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 33.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.60× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.10× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 6.64 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.32× (z +9.9) | — |
| [[SK-MEL-2 (line)]] | alt | 10.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 7.19 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.5× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 2 | 0 | [[Belinostat (drug)]] 5 µM 5.40× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 23.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.87× (z +9.7) | — |
| [[SHP-77 (line)]] | alt | 19.5 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.0656× (z -14.6) |
| [[AN3 CA (line)]] | alt | 39.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.118× (z -8.9) |
| [[C32 (line)]] | wt | 10.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 8.98× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0544× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 15.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +9.5) | — |
| [[AsPC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP44]] | +0.65 | +0.48 / +0.70 | both halves | 2e-05 | pathway: CDC42 GTPase cycle |
| [[ZYG11A]] | +0.64 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ABHD12]] | +0.61 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[DSCC1]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[TMEM131L]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[MBOAT1]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[C1orf21]] | +0.59 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[TSPAN33]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[TBC1D2B]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[SCML2]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[LYPD6]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00174]] | -0.68 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CHMP4A]] | -0.64 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.62 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[METTL6]] | -0.61 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[CDKL3]] | -0.60 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[FCF1]] | -0.59 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MSANTD3-TMEFF1]] | -0.59 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[GTF2H1]] | -0.58 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[FAM200A]] | -0.58 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ZNF407-AS1]] | -0.58 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[ZNF140]] | -0.58 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[SLC22A1]] | -0.58 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01239]] | B | LINC01239 activity lowers ARHGEF26's level | lines that do not express LINC01239 (19) vs lines expressing it (31) | 1.60× higher at baseline in the lines without LINC01239 | 0.064 | ⚠ within organs, on part of the lines; also absent: DMRTA1, ZFPM2-AS1, MIR4500HG |
| [[NEURL1B]] | B | NEURL1B activity raises ARHGEF26's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.00× lower at baseline in the lines without NEURL1B | 0.098 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[TMEM131L]] | C | TMEM131L activity raises ARHGEF26's level | lines that do not express TMEM131L (3) vs lines expressing it (47) | 5.17× lower at baseline in the lines without TMEM131L | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: DPF1, TBC1D19, ARHGEF26; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM131L]] | C | ARHGEF26 activity raises TMEM131L's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 3.50× lower at baseline in the lines without ARHGEF26 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1; co-absent with the target; its own permutation p |
| [[KLHL8]] | C | ARHGEF26 activity raises KLHL8's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ARHGEF26 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |
| [[NEURL1B]] | C | ARHGEF26 activity raises NEURL1B's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 2.31× lower at baseline in the lines without ARHGEF26 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |
| [[TLCD4]] | C | ARHGEF26 activity raises TLCD4's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 4.02× lower at baseline in the lines without ARHGEF26 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.9, 37.7); signed map (-18.9, 19.4). **Vector** length 74.7, 14.7% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +11.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +17.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +8.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +12.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +2.8 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.5 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.6 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | +1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.5 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.2 — chr3:154,121,003-154,257,827 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434D146, SGEF |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DR7](https://www.uniprot.org/uniprotkb/Q96DR7) (Rho guanine nucleotide exchange factor 26):

> Activates RhoG GTPase by promoting the exchange of GDP by GTP. Required for the formation of membrane ruffles during macropinocytosis. Required for the formation of cup-like structures during trans-endothelial migration of leukocytes. In case of Salmonella enterica infection, activated by SopB, which induces cytoskeleton rearrangements and promotes bacterial entry.

**Summary**, from NCBI Gene [26084](https://www.ncbi.nlm.nih.gov/gene/26084):

> This gene encodes a member of the Rho-guanine nucleotide exchange factor (Rho-GEF) family. These proteins regulate Rho GTPases by catalyzing the exchange of GDP for GTP. The encoded protein specifically activates RhoG and plays a role in the promotion of macropinocytosis. Underexpression of the encoded protein may be a predictive marker of chemoresistant disease. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:24490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24490) · Entrez [26084](https://www.ncbi.nlm.nih.gov/gene/26084) · UniProt [Q96DR7](https://www.uniprot.org/uniprotkb/Q96DR7) · Ensembl [ENSG00000114790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114790)

## Data

Gene col 3589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3589); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3589]; `tensor/DDL_lfc|DDL_z.npy` [3589]; `embed/gene_vectors.npy` [3589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3589 or target_col == 3589). Every well: [[ARHGEF26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
