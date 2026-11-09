---
symbol: "ZBTB33"
type: "gene"
col: 10828
ensembl_id: "ENSG00000177485"
name: "zinc finger and BTB domain containing 33"
location: "Xq24"
module: 7
arm: "+"
pooled_cpm: 24.0
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# ZBTB33

*zinc finger and BTB domain containing 33* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.19× (z +13.2, q 5e-37, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.615× (z -8.2, q 2e-13, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBQLN2]] (+0.81, fdr 7e-06), [[ZXDB]] (+0.74, fdr 7e-06), [[VEZF1]] (+0.73, fdr 7e-06); moves opposite to [[UQCRH]] (-0.67, fdr 1e-05), [[EFCAB14-AS1]] (-0.67, fdr 2e-05), [[DRD4]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.19×** | +13.2 | 5e-37 | 44/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +10.8 | 6e-25 | 39/48 (LS 180, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +9.3 | 2e-18 | 33/47 (A-427, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.4 | 2e-08 | 29/45 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +5.6 | 2e-06 | 25/48 (NCI-H2347, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.3 | 1e-05 | 28/48 (C32, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 4e-05 | 25/47 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 17/48 (H4, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.0 | 0.004 | 0/48 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.004 | 12/47 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.17× | +3.8 | 0.008 | 19/47 (LS 180, KATO III, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.009 | 9/47 (C-33 A, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | 1.20× | +3.0 | 0.10 | 13/45 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -8.2 | 2e-13 | 38/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -7.9 | 6e-13 | 34/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.639×** | -7.5 | 1e-11 | 34/47 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.696×** | -4.3 | 0.002 | 15/46 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **0.700×** | -4.3 | 0.002 | 17/48 (Hs 766T, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **0.719×** | -3.9 | 0.008 | 18/47 (SW1417, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.858× | -3.6 | 0.022 | 19/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.740×** | -3.6 | 0.022 | 12/48 (SW48, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.741×** | -3.6 | 0.022 | 16/48 (hTERT-HPNE, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.874× | -3.2 | 0.078 | 13/48 (SW 900, BT-474, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.767×** | -3.2 | 0.078 | 13/47 (SNU-423, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 17.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.14× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 46.5 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 2.27× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.410× (z -10.2) |
| [[A-427 (line)]] | wt | 22.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.22× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 21.2 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.04× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 24.6 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.57× (z +11.8) | — |
| [[A-172 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBQLN2]] | +0.81 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.74 | +0.60 / +0.76 | both halves | 7e-06 | same gene group |
| [[VEZF1]] | +0.73 | +0.61 / +0.80 | both halves | 7e-06 | same gene group |
| [[ZNF260]] | +0.72 | +0.59 / +0.76 | both halves | 7e-06 | same gene group |
| [[LIG4]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ZNF564]] | +0.70 | +0.59 / +0.66 | both halves | 7e-06 | same gene group |
| [[DTX3L]] | +0.69 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[ZNF770]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 | same gene group |
| [[ZNF816]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 | same gene group |
| [[TRMT5]] | +0.68 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[ZNF24]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 | same gene group |
| [[MIER3]] | +0.66 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UQCRH]] | -0.67 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[EFCAB14-AS1]] | -0.67 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[DRD4]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[TMEM41B]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[COX6C]] | -0.62 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[MPND]] | -0.60 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[KDELR1]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.60 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[DPM1]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SDHAP4-1]] | -0.59 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[SEZ6L2]] | -0.59 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[METRN]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-31.9, 13.0); signed map (3.3, -29.9). **Vector** length 98.5, 21.8% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.6 | +13.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +10.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.7 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +4.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | +2.3 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.2 | -8.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -7.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.8 | -7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.3 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.2 | -3.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.2 | -4.3 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | -2.7 | -3.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.7 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:120,250,752-120,258,398 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF-kaiso, kaiso, WUGSC:H_DJ525N14.1, KAISO, ZNF348 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Reactome | 9 pathways, smallest: Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86T24](https://www.uniprot.org/uniprotkb/Q86T24) (Transcriptional regulator Kaiso):

> Transcriptional regulator with bimodal DNA-binding specificity. Binds to methylated CpG dinucleotides in the consensus sequence 5'-CGCG-3' and also binds to the non-methylated consensus sequence 5'-CTGCNA-3' also known as the consensus kaiso binding site (KBS). Recruits the N-CoR repressor complex to promote histone deacetylation and the formation of repressive chromatin structures in target gene promoters. May contribute to the repression of target genes of the Wnt signaling pathway. May also …

**Summary**, from NCBI Gene [10009](https://www.ncbi.nlm.nih.gov/gene/10009):

> This gene encodes a transcriptional regulator with bimodal DNA-binding specificity, which binds to methylated CGCG and also to the non-methylated consensus KAISO-binding site TCCTGCNA. The protein contains an N-terminal POZ/BTB domain and 3 C-terminal zinc finger motifs. It recruits the N-CoR repressor complex to promote histone deacetylation and the formation of repressive chromatin structures in target gene promoters. It may contribute to the repression of target genes of the Wnt signaling …

**Accessions** — [HGNC:16682](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16682) · Entrez [10009](https://www.ncbi.nlm.nih.gov/gene/10009) · UniProt [Q86T24](https://www.uniprot.org/uniprotkb/Q86T24) · Ensembl [ENSG00000177485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177485)

## Data

Gene col 10828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10828); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10828]; `tensor/DDL_lfc|DDL_z.npy` [10828]; `embed/gene_vectors.npy` [10828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10828 or target_col == 10828). Every well: [[ZBTB33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
