---
symbol: "WNT5A"
type: "gene"
col: 3533
ensembl_id: "ENSG00000114251"
name: "Wnt family member 5A"
location: "3p14.3"
module: 13
arm: "+"
pooled_cpm: 34.9
n_lines_expressing: 20
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 52
direction_downstream: 71
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# WNT5A

*Wnt family member 5A* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +11.9, q 5e-30, up in 4 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Citalopram (hydrobromide) (drug)]] 0.05 µM: 1.34× (z +3.7, q 0.028, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.438× (z -10.4, q 2e-22, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A3]] (+0.68, fdr 7e-06), [[RFX8]] (+0.61, fdr 7e-06), [[THBS2]] (+0.60, fdr 9e-06); moves opposite to [[PATJ]] (-0.50, fdr 9e-05), [[NOXA1]] (-0.48, fdr 5e-05), [[DMTN]] (-0.43, fdr 2e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 52 arrows point to it, the strongest [[DMTN]] → it (grade B ⚠); 71 go from it, the strongest it → [[DBNDD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3533.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.57×** | +11.9 | 5e-30 | 4/18 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.7 | 7e-09 | 1/16 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +4.4 | 0.002 | 2/17 (NCI-H460, A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.028 | 9/18 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.028 | 8/18 (A-172, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.028 | 1/18 (SNU-423) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +3.6 | 0.028 | 2/18 (SW 900, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.028 | 5/18 (NCI-H460, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.4 | 0.037 | 2/18 (A-172, A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.059 | 0/18 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.059 | 2/17 (A498, NCI-H460) | inconsistent across doses | low cells (technical?) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.078 | 0/18 | inconsistent across doses | position effect removed |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.095 | 4/18 (A498, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3533.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.438×** | -10.4 | 2e-22 | 18/18 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.448×** | -10.1 | 2e-21 | 18/18 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -10.0 | 2e-21 | 17/18 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.473×** | -8.1 | 7e-14 | 15/18 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -7.5 | 5e-12 | 18/18 (HOP62, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.656×** | -5.0 | 6e-05 | 12/19 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.684×** | -4.4 | 9e-04 | 5/18 (SW480, NCI-H1792, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -4.2 | 0.002 | 7/18 (SW 1088, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -4.2 | 0.002 | 17/18 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.720×** | -4.1 | 0.002 | 6/18 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.508×** | -4.1 | 0.002 | 11/18 (H4, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.727×** | -4.0 | 0.003 | 2/17 (LOX-IMVI, SW480) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.735×** | -3.9 | 0.005 | 8/17 (H4, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.729×** | -3.8 | 0.006 | 11/18 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -3.7 | 0.009 | 12/18 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.560×** | -3.5 | 0.018 | 8/18 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3533. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 230 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0420× (z -26.4) |
| [[H4 (line)]] | wt | 135 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0310× (z -22.5) |
| [[hTERT-HPNE (line)]] | wt | 508 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0637× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 52.7 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -15.3) |
| [[HS-578T (line)]] | alt | 157 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0918× (z -17.3) |
| [[RPMI-7951 (line)]] | alt | 314 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -19.8) |
| [[SW480 (line)]] | alt | 23.6 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -17.3) |
| [[SW 1088 (line)]] | alt | 335 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0252× (z -14.5) |
| [[A-172 (line)]] | wt | 36.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -15.8) |
| [[A498 (line)]] | wt | 25.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -10.5) |
| [[J82 (line)]] | alt | 59.6 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 41.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.199× (z -10.5) |
| [[SNU-423 (line)]] | alt | 43.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -13.2) |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -10.3) |
| [[CHP-212 (line)]] | wt | 105 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0977× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.9) |
| [[A-427 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.34 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3533), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A3]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[RFX8]] | +0.61 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[THBS2]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PDGFRB]] | +0.60 | +0.62 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 442 |
| [[MME]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[PAPPA]] | +0.59 | +0.56 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[ADAMTS2]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LINC01615]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CNRIP1]] | +0.56 | +0.61 / +0.34 | both halves | 1e-04 | **novel candidate** |
| [[HS3ST3A1]] | +0.56 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[GYPC]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[LOX]] | +0.55 | +0.56 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 410 |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATJ]] | -0.50 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[NOXA1]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 | pathway: Killing mechanisms; STRING 509 |
| [[DMTN]] | -0.43 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[TSPAN3]] | -0.42 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[KIAA1522]] | -0.42 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[EPB41L1]] | -0.40 | -0.34 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*52 arrows, 52 of them with an alert ⚠; grade A 0, B 4, C 48. Shown: the 12 strongest; 40 more arrows (40 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMTN]] | B | DMTN activity lowers WNT5A's level | lines that do not express DMTN (14) vs lines expressing it (36) | 6.23× higher at baseline in the lines without DMTN | 0.011 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[NOXA1]] | B | NOXA1 activity lowers WNT5A's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 12.18× higher at baseline in the lines without NOXA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[SHC3]] | B | SHC3 activity raises WNT5A's level | lines that do not express SHC3 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without SHC3 | 0.047 | ⚠ within organs, on part of the lines; also absent: CCDC33, CCR3, RFX8; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises WNT5A's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDH13]] | C | CDH13 activity raises WNT5A's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 10.85× lower at baseline in the lines without CDH13 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises WNT5A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 13.75× lower at baseline in the lines without PDGFRB | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises WNT5A's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 12.84× lower at baseline in the lines without APCDD1L | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises WNT5A's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 9.16× lower at baseline in the lines without HS3ST3A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises WNT5A's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 6.92× lower at baseline in the lines without RFX8 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises WNT5A's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 9.77× lower at baseline in the lines without ADAMTS12 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises WNT5A's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 10.95× lower at baseline in the lines without ITGA11 | 0.001 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises WNT5A's level | lines that do not express CARMN (40) vs lines expressing it (10) | 14.39× lower at baseline in the lines without CARMN | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |

### Downstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 17, C 54. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DBNDD1]] | B | WNT5A activity lowers DBNDD1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.08× higher at baseline in the lines without WNT5A | 0.002 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[ITGA5]] | B | WNT5A activity raises ITGA5's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 4.25× lower at baseline in the lines without WNT5A | 0.005 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[SHC3]] | B | WNT5A activity raises SHC3's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without WNT5A | 0.007 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[TSHZ3]] | B | WNT5A activity strengthens TSHZ3's drug response | lines that do not express WNT5A (10) vs lines expressing it (13) | the lines without WNT5A respond 0.68× as strongly (z diff +1.16); strongest at Harringtonine 5 µM: 0.76x vs 0.40x (z diff +4.3) | 0.016 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; both ways; artifact flags |
| [[RILPL2]] | B | WNT5A activity raises RILPL2's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 1.45× lower at baseline in the lines without WNT5A | 0.018 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[NRP1]] | B | WNT5A activity raises NRP1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.56× lower at baseline in the lines without WNT5A | 0.018 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[RFTN1]] | B | WNT5A activity raises RFTN1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.87× lower at baseline in the lines without WNT5A | 0.035 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[NOXA1]] | B | WNT5A activity lowers NOXA1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.08× higher at baseline in the lines without WNT5A | 0.043 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[GPR68]] | B | WNT5A activity raises GPR68's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 1.96× lower at baseline in the lines without WNT5A | 0.043 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[SYTL3]] | B | WNT5A activity strengthens SYTL3's drug response | lines that do not express WNT5A (24) vs lines expressing it (15) | the lines without WNT5A respond 0.52× as strongly (z diff +2.53); strongest at Harringtonine 0.5 µM: 0.81x vs 0.20x (z diff +5.9) | 0.050 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; target measured in part of the lines; artifact flags |
| [[TSPAN3]] | B | WNT5A activity strengthens TSPAN3's drug response | lines that do not express WNT5A (30) vs lines expressing it (20) | the lines without WNT5A respond 0.81× as strongly (z diff +0.76); strongest at Idarubicin (hydrochloride) 5 µM: 1.00x vs 1.34x (z diff +3.7) | 0.052 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; both ways; artifact flags |
| [[SYTL3]] | B | WNT5A activity raises SYTL3's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without WNT5A | 0.053 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.5, 19.9); signed map (26.8, 47.5). **Vector** length 83.4, 30.3% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Signaling by PDGF* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.9 | +3.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.8 | +3.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.8 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.7 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -2.1 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 5A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:55,465,715-55,490,539 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hWNT5A |
| Gene groups (HGNC) | Wnt family |
| Hallmark sets | NOTCH_SIGNALING, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 21 pathways, smallest: Negative regulation of TCF-dependent signaling by WNT ligand antagonists; Killing mechanisms; WNT5:FZD7-mediated leishmania damping |
| Matched by | ensembl_id |

**Function**, from UniProt [P41221](https://www.uniprot.org/uniprotkb/P41221) (Protein Wnt-5a):

> Ligand for members of the frizzled family of seven transmembrane receptors. Can activate or inhibit canonical Wnt signaling, depending on receptor context. In the presence of FZD4, activates beta-catenin signaling. In the presence of ROR2, inhibits the canonical Wnt pathway by promoting beta-catenin degradation through a GSK3-independent pathway which involves down-regulation of beta-catenin-induced reporter gene expression (By similarity). Suppression of the canonical pathway allows …

**Summary**, from NCBI Gene [7474](https://www.ncbi.nlm.nih.gov/gene/7474):

> The WNT gene family consists of structurally related genes which encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. This gene encodes a member of the WNT family that signals through both the canonical and non-canonical WNT pathways. This protein is a ligand for the seven transmembrane receptor frizzled-5 and the tyrosine kinase orphan receptor 2. …

**Accessions** — [HGNC:12784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12784) · Entrez [7474](https://www.ncbi.nlm.nih.gov/gene/7474) · UniProt [P41221](https://www.uniprot.org/uniprotkb/P41221) · Ensembl [ENSG00000114251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114251)

## Data

Gene col 3533: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3533); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3533, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3533]; `tensor/DDL_lfc|DDL_z.npy` [3533]; `embed/gene_vectors.npy` [3533]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3533 or target_col == 3533). Every well: [[WNT5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
