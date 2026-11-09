---
symbol: "MFGE8"
type: "gene"
col: 6429
ensembl_id: "ENSG00000140545"
name: "milk fat globule EGF and factor V/VIII domain containing"
location: "15q26.1"
module: 97
arm: "+"
pooled_cpm: 44.94
n_lines_expressing: 43
n_dd_up: 39
n_dd_down: 5
n_dd_up_clean: 25
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# MFGE8

*milk fat globule EGF and factor V/VIII domain containing* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.14× (z +15.5, q 0e+00, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.585× (z -7.3, q 1e-10, down in 35 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.532× (z -4.5, q 0.002, down in 19 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HAPLN3]] (+0.68, fdr 1e-05, ⚠ same locus), [[CRLF1]] (+0.57, fdr 5e-05), [[NCOA3]] (+0.55, fdr 1e-05), [[ATP1A1]] (+0.54, fdr 1e-05); moves opposite to [[PNO1]] (-0.47, fdr 8e-05), [[ICE2]] (-0.46, fdr 1e-04), [[MAGOHB]] (-0.45, fdr 2e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[RECK]] → it (grade B ⚠); 8 go from it, the strongest it → [[CD81]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.14×** | +15.5 | 0e+00 | 37/41 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +14.5 | 6e-45 | 36/40 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.71×** | +13.5 | 2e-39 | 36/41 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +13.0 | 2e-36 | 38/41 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.37×** | +11.3 | 2e-27 | 28/32 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.27×** | +11.1 | 9e-27 | 38/41 (LoVo, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.11×** | +10.1 | 4e-22 | 31/36 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +8.3 | 7e-15 | 30/40 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.87×** | +8.2 | 2e-14 | 29/41 (HEC-1-A, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +8.1 | 3e-14 | 33/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +7.2 | 3e-11 | 27/37 (H4, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.69×** | +7.1 | 5e-11 | 28/40 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.73×** | +6.9 | 3e-10 | 20/32 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.65×** | +6.6 | 2e-09 | 31/41 (A498, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 8e-07 | 26/41 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.8 | 6e-05 | 20/41 (HT-29, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.39×** | +4.5 | 2e-04 | 20/41 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +3.9 | 0.003 | 16/41 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +3.9 | 0.003 | 20/40 (C-33 A, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.004 | 17/41 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.007 | 19/41 (A498, RPMI-7951, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.011 | 19/41 (A498, A549, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.011 | 18/40 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.011 | 18/41 (A498, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.585×** | -7.3 | 1e-10 | 35/41 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.532×** | -4.5 | 0.002 | 19/40 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -4.2 | 0.005 | 20/41 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.019 | 16/41 (C32, HS-578T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.028 | 15/39 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | 0.657× | -3.0 | 0.22 | 13/40 (SW480, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 22.6 | 8 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.56× (z +11.5) | — |
| [[A498 (line)]] | wt | 35.3 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +11.8) | — |
| [[SW480 (line)]] | alt | 20.6 | 6 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.84× (z +14.0) | — |
| [[HOP62 (line)]] | alt | 94.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.4) | — |
| [[LoVo (line)]] | wt | 15.1 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 7.05× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 44.5 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 2.56× (z +12.5) | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 25.8 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.05× (z +10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.64× (z +10.1) | — |
| [[C32 (line)]] | wt | 192 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.4) | — |
| [[KATO III (line)]] | alt | 16.8 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.45× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 222 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[RKO (line)]] | wt | 12.2 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.03× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 59.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 33.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 34.3 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.24× (z +8.9) | — |
| [[J82 (line)]] | alt | 13.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 35.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[A-172 (line)]] | wt | 74.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +11.9) | — |
| [[A549 (line)]] | wt | 29.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +20.6) | — |
| [[C-33 A (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.89× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[HS-578T (line)]] | alt | 52.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.15× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +11.6) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[SNU-1 (line)]] | wt | 27.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.54× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 34.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.13× (z +9.1) | — |
| [[SW48 (line)]] | wt | 15.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.17× (z +8.9) | — |
| [[A-427 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 94.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAPLN3]] | +0.68 | +0.54 / +0.78 | both halves | 1e-05 | STRING 526; ⚠ same locus (3.1 kb, same strand: neighbours can correlate without regulation) |
| [[CRLF1]] | +0.57 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[NCOA3]] | +0.55 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ATP1A1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ITGA5]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 | STRING 503 |
| [[TIMP2]] | +0.53 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[PTPN1]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[KCNB1]] | +0.53 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[AKAP13]] | +0.52 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[FOXO1]] | +0.52 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[TMSB10]] | +0.52 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[CPM]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[INSR]] | +0.52 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNO1]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ICE2]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[MAGOHB]] | -0.45 | -0.30 / -0.50 | both halves | 2e-04 |  |
| [[FBXW8]] | -0.43 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ZNG1F]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RECK]] | B | RECK activity raises MFGE8's level | lines that do not express RECK (12) vs lines expressing it (38) | 2.49× lower at baseline in the lines without RECK | 0.045 | ⚠ within organs, on part of the lines; also absent: OSBPL6, DZIP1L, STARD9 |
| [[TSC22D3]] | B | TSC22D3 activity raises MFGE8's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 2.33× lower at baseline in the lines without TSC22D3 | 0.074 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[HAPLN3]] | C | HAPLN3 activity raises MFGE8's level | lines that do not express HAPLN3 (7) vs lines expressing it (43) | 3.67× lower at baseline in the lines without HAPLN3 | 0.009 | ⚠ within organs, on part of the lines; also absent: GLIPR2, MFGE8, GLI2; maybe low, not absent; co-absent with the target |
| [[TIMP2]] | C | TIMP2 activity raises MFGE8's level | lines that do not express TIMP2 (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without TIMP2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CNTNAP1, P3H1, RDX; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD81]] | B | MFGE8 activity raises CD81's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.05× lower at baseline in the lines without MFGE8 | 0.022 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[SERINC1]] | B | MFGE8 activity raises SERINC1's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without MFGE8 | 0.023 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[TOX2]] | B | MFGE8 activity raises TOX2's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without MFGE8 | 0.049 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[MAOA]] | B | MFGE8 activity lowers MAOA's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.69× higher at baseline in the lines without MFGE8 | 0.059 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[FKBP1B]] | B | MFGE8 activity raises FKBP1B's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without MFGE8 | 0.081 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[HIP1]] | B | MFGE8 activity raises HIP1's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without MFGE8 | 0.090 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[IRS2]] | B | MFGE8 activity lowers IRS2's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.12× higher at baseline in the lines without MFGE8 | 0.090 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |
| [[HAPLN3]] | C | MFGE8 activity raises HAPLN3's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 3.19× lower at baseline in the lines without MFGE8 | 0.003 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B; co-absent with the target |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.7, 12.3); signed map (13.7, 34.3). **Vector** length 102, 26.7% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.3 | +8.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | +3.8 | +7.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.6 | +3.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.6 | +3.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +3.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.9 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.9 | -3.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.7 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | milk fat globule EGF and factor V/VIII domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:88,898,683-88,913,468 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SED1, EDIL1, BA46, OAcGD3S, HsT19888, MFG-E8, hP47; previously SPAG10 |
| Reactome | 3 pathways, smallest: Amyloid fiber formation; Post-translational protein phosphorylation; Regulation of Insulin-like Growth Factor (IGF) transport and uptake by Insulin-like Growth Factor Binding Proteins (IGFBPs) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08431](https://www.uniprot.org/uniprotkb/Q08431) (Lactadherin):

> Plays an important role in the maintenance of intestinal epithelial homeostasis and the promotion of mucosal healing. Promotes VEGF-dependent neovascularization (By similarity). Contributes to phagocytic removal of apoptotic cells in many tissues. Specific ligand for the alpha-v/beta-3 and alpha-v/beta-5 receptors. Also binds to phosphatidylserine-enriched cell surfaces in a receptor-independent manner. Zona pellucida-binding protein which may play a role in gamete interaction.; [Medin]: Main …

**Summary**, from NCBI Gene [4240](https://www.ncbi.nlm.nih.gov/gene/4240):

> This gene encodes a preproprotein that is proteolytically processed to form multiple protein products. The major encoded protein product, lactadherin, is a membrane glycoprotein that promotes phagocytosis of apoptotic cells. This protein has also been implicated in wound healing, autoimmune disease, and cancer. Lactadherin can be further processed to form a smaller cleavage product, medin, which comprises the major protein component of aortic medial amyloid (AMA). Alternative splicing results …

**Accessions** — [HGNC:7036](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7036) · Entrez [4240](https://www.ncbi.nlm.nih.gov/gene/4240) · UniProt [Q08431](https://www.uniprot.org/uniprotkb/Q08431) · Ensembl [ENSG00000140545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140545)

## Data

Gene col 6429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6429); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6429]; `tensor/DDL_lfc|DDL_z.npy` [6429]; `embed/gene_vectors.npy` [6429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6429 or target_col == 6429). Every well: [[MFGE8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFGE8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
