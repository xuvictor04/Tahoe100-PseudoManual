---
symbol: "CNNM3"
type: "gene"
col: 9692
ensembl_id: "ENSG00000168763"
name: "cyclin and CBS domain divalent metal cation transport mediator 3"
location: "2q11.2"
module: 225
arm: "+"
pooled_cpm: 9.29
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# CNNM3

*cyclin and CBS domain divalent metal cation transport mediator 3* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +6.7, q 9e-09, up in 17 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.584× (z -8.9, q 4e-16, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRK2]] (+0.61, fdr 1e-05), [[TENT4A]] (+0.54, fdr 5e-05), [[C2CD2L]] (+0.54, fdr 5e-05); moves opposite to [[RPL26L1]] (-0.55, fdr 1e-05), [[ZRANB2]] (-0.50, fdr 3e-05), [[LINC00702]] (-0.49, fdr 6e-05).
> It is in [[Module 225]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.7 | 9e-09 | 17/44 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.6 | 1e-08 | 11/18 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +5.5 | 8e-06 | 15/40 (HS-578T, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +5.2 | 2e-05 | 12/47 (A-172, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.38×** | +5.1 | 4e-05 | 8/25 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.4 | 9e-04 | 12/35 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.021 | 5/46 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.052 | 11/44 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.058 | 9/47 (A-172, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.058 | 5/44 (LS 180, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.058 | 7/44 (Panc 03.27, SHP-77, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +3.2 | 0.069 | 5/41 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[DTP3 (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.069 | 3/38 (PANC-1, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.1 | 0.069 | 3/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.584×** | -8.9 | 4e-16 | 28/46 (NCI-H23, C32, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.679×** | -6.7 | 8e-09 | 22/47 (HT-29, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.770×** | -6.3 | 4e-08 | 24/45 (A-172, NCI-H23, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.711×** | -5.9 | 5e-07 | 21/46 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.697×** | -5.9 | 5e-07 | 17/43 (SW480, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.6 | 2e-06 | 17/43 (SK-MEL-2, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.742×** | -5.1 | 2e-05 | 16/46 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.733×** | -5.1 | 2e-05 | 17/45 (SNU-423, RKO, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -4.9 | 7e-05 | 16/47 (C32, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.613×** | -4.4 | 6e-04 | 11/42 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.618×** | -4.3 | 8e-04 | 10/46 (NCI-H460, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.771×** | -4.0 | 0.004 | 10/46 (C32, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Altretamine (drug)]] 0.05 µM |  | **0.792×** | -3.7 | 0.009 | 8/46 (Panc 03.27, HCT15, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.863× | -3.6 | 0.013 | 8/47 (RPMI-7951, SW 1271, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.711×** | -3.1 | 0.082 | 8/32 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.14 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -8.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.287× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0688× (z -8.6) |
| [[SNU-423 (line)]] | alt | 6.91 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.114× (z -8.7) |
| [[A-427 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRK2]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TENT4A]] | +0.54 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[C2CD2L]] | +0.54 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[ZBTB44]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[TAF4]] | +0.53 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[GIT1]] | +0.52 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ATG9A]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[RNF44]] | +0.52 | +0.49 / +0.43 | both halves | 4e-05 |  |
| [[PDXP]] | +0.51 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[YPEL1]] | +0.50 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[CRAMP1]] | +0.50 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.50 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL26L1]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[ZRANB2]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LINC00702]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[PFDN1]] | -0.48 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[SMIM30]] | -0.47 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[TTN-AS1]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[PPID]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GTF2H3]] | -0.46 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[DNTTIP2]] | -0.46 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[FCF1]] | -0.46 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[RPF1]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[NSRP1]] | -0.45 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (3.8, -36.4); signed map (-23.1, 10.0). **Vector** length 60.5, 8.61% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.2 | +5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +0.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +5.2 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.7 | -6.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.7 | -8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.6 | -5.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -2.5 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | cyclin and CBS domain divalent metal cation transport mediator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q11.2 — chr2:96,816,245-96,835,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SLC70A3; previously ACDP3 |
| Gene groups (HGNC) | Solute carrier family 70, cyclin and CBS domain divalent metal cation transport mediators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE01](https://www.uniprot.org/uniprotkb/Q8NE01) (Metal transporter CNNM3):

> Probable metal transporter.

**Summary**, from NCBI Gene [26505](https://www.ncbi.nlm.nih.gov/gene/26505):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in magnesium ion homeostasis. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:104) · Entrez [26505](https://www.ncbi.nlm.nih.gov/gene/26505) · UniProt [Q8NE01](https://www.uniprot.org/uniprotkb/Q8NE01) · Ensembl [ENSG00000168763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168763)

## Data

Gene col 9692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9692); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9692]; `tensor/DDL_lfc|DDL_z.npy` [9692]; `embed/gene_vectors.npy` [9692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9692 or target_col == 9692). Every well: [[CNNM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNNM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
