---
symbol: "MAD2L1"
type: "gene"
col: 8870
ensembl_id: "ENSG00000164109"
name: "mitotic arrest deficient 2 like 1"
location: "4q27"
module: 22
arm: "+"
pooled_cpm: 21.34
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# MAD2L1

*mitotic arrest deficient 2 like 1* — 4q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.16× (z +13.6, q 3e-39, up in 30 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.30× (z +3.1, q 0.084, up in 12 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 4.21×, KATO III 4.64×, HT-29 5.63×, NCI-H460 5.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 3.35×, HT-29 5.30×, NCI-H460 4.71×, PANC-1 2.97×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 0.619× (z -5.9, q 3e-06, down in 29 of 48 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.746× (z -5.0, q 1e-04, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBK]] (+0.91, fdr 7e-06), [[CCNA2]] (+0.88, fdr 7e-06), [[BUB1B]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SW480 4.21×, KATO III 4.64×, HT-29 5.63×, NCI-H460 5.04×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SW480 3.35×, HT-29 5.30×, NCI-H460 4.71×, PANC-1 2.97×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **3.16×** | +13.6 | 3e-39 | 30/32 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.84×** | +12.8 | 3e-35 | 40/42 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.37×** | +9.8 | 2e-20 | 34/41 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **1.86×** | +7.6 | 3e-12 | 33/46 (PANC-1, SW 900, …) | all doses, flat | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.61×** | +5.8 | 6e-07 | 32/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.47×** | +4.8 | 2e-04 | 24/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.47×** | +4.7 | 2e-04 | 25/48 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.28×** | +4.3 | 0.001 | 16/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.40×** | +4.1 | 0.002 | 22/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.39×** | +4.0 | 0.003 | 22/48 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.38×** | +4.0 | 0.003 | 22/46 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | **1.40×** | +4.0 | 0.003 | 19/46 (H4, LoVo, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.084 | 12/48 (HOP62, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.619×** | -5.9 | 3e-06 | 29/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.746×** | -5.0 | 1e-04 | 26/48 (HCT15, HT-29, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.679×** | -4.7 | 4e-04 | 21/46 (hTERT-HPNE, SW 900, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.671×** | -4.6 | 6e-04 | 22/48 (LS 180, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.770×** | -4.5 | 8e-04 | 23/48 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.722×** | -3.8 | 0.017 | 20/48 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **0.810×** | -3.6 | 0.024 | 21/48 (A-427, RPMI-7951, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.027 | 14/47 (H4, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.809×** | -3.5 | 0.029 | 19/48 (SK-MEL-2, SW480, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.754×** | -3.4 | 0.030 | 14/48 (SW 1088, HCT15, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **0.742×** | -3.4 | 0.030 | 14/48 (H4, Hs 766T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -3.4 | 0.031 | 16/48 (NCI-H2347, SK-MEL-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.755×** | -3.3 | 0.043 | 17/47 (NCI-H2030, SW 1271, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.044 | 17/47 (LS 180, C-33 A, …) | rises with dose | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.689×** | -3.2 | 0.044 | 15/46 (C32, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.770×** | -3.2 | 0.051 | 16/46 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.8 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.318× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.241× (z -12.8) |
| [[LS 180 (line)]] | wt | 23.4 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.302× (z -9.1) |
| [[SW480 (line)]] | alt | 22.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.21× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 19.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.154× (z -9.5) |
| [[A-427 (line)]] | wt | 38.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.43× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | [[Selinexor (drug)]] 5 µM 0.328× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 26.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[NCI-H460 (line)]] | wt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[HOP62 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.109× (z -8.6) |
| [[KATO III (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.64× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.145× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0931× (z -8.7) |
| [[PANC-1 (line)]] | alt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | — |
| [[RKO (line)]] | wt | 34.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.198× (z -8.5) |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBK]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 952 |
| [[CCNA2]] | +0.88 | +0.89 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 988 |
| [[BUB1B]] | +0.87 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[LMNB1]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[KIF11]] | +0.86 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 973 |
| [[ARHGAP11A]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | STRING 461 |
| [[SKA3]] | +0.85 | +0.84 / +0.82 | both halves | 7e-06 | STRING 555 |
| [[CIT]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NCAPH]] | +0.85 | +0.87 / +0.82 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 734 |
| [[RACGAP1]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 870 |
| [[KIF15]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 654 |
| [[ANLN]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 | STRING 682 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises MAD2L1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.50× lower at baseline in the lines without PIMREG | 0.004 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises MAD2L1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without MYBL1 | 0.027 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises MAD2L1's level | compounds that target MTOR: 4 of 8 lower it (Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PBK]] | C | PBK activity raises MAD2L1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.73× lower at baseline in the lines without PBK | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises MAD2L1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.59× lower at baseline in the lines without AURKB | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises MAD2L1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDCA3]] | C | CDCA3 activity raises MAD2L1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.75× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[NDC80]] | C | NDC80 activity raises MAD2L1's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.26× lower at baseline in the lines without NDC80 | 0.086 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises MAD2L1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 2.49× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[SKA3]] | C | SKA3 activity raises MAD2L1's level | lines that do not express SKA3 (3) vs lines expressing it (47) | 2.56× lower at baseline in the lines without SKA3 | 0.096 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.8, -53.5); signed map (-46.9, -43.1). **Vector** length 117, 33.8% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.71 to 28); *mitotic spindle* (hallmark, mean cos +0.66 to 38); *G2/M Transition* (reactome, mean cos +0.62 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +4.1 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +3.9 | +12.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +3.3 | +9.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | +3.0 | +7.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +1.8 | +1.0 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~94% of this change | -5.2 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -3.4 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.7 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.4 | -5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.7 | -2.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | mitotic arrest deficient 2 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q27 — chr4:120,055,623-120,066,858 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAD2, HSMAD2 |
| Gene groups (HGNC) | HORMA domain containing |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 27 pathways, smallest: Inactivation of APC/C via direct inhibition of the APC/C complex; Inhibition of the proteolytic activity of APC/C required for the onset of anaphase by mitotic spindle checkpoint components; APC-Cdc20 mediated degradation of Nek2A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13257](https://www.uniprot.org/uniprotkb/Q13257) (Mitotic spindle assembly checkpoint protein MAD2A):

> Component of the mitotic checkpoint complex (MCC), which inhibits APC/C and delays chromosome segregation until all chromosomes are properly attached to the mitotic spindle. The MCC, which consists of CDC20, MAD2L1/MAD2, BUB1B/BUBR1 and BUB3, is a key player of the spindle assembly checkpoint. The MCC-bound APC/C complex is inactive and this delays the metaphase/anaphase transition. When the spindle assembly checkpoint is silenced, the MCC-APC/C complex recruits the E2 enzyme UBCH10 and …

**Summary**, from NCBI Gene [4085](https://www.ncbi.nlm.nih.gov/gene/4085):

> MAD2L1 is a component of the mitotic spindle assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate. MAD2L1 is related to the MAD2L2 gene located on chromosome 1. A MAD2 pseudogene has been mapped to chromosome 14. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6763](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6763) · Entrez [4085](https://www.ncbi.nlm.nih.gov/gene/4085) · UniProt [Q13257](https://www.uniprot.org/uniprotkb/Q13257) · Ensembl [ENSG00000164109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164109)

## Data

Gene col 8870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8870); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8870]; `tensor/DDL_lfc|DDL_z.npy` [8870]; `embed/gene_vectors.npy` [8870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8870 or target_col == 8870). Every well: [[MAD2L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAD2L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
