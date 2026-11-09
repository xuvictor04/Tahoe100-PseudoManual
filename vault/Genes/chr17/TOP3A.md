---
symbol: "TOP3A"
type: "gene"
col: 10809
ensembl_id: "ENSG00000177302"
name: "DNA topoisomerase III alpha"
location: "17p11.2"
module: 71
arm: "+"
pooled_cpm: 40.66
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# TOP3A

*DNA topoisomerase III alpha* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +20.6, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.594× (z -11.1, q 7e-26, down in 34 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.746× (z -6.2, q 7e-08, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLE3]] (+0.75, fdr 7e-06), [[CENPJ]] (+0.72, fdr 7e-06), [[MYO19]] (+0.67, fdr 7e-06); moves opposite to [[MTMR3]] (-0.63, fdr 1e-05), [[IFTAP]] (-0.63, fdr 7e-06), [[TAB2]] (-0.62, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +20.6 | 0e+00 | 45/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.56×** | +9.1 | 2e-17 | 32/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +9.0 | 4e-17 | 32/48 (C32, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +7.9 | 3e-13 | 31/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.2 | 3e-05 | 23/48 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.39×** | +5.0 | 5e-05 | 18/48 (LoVo, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.23×** | +4.5 | 6e-04 | 19/48 (NCI-H1573, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +4.0 | 0.005 | 21/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.19× | +3.7 | 0.015 | 20/48 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.015 | 9/48 (NCI-H460, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.19× | +3.6 | 0.015 | 16/48 (HT-29, RKO, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.18× | +3.6 | 0.017 | 16/48 (PANC-1, A-427, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.18× | +3.5 | 0.020 | 14/48 (Panc 03.27, J82, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.594×** | -11.1 | 7e-26 | 34/48 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.605×** | -10.3 | 2e-22 | 23/38 (SHP-77, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -10.2 | 3e-22 | 29/42 (C-33 A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -6.2 | 7e-08 | 28/48 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -6.2 | 7e-08 | 25/48 (SW480, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -4.8 | 1e-04 | 19/48 (Hs 766T, A-172, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.808×** | -4.5 | 5e-04 | 18/48 (CHP-212, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.867× | -4.0 | 0.004 | 22/48 (A498, A-172, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.832×** | -3.7 | 0.011 | 21/48 (A498, A-172, …) | inconsistent across doses | composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | 0.861× | -3.6 | 0.016 | 13/48 (A-427, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.839× | -3.6 | 0.018 | 16/47 (SW 1271, HEC-1-A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.792×** | -3.5 | 0.019 | 13/48 (HepG2/C3A, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.955× | -3.5 | 0.023 | 0/48 | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.028 | 14/47 (SW480, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **0.739×** | -3.4 | 0.029 | 17/48 (HS-578T, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.855× | -3.3 | 0.030 | 14/47 (hTERT-HPNE, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.856× | -3.3 | 0.032 | 16/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Alpelisib (drug)]] 5 µM |  | **0.760×** | -3.1 | 0.071 | 9/47 (HOP62, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.868× | -3.0 | 0.077 | 6/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.869× | -3.0 | 0.082 | 4/47 (PANC-1, LS 180, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.860× | -2.9 | 0.098 | 12/48 (SNU-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 71.0 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.449× (z -9.0) |
| [[A-172 (line)]] | wt | 55.5 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -18.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 71.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 30.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 36.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.443× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 158 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -21.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 76.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -18.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 29.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 53.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -18.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -10.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 43.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -13.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 31.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -9.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -20.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 46.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -10.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 49.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.165× (z -8.6) |
| [[CHP-212 (line)]] | wt | 35.6 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.0912× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 35.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.278× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +10.8) | — |
| [[hTERT-HPNE (line)]] | wt | 37.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -18.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -18.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +9.2) | — |
| [[RKO (line)]] | wt | 41.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 33.5 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.151× (z -11.0) |
| [[SW 1271 (line)]] | alt | 66.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0678× (z -9.5) |
| [[SW1417 (line)]] | alt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.1) | — |
| [[SW480 (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 54.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE3]] | +0.75 | +0.58 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 401 |
| [[CENPJ]] | +0.72 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[MYO19]] | +0.67 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[HAUS8]] | +0.67 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[HSPA14]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[CDCA5]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CENPO]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[FEN1]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 | pathway: DNA Double-Strand Break Repair; STRING 799 |
| [[DSN1]] | +0.60 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[GNAS-AS1]] | +0.60 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[QPCTL]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TOPBP1]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 753 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTMR3]] | -0.63 | -0.52 / -0.67 | both halves | 1e-05 |  |
| [[IFTAP]] | -0.63 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[TAB2]] | -0.62 | -0.46 / -0.72 | both halves | 3e-05 |  |
| [[DHFR2]] | -0.58 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[VAPA]] | -0.56 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CDC73]] | -0.54 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[GCOM1]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CEBPZOS]] | -0.53 | -0.49 / -0.58 | both halves | 2e-05 |  |
| [[CFL2]] | -0.53 | -0.40 / -0.64 | both halves | 4e-05 |  |
| [[PABIR1]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[AHR]] | -0.52 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[SAYSD1]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOP3A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZYG11A]] | B | ZYG11A activity raises TOP3A's level | lines that do not express ZYG11A (29) vs lines expressing it (21) | 1.04× lower at baseline in the lines without ZYG11A | 0.054 | ⚠ within organs, on part of the lines; also absent: ANOS1, LGSN, DAW1 |
| [[CFAP300]] | B | CFAP300 activity lowers TOP3A's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.11× higher at baseline in the lines without CFAP300 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.7, -48.6); signed map (-41.0, -40.0). **Vector** length 120, 31.9% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +20.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.5 | +9.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.9 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +5.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.4 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.7 | -4.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.2 | -11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.2 | -10.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA topoisomerase III alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:18,271,428-18,315,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZGRF7; previously TOP3 |
| Gene groups (HGNC) | Zinc fingers GRF-type; Topoisomerases |
| Reactome | 33 pathways, smallest: Strand-asynchronous mitochondrial DNA replication; Impaired BRCA2 binding to PALB2; Defective HDR through Homologous Recombination Repair (HRR) due to PALB2 loss of BRCA1 binding function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13472](https://www.uniprot.org/uniprotkb/Q13472) (DNA topoisomerase 3-alpha):

> Releases the supercoiling and torsional tension of DNA introduced during the DNA replication and transcription by transiently cleaving and rejoining one strand of the DNA duplex. Introduces a single-strand break via transesterification at a target site in duplex DNA. The scissile phosphodiester is attacked by the catalytic tyrosine of the enzyme, resulting in the formation of a DNA-(5'-phosphotyrosyl)-enzyme intermediate and the expulsion of a 3'-OH DNA strand. The free DNA strand then …

**Summary**, from NCBI Gene [7156](https://www.ncbi.nlm.nih.gov/gene/7156):

> This gene encodes a DNA topoisomerase, an enzyme that controls and alters the topologic states of DNA during transcription. This enzyme catalyzes the transient breaking and rejoining of a single strand of DNA which allows the strands to pass through one another, thus reducing the number of supercoils and altering the topology of DNA. This enzyme forms a complex with BLM which functions in the regulation of recombination in somatic cells. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:11992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11992) · Entrez [7156](https://www.ncbi.nlm.nih.gov/gene/7156) · UniProt [Q13472](https://www.uniprot.org/uniprotkb/Q13472) · Ensembl [ENSG00000177302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177302)

## Data

Gene col 10809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10809); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10809]; `tensor/DDL_lfc|DDL_z.npy` [10809]; `embed/gene_vectors.npy` [10809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10809 or target_col == 10809). Every well: [[TOP3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOP3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
