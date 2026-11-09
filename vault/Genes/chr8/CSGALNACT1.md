---
symbol: "CSGALNACT1"
type: "gene"
col: 7179
ensembl_id: "ENSG00000147408"
name: "chondroitin sulfate N-acetylgalactosaminyltransferase 1"
location: "8p21.3"
module: 167
arm: "+"
pooled_cpm: 124.21
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 37
n_dd_up_clean: 3
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# CSGALNACT1

*chondroitin sulfate N-acetylgalactosaminyltransferase 1* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.41× (z +4.7, q 0.002, up in 3 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.24× (z +4.4, q 0.002, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.397× (z -13.0, q 8e-36, down in 21 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KYNU]] (+0.70, fdr 7e-06), [[EYA4]] (+0.66, fdr 1e-05), [[LINC02015]] (+0.65, fdr 7e-06); moves opposite to [[TM4SF19]] (-0.44, fdr 5e-05), [[SGTB]] (-0.42, fdr 9e-05), [[HMOX2]] (-0.42, fdr 1e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PON3]] → it (grade B ⚠); 11 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +4.7 | 0.002 | 3/21 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 0.002 | 2/24 (HOP62, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.4 | 0.002 | 10/23 (HS-578T, PANC-1, …) | top dose only |  |
| [[IQ 1 (drug)]] 5 µM |  | **1.71×** | +4.0 | 0.010 | 12/23 (hTERT-HPNE, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +3.7 | 0.024 | 5/23 (HOP62, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.4 | 0.056 | 10/24 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +3.4 | 0.058 | 6/24 (HS-578T, HOP62, …) | rises with dose |  |
| [[Alpelisib (drug)]] 5 µM |  | 1.53× | +3.1 | 0.12 | 7/23 (SW480, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.14 | 2/24 (HOP62, PANC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.397×** | -13.0 | 8e-36 | 21/23 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.452×** | -11.2 | 2e-26 | 22/23 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.469×** | -10.6 | 4e-24 | 23/23 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.482×** | -10.2 | 2e-22 | 23/23 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.512×** | -9.4 | 7e-19 | 21/23 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.529×** | -8.9 | 4e-17 | 21/23 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -7.8 | 5e-13 | 22/23 (C32, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.401×** | -6.7 | 1e-09 | 21/23 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.402×** | -6.7 | 1e-09 | 23/23 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.609×** | -6.7 | 1e-09 | 16/23 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.670×** | -5.6 | 1e-06 | 17/23 (NCI-H1573, A498, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -5.5 | 2e-06 | 20/23 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.583×** | -5.4 | 3e-06 | 20/23 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.671×** | -5.4 | 3e-06 | 21/22 (NCI-H2030, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.782×** | -4.8 | 5e-05 | 19/23 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.719×** | -4.4 | 3e-04 | 14/23 (COLO 205, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.548×** | -4.4 | 3e-04 | 20/23 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 609 | 0 | 19 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -24.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.136× (z -19.2) |
| [[NCI-H2030 (line)]] | alt | 572 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0914× (z -36.2) |
| [[NCI-H1792 (line)]] | alt | 378 | 1 (1 ⚠) | 15 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +9.6) ⚠ position not correctable | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0815× (z -16.2) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.104× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 509 | 0 | 15 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0948× (z -21.0) |
| [[A498 (line)]] | wt | 118 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 193 | 0 | 14 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0825× (z -19.2) ⚠ toxic; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -17.2) |
| [[COLO 205 (line)]] | alt | 108 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -18.4) |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.103× (z -16.3) |
| [[A549 (line)]] | wt | 540 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.130× (z -14.6) |
| [[BT-474 (line)]] | alt | 108 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.142× (z -12.9) |
| [[C32 (line)]] | wt | 111 | 0 | 9 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.157× (z -15.5) |
| [[SW 900 (line)]] | alt | 98.0 | 0 | 9 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0950× (z -15.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.112× (z -14.7) |
| [[A-427 (line)]] | wt | 190 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.4) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 7 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.104× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.136× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 81.2 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.302× (z -9.1) |
| [[PANC-1 (line)]] | alt | 61.0 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.222× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.198× (z -10.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -9.6) |
| [[HS-578T (line)]] | alt | 125 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -11.4) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 56.4 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +9.5) ⚠ position not correctable | — |
| [[SW 1088 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0694× (z -8.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 16.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 28.1 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.16 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 25.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 9.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 33.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KYNU]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[EYA4]] | +0.66 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[RSPO3]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[BICC1]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[CYP24A1]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[TCIM]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[OLR1]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[CD38]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[GPRIN3]] | +0.56 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[CP]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[AHR]] | +0.54 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TM4SF19]] | -0.44 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[SGTB]] | -0.42 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[HMOX2]] | -0.42 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[KIF21B]] | -0.41 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[PCYT1A]] | -0.41 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[LSM11]] | -0.41 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[ARHGEF2]] | -0.41 | -0.37 / -0.32 | both halves | 2e-04 |  |
| [[C2CD2]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PON3]] | B | PON3 activity raises CSGALNACT1's level | lines that do not express PON3 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without PON3 | 0.054 | ⚠ within organs, on part of the lines; also absent: ESRP2, GOLT1A, ARHGEF5 |
| [[AHR]] | B | AHR activity raises CSGALNACT1's level | lines that do not express AHR (7) vs lines expressing it (43) | 4.15× lower at baseline in the lines without AHR | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises CSGALNACT1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without CYP1B1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[ATP10A]] | C | ATP10A activity raises CSGALNACT1's level | lines that do not express ATP10A (25) vs lines expressing it (25) | 4.29× lower at baseline in the lines without ATP10A | 0.005 | ⚠ within organs, on part of the lines; also absent: STAC, SALL1, TGFBI; co-absent with the target |
| [[FGA]] | C | FGA activity raises CSGALNACT1's level | lines that do not express FGA (43) vs lines expressing it (7) | 5.62× lower at baseline in the lines without FGA | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[LRRK2]] | C | LRRK2 activity raises CSGALNACT1's level | lines that do not express LRRK2 (25) vs lines expressing it (25) | 3.17× lower at baseline in the lines without LRRK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM110B, GFRA1, ADAMTS1; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises CSGALNACT1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 3.64× lower at baseline in the lines without KYNU | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises CSGALNACT1's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 5.83× lower at baseline in the lines without RSPO3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 6, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | CSGALNACT1 activity raises NREP's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 2.68× lower at baseline in the lines without CSGALNACT1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[PTPRM]] | B | CSGALNACT1 activity raises PTPRM's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.90× lower at baseline in the lines without CSGALNACT1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[LINC01239]] | B | CSGALNACT1 activity raises LINC01239's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without CSGALNACT1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[PLD1]] | B | CSGALNACT1 activity raises PLD1's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without CSGALNACT1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[HORMAD1]] | B | CSGALNACT1 activity raises HORMAD1's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without CSGALNACT1 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[PLPP3]] | B | CSGALNACT1 activity raises PLPP3's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 1.72× lower at baseline in the lines without CSGALNACT1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14 |
| [[ATP10A]] | C | CSGALNACT1 activity raises ATP10A's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.58× lower at baseline in the lines without CSGALNACT1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[EBF1]] | C | CSGALNACT1 activity raises EBF1's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.85× lower at baseline in the lines without CSGALNACT1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[KYNU]] | C | CSGALNACT1 activity raises KYNU's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without CSGALNACT1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[EYA4]] | C | CSGALNACT1 activity raises EYA4's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without CSGALNACT1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |
| [[CP]] | C | CSGALNACT1 activity raises CP's level | lines that do not express CSGALNACT1 (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without CSGALNACT1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BCL2A1, ATP10A, FGF14; co-absent with the target |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.1, 22.0); signed map (50.4, 24.9). **Vector** length 122, 41.7% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.7 | -10.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -7.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.9 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | chondroitin sulfate N-acetylgalactosaminyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:19,404,161-19,758,029 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CSGalNAcT-1, FLJ11264, ChGn |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDX6](https://www.uniprot.org/uniprotkb/Q8TDX6) (Chondroitin sulfate N-acetylgalactosaminyltransferase 1):

> Transfers 1,4-N-acetylgalactosamine (GalNAc) from UDP-GalNAc to the non-reducing end of glucuronic acid (GlcUA). Required for addition of the first GalNAc to the core tetrasaccharide linker and for elongation of chondroitin chains. Important role in chondroitin chain biosynthesis in cartilage formation and subsequent endochondral ossification. Moreover, is involved in the metabolism of aggrecan (By similarity).

**Summary**, from NCBI Gene [55790](https://www.ncbi.nlm.nih.gov/gene/55790):

> This gene encodes an enzyme that transfers N-acetylglucosamine (GalNAc) to the core tetrasaccharide linker and to elongating chondroitin sulfate chains in proteoglycans. Knockout of the orthologous mouse gene indicates that the protein is necessary for normal cartilage development and aggrecan metabolism. Mutations in this gene are associated with multiple sclerosis progression, and with mild skeletal dysplasia and joint laxity. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:24290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24290) · Entrez [55790](https://www.ncbi.nlm.nih.gov/gene/55790) · UniProt [Q8TDX6](https://www.uniprot.org/uniprotkb/Q8TDX6) · Ensembl [ENSG00000147408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147408)

## Data

Gene col 7179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7179); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7179]; `tensor/DDL_lfc|DDL_z.npy` [7179]; `embed/gene_vectors.npy` [7179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7179 or target_col == 7179). Every well: [[CSGALNACT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSGALNACT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
