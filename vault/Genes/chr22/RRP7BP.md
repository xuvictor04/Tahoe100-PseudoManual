---
symbol: "RRP7BP"
type: "gene"
col: 11332
ensembl_id: "ENSG00000182841"
name: "ribosomal RNA processing 7 homolog B, pseudogene"
location: "22q13.2"
module: 33
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RRP7BP

*ribosomal RNA processing 7 homolog B, pseudogene* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.19× (z +8.9, q 4e-16, up in 27 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.82× (z +6.8, q 2e-09, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Binimetinib (drug)]] 0.5 µM: 0.739× (z -4.1, q 0.025, down in 12 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP7BP-1]] (+0.71, fdr 7e-06, ⚠ same locus), [[POLR3H]] (+0.70, fdr 7e-06), [[TMEM201]] (+0.67, fdr 1e-05), [[SLC27A5]] (+0.66, fdr 1e-05); moves opposite to [[CGGBP1]] (-0.63, fdr 1e-05), [[RO60]] (-0.62, fdr 1e-05), [[SGO1-AS1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.19×** | +8.9 | 4e-16 | 27/46 (SW480, HS-578T, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.98×** | +7.7 | 3e-12 | 29/45 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +6.8 | 2e-09 | 22/46 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.79×** | +6.3 | 3e-08 | 14/24 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +5.4 | 8e-06 | 16/45 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +4.6 | 4e-04 | 11/35 (PANC-1, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.50×** | +4.6 | 4e-04 | 15/45 (NCI-H1792, HCT15, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.8 | 0.009 | 0/9 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.6 | 0.018 | 1/15 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.5 | 0.028 | 7/43 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.24×** | +3.5 | 0.028 | 2/48 (NCI-H460, A549) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.049 | 3/43 (NCI-H23, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.080 | 1/44 (HEC-1-A) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.39×** | +3.1 | 0.086 | 1/9 (A498) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 0.025 | 12/44 (A-427, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.708×** | -3.9 | 0.025 | 6/46 (RKO, LoVo, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | **0.717×** | -3.8 | 0.030 | 9/43 (J82, HT-29, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -3.6 | 0.045 | 10/35 (RKO, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.724×** | -3.5 | 0.049 | 11/40 (A498, KATO III, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **0.739×** | -3.4 | 0.057 | 15/41 (Panc 03.27, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 0.753× | -3.1 | 0.14 | 13/37 (HOP62, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.753× | -3.1 | 0.14 | 15/42 (LoVo, J82, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.0 | 0.14 | 19/40 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.766× | -3.0 | 0.14 | 9/19 (NCI-H2030, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 5.22 | 0 | 2 (2 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0592× (z -11.3) ⚠ cell-cycle shift, explains ~76% of this change |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0679× (z -8.5) |
| [[LoVo (line)]] | wt | 6.60 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.141× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 2.60 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[A-172 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP7BP-1]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[POLR3H]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.67 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A5]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ZNF787]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NOL10]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[C19orf48]] | +0.64 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ZNF496]] | +0.63 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MON1A]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NOP2]] | +0.63 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[GFOD2]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[CCDC138]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[TBRG4]] | +0.62 | +0.66 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | -0.63 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[RO60]] | -0.62 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SGO1-AS1]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.60 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ZHX1]] | -0.60 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.60 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CEP57]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[CYLD]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[ACBD5]] | -0.56 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[BAZ2B]] | -0.55 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[TRMT1L]] | -0.55 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[STXBP3]] | -0.55 | -0.57 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-4.2, -30.8); signed map (-12.8, -54.9). **Vector** length 55.7, 7.17% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.6 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.9 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +2.6 | +7.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +5.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +2.0 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +4.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.2 | +3.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal RNA processing 7 homolog B, pseudogene |
| Locus type | pseudogene |
| Location | 22q13.2 — chr22:42,574,733-42,582,001 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | dJ222E13.2; previously RRP7B |
| Matched by | ensembl_id |

UniProt [Q9NSQ0](https://www.uniprot.org/uniprotkb/Q9NSQ0) carries no function annotation.

**Summary**, from NCBI Gene [91695](https://www.ncbi.nlm.nih.gov/gene/91695):

> Predicted to be involved in rRNA processing and ribosomal small subunit assembly. Predicted to be part of CURI complex and UTP-C complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30454) · Entrez [91695](https://www.ncbi.nlm.nih.gov/gene/91695) · UniProt [Q9NSQ0](https://www.uniprot.org/uniprotkb/Q9NSQ0) · Ensembl [ENSG00000182841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182841)

## Data

Gene col 11332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11332); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11332]; `tensor/DDL_lfc|DDL_z.npy` [11332]; `embed/gene_vectors.npy` [11332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11332 or target_col == 11332). Every well: [[RRP7BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRP7BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
