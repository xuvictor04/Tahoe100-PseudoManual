---
symbol: "APBA1"
type: "gene"
col: 2841
ensembl_id: "ENSG00000107282"
name: "amyloid beta precursor protein binding family A member 1"
location: "9q21.12"
module: 115
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 44
n_dd_up: 25
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# APBA1

*amyloid beta precursor protein binding family A member 1* — 9q21.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.93× (z +24.9, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.500× (z -8.9, q 4e-16, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF5C]] (+0.64, fdr 9e-06), [[OTUD7A]] (+0.63, fdr 7e-05), [[SUSD4]] (+0.61, fdr 1e-04); moves opposite to [[CDK12]] (-0.53, fdr 2e-04), [[GPATCH2]] (-0.48, fdr 2e-04), [[PPP4R3B]] (-0.47, fdr 2e-04).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MAP2K1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PPP1R14C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2841.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.93×** | +24.9 | 0e+00 | 39/41 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.93×** | +17.6 | 0e+00 | 35/41 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.44×** | +15.9 | 0e+00 | 34/38 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.29×** | +15.3 | 0e+00 | 31/40 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.49×** | +15.0 | 0e+00 | 32/40 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.06×** | +14.4 | 8e-45 | 32/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +12.3 | 7e-33 | 18/35 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.87×** | +9.1 | 8e-18 | 24/40 (NCI-H460, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.0 | 1e-10 | 1/10 (BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.0 | 8e-08 | 14/39 (HOP62, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.2 | 1e-05 | 2/21 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.48×** | +5.0 | 2e-05 | 11/40 (SW480, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.4 | 5e-04 | 1/13 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.002 | 6/40 (NCI-H23, SW 900, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.009 | 5/40 (SW48, SHP-77, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.009 | 7/40 (SHP-77, Hs 766T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.011 | 7/40 (SW48, SHP-77, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.018 | 7/39 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2841.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.500×** | -8.9 | 4e-16 | 22/41 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -7.7 | 4e-12 | 23/40 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.541×** | -7.4 | 3e-11 | 21/40 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -6.4 | 2e-08 | 20/36 (Hs 766T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.703×** | -4.5 | 7e-04 | 15/40 (LOX-IMVI, SNU-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -4.4 | 0.001 | 12/35 (LOX-IMVI, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -4.3 | 0.001 | 14/40 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -4.2 | 0.002 | 11/36 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.739×** | -3.9 | 0.007 | 18/40 (SNU-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.737×** | -3.6 | 0.017 | 4/40 (SW 900, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.757×** | -3.6 | 0.018 | 9/40 (LOX-IMVI, SNU-1, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | **0.821×** | -3.6 | 0.018 | 11/41 (H4, A498, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.753×** | -3.5 | 0.020 | 4/40 (C32, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.761×** | -3.5 | 0.020 | 11/39 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2841. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 23.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -9.8) |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0874× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 2.16 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 16.7× (z +13.9) | — |
| [[SW480 (line)]] | alt | 5.66 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.36× (z +12.5) | — |
| [[A498 (line)]] | wt | 4.51 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0748× (z -10.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0978× (z -8.6) |
| [[C-33 A (line)]] | alt | 8.49 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0736× (z -8.7) |
| [[Hs 766T (line)]] | wt | 6.60 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0703× (z -10.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 2.02 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.16× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 6.27 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0592× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -11.1) |
| [[SHP-77 (line)]] | alt | 58.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -9.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 4.16 | 0 | 1 | — | [[Fenofibrate (drug)]] 0.05 µM 0.0469× (z -9.0) |
| [[SW1417 (line)]] | alt | 3.00 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.0× (z +10.5) | — |
| [[SW48 (line)]] | wt | 25.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -8.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2841), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF5C]] | +0.64 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[OTUD7A]] | +0.63 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[SUSD4]] | +0.61 | +0.35 / +0.70 | both halves | 1e-04 |  |
| [[ATP1A3]] | +0.60 | +0.24 / +0.71 | both halves | 4e-04 |  |
| [[TMOD2]] | +0.60 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CELF4]] | +0.60 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SLC4A8]] | +0.59 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[LINC00937]] | +0.56 | +0.38 / +0.68 | both halves | 7e-05 |  |
| [[RGS10]] | +0.56 | +0.32 / +0.58 | both halves | 1e-04 |  |
| [[HS6ST3]] | +0.56 | +0.38 / +0.67 | both halves | 7e-05 |  |
| [[SH3GL2]] | +0.56 | +0.42 / +0.64 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK12]] | -0.53 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[GPATCH2]] | -0.48 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[PPP4R3B]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[CARD8]] | -0.46 | -0.24 / -0.43 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers APBA1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R14C]] | B | APBA1 activity raises PPP1R14C's level | lines that do not express APBA1 (6) vs lines expressing it (44) | 3.21× lower at baseline in the lines without APBA1 | 0.070 | ⚠ within organs, on part of the lines; also absent: MATN2, CCDC102A, ENSG00000267131; maybe low, not absent |
| [[PRKAR2B]] | C | APBA1 activity raises PRKAR2B's level | lines that do not express APBA1 (6) vs lines expressing it (44) | 4.68× lower at baseline in the lines without APBA1 | 0.077 | ⚠ within organs, on part of the lines; also absent: MATN2, CCDC102A, ENSG00000267131; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.8, 35.4); signed map (20.8, 24.5). **Vector** length 66.3, 10.6% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.7 | +24.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.3 | +15.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.0 | +14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +7.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.8 | +5.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.5 | -3.5 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | amyloid beta precursor protein binding family A member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.12 — chr9:69,427,532-69,672,371 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D9S411E, X11; previously MINT1 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 9 pathways, smallest: Dopamine Neurotransmitter Release Cycle; Assembly and cell surface presentation of NMDA receptors; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02410](https://www.uniprot.org/uniprotkb/Q02410) (Amyloid-beta A4 precursor protein-binding family A member 1):

> Putative function in synaptic vesicle exocytosis by binding to Munc18-1, an essential component of the synaptic vesicle exocytotic machinery. May modulate processing of the amyloid-beta precursor protein (APP) and hence formation of APP-beta. Component of the LIN-10-LIN-2-LIN-7 complex, which associates with the motor protein KIF17 to transport vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules (By similarity).

**Summary**, from NCBI Gene [320](https://www.ncbi.nlm.nih.gov/gene/320):

> The protein encoded by this gene is a member of the X11 protein family. It is a neuronal adapter protein that interacts with the Alzheimer's disease amyloid precursor protein (APP). It stabilizes APP and inhibits production of proteolytic APP fragments including the A beta peptide that is deposited in the brains of Alzheimer's disease patients. This gene product is believed to be involved in signal transduction processes. It is also regarded as a putative vesicular trafficking protein in the …

**Accessions** — [HGNC:578](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:578) · Entrez [320](https://www.ncbi.nlm.nih.gov/gene/320) · UniProt [Q02410](https://www.uniprot.org/uniprotkb/Q02410) · Ensembl [ENSG00000107282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107282)

## Data

Gene col 2841: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2841); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2841, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2841]; `tensor/DDL_lfc|DDL_z.npy` [2841]; `embed/gene_vectors.npy` [2841]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2841 or target_col == 2841). Every well: [[APBA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APBA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
