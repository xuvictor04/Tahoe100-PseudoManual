---
symbol: "ARL13B"
type: "gene"
col: 9801
ensembl_id: "ENSG00000169379"
name: "ARF like GTPase 13B"
location: "3q11.1-q11.2"
module: 60
arm: "-"
pooled_cpm: 68.83
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# ARL13B

*ARF like GTPase 13B* — 3q11.1-q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.75× (z +52.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.795× (z -7.7, q 6e-12, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.455×, A-172 0.631×, A-427 0.667×; ⚠ cell-cycle shift, explains ~42% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.0973×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (HS-578T 0.188×; ⚠ toxic); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0636×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.476×).
> Its strongest partners by |cos| (65 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 36 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMC6]] (+0.68, fdr 1e-05), [[KRTCAP2]] (+0.54, fdr 1e-04), [[MIER1]] (+0.51, fdr 5e-05); moves opposite to [[HSPE1-MOB4]] (-0.59, fdr 5e-05), [[SERPINH1]] (-0.56, fdr 1e-05), [[UBXN8]] (-0.55, fdr 3e-04).
> It sits in the **-** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FER1L6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.75×** | +52.2 | 0e+00 | 48/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.14×** | +33.7 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.36×** | +33.6 | 0e+00 | 48/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.68×** | +30.9 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.43×** | +29.2 | 0e+00 | 48/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.37×** | +28.8 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.48×** | +21.5 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.13×** | +17.9 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +16.2 | 0e+00 | 45/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +13.9 | 3e-42 | 44/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +13.4 | 5e-39 | 44/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.76×** | +13.4 | 5e-39 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.73×** | +12.9 | 1e-36 | 43/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.54×** | +11.6 | 3e-29 | 36/49 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.62×** | +11.0 | 2e-26 | 38/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.31×** | +10.4 | 1e-23 | 44/49 (HEC-1-A, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +6.3 | 7e-09 | 28/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.65×** | +6.2 | 1e-08 | 25/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9801.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.455×, A-172 0.631×, A-427 0.667×; ⚠ cell-cycle shift, explains ~42% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.0973×; ⚠ toxic; cell-cycle shift, explains ~33% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (HS-578T 0.188×; ⚠ toxic); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0636×); [[Auranofin (drug)]] 5 µM in 1 line (HEC-1-A 0.476×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.795×** | -7.7 | 6e-12 | 25/48 (A498, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.837× | -4.2 | 0.006 | 16/48 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.849× | -3.9 | 0.016 | 21/48 (HEC-1-A, SHP-77, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.853× | -3.5 | 0.075 | 11/48 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.875× | -3.2 | 0.15 | 10/48 (COLO 205, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 53.0 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.86× (z +32.3) | — |
| [[A-427 (line)]] | wt | 117 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +21.6) | — |
| [[HEC-1-A (line)]] | alt | 91.7 | 12 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +27.7) | [[Auranofin (drug)]] 5 µM 0.476× (z -9.5) |
| [[PANC-1 (line)]] | alt | 104 | 13 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +46.0) | — |
| [[SW480 (line)]] | alt | 55.9 | 12 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +25.5) | — |
| [[BT-474 (line)]] | alt | 30.9 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +15.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0973× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 51.8 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +24.9) | — |
| [[NCI-H1573 (line)]] | alt | 46.8 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +27.1) | — |
| [[NCI-H23 (line)]] | alt | 100 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +25.0) | — |
| [[SNU-1 (line)]] | wt | 53.5 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 70.5 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +33.4) | — |
| [[RKO (line)]] | wt | 80.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.53× (z +27.1) | — |
| [[SW 900 (line)]] | alt | 80.5 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +22.5) | — |
| [[A-172 (line)]] | wt | 95.0 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.21× (z +30.6) | [[Selinexor (drug)]] 5 µM 0.631× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 30.8 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +24.4) | — |
| [[LoVo (line)]] | wt | 36.0 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +19.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.7 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +25.8) | — |
| [[Panc 03.27 (line)]] | alt | 54.8 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.43× (z +24.6) | — |
| [[SK-MEL-2 (line)]] | alt | 98.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +29.1) | — |
| [[SW1417 (line)]] | alt | 60.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +24.1) | — |
| [[A498 (line)]] | wt | 104 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +19.2) | [[Selinexor (drug)]] 5 µM 0.455× (z -15.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A549 (line)]] | wt | 95.3 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +27.4) | — |
| [[C32 (line)]] | wt | 58.7 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +23.9) | — |
| [[CFPAC-1 (line)]] | alt | 46.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.47× (z +26.6) | — |
| [[HT-29 (line)]] | alt | 63.4 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +23.6) | — |
| [[LOX-IMVI (line)]] | wt | 69.8 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +22.3) | — |
| [[LS 180 (line)]] | wt | 24.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +16.2) | — |
| [[SNU-423 (line)]] | alt | 45.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +21.8) | — |
| [[H4 (line)]] | wt | 57.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +16.1) | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +14.3) | — |
| [[HS-578T (line)]] | alt | 129 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +15.9) | [[Lonafarnib (drug)]] 5 µM 0.188× (z -9.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 43.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +20.2) | — |
| [[KATO III (line)]] | alt | 33.1 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +16.3) | — |
| [[NCI-H2030 (line)]] | alt | 50.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +24.7) | — |
| [[RPMI-7951 (line)]] | alt | 67.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +17.8) | — |
| [[C-33 A (line)]] | alt | 119 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.45× (z +10.0) | — |
| [[COLO 205 (line)]] | alt | 32.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 48.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +20.1) | — |
| [[J82 (line)]] | alt | 146 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +25.6) | — |
| [[SW48 (line)]] | wt | 37.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 30.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +19.4) | — |
| [[SHP-77 (line)]] | alt | 104 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.5) | — |
| [[SW 1088 (line)]] | alt | 73.1 | 0 | 2 (1 ⚠) | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0636× (z -9.5) |
| [[AN3 CA (line)]] | alt | 99.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC6]] | +0.68 | +0.55 / +0.72 | both halves | 1e-05 | **novel candidate** |
| [[KRTCAP2]] | +0.54 | +0.48 / +0.36 | both halves | 1e-04 |  |
| [[MIER1]] | +0.51 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[DNAJC1]] | +0.51 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SVIP]] | +0.51 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[CHD1]] | +0.50 | +0.22 / +0.52 | both halves | 6e-04 |  |
| [[HCFC2]] | +0.49 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[PAXX]] ⚠ | +0.49 | +0.24 / +0.43 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HERC1]] | +0.48 | +0.20 / +0.58 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CEP57L1]] | +0.48 | +0.17 / +0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[DOP1A]] | +0.47 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[SMCHD1]] | +0.47 | +0.26 / +0.50 | both halves | 3e-04 |  |
| [[CDKN2D]] | +0.45 | +0.22 / +0.38 | both halves | 6e-04 |  |
| [[ZFHX3-AS1]] | +0.44 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[EEA1]] | +0.44 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 28 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPE1-MOB4]] | -0.59 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SERPINH1]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[UBXN8]] | -0.55 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[NAXD]] | -0.53 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PARD6G-AS1]] | -0.53 | -0.10 / -0.54 | ⚠ one half (not replicated) | 0.003 |  |
| [[DNAJA4]] | -0.53 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[FKBP4]] | -0.52 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[AHSA1]] | -0.52 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PTOV1-AS1]] | -0.52 | -0.14 / -0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[PTCD1]] | -0.51 | -0.18 / -0.43 | ⚠ not reproduced | 9e-04 |  |
| [[GPN1]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[KCTD21-AS1]] | -0.47 | -0.02 / -0.42 | ⚠ not reproduced | 0.007 |  |
| [[SDHD]] | -0.47 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[AHSA2P]] | -0.47 | -0.29 / -0.43 | both halves | 3e-04 |  |
| [[MRPL18]] | -0.47 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[HSP90AA2P]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L6]] | B | FER1L6 activity lowers ARL13B's level | lines that do not express FER1L6 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without FER1L6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[DNAJA4]] | B | DNAJA4 activity lowers ARL13B's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 1.48× higher at baseline in the lines without DNAJA4 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-6.3, 26.8); signed map (-12.9, -2.2). **Vector** length 80.1, 22.5% of its response variance represented; |z| ≥ 3 in 1,418 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.3 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +33.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +16.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +13.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +10.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.7 | +2.5 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.7 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +4.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.7 | -3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -8.8 | -7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.3 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.0 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | +4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.9 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 13B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q11.1-q11.2 — chr3:93,980,139-94,055,678 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761H079, JBTS8; previously ARL2L1 |
| Gene groups (HGNC) | ARF GTPase family |
| Reactome | 16 pathways, smallest: ARL13B-mediated ciliary trafficking of INPP5E; Chaperone Mediated Autophagy; Late endosomal microautophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3SXY8](https://www.uniprot.org/uniprotkb/Q3SXY8) (ADP-ribosylation factor-like protein 13B):

> Cilium-specific protein required to control the microtubule-based, ciliary axoneme structure. May act by maintaining the association between IFT subcomplexes A and B. Binds GTP but is not able to hydrolyze fit; the GTPase activity remains unclear. Required to pattern the neural tube. Involved in cerebral cortex development: required for the initial formation of a polarized radial glial scaffold, the first step in the construction of the cerebral cortex, by regulating ciliary signaling. …

**Summary**, from NCBI Gene [200894](https://www.ncbi.nlm.nih.gov/gene/200894):

> This gene encodes a member of the ADP-ribosylation factor-like family. The encoded protein is a small GTPase that contains both N-terminal and C-terminal guanine nucleotide-binding motifs. This protein is localized in the cilia and plays a role in cilia formation and in maintenance of cilia. Mutations in this gene are the cause of Joubert syndrome 8. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:25419](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25419) · Entrez [200894](https://www.ncbi.nlm.nih.gov/gene/200894) · UniProt [Q3SXY8](https://www.uniprot.org/uniprotkb/Q3SXY8) · Ensembl [ENSG00000169379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169379)

## Data

Gene col 9801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9801); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9801]; `tensor/DDL_lfc|DDL_z.npy` [9801]; `embed/gene_vectors.npy` [9801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9801 or target_col == 9801). Every well: [[ARL13B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL13B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
