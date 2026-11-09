---
symbol: "RXRA"
type: "gene"
col: 11807
ensembl_id: "ENSG00000186350"
name: "retinoid X receptor alpha"
location: "9q34.2"
module: 3
arm: "+"
pooled_cpm: 26.93
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# RXRA

*retinoid X receptor alpha* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +6.1, q 7e-07, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.617× (z -11.8, q 1e-29, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TFEB]] (+0.60, fdr 1e-05), [[TEAD3]] (+0.56, fdr 1e-05), [[AGAP3]] (+0.54, fdr 1e-05); moves opposite to [[DCBLD2]] (-0.48, fdr 1e-04), [[AGK]] (-0.47, fdr 2e-04), [[TAF1A]] (-0.46, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.1 | 7e-07 | 22/48 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.0 | 2e-04 | 21/48 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.007 | 17/48 (A498, PANC-1, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.21× | +3.3 | 0.14 | 11/48 (KATO III, A-172, …) | top dose only | position effect removed |
| [[DT-061 (drug)]] 5 µM |  | 1.41× | +3.2 | 0.18 | 5/45 (HT-29, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.19 | 12/48 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.19 | 11/48 (NCI-H1573, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11807.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.617×** | -11.8 | 1e-29 | 33/47 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -10.8 | 9e-25 | 32/48 (A-427, LoVo, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -9.7 | 8e-20 | 30/46 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.684×** | -9.3 | 2e-18 | 34/48 (J82, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.647×** | -7.6 | 5e-12 | 32/48 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -7.4 | 1e-11 | 34/49 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -7.3 | 2e-11 | 27/48 (LoVo, A-172, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.709×** | -5.7 | 7e-07 | 25/48 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.728×** | -5.5 | 2e-06 | 20/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.572×** | -5.1 | 2e-05 | 20/48 (A498, KATO III, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.758×** | -4.8 | 8e-05 | 24/48 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.734×** | -4.5 | 4e-04 | 18/39 (C-33 A, SW48, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.613×** | -4.4 | 4e-04 | 21/48 (A498, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.778×** | -4.4 | 5e-04 | 22/48 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.776×** | -4.2 | 9e-04 | 22/46 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -4.1 | 0.001 | 19/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.637×** | -4.1 | 0.001 | 19/47 (MIA PaCa-2, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -3.9 | 0.004 | 17/48 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.038 | 14/48 (A-172, HT-29, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 44.0 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.8) |
| [[A-172 (line)]] | wt | 49.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -9.6) |
| [[C32 (line)]] | wt | 27.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.7) |
| [[LoVo (line)]] | wt | 22.5 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0607× (z -23.2) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -14.9) |
| [[RKO (line)]] | wt | 27.5 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +14.8) | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 40.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.498× (z -10.6) |
| [[HCT15 (line)]] | alt | 28.5 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0907× (z -10.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 29.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[SW 900 (line)]] | alt | 31.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.7) |
| [[A-427 (line)]] | wt | 14.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -9.8) |
| [[A549 (line)]] | wt | 23.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[H4 (line)]] | wt | 22.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0765× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.7) |
| [[J82 (line)]] | alt | 26.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.425× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -8.7) |
| [[A498 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFEB]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Circadian clock |
| [[TEAD3]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[AGAP3]] | +0.54 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[NOL4L]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NR2F6]] | +0.53 | +0.61 / +0.49 | both halves | 1e-05 | pathway: Nuclear Receptor transcription pathway |
| [[PIP5K1C]] | +0.53 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[PTPRJ]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[NFIC]] | +0.53 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[RAI1]] | +0.53 | +0.57 / +0.43 | both halves | 3e-05 | pathway: Circadian clock |
| [[TAF4]] | +0.52 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[FRAT2]] | +0.52 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TENT4B]] | +0.52 | +0.34 / +0.52 | both halves | 1e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCBLD2]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[AGK]] | -0.47 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[TAF1A]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 | pathway: Epigenetic regulation of gene expression |
| [[HDAC9]] | -0.46 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GTF2H3]] | -0.45 | -0.46 / -0.38 | both halves | 6e-05 | pathway: Epigenetic regulation of gene expression |
| [[SEMA3A]] | -0.45 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ZDHHC21]] | -0.43 | -0.19 / -0.54 | ⚠ one half (not replicated) | 8e-04 | pathway: Signaling by Nuclear Receptors |
| [[DUS4L]] | -0.43 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TOMM34]] | -0.43 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[EFL1]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[FKTN]] | -0.42 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[ICAM2]] | -0.42 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[SLC30A9]] | -0.42 | -0.54 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.292). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-8.8, -2.7); signed map (-18.6, 20.9). **Vector** length 97.9, 21.8% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -0.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.5 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +4.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.3 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.9 | -9.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.7 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -9.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.4 | -4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | -4.4 | -2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | retinoid X receptor alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:134,317,098-134,440,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NR2B1, RXRalpha, RXR-alpha |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Retinoid X receptors |
| Hallmark sets | BILE_ACID_METABOLISM, UV_RESPONSE_DN, P53_PATHWAY |
| Reactome | 57 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to triglyceride lipolysis in adipose; NR1H2 & NR1H3 regulate gene expression linked to gluconeogenesis; NR1H2 & NR1H3 regulate gene expression to limit cholesterol uptake |
| Matched by | ensembl_id |

**Function**, from UniProt [P19793](https://www.uniprot.org/uniprotkb/P19793) (Retinoic acid receptor RXR-alpha):

> Receptor for retinoic acid that acts as a transcription factor. Forms homo- or heterodimers with retinoic acid receptors (RARs) and binds to target response elements in response to their ligands, all-trans or 9-cis retinoic acid, to regulate gene expression in various biological processes. The RAR/RXR heterodimers bind to the retinoic acid response elements (RARE) composed of tandem 5'-AGGTCA-3' sites known as DR1-DR5 to regulate transcription. The high affinity ligand for retinoid X receptors …

**Summary**, from NCBI Gene [6256](https://www.ncbi.nlm.nih.gov/gene/6256):

> Retinoid X receptors (RXRs) and retinoic acid receptors (RARs) are nuclear receptors that mediate the biological effects of retinoids by their involvement in retinoic acid-mediated gene activation. These receptors function as transcription factors by binding as homodimers or heterodimers to specific sequences in the promoters of target genes. The protein encoded by this gene is a member of the steroid and thyroid hormone receptor superfamily of transcriptional regulators. Alternative splicing …

**Accessions** — [HGNC:10477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10477) · Entrez [6256](https://www.ncbi.nlm.nih.gov/gene/6256) · UniProt [P19793](https://www.uniprot.org/uniprotkb/P19793) · Ensembl [ENSG00000186350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186350)

## Data

Gene col 11807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11807); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11807]; `tensor/DDL_lfc|DDL_z.npy` [11807]; `embed/gene_vectors.npy` [11807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11807 or target_col == 11807). Every well: [[RXRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RXRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
