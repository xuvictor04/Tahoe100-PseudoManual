---
symbol: "MYADM-AS1"
type: "gene"
col: 13636
ensembl_id: "ENSG00000228323"
name: "MYADM antisense RNA 1"
location: "19q13.42"
module: 47
arm: "+"
pooled_cpm: 2.18
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# MYADM-AS1

*MYADM antisense RNA 1* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +15.2, q 0e+00, up in 19 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.598× (z -4.9, q 6e-04, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOM1]] (+0.64, fdr 1e-05), [[ERRFI1-DT]] (+0.62, fdr 1e-05), [[CHADL]] (+0.61, fdr 1e-05); moves opposite to [[CIAO3]] (-0.51, fdr 3e-05), [[UBA3]] (-0.50, fdr 6e-05), [[ATP5F1C]] (-0.47, fdr 5e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +15.2 | 0e+00 | 19/25 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.11×** | +10.4 | 5e-23 | 1/2 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.1 | 1e-17 | 3/11 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +8.8 | 2e-16 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.9 | 9e-05 | 2/40 (SW480, PANC-1) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.017 | 5/16 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.3 | 0.090 | 1/6 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.091 | 1/18 (RPMI-7951) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.25× | +3.1 | 0.13 | 1/39 (A498) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -4.9 | 6e-04 | 14/43 (BT-474, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -4.6 | 0.002 | 13/39 (HOP62, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -4.2 | 0.006 | 10/31 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -4.0 | 0.006 | 9/43 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.006 | 9/29 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -3.8 | 0.011 | 12/36 (NCI-H23, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.671×** | -3.6 | 0.018 | 10/30 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.672×** | -3.6 | 0.018 | 7/24 (J82, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.682×** | -3.6 | 0.018 | 6/30 (C-33 A, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.686×** | -3.6 | 0.021 | 6/42 (LOX-IMVI, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -3.5 | 0.023 | 10/42 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.771×** | -3.5 | 0.024 | 10/37 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.705×** | -3.3 | 0.040 | 8/42 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Phenylephrine (hydrochloride) (drug)]] 0.05 µM |  | **0.718×** | -3.1 | 0.066 | 5/40 (HS-578T, HCT15, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.718×** | -3.1 | 0.066 | 11/42 (J82, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.00 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0238× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 4.63 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0665× (z -11.6) |
| [[MIA PaCa-2 (line)]] | alt | 2.09 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.334× (z -10.3) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.977 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.680 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.780 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.659 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOM1]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[ERRFI1-DT]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CHADL]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[GAL3ST2]] | +0.61 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DPY19L3-DT]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ASGR1]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[FSCN2]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[RELA-DT]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[AZU1]] | +0.57 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[C19orf38]] | +0.57 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RALY-AS1]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 | same gene group |
| [[SPATA32]] | +0.56 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO3]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[UBA3]] | -0.50 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ATP5F1C]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.1, -12.2); signed map (19.2, 14.8). **Vector** length 46.2, 6.10% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.7 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.6 | +0.7 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MYADM antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.42 — chr19:53,854,581-53,869,107 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40384) · Entrez [105372457](https://www.ncbi.nlm.nih.gov/gene/105372457) · Ensembl [ENSG00000228323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228323)

## Data

Gene col 13636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13636); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13636]; `tensor/DDL_lfc|DDL_z.npy` [13636]; `embed/gene_vectors.npy` [13636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13636 or target_col == 13636). Every well: [[MYADM-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYADM-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
