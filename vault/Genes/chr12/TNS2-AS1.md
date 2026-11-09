---
symbol: "TNS2-AS1"
type: "gene"
col: 15035
ensembl_id: "ENSG00000257337"
name: "TNS2 antisense RNA 1"
location: "12q13.13"
module: 21
arm: "+"
pooled_cpm: 15.6
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TNS2-AS1

*TNS2 antisense RNA 1* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +17.4, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.771× (z -4.3, q 0.007, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H1573 0.428×; ⚠ cell-cycle shift, explains ~7% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF451-AS1]] (+0.69, fdr 1e-05), [[ABHD15-AS1]] (+0.69, fdr 1e-05), [[C12orf73]] (+0.67, fdr 2e-05); moves opposite to [[GPATCH11]] (-0.54, fdr 3e-04), [[KBTBD6]] (-0.53, fdr 6e-04), [[CEP295]] (-0.53, fdr 2e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +17.4 | 0e+00 | 41/46 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +15.8 | 0e+00 | 35/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +11.3 | 2e-27 | 23/29 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +9.8 | 2e-20 | 27/35 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +8.0 | 2e-13 | 28/43 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.99×** | +6.3 | 4e-08 | 21/48 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.9 | 7e-05 | 13/48 (KATO III, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 9e-04 | 17/46 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.3 | 9e-04 | 13/47 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.002 | 13/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.003 | 7/46 (Panc 03.27, A-172, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +4.0 | 0.003 | 15/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.26×** | +4.0 | 0.003 | 17/48 (KATO III, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.6 | 0.013 | 9/23 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.2 | 0.046 | 10/45 (J82, C-33 A, …) | top dose only | position effect removed |
| [[Estrone sulfate (potassium) (drug)]] 0.05 µM |  | 1.19× | +3.1 | 0.069 | 2/47 (A498, SW 900) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.084 | 8/44 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (NCI-H1573 0.428×; ⚠ cell-cycle shift, explains ~7% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.771×** | -4.3 | 0.007 | 13/46 (HCT15, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Larotrectinib (drug)]] 5 µM |  | 0.842× | -4.2 | 0.007 | 15/48 (LS 180, SW480, …) | top dose only | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.833× | -3.2 | 0.29 | 5/48 (NCI-H1573, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.2) | — |
| [[A-172 (line)]] | wt | 9.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.1) | — |
| [[A498 (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +15.6) | — |
| [[A549 (line)]] | wt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +10.1) | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +8.8) | — |
| [[C32 (line)]] | wt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 18.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.428× (z -9.0) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-427 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF451-AS1]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 | same gene group |
| [[ABHD15-AS1]] | +0.69 | +0.54 / +0.73 | both halves | 1e-05 | same gene group |
| [[C12orf73]] | +0.67 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[CHMP3-AS1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | same gene group |
| [[TICAM2-AS1]] | +0.65 | +0.58 / +0.66 | both halves | 8e-06 | same gene group |
| [[DSG2-AS1]] | +0.63 | +0.45 / +0.68 | both halves | 3e-05 | same gene group |
| [[SPATA21]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MAL2-AS1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 | same gene group |
| [[HRG-AS1]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 | same gene group |
| [[EOGT-DT]] | +0.61 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[EHBP1-AS1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[PLA2G6]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH11]] | -0.54 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[KBTBD6]] | -0.53 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[CEP295]] | -0.53 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[HPF1]] | -0.52 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[NSUN5]] | -0.51 | -0.21 / -0.57 | both halves | 6e-04 |  |
| [[ISCA2]] | -0.50 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[AGGF1]] | -0.50 | -0.16 / -0.60 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.660). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.1, 27.3); signed map (34.4, 3.9). **Vector** length 62.7, 9.34% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +17.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +9.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +4.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -0.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | TNS2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.13 — chr12:53,012,884-53,054,450 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-983P16.4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27464) · Entrez [283335](https://www.ncbi.nlm.nih.gov/gene/283335) · Ensembl [ENSG00000257337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257337)

## Data

Gene col 15035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15035); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15035]; `tensor/DDL_lfc|DDL_z.npy` [15035]; `embed/gene_vectors.npy` [15035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15035 or target_col == 15035). Every well: [[TNS2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNS2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
