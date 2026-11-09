---
symbol: "WWP2"
type: "gene"
col: 12580
ensembl_id: "ENSG00000198373"
name: "WW domain containing E3 ubiquitin protein ligase 2"
location: "16q22.1"
module: 172
arm: "+"
pooled_cpm: 73.59
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# WWP2

*WW domain containing E3 ubiquitin protein ligase 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.38× (z +11.4, q 1e-27, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.406× (z -22.7, q 0e+00, down in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.819× (z -5.0, q 3e-05, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 0.213×, RKO 0.145×, SHP-77 0.225×, NCI-H2030 0.223×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.0867×, NCI-H460 0.223×, SW480 0.324×, NCI-H23 0.200×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.384×, SHP-77 0.494×, SW480 0.570×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 0.658×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLTA]] (+0.58, fdr 1e-05), [[FBXW9]] (+0.52, fdr 2e-05), [[GMEB1]] (+0.51, fdr 3e-05); moves opposite to [[HOOK1]] (-0.44, fdr 2e-04), [[HPS3]] (-0.40, fdr 1e-04), [[SSX2IP]] (-0.40, fdr 2e-04).
> It is in [[Module 172]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12580.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +11.4 | 1e-27 | 27/48 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +10.2 | 6e-22 | 30/49 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.00×** | +7.1 | 2e-10 | 32/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +4.3 | 0.002 | 16/48 (NCI-H2030, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.50×** | +4.2 | 0.003 | 19/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.19× | +4.1 | 0.004 | 16/48 (A498, LoVo, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.027 | 12/48 (SNU-1, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.6 | 0.027 | 17/48 (SHP-77, KATO III, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.4 | 0.048 | 13/48 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.14× | +3.2 | 0.082 | 9/48 (SNU-423, A549, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.34× | +3.0 | 0.14 | 8/49 (NCI-H2030, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12580.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (NCI-H460 0.213×, RKO 0.145×, SHP-77 0.225×, NCI-H2030 0.223×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.0867×, NCI-H460 0.223×, SW480 0.324×, NCI-H23 0.200×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 3 lines (SK-MEL-2 0.384×, SHP-77 0.494×, SW480 0.570×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 0.658×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.406×** | -22.7 | 0e+00 | 38/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -14.5 | 3e-45 | 32/42 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.570×** | -13.1 | 5e-37 | 31/45 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.645×** | -10.6 | 3e-24 | 39/47 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.707×** | -8.4 | 4e-15 | 26/48 (AN3 CA, NCI-H460, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.763×** | -6.8 | 8e-10 | 27/47 (SW1417, COLO 205, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.814×** | -5.2 | 2e-05 | 22/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.819×** | -5.0 | 3e-05 | 20/48 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.889× | -4.2 | 0.002 | 10/48 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.856× | -3.8 | 0.008 | 20/47 (HepG2/C3A, CFPAC-1, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.800×** | -3.3 | 0.050 | 13/46 (SW48, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.873× | -3.2 | 0.075 | 13/48 (HCT15, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.886× | -3.1 | 0.088 | 11/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | 0.882× | -3.0 | 0.11 | 7/47 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12580. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 91.4 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -22.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 147 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.658× (z -8.8) |
| [[SW480 (line)]] | alt | 144 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.76× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.570× (z -9.0) |
| [[C32 (line)]] | wt | 180 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -15.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 74.6 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 66.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -14.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 78.7 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +18.8) | [[Bortezomib (drug)]] 5 µM 0.0491× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.384× (z -10.3) |
| [[A-427 (line)]] | wt | 52.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -14.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 97.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -15.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 71.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.315× (z -12.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 95.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -17.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 69.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -17.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.494× (z -9.3) |
| [[A-172 (line)]] | wt | 34.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 62.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -17.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 71.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0673× (z -16.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 108 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -17.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -12.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 51.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 94.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 70.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -11.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 66.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0867× (z -25.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -20.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 55.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 61.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.294× (z -9.5) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 85.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -16.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 46.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +15.0) | — |
| [[AN3 CA (line)]] | alt | 78.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0909× (z -13.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[AsPC-1 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -10.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 69.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.290× (z -12.5) ⚠ toxic |
| [[H4 (line)]] | wt | 47.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -15.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 92.8 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0510× (z -28.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 53.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 45.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +19.8) | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +14.7) | — |
| [[NCI-H2347 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.430× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12580), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLTA]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[FBXW9]] | +0.52 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[GMEB1]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[COMMD1]] | +0.51 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[FRS2]] | +0.51 | +0.55 / +0.35 | both halves | 1e-04 | pathway: Intracellular signaling by second messengers |
| [[SLC38A7]] | +0.51 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TMEM199]] | +0.50 | +0.48 / +0.34 | both halves | 1e-04 | same gene group |
| [[ZNF358]] | +0.48 | +0.43 / +0.51 | both halves | 4e-05 |  |
| [[SNX8]] | +0.48 | +0.47 / +0.42 | both halves | 4e-05 | same gene group |
| [[AREL1]] | +0.47 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[GPATCH3]] | +0.47 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[ZNF200]] | +0.47 | +0.47 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOOK1]] | -0.44 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[HPS3]] | -0.40 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[SSX2IP]] | -0.40 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[ACAD8]] | -0.39 | -0.29 / -0.37 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-50.2, 11.9); signed map (-6.1, -16.7). **Vector** length 99.9, 24.2% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +11.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +2.4 | +2.3 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -10.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.6 | -4.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -4.3 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.2 | -5.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | +0.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.2 | -2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | WW domain containing E3 ubiquitin protein ligase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,762,328-69,941,741 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIP2 |
| Gene groups (HGNC) | C2 and WW domain containing; MicroRNA protein coding host genes; Nedd4 family E3 ubiquitin protein ligases |
| Reactome | 13 pathways, smallest: NOTCH3 Activation and Transmission of Signal to the Nucleus; RHOU GTPase cycle; Signaling by NOTCH3 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00308](https://www.uniprot.org/uniprotkb/O00308) (NEDD4-like E3 ubiquitin-protein ligase WWP2):

> E3 ubiquitin-protein ligase which accepts ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then directly transfers the ubiquitin to targeted substrates. Polyubiquitinates POU5F1 by 'Lys-63'-linked conjugation and promotes it to proteasomal degradation; in embryonic stem cells (ESCs) the ubiquitination is proposed to regulate POU5F1 protein level. Ubiquitinates EGR2 and promotes it to proteasomal degradation; in T-cells the ubiquitination inhibits …

**Summary**, from NCBI Gene [11060](https://www.ncbi.nlm.nih.gov/gene/11060):

> This gene encodes a member of the Nedd4 family of E3 ligases, which play an important role in protein ubiquitination. The encoded protein contains four WW domains and may play a role in multiple processes including chondrogenesis and the regulation of oncogenic signaling pathways via interactions with Smad proteins and the tumor suppressor PTEN. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the …

**Accessions** — [HGNC:16804](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16804) · Entrez [11060](https://www.ncbi.nlm.nih.gov/gene/11060) · UniProt [O00308](https://www.uniprot.org/uniprotkb/O00308) · Ensembl [ENSG00000198373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198373)

## Data

Gene col 12580: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12580); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12580, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12580]; `tensor/DDL_lfc|DDL_z.npy` [12580]; `embed/gene_vectors.npy` [12580]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12580 or target_col == 12580). Every well: [[WWP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WWP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
