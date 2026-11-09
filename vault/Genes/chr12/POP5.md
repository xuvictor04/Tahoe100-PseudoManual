---
symbol: "POP5"
type: "gene"
col: 9444
ensembl_id: "ENSG00000167272"
name: "POP5 ribonuclease P/MRP subunit"
location: "12q24.31"
module: 58
arm: "+"
pooled_cpm: 5.63
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# POP5

*POP5 ribonuclease P/MRP subunit* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.36× (z +11.1, q 5e-26, up in 47 of 47 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.48× (z +4.2, q 0.001, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.582× (z -4.1, q 0.025, down in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0706×; ⚠ cell-cycle shift, explains ~90% of this change).
> Its strongest partners by |cos| (71 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 30 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP25]] (+0.69, fdr 4e-05), [[CDK5]] (+0.66, fdr 6e-05), [[REX1BD]] (+0.63, fdr 1e-04); moves opposite to [[RBM3]] (-0.60, fdr 4e-04), [[PSMD6-AS1]] (-0.54, fdr 6e-04), [[CHMP3]] (-0.54, fdr 0.002, ⚠ one half only (not replicated)), [[RRAGC-DT]] (-0.54, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 17 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9444.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **4.36×** | +11.1 | 5e-26 | 47/47 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **4.16×** | +10.8 | 1e-24 | 46/46 (LoVo, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **4.09×** | +10.2 | 2e-22 | 8/10 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **3.81×** | +10.1 | 7e-22 | 46/47 (LoVo, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **3.06×** | +8.4 | 4e-15 | 24/27 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.39×** | +6.3 | 3e-08 | 26/31 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.79×** | +6.2 | 4e-08 | 25/40 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **2.07×** | +5.1 | 2e-05 | 13/16 (HS-578T, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +4.5 | 5e-04 | 21/40 (LOX-IMVI, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.77×** | +4.3 | 1e-03 | 21/47 (RKO, SW 900, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.80×** | +4.3 | 1e-03 | 15/34 (HEC-1-A, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.2 | 0.001 | 22/46 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.007 | 15/46 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.68×** | +3.8 | 0.007 | 18/40 (HOP62, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.67×** | +3.7 | 0.007 | 20/43 (LS 180, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.022 | 13/43 (NCI-H1792, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9444.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0706×; ⚠ cell-cycle shift, explains ~90% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -4.1 | 0.025 | 19/46 (AsPC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.96 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9444. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0706× (z -11.0) ⚠ cell-cycle shift, explains ~90% of this change |
| [[A-172 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9444), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 27 of them with an alert (⚠; 26 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP25]] | +0.69 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[CDK5]] | +0.66 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[REX1BD]] | +0.63 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[POLR3K]] | +0.61 | +0.37 / +0.63 | both halves | 8e-05 |  |
| [[MICOS13]] | +0.60 | +0.25 / +0.59 | both halves | 4e-04 |  |
| [[MRPL12]] | +0.59 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[SLC25A11]] | +0.59 | +0.30 / +0.60 | both halves | 2e-04 |  |
| [[MRPS12]] | +0.59 | +0.36 / +0.61 | both halves | 1e-04 | STRING 410 |
| [[EXOSC4]] | +0.58 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[MRPL57]] | +0.58 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[POP7]] | +0.58 | +0.23 / +0.56 | both halves | 5e-04 | same gene group; pathway: tRNA processing; STRING 999 |
| [[ANTKMT]] | +0.58 | +0.24 / +0.58 | both halves | 4e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM3]] | -0.60 | -0.25 / -0.60 | both halves | 4e-04 |  |
| [[PSMD6-AS1]] | -0.54 | -0.22 / -0.49 | both halves | 6e-04 |  |
| [[CHMP3]] | -0.54 | -0.13 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[RRAGC-DT]] | -0.54 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ATN1]] | -0.53 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[CHD3]] | -0.51 | -0.23 / -0.45 | both halves | 5e-04 |  |
| [[PCBP2]] | -0.50 | -0.24 / -0.56 | both halves | 5e-04 |  |
| [[SPON1-AS1]] | -0.50 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[LSMEM1]] | -0.50 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[PIWIL2]] | -0.48 | -0.43 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[GALNT7-DT]] | -0.48 | -0.21 / -0.25 | both halves | 6e-04 |  |
| [[PPP1R3F]] | -0.48 | -0.25 / -0.26 | both halves | 4e-04 |  |
| [[TAS2R4]] | -0.47 | -0.29 / -0.28 | both halves | 3e-04 |  |
| [[SMIM15-AS1]] | -0.47 | -0.21 / -0.41 | both halves | 7e-04 |  |
| [[ALOX12-AS1]] | -0.47 | -0.32 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POP5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.5, -14.0); signed map (-26.5, -2.5). **Vector** length 50.4, 7.70% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.5 | +11.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.4 | +10.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.3 | +10.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.5 | -2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.3 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | POP5 ribonuclease P/MRP subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,578,764-120,581,402 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Nuclear RNase P complex subunits; RNase MRP complex subunits |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969H6](https://www.uniprot.org/uniprotkb/Q969H6) (Ribonuclease P/MRP protein subunit POP5):

> Component of ribonuclease P, a protein complex that generates mature tRNA molecules by cleaving their 5'-ends. Also a component of the MRP ribonuclease complex, which cleaves pre-rRNA sequences.

**Summary**, from NCBI Gene [51367](https://www.ncbi.nlm.nih.gov/gene/51367):

> Enables ribonuclease P RNA binding activity. Contributes to ribonuclease P activity. Involved in tRNA 5'-leader removal. Located in nucleolus and nucleoplasm. Part of multimeric ribonuclease P complex and ribonuclease MRP complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17689) · Entrez [51367](https://www.ncbi.nlm.nih.gov/gene/51367) · UniProt [Q969H6](https://www.uniprot.org/uniprotkb/Q969H6) · Ensembl [ENSG00000167272](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167272)

## Data

Gene col 9444: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9444); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9444, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9444]; `tensor/DDL_lfc|DDL_z.npy` [9444]; `embed/gene_vectors.npy` [9444]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9444 or target_col == 9444). Every well: [[POP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
