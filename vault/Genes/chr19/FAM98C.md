---
symbol: "FAM98C"
type: "gene"
col: 5039
ensembl_id: "ENSG00000130244"
name: "tRNA splicing ligase complex subunit 3C"
location: "19q13.2"
module: 20
arm: "-"
pooled_cpm: 7.67
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# FAM98C

*tRNA splicing ligase complex subunit 3C* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.84× (z +6.4, q 1e-07, up in 17 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.52× (z +6.2, q 2e-07, up in 23 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.480× (z -7.6, q 1e-11, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WASHC1]] (+0.67, fdr 7e-06), [[GATAD1]] (+0.67, fdr 7e-06), [[TERF2IP]] (+0.66, fdr 1e-05); moves opposite to [[PRKDC]] (-0.62, fdr 1e-05), [[EIF5A]] (-0.61, fdr 1e-05), [[ICMT]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5039.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.4 | 1e-07 | 17/32 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.2 | 2e-07 | 23/43 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.0 | 9e-05 | 20/36 (A-172, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.9 | 0.015 | 14/38 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +3.7 | 0.022 | 7/14 (A498, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5039.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.480×** | -7.6 | 1e-11 | 37/46 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -5.6 | 6e-06 | 26/47 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -5.5 | 8e-06 | 21/46 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.596×** | -5.4 | 1e-05 | 23/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.617×** | -5.0 | 6e-05 | 22/46 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.622×** | -4.9 | 7e-05 | 22/47 (HOP62, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -4.9 | 8e-05 | 24/45 (HS-578T, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.626×** | -4.9 | 8e-05 | 21/47 (CFPAC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.446×** | -4.4 | 7e-04 | 19/42 (NCI-H2030, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.678×** | -4.0 | 0.003 | 19/46 (NCI-H1792, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Folic acid (drug)]] 5 µM |  | **0.784×** | -3.6 | 0.017 | 12/48 (SW 1088, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.724×** | -3.4 | 0.037 | 15/45 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5039. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.87 | 0 | 2 | — | [[Monocrotaline (drug)]] 5 µM 0.0686× (z -9.1) |
| [[HOP62 (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -10.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5039), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WASHC1]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[GATAD1]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.66 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[SNRNP27]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.62 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[NKAP]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[POLR1H]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ZRSR2]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.62 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[ICMT]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[VMA21]] | -0.61 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.60 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[TGOLN2]] | -0.58 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[G3BP1]] | -0.58 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[TMX1]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PARP1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[DCAF16]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ATP5F1B]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.599). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.7, -30.5); signed map (-7.0, 4.8). **Vector** length 53.9, 8.13% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -7.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | +1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing ligase complex subunit 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:38,403,093-38,409,088 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ44669; previously FAM98C |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RN3](https://www.uniprot.org/uniprotkb/Q17RN3) (Protein TSLIG3C):

> Plays a role in osteoclastogenesis (in vitro).

**Summary**, from NCBI Gene [147965](https://www.ncbi.nlm.nih.gov/gene/147965):

> Predicted to be part of tRNA-splicing ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27119](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27119) · Entrez [147965](https://www.ncbi.nlm.nih.gov/gene/147965) · UniProt [Q17RN3](https://www.uniprot.org/uniprotkb/Q17RN3) · Ensembl [ENSG00000130244](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130244)

## Data

Gene col 5039: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5039); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5039, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5039]; `tensor/DDL_lfc|DDL_z.npy` [5039]; `embed/gene_vectors.npy` [5039]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5039 or target_col == 5039). Every well: [[FAM98C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM98C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
