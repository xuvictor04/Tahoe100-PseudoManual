---
symbol: "GORASP1"
type: "gene"
col: 3582
ensembl_id: "ENSG00000114745"
name: "golgi reassembly stacking protein 1"
location: "3p22.2"
module: 11
arm: "+"
pooled_cpm: 11.47
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# GORASP1

*golgi reassembly stacking protein 1* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.64× (z +10.6, q 1e-23, up in 27 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.122×); [[Silodosin (drug)]] 5 µM in 1 line (SW48 0.0982×); [[Digitoxin (drug)]] 5 µM in 1 line (SW 900 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP8]] (+0.66, fdr 1e-05), [[WASHC1]] (+0.66, fdr 7e-06), [[GFER]] (+0.65, fdr 7e-06); moves opposite to [[LDHB]] (-0.57, fdr 2e-05), [[OPA1]] (-0.56, fdr 1e-05), [[EIF1AX]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.6 | 1e-23 | 27/43 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.86×** | +9.1 | 2e-17 | 34/45 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.7 | 5e-16 | 34/46 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.0 | 3e-10 | 26/42 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.48×** | +6.0 | 2e-07 | 20/46 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.7 | 1e-06 | 20/40 (J82, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.5 | 4e-06 | 17/36 (KATO III, J82, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +4.3 | 0.001 | 13/42 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +4.0 | 0.004 | 12/41 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.013 | 10/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.26×** | +3.5 | 0.021 | 12/46 (A-427, A-172, …) | top dose only |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.031 | 9/45 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.070 | 8/48 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.070 | 6/44 (Hs 766T, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.24×** | +3.1 | 0.071 | 10/26 (LS 180, PANC-1, …) | two highest doses | composition shift |
| [[Trimetrexate (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.071 | 7/47 (HepG2/C3A, NCI-H1573, …) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.083 | 6/44 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3582.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (NCI-H23 0.122×); [[Silodosin (drug)]] 5 µM in 1 line (SW48 0.0982×); [[Digitoxin (drug)]] 5 µM in 1 line (SW 900 0.106×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -6.5 | 5e-08 | 10/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.807× | -3.1 | 0.50 | 15/47 (H4, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.122× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[SW 900 (line)]] | alt | 7.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[SW48 (line)]] | wt | 14.5 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0982× (z -9.7) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP8]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GFER]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ZCCHC3]] | +0.63 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[TADA2B]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[WHAMM]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[MED18]] | +0.61 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CPT1B]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[SIX5]] | +0.60 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RXRB]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TRIM47]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[DPF2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDHB]] | -0.57 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[OPA1]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[EIF1AX]] | -0.56 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[HSPD1]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[GLO1]] | -0.55 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[HSP90AB1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PARP1]] | -0.53 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[YWHAQ]] | -0.53 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPA1]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CYB5R4]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[NME2]] | -0.52 | -0.63 / -0.31 | both halves | 2e-04 |  |
| [[PAICS]] | -0.52 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.8, -1.8); signed map (1.2, -11.8). **Vector** length 62.6, 9.90% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +10.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.9 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.5 | +1.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.3 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | golgi reassembly stacking protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:39,095,222-39,108,369 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GRASP65, P65, FLJ23443; previously GOLPH5 |
| Gene groups (HGNC) | PDZ domain containing |
| Reactome | 12 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; COPII-mediated vesicle transport; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQQ3](https://www.uniprot.org/uniprotkb/Q9BQQ3) (Golgi reassembly-stacking protein 1):

> Key structural protein of the Golgi apparatus. The membrane cisternae of the Golgi apparatus adhere to each other to form stacks, which are aligned side by side to form the Golgi ribbon. Acting in concert with GORASP2/GRASP55, is required for the formation and maintenance of the Golgi ribbon, and may be dispensable for the formation of stacks. However, other studies suggest that GORASP1 plays an important role in assembly and membrane stacking of the cisternae, and in the reassembly of Golgi …

**Summary**, from NCBI Gene [64689](https://www.ncbi.nlm.nih.gov/gene/64689):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is a membrane protein involved in establishing the stacked structure of the Golgi apparatus. It is a caspase-3 substrate, and cleavage of this encoded protein contributes to Golgi fragmentation in apoptosis. This encoded protein can form a complex with the Golgi matrix protein GOLGA2, and this complex binds to the vesicle docking protein p115. …

**Accessions** — [HGNC:16769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16769) · Entrez [64689](https://www.ncbi.nlm.nih.gov/gene/64689) · UniProt [Q9BQQ3](https://www.uniprot.org/uniprotkb/Q9BQQ3) · Ensembl [ENSG00000114745](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114745)

## Data

Gene col 3582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3582); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3582]; `tensor/DDL_lfc|DDL_z.npy` [3582]; `embed/gene_vectors.npy` [3582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3582 or target_col == 3582). Every well: [[GORASP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GORASP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
