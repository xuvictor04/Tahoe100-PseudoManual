---
symbol: "SNN"
type: "gene"
col: 11556
ensembl_id: "ENSG00000184602"
name: "stannin"
location: "16p13.13"
module: 148
arm: "-"
pooled_cpm: 3.22
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/148"]
generated_by: "tahoemap"
---

# SNN

*stannin* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.21× (z +15.0, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.710× (z -5.1, q 2e-04, down in 20 of 34 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELL3]] (+0.69, fdr 1e-05), [[CABLES2]] (+0.68, fdr 1e-05), [[PEDS1]] (+0.66, fdr 1e-05); moves opposite to [[COX18]] (-0.68, fdr 8e-05), [[MCTS1]] (-0.66, fdr 2e-05), [[MAGOHB]] (-0.64, fdr 4e-05).
> It sits in the **-** arm of [[Module 148]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.21×** | +15.0 | 0e+00 | 45/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.92×** | +14.2 | 2e-43 | 43/44 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.97×** | +11.4 | 1e-27 | 38/46 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +7.0 | 5e-10 | 22/44 (KATO III, HT-29, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +6.3 | 2e-08 | 1/6 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.8 | 5e-07 | 5/19 (BT-474, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +5.1 | 2e-05 | 14/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.9 | 5e-05 | 6/18 (LoVo, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.9 | 5e-05 | 6/24 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.93×** | +4.9 | 6e-05 | 3/18 (HEC-1-A, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.38×** | +4.7 | 1e-04 | 8/39 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.2 | 0.001 | 11/40 (SHP-77, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +4.1 | 0.001 | 4/9 (J82, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.001 | 6/45 (RKO, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +3.9 | 0.003 | 12/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.014 | 9/39 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.024 | 10/44 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.024 | 3/40 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.031 | 6/40 (HS-578T, NCI-H1573, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.058 | 4/44 (A-172, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -5.1 | 2e-04 | 20/34 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.646×** | -4.6 | 0.001 | 11/32 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -3.5 | 0.099 | 11/45 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.562× | -3.2 | 0.23 | 11/32 (LoVo, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.21 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM 0.0506× (z -9.2) |
| [[A498 (line)]] | wt | 3.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -9.7) |
| [[LoVo (line)]] | wt | 3.74 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.1) |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0722× (z -8.9) |
| [[A-172 (line)]] | wt | 9.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELL3]] | +0.69 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PEDS1]] | +0.66 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.65 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[MAST3]] | +0.64 | +0.52 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_DN |
| [[GIT1]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[CYTH3]] | +0.62 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[SERAC1]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[DOK4]] | +0.62 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[VAT1]] | +0.62 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[GALNT11]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[STRN]] | +0.61 | +0.57 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX18]] | -0.68 | -0.67 / -0.37 | both halves | 8e-05 |  |
| [[MCTS1]] | -0.66 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MAGOHB]] | -0.64 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[KRR1]] | -0.63 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CLHC1]] | -0.63 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PCBP1-AS1]] | -0.63 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[TASOR]] | -0.63 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[ICE2]] | -0.62 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.62 | -0.52 / -0.43 | both halves | 4e-05 |  |
| [[INTS2]] | -0.61 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[DNAAF10]] | -0.60 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 148]]; 30 genes; this gene is in the **-** arm (projection on the module's main direction -0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.9, -1.2); signed map (-39.0, -3.2). **Vector** length 57.3, 8.05% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +14.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.3 | +15.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +7.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +11.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -3.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.4 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | stannin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,668,455-11,679,152 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | KRAS_SIGNALING_DN, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [O75324](https://www.uniprot.org/uniprotkb/O75324) (Stannin):

> Plays a role in the toxic effects of organotins. Plays a role in endosomal maturation.

**Summary**, from NCBI Gene [8303](https://www.ncbi.nlm.nih.gov/gene/8303):

> Enables metal ion binding activity. Predicted to be involved in response to toxic substance. Located in cytoplasm and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11149) · Entrez [8303](https://www.ncbi.nlm.nih.gov/gene/8303) · UniProt [O75324](https://www.uniprot.org/uniprotkb/O75324) · Ensembl [ENSG00000184602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184602)

## Data

Gene col 11556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11556); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11556]; `tensor/DDL_lfc|DDL_z.npy` [11556]; `embed/gene_vectors.npy` [11556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11556 or target_col == 11556). Every well: [[SNN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
