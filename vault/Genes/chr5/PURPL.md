---
symbol: "PURPL"
type: "gene"
col: 14689
ensembl_id: "ENSG00000250337"
name: "p53 upregulated regulator of p53 levels"
location: "5p14.1"
module: 62
arm: "+"
pooled_cpm: 80.68
n_lines_expressing: 25
n_dd_up: 46
n_dd_down: 7
n_dd_up_clean: 34
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 16
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# PURPL

*p53 upregulated regulator of p53 levels* — 5p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +13.2, q 4e-37, up in 12 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.684× (z -5.1, q 2e-04, down in 12 of 23 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 0.707× (z -4.6, q 9e-04, down in 12 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINCR]] (+0.78, fdr 7e-06), [[PTCHD4]] (+0.77, fdr 1e-05), [[ACTA2]] (+0.75, fdr 7e-06); moves opposite to [[TRAIP]] (-0.46, fdr 7e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[PPM1D]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +13.2 | 4e-37 | 12/23 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.30×** | +11.2 | 2e-26 | 12/22 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +10.6 | 7e-24 | 19/23 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +9.3 | 3e-18 | 13/23 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +9.2 | 3e-18 | 18/23 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.5 | 1e-15 | 14/23 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.7 | 1e-12 | 12/25 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +6.8 | 9e-10 | 16/23 (NCI-H460, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.1 | 8e-08 | 15/24 (SK-MEL-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-07 | 13/23 (A549, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 4e-06 | 13/23 (LoVo, H4, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 1e-05 | 14/23 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +5.1 | 2e-05 | 1/20 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +4.7 | 9e-05 | 15/24 (NCI-H23, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.41×** | +4.6 | 1e-04 | 16/23 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 2e-04 | 16/24 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 2e-04 | 16/23 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 3e-04 | 17/23 (NCI-H23, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.684×** | -5.1 | 2e-04 | 12/23 (NCI-H23, A-427, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.707×** | -4.6 | 9e-04 | 12/23 (NCI-H23, AN3 CA, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -4.6 | 9e-04 | 17/24 (NCI-H23, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -4.3 | 0.002 | 2/24 (SK-MEL-2, A-172) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.743×** | -3.9 | 0.009 | 17/23 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.777×** | -3.4 | 0.074 | 6/23 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.785×** | -3.2 | 0.098 | 10/23 (NCI-H2030, A-427, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.786×** | -3.2 | 0.098 | 17/23 (A-427, NCI-H23, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.791× | -3.1 | 0.12 | 17/23 (A-427, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.795× | -3.0 | 0.13 | 8/23 (LoVo, A549, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.13 | 2/23 (SNU-423, SNU-1) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.9 | 12 (3 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 249 | 8 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 221 | 6 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.78× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.248× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.277× (z -9.3) |
| [[H4 (line)]] | wt | 159 | 4 | 4 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.53× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 59.7 | 6 (3 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 11.0× (z +11.9) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 9.28× (z +11.0) | [[Daptomycin (drug)]] 0.5 µM 0.146× (z -9.5) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 151 | 6 (1 ⚠) | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 5.17× (z +11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 3.10× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 144 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.4) | — |
| [[A-427 (line)]] | wt | 1,160 | 1 | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.04× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 170 | 4 (1 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.61× (z +10.6) | [[Ixazomib citrate (drug)]] 5 µM 0.214× (z -9.9) |
| [[C32 (line)]] | wt | 84.5 | 4 | 1 | [[Selinexor (drug)]] 5 µM 3.79× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.202× (z -8.6) |
| [[SNU-1 (line)]] | wt | 51.6 | 4 (2 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.32× (z +10.4) | — |
| [[A-172 (line)]] | wt | 29.5 | 3 (2 ⚠) | 0 | [[Amsacrine (drug)]] 5 µM 5.37× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 3 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.32× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 4.17× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 232 | 1 | 1 | [[Selinexor (drug)]] 5 µM 2.36× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.211× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 34.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.07× (z +11.6) ⚠ position not correctable | — |
| [[NCI-H1792 (line)]] | alt | 128 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 26.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 62.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.11 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.44 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.79 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.08 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 917 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.73 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINCR]] | +0.78 | +0.63 / +0.82 | both halves | 7e-06 | same gene group |
| [[PTCHD4]] | +0.77 | +0.55 / +0.80 | both halves | 1e-05 | **novel candidate** |
| [[ACTA2]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[ZMAT3]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.71 | +0.50 / +0.76 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.70 | +0.37 / +0.77 | both halves | 7e-05 |  |
| [[DNAI3]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.69 | +0.56 / +0.74 | both halves | 1e-05 | **novel candidate** |
| [[GAS6-AS1]] | +0.67 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[PHLDA3]] | +0.65 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[RPS27L]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[FDXR]] | +0.65 | +0.46 / +0.75 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAIP]] | -0.46 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PURPL's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.7% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens PURPL's drug response | lines that do not express PINCR (9) vs lines expressing it (16) | the lines without PINCR respond 0.07× as strongly (z diff +4.43); strongest at Idarubicin (hydrochloride) 5 µM: 0.82x vs 2.22x (z diff +7.4) | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[ACTA2]] | B | ACTA2 activity raises PURPL's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 4.29× lower at baseline in the lines without ACTA2 | 0.020 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[DSC3]] | B | DSC3 activity raises PURPL's level | lines that do not express DSC3 (31) vs lines expressing it (19) | 1.42× lower at baseline in the lines without DSC3 | 0.098 | ⚠ within organs, on part of the lines; also absent: TFF2, VGLL3, MUC16 |
| [[TP53]] | C | TP53 activity strengthens PURPL's drug response | recorded loss-of-function mutation of TP53 in 12 lines vs 13 not recorded | the TP53-altered lines respond 0.16× as strongly (z diff +4.22); strongest at Idarubicin (hydrochloride) 0.5 µM: 0.94x vs 4.00x (z diff +7.2) | 0.669 over the table, 0.042 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); artifact flags |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPM1D]] | B | PURPL activity raises PPM1D's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without PURPL | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[TYMSOS]] | B | PURPL activity raises TYMSOS's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.59× lower at baseline in the lines without PURPL | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ZNF423]] | B | PURPL activity raises ZNF423's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without PURPL | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ADAMTS7]] | B | PURPL activity raises ADAMTS7's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without PURPL | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[FDXR]] | B | PURPL activity raises FDXR's level | lines that do not express PURPL (25) vs lines expressing it (25) | 2.08× lower at baseline in the lines without PURPL | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[MIR3659HG]] | B | PURPL activity raises MIR3659HG's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without PURPL | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[GREB1]] | B | PURPL activity raises GREB1's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without PURPL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[TRIAP1]] | B | PURPL activity raises TRIAP1's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.33× lower at baseline in the lines without PURPL | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[MDM2]] | B | PURPL activity raises MDM2's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without PURPL | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ABCA12]] | B | PURPL activity strengthens ABCA12's drug response | lines that do not express PURPL (18) vs lines expressing it (15) | the lines without PURPL respond 0.47× as strongly (z diff +1.34); strongest at Idarubicin (hydrochloride) 5 µM: 1.82x vs 6.28x (z diff +5.7) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1; target measured in part of the lines; artifact flags |
| [[ZNF423]] | B | PURPL activity strengthens ZNF423's drug response | lines that do not express PURPL (20) vs lines expressing it (21) | the lines without PURPL respond 0.71× as strongly (z diff +0.84); strongest at Doxorubicin (hydrochloride) 5 µM: 1.75x vs 3.95x (z diff +2.7) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1; target measured in part of the lines; artifact flags |
| [[ACTA2]] | B | PURPL activity raises ACTA2's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.86× lower at baseline in the lines without PURPL | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 36.6); signed map (42.7, -23.7). **Vector** length 101, 32.2% of its response variance represented; |z| ≥ 3 in 920 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *p53 targets up* (control, mean cos +0.59 to 26); *p53 pathway* (hallmark, mean cos +0.54 to 26); *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.57 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~7% of this change | +6.7 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +8.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.7 | +4.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -3.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | p53 upregulated regulator of p53 levels |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p14.1 — chr5:27,217,714-27,497,871 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC643401, RP11-46C20.1; previously LINC01021 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48995) · Entrez [643401](https://www.ncbi.nlm.nih.gov/gene/643401) · Ensembl [ENSG00000250337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250337)

## Data

Gene col 14689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14689); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14689]; `tensor/DDL_lfc|DDL_z.npy` [14689]; `embed/gene_vectors.npy` [14689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14689 or target_col == 14689). Every well: [[PURPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PURPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
