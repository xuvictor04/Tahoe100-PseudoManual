---
symbol: "MAPK7"
type: "gene"
col: 9320
ensembl_id: "ENSG00000166484"
name: "mitogen-activated protein kinase 7"
location: "17p11.2"
module: 2
arm: "+"
pooled_cpm: 7.62
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAPK7

*mitogen-activated protein kinase 7* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +4.8, q 0.001, up in 22 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.583× (z -8.8, q 1e-15, down in 35 of 45 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.526× (z -7.1, q 2e-10, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIC8A]] (+0.68, fdr 7e-06), [[TINF2]] (+0.67, fdr 7e-06), [[B4GALT7]] (+0.65, fdr 7e-06); moves opposite to [[PRPF4B]] (-0.52, fdr 6e-05), [[SSB]] (-0.52, fdr 4e-05), [[SMIM30]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.8 | 0.001 | 22/43 (Hs 766T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.52×** | +4.6 | 0.001 | 20/44 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +4.4 | 0.002 | 16/46 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.89×** | +3.8 | 0.020 | 10/46 (NCI-H2030, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.21 | 6/43 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.32× | +3.0 | 0.24 | 6/46 (SK-MEL-2, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.583×** | -8.8 | 1e-15 | 35/45 (A-172, J82, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -7.4 | 5e-11 | 27/42 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -7.1 | 2e-10 | 28/46 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.687×** | -6.1 | 1e-07 | 27/47 (NCI-H1792, SK-MEL-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.601×** | -5.9 | 5e-07 | 20/32 (PANC-1, A-172, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -5.7 | 1e-06 | 17/35 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.627×** | -5.0 | 5e-05 | 14/21 (PANC-1, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.670×** | -4.6 | 3e-04 | 15/45 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -4.5 | 5e-04 | 18/41 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -4.3 | 9e-04 | 19/47 (C-33 A, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.714×** | -3.9 | 0.005 | 15/46 (H4, C32, …) | all doses, flat | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.736×** | -3.5 | 0.020 | 11/47 (RPMI-7951, SW1417, …) | inconsistent across doses | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.754×** | -3.3 | 0.050 | 9/41 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.761×** | -3.2 | 0.064 | 15/47 (HS-578T, H4, …) | all doses, flat | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.761×** | -3.0 | 0.093 | 18/37 (LS 180, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -19.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -12.4) |
| [[C32 (line)]] | wt | 9.82 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0851× (z -10.3) ⚠ toxic · without an alert: [[Naproxen (drug)]] 0.05 µM 0.0974× (z -9.4) |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -9.6) |
| [[J82 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 5.02 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0622× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[RPMI-7951 (line)]] | alt | 8.69 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[A-427 (line)]] | wt | 5.60 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0880× (z -9.6) |
| [[A549 (line)]] | wt | 9.47 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[H4 (line)]] | wt | 11.0 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0647× (z -9.7) |
| [[HCT15 (line)]] | alt | 9.32 | 0 | 1 | — | [[Clofarabine (drug)]] 0.05 µM 0.0537× (z -9.9) |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -10.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 6.31 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 5.21 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0799× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 6.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 7.51 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 3.82 | 0 | 1 | — | [[Monocrotaline (drug)]] 5 µM 0.0809× (z -9.0) |
| [[A498 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIC8A]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 | same gene group |
| [[TINF2]] | +0.67 | +0.67 / +0.62 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[B4GALT7]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TESK1]] | +0.64 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[DDX41]] | +0.62 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PFKL]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[IPO13]] | +0.60 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[CRAT]] | +0.59 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[SPATA2]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.59 | +0.74 / +0.48 | both halves | 2e-05 |  |
| [[PRSS53]] | +0.58 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[GMPPB]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF4B]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[SSB]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SMIM30]] | -0.49 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[PNISR]] | -0.49 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[LUC7L3]] | -0.48 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[PUM2]] | -0.47 | -0.26 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (10.8, -22.7); signed map (-25.3, 3.2). **Vector** length 72.6, 12.0% of its response variance represented; |z| ≥ 3 in 1,010 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.4 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.9 | -8.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.4 | -5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.6 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,377,721-19,383,544 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BMK1, ERK5; previously PRKM7 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Mitogen-activated protein kinase 7 (ERK5) family |
| Reactome | 39 pathways, smallest: ERKs are inactivated; Gastrin-CREB signalling pathway via PKC and MAPK; ERK/MAPK targets |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13164](https://www.uniprot.org/uniprotkb/Q13164) (Mitogen-activated protein kinase 7):

> Plays a role in various cellular processes such as proliferation, differentiation and cell survival. The upstream activator of MAPK7 is the MAPK kinase MAP2K5. Upon activation, it translocates to the nucleus and phosphorylates various downstream targets including MEF2C. EGF activates MAPK7 through a Ras-independent and MAP2K5-dependent pathway. As part of the MAPK/ERK signaling pathway, acts as a negative regulator of apoptosis in cardiomyocytes via interaction with STUB1/CHIP and promotion of …

**Summary**, from NCBI Gene [5598](https://www.ncbi.nlm.nih.gov/gene/5598):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as an integration point for multiple biochemical signals, and are involved in a wide variety of cellular processes such as proliferation, differentiation, transcription regulation and development. This kinase is specifically activated by mitogen-activated protein kinase kinase 5 (MAP2K5/MEK5). It is involved in the downstream signaling processes of various receptor molecules including receptor type kinases, …

**Accessions** — [HGNC:6880](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6880) · Entrez [5598](https://www.ncbi.nlm.nih.gov/gene/5598) · UniProt [Q13164](https://www.uniprot.org/uniprotkb/Q13164) · Ensembl [ENSG00000166484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166484)

## Data

Gene col 9320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9320); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9320]; `tensor/DDL_lfc|DDL_z.npy` [9320]; `embed/gene_vectors.npy` [9320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9320 or target_col == 9320). Every well: [[MAPK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
