---
symbol: "ZBTB14"
type: "gene"
col: 12525
ensembl_id: "ENSG00000198081"
name: "zinc finger and BTB domain containing 14"
location: "18p11.31"
module: 16
arm: "+"
pooled_cpm: 8.56
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZBTB14

*zinc finger and BTB domain containing 14* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.13× (z +5.7, q 9e-06, up in 7 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Clotrimazole (drug)]] 5 µM: 1.31× (z +4.8, q 4e-04, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.408× (z -16.3, q 0e+00, down in 36 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCF]] (+0.61, fdr 1e-05), [[ZNF639]] (+0.58, fdr 1e-05), [[THAP11]] (+0.57, fdr 1e-05); moves opposite to [[ASPHD1]] (-0.54, fdr 1e-05), [[TALAM1]] (-0.52, fdr 2e-05), [[TM2D1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.7 | 9e-06 | 7/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Clotrimazole (drug)]] 5 µM |  | **1.31×** | +4.8 | 4e-04 | 22/48 (SHP-77, J82, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.5 | 0.096 | 11/37 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.30× | +3.4 | 0.11 | 9/46 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.28× | +3.2 | 0.16 | 6/46 (NCI-H2030, RKO, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.28× | +3.1 | 0.19 | 5/15 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12525.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -16.3 | 0e+00 | 36/45 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.422×** | -11.1 | 4e-26 | 37/47 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -10.4 | 6e-23 | 41/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -9.5 | 5e-19 | 34/47 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -8.7 | 6e-16 | 29/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.517×** | -8.5 | 2e-15 | 26/46 (NCI-H2030, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -8.2 | 1e-14 | 29/47 (C-33 A, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -7.5 | 6e-12 | 29/47 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -6.5 | 5e-09 | 25/46 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -6.2 | 3e-08 | 21/46 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -6.1 | 7e-08 | 24/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.635×** | -5.9 | 2e-07 | 23/44 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -5.8 | 3e-07 | 20/44 (A498, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -4.8 | 5e-05 | 17/47 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.689×** | -4.5 | 2e-04 | 17/44 (HT-29, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -4.2 | 8e-04 | 17/45 (NCI-H1573, HS-578T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 14.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0524× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -15.0) |
| [[PANC-1 (line)]] | alt | 12.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.8) |
| [[SW480 (line)]] | alt | 10.6 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -14.2) |
| [[A-172 (line)]] | wt | 9.72 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -14.0) |
| [[BT-474 (line)]] | alt | 5.75 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -10.3) |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0731× (z -10.5) |
| [[HS-578T (line)]] | alt | 6.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0570× (z -13.1) |
| [[A498 (line)]] | wt | 8.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -12.0) |
| [[COLO 205 (line)]] | alt | 5.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -8.8) |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0848× (z -9.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 7.85 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -12.4) |
| [[J82 (line)]] | alt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.5) |
| [[KATO III (line)]] | alt | 7.96 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0352× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 9.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.2) |
| [[MIA PaCa-2 (line)]] | alt | 9.40 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.130× (z -10.3) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0805× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~9% of this change |
| [[SK-MEL-2 (line)]] | alt | 7.56 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -10.7) |
| [[A-427 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCF]] | +0.61 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ZNF639]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 | same gene group |
| [[THAP11]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[ADO]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[MINPP1]] | +0.56 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[CAND1]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[C17orf58]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[C9orf64]] | +0.54 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ZNF816]] | +0.54 | +0.36 / +0.63 | both halves | 1e-04 | same gene group |
| [[PPP1R3D]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[AMACR]] | +0.53 | +0.38 / +0.49 | both halves | 6e-05 |  |
| [[PDIK1L]] | +0.53 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASPHD1]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TALAM1]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TM2D1]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RSL1D1-DT]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[RAP1B]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[MAL2-AS1]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[POLR2J3-1]] | -0.47 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[MALAT1]] | -0.47 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[ADNP-AS1]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.309). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-49.9, -1.1); signed map (-3.7, -35.8). **Vector** length 59.2, 8.59% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.7 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -3.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.4 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.2 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.1 | -16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.1 | -4.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -8.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:5,289,019-5,297,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF478; previously ZFP161 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43829](https://www.uniprot.org/uniprotkb/O43829) (Zinc finger and BTB domain-containing protein 14):

> Transcriptional activator of the dopamine transporter (DAT), binding its promoter at the consensus sequence 5'-CCTGCACAGTTCACGGA-3'. Binds to 5'-d(GCC)(n)-3' trinucleotide repeats in promoter regions and acts as a repressor of the FMR1 gene. Transcriptional repressor of MYC and thymidine kinase promoters.

**Summary**, from NCBI Gene [7541](https://www.ncbi.nlm.nih.gov/gene/7541):

> Enables DNA-binding transcription factor activity and transcription cis-regulatory region binding activity. Involved in negative regulation of DNA-templated transcription. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:12860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12860) · Entrez [7541](https://www.ncbi.nlm.nih.gov/gene/7541) · UniProt [O43829](https://www.uniprot.org/uniprotkb/O43829) · Ensembl [ENSG00000198081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198081)

## Data

Gene col 12525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12525); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12525]; `tensor/DDL_lfc|DDL_z.npy` [12525]; `embed/gene_vectors.npy` [12525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12525 or target_col == 12525). Every well: [[ZBTB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
