---
symbol: "SFT2D1"
type: "gene"
col: 12690
ensembl_id: "ENSG00000198818"
name: "SFT2 domain containing 1"
location: "6q27"
module: 0
arm: null
pooled_cpm: 44.97
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene"]
generated_by: "tahoemap"
---

# SFT2D1

*SFT2 domain containing 1* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.35× (z +6.7, q 1e-08, up in 27 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.28× (z +5.6, q 5e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.602× (z -16.2, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK4]] (+0.61, fdr 1e-05), [[LINC03009-1]] (+0.59, fdr 7e-06), [[PMPCA]] (+0.57, fdr 9e-06); moves opposite to [[CCT6P3]] (-0.55, fdr 1e-05), [[KMT2A]] (-0.54, fdr 1e-05), [[DMXL1]] (-0.53, fdr 3e-05).
> Its neighbourhood forms no module of 5 or more genes (module 0, unassigned).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +6.7 | 1e-08 | 27/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.6 | 5e-06 | 25/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +5.1 | 7e-05 | 25/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +4.8 | 2e-04 | 22/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.3 | 0.002 | 20/48 (SW480, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.13× | +3.8 | 0.016 | 13/48 (J82, Hs 766T, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.2 | 0.10 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 4 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.602×** | -16.2 | 0e+00 | 36/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -10.9 | 4e-25 | 40/48 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.639×** | -10.1 | 1e-21 | 37/48 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -9.9 | 7e-21 | 37/48 (KATO III, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.671×** | -9.0 | 2e-17 | 34/48 (KATO III, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.695×** | -8.2 | 2e-14 | 35/48 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.733×** | -7.7 | 8e-13 | 33/49 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.710×** | -7.7 | 8e-13 | 31/49 (A-427, NCI-H23, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -7.7 | 9e-13 | 37/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.792×** | -6.6 | 2e-09 | 30/48 (AsPC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -6.5 | 6e-09 | 25/48 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.756×** | -5.9 | 2e-07 | 26/48 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.771×** | -5.7 | 6e-07 | 26/47 (SW48, A-172, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.771×** | -5.7 | 6e-07 | 26/47 (A-427, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.779×** | -5.7 | 6e-07 | 25/47 (HOP62, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 59.4 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.611× (z -9.5) |
| [[KATO III (line)]] | alt | 59.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 42.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.8) |
| [[RKO (line)]] | wt | 76.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.374× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 48.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -13.8) |
| [[HT-29 (line)]] | alt | 45.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.5) |
| [[LoVo (line)]] | wt | 52.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.7) |
| [[LS 180 (line)]] | wt | 63.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 47.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.316× (z -10.3) |
| [[SW48 (line)]] | wt | 58.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -10.7) |
| [[A498 (line)]] | wt | 28.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -13.9) |
| [[A549 (line)]] | wt | 37.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.8) |
| [[AN3 CA (line)]] | alt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -8.8) |
| [[C32 (line)]] | wt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -9.1) |
| [[COLO 205 (line)]] | alt | 43.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 45.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.499× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.2) |
| [[SHP-77 (line)]] | alt | 48.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[SK-MEL-2 (line)]] | alt | 41.9 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0924× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.208× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[SNU-423 (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -10.8) |
| [[SW 1271 (line)]] | alt | 55.9 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0534× (z -11.2) |
| [[A-172 (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK4]] | +0.61 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[LINC03009-1]] | +0.59 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[PMPCA]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[SPRED2]] | +0.57 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[STARD3]] | +0.56 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[VPS37B]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[IPPK]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SDF2]] | +0.55 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[PDCD6]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZFYVE27]] | +0.54 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MOAP1]] | +0.53 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[AP1S1]] | +0.52 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6P3]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[KMT2A]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[DMXL1]] | -0.53 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[LGALS3]] | -0.50 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TTBK2]] | -0.50 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MAP4K5]] | -0.49 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[LRRC37A2]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[CFL2]] | -0.49 | -0.65 / -0.40 | both halves | 4e-05 |  |
| [[SETD2]] | -0.48 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[FYTTD1]] | -0.48 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[KIF13A]] | -0.48 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[TAOK1]] | -0.46 | -0.44 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SFT2D1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ITPRIP]] | B | ITPRIP activity raises SFT2D1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.21× lower at baseline in the lines without ITPRIP | 0.089 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[RHOU]] | B | RHOU activity lowers SFT2D1's level | lines that do not express RHOU (9) vs lines expressing it (41) | 1.20× higher at baseline in the lines without RHOU | 0.099 | ⚠ within organs, on part of the lines; also absent: JAKMIP3, HAP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: none (module 0: its neighbourhood formed no community of ≥ 5 genes).
- **Nodal map** (x, y) = (16.4, -22.5); signed map (-44.5, 20.7). **Vector** length 95.0, 21.6% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +6.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.8 | +5.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.2 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -0.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.8 | +1.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.7 | -7.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.3 | -7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.1 | -16.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -9.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.5 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -7.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.9 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | SFT2 domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,319,728-166,342,576 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC19825, pRGR1; previously C6orf83 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV19](https://www.uniprot.org/uniprotkb/Q8WV19) (Vesicle transport protein SFT2A):

> May be involved in fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex.

**Summary**, from NCBI Gene [113402](https://www.ncbi.nlm.nih.gov/gene/113402):

> Predicted to be involved in protein transport and vesicle-mediated transport. Predicted to be located in cytoplasm; endomembrane system; and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21102) · Entrez [113402](https://www.ncbi.nlm.nih.gov/gene/113402) · UniProt [Q8WV19](https://www.uniprot.org/uniprotkb/Q8WV19) · Ensembl [ENSG00000198818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198818)

## Data

Gene col 12690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12690); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12690]; `tensor/DDL_lfc|DDL_z.npy` [12690]; `embed/gene_vectors.npy` [12690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12690 or target_col == 12690). Every well: [[SFT2D1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFT2D1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
