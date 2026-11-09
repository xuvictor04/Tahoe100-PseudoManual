---
symbol: "RFTN1"
type: "gene"
col: 5200
ensembl_id: "ENSG00000131378"
name: "raftlin, lipid raft linker 1"
location: "3p24.3"
module: 13
arm: "+"
pooled_cpm: 26.14
n_lines_expressing: 30
n_dd_up: 15
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 33
direction_downstream: 12
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# RFTN1

*raftlin, lipid raft linker 1* — 3p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +9.2, q 2e-17, up in 2 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.32× (z +6.8, q 3e-09, up in 10 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.698× (z -6.1, q 5e-07, down in 18 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETS1]] (+0.66, fdr 7e-06), [[FRMD4A]] (+0.64, fdr 7e-06), [[BNC1]] (+0.64, fdr 1e-05); moves opposite to [[UBE4B]] (-0.46, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[TMEM200A]] → it (grade B ⚠); 12 go from it, the strongest it → [[FMNL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +9.2 | 2e-17 | 2/18 (RPMI-7951, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.1 | 2e-13 | 3/24 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +6.8 | 3e-09 | 10/28 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.44×** | +6.2 | 1e-07 | 12/27 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +5.8 | 8e-07 | 12/28 (PANC-1, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +5.3 | 1e-05 | 16/27 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 15/28 (NCI-H2347, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 1e-04 | 10/27 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.3 | 1e-03 | 10/28 (NCI-H2347, A549, …) | top dose only | composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +4.3 | 0.001 | 10/27 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 10/26 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.2 | 0.001 | 3/28 (PANC-1, H4, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.24×** | +3.7 | 0.009 | 6/27 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.009 | 7/26 (PANC-1, A-427, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.027 | 0/26 | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.2 | 0.047 | 13/27 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.698×** | -6.1 | 5e-07 | 18/27 (LOX-IMVI, A-172, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.714×** | -5.7 | 3e-06 | 16/27 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.723×** | -5.5 | 7e-06 | 10/26 (NCI-H23, HS-578T, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.744×** | -5.0 | 7e-05 | 17/27 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.769×** | -4.5 | 8e-04 | 14/27 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.788×** | -4.0 | 0.005 | 16/27 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.642×** | -3.9 | 0.007 | 13/23 (J82, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **0.792×** | -3.8 | 0.009 | 3/27 (RPMI-7951, A-172, …) | top dose only | plate-row cell shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.7 | 0.015 | 4/28 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.809×** | -3.6 | 0.017 | 13/27 (SNU-423, A-172, …) | two highest doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.871× | -3.3 | 0.045 | 5/28 (HS-578T, SW 900, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.832×** | -3.1 | 0.084 | 9/27 (HOP62, J82, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.1 | 0.085 | 10/28 (J82, HEC-1-A, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 0.835× | -3.1 | 0.085 | 11/28 (HOP62, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 142 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.179× (z -13.0) |
| [[A498 (line)]] | wt | 36.9 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +9.6) ⚠ cell-cycle shift, explains ~5% of this change | [[Panobinostat (drug)]] 5 µM 0.249× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 32.4 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.58× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -13.9) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.242× (z -10.2) |
| [[SNU-423 (line)]] | alt | 80.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -14.7) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.169× (z -13.2) |
| [[HOP62 (line)]] | alt | 65.5 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.320× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.337× (z -9.0) |
| [[HS-578T (line)]] | alt | 129 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -10.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -9.9) |
| [[J82 (line)]] | alt | 66.6 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -9.8) ⚠ cell-cycle shift, explains ~12% of this change |
| [[LOX-IMVI (line)]] | wt | 138 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 11.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.82× (z +10.1) | — |
| [[A549 (line)]] | wt | 17.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +14.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.09× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 10.3 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.169× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 50.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Docetaxel (drug)]] 0.05 µM 0.204× (z -9.6) ⚠ transcription drop; cell-cycle shift, explains ~6% of this change |
| [[PANC-1 (line)]] | alt | 8.98 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.30× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 62.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.293× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.617× (z -9.8) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 69.7 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.206× (z -9.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.61 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETS1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FRMD4A]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[BNC1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[LINC00702]] | +0.63 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ADAMTS12]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.60 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[AKT3]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[FMNL3]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[FRMD6]] | +0.58 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[EVA1A]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP31]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[APCDD1L-DT]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE4B]] | -0.46 | -0.39 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 14, C 19. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM200A]] | B | TMEM200A activity raises RFTN1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 4.01× lower at baseline in the lines without TMEM200A | 7e-04 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[SAMD3]] | B | SAMD3 activity raises RFTN1's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 3.70× lower at baseline in the lines without SAMD3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11 |
| [[FAM167A]] | B | FAM167A activity raises RFTN1's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 4.04× lower at baseline in the lines without FAM167A | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent |
| [[WNT5A]] | B | WNT5A activity raises RFTN1's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.87× lower at baseline in the lines without WNT5A | 0.035 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13 |
| [[SYNPO]] | B | SYNPO activity raises RFTN1's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 3.42× lower at baseline in the lines without SYNPO | 0.044 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[NECTIN3]] | B | NECTIN3 activity raises RFTN1's level | lines that do not express NECTIN3 (11) vs lines expressing it (39) | 3.37× lower at baseline in the lines without NECTIN3 | 0.061 | ⚠ within organs, on part of the lines; also absent: CD96, NECTIN3-AS1, GPR176 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises RFTN1's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 2.53× lower at baseline in the lines without C1QTNF1 | 0.061 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[ANXA8]] | B | ANXA8 activity raises RFTN1's level | lines that do not express ANXA8 (38) vs lines expressing it (12) | 2.72× lower at baseline in the lines without ANXA8 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5 |
| [[CDH13]] | B | CDH13 activity raises RFTN1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 4.07× lower at baseline in the lines without CDH13 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[EVA1A]] | B | EVA1A activity raises RFTN1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 2.85× lower at baseline in the lines without EVA1A | 0.068 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2 |
| [[FJX1]] | B | FJX1 activity raises RFTN1's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 3.65× lower at baseline in the lines without FJX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[HEG1]] | B | HEG1 activity raises RFTN1's level | lines that do not express HEG1 (11) vs lines expressing it (39) | 3.87× lower at baseline in the lines without HEG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 7, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMNL3]] | B | RFTN1 activity raises FMNL3's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without RFTN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[NECTIN3]] | B | RFTN1 activity raises NECTIN3's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.64× lower at baseline in the lines without RFTN1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[PALM2AKAP2]] | B | RFTN1 activity raises PALM2AKAP2's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 4.14× lower at baseline in the lines without RFTN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[HEG1]] | B | RFTN1 activity raises HEG1's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without RFTN1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[PPP2R5C]] | B | RFTN1 activity lowers PPP2R5C's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 1.29× higher at baseline in the lines without RFTN1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[DSE]] | B | RFTN1 activity raises DSE's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.03× lower at baseline in the lines without RFTN1 | 0.083 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[PRSS23]] | B | RFTN1 activity raises PRSS23's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 2.18× lower at baseline in the lines without RFTN1 | 0.095 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[GPR176]] | C | RFTN1 activity raises GPR176's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 7.94× lower at baseline in the lines without RFTN1 | 0.008 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1; co-absent with the target |
| [[EVC]] | C | RFTN1 activity raises EVC's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 4.66× lower at baseline in the lines without RFTN1 | 0.038 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1; co-absent with the target |
| [[LINC00702]] | C | RFTN1 activity raises LINC00702's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.30× lower at baseline in the lines without RFTN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1; co-absent with the target |
| [[FLI1]] | C | RFTN1 activity raises FLI1's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 4.41× lower at baseline in the lines without RFTN1 | 0.061 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1; co-absent with the target |
| [[FRMD4A]] | C | RFTN1 activity raises FRMD4A's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 4.28× lower at baseline in the lines without RFTN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.616). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 14.7); signed map (19.2, 45.0). **Vector** length 80.4, 21.0% of its response variance represented; |z| ≥ 3 in 728 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.2 | +4.3 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -6.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -2.3 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -5.0 |
|  | [[NG25 (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.6 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | raftlin, lipid raft linker 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.3 — chr3:16,313,574-16,514,026 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MIG2, KIAA0084, FLJ23866, Raftlin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14699](https://www.uniprot.org/uniprotkb/Q14699) (Raftlin):

> Involved in protein trafficking via association with clathrin and AP2 complex. Upon bacterial lipopolysaccharide stimulation, mediates internalization of TLR4 to endosomes in dendritic cells and macrophages; and internalization of poly(I:C) to TLR3-positive endosomes in myeloid dendritic cells and epithelial cells; resulting in activation of TICAM1-mediated signaling and subsequent IFNB1 production. Involved in T-cell antigen receptor-mediated signaling by regulating tyrosine kinase LCK …

**Summary**, from NCBI Gene [23180](https://www.ncbi.nlm.nih.gov/gene/23180):

> Enables double-stranded RNA binding activity. Involved in B cell receptor signaling pathway; membrane raft assembly; and positive regulation of growth rate. Acts upstream of or within dsRNA transport; response to exogenous dsRNA; and toll-like receptor 3 signaling pathway. Located in endosome; membrane raft; and plasma membrane. Part of protein-containing complex. Biomarker of glaucoma. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30278) · Entrez [23180](https://www.ncbi.nlm.nih.gov/gene/23180) · UniProt [Q14699](https://www.uniprot.org/uniprotkb/Q14699) · Ensembl [ENSG00000131378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131378)

## Data

Gene col 5200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5200); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5200]; `tensor/DDL_lfc|DDL_z.npy` [5200]; `embed/gene_vectors.npy` [5200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5200 or target_col == 5200). Every well: [[RFTN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFTN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
