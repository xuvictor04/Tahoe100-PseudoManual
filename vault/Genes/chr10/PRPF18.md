---
symbol: "PRPF18"
type: "gene"
col: 9152
ensembl_id: "ENSG00000165630"
name: "pre-mRNA processing factor 18"
location: "10p13"
module: 118
arm: "+"
pooled_cpm: 74.93
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# PRPF18

*pre-mRNA processing factor 18* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.24× (z +25.4, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.775× (z -5.7, q 7e-06, down in 26 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.847× (z -5.3, q 3e-05, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.0835×, NCI-H1573 0.414×, CFPAC-1 0.487×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.147×, NCI-H2030 0.402×, RPMI-7951 0.463×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.382×, SNU-1 0.325×, NCI-H2030 0.498×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM48]] (+0.64, fdr 1e-05), [[GALK2]] (+0.63, fdr 6e-05), [[SYNRG]] (+0.62, fdr 3e-05); moves opposite to [[GPR63]] (-0.60, fdr 2e-04), [[DGAT2]] (-0.60, fdr 2e-04), [[GNPNAT1]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.24×** | +25.4 | 0e+00 | 46/49 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +19.4 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.11×** | +16.7 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +16.2 | 0e+00 | 42/48 (NCI-H2030, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +15.9 | 0e+00 | 42/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.03×** | +14.6 | 0e+00 | 46/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +12.9 | 5e-36 | 46/48 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.89×** | +11.1 | 7e-27 | 41/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.8 | 2e-25 | 41/50 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +9.1 | 5e-18 | 31/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +8.5 | 6e-16 | 35/48 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +7.5 | 4e-12 | 34/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +5.2 | 9e-06 | 29/48 (A-172, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.17× | +5.0 | 3e-05 | 18/48 (Panc 03.27, SW1417, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +4.9 | 3e-05 | 25/48 (A549, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +4.8 | 5e-05 | 27/48 (LOX-IMVI, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.51×** | +4.3 | 5e-04 | 23/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 6e-04 | 22/48 (HOP62, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9152.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SNU-1 0.0835×, NCI-H1573 0.414×, CFPAC-1 0.487×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-1 0.147×, NCI-H2030 0.402×, RPMI-7951 0.463×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A-427 0.382×, SNU-1 0.325×, NCI-H2030 0.498×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.775×** | -5.7 | 7e-06 | 26/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -5.6 | 8e-06 | 28/47 (SNU-423, COLO 205, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -5.3 | 3e-05 | 18/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.797×** | -5.1 | 5e-05 | 24/49 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.800×** | -4.8 | 2e-04 | 21/44 (SNU-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.824×** | -4.3 | 0.001 | 23/48 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -4.2 | 0.002 | 2/50 (SW 1271, SW 1088) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.825×** | -4.1 | 0.003 | 26/49 (CFPAC-1, A498, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.706×** | -3.7 | 0.016 | 22/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.745× | -3.1 | 0.11 | 11/48 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 90.0 | 10 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +17.6) | — |
| [[HEC-1-A (line)]] | alt | 56.4 | 9 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +24.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 72.5 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +19.4) | — |
| [[J82 (line)]] | alt | 69.0 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +15.8) | — |
| [[NCI-H2030 (line)]] | alt | 112 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.402× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 53.3 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +17.2) | — |
| [[RKO (line)]] | wt | 113 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +19.2) | — |
| [[SK-MEL-2 (line)]] | alt | 79.6 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 102 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.09× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0835× (z -23.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 55.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 55.7 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 90.0 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +13.8) | — |
| [[NCI-H460 (line)]] | wt | 74.1 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +17.3) | — |
| [[A-172 (line)]] | wt | 58.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +18.2) | — |
| [[A549 (line)]] | wt | 76.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +13.4) | — |
| [[HS-578T (line)]] | alt | 60.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +14.0) | — |
| [[LoVo (line)]] | wt | 70.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +16.1) | — |
| [[LOX-IMVI (line)]] | wt | 70.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.7) | — |
| [[A-427 (line)]] | wt | 65.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 79.7 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 57.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.34× (z +11.7) | — |
| [[CFPAC-1 (line)]] | alt | 95.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 113 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 116 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 61.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 69.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 64.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 56.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 139 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -10.8) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 74.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +19.0) | — |
| [[SNU-423 (line)]] | alt | 58.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 101 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +11.7) | — |
| [[C32 (line)]] | wt | 45.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 67.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.0) | — |
| [[Hs 766T (line)]] | wt | 53.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 75.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +14.8) | — |
| [[H4 (line)]] | wt | 52.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +11.0) | — |
| [[HCT15 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 94.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.43× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 85.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.9) | — |
| [[KATO III (line)]] | alt | 84.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM48]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[GALK2]] | +0.63 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[SYNRG]] | +0.62 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[ING4]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[EFCAB6]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[RABL2A]] | +0.62 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CSNK2B]] | +0.61 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[SERINC1]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TMCO1]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[ISY1]] | +0.60 | +0.60 / +0.53 | both halves | 1e-05 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 785 |
| [[ZNF394]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ATP6V1E1]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR63]] | -0.60 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[DGAT2]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[GNPNAT1]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[LRRC8B]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[CEP85]] | -0.54 | -0.58 / -0.40 | both halves | 4e-05 |  |
| [[DNMT3B]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[JPH1]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[SSX2IP]] | -0.53 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[CDC7]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[POLR3G]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[CLN6]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SLC29A1]] | -0.51 | -0.54 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRPF18's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-20.3, 31.0); signed map (-3.3, -3.6). **Vector** length 88.2, 24.1% of its response variance represented; |z| ≥ 3 in 1,181 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.6 | +14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +25.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.1 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -6.8 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | +2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | pre-mRNA processing factor 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:13,586,939-13,668,445 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hPrp18 |
| Gene groups (HGNC) | Spliceosomal C complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99633](https://www.uniprot.org/uniprotkb/Q99633) (Pre-mRNA-splicing factor 18):

> Participates in the second step of pre-mRNA splicing.

**Summary**, from NCBI Gene [8559](https://www.ncbi.nlm.nih.gov/gene/8559):

> Pre-mRNA splicing occurs in 2 sequential transesterification steps. The protein encoded by this gene is found to be essential for the catalytic step II in pre-mRNA splicing process. It is found in the spliceosome, and contains seven WD repeats, which function in protein-protein interactions. This protein has a sequence similarity to the yeast splicing factor Prp18. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17351) · Entrez [8559](https://www.ncbi.nlm.nih.gov/gene/8559) · UniProt [Q99633](https://www.uniprot.org/uniprotkb/Q99633) · Ensembl [ENSG00000165630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165630)

## Data

Gene col 9152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9152); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9152]; `tensor/DDL_lfc|DDL_z.npy` [9152]; `embed/gene_vectors.npy` [9152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9152 or target_col == 9152). Every well: [[PRPF18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPF18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
