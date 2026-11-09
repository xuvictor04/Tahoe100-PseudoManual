---
symbol: "HLCS-AS1"
type: "gene"
col: 13419
ensembl_id: "ENSG00000224790"
name: "HLCS antisense RNA 1"
location: "21q22.13"
module: 15
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# HLCS-AS1

*HLCS antisense RNA 1* — 21q22.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.05× (z +6.9, q 3e-09, up in 15 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.371× (z -9.5, q 1e-18, down in 26 of 43 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.444× (z -7.8, q 2e-12, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF418]] (+0.59, fdr 2e-05), [[CTC-338M12.4]] (+0.57, fdr 3e-05), [[ZKSCAN2-DT]] (+0.56, fdr 5e-05); moves opposite to [[PRDX2]] (-0.53, fdr 3e-05), [[LRRC37A2]] (-0.50, fdr 2e-05), [[PKN2]] (-0.49, fdr 9e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +6.9 | 3e-09 | 15/37 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.8 | 3e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.7 | 2e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.43×** | +3.4 | 0.085 | 4/28 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.39× | +3.2 | 0.16 | 1/8 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.371×** | -9.5 | 1e-18 | 26/43 (RKO, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.557×** | -7.9 | 9e-13 | 20/29 (A498, HOP62, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.444×** | -7.8 | 2e-12 | 25/43 (HepG2/C3A, RKO, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.480×** | -7.0 | 3e-10 | 21/44 (J82, SW480, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.465×** | -6.9 | 6e-10 | 16/43 (SW480, HOP62, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.485×** | -6.6 | 3e-09 | 23/38 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.679×** | -3.7 | 0.018 | 8/40 (A498, H4, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.513×** | -3.3 | 0.055 | 6/38 (RKO, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.695×** | -3.3 | 0.055 | 3/44 (BT-474, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.707×** | -3.1 | 0.098 | 8/40 (SK-MEL-2, A-427, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.723×** | -3.1 | 0.098 | 6/38 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Tolcapone (drug)]] 0.05 µM |  | **0.724×** | -3.1 | 0.098 | 4/41 (KATO III, HS-578T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.727×** | -3.0 | 0.098 | 11/44 (A498, SW 900, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.798×** | -3.0 | 0.098 | 12/31 (HOP62, LoVo, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0721× (z -15.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 3.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -8.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 1.78 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0424× (z -8.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[PANC-1 (line)]] | alt | 1.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0599× (z -8.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.903 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.991 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF418]] | +0.59 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CTC-338M12.4]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ZKSCAN2-DT]] | +0.56 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[GTF3C2-AS2]] | +0.56 | +0.37 / +0.51 | both halves | 8e-05 | same gene group |
| [[LINC01409]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | +0.54 | +0.42 / +0.45 | both halves | 4e-05 | same gene group |
| [[TIGD1]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DPY19L3-DT]] | +0.53 | +0.42 / +0.42 | both halves | 4e-05 |  |
| [[RRN3P1]] | +0.52 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[TRNT1]] | +0.51 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[CCNY-AS1]] | +0.50 | +0.31 / +0.56 | both halves | 2e-04 | same gene group |
| [[SPRYD4]] | +0.50 | +0.35 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX2]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[LRRC37A2]] | -0.50 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PKN2]] | -0.49 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[SLC50A1]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PSME1]] | -0.49 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[TMEM205]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[MLLT3]] | -0.48 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CEPT1]] | -0.47 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TPR]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[NEDD9]] | -0.46 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[COX15]] | -0.46 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PHF21A]] | -0.46 | -0.48 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.432). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.1, 23.0); signed map (2.6, -0.9). **Vector** length 38.7, 3.92% of its response variance represented; |z| ≥ 3 in 1,022 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.0 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.0 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +0.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.8 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -6.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -1.0 | -3.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.0 | -7.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -3.1 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | HLCS antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 21q22.13 — chr21:36,966,461-36,975,164 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55850) · Entrez [122455337](https://www.ncbi.nlm.nih.gov/gene/122455337) · Ensembl [ENSG00000224790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224790)

## Data

Gene col 13419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13419); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13419]; `tensor/DDL_lfc|DDL_z.npy` [13419]; `embed/gene_vectors.npy` [13419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13419 or target_col == 13419). Every well: [[HLCS-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLCS-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
