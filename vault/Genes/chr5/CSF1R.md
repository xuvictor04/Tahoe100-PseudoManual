---
symbol: "CSF1R"
type: "gene"
col: 11302
ensembl_id: "ENSG00000182578"
name: "colony stimulating factor 1 receptor"
location: "5q32"
module: 13
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 24
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 22
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CSF1R

*colony stimulating factor 1 receptor* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.55× (z +12.8, q 6e-35, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 3.05× (z +12.3, q 3e-32, up in 6 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0722×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0923×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.236×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.197×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SNU-423 0.0470×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOCD1]] (+0.73, fdr 7e-06), [[COL5A3]] (+0.70, fdr 7e-06), [[GPR68]] (+0.65, fdr 7e-06); moves opposite to [[CHPT1]] (-0.52, fdr 4e-05), [[ARMC8]] (-0.50, fdr 3e-05), [[DPY19L1P1]] (-0.48, fdr 3e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SPOCD1]] → it (grade B ⚠); 22 go from it, the strongest it → [[DUSP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11302.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.55×** | +12.8 | 6e-35 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.05×** | +12.3 | 3e-32 | 6/15 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.25×** | +9.2 | 8e-18 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +8.9 | 7e-17 | 6/19 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.59×** | +7.4 | 1e-11 | 6/19 (SK-MEL-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +7.4 | 1e-11 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.1 | 8e-11 | 1/12 (SW480) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +6.7 | 2e-09 | 6/19 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.13×** | +4.2 | 0.002 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.002 | 7/18 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.70×** | +4.1 | 0.002 | 2/18 (SK-MEL-2, SW1417) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.58×** | +3.4 | 0.028 | 0/7 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +3.4 | 0.033 | 4/12 (HCT15, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.033 | 2/9 (hTERT-HPNE, A-172) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.3 | 0.034 | 0/8 | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.065 | 0/9 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.1 | 0.065 | 2/12 (NCI-H2347, A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.0 | 0.076 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.083 | 3/18 (A-172, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +2.9 | 0.083 | 2/16 (A-172, Panc 03.27) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11302.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0722×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0923×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.236×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.197×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SNU-423 0.0470×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.669× | -3.1 | 0.83 | 8/17 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11302. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 34.0 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0722× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -12.4) |
| [[SNU-423 (line)]] | alt | 6.51 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +8.9) | [[Bortezomib (drug)]] 0.05 µM 0.0470× (z -9.7) |
| [[A-172 (line)]] | wt | 2.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.7) | — |
| [[SK-MEL-2 (line)]] | alt | 1.39 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 21.3× (z +8.6) | — |
| [[A-427 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.737 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.421 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.655 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.718 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11302), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCD1]] | +0.73 | +0.58 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[COL5A3]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[GPR68]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[APCDD1L-DT]] | +0.65 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.64 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[PLEKHG4B]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SYNDIG1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[ITGA11]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[GRIN2A]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[COL7A1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[BAALC]] | +0.61 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHPT1]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[ARMC8]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[DPY19L1P1]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPOCD1]] | B | SPOCD1 activity raises CSF1R's level | lines that do not express SPOCD1 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without SPOCD1 | 0.078 | ⚠ within organs, on part of the lines; also absent: IL7R, ARMCX1, IDO1 |
| [[GDNF]] | C | GDNF activity raises CSF1R's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.17× lower at baseline in the lines without GDNF | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises CSF1R's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without EDNRA | 0.033 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[LINC01705]] | C | LINC01705 activity raises CSF1R's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without LINC01705 | 0.048 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises CSF1R's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.31× lower at baseline in the lines without PDGFRB | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[DGKI]] | C | DGKI activity raises CSF1R's level | lines that do not express DGKI (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without DGKI | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, LAMA1; maybe low, not absent; co-absent with the target |
| [[COL6A2]] | C | COL6A2 activity raises CSF1R's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without COL6A2 | 0.099 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 8, C 14. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | CSF1R activity raises DUSP10's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.21× lower at baseline in the lines without CSF1R | 0.006 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[COL5A3]] | B | CSF1R activity raises COL5A3's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.61× lower at baseline in the lines without CSF1R | 0.043 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[COL6A1]] | B | CSF1R activity raises COL6A1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.07× lower at baseline in the lines without CSF1R | 0.057 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[GDNF-AS1]] | B | CSF1R activity raises GDNF-AS1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.15× lower at baseline in the lines without CSF1R | 0.070 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[SGMS1]] | B | CSF1R activity lowers SGMS1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.30× higher at baseline in the lines without CSF1R | 0.074 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[GRIK4]] | B | CSF1R activity raises GRIK4's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.71× lower at baseline in the lines without CSF1R | 0.082 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[SEMA7A]] | B | CSF1R activity raises SEMA7A's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.79× lower at baseline in the lines without CSF1R | 0.094 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[KCNIP1]] | B | CSF1R activity raises KCNIP1's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 1.36× lower at baseline in the lines without CSF1R | 0.095 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[BAALC]] | C | CSF1R activity raises BAALC's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.78× lower at baseline in the lines without CSF1R | 0.012 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |
| [[LINC01705]] | C | CSF1R activity raises LINC01705's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.56× lower at baseline in the lines without CSF1R | 0.023 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |
| [[SARDH]] | C | CSF1R activity raises SARDH's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 2.51× lower at baseline in the lines without CSF1R | 0.024 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |
| [[GDNF]] | C | CSF1R activity raises GDNF's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.19× lower at baseline in the lines without CSF1R | 0.030 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.6, 14.5); signed map (22.1, 47.5). **Vector** length 36.5, 7.49% of its response variance represented; |z| ≥ 3 in 484 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of the extracellular matrix* (reactome, mean cos +0.50 to 11); *Collagen degradation* (reactome, mean cos +0.52 to 8); *Collagen chain trimerization* (reactome, mean cos +0.54 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.5 | +12.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.8 | +1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.6 | +1.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | colony stimulating factor 1 receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:150,053,291-150,113,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M-CSF-R, C-FMS, CSFR, CD115; previously FMS |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; CSF1R, KIT, FLT3 receptor tyrosine kinase family |
| Reactome | 5 pathways, smallest: Other interleukin signaling; Signaling by CSF1 (M-CSF) in myeloid cells; Transcriptional Regulation by VENTX |
| Matched by | ensembl_id |

**Function**, from UniProt [P07333](https://www.uniprot.org/uniprotkb/P07333) (Macrophage colony-stimulating factor 1 receptor):

> Tyrosine-protein kinase that acts as a cell-surface receptor for CSF1 and IL34 and plays an essential role in the regulation of survival, proliferation and differentiation of hematopoietic precursor cells, especially mononuclear phagocytes, such as macrophages and monocytes. Promotes the release of pro-inflammatory chemokines in response to IL34 and CSF1, and thereby plays an important role in innate immunity and in inflammatory processes. Plays an important role in the regulation of osteoclast …

**Summary**, from NCBI Gene [1436](https://www.ncbi.nlm.nih.gov/gene/1436):

> The protein encoded by this gene is the receptor for colony stimulating factor 1, a cytokine which controls the production, differentiation, and function of macrophages. This receptor mediates most if not all of the biological effects of this cytokine. Ligand binding activates the receptor kinase through a process of oligomerization and transphosphorylation. The encoded protein is a tyrosine kinase transmembrane receptor and member of the CSF1/PDGF receptor family of tyrosine-protein kinases. …

**Accessions** — [HGNC:2433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2433) · Entrez [1436](https://www.ncbi.nlm.nih.gov/gene/1436) · UniProt [P07333](https://www.uniprot.org/uniprotkb/P07333) · Ensembl [ENSG00000182578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182578)

## Data

Gene col 11302: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11302); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11302, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11302]; `tensor/DDL_lfc|DDL_z.npy` [11302]; `embed/gene_vectors.npy` [11302]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11302 or target_col == 11302). Every well: [[CSF1R — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSF1R.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
