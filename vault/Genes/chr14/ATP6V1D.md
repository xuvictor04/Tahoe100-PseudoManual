---
symbol: "ATP6V1D"
type: "gene"
col: 1983
ensembl_id: "ENSG00000100554"
name: "ATPase H+ transporting V1 subunit D"
location: "14q23.3"
module: 146
arm: "-"
pooled_cpm: 74.31
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/146"]
generated_by: "tahoemap"
---

# ATP6V1D

*ATPase H+ transporting V1 subunit D* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.76× (z +25.8, q 0e+00, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (SW 1088 0.0718×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0785×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.424×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB7A]] (+0.67, fdr 7e-06), [[BLZF1]] (+0.66, fdr 7e-06), [[VPS4B]] (+0.62, fdr 1e-05); moves opposite to [[AHCTF1]] (-0.61, fdr 7e-06), [[NAA16]] (-0.61, fdr 1e-05), [[MACIR]] (-0.59, fdr 1e-05).
> It sits in the **-** arm of [[Module 146]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.76×** | +25.8 | 0e+00 | 45/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.26×** | +21.3 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.02×** | +19.9 | 0e+00 | 48/48 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.92×** | +19.3 | 0e+00 | 48/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +16.4 | 0e+00 | 45/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +12.4 | 4e-33 | 48/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +12.0 | 5e-31 | 44/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.88×** | +11.4 | 3e-28 | 42/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.83×** | +10.9 | 7e-26 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +10.5 | 7e-24 | 42/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.76×** | +10.2 | 9e-23 | 41/49 (PANC-1, C32, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.67×** | +9.3 | 9e-19 | 37/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +8.7 | 1e-16 | 43/48 (HT-29, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.53×** | +7.6 | 9e-13 | 35/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.57×** | +7.5 | 2e-12 | 31/45 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.0 | 9e-11 | 36/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +6.5 | 2e-09 | 28/48 (A-427, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +5.9 | 1e-07 | 31/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +5.6 | 5e-07 | 28/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.6 | 6e-07 | 32/48 (LS 180, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1983.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (SW 1088 0.0718×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0785×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.424×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.05 µM |  | 0.869× | -3.5 | 0.15 | 18/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.873× | -3.5 | 0.15 | 15/48 (Panc 03.27, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.819× | -3.3 | 0.16 | 17/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.836× | -3.2 | 0.16 | 16/48 (AsPC-1, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.838× | -3.2 | 0.16 | 15/49 (LoVo, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 46.8 | 18 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +17.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.74× (z +16.5) | — |
| [[NCI-H460 (line)]] | wt | 64.2 | 15 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +27.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.8 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +23.3) | — |
| [[RKO (line)]] | wt | 109 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.8) | — |
| [[SNU-1 (line)]] | wt | 65.4 | 10 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.2) | — |
| [[SW480 (line)]] | alt | 88.5 | 10 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +15.7) | — |
| [[LOX-IMVI (line)]] | wt | 61.0 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +22.7) | — |
| [[HOP62 (line)]] | alt | 58.5 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +21.3) | — |
| [[A498 (line)]] | wt | 36.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.4) | — |
| [[BT-474 (line)]] | alt | 48.2 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +14.0) | — |
| [[C32 (line)]] | wt | 51.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.2) | — |
| [[HEC-1-A (line)]] | alt | 54.6 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 91.3 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +21.2) | — |
| [[SW 900 (line)]] | alt | 89.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.2) | — |
| [[A-172 (line)]] | wt | 49.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +18.9) | — |
| [[A-427 (line)]] | wt | 53.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.1) | — |
| [[A549 (line)]] | wt | 64.9 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +15.0) | — |
| [[HS-578T (line)]] | alt | 51.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.2) | — |
| [[LoVo (line)]] | wt | 82.7 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +18.6) | — |
| [[NCI-H1573 (line)]] | alt | 64.6 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +17.9) | — |
| [[NCI-H2030 (line)]] | alt | 103 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +16.8) | — |
| [[NCI-H23 (line)]] | alt | 109 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +20.2) | — |
| [[SW1417 (line)]] | alt | 62.9 | 6 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 87.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 68.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 2.88× (z +11.8) | — |
| [[KATO III (line)]] | alt | 91.0 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.23× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 107 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.6) | — |
| [[Panc 03.27 (line)]] | alt | 82.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +13.6) | — |
| [[SHP-77 (line)]] | alt | 68.5 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 64.7 | 5 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.32× (z +14.5) | — |
| [[SW48 (line)]] | wt | 66.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 6.01× (z +13.5) | — |
| [[C-33 A (line)]] | alt | 49.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.5) | — |
| [[CFPAC-1 (line)]] | alt | 127 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 66.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.7) | — |
| [[LS 180 (line)]] | wt | 60.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +14.8) | — |
| [[NCI-H1792 (line)]] | alt | 69.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 87.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +15.4) | — |
| [[SNU-423 (line)]] | alt | 94.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +18.8) | — |
| [[AsPC-1 (line)]] | alt | 143 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.1) | [[Cobimetinib (drug)]] 5 µM 0.424× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 69.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.51× (z +10.0) | — |
| [[H4 (line)]] | wt | 58.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +10.1) | — |
| [[J82 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +15.5) | — |
| [[SW 1088 (line)]] | alt | 69.6 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0718× (z -9.0) |
| [[HCT15 (line)]] | alt | 83.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 87.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB7A]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[BLZF1]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[VPS4B]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ZBTB43]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LAMTOR3]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 | pathway: Amino acids regulate mTORC1; STRING 726 |
| [[CPEB4]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[SYAP1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[SAP30BP]] | +0.56 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHM1]] | +0.56 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CLTA]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[BIN3]] | +0.55 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHCTF1]] | -0.61 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NAA16]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[MACIR]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[C6orf136]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[NSMCE4A]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TADA1]] | -0.57 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PDS5B]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[REV1]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[KDM1A]] | -0.56 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[UCK2]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PROSER1]] | -0.55 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[HSF2]] | -0.55 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP6V1D's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[WFDC3]] | B | WFDC3 activity raises ATP6V1D's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.22× lower at baseline in the lines without WFDC3 | 0.084 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 146]]; 31 genes; this gene is in the **-** arm (projection on the module's main direction -0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (17.7, -25.9); signed map (7.4, 16.9). **Vector** length 97.1, 32.0% of its response variance represented; |z| ≥ 3 in 1,340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +12.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.3 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +8.7 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.5 | +0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.3 | +0.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.8 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.6 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:67,294,371-67,360,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VATD, VMA8; previously ATP6M |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | MTORC1_SIGNALING, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 17 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5K8](https://www.uniprot.org/uniprotkb/Q9Y5K8) (V-type proton ATPase subunit D):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [51382](https://www.ncbi.nlm.nih.gov/gene/51382):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:13527](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13527) · Entrez [51382](https://www.ncbi.nlm.nih.gov/gene/51382) · UniProt [Q9Y5K8](https://www.uniprot.org/uniprotkb/Q9Y5K8) · Ensembl [ENSG00000100554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100554)

## Data

Gene col 1983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1983); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1983]; `tensor/DDL_lfc|DDL_z.npy` [1983]; `embed/gene_vectors.npy` [1983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1983 or target_col == 1983). Every well: [[ATP6V1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
