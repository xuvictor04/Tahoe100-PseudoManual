---
symbol: "TIMP1"
type: "gene"
col: 2231
ensembl_id: "ENSG00000102265"
name: "TIMP metallopeptidase inhibitor 1"
location: "Xp11.3"
module: 81
arm: "+"
pooled_cpm: 111.29
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 18
direction_downstream: 12
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# TIMP1

*TIMP metallopeptidase inhibitor 1* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +6.5, q 4e-08, up in 40 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 8.03×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 7.35×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -7.9, q 1e-12, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP6]] (+0.75, fdr 7e-06), [[STC1]] (+0.74, fdr 7e-06), [[SH3BGRL3]] (+0.69, fdr 7e-06); moves opposite to [[FUBP1]] (-0.61, fdr 1e-05), [[MIR3936HG]] (-0.54, fdr 1e-05), [[LARP1]] (-0.53, fdr 4e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[SERPIND1]] → it (grade B ⚠); 12 go from it, the strongest it → [[NT5E]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2231.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 8.03×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (NCI-H1573 7.35×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.61×** | +6.5 | 4e-08 | 40/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.20×** | +5.2 | 7e-05 | 32/40 (Hs 766T, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.93×** | +4.1 | 0.007 | 29/42 (SNU-1, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.7 | 0.027 | 29/44 (MIA PaCa-2, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.60× | +3.2 | 0.14 | 25/45 (NCI-H1573, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | 1.59× | +3.2 | 0.14 | 30/45 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2231.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.438×** | -7.9 | 1e-12 | 37/45 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.393×** | -4.9 | 2e-04 | 42/47 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.522×** | -4.1 | 0.009 | 40/45 (HepG2/C3A, HCT15, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.561×** | -3.8 | 0.024 | 29/44 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.546×** | -3.6 | 0.028 | 28/45 (HepG2/C3A, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.673×** | -3.6 | 0.028 | 36/45 (HepG2/C3A, HS-578T, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.308×** | -3.5 | 0.039 | 38/45 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.320×** | -3.4 | 0.048 | 38/47 (HepG2/C3A, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.596×** | -3.4 | 0.048 | 29/46 (C32, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | 0.632× | -3.1 | 0.11 | 31/45 (HOP62, H4, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.636× | -3.1 | 0.11 | 23/45 (HepG2/C3A, HOP62, …) | top dose only |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.639× | -3.0 | 0.12 | 28/45 (HCT15, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2231. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 774 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0510× (z -19.5) |
| [[NCI-H1792 (line)]] | alt | 283 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -14.2) |
| [[HOP62 (line)]] | alt | 347 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 61.4 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 8.03× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1088 (line)]] | alt | 217 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0986× (z -10.0) |
| [[AN3 CA (line)]] | alt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -11.1) |
| [[H4 (line)]] | wt | 238 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -13.9) |
| [[HS-578T (line)]] | alt | 268 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 558 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -10.2) |
| [[KATO III (line)]] | alt | 73.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 157 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 64.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 173 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 287 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.2) |
| [[A-172 (line)]] | wt | 78.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.24 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 46.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.9 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 231 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2231), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP6]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[STC1]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_ANGIOGENESIS |
| [[SH3BGRL3]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[MMP1]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 999 |
| [[ITGA2]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION |
| [[S100A16]] | +0.64 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[RAC2]] | +0.64 | +0.62 / +0.60 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[RGS17]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[MARCHF3]] | +0.63 | +0.57 / +0.60 | both halves | 8e-06 |  |
| [[ARID3B]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ABTB3]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYN1]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 | STRING 532; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PHC2]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUBP1]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[MIR3936HG]] | -0.54 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[LARP1]] | -0.53 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[PAIP1]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPIND1]] | B | SERPIND1 activity raises TIMP1's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 2.70× lower at baseline in the lines without SERPIND1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[NPAS2]] | B | NPAS2 activity raises TIMP1's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.68× lower at baseline in the lines without NPAS2 | 0.015 | ⚠ within organs, on part of the lines |
| [[PLAT]] | B | PLAT activity raises TIMP1's level | lines that do not express PLAT (28) vs lines expressing it (22) | 2.26× lower at baseline in the lines without PLAT | 0.018 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[ANTXR2]] | B | ANTXR2 activity raises TIMP1's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 2.71× lower at baseline in the lines without ANTXR2 | 0.020 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[SMOX]] | B | SMOX activity raises TIMP1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.24× lower at baseline in the lines without SMOX | 0.024 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[TMEM158]] | B | TMEM158 activity raises TIMP1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.26× lower at baseline in the lines without TMEM158 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[TESMIN]] | B | TESMIN activity lowers TIMP1's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.19× higher at baseline in the lines without TESMIN | 0.044 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[GFPT2]] | B | GFPT2 activity raises TIMP1's level | lines that do not express GFPT2 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without GFPT2 | 0.047 | ⚠ within organs, on part of the lines; also absent: PDCD1LG2, MIR100HG, AK5 |
| [[CD59]] | B | CD59 activity raises TIMP1's level | lines that do not express CD59 (7) vs lines expressing it (43) | 2.97× lower at baseline in the lines without CD59 | 0.060 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[HAS2]] | B | HAS2 activity raises TIMP1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without HAS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[BCL2A1]] | B | BCL2A1 activity raises TIMP1's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without BCL2A1 | 0.062 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[HTR7]] | B | HTR7 activity raises TIMP1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.98× lower at baseline in the lines without HTR7 | 0.067 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5E]] | C | TIMP1 activity raises NT5E's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 6.03× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[FXYD5]] | C | TIMP1 activity raises FXYD5's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 5.58× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[PLAUR]] | C | TIMP1 activity raises PLAUR's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 5.09× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[WWTR1]] | C | TIMP1 activity raises WWTR1's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.76× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[SHB]] | C | TIMP1 activity raises SHB's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.21× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[PLIN3]] | C | TIMP1 activity raises PLIN3's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[PTPN12]] | C | TIMP1 activity raises PTPN12's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[NUMB]] | C | TIMP1 activity raises NUMB's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 1.45× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[CD59]] | C | TIMP1 activity raises CD59's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.43× lower at baseline in the lines without TIMP1 | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent |
| [[ITGA5]] | C | TIMP1 activity raises ITGA5's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 5.55× lower at baseline in the lines without TIMP1 | 0.083 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent |
| [[EHD1]] | C | TIMP1 activity raises EHD1's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 1.63× lower at baseline in the lines without TIMP1 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent |
| [[ITGA2]] | C | TIMP1 activity raises ITGA2's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 2.52× lower at baseline in the lines without TIMP1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 2.9); signed map (3.2, 48.4). **Vector** length 108, 40.3% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | +4.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.7 | -0.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.6 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.0 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TIMP metallopeptidase inhibitor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,582,408-47,586,789 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPO; previously TIMP, CLGI |
| Gene groups (HGNC) | Tissue inhibitor of metallopeptidases |
| Hallmark sets | ANGIOGENESIS, COAGULATION, ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, APOPTOSIS, COMPLEMENT, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 16 pathways, smallest: TGFBR3 PTM regulation; Activation of Matrix Metalloproteinases; Interleukin-10 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P01033](https://www.uniprot.org/uniprotkb/P01033) (Metalloproteinase inhibitor 1):

> Metalloproteinase inhibitor that functions by forming one to one complexes with target metalloproteinases, such as collagenases, and irreversibly inactivates them by binding to their catalytic zinc cofactor. Acts on MMP1, MMP2, MMP3, MMP7, MMP8, MMP9, MMP10, MMP11, MMP12, MMP13 and MMP16. Does not act on MMP14. Also functions as a growth factor that regulates cell differentiation, migration and cell death and activates cellular signaling cascades via CD63 and ITGB1. Plays a role in integrin …

**Summary**, from NCBI Gene [7076](https://www.ncbi.nlm.nih.gov/gene/7076):

> This gene belongs to the TIMP gene family. The proteins encoded by this gene family are natural inhibitors of the matrix metalloproteinases (MMPs), a group of peptidases involved in degradation of the extracellular matrix. In addition to its inhibitory role against most of the known MMPs, the encoded protein is able to promote cell proliferation in a wide range of cell types, and may also have an anti-apoptotic function. Transcription of this gene is highly inducible in response to many …

**Accessions** — [HGNC:11820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11820) · Entrez [7076](https://www.ncbi.nlm.nih.gov/gene/7076) · UniProt [P01033](https://www.uniprot.org/uniprotkb/P01033) · Ensembl [ENSG00000102265](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102265)

## Data

Gene col 2231: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2231); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2231, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2231]; `tensor/DDL_lfc|DDL_z.npy` [2231]; `embed/gene_vectors.npy` [2231]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2231 or target_col == 2231). Every well: [[TIMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
