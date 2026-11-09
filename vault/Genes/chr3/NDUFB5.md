---
symbol: "NDUFB5"
type: "gene"
col: 5874
ensembl_id: "ENSG00000136521"
name: "NADH:ubiquinone oxidoreductase subunit B5"
location: "3q26.33"
module: 28
arm: "+"
pooled_cpm: 34.57
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# NDUFB5

*NADH:ubiquinone oxidoreductase subunit B5* — 3q26.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +14.8, q 0e+00, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.29× (z +4.3, q 0.002, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 4.93×, NCI-H460 5.04×, MIA PaCa-2 6.65×, PANC-1 3.77×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 5.14×, NCI-H1792 7.04×, A549 6.22×, PANC-1 3.40×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.644× (z -5.2, q 1e-04, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX13]] (+0.63, fdr 9e-05), [[C1orf43]] (+0.60, fdr 1e-05), [[ATP5PB]] (+0.60, fdr 1e-05); moves opposite to [[BMP8B]] (-0.56, fdr 3e-05), [[PPM1G]] (-0.52, fdr 2e-04), [[GPRIN1]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5874.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (SW480 4.93×, NCI-H460 5.04×, MIA PaCa-2 6.65×, PANC-1 3.77×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (SW480 5.14×, NCI-H1792 7.04×, A549 6.22×, PANC-1 3.40×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +14.8 | 0e+00 | 44/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +12.6 | 7e-34 | 35/38 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +9.5 | 5e-19 | 39/42 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.63×** | +5.7 | 1e-06 | 34/46 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.002 | 26/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.3 | 0.080 | 20/47 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.080 | 21/47 (BT-474, SW 1271, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.21×** | +3.2 | 0.086 | 19/48 (NCI-H2347, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -5.2 | 1e-04 | 26/48 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.472×** | -4.0 | 0.018 | 25/48 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.743×** | -3.5 | 0.084 | 19/48 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | 0.530× | -3.4 | 0.10 | 20/47 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.757× | -3.1 | 0.21 | 18/47 (AN3 CA, SW1417, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -3.0 | 0.22 | 18/48 (KATO III, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 39.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +12.4) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 18.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +11.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 37.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +13.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 35.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +13.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 27.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 33.5 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.0455× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 40.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 33.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +10.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +11.4) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 31.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.04× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 27.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +13.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 53.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 30.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +10.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +11.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.12× (z +11.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +9.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0537× (z -9.2) |
| [[A-427 (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX13]] | +0.63 | +0.36 / +0.67 | both halves | 9e-05 |  |
| [[C1orf43]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[ATP5PB]] | +0.60 | +0.64 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 954 |
| [[PMPCB]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 | STRING 771 |
| [[TMEM35B]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PHYH]] | +0.58 | +0.60 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[COPS5]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 | STRING 483 |
| [[FAM204A]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[ARFGEF2]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PHC3]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[PSMC2]] | +0.56 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[QRSL1]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMP8B]] | -0.56 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PPM1G]] | -0.52 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[GPRIN1]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[EHD4]] | -0.51 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[TMEM201]] | -0.51 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[KLF13]] | -0.51 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[KLHL17]] | -0.50 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[CSNK1E]] | -0.50 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[PAQR4]] | -0.50 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[CORO7]] | -0.50 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[RTL10]] | -0.49 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[TSEN54]] | -0.49 | -0.52 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.5, 16.8); signed map (10.0, -22.2). **Vector** length 56.6, 11.7% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | -0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.0 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.0 | -1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | +1.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | +1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase subunit B5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.33 — chr3:179,604,690-179,627,647 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SGDH, CI-SGDH, MGC12314 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase supernumerary subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43674](https://www.uniprot.org/uniprotkb/O43674) (NADH dehydrogenase):

> Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone.

**Summary**, from NCBI Gene [4711](https://www.ncbi.nlm.nih.gov/gene/4711):

> The protein encoded by this gene is a subunit of the multisubunit NADH:ubiquinone oxidoreductase (complex I). Mammalian complex I is composed of 45 different subunits. It locates at the mitochondrial inner membrane. This protein has NADH dehydrogenase activity and oxidoreductase activity. It transfers electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone. Three transcript variants encoding different isoforms have been found for …

**Accessions** — [HGNC:7700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7700) · Entrez [4711](https://www.ncbi.nlm.nih.gov/gene/4711) · UniProt [O43674](https://www.uniprot.org/uniprotkb/O43674) · Ensembl [ENSG00000136521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136521)

## Data

Gene col 5874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5874); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5874]; `tensor/DDL_lfc|DDL_z.npy` [5874]; `embed/gene_vectors.npy` [5874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5874 or target_col == 5874). Every well: [[NDUFB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
