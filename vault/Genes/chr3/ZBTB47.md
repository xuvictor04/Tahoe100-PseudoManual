---
symbol: "ZBTB47"
type: "gene"
col: 3595
ensembl_id: "ENSG00000114853"
name: "zinc finger and BTB domain containing 47"
location: "3p22.1"
module: 5
arm: "+"
pooled_cpm: 3.53
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 24
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ZBTB47

*zinc finger and BTB domain containing 47* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.99× (z +5.5, q 2e-05, up in 3 of 7 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.353× (z -12.2, q 3e-31, down in 32 of 36 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.359× (z -8.5, q 3e-15, down in 22 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASMTL-AS1]] (+0.61, fdr 1e-05), [[GGACT]] (+0.57, fdr 2e-05), [[SLC4A3]] (+0.56, fdr 1e-05); moves opposite to [[TESK2]] (-0.45, fdr 9e-05), [[MINDY2]] (-0.44, fdr 2e-04), [[ANAPC16]] (-0.44, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.99×** | +5.5 | 2e-05 | 3/7 (HS-578T, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.50× | +3.1 | 0.55 | 1/7 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.353×** | -12.2 | 3e-31 | 32/36 (HEC-1-A, RPMI-7951, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.262×** | -10.6 | 6e-24 | 32/41 (HS-578T, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.346×** | -8.8 | 3e-16 | 35/45 (J82, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.353×** | -8.6 | 1e-15 | 31/45 (SNU-423, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.359×** | -8.5 | 3e-15 | 22/35 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.434×** | -6.9 | 5e-10 | 26/43 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.453×** | -6.5 | 4e-09 | 19/28 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.453×** | -6.5 | 4e-09 | 23/44 (SK-MEL-2, A-427, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.454×** | -6.5 | 5e-09 | 25/43 (HEC-1-A, SNU-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.472×** | -6.2 | 3e-08 | 22/42 (HEC-1-A, SW 900, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.503×** | -5.7 | 7e-07 | 20/43 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.547×** | -5.0 | 3e-05 | 17/41 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -4.9 | 4e-05 | 17/34 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.581×** | -4.5 | 3e-04 | 16/44 (SNU-1, BT-474, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.396×** | -4.0 | 0.002 | 14/38 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -3.9 | 0.004 | 14/44 (Panc 03.27, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.415×** | -3.8 | 0.005 | 15/31 (SW480, NCI-H1792, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.650×** | -3.4 | 0.022 | 12/40 (C32, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.689×** | -3.1 | 0.055 | 7/43 (HEC-1-A, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **0.703×** | -2.9 | 0.088 | 8/44 (HOP62, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.706×** | -2.9 | 0.094 | 6/43 (HOP62, AsPC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -19.0) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0945× (z -14.2) |
| [[A-172 (line)]] | wt | 8.03 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -9.2) |
| [[HS-578T (line)]] | alt | 6.43 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0200× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0517× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 2.63 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0320× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 5.44 | 0 | 2 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0603× (z -9.2) |
| [[SNU-423 (line)]] | alt | 3.80 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW480 (line)]] | alt | 2.43 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.0825× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 1.69 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0623× (z -10.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 3.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -10.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[KATO III (line)]] | alt | 2.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -8.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[LoVo (line)]] | wt | 6.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0990× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 1.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0421× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 7.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0479× (z -14.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.947 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASMTL-AS1]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[GGACT]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SLC4A3]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MAPK12]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[BRD9]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[NBEAL2]] | +0.51 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SLC19A1]] | +0.51 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[SLC35C1]] | +0.51 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.49 | +0.38 / +0.54 | both halves | 7e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[NDST1]] | +0.49 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[WIZ]] | +0.49 | +0.43 / +0.47 | both halves | 3e-05 | same gene group |
| [[WASH9P]] | +0.48 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[NRBP2]] | +0.48 | +0.49 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TESK2]] | -0.45 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[MINDY2]] | -0.44 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[ANAPC16]] | -0.44 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CEP57]] | -0.43 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[TIMM17B]] ⚠ | -0.43 | -0.35 / -0.45 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[STARD10]] | -0.43 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[NABP2]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |
| [[CEP350]] | -0.42 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[ATP23]] | -0.42 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[HSCB]] | -0.42 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[PSMD10]] | -0.41 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[NUDT16L1]] | -0.41 | -0.33 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.393). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-11.9, -28.5); signed map (8.4, -50.6). **Vector** length 48.7, 5.89% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +5.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.5 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.5 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.4 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +1.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +1.7 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.6 | -10.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -1.9 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.7 | -8.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.3 | -0.9 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,653,697-42,667,580 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1190, DKFZp434N0615; previously ZNF651 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UFB7](https://www.uniprot.org/uniprotkb/Q9UFB7) (Zinc finger and BTB domain-containing protein 47):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [92999](https://www.ncbi.nlm.nih.gov/gene/92999):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26955) · Entrez [92999](https://www.ncbi.nlm.nih.gov/gene/92999) · UniProt [Q9UFB7](https://www.uniprot.org/uniprotkb/Q9UFB7) · Ensembl [ENSG00000114853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114853)

## Data

Gene col 3595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3595); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3595]; `tensor/DDL_lfc|DDL_z.npy` [3595]; `embed/gene_vectors.npy` [3595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3595 or target_col == 3595). Every well: [[ZBTB47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
