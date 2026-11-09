---
symbol: "ZDHHC20"
type: "gene"
col: 11129
ensembl_id: "ENSG00000180776"
name: "zDHHC palmitoyltransferase 20"
location: "13q12.11"
module: 57
arm: "+"
pooled_cpm: 138.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ZDHHC20

*zDHHC palmitoyltransferase 20* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.31× (z +5.7, q 7e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.738× (z -6.5, q 6e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDM1A]] (+0.66, fdr 7e-06), [[TBC1D2B]] (+0.65, fdr 7e-06), [[NDRG3]] (+0.65, fdr 7e-06); moves opposite to [[NFX1]] (-0.69, fdr 7e-06), [[SMIM12]] (-0.63, fdr 1e-05), [[ZNF75A]] (-0.61, fdr 7e-06).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MGAT4A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +5.7 | 7e-06 | 31/48 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.27×** | +5.1 | 9e-05 | 25/48 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.0 | 1e-04 | 25/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.8 | 2e-04 | 28/47 (COLO 205, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.005 | 24/45 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.023 | 23/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +3.5 | 0.032 | 20/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.066 | 21/48 (SW480, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.16× | +3.2 | 0.089 | 16/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.0 | 0.13 | 12/48 (SW 900, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11129.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.738×** | -6.5 | 6e-08 | 29/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -6.3 | 6e-08 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -6.1 | 2e-07 | 31/48 (NCI-H1573, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.776×** | -5.4 | 1e-05 | 31/48 (MIA PaCa-2, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.824×** | -3.8 | 0.016 | 22/48 (NCI-H2347, C-33 A, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.082 | 15/47 (C32, NCI-H460, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.900× | -3.2 | 0.11 | 11/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.857× | -3.2 | 0.11 | 16/47 (C32, BT-474, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 73.2 | 2 (2 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Harringtonine (drug)]] 0.5 µM 0.285× (z -16.4) |
| [[C32 (line)]] | wt | 260 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.400× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 78.9 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +13.1) | — |
| [[LoVo (line)]] | wt | 121 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.545× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -12.6) |
| [[SW1417 (line)]] | alt | 166 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +9.0) | — |
| [[A-172 (line)]] | wt | 114 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.99× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 89.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.93× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[KATO III (line)]] | alt | 194 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +14.0) | — |
| [[LOX-IMVI (line)]] | wt | 163 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.438× (z -10.3) |
| [[LS 180 (line)]] | wt | 203 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +12.9) | — |
| [[SW480 (line)]] | alt | 207 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +9.3) | — |
| [[A-427 (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.569× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 121 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +14.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[COLO 205 (line)]] | alt | 327 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +10.8) ⚠ toxic | — |
| [[HepG2_C3A (line)]] | wt | 123 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +10.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.472× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 100.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.428× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 170 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 196 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 223 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 172 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | +0.66 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TBC1D2B]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[TWSG1]] | +0.65 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[RNPEP]] | +0.64 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CLSTN1]] | +0.63 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[HDAC1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[FAM102B]] | +0.63 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[RPA1]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HMGN3]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PTK7]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SNX30]] | +0.61 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFX1]] | -0.69 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[SMIM12]] | -0.63 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.61 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[HELQ]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[UTP3]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[ZNF146]] | -0.59 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[C14orf119]] | -0.58 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[NME6]] | -0.58 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[TSSC4]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[UTP23]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[ESF1]] | -0.57 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGAT4A]] | B | MGAT4A activity raises ZDHHC20's level | lines that do not express MGAT4A (11) vs lines expressing it (39) | 1.54× lower at baseline in the lines without MGAT4A | 0.060 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, ZNF860, EPHA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.600). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-3.0, -5.9); signed map (-35.8, -12.2). **Vector** length 117, 33.3% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +5.1 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +4.6 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.9 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.6 | +2.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.9 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.2 | -2.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:21,348,784-21,459,370 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25952, DHHC20 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Reactome | 6 pathways, smallest: Maturation of spike protein_9694548; Translation of Structural Proteins_9694635; Late SARS-CoV-2 Infection Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5W0Z9](https://www.uniprot.org/uniprotkb/Q5W0Z9) (Palmitoyltransferase ZDHHC20):

> Palmitoyltransferase that could catalyze the addition of palmitate onto various protein substrates. Catalyzes palmitoylation of Cys residues in the cytoplasmic C-terminus of EGFR, and modulates the duration of EGFR signaling by modulating palmitoylation-dependent EGFR internalization and degradation. Has a preference for acyl-CoA with C16 fatty acid chains. Can also utilize acyl-CoA with C14 and C18 fatty acid chains. May palmitoylate CALHM1 subunit of gustatory voltage-gated ion channels and …

**Summary**, from NCBI Gene [253832](https://www.ncbi.nlm.nih.gov/gene/253832):

> Enables protein-cysteine S-palmitoyltransferase activity and zinc ion binding activity. Involved in DNA damage response and peptidyl-L-cysteine S-palmitoylation. Located in Golgi membrane; nucleus; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20749) · Entrez [253832](https://www.ncbi.nlm.nih.gov/gene/253832) · UniProt [Q5W0Z9](https://www.uniprot.org/uniprotkb/Q5W0Z9) · Ensembl [ENSG00000180776](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180776)

## Data

Gene col 11129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11129); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11129]; `tensor/DDL_lfc|DDL_z.npy` [11129]; `embed/gene_vectors.npy` [11129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11129 or target_col == 11129). Every well: [[ZDHHC20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
