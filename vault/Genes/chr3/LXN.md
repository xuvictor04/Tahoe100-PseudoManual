---
symbol: "LXN"
type: "gene"
col: 1246
ensembl_id: "ENSG00000079257"
name: "latexin"
location: "3q25.32"
module: 8
arm: "+"
pooled_cpm: 11.85
n_lines_expressing: 31
n_dd_up: 5
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LXN

*latexin* — 3q25.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.19× (z +9.4, q 4e-18, up in 5 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.48× (z +6.9, q 1e-09, up in 15 of 28 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 7.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 6.93×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.493× (z -8.8, q 1e-15, down in 21 of 27 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UPK1B]] (+0.56, fdr 2e-05), [[AGR2]] (+0.52, fdr 1e-04), [[SYTL2]] (+0.51, fdr 4e-05); moves opposite to [[LDLRAD3]] (-0.47, fdr 4e-05), [[ABLIM3]] (-0.44, fdr 1e-04), [[PXYLP1]] (-0.43, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HMGN2P46]] → it (grade B ⚠); 8 go from it, the strongest it → [[RIN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1246.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 7.74×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 6.93×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +9.4 | 4e-18 | 5/12 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.85×** | +7.6 | 7e-12 | 8/21 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +6.9 | 1e-09 | 15/28 (AsPC-1, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +6.8 | 1e-09 | 10/19 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.049 | 2/26 (J82, A549) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.23 | 7/28 (A498, AsPC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.493×** | -8.8 | 1e-15 | 21/27 (NCI-H460, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -7.9 | 1e-12 | 23/27 (NCI-H460, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.666×** | -5.0 | 9e-05 | 13/28 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.708×** | -4.3 | 0.003 | 12/27 (BT-474, J82, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.035 | 16/26 (NCI-H1573, BT-474, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.612× | -3.1 | 0.16 | 12/27 (hTERT-HPNE, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.782× | -3.0 | 0.16 | 7/27 (BT-474, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | 0.784× | -3.0 | 0.16 | 7/27 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.6 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -23.1) |
| [[BT-474 (line)]] | alt | 51.5 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0936× (z -10.9) |
| [[H4 (line)]] | wt | 10.9 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0564× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.172× (z -8.5) |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 22.4 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0700× (z -10.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -9.0) |
| [[PANC-1 (line)]] | alt | 18.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.74× (z +11.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0876× (z -11.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -8.5) |
| [[A-172 (line)]] | wt | 2.29 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UPK1B]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 | **novel candidate** |
| [[AGR2]] | +0.52 | +0.50 / +0.34 | both halves | 1e-04 |  |
| [[SYTL2]] | +0.51 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[TM4SF4]] | +0.51 | +0.47 / +0.40 | both halves | 4e-05 |  |
| [[TSPAN1]] | +0.50 | +0.46 / +0.32 | both halves | 2e-04 |  |
| [[EDIL3]] | +0.50 | +0.43 / +0.44 | both halves | 3e-05 |  |
| [[PLA2R1]] | +0.49 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[ITGB6]] | +0.48 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[LURAP1]] | +0.47 | +0.45 / +0.37 | both halves | 9e-05 |  |
| [[TRIM31]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[WDR72]] | +0.47 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[RARRES1]] | +0.46 | +0.39 / +0.45 | both halves | 5e-05 | ⚠ same locus (24.2 kb, same strand: neighbours can correlate without regulation) |
| [[RBM47]] | +0.46 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDLRAD3]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[ABLIM3]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[PXYLP1]] | -0.43 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[BCL2L1]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[TMEM164]] | -0.42 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[SHLD2]] | -0.42 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[TRMT6]] | -0.41 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[EXOSC7]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[MOSMO]] | -0.41 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[SYNE3]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[RTN4RL1]] | -0.40 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[ERGIC1]] | -0.40 | -0.31 / -0.45 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN2P46]] | B | HMGN2P46 activity raises LXN's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without HMGN2P46 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[SYTL2]] | B | SYTL2 activity raises LXN's level | lines that do not express SYTL2 (7) vs lines expressing it (43) | 1.99× lower at baseline in the lines without SYTL2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[SMOC1]] | B | SMOC1 activity raises LXN's level | lines that do not express SMOC1 (34) vs lines expressing it (16) | 1.70× lower at baseline in the lines without SMOC1 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CPLX2, LGSN, CYP24A1 |
| [[RBPMS]] | B | RBPMS activity raises LXN's level | lines that do not express RBPMS (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without RBPMS | 0.083 | ⚠ within organs, on part of the lines; also absent: FES, DGKG, CADPS2 |
| [[RIN2]] | B | RIN2 activity raises LXN's level | lines that do not express RIN2 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without RIN2 | 0.083 | ⚠ within organs, on part of the lines; also absent: ANTXR2; maybe low, not absent |
| [[AGR2]] | B | AGR2 activity raises LXN's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without AGR2 | 0.086 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RIN2]] | B | LXN activity raises RIN2's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.48× lower at baseline in the lines without LXN | 0.020 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[SMOC1]] | B | LXN activity raises SMOC1's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.56× lower at baseline in the lines without LXN | 0.020 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[AGR2]] | B | LXN activity raises AGR2's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.33× lower at baseline in the lines without LXN | 0.029 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[RIN2]] | B | LXN activity strengthens RIN2's drug response | lines that do not express LXN (13) vs lines expressing it (26) | the lines without LXN respond 0.74× as strongly (z diff +1.85); strongest at Bortezomib 0.05 µM: 0.55x vs 0.37x (z diff +3.1) | 0.035 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AHR]] | B | LXN activity raises AHR's level | lines that do not express LXN (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without LXN | 0.041 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[RBPMS]] | B | LXN activity raises RBPMS's level | lines that do not express LXN (19) vs lines expressing it (31) | 1.93× lower at baseline in the lines without LXN | 0.060 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[ATP1B1]] | B | LXN activity raises ATP1B1's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.12× lower at baseline in the lines without LXN | 0.078 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |
| [[SMIM31]] | B | LXN activity raises SMIM31's level | lines that do not express LXN (19) vs lines expressing it (31) | 2.00× lower at baseline in the lines without LXN | 0.092 | ⚠ within organs, on part of the lines; also absent: GPX3, CYP4F11, SLPI; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.410). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.6, 59.4); signed map (63.8, -0.0). **Vector** length 70.9, 16.6% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +6.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +1.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | latexin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.32 — chr3:158,645,822-158,672,648 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BS40](https://www.uniprot.org/uniprotkb/Q9BS40) (Latexin):

> Hardly reversible, non-competitive, and potent inhibitor of CPA1, CPA2 and CPA4. May play a role in inflammation.

**Summary**, from NCBI Gene [56925](https://www.ncbi.nlm.nih.gov/gene/56925):

> This gene encodes the only known protein inhibitor of zinc-dependent metallocarboxypeptidases. The encoded protein, latexin, downregulates the population size of hematopoietic stem cells. This protein is found to be downregulated in cancer cells because of promoter hypermethylation. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:13347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13347) · Entrez [56925](https://www.ncbi.nlm.nih.gov/gene/56925) · UniProt [Q9BS40](https://www.uniprot.org/uniprotkb/Q9BS40) · Ensembl [ENSG00000079257](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079257)

## Data

Gene col 1246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1246); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1246]; `tensor/DDL_lfc|DDL_z.npy` [1246]; `embed/gene_vectors.npy` [1246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1246 or target_col == 1246). Every well: [[LXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
