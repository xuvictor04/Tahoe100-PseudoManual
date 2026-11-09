---
symbol: "FAM185BP"
type: "gene"
col: 13204
ensembl_id: "ENSG00000214439"
name: "family with sequence similarity 185 member B, pseudogene"
location: "7q11.23"
module: 178
arm: "+"
pooled_cpm: 5.14
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/178"]
generated_by: "tahoemap"
---

# FAM185BP

*family with sequence similarity 185 member B, pseudogene* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.31× (z +9.9, q 3e-20, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.488× (z -8.5, q 7e-15, down in 25 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.643× (z -5.3, q 2e-05, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM174A]] (+0.68, fdr 1e-05), [[ING4]] (+0.64, fdr 7e-06), [[MARCHF8]] (+0.63, fdr 5e-05); moves opposite to [[AKIRIN1]] (-0.59, fdr 1e-05), [[TENM3]] (-0.51, fdr 1e-04), [[TNFRSF12A]] (-0.50, fdr 2e-05).
> It is in [[Module 178]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13204.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +9.9 | 3e-20 | 34/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +9.6 | 2e-19 | 32/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.5 | 5e-15 | 19/38 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +8.4 | 7e-15 | 25/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.64×** | +8.3 | 1e-14 | 18/46 (PANC-1, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.4 | 2e-08 | 3/10 (SNU-423, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.6 | 3e-04 | 12/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.004 | 10/37 (HEC-1-A, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.0 | 0.004 | 6/27 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.8 | 0.010 | 5/29 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.013 | 11/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.35×** | +3.5 | 0.019 | 8/42 (Panc 03.27, H4, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.32×** | +3.3 | 0.045 | 6/48 (SW1417, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +3.1 | 0.086 | 1/16 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.090 | 5/47 (SK-MEL-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.090 | 9/45 (HT-29, BT-474, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.090 | 5/44 (HT-29, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13204.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.488×** | -8.5 | 7e-15 | 25/47 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -5.9 | 9e-07 | 18/35 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.642×** | -5.3 | 2e-05 | 19/47 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.643×** | -5.3 | 2e-05 | 20/46 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.638×** | -5.2 | 3e-05 | 15/42 (A-172, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.513×** | -4.2 | 0.003 | 15/37 (SHP-77, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.556×** | -3.7 | 0.020 | 11/42 (MIA PaCa-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.725×** | -3.6 | 0.020 | 11/44 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -3.4 | 0.041 | 13/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.757×** | -3.3 | 0.050 | 13/44 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.080 | 10/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 3.72 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0543× (z -10.5) |
| [[LS 180 (line)]] | wt | 3.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0803× (z -8.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.271× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 7.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.22 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM174A]] | +0.68 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ING4]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MARCHF8]] | +0.63 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[PPOX]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SLC25A14]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ATG14]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CWC15]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[COQ8A]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ALDH6A1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ASB7]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[YPEL3]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HMBOX1]] | +0.57 | +0.39 / +0.44 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKIRIN1]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[TENM3]] | -0.51 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TNFRSF12A]] | -0.50 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TTPAL]] | -0.48 | -0.32 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 178]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.3, -20.5); signed map (-19.5, 6.6). **Vector** length 51.3, 6.24% of its response variance represented; |z| ≥ 3 in 995 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.5 | +8.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +0.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.1 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.0 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 185 member B, pseudogene |
| Locus type | pseudogene |
| Location | 7q11.23 — chr7:77,083,886-77,122,116 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously FAM185B |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21813](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21813) · Entrez [641808](https://www.ncbi.nlm.nih.gov/gene/641808) · Ensembl [ENSG00000214439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214439)

## Data

Gene col 13204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13204); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13204]; `tensor/DDL_lfc|DDL_z.npy` [13204]; `embed/gene_vectors.npy` [13204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13204 or target_col == 13204). Every well: [[FAM185BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM185BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
