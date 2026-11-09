---
symbol: "TMEM150A"
type: "gene"
col: 9717
ensembl_id: "ENSG00000168890"
name: "transmembrane protein 150A"
location: "2p11.2"
module: 6
arm: "-"
pooled_cpm: 2.5
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TMEM150A

*transmembrane protein 150A* — 2p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.86× (z +11.0, q 2e-25, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.77× (z +5.8, q 8e-07, up in 4 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.407× (z -6.5, q 3e-08, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DECR2]] (+0.60, fdr 1e-05), [[LENG9]] (+0.59, fdr 1e-05), [[MYL5]] (+0.58, fdr 1e-05); moves opposite to [[FANCI]] (-0.61, fdr 7e-06), [[RAD51AP1]] (-0.60, fdr 1e-05), [[ATAD5]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9717.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.86×** | +11.0 | 2e-25 | 4/4 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +9.6 | 3e-19 | 10/14 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.3 | 5e-11 | 3/6 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.48×** | +6.3 | 4e-08 | 8/13 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +5.8 | 8e-07 | 4/43 (SW1417, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +4.3 | 0.002 | 3/12 (A-427, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.2 | 0.002 | 9/20 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.78×** | +4.0 | 0.005 | 12/34 (PANC-1, A549, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **2.08×** | +3.5 | 0.025 | 4/31 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +3.3 | 0.048 | 10/38 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.072 | 5/44 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | 1.53× | +3.1 | 0.10 | 8/41 (NCI-H2030, SW480, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.52× | +3.0 | 0.11 | 7/43 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.52× | +3.0 | 0.11 | 6/28 (LoVo, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.407×** | -6.5 | 3e-08 | 27/46 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -6.5 | 3e-08 | 28/41 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.280×** | -4.8 | 2e-04 | 16/36 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -4.3 | 0.002 | 14/38 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -3.8 | 0.016 | 15/37 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.376×** | -3.7 | 0.016 | 11/27 (SW1417, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -3.7 | 0.016 | 12/25 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.661× | -3.0 | 0.17 | 11/40 (NCI-H1573, SHP-77, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.87 | 0 | 1 | — | [[Mifepristone (drug)]] 5 µM 0.0543× (z -9.9) |
| [[LoVo (line)]] | wt | 2.98 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0640× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 2.26 | 0 | 1 | — | [[Artemether (drug)]] 0.5 µM 0.0575× (z -9.4) |
| [[A-172 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DECR2]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[LENG9]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[MYL5]] | +0.58 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SURF2]] | +0.56 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[GRINA]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TMEM42]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[MLST8]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[MSRB2]] | +0.53 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.52 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MT1M]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[DPH1]] | +0.51 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCI]] | -0.61 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[RAD51AP1]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ATAD5]] | -0.60 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[CENPK]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RRM2]] | -0.56 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[CENPO]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[KNTC1]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SPC25]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DDIAS]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[POLQ]] | -0.54 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CDCA5]] | -0.54 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[RRM1]] | -0.54 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **-** arm (projection on the module's main direction -0.470). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.0, -46.9); signed map (39.3, -7.1). **Vector** length 47.3, 6.01% of its response variance represented; |z| ≥ 3 in 927 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +11.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -4.3 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 150A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p11.2 — chr2:85,598,547-85,603,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRAM5, TM6P1, FLJ90024, TTN1; previously TMEM150 |
| Gene groups (HGNC) | DRAM autophagy modulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TG1](https://www.uniprot.org/uniprotkb/Q86TG1) (Transmembrane protein 150A):

> Regulates localization of phosphatidylinositol 4-kinase (PI4K) to the plasma membrane, possibly by reducing the association of TTC7 (TTC7A or TTC7B) with the PI4K complex. Acts as a regulator of phosphatidylinositol 4-phosphate (PtdIns(4)P) synthesis. May also play a role in fasting-induced catabolism (By similarity).

**Summary**, from NCBI Gene [129303](https://www.ncbi.nlm.nih.gov/gene/129303):

> Involved in phosphatidylinositol phosphate biosynthetic process and protein localization to plasma membrane. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24677) · Entrez [129303](https://www.ncbi.nlm.nih.gov/gene/129303) · UniProt [Q86TG1](https://www.uniprot.org/uniprotkb/Q86TG1) · Ensembl [ENSG00000168890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168890)

## Data

Gene col 9717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9717); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9717]; `tensor/DDL_lfc|DDL_z.npy` [9717]; `embed/gene_vectors.npy` [9717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9717 or target_col == 9717). Every well: [[TMEM150A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM150A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
