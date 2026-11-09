---
symbol: "ALKBH4"
type: "gene"
col: 8405
ensembl_id: "ENSG00000160993"
name: "alkB homolog 4, lysine demethylase"
location: "7q22.1"
module: 119
arm: "+"
pooled_cpm: 6.48
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# ALKBH4

*alkB homolog 4, lysine demethylase* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.49× (z +4.1, q 0.015, up in 14 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.607× (z -5.1, q 2e-04, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL44]] (+0.77, fdr 7e-06), [[TEFM]] (+0.76, fdr 7e-06), [[TTF1]] (+0.75, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.60, fdr 3e-05), [[SMG1P3]] (-0.59, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PAQR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.015 | 14/46 (BT-474, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.015 | 13/48 (RKO, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.41× | +3.5 | 0.10 | 12/34 (KATO III, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.38× | +3.4 | 0.10 | 10/35 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Darinaparsin (drug)]] 5 µM |  | 1.25× | +3.3 | 0.12 | 7/48 (Hs 766T, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.36× | +3.2 | 0.14 | 3/47 (PANC-1, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8405.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.607×** | -5.1 | 2e-04 | 23/47 (SNU-423, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.621×** | -4.9 | 3e-04 | 20/32 (NCI-H460, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.615×** | -4.8 | 3e-04 | 17/37 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.634×** | -4.7 | 4e-04 | 17/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.660×** | -4.3 | 0.002 | 18/47 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.669×** | -4.0 | 0.007 | 18/45 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -3.6 | 0.027 | 18/46 (HS-578T, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.715×** | -3.4 | 0.043 | 14/44 (A-172, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.718×** | -3.4 | 0.044 | 10/47 (SW1417, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.064 | 15/42 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ivermectin (drug)]] 5 µM |  | **0.729×** | -3.2 | 0.064 | 4/47 (A498, SW480, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -3.2 | 0.071 | 15/43 (Panc 03.27, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.073 | 12/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.731×** | -3.1 | 0.084 | 10/40 (A549, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 6.36 | 0 | 3 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0970× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.87 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.177× (z -9.7) |
| [[C32 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -9.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 6.00 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0762× (z -8.9) |
| [[A-172 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL44]] | +0.77 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TEFM]] | +0.76 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[TTF1]] | +0.75 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.75 | +0.64 / +0.80 | both halves | 7e-06 |  |
| [[COIL]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.74 | +0.74 / +0.69 | both halves | 7e-06 | same gene group; STRING 955 |
| [[TIMM29]] | +0.73 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.72 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[SLC4A1AP]] | +0.72 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[NGDN]] | +0.71 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[PHAX]] | +0.71 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TMEM79]] | +0.69 | +0.58 / +0.68 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.60 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[SMG1P3]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR7]] | B | PAQR7 activity raises ALKBH4's level | lines that do not express PAQR7 (5) vs lines expressing it (45) | 1.18× lower at baseline in the lines without PAQR7 | 0.079 | ⚠ within organs, on part of the lines; also absent: DBN1, VASN, LTBP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.4, 7.1); signed map (-9.0, -12.1). **Vector** length 64.9, 10.8% of its response variance represented; |z| ≥ 3 in 722 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.6 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.0 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 4, lysine demethylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,456,238-102,464,863 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20013 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXW9](https://www.uniprot.org/uniprotkb/Q9NXW9) (Alpha-ketoglutarate-dependent dioxygenase alkB homolog 4):

> Dioxygenase that mediates demethylation of actin monomethylated at 'Lys-84' (K84me1), thereby acting as a regulator of actomyosin-processes. Demethylation of actin K84me1 is required for maintaining actomyosin dynamics supporting normal cleavage furrow ingression during cytokinesis and cell migration. In addition to proteins, also demethylates DNA: specifically demethylates DNA methylated on the 6th position of adenine (N(6)-methyladenosine) DNA, thereby regulating Polycomb silencing (By …

**Summary**, from NCBI Gene [54784](https://www.ncbi.nlm.nih.gov/gene/54784):

> Enables 2-oxoglutarate-dependent dioxygenase activity and actin binding activity. Involved in actomyosin structure organization and cleavage furrow ingression. Located in contractile ring and midbody. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21900) · Entrez [54784](https://www.ncbi.nlm.nih.gov/gene/54784) · UniProt [Q9NXW9](https://www.uniprot.org/uniprotkb/Q9NXW9) · Ensembl [ENSG00000160993](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160993)

## Data

Gene col 8405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8405); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8405]; `tensor/DDL_lfc|DDL_z.npy` [8405]; `embed/gene_vectors.npy` [8405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8405 or target_col == 8405). Every well: [[ALKBH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
