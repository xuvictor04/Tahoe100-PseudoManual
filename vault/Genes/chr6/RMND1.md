---
symbol: "RMND1"
type: "gene"
col: 7930
ensembl_id: "ENSG00000155906"
name: "required for meiotic nuclear division 1 homolog"
location: "6q25.1"
module: 33
arm: "+"
pooled_cpm: 34.56
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RMND1

*required for meiotic nuclear division 1 homolog* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.34× (z +19.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.654× (z -9.8, q 4e-20, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.121×, NCI-H23 0.271×, PANC-1 0.408×, A-172 0.263×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.269×, PANC-1 0.340×, RPMI-7951 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.0768×, PANC-1 0.397×; ⚠ toxic; transcription drop); [[Trimetrexate (drug)]] 0.5 µM in 1 line (CHP-212 0.0682×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 0.461×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.388×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAMM41]] (+0.73, fdr 1e-05), [[GEMIN5]] (+0.71, fdr 1e-05), [[PIGU]] (+0.67, fdr 2e-05); moves opposite to [[PSMD6-AS1]] (-0.64, fdr 4e-05), [[UBE2A]] (-0.63, fdr 1e-05), [[RNF217-AS1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NTN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7930.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.34×** | +19.7 | 0e+00 | 46/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +19.4 | 0e+00 | 46/48 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.12×** | +17.4 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +10.2 | 2e-22 | 37/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 3e-12 | 29/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.7 | 2e-04 | 16/48 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.15× | +4.7 | 2e-04 | 17/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.21×** | +4.4 | 9e-04 | 16/48 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +4.3 | 0.001 | 18/48 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.011 | 17/48 (HS-578T, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.5 | 0.023 | 6/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.083 | 5/48 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.1 | 0.085 | 12/48 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.10× | +3.1 | 0.085 | 3/48 (J82, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7930.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-427 0.121×, NCI-H23 0.271×, PANC-1 0.408×, A-172 0.263×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.269×, PANC-1 0.340×, RPMI-7951 0.195×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.0768×, PANC-1 0.397×; ⚠ toxic; transcription drop); [[Trimetrexate (drug)]] 0.5 µM in 1 line (CHP-212 0.0682×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 0.461×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.388×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -9.8 | 4e-20 | 31/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.689×** | -8.6 | 2e-15 | 29/46 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.686×** | -8.1 | 1e-13 | 28/43 (SK-MEL-2, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.717×** | -7.7 | 2e-12 | 28/47 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -7.1 | 2e-10 | 25/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.730×** | -7.0 | 2e-10 | 27/47 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.745×** | -6.5 | 5e-09 | 23/40 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.773×** | -5.9 | 2e-07 | 26/48 (SW480, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.785×** | -5.4 | 5e-06 | 22/48 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.805×** | -5.0 | 3e-05 | 21/48 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.810×** | -4.9 | 6e-05 | 22/48 (MIA PaCa-2, A549, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.854× | -3.7 | 0.012 | 12/48 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.867× | -3.3 | 0.042 | 9/48 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.764×** | -3.3 | 0.046 | 10/34 (hTERT-HPNE, C32, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.2 | 0.055 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.872× | -3.2 | 0.055 | 10/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7930. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.0 | 3 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.269× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -10.8) |
| [[PANC-1 (line)]] | alt | 41.9 | 3 | 6 (6 ⚠) | [[Belinostat (drug)]] 5 µM 2.36× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -13.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -13.2) ⚠ cell-cycle shift, explains ~79% of this change |
| [[A-427 (line)]] | wt | 42.8 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.31× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -10.0) |
| [[SNU-423 (line)]] | alt | 62.9 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.94× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -9.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 87.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.271× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.92× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.8) | — |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 2 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0682× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 42.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.06× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -10.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 33.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.9) | — |
| [[LoVo (line)]] | wt | 21.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +10.4) | — |
| [[RKO (line)]] | wt | 50.2 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.304× (z -10.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 57.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0768× (z -22.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 29.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 48.2 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.334× (z -8.5) |
| [[HS-578T (line)]] | alt | 31.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.93× (z +9.2) | — |
| [[J82 (line)]] | alt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.319× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 16.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.10× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.330× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 20.0 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -12.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.231× (z -8.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7930), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAMM41]] | +0.73 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GEMIN5]] | +0.71 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PIGU]] | +0.67 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[NLE1]] | +0.65 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EIF3M]] | +0.65 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[RAD17]] | +0.65 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[POLR3A]] | +0.65 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[DDX55]] | +0.64 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[DHX57]] | +0.63 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[BRAT1]] | +0.62 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[VPS37C]] | +0.61 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[VTA1]] | +0.61 | +0.51 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD6-AS1]] | -0.64 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[UBE2A]] | -0.63 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RNF217-AS1]] | -0.61 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | -0.60 | -0.31 / -0.32 | both halves | 2e-04 |  |
| [[CYP1B1-AS1]] | -0.59 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[HNRNPH3]] | -0.59 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.58 | -0.26 / -0.36 | both halves | 4e-04 |  |
| [[LSMEM1]] | -0.58 | -0.48 / -0.27 | both halves | 3e-04 |  |
| [[MICALL2]] | -0.57 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[LINC01135]] | -0.57 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[DDX5]] | -0.57 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[TTC6]] | -0.57 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NTN4 activity lowers RMND1's level | lines that do not express NTN4 (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without NTN4 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFAIP2, LINC02057, BMP2 |
| [[HDAC6]] | B | HDAC6 activity lowers RMND1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.4, -42.4); signed map (-8.7, -51.1). **Vector** length 90.6, 19.8% of its response variance represented; |z| ≥ 3 in 1,025 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.8 | +19.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +17.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +19.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -7.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.9 | -8.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | required for meiotic nuclear division 1 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:151,398,898-151,452,158 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA351K16.3, FLJ20627, RMD1; previously C6orf96 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWS8](https://www.uniprot.org/uniprotkb/Q9NWS8) (Required for meiotic nuclear division protein 1 homolog):

> Required for mitochondrial translation, possibly by coordinating the assembly or maintenance of the mitochondrial ribosome.

**Summary**, from NCBI Gene [55005](https://www.ncbi.nlm.nih.gov/gene/55005):

> The protein encoded by this gene belongs to the evolutionary conserved sif2 family of proteins that share the DUF155 domain in common. This protein is thought to be localized in the mitochondria and involved in mitochondrial translation. Mutations in this gene are associated with combined oxidative phosphorylation deficiency-11. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:21176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21176) · Entrez [55005](https://www.ncbi.nlm.nih.gov/gene/55005) · UniProt [Q9NWS8](https://www.uniprot.org/uniprotkb/Q9NWS8) · Ensembl [ENSG00000155906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155906)

## Data

Gene col 7930: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7930); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7930, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7930]; `tensor/DDL_lfc|DDL_z.npy` [7930]; `embed/gene_vectors.npy` [7930]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7930 or target_col == 7930). Every well: [[RMND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
