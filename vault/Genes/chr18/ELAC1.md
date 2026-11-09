---
symbol: "ELAC1"
type: "gene"
col: 6559
ensembl_id: "ENSG00000141642"
name: "elaC ribonuclease Z 1"
location: "18q21.2"
module: 28
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ELAC1

*elaC ribonuclease Z 1* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.28× (z +9.9, q 2e-20, up in 22 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.383× (z -8.2, q 2e-13, down in 28 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIGD6]] (+0.78, fdr 7e-06), [[ZBED9]] (+0.74, fdr 1e-05), [[BCDIN3D]] (+0.74, fdr 7e-06); moves opposite to [[SBNO1]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[NRIP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +9.9 | 2e-20 | 22/30 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.96×** | +8.9 | 2e-16 | 7/13 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.97×** | +8.2 | 6e-14 | 18/32 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +7.4 | 2e-11 | 20/29 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +5.6 | 2e-06 | 1/2 (A498) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.92×** | +5.6 | 2e-06 | 18/39 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.59×** | +5.6 | 2e-06 | 13/42 (SW480, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +5.4 | 4e-06 | 6/14 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +5.3 | 9e-06 | 15/41 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +4.9 | 5e-05 | 7/21 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.8 | 1e-04 | 0/0 | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +4.7 | 1e-04 | 15/39 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.7 | 0.009 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +3.6 | 0.012 | 9/40 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.48×** | +3.3 | 0.034 | 3/41 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.3 | 0.035 | 1/42 (LS 180) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.048 | 2/42 (LOX-IMVI, MIA PaCa-2) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6559.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.383×** | -8.2 | 2e-13 | 28/40 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.390×** | -8.0 | 3e-13 | 31/43 (SHP-77, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -6.3 | 5e-08 | 15/24 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.541×** | -5.2 | 2e-05 | 20/38 (SW1417, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.675×** | -3.4 | 0.078 | 12/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Gefitinib (drug)]] 5 µM |  | **0.676×** | -3.3 | 0.078 | 8/44 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.682×** | -3.3 | 0.078 | 9/35 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.763×** | -3.3 | 0.078 | 5/42 (RPMI-7951, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0613× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 3.12 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0753× (z -8.5) |
| [[A-172 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.700 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIGD6]] | +0.78 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.74 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[BCDIN3D]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.71 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[TACO1]] | +0.70 | +0.74 / +0.47 | both halves | 2e-05 |  |
| [[C7orf25]] | +0.70 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.70 | +0.79 / +0.45 | both halves | 3e-05 |  |
| [[ARL14EP]] | +0.70 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[TMEM128]] | +0.69 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.69 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[MTHFSD]] | +0.69 | +0.75 / +0.43 | both halves | 3e-05 |  |
| [[METTL18]] | +0.69 | +0.75 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SBNO1]] | -0.61 | -0.66 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRIP1]] | B | NRIP1 activity lowers ELAC1's level | lines that do not express NRIP1 (8) vs lines expressing it (42) | 1.62× higher at baseline in the lines without NRIP1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, ATXN1, ENSG00000232884; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ELAC1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[WHRN]] | C | WHRN activity raises ELAC1's level | lines that do not express WHRN (4) vs lines expressing it (46) | 1.41× lower at baseline in the lines without WHRN | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CLTCL1, NKAIN1, KIAA1549; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.0, 9.4); signed map (5.2, -25.6). **Vector** length 47.2, 5.98% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +7.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +5.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -8.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -8.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | +0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | elaC ribonuclease Z 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:50,967,991-50,988,121 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D29 |
| Gene groups (HGNC) | MBL fold containing DNA/RNA interacting subfamily; Endoribonucleases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H777](https://www.uniprot.org/uniprotkb/Q9H777) (Zinc phosphodiesterase ELAC protein 1):

> Zinc phosphodiesterase, which displays some tRNA 3'-processing endonuclease activity. Specifically involved in tRNA repair: acts downstream of the ribosome-associated quality control (RQC) pathway by removing a 2',3'-cyclic phosphate from tRNAs following cleavage by ANKZF1. tRNAs are then processed by TRNT1.

**Summary**, from NCBI Gene [55520](https://www.ncbi.nlm.nih.gov/gene/55520):

> Enables tRNA-specific ribonuclease activity. Involved in rescue of stalled cytosolic ribosome and tRNA 3'-end processing. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14197) · Entrez [55520](https://www.ncbi.nlm.nih.gov/gene/55520) · UniProt [Q9H777](https://www.uniprot.org/uniprotkb/Q9H777) · Ensembl [ENSG00000141642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141642)

## Data

Gene col 6559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6559); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6559]; `tensor/DDL_lfc|DDL_z.npy` [6559]; `embed/gene_vectors.npy` [6559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6559 or target_col == 6559). Every well: [[ELAC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELAC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
