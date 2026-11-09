---
symbol: "ZBED9"
type: "gene"
col: 13832
ensembl_id: "ENSG00000232040"
name: "SCAN domain containing 3"
location: "6p22.1"
module: 16
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 36
n_dd_up: 27
n_dd_down: 5
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBED9

*SCAN domain containing 3* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.91× (z +15.2, q 0e+00, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.458× (z -7.8, q 1e-12, down in 16 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.459× (z -7.8, q 1e-12, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF620]] (+0.79, fdr 7e-06), [[FAM200A]] (+0.76, fdr 7e-06), [[COQ5]] (+0.75, fdr 2e-05); moves opposite to [[SLC25A5]] (-0.67, fdr 2e-05), [[SMARCD2]] (-0.64, fdr 1e-05), [[UQCRH]] (-0.64, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF155]], [[ZNF221]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Capivasertib (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.91×** | +15.2 | 0e+00 | 25/28 (NCI-H2030, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.45×** | +12.5 | 4e-33 | 24/25 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.97×** | +9.7 | 9e-20 | 19/32 (CFPAC-1, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.60×** | +9.6 | 1e-19 | 22/33 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +9.2 | 3e-18 | 15/25 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.44×** | +8.6 | 7e-16 | 24/32 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +6.3 | 2e-08 | 15/33 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.84×** | +6.1 | 6e-08 | 14/32 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +5.8 | 3e-07 | 2/6 (NCI-H2347, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +5.7 | 6e-07 | 12/32 (A-427, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +5.3 | 6e-06 | 4/15 (HEC-1-A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.1 | 1e-05 | 11/33 (HOP62, NCI-H2030, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.59×** | +4.7 | 1e-04 | 10/29 (HOP62, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.7 | 1e-04 | 9/33 (A-427, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +4.5 | 2e-04 | 8/32 (SK-MEL-2, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.009 | 4/33 (CFPAC-1, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.009 | 5/29 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.013 | 1/25 (RKO) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -7.8 | 1e-12 | 16/25 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.459×** | -7.8 | 1e-12 | 19/33 (LS 180, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -6.6 | 1e-08 | 16/33 (HT-29, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -6.3 | 5e-08 | 15/33 (J82, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.613×** | -4.9 | 1e-04 | 12/33 (SW 900, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | 0.715× | -3.2 | 0.11 | 7/21 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Darolutamide (drug)]] 0.5 µM |  | 0.735× | -3.1 | 0.17 | 6/32 (SW1417, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 13.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +8.6) | [[Digitoxin (drug)]] 0.05 µM 0.177× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 7.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 2.53 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0426× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 7.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +9.6) | — |
| [[RKO (line)]] | wt | 6.48 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0932× (z -8.8) |
| [[SW480 (line)]] | alt | 3.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +9.0) | — |
| [[A-172 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.442 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF620]] | +0.79 | +0.86 / +0.62 | both halves | 7e-06 |  |
| [[FAM200A]] | +0.76 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[COQ5]] | +0.75 | +0.85 / +0.48 | both halves | 2e-05 |  |
| [[ELAC1]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[METTL18]] | +0.74 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.74 | +0.81 / +0.55 | both halves | 1e-05 |  |
| [[ZXDB]] | +0.73 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[FNBP1P1]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[GDAP1]] | +0.72 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[ZSCAN12]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[BCDIN3D]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.72 | +0.79 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A5]] | -0.67 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[SMARCD2]] | -0.64 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.64 | -0.71 / -0.46 | both halves | 3e-05 |  |
| [[CMC2]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.63 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[AP2A1]] | -0.62 | -0.71 / -0.49 | both halves | 1e-05 |  |
| [[KIAA1958]] | -0.62 | -0.68 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF155]], [[ZNF221]] | B | ZNF155, ZNF221 activity raises ZBED9's level | lines that do not express ZNF155, ZNF221 (5) vs lines expressing them (45) | 2.61× lower at baseline in the lines without ZNF155, ZNF221 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF540, ZNF529-AS1, AGK; co-absent genes |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Capivasertib (drug)]] 5 µM | B | ZBED9 activity raises the cells' numbers under Capivasertib 5 µM (protects the cells) | lines that do not express ZBED9 (14) vs lines expressing it (34) | the lines without ZBED9: 0.91× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: TDRP, ZNF583, POPDC3 |
| [[ZSCAN12]] | B | ZBED9 activity raises ZSCAN12's level | lines that do not express ZBED9 (14) vs lines expressing it (36) | 1.89× lower at baseline in the lines without ZBED9 | 0.092 | ⚠ within organs, on part of the lines; also absent: TDRP, ZNF583, POPDC3 |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.1, 9.8); signed map (4.9, -25.9). **Vector** length 49.2, 7.52% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +12.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +8.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.9 | -4.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +1.8 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -0.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | SCAN domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:28,570,535-28,616,212 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFP38-L, KIAA1925, FLJ31087, Buster4, FAM200D; previously ZNF305P2, ZNF452, ZBED9 |
| Gene groups (HGNC) | SCAN domain containing; Zinc fingers BED-type; Integrase like retrotransposon derived |
| Matched by | ensembl_id |

UniProt [Q6R2W3](https://www.uniprot.org/uniprotkb/Q6R2W3) carries no function annotation.

**Summary**, from NCBI Gene [114821](https://www.ncbi.nlm.nih.gov/gene/114821):

> Predicted to enable nucleic acid binding activity. Involved in positive regulation of cell cycle and positive regulation of epithelial cell proliferation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13851) · Entrez [114821](https://www.ncbi.nlm.nih.gov/gene/114821) · UniProt [Q6R2W3](https://www.uniprot.org/uniprotkb/Q6R2W3) · Ensembl [ENSG00000232040](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232040)

## Data

Gene col 13832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13832); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13832]; `tensor/DDL_lfc|DDL_z.npy` [13832]; `embed/gene_vectors.npy` [13832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13832 or target_col == 13832). Every well: [[ZBED9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
