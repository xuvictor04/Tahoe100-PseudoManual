---
symbol: "RALGPS2"
type: "gene"
col: 3772
ensembl_id: "ENSG00000116191"
name: "Ral GEF with PH domain and SH3 binding motif 2"
location: "1q25.2"
module: 1
arm: "-"
pooled_cpm: 169.23
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 35
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 7
direction_downstream: 17
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# RALGPS2

*Ral GEF with PH domain and SH3 binding motif 2* — 1q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +5.5, q 3e-05, up in 20 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.440× (z -24.4, q 0e+00, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAPGEF2]] (+0.60, fdr 2e-05), [[PIP4K2A]] (+0.58, fdr 4e-05), [[MBOAT2]] (+0.55, fdr 1e-05); moves opposite to [[QTRT1]] (-0.56, fdr 3e-05), [[DUS3L]] (-0.53, fdr 4e-05), [[UTP15]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[KCNK1]] → it (grade B ⚠); 17 go from it, the strongest it → [[AFG1L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3772.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +5.5 | 3e-05 | 20/41 (NCI-H460, J82, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +5.1 | 5e-05 | 23/40 (CFPAC-1, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.28×** | +5.1 | 5e-05 | 24/41 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.26×** | +4.8 | 2e-04 | 22/41 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.6 | 5e-04 | 19/42 (CFPAC-1, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.22×** | +4.2 | 0.003 | 20/40 (CFPAC-1, C32, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.8 | 0.011 | 18/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.7 | 0.014 | 17/42 (NCI-H460, HS-578T, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.052 | 20/41 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.058 | 14/40 (C32, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3772.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.440×** | -24.4 | 0e+00 | 38/42 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -18.0 | 0e+00 | 35/41 (SW48, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.524×** | -13.6 | 1e-39 | 33/41 (Panc 03.27, A549, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.540×** | -12.9 | 4e-36 | 33/41 (A549, AsPC-1, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.554×** | -11.9 | 1e-30 | 38/41 (SW 900, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.575×** | -11.2 | 5e-27 | 35/41 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -10.9 | 1e-25 | 36/41 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.597×** | -10.4 | 2e-23 | 36/43 (SW 900, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -10.4 | 2e-23 | 27/41 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -9.9 | 4e-21 | 34/42 (HEC-1-A, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.666×** | -8.5 | 8e-16 | 26/41 (SW480, A549, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.470×** | -8.3 | 5e-15 | 38/41 (AsPC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.680×** | -7.8 | 3e-13 | 32/40 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -7.7 | 6e-13 | 31/41 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.680×** | -7.5 | 3e-12 | 28/38 (Panc 03.27, CFPAC-1, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -6.7 | 8e-10 | 28/41 (A-172, A-427, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.558×** | -6.4 | 5e-09 | 31/41 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.576×** | -6.0 | 4e-08 | 34/41 (A498, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.745×** | -5.9 | 8e-08 | 27/41 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.585×** | -5.9 | 1e-07 | 31/41 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.768×** | -5.5 | 7e-07 | 25/41 (A498, J82, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.613×** | -5.4 | 2e-06 | 35/41 (A498, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.857× | -4.6 | 1e-04 | 16/41 (A498, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3772. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 191 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -22.4) |
| [[KATO III (line)]] | alt | 158 | 3 (2 ⚠) | 9 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.03× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 259 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -17.7) |
| [[RKO (line)]] | wt | 149 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -18.9) |
| [[LS 180 (line)]] | wt | 330 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -18.9) |
| [[SW48 (line)]] | wt | 413 | 2 (1 ⚠) | 8 (4 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 3.15× (z +10.3) ⚠ cell-cycle shift, explains ~89% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.80× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -21.6) |
| [[A-172 (line)]] | wt | 155 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -19.7) |
| [[AsPC-1 (line)]] | alt | 864 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 102 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -16.0) |
| [[SW 900 (line)]] | alt | 224 | 0 | 9 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -19.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 241 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -14.8) |
| [[HT-29 (line)]] | alt | 241 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -22.5) |
| [[C32 (line)]] | wt | 86.8 | 5 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.72× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -12.8) |
| [[SW480 (line)]] | alt | 105 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -15.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -11.0) |
| [[A549 (line)]] | wt | 174 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -22.6) |
| [[COLO 205 (line)]] | alt | 256 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.199× (z -16.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -13.4) |
| [[LoVo (line)]] | wt | 201 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -17.0) |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -18.3) |
| [[NCI-H2347 (line)]] | alt | 531 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -19.4) |
| [[NCI-H1573 (line)]] | alt | 170 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -16.7) |
| [[HOP62 (line)]] | alt | 127 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -15.3) |
| [[NCI-H460 (line)]] | wt | 51.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.93× (z +16.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.445× (z -8.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 176 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -18.2) |
| [[HCT15 (line)]] | alt | 213 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.1) |
| [[HS-578T (line)]] | alt | 90.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 192 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.8) |
| [[SNU-423 (line)]] | alt | 104 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -11.0) |
| [[SW1417 (line)]] | alt | 222 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -18.0) |
| [[Hs 766T (line)]] | wt | 78.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -11.6) |
| [[J82 (line)]] | alt | 113 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -15.3) |
| [[C-33 A (line)]] | alt | 178 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 85.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[AN3 CA (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3772), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF2]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[PIP4K2A]] | +0.58 | +0.71 / +0.41 | both halves | 4e-05 |  |
| [[MBOAT2]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PIK3CB]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[PRKCI]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ABHD3]] | +0.54 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[LPCAT2]] | +0.54 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CBL]] | +0.53 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[RAB11FIP1]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TTC9]] | +0.52 | +0.60 / +0.39 | both halves | 6e-05 |  |
| [[PDE5A]] | +0.52 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[RHOF]] | +0.52 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QTRT1]] | -0.56 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[DUS3L]] | -0.53 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[UTP15]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[PPAN]] | -0.52 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[C8orf33]] | -0.51 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[STK11IP]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[LINS1]] | -0.49 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[FIZ1]] | -0.49 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[NAT10]] | -0.49 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[TMEM128]] | -0.48 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[ERMARD]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[RRN3]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK1]] | B | KCNK1 activity raises RALGPS2's level | lines that do not express KCNK1 (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without KCNK1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132 |
| [[GALNT3]] | B | GALNT3 activity raises RALGPS2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 2.53× lower at baseline in the lines without GALNT3 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[MYO5B]] | B | MYO5B activity raises RALGPS2's level | lines that do not express MYO5B (26) vs lines expressing it (24) | 2.39× lower at baseline in the lines without MYO5B | 0.026 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[PROSER2]] | B | PROSER2 activity raises RALGPS2's level | lines that do not express PROSER2 (14) vs lines expressing it (36) | 2.15× lower at baseline in the lines without PROSER2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BIK, EPS8L2, SERPINB9P1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises RALGPS2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNK1]] | B | KCNK1 activity strengthens RALGPS2's drug response | lines that do not express KCNK1 (16) vs lines expressing it (27) | the lines without KCNK1 respond 0.72× as strongly (z diff +1.97); strongest at Panobinostat 5 µM: 0.75x vs 0.46x (z diff +4.2) | 0.081 | ⚠ within organs, on part of the lines; also absent: LAMB3, P2RY2, C6orf132; target measured in part of the lines; artifact flags |
| [[PLEKHA5]] | C | PLEKHA5 activity raises RALGPS2's level | lines that do not express PLEKHA5 (4) vs lines expressing it (46) | 3.93× lower at baseline in the lines without PLEKHA5 | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: SVIP, LRRCC1, USP53 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AFG1L]] | B | RALGPS2 activity lowers AFG1L's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 2.15× higher at baseline in the lines without RALGPS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[DUS3L]] | B | RALGPS2 activity lowers DUS3L's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.54× higher at baseline in the lines without RALGPS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[RRN3]] | B | RALGPS2 activity lowers RRN3's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.42× higher at baseline in the lines without RALGPS2 | 0.033 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[KCNK1]] | B | RALGPS2 activity raises KCNK1's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 5.69× lower at baseline in the lines without RALGPS2 | 0.035 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[UTP15]] | B | RALGPS2 activity lowers UTP15's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.72× higher at baseline in the lines without RALGPS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[LBH]] | B | RALGPS2 activity raises LBH's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 3.11× lower at baseline in the lines without RALGPS2 | 0.066 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[OSBPL3]] | B | RALGPS2 activity raises OSBPL3's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without RALGPS2 | 0.069 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[ZNF689]] | B | RALGPS2 activity lowers ZNF689's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.48× higher at baseline in the lines without RALGPS2 | 0.070 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[PPAN]] | B | RALGPS2 activity lowers PPAN's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.59× higher at baseline in the lines without RALGPS2 | 0.070 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[TSPAN33]] | B | RALGPS2 activity lowers TSPAN33's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.99× higher at baseline in the lines without RALGPS2 | 0.078 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[C19orf54]] | B | RALGPS2 activity lowers C19orf54's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.29× higher at baseline in the lines without RALGPS2 | 0.079 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[QTRT1]] | B | RALGPS2 activity lowers QTRT1's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 1.36× higher at baseline in the lines without RALGPS2 | 0.082 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.390). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.8, 5.9); signed map (-17.8, 28.8). **Vector** length 117, 37.5% of its response variance represented; |z| ≥ 3 in 1,616 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | +0.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +7.1 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.4 | +4.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.5 | +4.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.4 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -10.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.1 | -8.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -6.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.5 | -5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.4 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.2 | -6.0 |

## What is on record

|  |  |
|---|---|
| Name | Ral GEF with PH domain and SH3 binding motif 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.2 — chr1:178,725,165-178,921,842 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0351, FLJ10244, FLJ25604 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Ral GEF with PH domain and SH3 binding motif family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86X27](https://www.uniprot.org/uniprotkb/Q86X27) (Ras-specific guanine nucleotide-releasing factor RalGPS2):

> Guanine nucleotide exchange factor for the small GTPase RALA. May be involved in cytoskeletal organization. May also be involved in the stimulation of transcription in a Ras-independent fashion (By similarity).

**Summary**, from NCBI Gene [55103](https://www.ncbi.nlm.nih.gov/gene/55103):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in regulation of Ral protein signal transduction. Predicted to be located in cytoplasm. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30279](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30279) · Entrez [55103](https://www.ncbi.nlm.nih.gov/gene/55103) · UniProt [Q86X27](https://www.uniprot.org/uniprotkb/Q86X27) · Ensembl [ENSG00000116191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116191)

## Data

Gene col 3772: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3772); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3772, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3772]; `tensor/DDL_lfc|DDL_z.npy` [3772]; `embed/gene_vectors.npy` [3772]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3772 or target_col == 3772). Every well: [[RALGPS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALGPS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
