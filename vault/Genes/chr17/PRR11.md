---
symbol: "PRR11"
type: "gene"
col: 893
ensembl_id: "ENSG00000068489"
name: "proline rich 11"
location: "17q22"
module: 22
arm: "+"
pooled_cpm: 83.05
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PRR11

*proline rich 11* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +12.4, q 1e-32, up in 42 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Sodium Salicylate (drug)]] 5 µM: 1.25× (z +3.7, q 0.011, up in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (A-172 5.35×, A498 3.76×, NCI-H460 4.33×, HS-578T 5.02×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 3.95×, A-172 5.20×, PANC-1 3.48×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 5.29×, NCI-H2347 3.49×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (17 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.430× (z -9.1, q 7e-17, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 0.472× (z -4.6, q 3e-04, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DLGAP5]] (+0.91, fdr 7e-06), [[TOP2A]] (+0.89, fdr 7e-06), [[NCAPD2]] (+0.89, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 893.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 10 lines (A-172 5.35×, A498 3.76×, NCI-H460 4.33×, HS-578T 5.02×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 3.95×, A-172 5.20×, PANC-1 3.48×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 5.29×, NCI-H2347 3.49×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.4 | 1e-32 | 42/43 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.38×** | +11.2 | 8e-27 | 47/47 (A498, A-172, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.02×** | +7.6 | 5e-12 | 36/44 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~90% of this change | **1.74×** | +6.5 | 1e-08 | 39/47 (HOP62, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.41×** | +5.7 | 1e-06 | 39/47 (NCI-H23, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.43×** | +4.2 | 0.002 | 27/47 (KATO III, C-33 A, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.41×** | +4.1 | 0.004 | 25/46 (HOP62, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.93×** | +4.0 | 0.004 | 28/46 (RKO, HS-578T, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.011 | 29/47 (PANC-1, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.23×** | +3.4 | 0.033 | 22/47 (RKO, HS-578T, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.4 | 0.034 | 23/47 (KATO III, A-172, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +3.1 | 0.099 | 20/47 (KATO III, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.430×** | -9.1 | 7e-17 | 43/47 (SW480, A-172, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.465×** | -8.9 | 2e-16 | 37/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.612×** | -8.0 | 2e-13 | 37/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.502×** | -8.0 | 2e-13 | 42/47 (LOX-IMVI, H4, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.584×** | -6.0 | 2e-07 | 40/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **0.404×** | -5.5 | 4e-06 | 31/44 (NCI-H460, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.571×** | -5.1 | 3e-05 | 29/47 (LOX-IMVI, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -5.0 | 4e-05 | 33/47 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.660×** | -4.8 | 1e-04 | 27/47 (LOX-IMVI, H4, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.472×** | -4.6 | 3e-04 | 33/47 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **0.756×** | -4.5 | 3e-04 | 30/47 (LOX-IMVI, A498, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.690×** | -4.3 | 9e-04 | 26/47 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.714×** | -3.9 | 0.005 | 28/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.663×** | -3.7 | 0.008 | 28/47 (NCI-H1573, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -3.7 | 0.008 | 23/47 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.727×** | -3.7 | 0.008 | 26/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.011 | 21/47 (H4, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -3.4 | 0.023 | 22/47 (SK-MEL-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.054 | 23/46 (A-427, A498, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.671×** | -3.0 | 0.067 | 17/47 (A549, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.760×** | -2.9 | 0.083 | 15/47 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.760×** | -2.9 | 0.083 | 19/47 (NCI-H1573, SW1417, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.839× | -2.8 | 0.098 | 17/47 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.783×** | -2.8 | 0.098 | 14/47 (J82, HOP62, …) | top dose only |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.841× | -2.8 | 0.098 | 19/47 (Hs 766T, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +1.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 141 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0651× (z -16.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.233× (z -12.2) |
| [[LOX-IMVI (line)]] | wt | 140 | 1 (1 ⚠) | 10 (6 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.1) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.165× (z -14.8) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.324× (z -13.1) |
| [[A-172 (line)]] | wt | 73.3 | 3 (3 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.35× (z +12.7) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.212× (z -12.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.435× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 57.3 | 2 (2 ⚠) | 6 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.33× (z +11.2) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.281× (z -10.0) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.466× (z -8.5) |
| [[A549 (line)]] | wt | 102 | 1 (1 ⚠) | 6 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.28× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.222× (z -12.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.349× (z -12.0) |
| [[A498 (line)]] | wt | 86.1 | 2 (2 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.76× (z +12.1) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.160× (z -24.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.376× (z -13.0) |
| [[C32 (line)]] | wt | 62.1 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.62× (z +9.5) ⚠ toxic; transcription drop | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.140× (z -12.6) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.294× (z -11.1) |
| [[HOP62 (line)]] | alt | 170 | 2 (2 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.49× (z +10.7) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.309× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 93.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.33× (z +10.3) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.220× (z -12.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.374× (z -8.7) |
| [[HS-578T (line)]] | alt | 75.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +11.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 96.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.49× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 72.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 153 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.214× (z -17.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.409× (z -9.9) |
| [[BT-474 (line)]] | alt | 236 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.205× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 116 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 81.2 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.326× (z -10.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.364× (z -9.1) |
| [[LS 180 (line)]] | wt | 32.9 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.180× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.337× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 84.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[PANC-1 (line)]] | alt | 65.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 134 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.233× (z -9.2) |
| [[Hs 766T (line)]] | wt | 49.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.16× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +9.1) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 40.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 96.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -8.7) |
| [[SW 1271 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.176× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 157 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLGAP5]] | +0.91 | +0.91 / +0.87 | both halves | 7e-06 |  |
| [[TOP2A]] | +0.89 | +0.91 / +0.86 | both halves | 7e-06 |  |
| [[NCAPD2]] | +0.89 | +0.91 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[TPX2]] | +0.89 | +0.90 / +0.87 | both halves | 7e-06 |  |
| [[TROAP]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 |  |
| [[KIF4A]] | +0.88 | +0.89 / +0.85 | both halves | 7e-06 |  |
| [[BIRC5]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 |  |
| [[KIF18A]] | +0.87 | +0.90 / +0.84 | both halves | 7e-06 |  |
| [[BUB1]] | +0.87 | +0.87 / +0.85 | both halves | 7e-06 |  |
| [[CDCA3]] | +0.87 | +0.85 / +0.85 | both halves | 7e-06 |  |
| [[PIF1]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[NEK2]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises PRR11's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.07× lower at baseline in the lines without PIMREG | 0.060 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises PRR11's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 2.22× lower at baseline in the lines without FAM72B | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B |
| [[PBK]] | C | PBK activity raises PRR11's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.03× lower at baseline in the lines without PBK | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises PRR11's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.42× lower at baseline in the lines without AURKB | 0.051 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises PRR11's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.894). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.4, -56.6); signed map (-50.3, -42.2). **Vector** length 154, 61.9% of its response variance represented; |z| ≥ 3 in 1,294 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.70 to 60); *DREAM G2/M down* (control, mean cos +0.81 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.68 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.4 | +3.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +3.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.7 | +3.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -9.3 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -8.6 | -8.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~50% of this change | -8.4 | -9.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -8.0 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~94% of this change | -7.5 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.5 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -5.8 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.0 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:59,155,732-59,206,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11029 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96HE9](https://www.uniprot.org/uniprotkb/Q96HE9) (Proline-rich protein 11):

> Plays a critical role in cell cycle progression.

**Summary**, from NCBI Gene [55771](https://www.ncbi.nlm.nih.gov/gene/55771):

> Involved in regulation of cell cycle. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25619) · Entrez [55771](https://www.ncbi.nlm.nih.gov/gene/55771) · UniProt [Q96HE9](https://www.uniprot.org/uniprotkb/Q96HE9) · Ensembl [ENSG00000068489](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068489)

## Data

Gene col 893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 893); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 893]; `tensor/DDL_lfc|DDL_z.npy` [893]; `embed/gene_vectors.npy` [893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 893 or target_col == 893). Every well: [[PRR11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
