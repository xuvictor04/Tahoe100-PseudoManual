---
symbol: "TMEM44-AS1"
type: "gene"
col: 13812
ensembl_id: "ENSG00000231770"
name: "TMEM44 antisense RNA 1"
location: "3q29"
module: 10
arm: "+"
pooled_cpm: 3.13
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 4
n_dd_up_clean: 28
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# TMEM44-AS1

*TMEM44 antisense RNA 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 5.63× (z +16.4, q 0e+00, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.85× (z +15.2, q 0e+00, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.613× (z -5.1, q 2e-04, down in 15 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC3-AS1]] (+0.75, fdr 7e-06), [[ACAD9-DT]] (+0.73, fdr 1e-05), [[PGBD4]] (+0.69, fdr 7e-06); moves opposite to [[DCUN1D2]] (-0.61, fdr 9e-05), [[CENPJ]] (-0.58, fdr 2e-05), [[TREX2]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.63×** | +16.4 | 0e+00 | 5/6 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.85×** | +15.2 | 0e+00 | 30/35 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.25×** | +11.8 | 1e-29 | 23/33 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.17×** | +11.2 | 5e-27 | 22/46 (PANC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.72×** | +10.3 | 1e-22 | 10/16 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +9.7 | 3e-20 | 26/34 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +7.7 | 1e-12 | 3/4 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.10×** | +7.6 | 2e-12 | 29/47 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +6.5 | 7e-09 | 23/43 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +5.8 | 3e-07 | 18/44 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.0 | 2e-05 | 15/40 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.55×** | +4.5 | 3e-04 | 5/38 (KATO III, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.5 | 4e-04 | 14/44 (HS-578T, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.2 | 0.001 | 17/46 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.8 | 0.005 | 6/17 (J82, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Belzutifan (drug)]] 5 µM |  | **2.02×** | +3.8 | 0.006 | 1/22 (HEC-1-A) | top dose only | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.64×** | +3.6 | 0.009 | 2/34 (A-427, RPMI-7951) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.009 | 5/43 (SNU-423, KATO III, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.42×** | +3.6 | 0.011 | 12/35 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13812.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -5.1 | 2e-04 | 15/46 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -4.4 | 0.002 | 13/32 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.655×** | -4.4 | 0.002 | 12/40 (RPMI-7951, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -3.5 | 0.062 | 11/41 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.718× | -3.3 | 0.11 | 8/41 (HS-578T, SNU-423, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.733× | -3.2 | 0.12 | 11/42 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | 0.566× | -3.1 | 0.17 | 2/34 (KATO III, A-427) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 4.64 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0499× (z -11.8) |
| [[A-172 (line)]] | wt | 2.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +11.4) | — |
| [[A498 (line)]] | wt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 2.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.87× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 2.42 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 12.8× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 1.64 | 1 | 0 | [[Anastrozole (drug)]] 0.5 µM 1.70× (z +15.1) | — |
| [[SW1417 (line)]] | alt | 4.34 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0942× (z -8.7) |
| [[A-427 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC3-AS1]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | same gene group |
| [[ACAD9-DT]] | +0.73 | +0.85 / +0.53 | both halves | 1e-05 |  |
| [[PGBD4]] | +0.69 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[ZNF407-AS1]] | +0.68 | +0.77 / +0.56 | both halves | 1e-05 | same gene group |
| [[FNBP1P1]] | +0.67 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[GUCY2C-AS1]] | +0.67 | +0.75 / +0.57 | both halves | 1e-05 | same gene group |
| [[TIGD6]] | +0.67 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.66 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[MYO16]] | +0.65 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[DNAH3]] | +0.64 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[MOCS3]] | +0.63 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[PDCL3P4]] | +0.62 | +0.76 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCUN1D2]] | -0.61 | -0.71 / -0.36 | both halves | 9e-05 |  |
| [[CENPJ]] | -0.58 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[TREX2]] | -0.57 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[MTFR1]] | -0.53 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[DDX12P]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[TBCD]] | -0.53 | -0.61 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.618). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (4.7, 14.3); signed map (29.1, -13.6). **Vector** length 46.9, 5.84% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +15.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +16.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -5.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -3.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -0.9 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | TMEM44 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q29 — chr3:194,583,991-194,590,260 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44272) · Entrez [100507297](https://www.ncbi.nlm.nih.gov/gene/100507297) · Ensembl [ENSG00000231770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231770)

## Data

Gene col 13812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13812); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13812]; `tensor/DDL_lfc|DDL_z.npy` [13812]; `embed/gene_vectors.npy` [13812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13812 or target_col == 13812). Every well: [[TMEM44-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM44-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
