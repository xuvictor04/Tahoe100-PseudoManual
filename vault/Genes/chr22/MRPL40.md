---
symbol: "MRPL40"
type: "gene"
col: 11701
ensembl_id: "ENSG00000185608"
name: "mitochondrial ribosomal protein L40"
location: "22q11.21"
module: 58
arm: "+"
pooled_cpm: 8.44
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MRPL40

*mitochondrial ribosomal protein L40* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +9.6, q 5e-19, up in 15 of 16 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.52× (z +4.5, q 6e-04, up in 25 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 5.68×, A498 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.447× (z -6.2, q 4e-07, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNAPIN]] (+0.71, fdr 7e-06), [[MRPL57]] (+0.70, fdr 7e-06), [[HDDC3]] (+0.69, fdr 1e-05); moves opposite to [[NPIPB11]] (-0.57, fdr 9e-05), [[SLC25A53]] (-0.56, fdr 2e-05), [[ARL17A]] (-0.55, fdr 3e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC44A2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11701.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 5.68×, A498 5.22×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.70×** | +9.6 | 5e-19 | 15/16 (HT-29, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.43×** | +9.4 | 2e-18 | 32/33 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.58×** | +6.7 | 5e-09 | 22/22 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.95×** | +5.1 | 6e-05 | 30/38 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.82×** | +4.5 | 6e-04 | 22/47 (SK-MEL-2, J82, …) | two highest doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +4.5 | 6e-04 | 25/47 (SK-MEL-2, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +4.5 | 7e-04 | 27/46 (NCI-H1573, SNU-423, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +3.6 | 0.021 | 6/48 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.58×** | +3.5 | 0.033 | 17/47 (SK-MEL-2, A498, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.1 | 0.12 | 16/36 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~16% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -6.2 | 4e-07 | 37/46 (AsPC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.466×** | -5.8 | 1e-06 | 39/47 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -5.8 | 1e-06 | 32/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.554×** | -4.5 | 9e-04 | 25/46 (C32, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -3.9 | 0.010 | 22/42 (HT-29, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.720×** | -3.6 | 0.033 | 25/45 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | 0.400× | -3.1 | 0.15 | 17/40 (RKO, A-427, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 3.58 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0382× (z -10.1) |
| [[HT-29 (line)]] | alt | 9.32 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -9.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -9.9) |
| [[PANC-1 (line)]] | alt | 8.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[SNU-423 (line)]] | alt | 9.47 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.118× (z -8.7) |
| [[A-172 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNAPIN]] | +0.71 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MRPL57]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 881 |
| [[HDDC3]] | +0.69 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[MLST8]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.67 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[NDUFAF3]] | +0.66 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[COMMD8]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[THYN1]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NDUFB10]] | +0.64 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[TRAPPC5]] | +0.64 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[DNAJC19]] | +0.63 | +0.36 / +0.69 | both halves | 1e-04 |  |
| [[RPUSD3]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB11]] | -0.57 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[SLC25A53]] | -0.56 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ARL17A]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[CAPN15]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A2]] | C | SLC44A2 activity raises MRPL40's level | lines that do not express SLC44A2 (4) vs lines expressing it (46) | 1.49× lower at baseline in the lines without SLC44A2 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC45, CLSPN, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.6, -11.7); signed map (-20.9, -4.5). **Vector** length 50.8, 8.29% of its response variance represented; |z| ≥ 3 in 693 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.4 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.0 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +1.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.8 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -0.9 | -2.9 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L40 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:19,432,545-19,436,075 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MRP-L22, mL40; previously NLVCF |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Hallmark sets | DNA_REPAIR |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NQ50](https://www.uniprot.org/uniprotkb/Q9NQ50) carries no function annotation.

**Summary**, from NCBI Gene [64976](https://www.ncbi.nlm.nih.gov/gene/64976):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14491) · Entrez [64976](https://www.ncbi.nlm.nih.gov/gene/64976) · UniProt [Q9NQ50](https://www.uniprot.org/uniprotkb/Q9NQ50) · Ensembl [ENSG00000185608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185608)

## Data

Gene col 11701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11701); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11701]; `tensor/DDL_lfc|DDL_z.npy` [11701]; `embed/gene_vectors.npy` [11701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11701 or target_col == 11701). Every well: [[MRPL40 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL40.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
