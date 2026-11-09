---
symbol: "FAM131B-AS2"
type: "gene"
col: 13850
ensembl_id: "ENSG00000232533"
name: "FAM131B antisense RNA 2"
location: "7q34"
module: 101
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# FAM131B-AS2

*FAM131B antisense RNA 2* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.77× (z +6.6, q 2e-08, up in 16 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.52× (z +3.8, q 0.023, up in 14 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.421× (z -5.6, q 1e-05, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MILIP]] (+0.70, fdr 7e-06), [[PPP1R14B-AS1]] (+0.69, fdr 1e-05), [[C14orf119]] (+0.64, fdr 1e-05); moves opposite to [[RPA1]] (-0.63, fdr 7e-06), [[NUDT21]] (-0.60, fdr 1e-05), [[ANAPC5]] (-0.60, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.77×** | +6.6 | 2e-08 | 16/23 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +4.5 | 0.002 | 3/7 (NCI-H2030, A498, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.023 | 14/44 (H4, NCI-H2030, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.78×** | +3.7 | 0.025 | 10/20 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +3.7 | 0.026 | 3/9 (HS-578T, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.4 | 0.057 | 5/19 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | 1.66× | +3.2 | 0.12 | 13/43 (KATO III, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 1.40× | +3.1 | 0.14 | 13/42 (HOP62, LS 180, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.60× | +3.0 | 0.16 | 9/32 (SW1417, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -5.6 | 1e-05 | 28/45 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -5.4 | 1e-05 | 21/40 (A549, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -4.0 | 0.010 | 19/40 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.543×** | -4.0 | 0.011 | 18/44 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.556×** | -3.8 | 0.014 | 20/40 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.557×** | -3.8 | 0.014 | 16/44 (HS-578T, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.573×** | -3.4 | 0.053 | 15/39 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Tadalafil (drug)]] 5 µM |  | 0.611× | -3.1 | 0.15 | 13/41 (HEC-1-A, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.72 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0316× (z -10.3) |
| [[A-172 (line)]] | wt | 6.04 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0777× (z -8.8) |
| [[PANC-1 (line)]] | alt | 2.92 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0823× (z -9.2) |
| [[A-427 (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MILIP]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PPP1R14B-AS1]] | +0.69 | +0.52 / +0.71 | both halves | 1e-05 | same gene group |
| [[C14orf119]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF75A]] | +0.64 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DENND3-AS1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[RELA-DT]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[LETM2]] | +0.62 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[STYXL1]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[C11orf91]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[EID2]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NOP14-AS1]] | +0.59 | +0.71 / +0.45 | both halves | 3e-05 | same gene group |
| [[UTP3]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | -0.63 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[NUDT21]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ANAPC5]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[MPHOSPH9]] | -0.59 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[EEF1AKMT2]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[NDUFV1]] | -0.53 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[DDX12P]] | -0.53 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[TBCD]] | -0.53 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[IFT122]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.53 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[PRDX3]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ALG6]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.644). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, -4.5); signed map (1.2, 31.7). **Vector** length 52.6, 8.42% of its response variance represented; |z| ≥ 3 in 744 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +3.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +2.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | FAM131B antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q34 — chr7:143,379,683-143,381,036 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PCAL7 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56141) · Entrez [100507507](https://www.ncbi.nlm.nih.gov/gene/100507507) · Ensembl [ENSG00000232533](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232533)

## Data

Gene col 13850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13850); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13850]; `tensor/DDL_lfc|DDL_z.npy` [13850]; `embed/gene_vectors.npy` [13850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13850 or target_col == 13850). Every well: [[FAM131B-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM131B-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
