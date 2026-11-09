---
symbol: "UEVLD"
type: "gene"
col: 7486
ensembl_id: "ENSG00000151116"
name: "UEV and lactate/malate dehyrogenase domains"
location: "11p15.1"
module: 194
arm: "+"
pooled_cpm: 40.22
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/194"]
generated_by: "tahoemap"
---

# UEVLD

*UEV and lactate/malate dehyrogenase domains* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +10.7, q 9e-24, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.634× (z -9.0, q 2e-16, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RC3H2]] (+0.65, fdr 7e-06), [[LTO1]] (+0.62, fdr 3e-05), [[CPSF2]] (+0.60, fdr 2e-05); moves opposite to [[GUSBP18]] (-0.65, fdr 1e-05), [[CFD]] (-0.59, fdr 4e-05), [[ACACB]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 194]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +10.7 | 9e-24 | 43/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +10.3 | 3e-22 | 36/47 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +10.2 | 4e-22 | 42/48 (HS-578T, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +6.9 | 8e-10 | 24/35 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +6.5 | 7e-09 | 32/48 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.4 | 2e-08 | 29/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.38×** | +6.3 | 2e-08 | 37/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +5.9 | 3e-07 | 26/45 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +5.5 | 2e-06 | 23/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.9 | 7e-05 | 21/48 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 22/48 (HEC-1-A, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.25×** | +4.4 | 4e-04 | 19/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.26×** | +4.4 | 5e-04 | 22/46 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.3 | 6e-04 | 21/47 (NCI-H2347, A-427, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 18/47 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.004 | 18/48 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.009 | 10/48 (NCI-H2347, A549, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.067 | 3/48 (NCI-H2347, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -9.0 | 2e-16 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -8.8 | 3e-16 | 35/47 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.671×** | -7.9 | 7e-13 | 30/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.496×** | -7.2 | 8e-11 | 31/47 (A-427, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.540×** | -6.3 | 3e-08 | 29/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -6.1 | 9e-08 | 26/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.730×** | -5.7 | 8e-07 | 26/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 49.1 | 1 | 5 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.298× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 37.0 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.67× (z +11.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.185× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -10.5) |
| [[PANC-1 (line)]] | alt | 58.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.346× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 32.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.294× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -9.2) |
| [[J82 (line)]] | alt | 64.3 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.286× (z -13.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -10.6) |
| [[A-427 (line)]] | wt | 45.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.139× (z -10.7) |
| [[HS-578T (line)]] | alt | 38.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.321× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 34.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 56.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 46.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 57.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.404× (z -9.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 44.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[A-172 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RC3H2]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[LTO1]] | +0.62 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[CPSF2]] | +0.60 | +0.66 / +0.49 | both halves | 2e-05 |  |
| [[SLC30A9]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 | STRING 609 |
| [[CSTF3]] | +0.60 | +0.71 / +0.38 | both halves | 6e-05 |  |
| [[RPAP2]] | +0.60 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[DUS4L]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DESI1]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[PSME3IP1]] | +0.58 | +0.56 / +0.39 | both halves | 6e-05 |  |
| [[ZFR]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.57 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[ZNF621]] | +0.57 | +0.58 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP18]] | -0.65 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CFD]] | -0.59 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ACACB]] | -0.56 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[FBXL16]] | -0.55 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[RADX]] | -0.55 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PODXL2]] | -0.55 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SMARCD3]] | -0.54 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[SLC66A2]] | -0.54 | -0.56 / -0.35 | both halves | 1e-04 |  |
| [[FOXO6]] | -0.53 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[MAST3]] | -0.53 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[PNKD]] | -0.52 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[NR2F6]] | -0.52 | -0.52 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UEVLD's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 194]]; 17 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (9.5, 6.7); signed map (17.3, -28.3). **Vector** length 89.1, 19.9% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +6.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +6.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +10.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | +0.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.8 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -0.7 |
|  | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | UEV and lactate/malate dehyrogenase domains |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:18,529,609-18,588,747 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Attp, UEV3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IX04](https://www.uniprot.org/uniprotkb/Q8IX04) (Ubiquitin-conjugating enzyme E2 variant 3):

> Possible negative regulator of polyubiquitination.

**Summary**, from NCBI Gene [55293](https://www.ncbi.nlm.nih.gov/gene/55293):

> Predicted to enable ubiquitin binding activity. Predicted to be involved in endosome to lysosome transport. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30866) · Entrez [55293](https://www.ncbi.nlm.nih.gov/gene/55293) · UniProt [Q8IX04](https://www.uniprot.org/uniprotkb/Q8IX04) · Ensembl [ENSG00000151116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151116)

## Data

Gene col 7486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7486); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7486]; `tensor/DDL_lfc|DDL_z.npy` [7486]; `embed/gene_vectors.npy` [7486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7486 or target_col == 7486). Every well: [[UEVLD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UEVLD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
