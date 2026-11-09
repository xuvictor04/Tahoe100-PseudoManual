---
symbol: "KIFC2"
type: "gene"
col: 9523
ensembl_id: "ENSG00000167702"
name: "kinesin family member C2"
location: "8q24.3"
module: 2
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KIFC2

*kinesin family member C2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.33× (z +10.8, q 1e-24, up in 29 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.99× (z +6.2, q 9e-08, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.489× (z -6.4, q 8e-08, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKQ]] (+0.64, fdr 1e-05), [[SBF1]] (+0.63, fdr 8e-06), [[ANO8]] (+0.63, fdr 1e-05); moves opposite to [[SMIM15]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9523.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.33×** | +10.8 | 1e-24 | 29/31 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.93×** | +9.3 | 3e-18 | 15/16 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +6.2 | 9e-08 | 35/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.81×** | +5.5 | 4e-06 | 31/37 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.40×** | +4.7 | 3e-04 | 26/37 (SW1417, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.7 | 3e-04 | 23/42 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 3e-04 | 20/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.29×** | +4.4 | 6e-04 | 25/41 (LoVo, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +4.2 | 0.002 | 10/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **2.17×** | +4.1 | 0.002 | 15/44 (NCI-H2347, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.002 | 20/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.07×** | +3.9 | 0.004 | 14/43 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +3.6 | 0.014 | 12/47 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.014 | 17/41 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.028 | 14/45 (HOP62, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.075 | 15/43 (NCI-H460, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.74×** | +3.0 | 0.086 | 5/39 (CFPAC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.086 | 13/39 (NCI-H2347, C32, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9523.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.489×** | -6.4 | 8e-08 | 28/46 (LOX-IMVI, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.593×** | -4.0 | 0.015 | 14/40 (LoVo, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.639×** | -3.8 | 0.029 | 12/44 (SNU-1, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.692× | -3.3 | 0.14 | 14/46 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 9.74 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.130× (z -9.4) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0806× (z -8.5) |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0923× (z -8.7) |
| [[LoVo (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 8.55 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.35× (z +10.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 6.28 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.61× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 8.70 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0864× (z -9.0) ⚠ toxic |
| [[SW48 (line)]] | wt | 14.7 | 0 | 1 | — | [[Vandetanib (drug)]] 0.05 µM 0.0641× (z -10.5) |
| [[A-172 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKQ]] | +0.64 | +0.55 / +0.61 | both halves | 1e-05 | STRING 446 |
| [[SBF1]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[ANO8]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RHOT2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PGAP6]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[GNA11]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[MEX3D]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DGAT1]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NSMF]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[GDI1]] | +0.58 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[PCBP4]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[UCKL1]] | +0.57 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.641). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-9.3, -22.9); signed map (-26.8, 2.0). **Vector** length 67.6, 14.1% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +10.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +3.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.9 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.7 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -3.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,466,043-144,474,202 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AC6](https://www.uniprot.org/uniprotkb/Q96AC6) (Kinesin-like protein KIFC2):

> May play a role in microtubule-dependent retrograde axonal transport. May function as the motor for the transport of multivesicular body (MVB)-like organelles in dendrites (By similarity).

**Summary**, from NCBI Gene [90990](https://www.ncbi.nlm.nih.gov/gene/90990):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and plus-end-directed microtubule motor activity. Predicted to be involved in anterograde dendritic transport of neurotransmitter receptor complex; axon guidance; and synaptic vesicle transport. Predicted to be located in cytoskeleton and dendrite cytoplasm. Predicted to be part of kinesin complex. Predicted to be active in cytoplasm and microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29530) · Entrez [90990](https://www.ncbi.nlm.nih.gov/gene/90990) · UniProt [Q96AC6](https://www.uniprot.org/uniprotkb/Q96AC6) · Ensembl [ENSG00000167702](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167702)

## Data

Gene col 9523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9523); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9523]; `tensor/DDL_lfc|DDL_z.npy` [9523]; `embed/gene_vectors.npy` [9523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9523 or target_col == 9523). Every well: [[KIFC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIFC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
