---
symbol: "NDUFA10"
type: "gene"
col: 5064
ensembl_id: "ENSG00000130414"
name: "NADH:ubiquinone oxidoreductase subunit A10"
location: "2q37.3"
module: 20
arm: "+"
pooled_cpm: 100.43
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# NDUFA10

*NADH:ubiquinone oxidoreductase subunit A10* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.66× (z +15.4, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.53× (z +14.8, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.781× (z -10.7, q 7e-24, down in 37 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.439×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MFN2]] (+0.73, fdr 7e-06), [[CHID1]] (+0.68, fdr 7e-06), [[FUBP3]] (+0.67, fdr 7e-06); moves opposite to [[PIM3]] (-0.62, fdr 1e-05), [[BTG1]] (-0.61, fdr 2e-05), [[H3-3B]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +15.4 | 0e+00 | 44/49 (MIA PaCa-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.53×** | +14.8 | 0e+00 | 45/49 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +12.6 | 4e-34 | 35/45 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +12.0 | 4e-31 | 43/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.44×** | +10.7 | 1e-24 | 33/44 (MIA PaCa-2, A-427, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +10.6 | 3e-24 | 40/48 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +9.0 | 2e-17 | 31/48 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +8.0 | 1e-13 | 35/48 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +7.0 | 2e-10 | 29/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +6.9 | 3e-10 | 28/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +6.7 | 1e-09 | 29/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.49×** | +6.4 | 1e-08 | 29/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +6.3 | 1e-08 | 29/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +6.2 | 2e-08 | 17/49 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.2 | 2e-08 | 22/38 (A-172, NCI-H1792, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +5.9 | 1e-07 | 26/48 (SW 900, HCT15, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.34×** | +4.7 | 9e-05 | 21/48 (NCI-H460, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.31×** | +4.4 | 3e-04 | 20/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 3e-04 | 18/49 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +4.2 | 7e-04 | 19/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | 1.12× | +3.5 | 0.009 | 5/48 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.010 | 10/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.015 | 13/48 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.023 | 6/48 (RKO, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5064.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.439×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.781×** | -10.7 | 7e-24 | 37/48 (HOP62, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.756×** | -8.6 | 3e-15 | 34/49 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.889× | -5.1 | 6e-05 | 14/48 (RKO, SW480, …) | rises with dose | low cells (technical?) |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.895× | -3.4 | 0.089 | 6/49 (NCI-H2030, Panc 03.27, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.3 | 0.12 | 18/48 (A-427, Panc 03.27, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.19 | 12/48 (SW 1271, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 103 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.76× (z +10.8) | — |
| [[SW480 (line)]] | alt | 110 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +12.6) | — |
| [[LoVo (line)]] | wt | 97.8 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.51× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.22× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 116 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 112 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.96× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.94× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 111 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 129 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.80× (z +9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 142 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.91× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 72.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +9.1) | — |
| [[A549 (line)]] | wt | 102 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.37× (z +8.8) | — |
| [[KATO III (line)]] | alt | 85.1 | 3 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.32× (z +9.0) | — |
| [[A-427 (line)]] | wt | 104 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.41× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 98.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.06× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 73.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 94.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.08× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 84.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 2.87× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 79.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 77.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.82× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.39× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 91.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 97.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 96.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 142 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 123 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFN2]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[CHID1]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[FUBP3]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[LY6G5B]] | +0.66 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SPTLC1]] | +0.63 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[EMC1]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[GCN1]] | +0.63 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[EIF3F]] | +0.63 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[DNAAF5]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[FAM120A]] | +0.61 | +0.42 / +0.68 | both halves | 4e-05 |  |
| [[ANAPC2]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIM3]] | -0.62 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[BTG1]] | -0.61 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[H3-3B]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[USP53]] | -0.57 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[FOXA2]] | -0.57 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[COMMD3]] | -0.56 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[LINC01273]] | -0.56 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[TCAF1]] | -0.56 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ARL4D]] | -0.55 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[SMIM29]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[RAB9A]] | -0.53 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[PNRC1]] | -0.53 | -0.34 / -0.60 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.596). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-19.4, -28.1); signed map (-24.2, -44.8). **Vector** length 106, 27.5% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +10.8 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +15.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +12.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.5 | +10.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +14.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +9.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.8 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.4 | -8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit A10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:239,892,450-240,025,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CI-42k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits; Flavoproteins |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95299](https://www.uniprot.org/uniprotkb/O95299) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4705](https://www.ncbi.nlm.nih.gov/gene/4705):

> The protein encoded by this gene is a component of 42 kDa complex I, the first enzyme complex in the electron transport chain of mitochondria. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. A mutation in this gene was found in an individual with Leigh syndrome. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:7684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7684) · Entrez [4705](https://www.ncbi.nlm.nih.gov/gene/4705) · UniProt [O95299](https://www.uniprot.org/uniprotkb/O95299) · Ensembl [ENSG00000130414](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130414)

## Data

Gene col 5064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5064); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5064]; `tensor/DDL_lfc|DDL_z.npy` [5064]; `embed/gene_vectors.npy` [5064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5064 or target_col == 5064). Every well: [[NDUFA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
