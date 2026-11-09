---
symbol: "BRI3BP"
type: "gene"
col: 11604
ensembl_id: "ENSG00000184992"
name: "BRI3 binding protein"
location: "12q24.31"
module: 6
arm: "+"
pooled_cpm: 39.19
n_lines_expressing: 49
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# BRI3BP

*BRI3 binding protein* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +11.0, q 3e-25, up in 37 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +3.7, q 0.013, up in 21 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 15.0×, A549 3.71×, SNU-423 7.34×, A498 3.87×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 6.14×, NCI-H1792 7.63×, HOP62 5.90×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.68×, NCI-H1792 3.36×, NCI-H1573 2.80×; ⚠ cell-cycle shift, explains ~62% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.341× (z -16.8, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM2]] (+0.73, fdr 7e-06), [[FANCA]] (+0.73, fdr 7e-06), [[DSCC1]] (+0.70, fdr 7e-06); moves opposite to [[TCEANC]] (-0.68, fdr 2e-05), [[RAD52]] (-0.62, fdr 4e-05), [[CIRBP]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARMCX1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11604.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 15.0×, A549 3.71×, SNU-423 7.34×, A498 3.87×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H1573 6.14×, NCI-H1792 7.63×, HOP62 5.90×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 2.68×, NCI-H1792 3.36×, NCI-H1573 2.80×; ⚠ cell-cycle shift, explains ~62% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **2.80×** | +11.0 | 3e-25 | 37/43 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.53×** | +9.8 | 2e-20 | 30/38 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.19×** | +8.6 | 1e-15 | 39/46 (A498, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **2.02×** | +7.7 | 1e-12 | 32/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.01×** | +7.7 | 2e-12 | 32/47 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.81×** | +6.5 | 7e-09 | 37/46 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.78×** | +6.0 | 2e-07 | 35/47 (MIA PaCa-2, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.72×** | +5.5 | 2e-06 | 25/40 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.41×** | +5.4 | 5e-06 | 27/46 (A549, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.50×** | +4.5 | 4e-04 | 26/43 (HT-29, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.013 | 21/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +3.5 | 0.019 | 19/47 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.39×** | +3.5 | 0.019 | 23/46 (SW480, HCT15, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.25×** | +3.5 | 0.021 | 24/47 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +3.4 | 0.029 | 19/46 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11604.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.341×** | -16.8 | 0e+00 | 41/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -12.2 | 9e-32 | 41/46 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -8.1 | 1e-13 | 34/47 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.324×** | -6.5 | 1e-08 | 33/47 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.333×** | -6.4 | 2e-08 | 32/45 (LS 180, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.587×** | -5.9 | 3e-07 | 35/46 (A-427, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.690×** | -5.8 | 4e-07 | 33/47 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.635×** | -5.0 | 3e-05 | 32/47 (NCI-H23, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -3.7 | 0.014 | 23/46 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.554×** | -3.4 | 0.035 | 19/46 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -3.2 | 0.060 | 21/46 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -3.2 | 0.063 | 21/47 (A-427, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **0.751×** | -3.2 | 0.063 | 21/46 (CFPAC-1, A-427, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.758×** | -3.1 | 0.083 | 16/47 (HCT15, A-427, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.90 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11604. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 124 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0564× (z -35.2) |
| [[NCI-H23 (line)]] | alt | 66.0 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -22.1) |
| [[A498 (line)]] | wt | 17.7 | 5 (5 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.79× (z +9.4) ⚠ cell-cycle shift, explains ~85% of this change | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -10.7) |
| [[A549 (line)]] | wt | 36.2 | 2 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +10.4) ⚠ cell-cycle shift, explains ~62% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 30.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 49.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -18.4) |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 48.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -18.6) |
| [[SNU-1 (line)]] | wt | 41.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0586× (z -16.2) |
| [[COLO 205 (line)]] | alt | 75.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.8) |
| [[HOP62 (line)]] | alt | 18.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.90× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.7) |
| [[HT-29 (line)]] | alt | 44.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -8.7) |
| [[LS 180 (line)]] | wt | 57.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 17.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.0× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H2347 (line)]] | alt | 27.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[RKO (line)]] | wt | 44.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.7) |
| [[SW1417 (line)]] | alt | 29.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -9.9) |
| [[A-172 (line)]] | wt | 23.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.9) |
| [[C-33 A (line)]] | alt | 91.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -14.3) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 26.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 43.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -10.1) |
| [[KATO III (line)]] | alt | 56.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.8) |
| [[LoVo (line)]] | wt | 57.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.7) |
| [[PANC-1 (line)]] | alt | 61.1 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.341× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -9.0) |
| [[SW480 (line)]] | alt | 54.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.2) |
| [[H4 (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0489× (z -13.0) |
| [[HCT15 (line)]] | alt | 47.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.5) |
| [[Hs 766T (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.5) |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.5) |
| [[J82 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 33.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0647× (z -12.3) |
| [[SNU-423 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.34× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.1) |
| [[SW48 (line)]] | wt | 56.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.221× (z -9.4) |
| [[AN3 CA (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11604), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM2]] | +0.73 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[FANCA]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[POLA1]] | +0.66 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CDC7]] | +0.66 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CDC45]] | +0.66 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[RNGTT]] | +0.66 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EXO1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[WDR76]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[BLM]] | +0.65 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCEANC]] | -0.68 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[RAD52]] | -0.62 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[CIRBP]] | -0.62 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[ETFRF1]] | -0.62 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[COPS5]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[NFKBIL1]] | -0.61 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[ATP6V1G1]] | -0.61 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.61 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ZNF181]] | -0.61 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.61 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[AK9]] | -0.61 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARMCX1]] | B | ARMCX1 activity lowers BRI3BP's level | lines that do not express ARMCX1 (23) vs lines expressing it (27) | 2.14× higher at baseline in the lines without ARMCX1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CTHRC1, CDH2, RFTN1 |
| [[ATP11A]] | C | ATP11A activity raises BRI3BP's level | lines that do not express ATP11A (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without ATP11A | 0.052 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: PLEKHG3, PPP1R26, IMPA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.659). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.9, -43.6); signed map (-36.3, -43.4). **Vector** length 103, 31.9% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *DNA Replication* (reactome, mean cos +0.52 to 40); *E2F G1/S* (control, mean cos +0.52 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +3.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.4 | +6.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.2 | +8.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.8 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +3.7 | +7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +0.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +0.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -16.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.7 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.1 | -1.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | BRI3 binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:124,993,645-125,031,231 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BNAS1, KG19, HCCR-2, HCCRBP-3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WY22](https://www.uniprot.org/uniprotkb/Q8WY22) (BRI3-binding protein):

> Involved in tumorigenesis and may function by stabilizing p53/TP53.

**Summary**, from NCBI Gene [140707](https://www.ncbi.nlm.nih.gov/gene/140707):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14251) · Entrez [140707](https://www.ncbi.nlm.nih.gov/gene/140707) · UniProt [Q8WY22](https://www.uniprot.org/uniprotkb/Q8WY22) · Ensembl [ENSG00000184992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184992)

## Data

Gene col 11604: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11604); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11604, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11604]; `tensor/DDL_lfc|DDL_z.npy` [11604]; `embed/gene_vectors.npy` [11604]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11604 or target_col == 11604). Every well: [[BRI3BP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRI3BP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
