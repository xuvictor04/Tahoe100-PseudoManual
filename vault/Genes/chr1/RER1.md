---
symbol: "RER1"
type: "gene"
col: 8115
ensembl_id: "ENSG00000157916"
name: "retention in endoplasmic reticulum sorting receptor 1"
location: "1p36.32"
module: 52
arm: "+"
pooled_cpm: 39.12
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# RER1

*retention in endoplasmic reticulum sorting receptor 1* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.77× (z +11.2, q 1e-26, up in 28 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Medroxyprogesterone acetate (drug)]] 0.5 µM: 1.30× (z +5.4, q 1e-05, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.693× (z -10.7, q 6e-24, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARFGAP1]] (+0.76, fdr 7e-06), [[TMEM104]] (+0.74, fdr 7e-06), [[CHFR]] (+0.73, fdr 7e-06); moves opposite to [[PUM1]] (-0.57, fdr 6e-05), [[TLK1]] (-0.55, fdr 3e-05), [[SETD2]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8115.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +11.2 | 1e-26 | 28/39 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.65×** | +10.3 | 3e-22 | 31/45 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.9 | 9e-10 | 24/41 (A-427, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.30×** | +5.4 | 1e-05 | 20/47 (RKO, LoVo, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.44×** | +5.3 | 1e-05 | 25/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +5.0 | 5e-05 | 25/45 (J82, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **1.23×** | +4.0 | 0.004 | 21/45 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.21×** | +4.0 | 0.005 | 16/48 (COLO 205, HOP62, …) | two highest doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.20× | +3.7 | 0.012 | 16/47 (SW480, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 0.5 µM |  | 1.19× | +3.5 | 0.025 | 12/48 (SW 900, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.025 | 9/46 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +3.3 | 0.041 | 14/48 (NCI-H2030, Panc 03.27, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.041 | 6/48 (A-427, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.17× | +3.2 | 0.060 | 13/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.075 | 11/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8115.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.693×** | -10.7 | 6e-24 | 31/47 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.608×** | -9.9 | 2e-20 | 39/48 (RPMI-7951, J82, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.622×** | -9.8 | 3e-20 | 28/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.658×** | -8.6 | 8e-16 | 36/48 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.683×** | -7.9 | 4e-13 | 33/48 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -6.7 | 2e-09 | 28/47 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.555×** | -6.4 | 2e-08 | 31/49 (SW480, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.752×** | -5.9 | 3e-07 | 26/48 (H4, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.759×** | -5.7 | 8e-07 | 29/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.773×** | -5.3 | 6e-06 | 23/48 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -5.1 | 2e-05 | 24/48 (RPMI-7951, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.783×** | -5.0 | 2e-05 | 24/47 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.803×** | -4.4 | 5e-04 | 21/48 (AN3 CA, SNU-423, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.844× | -3.5 | 0.018 | 16/48 (A-172, HOP62, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.892× | -3.4 | 0.030 | 15/48 (A-427, SW 900, …) | rises with dose | low cells (technical?) |
| [[Adenosine (drug)]] 0.5 µM |  | 0.852× | -3.3 | 0.032 | 6/48 (KATO III, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8115. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 69.8 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -10.1) |
| [[A-427 (line)]] | wt | 41.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 4.18× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.5) |
| [[HOP62 (line)]] | alt | 44.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -8.9) |
| [[KATO III (line)]] | alt | 44.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.339× (z -10.3) |
| [[LoVo (line)]] | wt | 39.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.398× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.96× (z +10.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.399× (z -9.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 57.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.451× (z -11.3) |
| [[A549 (line)]] | wt | 26.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -8.9) |
| [[HS-578T (line)]] | alt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -10.0) |
| [[J82 (line)]] | alt | 51.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.77× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 39.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.353× (z -8.6) |
| [[SNU-1 (line)]] | wt | 28.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.361× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 73.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8115), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP1]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[TMEM104]] | +0.74 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CHFR]] | +0.73 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[YKT6]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[GOLGA3]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[BET1L]] | +0.71 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[CHPF2]] | +0.70 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[SZT2]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[DPH7]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[FUBP3]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[UVSSA]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GAK]] | +0.67 | +0.50 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM1]] | -0.57 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[TLK1]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SETD2]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (10.1, -28.0); signed map (-50.6, 3.1). **Vector** length 90.1, 19.4% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.6 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +5.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.8 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -10.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.0 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | retention in endoplasmic reticulum sorting receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:2,391,775-2,405,442 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [O15258](https://www.uniprot.org/uniprotkb/O15258) (Protein RER1):

> Involved in the retention or retrieval of proteins localized in the endoplasmic reticulum from the early Golgi compartment, including the gamma-secretase complex subunit PEN-2 (PSENEN). Regulates intracellular trafficking of the gamma-secretase complex and amyloid-beta precursor protein (APP), thereby controlling APP levels at the cell surface and influencing the release of amyloid-beta peptides generated through gamma-secretase mediated processing of APP. During cerebral cortex and neural stem …

**Summary**, from NCBI Gene [11079](https://www.ncbi.nlm.nih.gov/gene/11079):

> The protein encoded by this gene is a multi-pass membrane protein that is localized to the golgi apparatus. It is involved in the retention of endoplasmic reticulum (ER) membrane proteins in the ER and retrieval of ER membrane proteins from the early Golgi compartment to facilitate gamma-secretase complex assembly. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:30309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30309) · Entrez [11079](https://www.ncbi.nlm.nih.gov/gene/11079) · UniProt [O15258](https://www.uniprot.org/uniprotkb/O15258) · Ensembl [ENSG00000157916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157916)

## Data

Gene col 8115: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8115); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8115, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8115]; `tensor/DDL_lfc|DDL_z.npy` [8115]; `embed/gene_vectors.npy` [8115]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8115 or target_col == 8115). Every well: [[RER1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RER1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
