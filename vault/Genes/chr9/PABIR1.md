---
symbol: "PABIR1"
type: "gene"
col: 11958
ensembl_id: "ENSG00000187866"
name: "PP2A Aalpha (PPP2R1A) and B55A (PPP2R2A) interacting phosphatase regulator 1"
location: "9q21.11"
module: 16
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# PABIR1

*PP2A Aalpha (PPP2R1A) and B55A (PPP2R2A) interacting phosphatase regulator 1* — 9q21.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +12.4, q 2e-32, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.422× (z -9.1, q 3e-17, down in 22 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.604× (z -5.4, q 2e-05, down in 19 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSTF2T]] (+0.76, fdr 7e-06), [[KLHL9]] (+0.76, fdr 7e-06), [[RTL6]] (+0.74, fdr 7e-06); moves opposite to [[GNRH1]] (-0.69, fdr 7e-06), [[TPTEP2-CSNK1E]] (-0.63, fdr 7e-06), [[DRD4]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +12.4 | 2e-32 | 31/37 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.02×** | +11.7 | 4e-29 | 40/46 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +11.2 | 1e-26 | 41/45 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.62×** | +9.8 | 2e-20 | 35/42 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.31×** | +8.8 | 1e-16 | 36/46 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.35×** | +8.3 | 7e-15 | 8/12 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +8.1 | 5e-14 | 30/45 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.15×** | +8.1 | 5e-14 | 22/36 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.69×** | +7.8 | 3e-13 | 14/45 (HEC-1-A, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +7.7 | 9e-13 | 0/5 | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.72×** | +5.5 | 2e-06 | 15/41 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.2 | 1e-05 | 6/21 (HS-578T, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +4.9 | 5e-05 | 4/21 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.5 | 2e-04 | 7/24 (KATO III, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.58×** | +4.5 | 3e-04 | 7/36 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +4.4 | 4e-04 | 13/46 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 6e-04 | 8/44 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +4.0 | 0.002 | 8/38 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.006 | 8/44 (AsPC-1, HepG2/C3A, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.009 | 5/46 (A498, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.422×** | -9.1 | 3e-17 | 22/35 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.604×** | -5.4 | 2e-05 | 19/44 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.660×** | -4.4 | 0.002 | 17/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -3.7 | 0.034 | 15/44 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rifaximin (drug)]] 0.05 µM |  | 0.725× | -3.2 | 0.17 | 11/42 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.813× | -3.1 | 0.17 | 10/46 (SNU-1, HT-29, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.749× | -3.1 | 0.17 | 11/45 (KATO III, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 7.98 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -9.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSTF2T]] | +0.76 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.76 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[RTL6]] | +0.74 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[SAYSD1]] | +0.73 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[ZNF510]] | +0.72 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[SLC35A4]] | +0.72 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[C7orf25]] | +0.71 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[SRP68]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ZNF252P-1]] | +0.71 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[BBS10]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ZNF260]] | +0.69 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[ZNF502]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNRH1]] | -0.69 | -0.68 / -0.69 | both halves | 7e-06 |  |
| [[TPTEP2-CSNK1E]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[DRD4]] | -0.61 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[C9orf153]] | -0.60 | -0.49 / -0.57 | both halves | 2e-05 |  |
| [[METTL21A]] | -0.59 | -0.40 / -0.59 | both halves | 5e-05 |  |
| [[MBOAT7]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[SMG1P5]] | -0.59 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[PPP1R32]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.59 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.58 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[EEF1AKMT4]] | -0.58 | -0.59 / -0.59 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.830). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.4, 11.8); signed map (0.9, -29.6). **Vector** length 55.7, 7.23% of its response variance represented; |z| ≥ 3 in 1,098 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +9.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +8.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +4.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -3.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -2.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | PP2A Aalpha (PPP2R1A) and B55A (PPP2R2A) interacting phosphatase regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.11 — chr9:68,780,065-68,785,566 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17347; previously C9orf42, FAM122A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96E09](https://www.uniprot.org/uniprotkb/Q96E09) (PPP2R1A-PPP2R2A-interacting phosphatase regulator 1):

> Acts as an inhibitor of serine/threonine-protein phosphatase 2A (PP2A) activity. Inhibits PP2A activity by blocking the substrate binding site on PPP2R2A and the active site of PPP2CA. Potentiates ubiquitin-mediated proteasomal degradation of serine/threonine-protein phosphatase 2A catalytic subunit alpha (PPP2CA). Inhibits PP2A-mediated dephosphorylation of WEE1, promoting ubiquitin-mediated proteolysis of WEE1, thereby releasing G2/M checkpoint.

**Summary**, from NCBI Gene [116224](https://www.ncbi.nlm.nih.gov/gene/116224):

> Enables protein phosphatase 2A binding activity and protein serine/threonine phosphatase inhibitor activity. Involved in mitotic G2/M transition checkpoint; positive regulation of cell growth; and positive regulation of proteasomal ubiquitin-dependent protein catabolic process. Located in cytoplasm and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23490) · Entrez [116224](https://www.ncbi.nlm.nih.gov/gene/116224) · UniProt [Q96E09](https://www.uniprot.org/uniprotkb/Q96E09) · Ensembl [ENSG00000187866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187866)

## Data

Gene col 11958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11958); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11958]; `tensor/DDL_lfc|DDL_z.npy` [11958]; `embed/gene_vectors.npy` [11958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11958 or target_col == 11958). Every well: [[PABIR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PABIR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
