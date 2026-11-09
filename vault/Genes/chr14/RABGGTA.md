---
symbol: "RABGGTA"
type: "gene"
col: 2049
ensembl_id: "ENSG00000100949"
name: "Rab geranylgeranyltransferase subunit alpha"
location: "14q12"
module: 96
arm: "+"
pooled_cpm: 4.42
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# RABGGTA

*Rab geranylgeranyltransferase subunit alpha* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.32× (z +9.3, q 7e-18, up in 4 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 0.05 µM: 1.43× (z +3.9, q 0.012, up in 4 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.453× (z -9.1, q 6e-17, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FASTK]] (+0.62, fdr 1e-05), [[PIDD1]] (+0.62, fdr 6e-05), [[CZIB]] (+0.58, fdr 1e-05); moves opposite to [[CBX3]] (-0.49, fdr 6e-04), [[ATP5F1E]] (-0.45, fdr 2e-04), [[KTN1]] (-0.44, fdr 7e-05).
> It is in [[Module 096]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2049.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.3 | 7e-18 | 4/7 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +7.0 | 8e-10 | 6/10 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.4 | 3e-08 | 12/22 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.6 | 5e-04 | 8/28 (NCI-H2347, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 0.05 µM |  | **1.43×** | +3.9 | 0.012 | 4/43 (NCI-H2347, RKO, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.053 | 9/25 (A498, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[OTS514 (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.068 | 1/23 (HOP62) | top dose only | noisy plate (z scaled); position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.077 | 1/44 (LoVo) | top dose only | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.2 | 0.077 | 3/13 (PANC-1, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.095 | 5/37 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.32× | +3.0 | 0.11 | 7/40 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.11 | 1/43 (NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2049.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.453×** | -9.1 | 6e-17 | 28/47 (hTERT-HPNE, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -8.9 | 1e-16 | 26/37 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -8.0 | 2e-13 | 28/44 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.522×** | -7.4 | 1e-11 | 23/45 (NCI-H2030, SNU-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -7.0 | 3e-10 | 21/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.564×** | -6.6 | 5e-09 | 22/44 (BT-474, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -6.5 | 8e-09 | 20/40 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.579×** | -6.3 | 3e-08 | 18/47 (NCI-H2347, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -6.1 | 9e-08 | 17/36 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.606×** | -5.2 | 1e-05 | 12/38 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.427×** | -5.1 | 2e-05 | 11/42 (A-427, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.455×** | -4.7 | 1e-04 | 18/42 (KATO III, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.762×** | -4.4 | 5e-04 | 14/45 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.681×** | -4.4 | 5e-04 | 16/43 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.546×** | -3.6 | 0.011 | 13/38 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -3.4 | 0.022 | 15/44 (HOP62, SK-MEL-2, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2049. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.37 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0845× (z -11.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.4) |
| [[HCT15 (line)]] | alt | 7.22 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0628× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 4.45 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0997× (z -8.5) |
| [[HOP62 (line)]] | alt | 3.07 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0764× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 1 | — | [[Panobinostat (drug)]] 0.05 µM 0.0266× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 4.41 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0561× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 13.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 3.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.4) |
| [[PANC-1 (line)]] | alt | 3.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -9.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.52 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2049), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FASTK]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[PIDD1]] | +0.62 | +0.38 / +0.62 | both halves | 6e-05 | pathway: TP53 Regulates Transcription of Cell Death Genes |
| [[CZIB]] | +0.58 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MEN1]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[BCS1L]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[MRPL49]] | +0.54 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[NOC4L]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ULK3]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[ALKBH6]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[IDH3G]] | +0.52 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[OPLAH]] ⚠ | +0.52 | +0.50 / +0.40 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TARBP2]] | +0.52 | +0.46 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX3]] | -0.49 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[ATP5F1E]] | -0.45 | -0.42 / -0.31 | both halves | 2e-04 |  |
| [[KTN1]] | -0.44 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[RNF24]] | -0.44 | -0.43 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.5, -26.3); signed map (-7.4, -33.1). **Vector** length 44.0, 4.90% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.2 | +1.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.5 | -9.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -7.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.7 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Rab geranylgeranyltransferase subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,265,538-24,271,611 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTAR3 |
| Gene groups (HGNC) | Prenyltransferase alpha subunit repeat containing; Rab geranylgeranyltransferase subunits |
| Reactome | 4 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; TP53 Regulates Transcription of Cell Death Genes; RAB geranylgeranylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92696](https://www.uniprot.org/uniprotkb/Q92696) (Geranylgeranyl transferase type-2 subunit alpha):

> Catalyzes the transfer of a geranylgeranyl moiety from geranylgeranyl diphosphate to both cysteines of Rab proteins with the C-terminal sequence -XXCC, -XCXC and -CCXX, such as RAB1A, RAB3A, RAB5A and RAB7A.

**Summary**, from NCBI Gene [5875](https://www.ncbi.nlm.nih.gov/gene/5875):

> Predicted to enable small GTPase binding activity. Predicted to contribute to Rab geranylgeranyltransferase activity. Predicted to be involved in endoplasmic reticulum to Golgi vesicle-mediated transport and protein geranylgeranylation. Predicted to be located in cytosol and plasma membrane. Predicted to be part of Rab-protein geranylgeranyltransferase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9795) · Entrez [5875](https://www.ncbi.nlm.nih.gov/gene/5875) · UniProt [Q92696](https://www.uniprot.org/uniprotkb/Q92696) · Ensembl [ENSG00000100949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100949)

## Data

Gene col 2049: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2049); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2049, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2049]; `tensor/DDL_lfc|DDL_z.npy` [2049]; `embed/gene_vectors.npy` [2049]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2049 or target_col == 2049). Every well: [[RABGGTA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RABGGTA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
