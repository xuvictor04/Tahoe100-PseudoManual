---
symbol: "GATB"
type: "gene"
col: 676
ensembl_id: "ENSG00000059691"
name: "glutamyl-tRNA amidotransferase subunit B"
location: "4q31.3"
module: 1
arm: "+"
pooled_cpm: 12.72
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GATB

*glutamyl-tRNA amidotransferase subunit B* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.63× (z +7.8, q 3e-12, up in 29 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.562× (z -9.2, q 2e-17, down in 30 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.682× (z -8.6, q 2e-15, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AFG1L]] (+0.75, fdr 7e-06), [[ALG1]] (+0.73, fdr 7e-06), [[TCTN1]] (+0.73, fdr 7e-06); moves opposite to [[CDKN2D]] (-0.64, fdr 1e-05), [[DNAJC1]] (-0.64, fdr 8e-06), [[PDXP]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF528]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 676.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.8 | 3e-12 | 29/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +6.7 | 7e-09 | 28/48 (NCI-H1573, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.39×** | +5.0 | 1e-04 | 14/46 (C32, A498, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +4.6 | 7e-04 | 17/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.5 | 9e-04 | 13/48 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.006 | 13/48 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.008 | 14/44 (C32, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.7 | 0.013 | 12/24 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.019 | 9/48 (BT-474, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +3.5 | 0.022 | 9/46 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.022 | 12/48 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.4 | 0.035 | 3/48 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.043 | 14/46 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.051 | 7/47 (RKO, NCI-H1792, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +3.2 | 0.051 | 4/43 (HCT15, A498, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.053 | 12/48 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 676.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -9.2 | 2e-17 | 30/46 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.682×** | -8.6 | 2e-15 | 37/48 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.672×** | -6.3 | 4e-08 | 25/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.675×** | -6.3 | 5e-08 | 25/48 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.695×** | -5.8 | 7e-07 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.785×** | -3.9 | 0.010 | 13/47 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.633×** | -3.8 | 0.011 | 16/45 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.802×** | -3.4 | 0.041 | 10/48 (SW480, SNU-423, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.801×** | -3.4 | 0.041 | 14/41 (A-172, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.811×** | -3.3 | 0.047 | 13/46 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.812×** | -3.2 | 0.071 | 14/46 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.821× | -3.1 | 0.10 | 9/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.820× | -3.0 | 0.10 | 13/47 (Panc 03.27, PANC-1, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 676. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 32.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +15.9) | — |
| [[PANC-1 (line)]] | alt | 9.87 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.275× (z -9.8) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.188× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 13.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.322× (z -8.7) |
| [[C32 (line)]] | wt | 12.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.107× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 11.7 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.231× (z -8.9) |
| [[H4 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0751× (z -10.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.163× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.107× (z -9.5) |
| [[HT-29 (line)]] | alt | 6.23 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.104× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.116× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -8.6) ⚠ cell-cycle shift, explains ~11% of this change |
| [[RKO (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -9.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.8) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.232× (z -8.5) |
| [[SW48 (line)]] | wt | 12.6 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0851× (z -8.9) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 676), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AFG1L]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ALG1]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[MTHFSD]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[CHM]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.69 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.69 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[MRRF]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | STRING 405 |
| [[RPTOR]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[MRPL45]] | +0.67 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[FARS2]] | +0.67 | +0.68 / +0.64 | both halves | 7e-06 | STRING 496 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2D]] | -0.64 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[DNAJC1]] | -0.64 | -0.62 / -0.57 | both halves | 8e-06 |  |
| [[PDXP]] | -0.60 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ETHE1]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[ANKRD37]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CCNYL1]] | -0.57 | -0.42 / -0.65 | both halves | 4e-05 |  |
| [[RPS6KA5]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF528]] | B | ZNF528 activity raises GATB's level | lines that do not express ZNF528 (21) vs lines expressing it (29) | 1.10× lower at baseline in the lines without ZNF528 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF528-AS1, ZNF625, ZNF880 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.9, 10.8); signed map (9.1, -31.2). **Vector** length 81.5, 14.7% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +5.3 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +3.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.6 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +2.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.3 | -8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.7 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.0 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.5 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | glutamyl-tRNA amidotransferase subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:151,670,504-151,761,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PET112L, PET112 |
| Gene groups (HGNC) | Glutamyl-tRNA amidotransferase subunits; Ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [O75879](https://www.uniprot.org/uniprotkb/O75879) (Glutamyl-tRNA(Gln) amidotransferase subunit B, mitochondrial):

> Catalytic subunit of the mitochondrial Glu-tRNA(Gln) amidotransferase complex GatCAB (Probable). GatCAB allows the formation of correctly charged Gln-tRNA(Gln) through the transamidation of misacylated Glu-tRNA(Gln) in the mitochondria. The reaction takes place in the presence of glutamine and ATP through an activated gamma-phospho-Glu-tRNA(Gln) (By similarity). This subunit probably recognizes tRNA(Gln) and mediates the transamidation of misloaded Glu by catalyzing formation of the activated …

**Summary**, from NCBI Gene [5188](https://www.ncbi.nlm.nih.gov/gene/5188):

> Contributes to glutaminyl-tRNA synthase (glutamine-hydrolyzing) activity. Involved in glutaminyl-tRNAGln biosynthesis via transamidation and mitochondrial translation. Located in mitochondrion. Part of glutamyl-tRNA(Gln) amidotransferase complex. Implicated in combined oxidative phosphorylation deficiency 41. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:8849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8849) · Entrez [5188](https://www.ncbi.nlm.nih.gov/gene/5188) · UniProt [O75879](https://www.uniprot.org/uniprotkb/O75879) · Ensembl [ENSG00000059691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000059691)

## Data

Gene col 676: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 676); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 676, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 676]; `tensor/DDL_lfc|DDL_z.npy` [676]; `embed/gene_vectors.npy` [676]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 676 or target_col == 676). Every well: [[GATB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
