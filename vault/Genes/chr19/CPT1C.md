---
symbol: "CPT1C"
type: "gene"
col: 9763
ensembl_id: "ENSG00000169169"
name: "carnitine palmitoyltransferase 1C"
location: "19q13.33"
module: 53
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CPT1C

*carnitine palmitoyltransferase 1C* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.90× (z +19.7, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.568× (z -5.0, q 3e-04, down in 13 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.124×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM41]] (+0.81, fdr 7e-06), [[FNDC7]] (+0.80, fdr 7e-06), [[PYGM]] (+0.80, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.90×** | +19.7 | 0e+00 | 29/32 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +12.5 | 2e-33 | 22/31 (LOX-IMVI, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.94×** | +11.6 | 1e-28 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.17×** | +10.1 | 6e-22 | 28/43 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.91×** | +9.4 | 8e-19 | 27/40 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.79×** | +8.6 | 5e-16 | 6/10 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.16×** | +6.7 | 1e-09 | 3/11 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 20/41 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.26×** | +6.6 | 2e-09 | 0/4 | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.18×** | +6.6 | 3e-09 | 13/25 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.2 | 1e-05 | 7/41 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +5.1 | 1e-05 | 15/37 (SW480, HOP62, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +4.9 | 5e-05 | 12/44 (A498, SW480, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.79×** | +4.8 | 7e-05 | 13/40 (C-33 A, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.66×** | +4.4 | 4e-04 | 12/42 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.1 | 0.002 | 12/43 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[EX229 (drug)]] 5 µM |  | **2.36×** | +3.9 | 0.003 | 0/22 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.003 | 7/39 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.083 | 0/42 | top dose only |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.100 | 2/40 (SHP-77, KATO III) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9763.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HEC-1-A 0.124×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -5.0 | 3e-04 | 13/39 (HEC-1-A, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.699× | -3.2 | 0.30 | 13/43 (HEC-1-A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | 0.506× | -3.2 | 0.30 | 3/23 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 1.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.626 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.792 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.787 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM41]] | +0.81 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.80 | +0.83 / +0.77 | both halves | 7e-06 |  |
| [[PYGM]] | +0.80 | +0.78 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[MIR9-1HG]] | +0.79 | +0.83 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GRAMD2A]] | +0.78 | +0.75 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[AZU1]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[SGSM3-AS1]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CPNE9]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.78 | +0.81 / +0.72 | both halves | 7e-06 |  |
| [[ELAVL3]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 |  |
| [[KIF17]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.77 | +0.80 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPT1C's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F2]] | B | F2 activity raises CPT1C's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.84× lower at baseline in the lines without F2 | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SH2D4B]] | C | SH2D4B activity lowers CPT1C's level | lines that do not express SH2D4B (3) vs lines expressing it (47) | 1.71× higher at baseline in the lines without SH2D4B | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ENSG00000249951, ARHGAP15, B4GALT1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.865). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, -16.4); signed map (16.7, 12.9). **Vector** length 52.1, 6.79% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +19.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.1 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -1.2 |
|  | [[NG25 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.5 | -2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | carnitine palmitoyltransferase 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,690,898-49,713,731 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23809, CPTIC, CPT1P, CATL1 |
| Gene groups (HGNC) | Carnitine palmitoyltransferase family; Thioester hydrolases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCG5](https://www.uniprot.org/uniprotkb/Q8TCG5) (Palmitoyl thioesterase CPT1C):

> Palmitoyl thioesterase specifically expressed in the endoplasmic reticulum of neurons. Modulates the trafficking of the glutamate receptor, AMPAR, to plasma membrane through depalmitoylation of GRIA1. Also regulates AMPR trafficking through the regulation of SACM1L phosphatidylinositol-3-phosphatase activity by interaction in a malonyl-CoA dependent manner (By similarity). Binds malonyl-CoA and couples malonyl-CoA to ceramide levels, necessary for proper spine maturation and contributing to …

**Summary**, from NCBI Gene [126129](https://www.ncbi.nlm.nih.gov/gene/126129):

> This gene encodes a member of the carnitine/choline acetyltransferase family. The encoded protein regulates the beta-oxidation and transport of long-chain fatty acids into mitochondria, and may play a role in the regulation of feeding behavior and whole-body energy homeostasis. Alternatively spliced transcript variants encoding multiple protein isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:18540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18540) · Entrez [126129](https://www.ncbi.nlm.nih.gov/gene/126129) · UniProt [Q8TCG5](https://www.uniprot.org/uniprotkb/Q8TCG5) · Ensembl [ENSG00000169169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169169)

## Data

Gene col 9763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9763); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9763]; `tensor/DDL_lfc|DDL_z.npy` [9763]; `embed/gene_vectors.npy` [9763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9763 or target_col == 9763). Every well: [[CPT1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPT1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
