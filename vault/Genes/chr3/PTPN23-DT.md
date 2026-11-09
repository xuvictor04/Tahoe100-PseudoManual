---
symbol: "PTPN23-DT"
type: "gene"
col: 15270
ensembl_id: "ENSG00000260236"
name: "PTPN23 divergent transcript"
location: "3p21.31"
module: 35
arm: "+"
pooled_cpm: 3.29
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# PTPN23-DT

*PTPN23 divergent transcript* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +8.7, q 2e-15, up in 19 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.458× (z -8.5, q 1e-14, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C17orf100]] (+0.69, fdr 1e-05), [[CCT6B]] (+0.68, fdr 3e-05), [[UBE2D3-AS1]] (+0.67, fdr 2e-05); moves opposite to [[TMEM245]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15270.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.7 | 2e-15 | 19/35 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.4 | 5e-11 | 5/8 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +6.1 | 2e-07 | 18/44 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +6.1 | 2e-07 | 14/44 (HEC-1-A, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.4 | 0.001 | 3/23 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.44×** | +3.9 | 0.008 | 10/42 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.014 | 12/43 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.027 | 6/44 (HEC-1-A, J82, …) | top dose only |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM |  | 1.32× | +3.0 | 0.15 | 4/41 (COLO 205, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15270.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.458×** | -8.5 | 1e-14 | 30/45 (RPMI-7951, BT-474, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.486×** | -7.8 | 1e-12 | 25/45 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.539×** | -6.7 | 4e-09 | 18/32 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.592×** | -5.7 | 2e-06 | 17/44 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -4.9 | 1e-04 | 14/44 (HOP62, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.676×** | -4.3 | 0.002 | 12/45 (HT-29, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.681×** | -4.0 | 0.005 | 15/42 (NCI-H1573, NCI-H1792, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.692×** | -3.8 | 0.009 | 17/43 (SW48, A498, …) | rises with dose | composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.706×** | -3.8 | 0.010 | 11/46 (COLO 205, NCI-H2030, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.744×** | -3.2 | 0.074 | 8/43 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **0.732×** | -3.2 | 0.074 | 11/41 (SNU-423, HCT15, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.755× | -3.0 | 0.11 | 9/38 (SW 900, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15270. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.56 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0851× (z -10.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0794× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 3.73 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0887× (z -9.3) |
| [[SW1417 (line)]] | alt | 5.43 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0647× (z -10.5) |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.54 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15270), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C17orf100]] | +0.69 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CCT6B]] | +0.68 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[UBE2D3-AS1]] | +0.67 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ATXN7L3-AS1]] | +0.67 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[GSK3B-DT]] | +0.66 | +0.46 / +0.58 | both halves | 3e-05 | same gene group |
| [[DUSP28]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SUMO2P17]] | +0.65 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ZFHX2-AS1]] | +0.65 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[LRP2BP]] | +0.64 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[GTF2IP14]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[SMC5-DT]] | +0.64 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[LRRC41]] | +0.63 | +0.34 / +0.60 | both halves | 1e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM245]] | -0.54 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.665). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.8, 11.5); signed map (22.5, -3.3). **Vector** length 54.6, 6.99% of its response variance represented; |z| ≥ 3 in 1,003 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +8.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +4.2 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +2.6 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | PTPN23 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p21.31 — chr3:47,379,089-47,381,519 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55397) · Entrez [119863865](https://www.ncbi.nlm.nih.gov/gene/119863865) · Ensembl [ENSG00000260236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260236)

## Data

Gene col 15270: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15270); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15270, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15270]; `tensor/DDL_lfc|DDL_z.npy` [15270]; `embed/gene_vectors.npy` [15270]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15270 or target_col == 15270). Every well: [[PTPN23-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN23-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
