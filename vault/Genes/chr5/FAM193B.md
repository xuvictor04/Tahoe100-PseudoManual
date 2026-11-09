---
symbol: "FAM193B"
type: "gene"
col: 7059
ensembl_id: "ENSG00000146067"
name: "family with sequence similarity 193 member B"
location: "5q35.3"
module: 3
arm: "+"
pooled_cpm: 79.44
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FAM193B

*family with sequence similarity 193 member B* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.46× (z +8.2, q 1e-13, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.397× (z -19.2, q 0e+00, down in 40 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.633× (z -14.0, q 5e-42, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MALSU1]] (+0.75, fdr 7e-06), [[RAB40C]] (+0.74, fdr 7e-06), [[CRYZL1]] (+0.72, fdr 7e-06); moves opposite to [[KRT8P12]] (-0.67, fdr 7e-06), [[TRIP12]] (-0.64, fdr 1e-05), [[PSME3]] (-0.63, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SMIM3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +8.2 | 1e-13 | 33/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.5 | 2e-11 | 32/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.77×** | +6.5 | 2e-08 | 37/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 1e-06 | 30/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.2 | 0.002 | 22/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +3.9 | 0.010 | 21/47 (RPMI-7951, A-172, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.017 | 23/49 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.027 | 9/48 (LOX-IMVI, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.12× | +3.4 | 0.044 | 4/48 (A498, CHP-212, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.060 | 15/48 (HS-578T, SNU-423, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.1 | 0.090 | 12/47 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.10× | +3.1 | 0.10 | 1/48 (C-33 A) | top dose only |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.10 | 8/48 (NCI-H2030, Panc 03.27, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7059.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.397×** | -19.2 | 0e+00 | 40/43 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.426×** | -18.4 | 0e+00 | 45/49 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.633×** | -14.0 | 5e-42 | 42/49 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.536×** | -12.4 | 2e-33 | 39/45 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.718×** | -7.1 | 1e-10 | 36/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.730×** | -6.8 | 1e-09 | 36/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.733×** | -6.7 | 2e-09 | 31/48 (A-172, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.731×** | -6.5 | 7e-09 | 29/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -6.0 | 1e-07 | 31/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.758×** | -6.0 | 1e-07 | 32/48 (SW 1271, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.765×** | -5.8 | 4e-07 | 31/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.771×** | -5.4 | 3e-06 | 31/50 (SK-MEL-2, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.774×** | -5.3 | 5e-06 | 27/48 (hTERT-HPNE, H4, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.791×** | -5.1 | 2e-05 | 25/48 (C32, A-172, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.796×** | -4.9 | 3e-05 | 25/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.793×** | -4.8 | 5e-05 | 27/48 (HS-578T, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.859× | -4.6 | 1e-04 | 18/48 (A-172, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.817×** | -4.3 | 4e-04 | 23/48 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.772×** | -4.0 | 0.002 | 23/47 (A-427, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.837× | -3.8 | 0.003 | 18/49 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.842× | -3.7 | 0.005 | 19/49 (HT-29, A-172, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 0.05 µM |  | **0.832×** | -3.6 | 0.005 | 22/48 (SW 1271, SW48, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.724×** | -3.6 | 0.005 | 15/48 (NCI-H2347, C32, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -3.6 | 0.007 | 17/48 (NCI-H2347, A-172, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 150 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -22.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -19.7) |
| [[HS-578T (line)]] | alt | 144 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.3) |
| [[C32 (line)]] | wt | 61.3 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 100 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 95.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.500× (z -10.0) |
| [[SW 900 (line)]] | alt | 169 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -12.9) |
| [[HOP62 (line)]] | alt | 81.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -10.1) |
| [[SNU-423 (line)]] | alt | 98.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -15.9) |
| [[A498 (line)]] | wt | 69.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 64.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -14.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 63.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 90.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -9.6) |
| [[BT-474 (line)]] | alt | 67.2 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.2) | — |
| [[LoVo (line)]] | wt | 79.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 71.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.102× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 70.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -12.4) |
| [[PANC-1 (line)]] | alt | 66.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 88.2 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -23.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -10.8) |
| [[A549 (line)]] | wt | 79.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 91.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -25.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 71.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.317× (z -10.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 62.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 70.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 65.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -22.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 70.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 72.1 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.7) | — |
| [[A-427 (line)]] | wt | 81.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -10.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -11.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HT-29 (line)]] | alt | 57.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.288× (z -11.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 60.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.0) |
| [[LS 180 (line)]] | wt | 62.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +8.8) | — |
| [[RKO (line)]] | wt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -13.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 56.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0640× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.105× (z -11.3) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.477× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 68.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALSU1]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.74 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[CRYZL1]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[COG7]] | +0.69 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[MZT2B]] | +0.69 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[CCZ1B]] | +0.68 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[SDHAP2]] | +0.68 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ARSK]] | +0.67 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[TULP3]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[GTF2H2B]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRT8P12]] | -0.67 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TRIP12]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[PSME3]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.63 | -0.61 / -0.59 | both halves | 7e-06 |  |
| [[WDR1]] | -0.63 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[ACTR3]] | -0.63 | -0.33 / -0.66 | both halves | 1e-04 |  |
| [[HNRNPK]] | -0.63 | -0.63 / -0.63 | both halves | 7e-06 |  |
| [[CCT7]] | -0.62 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.61 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[PTPN11]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.60 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[ADAT1]] | -0.60 | -0.68 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMIM3]] | B | SMIM3 activity raises FAM193B's level | lines that do not express SMIM3 (11) vs lines expressing it (39) | 1.23× lower at baseline in the lines without SMIM3 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SNHG18]] | B | SNHG18 activity raises FAM193B's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.22× lower at baseline in the lines without SNHG18 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.6, -13.8); signed map (-29.0, 11.7). **Vector** length 112, 33.3% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.0 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +1.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.6 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.5 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -6.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.4 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 193 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,519,789-177,554,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1931, FLJ10404, IRIZIO |
| Matched by | ensembl_id |

UniProt [Q96PV7](https://www.uniprot.org/uniprotkb/Q96PV7) carries no function annotation.

**Summary**, from NCBI Gene [54540](https://www.ncbi.nlm.nih.gov/gene/54540):

> Located in cytoplasm; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25524) · Entrez [54540](https://www.ncbi.nlm.nih.gov/gene/54540) · UniProt [Q96PV7](https://www.uniprot.org/uniprotkb/Q96PV7) · Ensembl [ENSG00000146067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146067)

## Data

Gene col 7059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7059); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7059]; `tensor/DDL_lfc|DDL_z.npy` [7059]; `embed/gene_vectors.npy` [7059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7059 or target_col == 7059). Every well: [[FAM193B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM193B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
