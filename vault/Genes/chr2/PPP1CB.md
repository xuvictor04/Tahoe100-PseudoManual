---
symbol: "PPP1CB"
type: "gene"
col: 13122
ensembl_id: "ENSG00000213639"
name: "protein phosphatase 1 catalytic subunit beta"
location: "2p23.2"
module: 171
arm: "+"
pooled_cpm: 138.94
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# PPP1CB

*protein phosphatase 1 catalytic subunit beta* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.50× (z +8.7, q 2e-15, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.508× (z -7.5, q 5e-11, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.690× (z -5.8, q 2e-06, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1A]] (+0.65, fdr 7e-06), [[BBS2]] (+0.63, fdr 1e-05), [[ERMP1]] (+0.63, fdr 7e-06); moves opposite to [[CLCF1]] (-0.61, fdr 1e-05), [[SLC66A1]] (-0.61, fdr 7e-06), [[TNFRSF12A]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.50×** | +8.7 | 2e-15 | 48/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.41×** | +7.1 | 4e-10 | 44/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +5.0 | 8e-05 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +4.3 | 0.003 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.094 | 34/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.508×** | -7.5 | 5e-11 | 47/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.556×** | -6.5 | 3e-08 | 44/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -5.8 | 2e-06 | 38/49 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.604×** | -5.6 | 4e-06 | 43/48 (CFPAC-1, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **0.677×** | -4.0 | 0.008 | 29/45 (NCI-H2347, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.715×** | -3.7 | 0.021 | 28/49 (NCI-H2347, CFPAC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.731×** | -3.4 | 0.046 | 32/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.654×** | -3.3 | 0.060 | 36/48 (SW 1271, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.761× | -3.0 | 0.16 | 31/48 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.84× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.66× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 245 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -12.1) |
| [[AsPC-1 (line)]] | alt | 176 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.301× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 204 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.26× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 165 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.355× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[HCT15 (line)]] | alt | 178 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.85× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -8.7) |
| [[HT-29 (line)]] | alt | 168 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.4) |
| [[LoVo (line)]] | wt | 79.0 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.68× (z +9.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 6.06× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 103 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.71× (z +11.7) | — |
| [[SW480 (line)]] | alt | 137 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 6.30× (z +10.1) | — |
| [[A-427 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.338× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[A498 (line)]] | wt | 198 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.7) |
| [[CHP-212 (line)]] | wt | 110 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.103× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 152 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.23× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.25× (z +9.7) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 113 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.40× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.350× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[SW 900 (line)]] | alt | 230 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW1417 (line)]] | alt | 206 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -9.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 158 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 135 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | +0.65 | +0.69 / +0.66 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[BBS2]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ERMP1]] | +0.63 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[CAPZA2]] | +0.62 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[CYB5A]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CHASERR]] | +0.61 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[FBXO7]] | +0.60 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PDK1]] | +0.60 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[DSTN]] | +0.60 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[COPS4]] | +0.59 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[MLLT10]] | +0.59 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[MORF4L1]] | +0.58 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | -0.61 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[SLC66A1]] | -0.61 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | -0.59 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[EIF3J]] | -0.58 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[SETX]] | -0.57 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[ZNF274]] | -0.56 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.55 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NIP7]] | -0.55 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ATG7]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 | pathway: Oncogenic MAPK signaling |
| [[PWP2]] | -0.54 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TUBA1C]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 | pathway: G2/M Transition |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PPP1CB's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.611). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-5.3, -8.3); signed map (-32.3, -15.9). **Vector** length 99.4, 35.4% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +6.2 | -3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | +5.8 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +5.2 | -4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.3 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +7.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.6 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -0.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 catalytic subunit beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:28,751,640-28,802,940 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PP1Cbeta, PPP1CD, PP1Cdelta, PP1B, PP-1B, PP1beta, PP1c, MP |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits |
| Reactome | 38 pathways, smallest: Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function; Signaling by MRAS-complex mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P62140](https://www.uniprot.org/uniprotkb/P62140) (Serine/threonine-protein phosphatase PP1-beta catalytic subunit):

> Protein phosphatase that associates with over 200 regulatory proteins to form highly specific holoenzymes which dephosphorylate hundreds of biological targets. Protein phosphatase (PP1) is essential for cell division, it participates in the regulation of glycogen metabolism, muscle contractility and protein synthesis. Involved in regulation of ionic conductances and long-term synaptic plasticity. Component of the PTW/PP1 phosphatase complex, which plays a role in the control of chromatin …

**Summary**, from NCBI Gene [5500](https://www.ncbi.nlm.nih.gov/gene/5500):

> The protein encoded by this gene is one of the three catalytic subunits of protein phosphatase 1 (PP1). PP1 is a serine/threonine specific protein phosphatase known to be involved in the regulation of a variety of cellular processes, such as cell division, glycogen metabolism, muscle contractility, protein synthesis, and HIV-1 viral transcription. Mouse studies suggest that PP1 functions as a suppressor of learning and memory. Two alternatively spliced transcript variants encoding distinct …

**Accessions** — [HGNC:9282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9282) · Entrez [5500](https://www.ncbi.nlm.nih.gov/gene/5500) · UniProt [P62140](https://www.uniprot.org/uniprotkb/P62140) · Ensembl [ENSG00000213639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213639)

## Data

Gene col 13122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13122); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13122]; `tensor/DDL_lfc|DDL_z.npy` [13122]; `embed/gene_vectors.npy` [13122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13122 or target_col == 13122). Every well: [[PPP1CB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1CB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
