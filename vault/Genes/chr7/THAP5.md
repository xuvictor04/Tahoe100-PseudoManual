---
symbol: "THAP5"
type: "gene"
col: 10851
ensembl_id: "ENSG00000177683"
name: "THAP domain containing 5"
location: "7q31.1"
module: 11
arm: "+"
pooled_cpm: 23.14
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# THAP5

*THAP domain containing 5* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.39× (z +11.8, q 3e-29, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.337× (z -7.7, q 7e-12, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIP11]] (+0.75, fdr 7e-06), [[ERCC4]] (+0.74, fdr 7e-06), [[ASF1A]] (+0.71, fdr 7e-06); moves opposite to [[SMARCD2]] (-0.67, fdr 7e-06), [[SNHG30]] (-0.67, fdr 7e-06), [[CD46]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10851.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.39×** | +11.8 | 3e-29 | 45/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +10.8 | 9e-25 | 43/47 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +10.4 | 8e-23 | 44/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +9.3 | 1e-18 | 39/47 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.62×** | +6.5 | 7e-09 | 36/48 (RKO, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.3 | 3e-08 | 23/44 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +6.2 | 4e-08 | 32/44 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +6.1 | 6e-08 | 32/48 (A-172, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.2 | 1e-05 | 18/34 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.028 | 20/47 (NCI-H460, SW1417, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.040 | 14/48 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.19× | +3.3 | 0.043 | 14/48 (SNU-423, hTERT-HPNE, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.0 | 0.11 | 0/48 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10851.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.337×** | -7.7 | 7e-12 | 36/48 (RKO, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.374×** | -7.0 | 9e-10 | 32/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.629×** | -6.3 | 6e-08 | 30/47 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.649×** | -5.6 | 2e-06 | 26/47 (SW48, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.682×** | -5.2 | 2e-05 | 25/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -4.2 | 0.003 | 20/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.590×** | -3.7 | 0.015 | 18/39 (SNU-423, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.634×** | -3.2 | 0.087 | 11/28 (HT-29, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10851. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 27.7 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.81× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -15.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 39.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.39× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 27.7 | 0 | 2 (1 ⚠) | — | [[Pyridoxine (drug)]] 0.5 µM 0.0564× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 32.7 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.79× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 19.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.300× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -9.6) |
| [[SW480 (line)]] | alt | 19.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.12× (z +10.1) | — |
| [[A-172 (line)]] | wt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.3) | — |
| [[A498 (line)]] | wt | 39.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 13.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.74× (z +8.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.111× (z -10.8) ⚠ transcription drop |
| [[COLO 205 (line)]] | alt | 20.3 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.99× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -8.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10851), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | +0.75 | +0.82 / +0.72 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.74 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[ASF1A]] | +0.71 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[RTL6]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[NSRP1]] | +0.70 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[NME6]] | +0.70 | +0.82 / +0.57 | both halves | 1e-05 |  |
| [[LIG4]] | +0.69 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[UBQLN2]] | +0.68 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[LZIC]] | +0.67 | +0.79 / +0.57 | both halves | 8e-06 |  |
| [[ARL14EP]] | +0.67 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[ZNF770]] | +0.67 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ARCN1]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCD2]] | -0.67 | -0.69 / -0.62 | both halves | 7e-06 |  |
| [[SNHG30]] | -0.67 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[CD46]] | -0.65 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[CD81]] | -0.65 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[IGSF8]] | -0.64 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[SDHAP4]] | -0.62 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[NME2]] | -0.62 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[SEC11A]] | -0.62 | -0.70 / -0.57 | both halves | 1e-05 |  |
| [[DHRS1]] | -0.61 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[MFSD14CP]] | -0.60 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[MED17]] | -0.60 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[SMG1P5]] | -0.60 | -0.57 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-33.3, 8.0); signed map (1.6, -22.3). **Vector** length 103, 25.0% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +11.8 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.8 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.9 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.6 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.5 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.2 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.0 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.2 | -7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -7.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.1 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:108,554,543-108,569,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313O1132 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6K1](https://www.uniprot.org/uniprotkb/Q7Z6K1) (THAP domain-containing protein 5):

> Has sequence-specific DNA-binding activity and can function as transcriptional repressor (in vitro). May be a regulator of cell cycle: THAP5 overexpression in human cell lines causes cell cycle arrest at G2/M phase.

**Summary**, from NCBI Gene [168451](https://www.ncbi.nlm.nih.gov/gene/168451):

> Enables protease binding activity. Involved in negative regulation of cell cycle and negative regulation of transcription by RNA polymerase II. Located in chromatin and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23188) · Entrez [168451](https://www.ncbi.nlm.nih.gov/gene/168451) · UniProt [Q7Z6K1](https://www.uniprot.org/uniprotkb/Q7Z6K1) · Ensembl [ENSG00000177683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177683)

## Data

Gene col 10851: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10851); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10851, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10851]; `tensor/DDL_lfc|DDL_z.npy` [10851]; `embed/gene_vectors.npy` [10851]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10851 or target_col == 10851). Every well: [[THAP5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
