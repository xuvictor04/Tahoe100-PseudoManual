---
symbol: "PPP2R5C"
type: "gene"
col: 1217
ensembl_id: "ENSG00000078304"
name: "protein phosphatase 2 regulatory subunit B'gamma"
location: "14q32.31"
module: 32
arm: "+"
pooled_cpm: 176.21
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PPP2R5C

*protein phosphatase 2 regulatory subunit B'gamma* — 14q32.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 1.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 1.58×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 1.81×; ⚠ cell-cycle shift, explains <1% of this change).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.800× (z -11.1, q 1e-25, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STN1]] (+0.54, fdr 1e-04), [[TBC1D8]] (+0.54, fdr 2e-05), [[LINC02320]] (+0.51, fdr 2e-05, ⚠ same locus), [[ARHGAP12]] (+0.50, fdr 3e-05); moves opposite to [[DENND5A]] (-0.51, fdr 7e-04), [[IFIT5]] (-0.51, fdr 5e-05), [[ZBTB21]] (-0.51, fdr 3e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1217.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (HEC-1-A 1.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW48 1.58×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW48 1.81×; ⚠ cell-cycle shift, explains <1% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +5.8 | 4e-06 | 15/48 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.5 | 0.002 | 10/49 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.13× | +4.4 | 0.002 | 16/48 (SW48, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.9 | 0.012 | 14/48 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.12× | +3.9 | 0.012 | 7/47 (SW480, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.10× | +3.4 | 0.074 | 13/48 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.19× | +3.3 | 0.084 | 18/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | 1.18× | +3.1 | 0.14 | 8/48 (NCI-H460, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.09× | +3.0 | 0.16 | 1/48 (SW 1271) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1217.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.800×** | -11.1 | 1e-25 | 27/48 (AN3 CA, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.818×** | -10.0 | 5e-21 | 26/49 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~11% of this change | **0.801×** | -7.5 | 1e-11 | 26/47 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.831×** | -6.5 | 1e-08 | 23/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.831×** | -6.5 | 1e-08 | 22/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.837× | -6.0 | 2e-07 | 22/48 (NCI-H1573, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.861× | -5.2 | 1e-05 | 16/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.865× | -5.1 | 2e-05 | 16/48 (NCI-H460, CFPAC-1, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.764×** | -4.9 | 5e-05 | 22/48 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -4.6 | 2e-04 | 17/48 (LoVo, A498, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.779×** | -4.6 | 2e-04 | 22/49 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.878× | -4.6 | 2e-04 | 10/47 (LS 180, HepG2/C3A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -4.5 | 4e-04 | 18/48 (A498, CFPAC-1, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.797×** | -4.2 | 0.001 | 18/48 (LoVo, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | 0.885× | -4.1 | 0.002 | 18/44 (SW48, LoVo, …) | all doses, flat | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.914× | -3.7 | 0.008 | 7/48 (NCI-H460, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.009 | 19/48 (LoVo, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.047 | 9/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 220 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -16.2) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.576× (z -12.1) |
| [[LoVo (line)]] | wt | 249 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 187 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -18.5) |
| [[NCI-H1573 (line)]] | alt | 217 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -16.5) |
| [[SW48 (line)]] | wt | 296 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[SW480 (line)]] | alt | 274 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.500× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A498 (line)]] | wt | 98.7 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.570× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 176 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.517× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.639× (z -10.0) |
| [[AN3 CA (line)]] | alt | 195 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -21.8) |
| [[AsPC-1 (line)]] | alt | 187 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -14.8) |
| [[COLO 205 (line)]] | alt | 149 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.558× (z -9.8) |
| [[HT-29 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -9.3) |
| [[KATO III (line)]] | alt | 176 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.566× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[LS 180 (line)]] | wt | 378 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.9) ⚠ cell-cycle shift, explains ~7% of this change |
| [[MIA PaCa-2 (line)]] | alt | 205 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.580× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~11% of this change |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[Panc 03.27 (line)]] | alt | 221 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.546× (z -11.1) |
| [[SW 1088 (line)]] | alt | 166 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.05 µM 0.139× (z -9.3) |
| [[A-172 (line)]] | wt | 97.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 143 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 149 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 156 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 209 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STN1]] | +0.54 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TBC1D8]] | +0.54 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[LINC02320]] | +0.51 | +0.53 / +0.48 | both halves | 2e-05 | ⚠ same locus (30.6 kb: neighbours can correlate without regulation) |
| [[ARHGAP12]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[GLG1]] | +0.48 | +0.57 / +0.37 | both halves | 9e-05 |  |
| [[NDUFB6]] | +0.48 | +0.47 / +0.34 | both halves | 1e-04 |  |
| [[MARF1]] | +0.48 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[GMCL1]] | +0.47 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[SMARCD2]] | +0.47 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[DCAF7]] | +0.47 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[IGFBP4]] | +0.47 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[CKLF]] | +0.47 | +0.57 / +0.22 | both halves | 6e-04 |  |
| [[ABHD2]] | +0.46 | +0.42 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5A]] | -0.51 | -0.21 / -0.54 | both halves | 7e-04 |  |
| [[IFIT5]] | -0.51 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ZBTB21]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[GPR158]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RASGRP3]] | -0.50 | -0.46 / -0.42 | both halves | 4e-05 | pathway: MAPK family signaling cascades |
| [[MB21D2]] | -0.50 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ZNFX1]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[PHF11]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[CLIP1]] | -0.48 | -0.54 / -0.35 | both halves | 1e-04 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| [[SAMD9]] | -0.48 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[RSAD2]] | -0.48 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[PARP14]] | -0.48 | -0.51 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises PPP2R5C's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.37× lower at baseline in the lines without LINC02320 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[HMOX1]] | B | HMOX1 activity lowers PPP2R5C's level | lines that do not express HMOX1 (9) vs lines expressing it (41) | 1.30× higher at baseline in the lines without HMOX1 | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[RFTN1]] | B | RFTN1 activity lowers PPP2R5C's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 1.29× higher at baseline in the lines without RFTN1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction -0.410). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, -2.4); signed map (-13.0, 49.6). **Vector** length 110, 27.7% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.7 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +5.9 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | +5.0 | -4.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.8 | +3.9 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +2.1 | +0.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -11.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.4 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | -1.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.5 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.4 | -1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit B'gamma |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.31 — chr14:101,761,709-101,927,989 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B56G, PR61G, B56gamma |
| Gene groups (HGNC) | Protein phosphatase 2 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 56 pathways, smallest: APC truncation mutants have impaired AXIN binding; AXIN missense mutants destabilize the destruction complex; Signaling by AMER1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13362](https://www.uniprot.org/uniprotkb/Q13362) (Serine/threonine-protein phosphatase 2A 56 kDa regulatory subunit gamma isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment. The PP2A-PPP2R5C holoenzyme may specifically dephosphorylate and activate TP53 and play a role in DNA damage-induced inhibition of cell proliferation. PP2A-PPP2R5C may also regulate the ERK signaling pathway through ERK dephosphorylation.

**Summary**, from NCBI Gene [5527](https://www.ncbi.nlm.nih.gov/gene/5527):

> The product of this gene belongs to the phosphatase 2A regulatory subunit B family. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9311) · Entrez [5527](https://www.ncbi.nlm.nih.gov/gene/5527) · UniProt [Q13362](https://www.uniprot.org/uniprotkb/Q13362) · Ensembl [ENSG00000078304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078304)

## Data

Gene col 1217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1217); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1217]; `tensor/DDL_lfc|DDL_z.npy` [1217]; `embed/gene_vectors.npy` [1217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1217 or target_col == 1217). Every well: [[PPP2R5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
