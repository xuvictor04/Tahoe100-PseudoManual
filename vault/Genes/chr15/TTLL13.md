---
symbol: "TTLL13"
type: "gene"
col: 13108
ensembl_id: "ENSG00000213471"
name: "tubulin tyrosine ligase like 13"
location: "15q26.1"
module: 38
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# TTLL13

*tubulin tyrosine ligase like 13* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.42× (z +7.6, q 1e-11, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.281× (z -11.0, q 3e-25, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDPGP1]] (+0.75, fdr 7e-06, ⚠ same locus), [[PDE2A]] (+0.72, fdr 7e-06), [[PYGM]] (+0.71, fdr 7e-06), [[SMIM41]] (+0.71, fdr 7e-06); moves opposite to [[CASD1]] (-0.56, fdr 4e-05), [[NNT]] (-0.54, fdr 2e-05), [[ZMYND11]] (-0.54, fdr 3e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SRMS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +7.6 | 1e-11 | 30/45 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.39×** | +7.5 | 2e-11 | 30/46 (A498, HOP62, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +6.8 | 3e-09 | 24/44 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.10×** | +6.4 | 2e-08 | 22/45 (CFPAC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.8 | 6e-07 | 22/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +5.1 | 3e-05 | 16/39 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.75×** | +4.8 | 1e-04 | 18/45 (A498, A-172, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.006 | 13/35 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.49×** | +3.5 | 0.035 | 6/37 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13108.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.281×** | -11.0 | 3e-25 | 38/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.293×** | -10.6 | 7e-24 | 32/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.377×** | -8.5 | 5e-15 | 28/33 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -7.7 | 2e-12 | 25/38 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.421×** | -7.2 | 6e-11 | 21/26 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.438×** | -6.9 | 6e-10 | 30/40 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -6.7 | 2e-09 | 25/44 (LOX-IMVI, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.469×** | -6.6 | 4e-09 | 25/41 (NCI-H1792, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.554×** | -5.1 | 2e-05 | 22/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.565×** | -5.0 | 4e-05 | 20/36 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.670×** | -4.9 | 5e-05 | 14/44 (HEC-1-A, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.575×** | -4.8 | 8e-05 | 14/45 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -4.5 | 4e-04 | 14/39 (A549, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.609×** | -4.3 | 7e-04 | 16/41 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.586×** | -4.3 | 7e-04 | 14/44 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.403×** | -4.1 | 0.001 | 14/32 (COLO 205, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.1 | 0.002 | 16/42 (HEC-1-A, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 26.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -12.4) |
| [[LoVo (line)]] | wt | 16.1 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0679× (z -12.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0955× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 6.23 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -11.3) |
| [[A498 (line)]] | wt | 3.23 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0718× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 7.52 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0467× (z -10.7) |
| [[A549 (line)]] | wt | 8.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0271× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 3.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0390× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 7.07 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0642× (z -8.8) |
| [[PANC-1 (line)]] | alt | 4.19 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0424× (z -13.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 6.10 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0657× (z -8.7) |
| [[A-172 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDPGP1]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 | ⚠ same locus (3.7 kb, same strand: neighbours can correlate without regulation) |
| [[PDE2A]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[PYGM]] | +0.71 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.71 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ADORA1]] | +0.70 | +0.58 / +0.80 | both halves | 7e-06 |  |
| [[TINCR]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[HAP1]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[PRKCG]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ASIC4]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.66 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[COL20A1]] | +0.65 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GP6]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[A3GALT2]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | -0.56 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[NNT]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ZMYND11]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[ZNF253]] | -0.54 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[DMAC2L]] | -0.53 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PTAR1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MTHFSD]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | SRMS activity raises TTLL13's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.62× lower at baseline in the lines without SRMS | 0.010 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[TFF1]] | B | TFF1 activity raises TTLL13's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 1.77× lower at baseline in the lines without TFF1 | 0.015 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TTLL13's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers TTLL13's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PTK6]] | B | PTK6 activity raises TTLL13's level | lines that do not express PTK6 (17) vs lines expressing it (33) | 1.62× lower at baseline in the lines without PTK6 | 0.078 | ⚠ within organs, on part of the lines; also absent: CDCP1, EVPL, PKP3; maybe low, not absent |
| [[GDPGP1]] | C | GDPGP1's natural level strengthens TTLL13's drug response | GDPGP1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.68, reverse +0.52; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.5, -18.4); signed map (14.7, 13.7). **Vector** length 87.3, 17.6% of its response variance represented; |z| ≥ 3 in 1,217 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.3 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.7 | +3.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.8 | -11.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -10.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.6 | -6.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -2.2 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,249,530-90,265,482 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46079, MGC33417; previously TTLL13P |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NNM8](https://www.uniprot.org/uniprotkb/A6NNM8) (Tubulin polyglutamylase TTLL13):

> Polyglutamylase which modifies tubulin, generating polyglutamate side chains of variable lengths on the gamma-carboxyl group of specific glutamate residues within the C-terminal tail of tubulin. Mediates ATP-dependent polyglutamate side-chain elongation of the polyglutamylation reaction but not the initiation step (By similarity). Preferentially modifies the alpha-tubulin tail over a beta-tail (By similarity). Mediates spindle-pole microtubule glutamylation in a CFAP100-dependent manner, a …

**Summary**, from NCBI Gene [440307](https://www.ncbi.nlm.nih.gov/gene/440307):

> Predicted to enable tubulin binding activity and tubulin-glutamic acid ligase activity. Predicted to be involved in microtubule bundle formation. Predicted to be located in cytosol. Predicted to be active in ciliary basal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32484) · Entrez [440307](https://www.ncbi.nlm.nih.gov/gene/440307) · UniProt [A6NNM8](https://www.uniprot.org/uniprotkb/A6NNM8) · Ensembl [ENSG00000213471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213471)

## Data

Gene col 13108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13108); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13108]; `tensor/DDL_lfc|DDL_z.npy` [13108]; `embed/gene_vectors.npy` [13108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13108 or target_col == 13108). Every well: [[TTLL13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
