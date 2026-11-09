---
symbol: "C7orf25"
type: "gene"
col: 5833
ensembl_id: "ENSG00000136197"
name: "chromosome 7 open reading frame 25"
location: "7p14.1"
module: 16
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# C7orf25

*chromosome 7 open reading frame 25* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.37× (z +9.2, q 3e-17, up in 33 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 2.38× (z +7.1, q 2e-10, up in 31 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.493× (z -5.8, q 4e-06, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX20]] (+0.79, fdr 7e-06), [[ZNF747]] (+0.76, fdr 7e-06), [[CENPBD1P]] (+0.74, fdr 7e-06); moves opposite to [[UQCRH]] (-0.67, fdr 7e-06), [[SDHAP2]] (-0.65, fdr 1e-05), [[HSPB11]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5833.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.37×** | +9.2 | 3e-17 | 33/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +8.0 | 3e-13 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.38×** | +7.1 | 2e-10 | 31/44 (HEC-1-A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +5.1 | 5e-05 | 9/45 (SW1417, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.0 | 6e-05 | 2/5 (J82, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.0 | 6e-05 | 10/35 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +4.7 | 2e-04 | 18/42 (A-427, NCI-H2347, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +4.5 | 4e-04 | 13/35 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.5 | 5e-04 | 8/17 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +4.4 | 6e-04 | 16/42 (HEC-1-A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.012 | 11/45 (A-172, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.61×** | +3.7 | 0.012 | 2/29 (A-172, HEC-1-A) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.5 | 0.022 | 5/19 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.022 | 8/33 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.027 | 9/40 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.061 | 2/44 (PANC-1, KATO III) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.061 | 3/44 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.067 | 7/40 (A-427, SW48, …) | inconsistent across doses | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **1.44×** | +3.0 | 0.075 | 4/43 (HCT15, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5833.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.493×** | -5.8 | 4e-06 | 21/42 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.581×** | -4.4 | 0.003 | 18/46 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -4.3 | 0.003 | 20/44 (LoVo, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.626×** | -3.8 | 0.019 | 12/42 (SHP-77, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -3.4 | 0.080 | 11/29 (A-427, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5833. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.96 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.121× (z -9.1) ⚠ toxic |
| [[A-427 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.942 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5833), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX20]] | +0.79 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[ZNF747]] | +0.76 | +0.81 / +0.62 | both halves | 7e-06 |  |
| [[CENPBD1P]] | +0.74 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.74 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[CSTF2T]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[C9orf64]] | +0.73 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[LIG4]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.73 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[IRF2BP1]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[BBS10]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[PABIR1]] | +0.71 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.71 | +0.69 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.67 | -0.67 / -0.59 | both halves | 7e-06 |  |
| [[SDHAP2]] | -0.65 | -0.73 / -0.56 | both halves | 1e-05 |  |
| [[HSPB11]] | -0.64 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.64 | -0.74 / -0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.62 | -0.67 / -0.51 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.62 | -0.62 / -0.57 | both halves | 9e-06 |  |
| [[SLC17A5]] | -0.62 | -0.71 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP1]] | -0.61 | -0.68 / -0.51 | both halves | 1e-05 |  |
| [[TOMM20]] | -0.61 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[QPCTL]] | -0.61 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.59 | -0.66 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.775). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.1, 12.9); signed map (2.0, -29.9). **Vector** length 52.2, 6.98% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +4.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.3 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -5.8 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 7 open reading frame 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:42,909,273-42,912,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PANAD, MGC2821 |
| Matched by | ensembl_id |

UniProt [Q9BPX7](https://www.uniprot.org/uniprotkb/Q9BPX7) carries no function annotation.

**Summary**, from NCBI Gene [79020](https://www.ncbi.nlm.nih.gov/gene/79020):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21703](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21703) · Entrez [79020](https://www.ncbi.nlm.nih.gov/gene/79020) · UniProt [Q9BPX7](https://www.uniprot.org/uniprotkb/Q9BPX7) · Ensembl [ENSG00000136197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136197)

## Data

Gene col 5833: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5833); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5833, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5833]; `tensor/DDL_lfc|DDL_z.npy` [5833]; `embed/gene_vectors.npy` [5833]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5833 or target_col == 5833). Every well: [[C7orf25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C7orf25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
