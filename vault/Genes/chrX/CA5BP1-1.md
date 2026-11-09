---
symbol: "CA5BP1-1"
type: "gene"
col: 16501
ensembl_id: "ENSG00000290746"
name: ""
location: ""
module: 20
arm: "+"
pooled_cpm: 5.4
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CA5BP1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.93× (z +5.0, q 3e-04, up in 22 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.697× (z -4.6, q 0.001, down in 19 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPN1]] (+0.70, fdr 7e-06), [[AGBL5]] (+0.64, fdr 1e-05), [[EOLA2]] (+0.63, fdr 7e-06); moves opposite to [[SIRT6]] (-0.60, fdr 1e-05), [[NEMF]] (-0.56, fdr 2e-05), [[GGT7]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.93×** | +5.0 | 3e-04 | 22/42 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +3.7 | 0.063 | 9/39 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.073 | 16/46 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.087 | 8/41 (NCI-H2030, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.22 | 10/45 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.697×** | -4.6 | 0.001 | 19/45 (COLO 205, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.606×** | -4.5 | 0.001 | 20/42 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.706×** | -4.5 | 0.001 | 13/44 (SNU-1, HCT15, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.612×** | -4.4 | 0.001 | 16/46 (LoVo, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.684×** | -3.4 | 0.053 | 12/45 (HS-578T, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.587×** | -3.4 | 0.053 | 16/35 (SW480, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.688×** | -3.4 | 0.053 | 13/45 (A498, H4, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.689×** | -3.4 | 0.053 | 18/44 (A-427, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.692×** | -3.3 | 0.054 | 13/46 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.783×** | -3.1 | 0.095 | 13/45 (Hs 766T, J82, …) | top dose only | position effect removed |
| [[palbociclib (drug)]] 0.05 µM |  | **0.696×** | -3.1 | 0.100 | 11/44 (H4, SHP-77, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.91 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0856× (z -9.0) |
| [[A-427 (line)]] | wt | 4.94 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.0437× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 4.96 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0597× (z -10.7) |
| [[HOP62 (line)]] | alt | 3.43 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0613× (z -9.6) |
| [[Hs 766T (line)]] | wt | 7.70 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.102× (z -9.2) |
| [[HS-578T (line)]] | alt | 7.83 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0879× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 9.52 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.144× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.126× (z -8.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2347 (line)]] | alt | 4.53 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0699× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 3.72 | 0 | 1 | — | [[Berbamine (drug)]] 0.05 µM 0.0567× (z -9.1) |
| [[SHP-77 (line)]] | alt | 4.00 | 0 | 1 | — | [[Clonidine (hydrochloride) (drug)]] 0.5 µM 0.0558× (z -8.7) |
| [[SW480 (line)]] | alt | 6.43 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0520× (z -10.6) |
| [[A498 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPN1]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[AGBL5]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EOLA2]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[DHFR]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ANKRD30BL]] | +0.62 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[PTPN18]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LY6G5B]] | +0.61 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[TXNDC5]] | +0.60 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.60 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[BAG6]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[RPSA]] | +0.59 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[HFM1]] | +0.58 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIRT6]] | -0.60 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[NEMF]] | -0.56 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GGT7]] | -0.56 | -0.39 / -0.57 | both halves | 5e-05 |  |
| [[NT5C]] | -0.56 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MTLN]] ⚠ | -0.55 | -0.31 / -0.62 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CROCCP2-1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[IL10RB]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[PLIN3]] | -0.53 | -0.16 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[ADRM1]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[LRRC8E]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[SUMO4]] | -0.52 | -0.28 / -0.53 | both halves | 3e-04 |  |
| [[TMEM70]] | -0.52 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[LSM10]] | -0.52 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[TENT4B]] | -0.52 | -0.35 / -0.58 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.631). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-23.2, -24.5); signed map (-19.4, -33.5). **Vector** length 52.6, 6.58% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.2 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | -2.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.6 | -1.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.0 | +1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.0 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.3 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.0 |

## What is on record

> [!warning] No registry record
> CA5BP1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16501); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16501]; `tensor/DDL_lfc|DDL_z.npy` [16501]; `embed/gene_vectors.npy` [16501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16501 or target_col == 16501). Every well: [[CA5BP1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CA5BP1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
