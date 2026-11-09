---
symbol: "APBA2"
type: "gene"
col: 419
ensembl_id: "ENSG00000034053"
name: "amyloid beta precursor protein binding family A member 2"
location: "15q13.1"
module: 132
arm: "+"
pooled_cpm: 31.75
n_lines_expressing: 32
n_dd_up: 0
n_dd_down: 40
n_dd_up_clean: 0
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# APBA2

*amyloid beta precursor protein binding family A member 2* — 15q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.283× (z -33.5, q 0e+00, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCOLCE2]] (+0.59, fdr 2e-05), [[PYGL]] (+0.57, fdr 1e-05), [[SERGEF]] (+0.54, fdr 1e-05); moves opposite to [[MYO7B]] (-0.49, fdr 1e-04), [[KLF3]] (-0.48, fdr 4e-05), [[TJP2]] (-0.48, fdr 2e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KIF26A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.4 | 0.45 | 5/29 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 1.37× | +3.1 | 0.54 | 9/26 (BT-474, A549, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.283×** | -33.5 | 0e+00 | 26/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.292×** | -23.1 | 0e+00 | 27/30 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.298×** | -22.8 | 0e+00 | 28/30 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.298×** | -21.9 | 0e+00 | 26/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.320×** | -21.4 | 0e+00 | 28/30 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.321×** | -21.3 | 0e+00 | 26/30 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.532×** | -11.8 | 2e-30 | 23/30 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.538×** | -11.6 | 2e-29 | 23/29 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.560×** | -10.9 | 9e-26 | 22/30 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.564×** | -10.8 | 3e-25 | 19/28 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -10.6 | 9e-25 | 19/29 (C32, A-172, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.568×** | -10.2 | 1e-22 | 16/22 (C-33 A, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.605×** | -9.4 | 2e-19 | 21/30 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.607×** | -9.4 | 3e-19 | 20/30 (SW 900, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -9.2 | 2e-18 | 21/30 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.716×** | -8.8 | 3e-17 | 18/30 (NCI-H2030, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -7.7 | 6e-13 | 17/30 (C32, HEC-1-A, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -7.4 | 6e-12 | 18/30 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.678×** | -7.3 | 1e-11 | 17/30 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.764×** | -7.1 | 3e-11 | 16/30 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 131 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0564× (z -37.0) |
| [[NCI-H460 (line)]] | wt | 84.8 | 0 | 19 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -38.3) |
| [[HEC-1-A (line)]] | alt | 56.4 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -29.0) |
| [[NCI-H2030 (line)]] | alt | 122 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -34.5) |
| [[A549 (line)]] | wt | 52.7 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -34.6) |
| [[C-33 A (line)]] | alt | 168 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0683× (z -27.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.170× (z -18.6) |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0852× (z -20.1) |
| [[NCI-H23 (line)]] | alt | 45.3 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -27.3) |
| [[SW 900 (line)]] | alt | 73.9 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 86.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -24.7) |
| [[AN3 CA (line)]] | alt | 82.6 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0772× (z -14.5) |
| [[A-172 (line)]] | wt | 46.8 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.203× (z -14.4) |
| [[HOP62 (line)]] | alt | 52.7 | 0 | 6 | — | [[Harringtonine (drug)]] 5 µM 0.254× (z -13.5) |
| [[BT-474 (line)]] | alt | 56.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.7) |
| [[A498 (line)]] | wt | 27.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -17.0) |
| [[SHP-77 (line)]] | alt | 64.7 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.238× (z -13.9) |
| [[A-427 (line)]] | wt | 33.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -16.5) |
| [[H4 (line)]] | wt | 64.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -22.2) |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.180× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -10.3) |
| [[CHP-212 (line)]] | wt | 68.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.4) |
| [[RPMI-7951 (line)]] | alt | 30.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.0) |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0728× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.54 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCOLCE2]] | +0.59 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PYGL]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SERGEF]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[TRABD2B]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LRAT]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[AFAP1L1]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[RASGEF1C]] | +0.52 | +0.38 / +0.52 | both halves | 6e-05 |  |
| [[BRSK2]] | +0.52 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SHANK3]] | +0.51 | +0.51 / +0.53 | both halves | 1e-05 | same gene group; pathway: Neurexins and neuroligins |
| [[FBXO17]] | +0.51 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[CHSY1]] | +0.51 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[DPYSL4]] | +0.51 | +0.41 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO7B]] | -0.49 | -0.54 / -0.34 | both halves | 1e-04 |  |
| [[KLF3]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TJP2]] | -0.48 | -0.31 / -0.43 | both halves | 2e-04 | same gene group |
| [[LGR6]] | -0.47 | -0.53 / -0.25 | both halves | 4e-04 |  |
| [[UGT1A9]] | -0.46 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[UGT1A8]] | -0.45 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ABO]] | -0.45 | -0.50 / -0.24 | both halves | 5e-04 |  |
| [[TNFRSF14-AS1]] | -0.44 | -0.56 / -0.20 | both halves | 7e-04 |  |
| [[EPS8L3]] | -0.44 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[C11orf54]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[FGD5]] | -0.43 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[AFAP1L2]] | -0.43 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF26A]] | B | KIF26A activity raises APBA2's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 4.15× lower at baseline in the lines without KIF26A | 0.034 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[ST6GAL1]] | B | ST6GAL1 activity strengthens APBA2's drug response | lines that do not express ST6GAL1 (8) vs lines expressing it (22) | the lines without ST6GAL1 respond 0.63× as strongly (z diff +3.05); strongest at Digitoxin 5 µM: 0.77x vs 0.45x (z diff +4.2) | 0.042 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, MYT1, ENSG00000290588; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises APBA2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.2, 44.7); signed map (-27.3, 37.2). **Vector** length 88.8, 21.8% of its response variance represented; |z| ≥ 3 in 957 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | -7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | -1.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.5 | -10.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -21.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.6 | -4.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -9.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.5 | -7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -2.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q13.1 — chr15:28,884,483-29,118,315 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D15S1518E, LIN-10, MGC:14091, HsT16821; previously X11L, MINT2 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 3 pathways, smallest: Neurexins and neuroligins; Protein-protein interactions at synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99767](https://www.uniprot.org/uniprotkb/Q99767) (Amyloid-beta A4 precursor protein-binding family A member 2):

> Putative function in synaptic vesicle exocytosis by binding to STXBP1, an essential component of the synaptic vesicle exocytotic machinery. May modulate processing of the amyloid-beta precursor protein (APP) and hence formation of APP-beta.

**Summary**, from NCBI Gene [321](https://www.ncbi.nlm.nih.gov/gene/321):

> The protein encoded by this gene is a member of the X11 protein family. It is a neuronal adapter protein that interacts with the Alzheimer's disease amyloid precursor protein (APP). It stabilizes APP and inhibits production of proteolytic APP fragments including the A beta peptide that is deposited in the brains of Alzheimer's disease patients. This gene product is believed to be involved in signal transduction processes. It is also regarded as a putative vesicular trafficking protein in the …

**Accessions** — [HGNC:579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:579) · Entrez [321](https://www.ncbi.nlm.nih.gov/gene/321) · UniProt [Q99767](https://www.uniprot.org/uniprotkb/Q99767) · Ensembl [ENSG00000034053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034053)

## Data

Gene col 419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 419); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 419]; `tensor/DDL_lfc|DDL_z.npy` [419]; `embed/gene_vectors.npy` [419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 419 or target_col == 419). Every well: [[APBA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
