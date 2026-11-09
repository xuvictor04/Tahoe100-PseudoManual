---
symbol: "DANT1"
type: "gene"
col: 13703
ensembl_id: "ENSG00000229335"
name: "DXZ4 associated non-coding transcript 1, proximal"
location: "Xq23"
module: 10
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 38
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# DANT1

*DXZ4 associated non-coding transcript 1, proximal* — Xq23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.15× (z +9.6, q 5e-19, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +4.2, q 0.003, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.607× (z -4.4, q 0.006, down in 10 of 30 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFPL1S]] (+0.64, fdr 1e-05), [[ADGRB1]] (+0.56, fdr 3e-05), [[MYADM-AS1]] (+0.55, fdr 2e-05); moves opposite to [[DBT]] (-0.43, fdr 4e-04), [[NSL1]] (-0.42, fdr 1e-04), [[ABITRAM]] (-0.41, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.6 | 5e-19 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +8.8 | 5e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.66×** | +7.5 | 1e-11 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.003 | 2/20 (A498, RPMI-7951) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.0 | 0.007 | 0/8 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.038 | 1/26 (NCI-H23) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.3 | 0.085 | 0/5 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.607×** | -4.4 | 0.006 | 10/30 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.618×** | -4.2 | 0.006 | 9/21 (HEC-1-A, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.623×** | -4.1 | 0.006 | 12/30 (HEC-1-A, SW48, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.625×** | -4.1 | 0.006 | 14/27 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.626×** | -3.9 | 0.010 | 10/24 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.629×** | -3.9 | 0.010 | 8/32 (CFPAC-1, HepG2/C3A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.644×** | -3.8 | 0.010 | 12/33 (HEC-1-A, SW48, …) | rises with dose |  |
| [[Flutamide (drug)]] 0.5 µM |  | **0.649×** | -3.8 | 0.011 | 10/25 (SW48, H4, …) | inconsistent across doses |  |
| [[IQ 1 (drug)]] 0.05 µM |  | **0.676×** | -3.2 | 0.078 | 2/28 (NCI-H460, NCI-H2030) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.698×** | -3.1 | 0.095 | 11/29 (HEC-1-A, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0831× (z -11.2) |
| [[A549 (line)]] | wt | 6.47 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0502× (z -12.2) ⚠ cell-cycle shift, explains ~98% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0446× (z -9.0) |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0142× (z -12.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 45.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0952× (z -8.9) ⚠ cell-cycle shift, explains ~98% of this change |
| [[A-172 (line)]] | wt | 0.755 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.591 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.655 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.983 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.743 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.980 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.834 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.646 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFPL1S]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 | same gene group |
| [[ADGRB1]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[MYADM-AS1]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CAPN14]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[RNF215]] | +0.54 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[SSPOP]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ANKS1B]] | +0.53 | +0.47 / +0.32 | both halves | 2e-04 |  |
| [[MIR1915HG]] | +0.53 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SLC6A11]] | +0.52 | +0.31 / +0.20 | both halves | 7e-04 |  |
| [[LINC02026]] | +0.51 | +0.59 / +0.30 | both halves | 2e-04 |  |
| [[LINC02384]] | +0.50 | +0.37 / +0.42 | both halves | 9e-05 |  |
| [[AGBL2]] | +0.50 | +0.31 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DBT]] | -0.43 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[NSL1]] | -0.42 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[ABITRAM]] | -0.41 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[ISCA2]] | -0.40 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[PPP1R7]] | -0.40 | -0.28 / -0.35 | both halves | 3e-04 |  |
| [[ACOT8]] | -0.40 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[BLOC1S5]] | -0.40 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.39 | -0.25 / -0.34 | both halves | 4e-04 |  |
| [[CNEP1R1]] | -0.39 | -0.33 / -0.29 | both halves | 2e-04 |  |
| [[NUDT12]] | -0.39 | -0.29 / -0.32 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.359). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.8, 33.0); signed map (37.5, -6.9). **Vector** length 34.1, 4.17% of its response variance represented; |z| ≥ 3 in 802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.3 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | +1.2 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +0.8 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +0.6 | +0.8 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +0.6 | +1.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.6 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | -0.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.6 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.0 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -3.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DXZ4 associated non-coding transcript 1, proximal |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq23 — chrX:115,840,899-115,908,066 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50863) · Entrez [106029310](https://www.ncbi.nlm.nih.gov/gene/106029310) · Ensembl [ENSG00000229335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229335)

## Data

Gene col 13703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13703); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13703]; `tensor/DDL_lfc|DDL_z.npy` [13703]; `embed/gene_vectors.npy` [13703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13703 or target_col == 13703). Every well: [[DANT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DANT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
