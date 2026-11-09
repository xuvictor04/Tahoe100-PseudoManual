---
symbol: "GRPEL1"
type: "gene"
col: 3058
ensembl_id: "ENSG00000109519"
name: "GrpE like 1, mitochondrial"
location: "4p16.1"
module: 105
arm: "+"
pooled_cpm: 35.08
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# GRPEL1

*GrpE like 1, mitochondrial* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +15.9, q 0e+00, up in 47 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.326×, SK-MEL-2 0.360×, NCI-H23 0.387×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.225×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCAF2]] (+0.61, fdr 1e-05), [[CHSY1]] (+0.60, fdr 1e-05), [[EIF4A1]] (+0.59, fdr 1e-05); moves opposite to [[PPFIBP2]] (-0.51, fdr 5e-05), [[ADGRG1]] (-0.50, fdr 4e-05), [[PER3]] (-0.48, fdr 7e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +15.9 | 0e+00 | 47/48 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +8.7 | 1e-15 | 37/45 (NCI-H1573, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.92×** | +8.5 | 3e-15 | 43/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.78×** | +7.6 | 6e-12 | 47/48 (SW480, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.3 | 3e-11 | 37/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.74×** | +7.0 | 3e-10 | 37/48 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.0 | 3e-10 | 39/48 (HOP62, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.69×** | +6.8 | 9e-10 | 37/48 (NCI-H2030, HOP62, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.67×** | +6.7 | 2e-09 | 30/45 (SW480, A498, …) | all doses, flat | composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.70×** | +6.6 | 2e-09 | 33/47 (HOP62, RKO, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.58×** | +6.5 | 5e-09 | 35/46 (HOP62, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.60×** | +6.1 | 4e-08 | 36/48 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.50×** | +5.3 | 4e-06 | 35/47 (SW480, KATO III, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +5.2 | 7e-06 | 37/42 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.48×** | +5.1 | 1e-05 | 33/48 (H4, SW480, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 30/47 (HOP62, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +5.1 | 1e-05 | 27/47 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 26/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.91×** | +4.4 | 3e-04 | 33/47 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.8 | 0.004 | 25/48 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.50×** | +3.7 | 0.004 | 23/47 (NCI-H23, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.013 | 19/48 (HOP62, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.016 | 19/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.019 | 21/48 (C32, COLO 205, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3058.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (A-427 0.326×, SK-MEL-2 0.360×, NCI-H23 0.387×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.225×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.837× | -3.3 | 0.17 | 18/48 (SW 1088, NCI-H661, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.3 | 0.17 | 18/48 (CFPAC-1, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | 0.621× | -3.3 | 0.17 | 17/48 (A-427, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.834× | -3.1 | 0.17 | 15/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.793× | -3.1 | 0.17 | 16/48 (J82, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.840× | -3.1 | 0.17 | 15/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.786× | -3.1 | 0.17 | 17/47 (NCI-H1573, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.757× | -3.0 | 0.17 | 18/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 36.1 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.98× (z +10.3) | — |
| [[A498 (line)]] | wt | 34.7 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 39.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 38.7 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.40× (z +9.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.22× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 47.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[A-172 (line)]] | wt | 28.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.0) | — |
| [[A-427 (line)]] | wt | 41.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 33.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 57.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +11.2) | — |
| [[HEC-1-A (line)]] | alt | 39.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 29.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.2) | — |
| [[HS-578T (line)]] | alt | 21.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 25.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +11.3) | — |
| [[J82 (line)]] | alt | 59.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.9) | — |
| [[KATO III (line)]] | alt | 44.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.2) | — |
| [[LoVo (line)]] | wt | 36.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +10.2) | — |
| [[LOX-IMVI (line)]] | wt | 35.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.66× (z +10.2) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 29.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.1) | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 25.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 58.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCAF2]] | +0.61 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CHSY1]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[EIF4A1]] | +0.59 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[TSR1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CRYBG3]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[AK4]] | +0.57 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NIM1K]] | +0.57 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[AK2]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[RNF217]] | +0.55 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[OXSM]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[DDX24]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[STBD1]] | +0.53 | +0.44 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPFIBP2]] | -0.51 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ADGRG1]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PER3]] | -0.48 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[SNX12]] | -0.47 | -0.21 / -0.50 | both halves | 7e-04 |  |
| [[VAMP2]] | -0.46 | -0.44 / -0.36 | both halves | 1e-04 | pathway: Protein localization |
| [[FAM151B-DT]] | -0.45 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[MBD6]] | -0.45 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ZNF219]] | -0.44 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[ITGAV]] | -0.44 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[PRPF4B]] | -0.44 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[ABHD16A]] | -0.43 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[ANO9]] | -0.43 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GRPEL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.520). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.7, -18.2); signed map (-42.2, 26.7). **Vector** length 85.0, 22.7% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +15.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +3.7 | +6.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.5 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +7.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.0 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | -3.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | GrpE like 1, mitochondrial |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:7,058,671-7,068,085 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25609, GrpE, hMGE |
| Gene groups (HGNC) | TIM23 complex |
| Hallmark sets | UV_RESPONSE_UP, ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 5 pathways, smallest: Mitochondrial protein import; Dengue Virus-Host Interactions; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAV7](https://www.uniprot.org/uniprotkb/Q9HAV7) (GrpE protein homolog 1, mitochondrial):

> Nucleotide exchange factor (NEF) for mitochondrial HSP70 (mt-HSP70/HSPA9), facilitating the release of ADP from HSPA9 to allow ATP rebinding, which is essential for the chaperone cycle. Functions as a component of the presequence translocase-associated motor (PAM) complex, which drives ATP-dependent import of proteins into the mitochondrial matrix. In the PAM complex, supports the HSPA9-driven pulling mechanism that translocates polypeptides through the TIM23 complex. May control the …

**Summary**, from NCBI Gene [80273](https://www.ncbi.nlm.nih.gov/gene/80273):

> Enables identical protein binding activity and unfolded protein binding activity. Predicted to be involved in protein import into mitochondrial matrix. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19696) · Entrez [80273](https://www.ncbi.nlm.nih.gov/gene/80273) · UniProt [Q9HAV7](https://www.uniprot.org/uniprotkb/Q9HAV7) · Ensembl [ENSG00000109519](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109519)

## Data

Gene col 3058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3058); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3058]; `tensor/DDL_lfc|DDL_z.npy` [3058]; `embed/gene_vectors.npy` [3058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3058 or target_col == 3058). Every well: [[GRPEL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRPEL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
