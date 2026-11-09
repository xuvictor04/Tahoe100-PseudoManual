---
symbol: "ZCCHC9"
type: "gene"
col: 5237
ensembl_id: "ENSG00000131732"
name: "zinc finger CCHC-type containing 9"
location: "5q14.1"
module: 12
arm: "+"
pooled_cpm: 35.81
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# ZCCHC9

*zinc finger CCHC-type containing 9* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.30× (z +4.4, q 0.006, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.725× (z -7.4, q 8e-11, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRA10AC1]] (+0.72, fdr 7e-06), [[NKAP]] (+0.70, fdr 7e-06), [[PIGBOS1]] (+0.69, fdr 7e-06); moves opposite to [[STT3B]] (-0.65, fdr 1e-05), [[SMG1P3]] (-0.63, fdr 1e-05), [[RBBP7]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 0.006 | 18/48 (A-427, LOX-IMVI, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.24×** | +3.6 | 0.061 | 23/47 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.061 | 17/48 (Hs 766T, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.22× | +3.3 | 0.15 | 16/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.19 | 13/47 (PANC-1, NCI-H460, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.22 | 11/47 (PANC-1, SNU-423, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.725×** | -7.4 | 8e-11 | 27/47 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.640×** | -7.3 | 9e-11 | 33/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -7.2 | 9e-11 | 28/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.364×** | -7.2 | 9e-11 | 35/49 (A549, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.650×** | -7.0 | 2e-10 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.699×** | -5.8 | 5e-07 | 26/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.460×** | -5.5 | 3e-06 | 31/48 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -5.2 | 1e-05 | 24/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.803×** | -5.0 | 3e-05 | 24/48 (Hs 766T, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.732×** | -4.9 | 6e-05 | 24/47 (HS-578T, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.769×** | -4.3 | 1e-03 | 24/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.762×** | -4.3 | 1e-03 | 23/48 (C32, A-172, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.784×** | -3.7 | 0.008 | 19/47 (SW48, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | 0.818× | -3.0 | 0.10 | 13/41 (hTERT-HPNE, SW 900, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 43.6 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.466× (z -10.6) |
| [[SW 900 (line)]] | alt | 51.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.5) |
| [[HOP62 (line)]] | alt | 34.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.392× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 33.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0763× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.346× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 34.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 2 | — | [[Norepinephrine (hydrochloride) (drug)]] 0.05 µM 0.0640× (z -9.3) |
| [[SW480 (line)]] | alt | 34.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.375× (z -10.0) |
| [[A-172 (line)]] | wt | 37.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.8) |
| [[C32 (line)]] | wt | 26.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -10.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.265× (z -8.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -15.3) ⚠ cell-cycle shift, explains ~52% of this change |
| [[NCI-H2347 (line)]] | alt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 37.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.5) |
| [[PANC-1 (line)]] | alt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.3) |
| [[SW 1088 (line)]] | alt | 59.9 | 0 | 1 | — | [[Malotilate (drug)]] 5 µM 0.0583× (z -9.1) |
| [[SW 1271 (line)]] | alt | 55.8 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0854× (z -9.1) |
| [[A-427 (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRA10AC1]] | +0.72 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[NKAP]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PIGBOS1]] | +0.69 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MRPS18C]] | +0.69 | +0.51 / +0.74 | both halves | 1e-05 |  |
| [[ZNF766]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SEC62]] | +0.68 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[MRPL2]] | +0.67 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.67 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CCDC127]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MRPS31]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.66 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ALG2]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STT3B]] | -0.65 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.61 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[AKT1]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ATP2A2]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ILF3]] | -0.58 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[RPSA]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[ADAM15]] | -0.57 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[FKBP9]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[CRTAP]] | -0.57 | -0.48 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-40.0, -10.6); signed map (-12.8, -5.6). **Vector** length 82.4, 18.2% of its response variance represented; |z| ≥ 3 in 709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +4.8 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.0 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.6 | -3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.9 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.5 | -5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.0 | -2.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:81,301,587-81,313,297 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761J139, PPP1R41 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N567](https://www.uniprot.org/uniprotkb/Q8N567) (Zinc finger CCHC domain-containing protein 9):

> May down-regulate transcription mediated by NF-kappa-B and the serum response element.

**Summary**, from NCBI Gene [84240](https://www.ncbi.nlm.nih.gov/gene/84240):

> Enables RNA binding activity. Predicted to be involved in DNA-templated transcription. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25424](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25424) · Entrez [84240](https://www.ncbi.nlm.nih.gov/gene/84240) · UniProt [Q8N567](https://www.uniprot.org/uniprotkb/Q8N567) · Ensembl [ENSG00000131732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131732)

## Data

Gene col 5237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5237); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5237]; `tensor/DDL_lfc|DDL_z.npy` [5237]; `embed/gene_vectors.npy` [5237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5237 or target_col == 5237). Every well: [[ZCCHC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
