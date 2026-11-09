---
symbol: "GPAT4-AS1"
type: "gene"
col: 14786
ensembl_id: "ENSG00000253133"
name: "GPAT4 and GINS4 antisense RNA 1"
location: "8p11.21"
module: 35
arm: "+"
pooled_cpm: 4.74
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 21
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# GPAT4-AS1

*GPAT4 and GINS4 antisense RNA 1* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.83× (z +10.9, q 6e-25, up in 27 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.473× (z -9.5, q 1e-18, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP34-DT]] (+0.73, fdr 7e-06), [[GTF2IRD2]] (+0.71, fdr 1e-05), [[GTF2IRD2B]] (+0.69, fdr 1e-05); moves opposite to [[PHF6]] (-0.59, fdr 3e-05), [[METAP1]] (-0.57, fdr 5e-05), [[EDA]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TP53]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.9 | 6e-25 | 27/39 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.0 | 6e-07 | 1/8 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +5.0 | 1e-04 | 14/38 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.011 | 9/27 (HEC-1-A, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.43× | +3.3 | 0.13 | 3/34 (Panc 03.27, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.30× | +3.1 | 0.16 | 5/13 (NCI-H460, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.473×** | -9.5 | 1e-18 | 29/46 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.572×** | -7.1 | 4e-10 | 25/45 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.603×** | -6.4 | 3e-08 | 18/46 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.613×** | -6.2 | 9e-08 | 19/39 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.436×** | -5.5 | 4e-06 | 15/43 (NCI-H1792, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.660×** | -5.2 | 1e-05 | 15/44 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -5.1 | 2e-05 | 17/46 (Hs 766T, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.678×** | -4.9 | 6e-05 | 15/46 (COLO 205, NCI-H1792, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.724×** | -4.1 | 0.003 | 13/43 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.730×** | -4.0 | 0.004 | 14/45 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.733×** | -3.9 | 0.005 | 10/45 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.731×** | -3.8 | 0.007 | 9/39 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.761×** | -3.4 | 0.023 | 10/41 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.594×** | -3.4 | 0.023 | 10/39 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.599×** | -3.4 | 0.027 | 2/35 (NCI-H460, MIA PaCa-2) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Larotrectinib (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.030 | 10/45 (H4, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -3.2 | 0.037 | 6/44 (A549, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -3.2 | 0.042 | 12/45 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 7.86 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.133× (z -9.1) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 4.30 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0840× (z -9.0) |
| [[HOP62 (line)]] | alt | 7.12 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0833× (z -13.0) |
| [[Hs 766T (line)]] | wt | 5.10 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.160× (z -9.2) |
| [[KATO III (line)]] | alt | 6.16 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0709× (z -11.7) |
| [[SW480 (line)]] | alt | 5.89 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.215× (z -8.9) |
| [[A-172 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP34-DT]] | +0.73 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GTF2IRD2]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[GTF2IRD2B]] | +0.69 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[NDUFAF1]] | +0.67 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PPP2R3C]] | +0.66 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[SPATA1]] | +0.66 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[CYP20A1]] | +0.65 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[NRL]] | +0.65 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[CNPY2-AS1]] | +0.65 | +0.43 / +0.59 | both halves | 3e-05 | same gene group |
| [[ERCC6L2-AS1]] | +0.64 | +0.61 / +0.34 | both halves | 1e-04 | same gene group |
| [[AP4S1]] | +0.64 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[NEK8]] | +0.64 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.59 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[METAP1]] | -0.57 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[EDA]] | -0.56 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[CDCA7L]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[RRP1B]] | -0.55 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[FYCO1]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | C | TP53 activity lowers GPAT4-AS1's level | lines that do not express TP53 (3) vs lines expressing it (47) | 1.59× higher at baseline in the lines without TP53 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF483, AGK, MCM2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (2.9, 15.2); signed map (23.5, -9.1). **Vector** length 56.8, 7.63% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.0 | +0.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -6.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.9 | -7.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.6 | -4.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | GPAT4 and GINS4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8p11.21 — chr8:41,509,593-41,578,421 (-) |
| Ensembl biotype | lncRNA |
| Also known as | GIAT4RA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55539](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55539) · Entrez [102723729](https://www.ncbi.nlm.nih.gov/gene/102723729) · Ensembl [ENSG00000253133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253133)

## Data

Gene col 14786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14786); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14786]; `tensor/DDL_lfc|DDL_z.npy` [14786]; `embed/gene_vectors.npy` [14786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14786 or target_col == 14786). Every well: [[GPAT4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPAT4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
