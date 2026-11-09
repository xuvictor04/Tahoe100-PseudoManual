---
symbol: "FAM27C"
type: "gene"
col: 13797
ensembl_id: "ENSG00000231527"
name: "family with sequence similarity 27 member C"
location: "9q13"
module: 133
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# FAM27C

*family with sequence similarity 27 member C* — 9q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.81× (z +9.1, q 7e-17, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +7.3, q 9e-11, up in 10 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.478× (z -6.9, q 3e-09, down in 19 of 43 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.537× (z -5.8, q 8e-07, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DMGDH]] (+0.62, fdr 3e-05), [[SLC6A9]] (+0.61, fdr 1e-05), [[NBR2]] (+0.61, fdr 3e-05); moves opposite to [[H3-3B]] (-0.52, fdr 2e-04), [[PDHB]] (-0.47, fdr 7e-04), [[HPF1]] (-0.46, fdr 4e-04).
> It is in [[Module 133]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +9.1 | 7e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +7.3 | 9e-11 | 10/27 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.7 | 2e-06 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.1 | 0.007 | 4/36 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.35×** | +4.0 | 0.007 | 1/41 (MIA PaCa-2) | rises with dose | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.9 | 0.008 | 1/18 (SW480) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.4 | 0.060 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.083 | 4/23 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.40× | +3.1 | 0.11 | 1/35 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.478×** | -6.9 | 3e-09 | 19/43 (KATO III, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.520×** | -6.1 | 3e-07 | 19/39 (LoVo, C-33 A, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.637×** | -6.0 | 4e-07 | 21/30 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.537×** | -5.8 | 8e-07 | 17/42 (SNU-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.556×** | -5.2 | 3e-05 | 10/36 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.593×** | -4.9 | 1e-04 | 14/28 (LS 180, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.685×** | -3.5 | 0.032 | 14/40 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.695×** | -3.4 | 0.047 | 12/34 (C32, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.699×** | -3.4 | 0.050 | 8/40 (KATO III, A-427, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.691×** | -3.3 | 0.065 | 8/41 (SW1417, SNU-1, …) | top dose only |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.715×** | -3.1 | 0.086 | 8/38 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.719×** | -3.1 | 0.098 | 12/39 (KATO III, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0724× (z -11.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.739 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.985 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.610 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.698 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DMGDH]] | +0.62 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SLC6A9]] | +0.61 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[NBR2]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[YARS1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[TMEM268]] | +0.60 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[IARS1]] | +0.58 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[PCK2]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[VLDLR-AS1]] | +0.57 | +0.27 / +0.60 | both halves | 3e-04 |  |
| [[MKRN5P]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[GARS1-DT]] | +0.56 | +0.39 / +0.49 | both halves | 5e-05 |  |
| [[MOCOS]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TMPRSS5]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[H3-3B]] | -0.52 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[PDHB]] | -0.47 | -0.20 / -0.46 | both halves | 7e-04 |  |
| [[HPF1]] | -0.46 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[MAP1S]] | -0.46 | -0.40 / -0.26 | both halves | 3e-04 |  |
| [[SLC25A4]] | -0.45 | -0.27 / -0.31 | both halves | 3e-04 |  |
| [[SAV1]] | -0.44 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[TXNDC17]] | -0.44 | -0.26 / -0.34 | both halves | 4e-04 |  |
| [[SNAP29]] | -0.43 | -0.21 / -0.25 | both halves | 7e-04 |  |
| [[SNAPIN]] | -0.43 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[SLC25A11]] | -0.43 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[MEA1]] | -0.43 | -0.30 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.659). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.1, 46.3); signed map (-13.7, 22.3). **Vector** length 35.5, 3.48% of its response variance represented; |z| ≥ 3 in 987 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +0.8 | +0.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.2 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.1 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | +0.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 27 member C |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q13 — chr9:61,854,148-62,096,920 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bA374M1.5, FAM27A3, bA7G23.5, FAM27A1; previously FAM27A |
| Gene groups (HGNC) | Long non-coding RNAs with FAM root symbol |
| Matched by | ensembl_id |

UniProt [Q5VT28](https://www.uniprot.org/uniprotkb/Q5VT28) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23668) · Entrez [100132948](https://www.ncbi.nlm.nih.gov/gene/100132948) · UniProt [Q5VT28](https://www.uniprot.org/uniprotkb/Q5VT28) · Ensembl [ENSG00000231527](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231527)

## Data

Gene col 13797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13797); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13797]; `tensor/DDL_lfc|DDL_z.npy` [13797]; `embed/gene_vectors.npy` [13797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13797 or target_col == 13797). Every well: [[FAM27C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM27C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
