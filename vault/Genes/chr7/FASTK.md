---
symbol: "FASTK"
type: "gene"
col: 9022
ensembl_id: "ENSG00000164896"
name: "Fas activated serine/threonine kinase"
location: "7q36.1"
module: 96
arm: "+"
pooled_cpm: 8.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# FASTK

*Fas activated serine/threonine kinase* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +10.0, q 1e-20, up in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +4.9, q 9e-05, up in 19 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.530× (z -7.4, q 8e-11, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX17]] (+0.64, fdr 1e-05), [[RABGGTA]] (+0.62, fdr 1e-05), [[GMPPB]] (+0.60, fdr 1e-05); moves opposite to [[RPLP1]] (-0.52, fdr 1e-04), [[CBX3]] (-0.50, fdr 6e-05), [[RPL35]] (-0.49, fdr 3e-04, ⚠ RPL35 in the vector space only through flagged drug-doses), [[RPL26]] (-0.49, fdr 2e-04).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9022.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +10.0 | 1e-20 | 24/32 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.1 | 2e-13 | 11/16 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.6 | 7e-09 | 14/21 (KATO III, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +5.7 | 2e-06 | 20/39 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.9 | 9e-05 | 19/43 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +4.1 | 0.003 | 7/22 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.030 | 5/45 (A498, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.3 | 0.070 | 13/39 (SW1417, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.45× | +3.0 | 0.16 | 10/39 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9022.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -7.4 | 8e-11 | 33/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.534×** | -7.3 | 8e-11 | 32/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -6.3 | 5e-08 | 27/45 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -6.1 | 1e-07 | 24/44 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.382×** | -5.8 | 6e-07 | 23/41 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -5.4 | 5e-06 | 22/46 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.759×** | -4.6 | 4e-04 | 16/45 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -4.5 | 5e-04 | 17/47 (SW48, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.697×** | -4.2 | 0.002 | 16/46 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -3.2 | 0.069 | 14/45 (H4, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.2 | 0.082 | 12/48 (SW 1088, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9022. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 9.59 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0458× (z -10.8) |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0908× (z -10.7) |
| [[H4 (line)]] | wt | 12.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0803× (z -9.4) |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0815× (z -9.5) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 9.43 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.153× (z -8.5) ⚠ cell-cycle shift, explains ~23% of this change |
| [[J82 (line)]] | alt | 7.22 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0640× (z -11.7) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.199× (z -9.2) |
| [[RKO (line)]] | wt | 8.31 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.101× (z -9.0) |
| [[SW 900 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9022), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX17]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[RABGGTA]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GMPPB]] | +0.60 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ACP2]] | +0.60 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[POLDIP2]] | +0.57 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[IDH3G]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MRPL49]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[NOC4L]] | +0.56 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CZIB]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[OTUB1]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[C5orf15]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[TMEM214]] | +0.55 | +0.47 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 11 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP1]] | -0.52 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[CBX3]] | -0.50 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[RPL35]] ⚠ | -0.49 | -0.52 / -0.28 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | -0.49 | -0.56 / -0.30 | both halves | 2e-04 |  |
| [[RPL35A]] | -0.48 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[TALAM1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[COX6C]] | -0.48 | -0.56 / -0.24 | both halves | 4e-04 |  |
| [[RPL18]] ⚠ | -0.48 | -0.57 / -0.23 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6A1]] | -0.47 | -0.56 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[RPS28]] ⚠ | -0.47 | -0.54 / -0.21 | both halves | 6e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL9]] ⚠ | -0.47 | -0.52 / -0.30 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | -0.47 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[RPS12]] | -0.47 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[RPS14]] | -0.47 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[RPLP2]] | -0.47 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[RPL34]] | -0.47 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[ATP5F1E]] | -0.46 | -0.45 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.7, -26.5); signed map (-7.3, -32.9). **Vector** length 54.3, 7.41% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.0 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Rifaximin (drug)]] 5 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | Fas activated serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,076,624-151,080,866 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FASTKD0, FAST |
| Gene groups (HGNC) | FASTK mitochondrial RNA binding family |
| Reactome | 3 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; Mitochondrial RNA degradation; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14296](https://www.uniprot.org/uniprotkb/Q14296) (Fas-activated serine/threonine kinase):

> Phosphorylates the splicing regulator TIA1, thereby promoting the inclusion of FAS exon 6, which leads to an mRNA encoding a pro-apoptotic form of the receptor.; [Isoform 4]: Required for the biogenesis of some mitochondrial-encoded mRNAs, specifically stabilizes ND6 (NADH dehydrogenase complex subunit 6) mRNA, and regulates its levels.

**Summary**, from NCBI Gene [10922](https://www.ncbi.nlm.nih.gov/gene/10922):

> The protein encoded by this gene is a member of the serine/threonine protein kinase family. This kinase was shown to be activated rapidly during Fas-mediated apoptosis in Jurkat cells. In response to Fas receptor ligation, it phosphorylates TIA1, an apoptosis-promoting nuclear RNA-binding protein. The encoded protein is a strong inducer of lymphocyte apoptosis. Two transcript variants encoding different isoforms have been found for this gene. Other variants exist, but their full-length natures …

**Accessions** — [HGNC:24676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24676) · Entrez [10922](https://www.ncbi.nlm.nih.gov/gene/10922) · UniProt [Q14296](https://www.uniprot.org/uniprotkb/Q14296) · Ensembl [ENSG00000164896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164896)

## Data

Gene col 9022: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9022); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9022, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9022]; `tensor/DDL_lfc|DDL_z.npy` [9022]; `embed/gene_vectors.npy` [9022]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9022 or target_col == 9022). Every well: [[FASTK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FASTK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
