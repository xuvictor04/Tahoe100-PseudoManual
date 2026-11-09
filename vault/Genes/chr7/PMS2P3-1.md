---
symbol: "PMS2P3-1"
type: "gene"
col: 16578
ensembl_id: "ENSG00000291092"
name: ""
location: ""
module: 168
arm: "+"
pooled_cpm: 10.29
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# PMS2P3-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.42× (z +6.3, q 2e-07, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.358× (z -8.0, q 5e-13, down in 21 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.406× (z -7.1, q 5e-10, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3]] (+0.89, fdr 7e-06, ⚠ same locus), [[RNF4]] (+0.80, fdr 7e-06), [[CRYBB2P1]] (+0.78, fdr 7e-06), [[SDHAP4]] (+0.78, fdr 7e-06); moves opposite to [[BPTF]] (-0.72, fdr 7e-06), [[EPC2]] (-0.69, fdr 7e-06), [[CUX1]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[P3H3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.42×** | +6.3 | 2e-07 | 38/47 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.08×** | +4.8 | 5e-04 | 31/44 (HS-578T, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +4.7 | 5e-04 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.4 | 0.002 | 22/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.015 | 18/47 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.025 | 18/47 (MIA PaCa-2, C32, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.054 | 17/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.066 | 17/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Roxadustat (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.066 | 12/46 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.090 | 14/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Oxaliplatin (drug)]] 0.05 µM |  | 1.50× | +3.1 | 0.11 | 12/48 (NCI-H1573, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -8.0 | 5e-13 | 21/24 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.406×** | -7.1 | 5e-10 | 37/47 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.551×** | -6.9 | 1e-09 | 31/47 (SNU-423, AsPC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.434×** | -6.2 | 9e-08 | 27/34 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -3.6 | 0.032 | 23/45 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.662×** | -3.4 | 0.066 | 21/48 (SW 1088, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.663×** | -3.3 | 0.066 | 16/48 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.673×** | -3.2 | 0.086 | 11/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.676×** | -3.2 | 0.088 | 16/48 (LS 180, SW 1088, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.683×** | -3.1 | 0.094 | 14/47 (COLO 205, NCI-H2030, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.687×** | -3.1 | 0.094 | 12/47 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.687×** | -3.1 | 0.094 | 17/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.687×** | -3.1 | 0.094 | 13/48 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 11.4 | 0 | 4 (1 ⚠) | — | [[Celecoxib (drug)]] 0.05 µM 0.0696× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[NCI-H2030 (line)]] | alt | 8.64 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0647× (z -12.1) ⚠ toxic |
| [[A-172 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[KATO III (line)]] | alt | 8.60 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.5 µM 0.0474× (z -13.3) |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0441× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0738× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.7) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3]] | +0.89 | +0.85 / +0.88 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[RNF4]] | +0.80 | +0.86 / +0.70 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[SDHAP4]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[ALG9]] | +0.74 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[SDHAP1]] | +0.74 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[NAPB]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.74 | +0.82 / +0.57 | both halves | 9e-06 |  |
| [[NDUFAF7]] | +0.73 | +0.79 / +0.65 | both halves | 7e-06 |  |
| [[RPA1]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[SEC11A]] | +0.72 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.72 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[ATPAF2]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPTF]] | -0.72 | -0.75 / -0.65 | both halves | 7e-06 |  |
| [[EPC2]] | -0.69 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[CUX1]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[SKIL]] | -0.68 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[TIAM2]] | -0.67 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[LZIC]] | -0.67 | -0.75 / -0.55 | both halves | 1e-05 |  |
| [[ERCC6L2]] | -0.66 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[ZNF764]] | -0.65 | -0.73 / -0.53 | both halves | 1e-05 |  |
| [[LYRM2]] | -0.65 | -0.73 / -0.57 | both halves | 9e-06 |  |
| [[ZNF644]] | -0.65 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[LARP7]] | -0.65 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[INO80]] | -0.64 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises PMS2P3-1's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.22× lower at baseline in the lines without P3H3 | 0.030 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[C21orf91]] | B | C21orf91 activity lowers PMS2P3-1's level | lines that do not express C21orf91 (5) vs lines expressing it (45) | 1.27× higher at baseline in the lines without C21orf91 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: USP25, GSDMD, RALGPS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.912). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-4.6, -14.7); signed map (-39.1, -11.3). **Vector** length 78.4, 16.3% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +0.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.2 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.9 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.4 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Thymol (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.8 | -2.6 |

## What is on record

> [!warning] No registry record
> PMS2P3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16578); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16578]; `tensor/DDL_lfc|DDL_z.npy` [16578]; `embed/gene_vectors.npy` [16578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16578 or target_col == 16578). Every well: [[PMS2P3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2P3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
