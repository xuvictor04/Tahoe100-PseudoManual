---
symbol: "TMBIM4"
type: "gene"
col: 7931
ensembl_id: "ENSG00000155957"
name: "transmembrane BAX inhibitor motif containing 4"
location: "12q14.3"
module: 1
arm: "+"
pooled_cpm: 42.81
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 31
n_dd_up_clean: 2
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TMBIM4

*transmembrane BAX inhibitor motif containing 4* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 1.30× (z +5.0, q 4e-04, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.270× (z -24.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM128]] (+0.67, fdr 1e-05), [[HDHD2]] (+0.61, fdr 1e-05), [[DMAC2L]] (+0.60, fdr 2e-05); moves opposite to [[RNF122]] (-0.56, fdr 3e-05), [[ABCB6]] (-0.54, fdr 4e-05), [[P4HA2]] (-0.51, fdr 8e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NDRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +5.0 | 4e-04 | 25/48 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +4.4 | 0.003 | 20/44 (SNU-423, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pralsetinib (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.008 | 19/48 (COLO 205, A498, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.270×** | -24.9 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.414×** | -24.4 | 0e+00 | 45/47 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.290×** | -24.2 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.331×** | -21.7 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.468×** | -14.9 | 0e+00 | 42/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -13.1 | 4e-37 | 41/47 (PANC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.505×** | -12.8 | 8e-36 | 42/47 (RKO, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.523×** | -12.7 | 4e-35 | 44/48 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.636×** | -12.5 | 6e-34 | 35/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.548×** | -11.5 | 1e-28 | 40/47 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.560×** | -11.0 | 1e-26 | 38/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.569×** | -11.0 | 1e-26 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.574×** | -10.6 | 2e-24 | 38/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.604×** | -9.5 | 9e-20 | 37/48 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -9.5 | 1e-19 | 37/48 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.621×** | -9.1 | 5e-18 | 38/48 (LoVo, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -8.9 | 2e-17 | 33/48 (RKO, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 39.3 | 0 | 16 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -20.3) |
| [[PANC-1 (line)]] | alt | 83.9 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -21.6) |
| [[HT-29 (line)]] | alt | 56.8 | 0 | 11 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 45.7 | 0 | 11 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -18.5) |
| [[LS 180 (line)]] | wt | 61.5 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -23.0) |
| [[RKO (line)]] | wt | 60.9 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -20.2) |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -19.2) |
| [[J82 (line)]] | alt | 29.2 | 0 | 7 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -11.9) |
| [[A-427 (line)]] | wt | 57.1 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -12.9) |
| [[A549 (line)]] | wt | 35.4 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.222× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.224× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 35.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -14.0) |
| [[LoVo (line)]] | wt | 32.2 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 70.5 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.286× (z -18.4) |
| [[SW1417 (line)]] | alt | 32.4 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -15.7) |
| [[Hs 766T (line)]] | wt | 53.9 | 0 | 5 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0517× (z -14.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -14.1) |
| [[hTERT-HPNE (line)]] | wt | 36.1 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -11.8) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 53.6 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -12.3) |
| [[BT-474 (line)]] | alt | 46.7 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -10.1) |
| [[H4 (line)]] | wt | 53.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -11.2) |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.8) |
| [[KATO III (line)]] | alt | 23.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -16.3) |
| [[LOX-IMVI (line)]] | wt | 44.7 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.174× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 40.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.3) |
| [[SNU-1 (line)]] | wt | 50.5 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -17.6) |
| [[A-172 (line)]] | wt | 39.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.289× (z -12.0) |
| [[A498 (line)]] | wt | 49.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 40.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -17.3) |
| [[HOP62 (line)]] | alt | 28.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.276× (z -10.0) |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -11.9) |
| [[SNU-423 (line)]] | alt | 38.5 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -12.9) |
| [[C-33 A (line)]] | alt | 32.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 31.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 35.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 41.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -8.7) |
| [[SW 1271 (line)]] | alt | 61.9 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0675× (z -10.0) |
| [[SW 900 (line)]] | alt | 34.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -12.3) |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM128]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[HDHD2]] | +0.61 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[DMAC2L]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PGGT1B]] | +0.57 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[C5orf63]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[EHHADH]] | +0.57 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[TMEM209]] | +0.56 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PTAR1]] | +0.56 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[PIGO]] | +0.56 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[NHLRC2]] | +0.55 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[GUF1]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[CHURC1]] | +0.54 | +0.40 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF122]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[ABCB6]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[P4HA2]] | -0.51 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[FAM219A]] | -0.50 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[NDRG1]] | -0.49 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[MACO1]] | -0.49 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[PI4KAP2]] | -0.47 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[LRRFIP1]] | -0.47 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[KDM4B]] | -0.47 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[TPI1]] | -0.47 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[C9orf24]] | -0.46 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[VDAC1]] | -0.46 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | B | NDRG1 activity lowers TMBIM4's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.30× higher at baseline in the lines without NDRG1 | 0.081 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.8, -17.5); signed map (1.0, -37.0). **Vector** length 73.6, 17.7% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | -12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.6 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | -6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +5.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -24.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -12.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -11.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -9.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.9 | -5.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane BAX inhibitor motif containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:66,135,846-66,170,027 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-119, S1R, ZPRO, LFG4, GAAP |
| Gene groups (HGNC) | Transmembrane BAX inhibitor motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC24](https://www.uniprot.org/uniprotkb/Q9HC24) (Protein lifeguard 4):

> Anti-apoptotic protein which can inhibit apoptosis induced by intrinsic and extrinsic apoptotic stimuli. Can modulate both capacitative Ca2+ entry and inositol 1,4,5-trisphosphate (IP3)-mediated Ca2+ release.

**Summary**, from NCBI Gene [51643](https://www.ncbi.nlm.nih.gov/gene/51643):

> Predicted to enable calcium channel activity. Involved in negative regulation of apoptotic process and regulation of calcium-mediated signaling. Located in Golgi stack and endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24257) · Entrez [51643](https://www.ncbi.nlm.nih.gov/gene/51643) · UniProt [Q9HC24](https://www.uniprot.org/uniprotkb/Q9HC24) · Ensembl [ENSG00000155957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155957)

## Data

Gene col 7931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7931); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7931]; `tensor/DDL_lfc|DDL_z.npy` [7931]; `embed/gene_vectors.npy` [7931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7931 or target_col == 7931). Every well: [[TMBIM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMBIM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
