---
symbol: "MKRN5P"
type: "gene"
col: 13398
ensembl_id: "ENSG00000224430"
name: "makorin ring finger protein 5, pseudogene"
location: "Xq13.2"
module: 126
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# MKRN5P

*makorin ring finger protein 5, pseudogene* — Xq13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.10× (z +4.7, q 0.001, up in 0 of 2 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.399× (z -8.6, q 6e-15, down in 26 of 29 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 0.600× (z -3.2, q 0.053, down in 11 of 33 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.0866×, SW480 0.146×, A498 0.105×, NCI-H460 0.181×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0423×, SW480 0.0902×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0694×; ⚠ cell-cycle shift, explains ~29% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0777×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNIP2]] (+0.65, fdr 1e-05), [[EPM2A]] (+0.63, fdr 4e-05), [[IL18BP]] (+0.62, fdr 2e-05); moves opposite to [[DPF1]] (-0.62, fdr 2e-05), [[INIP]] (-0.58, fdr 7e-05), [[LAGE3]] (-0.57, fdr 2e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13398.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +4.7 | 0.001 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13398.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (NCI-H1573 0.0866×, SW480 0.146×, A498 0.105×, NCI-H460 0.181×, …; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.0423×, SW480 0.0902×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0694×; ⚠ cell-cycle shift, explains ~29% of this change); [[Decitabine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0777×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.399×** | -8.6 | 6e-15 | 26/29 (NCI-H1573, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.288×** | -8.2 | 4e-14 | 36/44 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.275×** | -8.2 | 4e-14 | 28/37 (A498, AsPC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.294×** | -8.1 | 9e-14 | 33/44 (A-172, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.380×** | -6.4 | 2e-08 | 24/43 (BT-474, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.476×** | -4.7 | 2e-04 | 9/9 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.517×** | -4.4 | 0.001 | 16/44 (SNU-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.295×** | -4.2 | 0.002 | 14/33 (PANC-1, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.547×** | -4.0 | 0.004 | 11/44 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.558×** | -3.9 | 0.007 | 16/27 (NCI-H460, SW1417, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.570×** | -3.7 | 0.011 | 15/42 (C32, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.600×** | -3.4 | 0.035 | 12/45 (PANC-1, AsPC-1, …) | inconsistent across doses | composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **0.600×** | -3.2 | 0.053 | 11/33 (NCI-H23, A498, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.611×** | -3.1 | 0.072 | 9/44 (KATO III, NCI-H23, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.626×** | -3.1 | 0.075 | 9/44 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13398. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.41 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0694× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Decitabine (drug)]] 0.05 µM 0.0777× (z -8.7) |
| [[PANC-1 (line)]] | alt | 3.94 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0423× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 2.93 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -9.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 2.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -9.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H1573 (line)]] | alt | 3.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -10.8) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.832 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.758 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.708 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.978 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.951 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.997 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13398), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNIP2]] | +0.65 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[EPM2A]] | +0.63 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[IL18BP]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[TMPRSS5]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LINC01355]] | +0.59 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[GLIPR1-AS1]] | +0.59 | +0.32 / +0.46 | both halves | 2e-04 |  |
| [[SAP30L-AS1]] | +0.58 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[WASH9P]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[HCFC1]] | +0.57 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[CYP2D7]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FAM27C]] | +0.56 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[CERS2]] | +0.56 | +0.29 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPF1]] | -0.62 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[INIP]] | -0.58 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[LAGE3]] | -0.57 | -0.31 / -0.53 | both halves | 2e-04 |  |
| [[CDKN2D]] | -0.56 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[ACTR1B]] | -0.56 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[EPN2]] | -0.56 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[RNF24]] | -0.55 | -0.37 / -0.48 | both halves | 8e-05 | same gene group |
| [[SLC25A4]] | -0.55 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[TXNDC17]] | -0.55 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[FSCN1]] | -0.54 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[PAXX]] ⚠ | -0.54 | -0.19 / -0.47 | ⚠ not reproduced | 8e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ST3GAL5]] | -0.54 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[SLC25A11]] | -0.54 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.6, -15.9); signed map (-9.4, -36.7). **Vector** length 46.6, 5.42% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.0 | -8.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.9 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.7 | -8.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | +0.9 |

## What is on record

|  |  |
|---|---|
| Name | makorin ring finger protein 5, pseudogene |
| Locus type | pseudogene |
| Location | Xq13.2 — chrX:74,161,062-74,162,528 (-) |
| Ensembl biotype | processed_pseudogene |
| Also known as | ZNF-Xq; previously ZNF127L2, MKRNP1 |
| Gene groups (HGNC) | Ring finger proteins |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:7117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7117) · Entrez [7683](https://www.ncbi.nlm.nih.gov/gene/7683) · Ensembl [ENSG00000224430](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224430)

## Data

Gene col 13398: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13398); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13398, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13398]; `tensor/DDL_lfc|DDL_z.npy` [13398]; `embed/gene_vectors.npy` [13398]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13398 or target_col == 13398). Every well: [[MKRN5P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKRN5P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
