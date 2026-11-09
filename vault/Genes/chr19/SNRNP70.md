---
symbol: "SNRNP70"
type: "gene"
col: 2505
ensembl_id: "ENSG00000104852"
name: "small nuclear ribonucleoprotein U1 subunit 70"
location: "19q13.33"
module: 33
arm: "+"
pooled_cpm: 96.82
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# SNRNP70

*small nuclear ribonucleoprotein U1 subunit 70* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (15 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.31× (z +12.4, q 1e-32, up in 47 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.170×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.447×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.521×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PELP1]] (+0.63, fdr 1e-05), [[SRRT]] (+0.63, fdr 1e-05), [[ZNF787]] (+0.63, fdr 1e-05); moves opposite to [[RO60]] (-0.56, fdr 2e-05), [[LSMEM1]] (-0.49, fdr 2e-04), [[MIB1]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 20 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.31×** | +12.4 | 1e-32 | 47/49 (SW480, SW1417, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +12.1 | 2e-31 | 45/48 (NCI-H1792, RKO, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.07×** | +11.6 | 5e-29 | 39/48 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.58×** | +10.2 | 2e-22 | 39/48 (NCI-H1792, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.31×** | +8.4 | 3e-15 | 31/48 (A549, NCI-H1792, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.43×** | +8.0 | 9e-14 | 39/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +8.0 | 9e-14 | 36/47 (LOX-IMVI, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **1.38×** | +7.2 | 4e-11 | 33/49 (RKO, NCI-H23, …) | all doses, flat | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.37×** | +6.8 | 5e-10 | 28/47 (LoVo, COLO 205, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.38×** | +6.7 | 1e-09 | 29/45 (NCI-H1573, NCI-H23, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.34×** | +6.6 | 2e-09 | 38/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +6.4 | 8e-09 | 29/38 (SW480, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.34×** | +6.3 | 2e-08 | 28/44 (A498, HT-29, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.32×** | +6.2 | 3e-08 | 34/48 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.32×** | +6.0 | 7e-08 | 33/48 (A549, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +5.9 | 1e-07 | 34/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +5.3 | 3e-06 | 32/48 (SNU-1, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 8e-05 | 26/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.1 | 0.001 | 23/47 (SW48, SW1417, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.31×** | +4.0 | 0.001 | 19/48 (NCI-H460, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.003 | 23/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.005 | 18/49 (NCI-H460, A549, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.020 | 18/49 (SNU-423, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.022 | 20/48 (MIA PaCa-2, AN3 CA, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.030 | 11/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.068 | 15/47 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2505.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.170×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.447×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (H4 0.521×; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (SW 1271 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.868× | -3.2 | 0.78 | 11/48 (HT-29, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 84.9 | 5 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.11× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 62.4 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +14.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.88× (z +10.2) | — |
| [[LoVo (line)]] | wt | 92.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.6) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.05× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 144 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.86× (z +9.2) | — |
| [[HT-29 (line)]] | alt | 114 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +12.5) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.80× (z +8.8) | — |
| [[RKO (line)]] | wt | 122 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.16× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.15× (z +8.5) | — |
| [[A549 (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.6) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[HEC-1-A (line)]] | alt | 168 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.98× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 76.2 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 5.56× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 67.1 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.36× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | — |
| [[SW480 (line)]] | alt | 114 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.89× (z +10.0) | — |
| [[A498 (line)]] | wt | 98.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.17× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[C-33 A (line)]] | alt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[H4 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.10× (z +8.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | — |
| [[PANC-1 (line)]] | alt | 75.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.61× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 93.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW 1271 (line)]] | alt | 68.2 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[SW48 (line)]] | wt | 104 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.03× (z +10.7) | — |
| [[A-172 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 221 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 83.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PELP1]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SRRT]] | +0.63 | +0.77 / +0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 627 |
| [[ZNF787]] | +0.63 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CLASRP]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 | STRING 480 |
| [[BTBD2]] | +0.61 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[DDX55]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SMIM8]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SCAP]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[ZGPAT]] | +0.56 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[NUP160]] | +0.55 | +0.36 / +0.48 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[THRAP3]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 | STRING 555 |
| [[LRFN3]] | +0.55 | +0.40 / +0.43 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RO60]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 | STRING 837 |
| [[LSMEM1]] | -0.49 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[MIB1]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.47 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[METTL21A]] | -0.46 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[C14orf28]] | -0.46 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[SDCBP]] | -0.46 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-32.7, -5.8); signed map (-15.1, -26.5). **Vector** length 79.6, 19.2% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +12.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +11.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.6 | +5.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.2 | +10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +12.1 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.7 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +4.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.6 | +1.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.7 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -2.9 | +2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.3 | -2.1 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.7 | -2.6 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U1 subunit 70 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,085,419-49,108,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U1-70K, Snp1; previously RNPU1Z, RPU1, SNRP70 |
| Gene groups (HGNC) | RNA binding motif containing; U1 small nuclear ribonucleoprotein |
| Reactome | 6 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P08621](https://www.uniprot.org/uniprotkb/P08621) (U1 small nuclear ribonucleoprotein 70 kDa):

> Component of the spliceosomal U1 snRNP, which is essential for recognition of the pre-mRNA 5' splice-site and the subsequent assembly of the spliceosome. SNRNP70 binds to the loop I region of U1-snRNA.; [Isoform 3]: Truncated isoforms that lack the RRM domain cannot bind U1-snRNA.; [Isoform 4]: Truncated isoforms that lack the RRM domain cannot bind U1-snRNA.

**Summary**, from NCBI Gene [6625](https://www.ncbi.nlm.nih.gov/gene/6625):

> Enables U1 snRNA binding activity. Involved in several processes, including negative regulation of chaperone-mediated autophagy; negative regulation of protein refolding; and regulation of RNA splicing. Located in lysosomal lumen and nucleoplasm. Part of U1 snRNP and spliceosomal complex. Implicated in disease of mental health and systemic lupus erythematosus. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11150) · Entrez [6625](https://www.ncbi.nlm.nih.gov/gene/6625) · UniProt [P08621](https://www.uniprot.org/uniprotkb/P08621) · Ensembl [ENSG00000104852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104852)

## Data

Gene col 2505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2505); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2505]; `tensor/DDL_lfc|DDL_z.npy` [2505]; `embed/gene_vectors.npy` [2505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2505 or target_col == 2505). Every well: [[SNRNP70 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP70.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
