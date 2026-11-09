---
symbol: "B4GALT6"
type: "gene"
col: 3978
ensembl_id: "ENSG00000118276"
name: "beta-1,4-galactosyltransferase 6"
location: "18q12.1"
module: 92
arm: "+"
pooled_cpm: 27.61
n_lines_expressing: 41
n_dd_up: 18
n_dd_down: 39
n_dd_up_clean: 7
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# B4GALT6

*beta-1,4-galactosyltransferase 6* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.46× (z +9.3, q 6e-18, up in 25 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.488× (z -12.1, q 3e-31, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHLDA1]] (+0.70, fdr 7e-06), [[ANTXR2]] (+0.69, fdr 7e-06), [[SPRY4-AS1]] (+0.67, fdr 7e-06); moves opposite to [[C1R]] (-0.58, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CLDN11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +9.3 | 6e-18 | 25/39 (LoVo, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.63×** | +8.2 | 5e-14 | 17/30 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +7.5 | 9e-12 | 23/38 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +6.5 | 8e-09 | 22/38 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.2 | 4e-08 | 20/38 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +6.2 | 4e-08 | 18/38 (NCI-H1792, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.40×** | +5.7 | 1e-06 | 17/38 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.34×** | +5.1 | 3e-05 | 19/38 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 2e-04 | 17/38 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.30×** | +4.3 | 9e-04 | 12/35 (A-172, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.30×** | +4.3 | 9e-04 | 14/34 (C32, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.27×** | +4.2 | 0.001 | 17/38 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **1.27×** | +4.0 | 0.002 | 15/37 (NCI-H460, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.8 | 0.006 | 8/39 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +3.3 | 0.033 | 12/38 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.035 | 7/39 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Ritonavir (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.050 | 2/38 (A-427, AsPC-1) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.082 | 8/39 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 2 with an alert ⚠; shown: the 15 strongest. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3978.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.488×** | -12.1 | 3e-31 | 29/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.589×** | -11.0 | 9e-26 | 32/39 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.539×** | -10.2 | 3e-22 | 28/38 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.578×** | -9.1 | 9e-18 | 28/38 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.667×** | -8.3 | 1e-14 | 28/39 (NCI-H1573, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.634×** | -8.2 | 2e-14 | 29/39 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.629×** | -7.7 | 8e-13 | 22/38 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.665×** | -6.7 | 2e-09 | 22/39 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.758×** | -6.6 | 2e-09 | 23/39 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.768×** | -6.4 | 1e-08 | 22/39 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.687×** | -6.2 | 3e-08 | 20/38 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.681×** | -6.2 | 3e-08 | 20/38 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.714×** | -5.8 | 2e-07 | 19/39 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -5.7 | 5e-07 | 20/39 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -5.5 | 1e-06 | 16/38 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 9 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.126× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 55.0 | 2 | 7 | [[Harringtonine (drug)]] 0.5 µM 4.17× (z +10.5) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.194× (z -12.1) |
| [[RKO (line)]] | wt | 77.3 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 36.3 | 1 (1 ⚠) | 7 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.72× (z +10.1) ⚠ toxic; cell-cycle shift, explains ~24% of this change | [[Binimetinib (drug)]] 5 µM 0.294× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 64.5 | 0 | 4 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.522× (z -17.3) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.319× (z -9.1) |
| [[C32 (line)]] | wt | 49.1 | 0 | 3 | — | [[Trametinib (drug)]] 0.5 µM 0.252× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 23.4 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.96× (z +9.2) | — |
| [[A-427 (line)]] | wt | 97.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.419× (z -9.5) |
| [[LoVo (line)]] | wt | 17.8 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.38× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.386× (z -9.1) |
| [[A498 (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +9.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.113× (z -8.8) |
| [[H4 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -8.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HOP62 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.619× (z -11.0) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 31.3 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.643× (z -10.8) ⚠ position not correctable |
| [[SW48 (line)]] | wt | 47.3 | 1 | 0 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 6.27× (z +8.6) | — |
| [[A-172 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.16 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 73.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHLDA1]] | +0.70 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[IL31RA]] | +0.67 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SPRED1]] | +0.67 | +0.57 / +0.70 | both halves | 8e-06 |  |
| [[NT5E]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ETV4]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[STAMBPL1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ADGRL4]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[LIF]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SPRY2]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[PRDM8]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1R]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity lowers B4GALT6's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.65× higher at baseline in the lines without LOX | 0.015 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[CSF2]] | B | CSF2 activity lowers B4GALT6's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 1.50× higher at baseline in the lines without CSF2 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[ALDH3B1]] | B | ALDH3B1 activity lowers B4GALT6's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 1.78× higher at baseline in the lines without ALDH3B1 | 0.034 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CLDN11]] | B | CLDN11 activity lowers B4GALT6's level | lines that do not express CLDN11 (26) vs lines expressing it (24) | 1.15× higher at baseline in the lines without CLDN11 | 0.068 | ⚠ within organs, on part of the lines; also absent: LAPTM5, SLC25A24P1, CCDC152; maybe low, not absent |
| [[PLAU]] | B | PLAU activity lowers B4GALT6's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.39× higher at baseline in the lines without PLAU | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[CXCL8]] | B | CXCL8 activity lowers B4GALT6's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 1.45× higher at baseline in the lines without CXCL8 | 0.073 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN11]] | B | B4GALT6 activity lowers CLDN11's level | lines that do not express B4GALT6 (9) vs lines expressing it (41) | 2.43× higher at baseline in the lines without B4GALT6 | 0.027 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 8.1); signed map (9.6, 46.5). **Vector** length 123, 33.3% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MAPK output* (control, mean cos +0.60 to 8); *Pre-NOTCH Expression and Processing* (reactome, mean cos +0.52 to 5); *MAPK family signaling cascades* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +4.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.6 | +8.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.4 | +2.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.6 | -12.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -7.6 | -11.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.5 | -8.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.3 | -10.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.1 | -9.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.0 | -8.3 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-galactosyltransferase 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,622,246-31,685,836 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta4GalT-VI |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Reactome | 14 pathways, smallest: N-Glycan antennae elongation; Glycosphingolipid biosynthesis; Keratan sulfate biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBX8](https://www.uniprot.org/uniprotkb/Q9UBX8) (Beta-1,4-galactosyltransferase 6):

> Catalyzes the synthesis of lactosylceramide (LacCer) via the transfer of galactose from UDP-galactose to glucosylceramide (GlcCer). LacCer is the starting point in the biosynthesis of all gangliosides (membrane-bound glycosphingolipids) which play pivotal roles in the CNS including neuronal maturation and axonal and myelin formation (By similarity).

**Summary**, from NCBI Gene [9331](https://www.ncbi.nlm.nih.gov/gene/9331):

> This gene is one of seven beta-1,4-galactosyltransferase (beta4GalT) genes in human. They encode type II membrane-bound glycoproteins that appear to have exclusive specificity for the donor substrate UDP-galactose; all transfer galactose in a beta1,4 linkage to similar acceptor sugars: GlcNAc, Glc, and Xyl. Each beta4GalT has a distinct function in the biosynthesis of different glycoconjugates and saccharide structures. As type II membrane proteins, they have an N-terminal hydrophobic signal …

**Accessions** — [HGNC:929](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:929) · Entrez [9331](https://www.ncbi.nlm.nih.gov/gene/9331) · UniProt [Q9UBX8](https://www.uniprot.org/uniprotkb/Q9UBX8) · Ensembl [ENSG00000118276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118276)

## Data

Gene col 3978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3978); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3978]; `tensor/DDL_lfc|DDL_z.npy` [3978]; `embed/gene_vectors.npy` [3978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3978 or target_col == 3978). Every well: [[B4GALT6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALT6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
