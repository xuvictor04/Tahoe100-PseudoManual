---
symbol: "ESF1"
type: "gene"
col: 1562
ensembl_id: "ENSG00000089048"
name: "ESF1 nucleolar pre-rRNA processing protein"
location: "20p12.1"
module: 11
arm: "+"
pooled_cpm: 131.47
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# ESF1

*ESF1 nucleolar pre-rRNA processing protein* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.15× (z +24.9, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.418×, SHP-77 0.416×, A-172 0.390×, SNU-1 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (AN3 CA 0.197×, PANC-1 0.500×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.482×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPZ]] (+0.84, fdr 7e-06), [[ZNF146]] (+0.80, fdr 7e-06), [[NIFK]] (+0.79, fdr 7e-06); moves opposite to [[HIPK1]] (-0.69, fdr 7e-06), [[TMEM30A]] (-0.66, fdr 7e-06), [[LAPTM4A]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[APLP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.15×** | +24.9 | 0e+00 | 48/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.53×** | +20.1 | 0e+00 | 48/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.65×** | +15.0 | 0e+00 | 48/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.92×** | +10.4 | 3e-23 | 44/48 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.85×** | +9.8 | 9e-21 | 47/48 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +7.3 | 3e-11 | 41/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.09×** | +6.1 | 7e-08 | 43/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.04×** | +5.9 | 2e-07 | 36/49 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.99×** | +5.8 | 5e-07 | 43/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.92×** | +5.5 | 3e-06 | 42/48 (PANC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.40×** | +5.4 | 3e-06 | 31/48 (HS-578T, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.87×** | +5.2 | 8e-06 | 41/48 (KATO III, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +4.9 | 4e-05 | 28/48 (HS-578T, C32, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.76×** | +4.7 | 1e-04 | 37/48 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.34×** | +4.7 | 1e-04 | 29/48 (HS-578T, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.6 | 0.011 | 33/47 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.022 | 21/48 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.55×** | +3.2 | 0.038 | 26/49 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.055 | 21/48 (NCI-H1792, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (MIA PaCa-2 0.418×, SHP-77 0.416×, A-172 0.390×, SNU-1 0.397×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (AN3 CA 0.197×, PANC-1 0.500×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.482×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.861× | -3.3 | 0.32 | 11/48 (Hs 766T, PANC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.802× | -3.3 | 0.32 | 23/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 93.6 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +27.2) | — |
| [[PANC-1 (line)]] | alt | 207 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +22.5) | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 156 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +27.6) | — |
| [[A-172 (line)]] | wt | 89.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.50× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 103 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 142 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.68× (z +18.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 218 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 195 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +12.2) | — |
| [[A498 (line)]] | wt | 97.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +13.7) | — |
| [[A549 (line)]] | wt | 151 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +20.7) | — |
| [[AsPC-1 (line)]] | alt | 57.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +17.7) | — |
| [[COLO 205 (line)]] | alt | 112 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +18.5) | — |
| [[Hs 766T (line)]] | wt | 132 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +21.2) | — |
| [[hTERT-HPNE (line)]] | wt | 98.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +18.6) | — |
| [[KATO III (line)]] | alt | 185 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.7) | — |
| [[NCI-H1573 (line)]] | alt | 49.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +21.7) | — |
| [[NCI-H1792 (line)]] | alt | 53.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +18.4) | — |
| [[RKO (line)]] | wt | 271 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +14.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 160 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 111 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +19.1) | — |
| [[SNU-1 (line)]] | wt | 230 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 115 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +20.4) | — |
| [[H4 (line)]] | wt | 148 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +17.6) | — |
| [[HEC-1-A (line)]] | alt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 140 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +21.4) | — |
| [[HT-29 (line)]] | alt | 89.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +19.0) | — |
| [[J82 (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +22.6) | — |
| [[LoVo (line)]] | wt | 93.1 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.75× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 226 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +18.7) | — |
| [[SNU-423 (line)]] | alt | 181 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +24.7) | — |
| [[SW 900 (line)]] | alt | 91.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +15.4) | — |
| [[C32 (line)]] | wt | 99.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) | — |
| [[HCT15 (line)]] | alt | 135 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 88.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 47.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +21.8) | — |
| [[NCI-H23 (line)]] | alt | 140 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 95.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +11.5) | — |
| [[A-427 (line)]] | wt | 105 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 172 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 265 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | +0.84 | +0.88 / +0.80 | both halves | 7e-06 | STRING 928 |
| [[ZNF146]] | +0.80 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[NIFK]] | +0.79 | +0.77 / +0.80 | both halves | 7e-06 | STRING 868 |
| [[SURF6]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 | STRING 900 |
| [[NOL8]] | +0.76 | +0.86 / +0.71 | both halves | 7e-06 | STRING 517 |
| [[MRPS18B]] | +0.76 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[UTP14A]] | +0.74 | +0.77 / +0.69 | both halves | 7e-06 | same gene group; STRING 892 |
| [[CWC22]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.73 | +0.80 / +0.69 | both halves | 7e-06 | STRING 414 |
| [[REXO4]] | +0.73 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.72 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[PRPF38B]] | +0.72 | +0.77 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIPK1]] | -0.69 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[TMEM30A]] | -0.66 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[LAPTM4A]] | -0.65 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[TM9SF2]] | -0.65 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[ERMP1]] | -0.62 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[PRKACA]] | -0.62 | -0.40 / -0.69 | both halves | 4e-05 |  |
| [[PGRMC1]] | -0.62 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[CMPK1]] | -0.61 | -0.68 / -0.57 | both halves | 9e-06 |  |
| [[MAPK9]] | -0.61 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RPN1]] | -0.61 | -0.64 / -0.61 | both halves | 7e-06 | STRING 408 |
| [[ITM2C]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[TWSG1]] | -0.60 | -0.59 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises ESF1's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 1.15× lower at baseline in the lines without APLP1 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.749). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-40.1, 1.1); signed map (-1.4, -20.2). **Vector** length 143, 53.1% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.3 | +20.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.7 | +9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.6 | +10.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +24.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +15.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +7.3 |
|  | [[EX229 (drug)]] 5 µM |  | +6.8 | +6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.3 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.3 | +5.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.8 | +5.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.1 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.5 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -3.3 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.7 | -3.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ESF1 nucleolar pre-rRNA processing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:13,714,322-13,784,919 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA526K24.1; previously C20orf6 |
| Gene groups (HGNC) | SSU processome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H501](https://www.uniprot.org/uniprotkb/Q9H501) (ESF1 homolog):

> May constitute a novel regulatory system for basal transcription. Negatively regulates ABT1 (By similarity).

**Summary**, from NCBI Gene [51575](https://www.ncbi.nlm.nih.gov/gene/51575):

> Enables RNA binding activity. Predicted to be involved in rRNA processing. Located in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15898) · Entrez [51575](https://www.ncbi.nlm.nih.gov/gene/51575) · UniProt [Q9H501](https://www.uniprot.org/uniprotkb/Q9H501) · Ensembl [ENSG00000089048](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089048)

## Data

Gene col 1562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1562); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1562]; `tensor/DDL_lfc|DDL_z.npy` [1562]; `embed/gene_vectors.npy` [1562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1562 or target_col == 1562). Every well: [[ESF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
