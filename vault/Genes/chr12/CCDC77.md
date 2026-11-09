---
symbol: "CCDC77"
type: "gene"
col: 4195
ensembl_id: "ENSG00000120647"
name: "coiled-coil domain containing 77"
location: "12p13.33"
module: 67
arm: "+"
pooled_cpm: 25.6
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CCDC77

*coiled-coil domain containing 77* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +18.1, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.494× (z -8.9, q 3e-16, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCM]] (+0.74, fdr 7e-06), [[CDC25C]] (+0.72, fdr 7e-06), [[OIP5]] (+0.67, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4195.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +18.1 | 0e+00 | 40/48 (Panc 03.27, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.96×** | +16.3 | 0e+00 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.82×** | +14.4 | 4e-45 | 36/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +12.8 | 2e-35 | 33/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +12.5 | 1e-33 | 34/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.59×** | +11.2 | 2e-27 | 31/47 (LoVo, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.3 | 2e-11 | 18/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.29×** | +6.1 | 8e-08 | 18/47 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +6.0 | 1e-07 | 15/48 (A498, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +5.3 | 8e-06 | 14/48 (SW 900, RKO, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.25×** | +5.2 | 8e-06 | 15/45 (SW480, HT-29, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.22×** | +4.9 | 5e-05 | 18/47 (A-427, LoVo, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.42×** | +4.5 | 3e-04 | 10/47 (A498, C32, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.41×** | +4.3 | 6e-04 | 6/46 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.3 | 8e-04 | 13/48 (HOP62, H4, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 1.19× | +4.2 | 8e-04 | 9/47 (A-172, AN3 CA, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.19× | +4.2 | 8e-04 | 13/48 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.004 | 6/48 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.018 | 6/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.09× | +3.1 | 0.048 | 9/48 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.063 | 6/47 (NCI-H23, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4195.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -8.9 | 3e-16 | 23/48 (A498, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -8.8 | 4e-16 | 30/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -7.4 | 3e-11 | 21/48 (MIA PaCa-2, SNU-1, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -7.2 | 9e-11 | 21/47 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.748×** | -7.0 | 3e-10 | 21/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.755×** | -6.8 | 1e-09 | 20/47 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.758×** | -6.7 | 2e-09 | 24/47 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.624×** | -5.9 | 2e-07 | 16/48 (SW 900, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.792×** | -5.6 | 1e-06 | 18/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.807×** | -5.2 | 1e-05 | 18/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.679×** | -4.9 | 5e-05 | 13/47 (SW 900, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.814×** | -4.8 | 9e-05 | 15/34 (SW480, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.812×** | -4.7 | 9e-05 | 15/48 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.871× | -4.7 | 1e-04 | 14/48 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.878× | -4.4 | 4e-04 | 9/48 (H4, MIA PaCa-2, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.705×** | -4.4 | 4e-04 | 14/47 (SNU-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.835× | -4.3 | 5e-04 | 13/47 (HCT15, SNU-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.710×** | -4.3 | 5e-04 | 13/47 (SW 900, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.853× | -3.6 | 0.007 | 9/47 (A-427, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4195. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.5 | 4 (1 ⚠) | 7 (5 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.8) | [[Digitoxin (drug)]] 0.5 µM 0.362× (z -14.8) |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -10.9) |
| [[A498 (line)]] | wt | 30.5 | 0 | 5 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.404× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.0 | 1 | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +9.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -14.1) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.211× (z -12.7) |
| [[A-427 (line)]] | wt | 69.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 43.1 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 20.4 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.6) | — |
| [[LoVo (line)]] | wt | 22.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 40.4 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0649× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 35.1 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0607× (z -11.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0956× (z -9.1) ⚠ toxic |
| [[H4 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.307× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0970× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.166× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.210× (z -9.0) |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[SW1417 (line)]] | alt | 15.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.0) | — |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4195), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCM]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CDC25C]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[OIP5]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[TICRR]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CDCA5]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[HAUS8]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[CENPQ]] | +0.65 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[KIF22]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SLF1]] | +0.63 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[POC1A]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[C21orf58]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[CEP152]] | +0.63 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CCDC77's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF595]] | B | ZNF595 activity raises CCDC77's level | lines that do not express ZNF595 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without ZNF595 | 0.018 | ⚠ within organs, on part of the lines; also absent: TIGD7, ZNF530, MSN |
| [[DSCC1]] | C | DSCC1 activity raises CCDC77's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without DSCC1 | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.8, -50.4); signed map (-43.4, -41.6). **Vector** length 88.2, 18.7% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 12); *G2/M checkpoint* (hallmark, mean cos +0.55 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +12.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.5 |
|  | [[NG25 (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +1.7 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +0.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +4.5 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.3 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -5.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -5.8 | -6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.3 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -4.8 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -7.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 77 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:389,273-442,642 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13183 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

UniProt [Q9BR77](https://www.uniprot.org/uniprotkb/Q9BR77) carries no function annotation.

**Summary**, from NCBI Gene [84318](https://www.ncbi.nlm.nih.gov/gene/84318):

> Located in centrosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28203](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28203) · Entrez [84318](https://www.ncbi.nlm.nih.gov/gene/84318) · UniProt [Q9BR77](https://www.uniprot.org/uniprotkb/Q9BR77) · Ensembl [ENSG00000120647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120647)

## Data

Gene col 4195: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4195); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4195, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4195]; `tensor/DDL_lfc|DDL_z.npy` [4195]; `embed/gene_vectors.npy` [4195]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4195 or target_col == 4195). Every well: [[CCDC77 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC77.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
