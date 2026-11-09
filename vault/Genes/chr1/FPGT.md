---
symbol: "FPGT"
type: "gene"
col: 14890
ensembl_id: "ENSG00000254685"
name: "fucose-1-phosphate guanylyltransferase"
location: "1p31.1"
module: 17
arm: "+"
pooled_cpm: 14.48
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 36
n_dd_up_clean: 17
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# FPGT

*fucose-1-phosphate guanylyltransferase* — 1p31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.81× (z +8.5, q 9e-15, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.279× (z -18.2, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC2LI1]] (+0.69, fdr 7e-06), [[RWDD3]] (+0.66, fdr 7e-06), [[METTL14]] (+0.65, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.63, fdr 7e-06), [[EGR3]] (-0.58, fdr 1e-05), [[UBASH3B]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NRP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.81×** | +8.5 | 9e-15 | 36/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.34×** | +6.0 | 5e-07 | 23/48 (A498, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.5 | 7e-06 | 25/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +4.9 | 1e-04 | 18/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +4.9 | 1e-04 | 17/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.44×** | +4.8 | 1e-04 | 21/47 (SW480, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.26×** | +4.7 | 2e-04 | 19/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +4.6 | 3e-04 | 16/47 (SW480, SW48, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 3e-04 | 19/47 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 4e-04 | 17/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +4.4 | 5e-04 | 19/48 (HCT15, NCI-H2347, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +4.3 | 8e-04 | 14/47 (KATO III, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.001 | 15/48 (SW480, LoVo, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 15/48 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 11/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.014 | 13/48 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.020 | 8/47 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.279×** | -18.2 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.290×** | -17.7 | 0e+00 | 41/46 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.435×** | -16.8 | 0e+00 | 40/47 (PANC-1, HS-578T, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.344×** | -14.9 | 0e+00 | 43/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.375×** | -13.5 | 3e-39 | 35/47 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.383×** | -13.4 | 1e-38 | 39/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.491×** | -10.1 | 3e-22 | 31/47 (RPMI-7951, C32, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.487×** | -9.8 | 5e-21 | 29/43 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.277×** | -9.6 | 7e-20 | 34/48 (NCI-H460, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.514×** | -9.5 | 1e-19 | 36/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.639×** | -9.0 | 1e-17 | 27/46 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.335×** | -8.1 | 2e-14 | 30/44 (RKO, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -7.2 | 3e-11 | 31/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -7.1 | 6e-11 | 24/46 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -6.9 | 2e-10 | 28/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.650×** | -6.1 | 3e-08 | 24/47 (SW480, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.752×** | -5.7 | 3e-07 | 25/48 (Hs 766T, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -5.2 | 6e-06 | 17/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.784×** | -4.9 | 3e-05 | 19/48 (MIA PaCa-2, Hs 766T, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.560×** | -4.3 | 4e-04 | 17/45 (NCI-H460, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 14 (8 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.133× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.177× (z -14.8) |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -17.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.118× (z -15.4) |
| [[Hs 766T (line)]] | wt | 29.2 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -11.8) |
| [[C32 (line)]] | wt | 19.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -10.4) |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -14.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0600× (z -13.5) |
| [[SW480 (line)]] | alt | 12.0 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.142× (z -13.7) |
| [[H4 (line)]] | wt | 15.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.206× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.60× (z +9.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0829× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -10.1) |
| [[A498 (line)]] | wt | 23.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -9.9) |
| [[HOP62 (line)]] | alt | 9.20 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -14.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0742× (z -14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0497× (z -13.2) |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.103× (z -8.8) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.131× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0717× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 22.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -12.2) |
| [[NCI-H23 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.202× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 9.28 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -10.2) |
| [[A549 (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.4) ⚠ cell-cycle shift, explains ~36% of this change |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.111× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.135× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -11.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0584× (z -12.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -14.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -14.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -10.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0883× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -9.6) |
| [[A-427 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2LI1]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RWDD3]] | +0.66 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[METTL14]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[USP30]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[C12orf76]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NSL1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[UBXN2B]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[ZNF112]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MBIP]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[CDC40]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CRYZL1]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.63 | -0.58 / -0.62 | both halves | 7e-06 |  |
| [[EGR3]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[UBASH3B]] | -0.57 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ACTN1]] | -0.57 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[MAMLD1]] | -0.57 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[NACC1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ABR]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | -0.56 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[E2F3]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[SCHIP1]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRP1]] | B | NRP1 activity lowers FPGT's level | lines that do not express NRP1 (16) vs lines expressing it (34) | 1.30× higher at baseline in the lines without NRP1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: BDKRB2, MX2, FAM107B |
| [[TOP2A]] | B | TOP2A activity raises FPGT's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K1]] | B | MAP2K1 activity lowers FPGT's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TNNI3K]] | C | TNNI3K activity raises FPGT's level | lines that do not express TNNI3K (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without TNNI3K | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: CORIN, CLEC2D, CFAP58; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.657). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-23.2, -3.4); signed map (-23.0, -11.9). **Vector** length 63.3, 12.0% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +8.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +3.6 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.3 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.4 | -6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | -2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | +0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -6.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Estrone sulfate (potassium) (drug)]] 5 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | fucose-1-phosphate guanylyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.1 — chr1:74,198,238-74,234,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GFPP |
| Reactome | 4 pathways, smallest: GDP-fucose biosynthesis; Synthesis of substrates in N-glycan biosythesis; Biosynthesis of the N-glycan precursor (dolichol lipid-linked oligosaccharide, LLO) and transfer to a nascent protein |
| Matched by | ensembl_id |

**Function**, from UniProt [O14772](https://www.uniprot.org/uniprotkb/O14772) (Fucose-1-phosphate guanylyltransferase):

> Catalyzes the formation of GDP-L-fucose from GTP and L-fucose-1-phosphate. Functions as a salvage pathway to reutilize L-fucose arising from the turnover of glycoproteins and glycolipids.

**Summary**, from NCBI Gene [8790](https://www.ncbi.nlm.nih.gov/gene/8790):

> L-fucose is a key sugar in glycoproteins and other complex carbohydrates since it may be involved in many of the functional roles of these macromolecules, such as in cell-cell recognition. The fucosyl donor for these fucosylated oligosaccharides is GDP-beta-L-fucose. There are two alternate pathways for the biosynthesis of GDP-fucose; the major pathway converts GDP-alpha-D-mannose to GDP-beta-L-fucose. The protein encoded by this gene participates in an alternate pathway that is present in …

**Accessions** — [HGNC:3825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3825) · Entrez [8790](https://www.ncbi.nlm.nih.gov/gene/8790) · UniProt [O14772](https://www.uniprot.org/uniprotkb/O14772) · Ensembl [ENSG00000254685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254685)

## Data

Gene col 14890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14890); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14890]; `tensor/DDL_lfc|DDL_z.npy` [14890]; `embed/gene_vectors.npy` [14890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14890 or target_col == 14890). Every well: [[FPGT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FPGT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
