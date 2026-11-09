---
symbol: "ADAMTS12"
type: "gene"
col: 7515
ensembl_id: "ENSG00000151388"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 12"
location: "5p13.3-p13.2"
module: 13
arm: "+"
pooled_cpm: 35.52
n_lines_expressing: 17
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 65
direction_downstream: 76
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS12

*ADAM metallopeptidase with thrombospondin type 1 motif 12* — 5p13.3-p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +10.2, q 7e-22, up in 2 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.65× (z +8.2, q 3e-14, up in 1 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.634× (z -5.2, q 9e-05, down in 9 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM200A]] (+0.69, fdr 7e-06), [[APCDD1L]] (+0.68, fdr 7e-06), [[APBB1IP]] (+0.67, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 65 arrows point to it, the strongest [[FAM167A]] → it (grade B ⚠); 76 go from it, the strongest it → [[NRP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7515.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +10.2 | 7e-22 | 2/14 (A549, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.2 | 9e-18 | 3/13 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.2 | 3e-14 | 1/15 (A549) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.9 | 6e-10 | 3/14 (A-172, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +4.6 | 4e-04 | 10/15 (H4, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.06×** | +4.4 | 0.001 | 10/16 (HOP62, SNU-423, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.004 | 10/14 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.017 | 5/15 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.020 | 10/15 (HOP62, H4, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.022 | 4/15 (A-172, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.023 | 5/15 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.033 | 3/15 (A549, NCI-H1792, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.068 | 0/16 | top dose only | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.30×** | +3.0 | 0.093 | 0/14 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7515.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.634×** | -5.2 | 9e-05 | 9/15 (hTERT-HPNE, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.684×** | -4.4 | 0.004 | 6/14 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.008 | 9/15 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.704×** | -4.0 | 0.008 | 11/15 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.012 | 7/15 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.698×** | -3.7 | 0.016 | 6/16 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.797×** | -3.7 | 0.016 | 9/15 (hTERT-HPNE, A498, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.016 | 6/14 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.719×** | -3.6 | 0.022 | 1/15 (A-172) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.023 | 10/15 (hTERT-HPNE, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.030 | 6/15 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.039 | 7/15 (hTERT-HPNE, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.755×** | -3.2 | 0.053 | 8/15 (hTERT-HPNE, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.749×** | -3.2 | 0.058 | 9/14 (H4, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.592×** | -3.2 | 0.060 | 3/15 (hTERT-HPNE, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7515. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 747 | 0 | 13 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.106× (z -15.2) |
| [[A-172 (line)]] | wt | 22.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 7.81× (z +10.2) | — |
| [[H4 (line)]] | wt | 38.7 | 3 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 12.7× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.116× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 79.4 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.67× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 89.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0943× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 164 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -9.6) |
| [[SNU-423 (line)]] | alt | 113 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -9.4) |
| [[A549 (line)]] | wt | 11.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.78× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -9.8) |
| [[J82 (line)]] | alt | 75.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.5) |
| [[A-427 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.40 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.36 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.91 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.83 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7515), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM200A]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.68 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[APBB1IP]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[AK5]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[FRMD4A]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[GLIS3]] | +0.65 | +0.69 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[EVC]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[VEPH1]] | +0.63 | +0.65 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[APCDD1L-DT]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[SIGLEC15]] | +0.61 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 3, C 62. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM167A]] | B | FAM167A activity raises ADAMTS12's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 3.72× lower at baseline in the lines without FAM167A | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[GPR68]] | B | GPR68 activity raises ADAMTS12's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without GPR68 | 0.094 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[SHC3]] | B | SHC3 activity raises ADAMTS12's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without SHC3 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[WNT5A]] | C | WNT5A activity raises ADAMTS12's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 7.30× lower at baseline in the lines without WNT5A | 3e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises ADAMTS12's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 12.63× lower at baseline in the lines without LINC01411 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises ADAMTS12's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 7.80× lower at baseline in the lines without APCDD1L | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[SAMD3]] | C | SAMD3 activity raises ADAMTS12's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 5.66× lower at baseline in the lines without SAMD3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[EDNRA]] | C | EDNRA activity raises ADAMTS12's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 7.39× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; co-absent with the target |
| [[TMEM200A]] | C | TMEM200A activity raises ADAMTS12's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 5.58× lower at baseline in the lines without TMEM200A | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |
| [[APBB1IP]] | C | APBB1IP activity raises ADAMTS12's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 11.89× lower at baseline in the lines without APBB1IP | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises ADAMTS12's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 7.12× lower at baseline in the lines without PDCD1LG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises ADAMTS12's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 6.33× lower at baseline in the lines without CDH13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 13, C 63. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | ADAMTS12 activity raises NRP1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.42× lower at baseline in the lines without ADAMTS12 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[FAM167A]] | B | ADAMTS12 activity raises FAM167A's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without ADAMTS12 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[CD44]] | B | ADAMTS12 activity raises CD44's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.95× lower at baseline in the lines without ADAMTS12 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[MYO10]] | B | ADAMTS12 activity raises MYO10's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.26× lower at baseline in the lines without ADAMTS12 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[GPR68]] | B | ADAMTS12 activity raises GPR68's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.24× lower at baseline in the lines without ADAMTS12 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[MIR4435-2HG]] | B | ADAMTS12 activity raises MIR4435-2HG's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 1.74× lower at baseline in the lines without ADAMTS12 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[EVC]] | B | ADAMTS12 activity raises EVC's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without ADAMTS12 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[RAI14]] | B | ADAMTS12 activity raises RAI14's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without ADAMTS12 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[SORCS2]] | B | ADAMTS12 activity raises SORCS2's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without ADAMTS12 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[SPEG]] | B | ADAMTS12 activity raises SPEG's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 2.92× lower at baseline in the lines without ADAMTS12 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1 |
| [[CYTOR]] | B | ADAMTS12 activity weakens CYTOR's drug response | lines that do not express ADAMTS12 (31) vs lines expressing it (17) | the lines without ADAMTS12 respond 1.55× as strongly (z diff -1.97); strongest at Harringtonine 5 µM: 2.50x vs 1.30x (z diff -5.0) | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; target measured in part of the lines; artifact flags |
| [[ARHGAP22]] | B | ADAMTS12 activity strengthens ARHGAP22's drug response | lines that do not express ADAMTS12 (14) vs lines expressing it (13) | the lines without ADAMTS12 respond 0.72× as strongly (z diff +1.81); strongest at Belinostat 5 µM: 0.61x vs 0.32x (z diff +5.0) | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.8, 17.2); signed map (21.5, 47.0). **Vector** length 68.6, 26.6% of its response variance represented; |z| ≥ 3 in 412 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.5 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.3-p13.2 — chr5:33,523,535-33,892,019 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P58397](https://www.uniprot.org/uniprotkb/P58397) (A disintegrin and metalloproteinase with thrombospondin motifs 12):

> Metalloprotease that may play a role in the degradation of COMP. Also cleaves alpha-2 macroglobulin and aggregan. Has anti-tumorigenic properties.

**Summary**, from NCBI Gene [81792](https://www.ncbi.nlm.nih.gov/gene/81792):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS-1) motif. Individual members of this family differ in the number of C-terminal TS-1 motifs, and some have unique C-terminal domains. The enzyme encoded by this gene contains eight TS-1 motifs. It …

**Accessions** — [HGNC:14605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14605) · Entrez [81792](https://www.ncbi.nlm.nih.gov/gene/81792) · UniProt [P58397](https://www.uniprot.org/uniprotkb/P58397) · Ensembl [ENSG00000151388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151388)

## Data

Gene col 7515: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7515); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7515, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7515]; `tensor/DDL_lfc|DDL_z.npy` [7515]; `embed/gene_vectors.npy` [7515]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7515 or target_col == 7515). Every well: [[ADAMTS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
