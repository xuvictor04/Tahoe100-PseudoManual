---
symbol: "CA5B"
type: "gene"
col: 9780
ensembl_id: "ENSG00000169239"
name: "carbonic anhydrase 5B"
location: "Xp22.2"
module: 42
arm: "+"
pooled_cpm: 74.57
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# CA5B

*carbonic anhydrase 5B* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.60× (z +11.9, q 1e-29, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.686× (z -12.0, q 4e-30, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOMO2]] (+0.67, fdr 7e-06), [[SEPTIN2]] (+0.63, fdr 7e-06), [[AP2A1]] (+0.59, fdr 1e-05); moves opposite to [[TRIM47]] (-0.63, fdr 2e-05), [[SDSL]] (-0.60, fdr 2e-05), [[METTL18]] (-0.58, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CA5BP1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +11.9 | 1e-29 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +9.4 | 1e-18 | 36/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +8.7 | 6e-16 | 35/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +7.9 | 3e-13 | 34/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.6 | 2e-06 | 24/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.20×** | +4.7 | 3e-04 | 19/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.008 | 14/48 (MIA PaCa-2, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.9 | 0.008 | 18/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.014 | 11/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.015 | 20/47 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.019 | 17/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.033 | 20/49 (C-33 A, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.051 | 8/48 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.26× | +3.0 | 0.10 | 17/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9780.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.686×** | -12.0 | 4e-30 | 31/48 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -7.8 | 2e-12 | 27/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -6.4 | 2e-08 | 26/48 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.792×** | -5.9 | 5e-07 | 28/49 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.863× | -4.9 | 1e-04 | 20/48 (HS-578T, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -4.2 | 0.002 | 18/49 (SNU-1, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.854× | -3.8 | 0.010 | 20/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -3.7 | 0.018 | 13/48 (NCI-H1792, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | 0.862× | -3.5 | 0.034 | 20/45 (NCI-H2030, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.875× | -3.4 | 0.043 | 15/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~42% of this change | 0.882× | -3.2 | 0.074 | 15/47 (H4, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +16.9) | — |
| [[LoVo (line)]] | wt | 60.7 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 85.3 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 191 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 51.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 87.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.468× (z -8.5) |
| [[HS-578T (line)]] | alt | 123 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 51.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.349× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 54.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -12.4) |
| [[RKO (line)]] | wt | 74.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -11.9) |
| [[A498 (line)]] | wt | 73.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 75.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.298× (z -9.0) |
| [[HCT15 (line)]] | alt | 59.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -8.7) |
| [[HOP62 (line)]] | alt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.4) |
| [[Hs 766T (line)]] | wt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 91.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 47.2 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.50× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 47.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 74.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 67.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -13.1) |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 95.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.0) |
| [[SW480 (line)]] | alt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.579× (z -11.7) |
| [[A-172 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOMO2]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SEPTIN2]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[AP2A1]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TCTN3]] | +0.59 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[P4HB]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[OSTC]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC31A1]] | +0.59 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[GET1]] | +0.57 | +0.62 / +0.38 | both halves | 7e-05 |  |
| [[NOMO1]] | +0.57 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SEL1L]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[MLEC]] | +0.57 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[TXNDC12]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM47]] | -0.63 | -0.66 / -0.47 | both halves | 2e-05 |  |
| [[SDSL]] | -0.60 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[METTL18]] | -0.58 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[PIGV]] | -0.57 | -0.67 / -0.26 | both halves | 4e-04 |  |
| [[ZNF155]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[LACC1]] | -0.56 | -0.68 / -0.31 | both halves | 2e-04 |  |
| [[ANOS2P]] | -0.55 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[CFLAR-AS1]] | -0.55 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[ZNF620]] | -0.55 | -0.67 / -0.34 | both halves | 1e-04 |  |
| [[USP27X]] | -0.55 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.55 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NANOS3]] | -0.55 | -0.61 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA5BP1]] | C | CA5BP1's natural level strengthens CA5B's drug response | CA5BP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.56; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.1, 9.8); signed map (-58.1, 6.7). **Vector** length 93.6, 20.6% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.3 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.1 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +3.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.7 | +1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.5 | -12.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -6.5 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | carbonic anhydrase 5B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:15,688,830-15,788,411 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Carbonic anhydrases |
| Reactome | 1 pathways, smallest: Reversible hydration of carbon dioxide |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D0](https://www.uniprot.org/uniprotkb/Q9Y2D0) (Carbonic anhydrase 5B, mitochondrial):

> Mitochondrial carbonic anhydrase that catalyzes the reversible conversion of carbon dioxide to bicarbonate/HCO3.

**Summary**, from NCBI Gene [11238](https://www.ncbi.nlm.nih.gov/gene/11238):

> Carbonic anhydrases (CAs) are a large family of zinc metalloenzymes that catalyze the reversible hydration of carbon dioxide. They participate in a variety of biological processes, including respiration, calcification, acid-base balance, bone resorption, and the formation of aqueous humor, cerebrospinal fluid, saliva, and gastric acid. They show extensive diversity in tissue distribution and in their subcellular localization. This gene encodes carbonic anhydrase 5B. CA5B, and the related CA5A …

**Accessions** — [HGNC:1378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1378) · Entrez [11238](https://www.ncbi.nlm.nih.gov/gene/11238) · UniProt [Q9Y2D0](https://www.uniprot.org/uniprotkb/Q9Y2D0) · Ensembl [ENSG00000169239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169239)

## Data

Gene col 9780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9780); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9780]; `tensor/DDL_lfc|DDL_z.npy` [9780]; `embed/gene_vectors.npy` [9780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9780 or target_col == 9780). Every well: [[CA5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
