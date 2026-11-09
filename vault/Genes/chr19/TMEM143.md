---
symbol: "TMEM143"
type: "gene"
col: 8441
ensembl_id: "ENSG00000161558"
name: "transmembrane protein 143"
location: "19q13.32"
module: 175
arm: "+"
pooled_cpm: 6.07
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 37
n_dd_up_clean: 7
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/175"]
generated_by: "tahoemap"
---

# TMEM143

*transmembrane protein 143* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.61× (z +5.8, q 4e-06, up in 6 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.57× (z +5.7, q 4e-06, up in 15 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.299× (z -15.3, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG7]] (+0.62, fdr 2e-05), [[CRYZL1]] (+0.61, fdr 1e-05), [[HAUS4]] (+0.61, fdr 1e-05); moves opposite to [[BACH1]] (-0.57, fdr 1e-05), [[TBILA]] (-0.57, fdr 1e-05), [[TNFRSF12A]] (-0.56, fdr 1e-05).
> It is in [[Module 175]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8441.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +5.8 | 4e-06 | 6/13 (J82, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.7 | 4e-06 | 15/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.40×** | +4.2 | 0.004 | 11/44 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 0.004 | 10/37 (NCI-H1792, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.005 | 5/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.006 | 7/47 (SW480, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.006 | 5/43 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.040 | 5/48 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.29× | +3.1 | 0.11 | 7/34 (HT-29, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.13 | 7/44 (HS-578T, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.13 | 5/47 (NCI-H2347, SW480, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | 1.29× | +3.0 | 0.13 | 2/41 (NCI-H2030, SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8441.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.299×** | -15.3 | 0e+00 | 38/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.359×** | -13.0 | 4e-36 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -12.5 | 2e-33 | 31/42 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.390×** | -11.9 | 1e-30 | 37/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.403×** | -11.5 | 1e-28 | 32/41 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -10.6 | 4e-24 | 30/41 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.440×** | -10.0 | 1e-21 | 32/46 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -7.9 | 2e-13 | 25/46 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.580×** | -6.6 | 2e-09 | 18/38 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.611×** | -6.3 | 2e-08 | 19/46 (RPMI-7951, Hs 766T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -5.9 | 2e-07 | 18/38 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.662×** | -5.2 | 8e-06 | 16/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.666×** | -5.0 | 3e-05 | 14/44 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -4.9 | 4e-05 | 14/46 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -4.8 | 6e-05 | 17/33 (A-427, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -4.7 | 8e-05 | 14/40 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.690×** | -4.7 | 9e-05 | 14/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.696×** | -4.6 | 1e-04 | 19/45 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8441. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.83 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0863× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.171× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 5.23 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.0992× (z -11.5) |
| [[COLO 205 (line)]] | alt | 8.08 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0478× (z -10.1) |
| [[HOP62 (line)]] | alt | 4.71 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0708× (z -11.1) |
| [[PANC-1 (line)]] | alt | 6.14 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -12.4) |
| [[A-427 (line)]] | wt | 9.88 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -9.2) ⚠ toxic |
| [[A498 (line)]] | wt | 7.03 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -14.8) |
| [[Hs 766T (line)]] | wt | 6.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.114× (z -8.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 7.40 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.9) |
| [[KATO III (line)]] | alt | 6.09 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0443× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0870× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 6.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 7.51 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0764× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 4.18 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0620× (z -8.5) |
| [[SNU-423 (line)]] | alt | 4.53 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0760× (z -9.3) |
| [[A-172 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8441), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | +0.62 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[CRYZL1]] | +0.61 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[HAUS4]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[USPL1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PGAP2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.58 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[TENT2]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SASS6]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[INPP5B]] | +0.57 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[USP30]] | +0.57 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[ZFP14]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[OSBPL7]] | +0.54 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[TBILA]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TNFRSF12A]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RSC1A1]] | -0.55 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ELK4]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[MYL12A]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DDX5]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ARAP2]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[MSRA]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[S100A11]] | -0.51 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[TEAD1]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises TMEM143's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without ZNF594-DT | 0.002 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[RDM1P5]] | B | RDM1P5 activity raises TMEM143's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.45× lower at baseline in the lines without RDM1P5 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 175]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.6, -50.4); signed map (-39.4, -20.9). **Vector** length 57.2, 8.31% of its response variance represented; |z| ≥ 3 in 947 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.1 | -4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +4.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -7.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -13.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -15.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 143 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:48,332,356-48,364,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10922 |
| Matched by | ensembl_id |

UniProt [Q96AN5](https://www.uniprot.org/uniprotkb/Q96AN5) carries no function annotation.

**Summary**, from NCBI Gene [55260](https://www.ncbi.nlm.nih.gov/gene/55260):

> Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25603) · Entrez [55260](https://www.ncbi.nlm.nih.gov/gene/55260) · UniProt [Q96AN5](https://www.uniprot.org/uniprotkb/Q96AN5) · Ensembl [ENSG00000161558](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161558)

## Data

Gene col 8441: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8441); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8441, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8441]; `tensor/DDL_lfc|DDL_z.npy` [8441]; `embed/gene_vectors.npy` [8441]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8441 or target_col == 8441). Every well: [[TMEM143 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM143.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
