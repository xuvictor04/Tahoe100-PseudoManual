---
symbol: "ADCK5"
type: "gene"
col: 10343
ensembl_id: "ENSG00000173137"
name: "aarF domain containing kinase 5"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ADCK5

*aarF domain containing kinase 5* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.37× (z +15.4, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.530× (z -6.6, q 2e-08, down in 21 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.571× (z -5.8, q 1e-06, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFYVE21]] (+0.70, fdr 9e-06), [[CAPN10]] (+0.69, fdr 1e-05), [[TELO2]] (+0.69, fdr 1e-05); moves opposite to [[LACTB2]] (-0.55, fdr 3e-04), [[ARMCX5-GPRASP2]] (-0.54, fdr 1e-04), [[RIPK2-DT]] (-0.53, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.37×** | +15.4 | 0e+00 | 45/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.36×** | +12.7 | 3e-34 | 42/44 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.67×** | +10.3 | 2e-22 | 37/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.9 | 7e-10 | 21/37 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +3.9 | 0.011 | 1/8 (NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.6 | 0.033 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.3 | 0.087 | 10/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.51× | +3.1 | 0.13 | 3/32 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.34× | +3.1 | 0.13 | 3/42 (LoVo, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Omeprazole (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.15 | 3/39 (C32, A549, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.530×** | -6.6 | 2e-08 | 21/34 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -5.8 | 1e-06 | 22/46 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.649×** | -4.3 | 0.003 | 16/41 (NCI-H23, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -4.0 | 0.009 | 19/43 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.693×** | -3.8 | 0.015 | 10/44 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -3.8 | 0.015 | 13/40 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.3 | 0.068 | 9/43 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **0.800×** | -3.3 | 0.068 | 5/44 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.738× | -3.1 | 0.14 | 11/43 (BT-474, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.83 | 0 | 3 (2 ⚠) | — | [[Canagliflozin (drug)]] 5 µM 0.0916× (z -9.4) |
| [[KATO III (line)]] | alt | 4.72 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0702× (z -10.2) |
| [[SW480 (line)]] | alt | 3.24 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 7.72× (z +8.5) | [[Menadione (drug)]] 0.05 µM 0.0709× (z -10.3) |
| [[A498 (line)]] | wt | 4.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0795× (z -11.0) ⚠ cell-cycle shift, explains ~82% of this change |
| [[C32 (line)]] | wt | 5.03 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0676× (z -8.6) |
| [[J82 (line)]] | alt | 5.29 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -9.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE21]] | +0.70 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[CAPN10]] | +0.69 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TELO2]] | +0.69 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.68 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[SBF1]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ZDHHC8]] | +0.68 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[CPSF1]] | +0.67 | +0.56 / +0.59 | both halves | 1e-05 | STRING 628; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[KLHL17]] | +0.66 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[DGKQ]] | +0.64 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[ABHD17A]] | +0.63 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[CHTF18]] | +0.63 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[AKT1]] | +0.62 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.61 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LACTB2]] | -0.55 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.54 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[RIPK2-DT]] | -0.53 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ZNF711]] | -0.53 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ADCK5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.785). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.8, -23.2); signed map (-44.8, -10.7). **Vector** length 47.4, 5.42% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.2 | +15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +12.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.3 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | aarF domain containing kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,373,101-144,393,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35454 |
| Gene groups (HGNC) | ADCK family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MIX3](https://www.uniprot.org/uniprotkb/Q3MIX3) (Uncharacterized aarF domain-containing protein kinase 5):

> The function of this protein is not yet clear. It is not known if it has protein kinase activity and what type of substrate it would phosphorylate (Ser, Thr or Tyr).

**Summary**, from NCBI Gene [203054](https://www.ncbi.nlm.nih.gov/gene/203054):

> Predicted to enable protein serine/threonine kinase activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21738](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21738) · Entrez [203054](https://www.ncbi.nlm.nih.gov/gene/203054) · UniProt [Q3MIX3](https://www.uniprot.org/uniprotkb/Q3MIX3) · Ensembl [ENSG00000173137](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173137)

## Data

Gene col 10343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10343); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10343]; `tensor/DDL_lfc|DDL_z.npy` [10343]; `embed/gene_vectors.npy` [10343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10343 or target_col == 10343). Every well: [[ADCK5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADCK5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
