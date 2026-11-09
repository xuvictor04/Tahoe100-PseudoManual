---
symbol: "EFCAB13"
type: "gene"
col: 10965
ensembl_id: "ENSG00000178852"
name: "EF-hand calcium binding domain 13"
location: "17q21.32"
module: 13
arm: "+"
pooled_cpm: 50.79
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 38
n_dd_up_clean: 3
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 9
direction_downstream: 5
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EFCAB13

*EF-hand calcium binding domain 13* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.36× (z +4.1, q 0.012, up in 14 of 34 measured lines) ⚠ cell-cycle shift, explains ~22% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.33× (z +3.8, q 0.023, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.374× (z -18.4, q 0e+00, down in 30 of 34 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.362× (z -13.4, q 7e-39, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB3]] (+0.80, fdr 7e-06, ⚠ same locus), [[ADAMTS9-AS2]] (+0.64, fdr 7e-06), [[LOXL2]] (+0.55, fdr 1e-05), [[OSMR-DT]] (+0.53, fdr 3e-05); moves opposite to [[RNF43]] (-0.50, fdr 4e-05), [[AXIN2]] (-0.48, fdr 4e-05), [[LINC02253]] (-0.47, fdr 7e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[RNF217]] → it (grade B ⚠); 5 go from it, the strongest it → [[IL1RAP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10965.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.36×** | +4.1 | 0.012 | 14/34 (A498, BT-474, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.38×** | +4.1 | 0.012 | 20/33 (hTERT-HPNE, J82, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +3.8 | 0.023 | 18/33 (hTERT-HPNE, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.023 | 20/35 (A498, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.058 | 15/34 (SW 900, NCI-H2347, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.20× | +3.4 | 0.067 | 13/34 (J82, NCI-H2030, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.29× | +3.2 | 0.11 | 15/34 (A498, A-172, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 5 µM |  | 1.58× | +3.2 | 0.11 | 14/34 (NCI-H23, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 1.55× | +3.0 | 0.15 | 17/34 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 19 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10965.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.374×** | -18.4 | 0e+00 | 30/34 (CFPAC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.287×** | -16.5 | 0e+00 | 30/34 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.316×** | -15.2 | 0e+00 | 33/34 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.343×** | -13.6 | 7e-40 | 32/34 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.362×** | -13.4 | 7e-39 | 30/34 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.433×** | -11.0 | 2e-26 | 30/34 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.488×** | -9.5 | 3e-19 | 30/34 (PANC-1, CHP-212, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.500×** | -8.8 | 1e-16 | 27/33 (hTERT-HPNE, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.516×** | -8.7 | 2e-16 | 28/34 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.547×** | -8.0 | 1e-13 | 27/34 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -7.3 | 2e-11 | 29/35 (SNU-423, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -7.2 | 3e-11 | 24/34 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.600×** | -6.2 | 2e-08 | 22/31 (NCI-H23, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.635×** | -5.8 | 3e-07 | 22/33 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.668×** | -5.3 | 4e-06 | 22/34 (C32, HS-578T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.497×** | -4.8 | 5e-05 | 24/34 (CFPAC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -4.8 | 6e-05 | 23/34 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.501×** | -4.8 | 6e-05 | 24/34 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.519×** | -4.5 | 2e-04 | 21/34 (Hs 766T, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.811×** | -3.9 | 0.002 | 19/34 (C32, CHP-212, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.749×** | -3.8 | 0.003 | 15/34 (A549, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.817×** | -3.8 | 0.003 | 18/34 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.595×** | -3.6 | 0.007 | 16/34 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -3.5 | 0.008 | 21/34 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.688×** | -3.5 | 0.008 | 16/34 (SW 900, H4, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.601×** | -3.5 | 0.008 | 18/34 (Hs 766T, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10965. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -24.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -15.1) |
| [[Hs 766T (line)]] | wt | 127 | 0 | 12 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.239× (z -10.8) |
| [[A549 (line)]] | wt | 82.8 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -22.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0800× (z -17.3) |
| [[C32 (line)]] | wt | 240 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -22.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -13.3) |
| [[NCI-H23 (line)]] | alt | 84.6 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -13.7) |
| [[PANC-1 (line)]] | alt | 53.9 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -21.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -17.0) |
| [[HEC-1-A (line)]] | alt | 149 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -12.7) |
| [[HS-578T (line)]] | alt | 87.3 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -15.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -10.4) |
| [[J82 (line)]] | alt | 75.4 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.152× (z -15.0) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 101 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.279× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 193 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -16.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -11.0) |
| [[H4 (line)]] | wt | 49.9 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0498× (z -16.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.187× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 79.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.7) |
| [[Panc 03.27 (line)]] | alt | 67.6 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -15.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW1417 (line)]] | alt | 33.4 | 1 (1 ⚠) | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.164× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 50.5 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.150× (z -8.5) |
| [[AsPC-1 (line)]] | alt | 55.0 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 77.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -16.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW 900 (line)]] | alt | 66.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -13.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.148× (z -10.8) |
| [[BT-474 (line)]] | alt | 30.0 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0559× (z -10.5) |
| [[HCT15 (line)]] | alt | 25.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0472× (z -16.0) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CHP-212 (line)]] | wt | 79.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.120× (z -9.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.269× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 18.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 28.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.298× (z -9.6) |
| [[SW 1088 (line)]] | alt | 96.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A498 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.48 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.16 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.48 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.15 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.57 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 10.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10965), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB3]] | +0.80 | +0.79 / +0.83 | both halves | 7e-06 | ⚠ same locus (9.5 kb, same strand: neighbours can correlate without regulation) |
| [[ADAMTS9-AS2]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[LOXL2]] | +0.55 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[OSMR-DT]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[EFCAB13-DT]] | +0.53 | +0.37 / +0.58 | both halves | 7e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[OSMR]] | +0.52 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[FAM20C]] | +0.52 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[LUCAT1]] | +0.52 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PPP4R1L]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[LINC02882]] | +0.50 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[CLDN14-AS1]] | +0.50 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[FBLN7]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[NRG3]] | +0.50 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SETBP1]] | +0.49 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF43]] | -0.50 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[AXIN2]] | -0.48 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[LINC02253]] | -0.47 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[FGD3]] | -0.45 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[PPM1H]] | -0.45 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PIK3C2B]] | -0.45 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PPFIBP2]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[DLEU1]] | -0.43 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[ANO9]] | -0.43 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[SLC5A4-AS1]] | -0.43 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[LINC01622]] | -0.43 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PEG10]] | -0.42 | -0.40 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF217]] | B | RNF217 activity raises EFCAB13's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 3.45× lower at baseline in the lines without RNF217 | 0.023 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[IL1RAP]] | B | IL1RAP activity raises EFCAB13's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 3.90× lower at baseline in the lines without IL1RAP | 0.030 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[LINC02813]] | B | LINC02813 activity raises EFCAB13's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without LINC02813 | 0.030 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN |
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises EFCAB13's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 3.12× lower at baseline in the lines without ADAMTS9-AS2 | 0.045 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[CTSL]] | B | CTSL activity raises EFCAB13's level | lines that do not express CTSL (9) vs lines expressing it (41) | 3.62× lower at baseline in the lines without CTSL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000286964, FRMD6, SYDE1; maybe low, not absent |
| [[HTR7]] | B | HTR7 activity raises EFCAB13's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without HTR7 | 0.074 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[ITGB3]] | C | ITGB3 activity raises EFCAB13's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 4.27× lower at baseline in the lines without ITGB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[SETBP1]] | C | SETBP1 activity raises EFCAB13's level | lines that do not express SETBP1 (19) vs lines expressing it (31) | 2.98× lower at baseline in the lines without SETBP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAM7-AS1, ENSG00000253471, DPYSL3; co-absent with the target |
| [[TSHZ3]], [[TSHZ3-AS1]] | C | TSHZ3, TSHZ3-AS1 activity raises EFCAB13's level | lines that do not express TSHZ3, TSHZ3-AS1 (25) vs lines expressing them (25) | 2.67× lower at baseline in the lines without TSHZ3, TSHZ3-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target; co-absent genes |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | EFCAB13 activity raises IL1RAP's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 2.77× lower at baseline in the lines without EFCAB13 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[ST6GALNAC2]] | B | EFCAB13 activity raises ST6GALNAC2's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 1.58× lower at baseline in the lines without EFCAB13 | 0.032 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[EFCAB13-DT]] | B | EFCAB13 activity raises EFCAB13-DT's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without EFCAB13 | 0.068 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[RNF217]] | B | EFCAB13 activity raises RNF217's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 3.18× lower at baseline in the lines without EFCAB13 | 0.074 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent |
| [[ITGB3]] | C | EFCAB13 activity raises ITGB3's level | lines that do not express EFCAB13 (14) vs lines expressing it (36) | 5.89× lower at baseline in the lines without EFCAB13 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNS3, TRIM6, GPR176; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.432). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.1, 23.8); signed map (31.1, 48.8). **Vector** length 95.9, 27.4% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.7 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +0.9 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.3 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -8.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -2.7 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -8.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -4.8 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | EF-hand calcium binding domain 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,323,290-47,441,312 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40342; previously C17orf57 |
| Gene groups (HGNC) | EF-hand domain containing |
| Matched by | ensembl_id |

UniProt [Q8IY85](https://www.uniprot.org/uniprotkb/Q8IY85) carries no function annotation.

**Summary**, from NCBI Gene [124989](https://www.ncbi.nlm.nih.gov/gene/124989):

> Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26864) · Entrez [124989](https://www.ncbi.nlm.nih.gov/gene/124989) · UniProt [Q8IY85](https://www.uniprot.org/uniprotkb/Q8IY85) · Ensembl [ENSG00000178852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178852)

## Data

Gene col 10965: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10965); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10965, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10965]; `tensor/DDL_lfc|DDL_z.npy` [10965]; `embed/gene_vectors.npy` [10965]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10965 or target_col == 10965). Every well: [[EFCAB13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
