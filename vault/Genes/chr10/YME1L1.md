---
symbol: "YME1L1"
type: "gene"
col: 5900
ensembl_id: "ENSG00000136758"
name: "YME1 like 1 ATPase"
location: "10p12.1"
module: 159
arm: "+"
pooled_cpm: 240.2
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# YME1L1

*YME1 like 1 ATPase* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +25.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.700× (z -7.9, q 2e-12, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAN2]] (+0.67, fdr 2e-05), [[CCT6B]] (+0.66, fdr 2e-05), [[COPB2]] (+0.65, fdr 7e-06); moves opposite to [[INPP4A]] (-0.61, fdr 1e-05), [[BTBD3]] (-0.60, fdr 9e-05), [[EPS15]] (-0.60, fdr 2e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +25.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +14.4 | 2e-44 | 48/49 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +9.9 | 1e-20 | 45/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.53×** | +9.5 | 4e-19 | 42/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.6 | 2e-12 | 35/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.3 | 1e-05 | 23/49 (AsPC-1, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +4.1 | 0.003 | 24/48 (NCI-H460, SW48, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~4% of this change | 1.18× | +3.5 | 0.039 | 19/47 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.2 | 0.090 | 20/50 (BT-474, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.700×** | -7.9 | 2e-12 | 36/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -7.7 | 4e-12 | 37/48 (SK-MEL-2, HepG2/C3A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.716×** | -7.4 | 3e-11 | 35/48 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.728×** | -7.0 | 3e-10 | 33/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.738×** | -6.7 | 2e-09 | 40/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.817×** | -4.5 | 7e-04 | 27/49 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.839× | -3.7 | 0.014 | 23/48 (J82, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | 0.840× | -3.7 | 0.014 | 21/47 (HCT15, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.847× | -3.7 | 0.014 | 22/48 (CFPAC-1, SW 900, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.753×** | -3.3 | 0.059 | 26/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 165 | 10 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +35.3) | — |
| [[HOP62 (line)]] | alt | 200 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +28.0) | [[Panobinostat (drug)]] 0.5 µM 0.554× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 313 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.515× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 215 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +27.5) | — |
| [[BT-474 (line)]] | alt | 197 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.32× (z +12.6) | — |
| [[CFPAC-1 (line)]] | alt | 397 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +18.2) | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -11.7) |
| [[HT-29 (line)]] | alt | 260 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +13.9) | [[Belinostat (drug)]] 5 µM 0.530× (z -9.4) |
| [[LoVo (line)]] | wt | 290 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +23.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 292 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +23.2) | — |
| [[A-172 (line)]] | wt | 210 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +31.6) | — |
| [[HEC-1-A (line)]] | alt | 205 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +18.2) | — |
| [[NCI-H1573 (line)]] | alt | 205 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +25.0) | — |
| [[PANC-1 (line)]] | alt | 175 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +32.2) | — |
| [[RKO (line)]] | wt | 264 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +19.0) | — |
| [[RPMI-7951 (line)]] | alt | 339 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.591× (z -8.6) |
| [[SW480 (line)]] | alt | 234 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 5.75× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 166 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.2) | — |
| [[KATO III (line)]] | alt | 178 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.553× (z -8.7) |
| [[LS 180 (line)]] | wt | 242 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 224 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +22.4) | — |
| [[SNU-1 (line)]] | wt | 243 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +18.4) | — |
| [[SW 900 (line)]] | alt | 361 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +15.3) | [[Panobinostat (drug)]] 0.5 µM 0.520× (z -8.8) |
| [[SW1417 (line)]] | alt | 244 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.00× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.560× (z -8.9) |
| [[SW48 (line)]] | wt | 245 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +18.2) | — |
| [[A-427 (line)]] | wt | 235 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +15.0) | — |
| [[A549 (line)]] | wt | 246 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +20.6) | — |
| [[C-33 A (line)]] | alt | 211 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.33× (z +13.3) | — |
| [[C32 (line)]] | wt | 83.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +16.0) | — |
| [[HCT15 (line)]] | alt | 371 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.25× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 354 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.0) | [[Belinostat (drug)]] 5 µM 0.548× (z -8.6) |
| [[Hs 766T (line)]] | wt | 177 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +11.8) | — |
| [[HS-578T (line)]] | alt | 190 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +18.8) | — |
| [[hTERT-HPNE (line)]] | wt | 243 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +16.2) | — |
| [[NCI-H2030 (line)]] | alt | 400 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +18.0) | — |
| [[NCI-H23 (line)]] | alt | 197 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +13.4) | — |
| [[Panc 03.27 (line)]] | alt | 175 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.0) | — |
| [[A498 (line)]] | wt | 290 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +12.6) | — |
| [[J82 (line)]] | alt | 262 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +22.9) | — |
| [[NCI-H1792 (line)]] | alt | 348 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +19.4) | — |
| [[NCI-H2347 (line)]] | alt | 253 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 200 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +23.0) | — |
| [[SW 1088 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.137× (z -10.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 204 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 267 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 198 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 235 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAN2]] | +0.67 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[CCT6B]] | +0.66 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[COPB2]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[USP8]] | +0.63 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[ZNF490]] | +0.62 | +0.62 / +0.28 | both halves | 3e-04 |  |
| [[SMC5-DT]] | +0.61 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[C5AR1]] | +0.61 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[C6orf62]] | +0.59 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[HCLS1]] | +0.59 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[METTL6]] | +0.58 | +0.43 / +0.41 | both halves | 4e-05 |  |
| [[ERI2]] | +0.58 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[MAGED2]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP4A]] | -0.61 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[BTBD3]] | -0.60 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[EPS15]] | -0.60 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[ANKS6]] | -0.59 | -0.57 / -0.59 | both halves | 1e-05 |  |
| [[SLC23A2]] | -0.58 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[BRF1]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ABHD6]] | -0.57 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[NAA40]] | -0.56 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[EXOC2]] | -0.56 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[TTLL4]] | -0.55 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[CEP85]] | -0.55 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[RRP1B]] | -0.54 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises YME1L1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises YME1L1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction -0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.8, -35.3); signed map (15.7, -4.8). **Vector** length 114, 39.9% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.9 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +25.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.3 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +7.3 | +2.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.8 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.7 | -0.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.6 | +1.2 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.6 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.2 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.1 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.2 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -6.7 | +4.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.8 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | +1.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | YME1 like 1 ATPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:27,110,111-27,155,266 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YME1L |
| Gene groups (HGNC) | AAA ATPases |
| Reactome | 7 pathways, smallest: Cellular response to mitochondrial stress; Processing of SMDT1; Mitochondrial calcium ion transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96TA2](https://www.uniprot.org/uniprotkb/Q96TA2) (ATP-dependent zinc metalloprotease YME1L1):

> ATP-dependent metalloprotease that catalyzes the degradation of folded and unfolded proteins with a suitable degron sequence in the mitochondrial intermembrane region. Plays an important role in regulating mitochondrial morphology and function by cleaving OPA1 at position S2, giving rise to a form of OPA1 that promotes maintenance of normal mitochondrial structure and mitochondrial protein metabolism. Ensures cell proliferation, maintains normal cristae morphology and complex I respiration …

**Summary**, from NCBI Gene [10730](https://www.ncbi.nlm.nih.gov/gene/10730):

> The protein encoded by this gene is the human ortholog of yeast mitochondrial AAA metalloprotease, Yme1p. It is localized in the mitochondria and can functionally complement a yme1 disruptant yeast strain. It is proposed that this gene plays a role in mitochondrial protein metabolism and could be involved in mitochondrial pathologies. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:12843](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12843) · Entrez [10730](https://www.ncbi.nlm.nih.gov/gene/10730) · UniProt [Q96TA2](https://www.uniprot.org/uniprotkb/Q96TA2) · Ensembl [ENSG00000136758](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136758)

## Data

Gene col 5900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5900); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5900]; `tensor/DDL_lfc|DDL_z.npy` [5900]; `embed/gene_vectors.npy` [5900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5900 or target_col == 5900). Every well: [[YME1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YME1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
