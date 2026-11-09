---
symbol: "PDGFRB"
type: "gene"
col: 3495
ensembl_id: "ENSG00000113721"
name: "platelet derived growth factor receptor beta"
location: "5q32"
module: 13
arm: "+"
pooled_cpm: 11.25
n_lines_expressing: 14
n_dd_up: 10
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 77
direction_downstream: 96
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# PDGFRB

*platelet derived growth factor receptor beta* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.04× (z +12.8, q 5e-35, up in 3 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pyridoxine (drug)]] 0.5 µM: 1.48× (z +3.6, q 0.026, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.437× (z -7.6, q 2e-11, down in 10 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A1]] (+0.79, fdr 7e-06), [[CARMN]] (+0.78, fdr 7e-06), [[COL6A3]] (+0.74, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 77 arrows point to it, the strongest [[CLEC11A]] → it (grade B ⚠); 96 go from it, the strongest it → [[CLEC11A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3495.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.04×** | +12.8 | 5e-35 | 3/11 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.74×** | +11.7 | 5e-29 | 3/9 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.6 | 1e-15 | 4/10 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.2 | 0.004 | 0/7 | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.7 | 0.026 | 0/10 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.026 | 1/11 (J82) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.026 | 2/11 (RPMI-7951, A-172) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +3.6 | 0.026 | 2/9 (A-172, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.041 | 4/11 (NCI-H460, A-172, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.41×** | +3.2 | 0.087 | 4/11 (SNU-423, CHP-212, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.59× | +3.0 | 0.12 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.12 | 0/11 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3495.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.437×** | -7.6 | 2e-11 | 10/11 (hTERT-HPNE, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -6.7 | 7e-09 | 11/12 (HOP62, H4, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.624×** | -6.1 | 2e-07 | 11/12 (RPMI-7951, SW 1088, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.529×** | -5.8 | 7e-07 | 12/12 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.539×** | -5.7 | 1e-06 | 8/11 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.538×** | -5.5 | 4e-06 | 10/11 (CHP-212, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.552×** | -5.5 | 4e-06 | 9/11 (hTERT-HPNE, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.565×** | -5.2 | 1e-05 | 11/12 (RPMI-7951, SW 1088, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -5.1 | 2e-05 | 9/11 (H4, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -5.0 | 3e-05 | 10/12 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.718×** | -4.3 | 8e-04 | 7/12 (RPMI-7951, J82, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.631×** | -4.2 | 0.001 | 11/11 (H4, RPMI-7951, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.629×** | -4.1 | 0.002 | 6/11 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.683×** | -3.5 | 0.018 | 0/12 | two highest doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.684×** | -3.5 | 0.018 | 7/12 (CHP-212, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.680×** | -3.4 | 0.023 | 5/10 (H4, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.054 | 11/12 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3495. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 163 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0787× (z -16.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0885× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 233 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0304× (z -15.4) |
| [[HOP62 (line)]] | alt | 110 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0926× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0918× (z -12.4) |
| [[H4 (line)]] | wt | 31.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0850× (z -9.7) |
| [[J82 (line)]] | alt | 15.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 77.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 3.57 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0589× (z -10.6) |
| [[SW 1088 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.895 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.912 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.775 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.750 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.736 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.726 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.681 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.727 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.994 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.04 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3495), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A1]] | +0.79 | +0.79 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 406 |
| [[CARMN]] | +0.78 | +0.79 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[COL6A3]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 633 |
| [[APCDD1L]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[ARHGEF6]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[COL1A2]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 629 |
| [[THBS2]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 449 |
| [[KCNE4]] | +0.70 | +0.69 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01615]] | +0.69 | +0.72 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[NID2]] | +0.68 | +0.58 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 421 |
| [[FBN1]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 546 |
| [[ITGA11]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 | STRING 638 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 1, C 76. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLEC11A]] | B | CLEC11A activity raises PDGFRB's level | lines that do not express CLEC11A (21) vs lines expressing it (29) | 1.77× lower at baseline in the lines without CLEC11A | 0.079 | ⚠ within organs, on part of the lines; also absent: GABBR2, JAKMIP1, SHANK1 |
| [[CARMN]] | C | CARMN activity raises PDGFRB's level | lines that do not express CARMN (40) vs lines expressing it (10) | 17.21× lower at baseline in the lines without CARMN | 9e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises PDGFRB's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 10.48× lower at baseline in the lines without LINC01411 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises PDGFRB's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 9.97× lower at baseline in the lines without APCDD1L | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises PDGFRB's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 6.74× lower at baseline in the lines without WNT5A | 0.001 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises PDGFRB's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 8.34× lower at baseline in the lines without MMP2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises PDGFRB's level | lines that do not express SPARC (34) vs lines expressing it (16) | 8.14× lower at baseline in the lines without SPARC | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises PDGFRB's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 7.39× lower at baseline in the lines without ITGA4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises PDGFRB's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 10.02× lower at baseline in the lines without ITGA11 | 0.001 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises PDGFRB's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 6.37× lower at baseline in the lines without COL1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises PDGFRB's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.74× lower at baseline in the lines without COL5A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises PDGFRB's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 4.59× lower at baseline in the lines without FBN1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |

### Downstream of this gene

*96 arrows, 96 of them with an alert ⚠; grade A 0, B 21, C 75. Shown: the 12 strongest; 84 more arrows (84 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLEC11A]] | B | PDGFRB activity raises CLEC11A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.17× lower at baseline in the lines without PDGFRB | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SLCO1C1]] | B | PDGFRB activity raises SLCO1C1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[THBS2-AS1]] | B | PDGFRB activity raises THBS2-AS1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 1.73× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[PCBP3]] | B | PDGFRB activity raises PCBP3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.62× lower at baseline in the lines without PDGFRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[PAPSS2]] | B | PDGFRB activity raises PAPSS2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.67× lower at baseline in the lines without PDGFRB | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[LOXL1]] | B | PDGFRB activity raises LOXL1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 3.34× lower at baseline in the lines without PDGFRB | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[B3GNT9]] | B | PDGFRB activity raises B3GNT9's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 1.85× lower at baseline in the lines without PDGFRB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[NOTCH3]] | B | PDGFRB activity raises NOTCH3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.97× lower at baseline in the lines without PDGFRB | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SSC5D]] | B | PDGFRB activity raises SSC5D's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without PDGFRB | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[TMEM45A]] | B | PDGFRB activity raises TMEM45A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.46× lower at baseline in the lines without PDGFRB | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SLC14A2]] | B | PDGFRB activity raises SLC14A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without PDGFRB | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[SYTL3]] | B | PDGFRB activity raises SYTL3's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without PDGFRB | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.4, 19.3); signed map (25.7, 45.2). **Vector** length 67.9, 31.6% of its response variance represented; |z| ≥ 3 in 370 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen formation* (reactome, mean cos +0.55 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.56 to 10); *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.58 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +8.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -5.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -4.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:150,113,839-150,155,872 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JTK12, CD140b, PDGFR1; previously PDGFR |
| Gene groups (HGNC) | CD molecules; I-set domain containing; Platelet derived growth factor receptor family |
| Hallmark sets | UV_RESPONSE_DN, APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 13 pathways, smallest: Downstream signal transduction; Signaling by PDGF; Constitutive Signaling by Aberrant PI3K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P09619](https://www.uniprot.org/uniprotkb/P09619) (Platelet-derived growth factor receptor beta):

> Tyrosine-protein kinase that acts as a cell-surface receptor for homodimeric PDGFB and PDGFD and for heterodimers formed by PDGFA and PDGFB, and plays an essential role in the regulation of embryonic development, cell proliferation, survival, differentiation, chemotaxis and migration. Plays an essential role in blood vessel development by promoting proliferation, migration and recruitment of pericytes and smooth muscle cells to endothelial cells. Plays a role in the migration of vascular smooth …

**Summary**, from NCBI Gene [5159](https://www.ncbi.nlm.nih.gov/gene/5159):

> The protein encoded by this gene is a cell surface tyrosine kinase receptor for members of the platelet-derived growth factor family. These growth factors are mitogens for cells of mesenchymal origin. The identity of the growth factor bound to a receptor monomer determines whether the functional receptor is a homodimer (PDGFB or PDGFD) or a heterodimer (PDGFA and PDGFB). This gene is essential for normal development of the cardiovascular system and aids in rearrangement of the actin …

**Accessions** — [HGNC:8804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8804) · Entrez [5159](https://www.ncbi.nlm.nih.gov/gene/5159) · UniProt [P09619](https://www.uniprot.org/uniprotkb/P09619) · Ensembl [ENSG00000113721](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113721)

## Data

Gene col 3495: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3495); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3495, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3495]; `tensor/DDL_lfc|DDL_z.npy` [3495]; `embed/gene_vectors.npy` [3495]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3495 or target_col == 3495). Every well: [[PDGFRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
