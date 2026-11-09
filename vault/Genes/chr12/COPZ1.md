---
symbol: "COPZ1"
type: "gene"
col: 3236
ensembl_id: "ENSG00000111481"
name: "coat protein complex I subunit zeta 1"
location: "12q13.13"
module: 42
arm: "+"
pooled_cpm: 54.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# COPZ1

*coat protein complex I subunit zeta 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +18.4, q 0e+00, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +6.7, q 4e-09, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.710× (z -7.0, q 2e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF6]] (+0.67, fdr 7e-06), [[LSM1]] (+0.67, fdr 1e-05), [[NDUFS1]] (+0.60, fdr 1e-05); moves opposite to [[RGS19]] (-0.59, fdr 3e-05), [[TMCO6]] (-0.57, fdr 3e-05), [[METAP1]] (-0.55, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +18.4 | 0e+00 | 45/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +15.4 | 0e+00 | 39/40 (A-427, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +9.4 | 8e-19 | 34/44 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.7 | 4e-09 | 24/48 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +6.6 | 5e-09 | 31/48 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.32×** | +5.7 | 1e-06 | 26/47 (NCI-H1573, A-427, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +5.1 | 3e-05 | 27/48 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~50% of this change | **1.24×** | +4.4 | 1e-03 | 25/47 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.22×** | +4.0 | 0.004 | 18/48 (NCI-H23, A498, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.007 | 19/47 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.6 | 0.015 | 13/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.17× | +3.2 | 0.072 | 18/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.17× | +3.1 | 0.098 | 20/48 (COLO 205, NCI-H23, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.710×** | -7.0 | 2e-09 | 29/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.757×** | -5.7 | 4e-06 | 26/48 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.831×** | -5.3 | 2e-05 | 23/48 (NCI-H1573, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.815×** | -4.2 | 0.004 | 21/48 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 0.879× | -3.7 | 0.022 | 13/48 (NCI-H460, HOP62, …) | top dose only | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.841× | -3.3 | 0.071 | 17/47 (Panc 03.27, SW48, …) | inconsistent across doses |  |
| [[Adenine (drug)]] 5 µM |  | 0.891× | -3.3 | 0.071 | 8/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.685× | -3.2 | 0.11 | 11/48 (CHP-212, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 37.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 60.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +8.5) | — |
| [[A-427 (line)]] | wt | 55.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 65.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.7) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 39.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 39.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 52.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.42× (z +9.7) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 56.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +9.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 36.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 63.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +11.7) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 133 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 51.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +10.9) | — |
| [[NCI-H460 (line)]] | wt | 52.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +11.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 44.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 46.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 67.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +13.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.133× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 56.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.477× (z -8.8) |
| [[Hs 766T (line)]] | wt | 54.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 95.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +10.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 48.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 47.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.28× (z +14.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 38.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.94× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 49.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.90× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF6]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[LSM1]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[NDUFS1]] | +0.60 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[PCGF3-AS1]] | +0.59 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.59 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SLC35B1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[C9orf85]] | +0.57 | +0.60 / +0.33 | both halves | 1e-04 |  |
| [[ZBTB8OS]] | +0.56 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PHC3]] | +0.56 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[MCTS1]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZNF547]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[COPB2]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 999 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS19]] | -0.59 | -0.52 / -0.44 | both halves | 3e-05 | same gene group |
| [[TMCO6]] | -0.57 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[METAP1]] | -0.55 | -0.51 / -0.47 | both halves | 2e-05 | same gene group |
| [[PAFAH1B3]] | -0.53 | -0.52 / -0.40 | both halves | 5e-05 | pathway: Golgi-to-ER retrograde transport |
| [[PAQR4]] | -0.52 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[RCL1]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 | same gene group |
| [[INPP5F]] | -0.51 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[GNAZ]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[FANCE]] | -0.51 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[SMG1P2]] | -0.50 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[B3GNT2]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 | same gene group |
| [[BTBD3]] | -0.50 | -0.46 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises COPZ1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises COPZ1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.250). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.9, -10.4); signed map (-6.0, -11.9). **Vector** length 81.7, 18.6% of its response variance represented; |z| ≥ 3 in 687 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +5.2 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +18.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +15.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +0.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.0 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | -0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | -1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -5.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -0.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | +0.0 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coat protein complex I subunit zeta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,301,202-54,351,846 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-120; previously COPZ |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Coat protein complex I |
| Reactome | 9 pathways, smallest: COPI-dependent Golgi-to-ER retrograde traffic; COPI-mediated anterograde transport; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P61923](https://www.uniprot.org/uniprotkb/P61923) (Coatomer subunit zeta-1):

> Component of the coatomer complex, involved in retrograde Golgi-to-ER transport. The coatomer is a cytosolic protein complex that binds to dilysine motifs and reversibly associates with Golgi non-clathrin-coated vesicles, which further mediate biosynthetic protein transport from the ER, via the Golgi up to the trans Golgi network. Coatomer complex is required for budding from Golgi membranes, and is essential for the retrograde Golgi-to-ER transport of dilysine-tagged proteins (By similarity). …

**Summary**, from NCBI Gene [22818](https://www.ncbi.nlm.nih.gov/gene/22818):

> This gene encodes a subunit of the cytoplasmic coatamer protein complex, which is involved in autophagy and intracellular protein trafficking. The coatomer protein complex is comprised of seven subunits and functions as the coat protein of coat protein complex (COP)I-vesicles. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:2243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2243) · Entrez [22818](https://www.ncbi.nlm.nih.gov/gene/22818) · UniProt [P61923](https://www.uniprot.org/uniprotkb/P61923) · Ensembl [ENSG00000111481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111481)

## Data

Gene col 3236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3236); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3236]; `tensor/DDL_lfc|DDL_z.npy` [3236]; `embed/gene_vectors.npy` [3236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3236 or target_col == 3236). Every well: [[COPZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
