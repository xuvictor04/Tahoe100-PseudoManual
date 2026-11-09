---
symbol: "ADAT3"
type: "gene"
col: 13121
ensembl_id: "ENSG00000213638"
name: "adenosine deaminase tRNA specific 3"
location: "19p13.3"
module: 15
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ADAT3

*adenosine deaminase tRNA specific 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.13× (z +7.3, q 1e-10, up in 6 of 12 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +5.0, q 9e-05, up in 9 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.812× (z -7.5, q 3e-11, down in 32 of 46 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 0.5 µM in 1 line (PANC-1 0.0837×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0784×; ⚠ transcription drop; unreliable plate only).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBL1]] (+0.57, fdr 2e-05), [[CAPN10-DT]] (+0.55, fdr 3e-05), [[MED9]] (+0.55, fdr 1e-05); moves opposite to [[MRPS10]] (-0.56, fdr 3e-05), [[ASF1A]] (-0.53, fdr 1e-05), [[FIBP]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TES]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +7.3 | 1e-10 | 6/12 (HEC-1-A, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.2 | 2e-10 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +5.0 | 9e-05 | 9/46 (COLO 205, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.6 | 5e-04 | 8/23 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.38×** | +4.6 | 5e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.2 | 0.003 | 7/29 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.006 | 10/40 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.7 | 0.013 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.27×** | +3.4 | 0.048 | 2/43 (NCI-H2030, A-172) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.092 | 1/19 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 0.5 µM in 1 line (PANC-1 0.0837×); [[Ivabradine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0784×; ⚠ transcription drop; unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.812×** | -7.5 | 3e-11 | 32/46 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.720× | -3.3 | 0.27 | 7/43 (HT-29, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Isocorydine (drug)]] 5 µM |  | 0.805× | -3.1 | 0.38 | 3/45 (Hs 766T, H4, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.55 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0784× (z -8.5) ⚠ transcription drop; unreliable plate only |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0837× (z -9.0) |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBL1]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CAPN10-DT]] | +0.55 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[MED9]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[PCGF3]] | +0.55 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CTC-338M12.4]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[STAG3L4-1]] | +0.55 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[BCL7C]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[SCAMP4]] | +0.54 | +0.56 / +0.38 | both halves | 6e-05 | STRING 446; ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of SCAMP4 on the same strand (can correlate by spillover, not regulation) |
| [[SMG1P5]] | +0.54 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[RBM14-RBM4]] | +0.53 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[PTDSS2]] | +0.53 | +0.67 / +0.36 | both halves | 1e-04 |  |
| [[ATPAF2]] | +0.53 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[CTTN-DT]] | +0.53 | +0.23 / +0.50 | both halves | 5e-04 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS10]] | -0.56 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[ASF1A]] | -0.53 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[FIBP]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ZNF184]] | -0.52 | -0.53 / -0.36 | both halves | 9e-05 |  |
| [[BBS10]] | -0.51 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[TRMT1L]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SF3B1]] | -0.50 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[SCOC]] | -0.50 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[DZIP3]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[SNAPIN]] | -0.48 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SFR1]] | -0.48 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[MIF4GD]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TES]] | B | TES activity lowers ADAT3's level | lines that do not express TES (8) vs lines expressing it (42) | 1.18× higher at baseline in the lines without TES | 0.060 | ⚠ within organs, on part of the lines; also absent: FAM241A, GPR39, TBC1D8B; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.419). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.7, 0.2); signed map (-3.5, -1.3). **Vector** length 28.3, 1.98% of its response variance represented; |z| ≥ 3 in 1,072 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +7.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +1.2 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +1.1 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +0.7 | +2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +0.7 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.8 | -1.9 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -0.8 | -0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.7 | -1.8 |
|  | [[Lumateperone (tosylate) (drug)]] 0.5 µM |  | -0.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | adenosine deaminase tRNA specific 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,905,399-1,913,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAD3 |
| Gene groups (HGNC) | Adenosine deaminases acting on RNA |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY9](https://www.uniprot.org/uniprotkb/Q96EY9) (tRNA-specific adenosine-34 deaminase regulatory subunit ADAT3):

> Non-catalytic subunit of the tRNA-specific adenosine-34 deaminase complex, composed of the ADAT2 catalytic subunit and the ADAT3 regulatory subunit, which deaminates adenosine-34 (the first, also called wobble position of the anticodon) to inosine in many tRNAs. Inosine-34 allows the decoding of 3 different nucleotides at the third position of mRNA codons, as inosine is able to pair with U, C, and A. Required for binding of the ADAT2-ADAT3 complex to tRNA through its N-terminus, which rotates …

**Summary**, from NCBI Gene [113179](https://www.ncbi.nlm.nih.gov/gene/113179):

> This gene encodes a subunit of a tRNA-specific adenosine deaminase. This heterodimeric enzyme converts adenosine to inosine in the tRNA anticodon. A mutation in this gene causes a syndrome characterized by intellectual disability and strabismus. This gene shares its 5' exon with the overlapping gene, secretory carrier membrane protein 4 (Gene ID: 113178). [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:25151](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25151) · Entrez [113179](https://www.ncbi.nlm.nih.gov/gene/113179) · UniProt [Q96EY9](https://www.uniprot.org/uniprotkb/Q96EY9) · Ensembl [ENSG00000213638](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213638)

## Data

Gene col 13121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13121); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13121]; `tensor/DDL_lfc|DDL_z.npy` [13121]; `embed/gene_vectors.npy` [13121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13121 or target_col == 13121). Every well: [[ADAT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
