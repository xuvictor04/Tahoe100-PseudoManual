---
symbol: "KIF20A"
type: "gene"
col: 3423
ensembl_id: "ENSG00000112984"
name: "kinesin family member 20A"
location: "5q31.2"
module: 22
arm: "+"
pooled_cpm: 21.65
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 37
n_dd_up_clean: 4
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# KIF20A

*kinesin family member 20A* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (13 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 2.13× (z +8.4, q 2e-14, up in 36 of 45 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~80% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 2.73× (z +5.8, q 6e-07, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.352× (z -10.9, q 9e-25, down in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.414× (z -9.7, q 5e-20, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB2]] (+0.93, fdr 7e-06), [[NEK2]] (+0.93, fdr 7e-06), [[CCNB1]] (+0.92, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 13 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | **2.13×** | +8.4 | 2e-14 | 36/45 (HOP62, PANC-1, …) | all doses, flat | low cells (technical?); position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **3.54×** | +7.3 | 6e-11 | 33/45 (PANC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.54×** | +6.8 | 3e-09 | 36/47 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +6.3 | 5e-08 | 25/46 (Panc 03.27, SW1417, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.73×** | +5.8 | 6e-07 | 24/46 (HEC-1-A, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.65×** | +5.7 | 1e-06 | 26/47 (A-427, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.58×** | +5.1 | 3e-05 | 22/46 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.57×** | +5.1 | 3e-05 | 23/47 (NCI-H23, SW480, …) | all doses, flat | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.38×** | +5.0 | 5e-05 | 21/47 (PANC-1, HT-29, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +4.9 | 6e-05 | 23/47 (KATO III, SW1417, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.52×** | +4.7 | 1e-04 | 19/46 (KATO III, C-33 A, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.45×** | +4.2 | 0.001 | 21/47 (PANC-1, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.48×** | +4.0 | 0.002 | 12/35 (A-172, LoVo, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +3.7 | 0.009 | 16/46 (KATO III, NCI-H23, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.38×** | +3.6 | 0.010 | 21/46 (KATO III, SW1417, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.069 | 10/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.089 | 12/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.352×** | -10.9 | 9e-25 | 36/47 (A-172, PANC-1, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.397×** | -10.2 | 9e-22 | 35/46 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.414×** | -9.7 | 5e-20 | 36/46 (C32, AN3 CA, …) | top dose only | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.434×** | -8.8 | 1e-16 | 41/46 (NCI-H1573, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.461×** | -8.5 | 2e-15 | 38/46 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.474×** | -8.2 | 2e-14 | 33/47 (A-427, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.487×** | -7.9 | 2e-13 | 41/47 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.509×** | -7.4 | 9e-12 | 25/46 (H4, LOX-IMVI, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.621×** | -7.3 | 1e-11 | 28/47 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.629×** | -7.0 | 1e-10 | 27/47 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.534×** | -6.6 | 2e-09 | 31/46 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.590×** | -5.8 | 4e-07 | 28/46 (NCI-H2030, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.581×** | -5.5 | 2e-06 | 26/46 (PANC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.386×** | -5.5 | 2e-06 | 23/46 (HEC-1-A, BT-474, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.689×** | -5.4 | 2e-06 | 26/47 (HOP62, SW480, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.605×** | -5.1 | 1e-05 | 25/46 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.420×** | -5.0 | 2e-05 | 27/45 (MIA PaCa-2, Panc 03.27, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.649×** | -4.7 | 7e-05 | 22/47 (HEC-1-A, HS-578T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.002 | 15/47 (MIA PaCa-2, NCI-H1792, …) | top dose only | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.711×** | -3.7 | 0.005 | 16/46 (HepG2/C3A, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.008 | 17/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | **0.729×** | -3.4 | 0.013 | 20/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.737×** | -3.3 | 0.020 | 8/47 (A-427, SW 1088, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.3 | 0.020 | 22/47 (C32, HOP62, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.811×** | -3.3 | 0.021 | 21/47 (A-427, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +1.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 7 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -9.8) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.227× (z -9.5) |
| [[A498 (line)]] | wt | 15.9 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.114× (z -16.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.278× (z -10.0) |
| [[A-427 (line)]] | wt | 45.7 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.204× (z -14.3) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 61.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0680× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0916× (z -10.1) |
| [[H4 (line)]] | wt | 34.5 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0458× (z -11.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.177× (z -9.2) |
| [[SW480 (line)]] | alt | 22.4 | 0 | 3 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.200× (z -10.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.0) |
| [[C32 (line)]] | wt | 16.4 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0727× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 38.8 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -12.4) ⚠ cell-cycle shift, explains ~51% of this change |
| [[KATO III (line)]] | alt | 7.59 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 13.3× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 12.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.151× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 47.2 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 5 µM 0.396× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.190× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 33.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.188× (z -9.2) |
| [[A-172 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0729× (z -12.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 25.2 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 5.27× (z +10.1) ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0632× (z -10.3) |
| [[HS-578T (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.100× (z -11.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 6.71 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0816× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.197× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.48× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.147× (z -11.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 43.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -9.6) |
| [[SW1417 (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 17.1 | 0 | 1 | — | [[Amsacrine (drug)]] 0.5 µM 0.0299× (z -12.9) |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB2]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | STRING 938 |
| [[NEK2]] | +0.93 | +0.92 / +0.93 | both halves | 7e-06 | STRING 948 |
| [[CCNB1]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | STRING 954 |
| [[CCNA2]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 974 |
| [[PLK1]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: Mitotic Telophase/Cytokinesis; STRING 990 |
| [[DLGAP5]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | STRING 970 |
| [[BUB1]] | +0.89 | +0.88 / +0.88 | both halves | 7e-06 | STRING 959 |
| [[TOP2A]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 974 |
| [[TROAP]] | +0.88 | +0.87 / +0.89 | both halves | 7e-06 | STRING 831 |
| [[PIF1]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[PSRC1]] | +0.88 | +0.90 / +0.88 | both halves | 7e-06 | STRING 505 |
| [[CKAP2]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 861 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises KIF20A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises KIF20A's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without NEURL1B | 0.035 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[TOP2A]] | B | TOP2A activity raises KIF20A's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AURKB]] | C | AURKB activity raises KIF20A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.25× lower at baseline in the lines without AURKB | 0.016 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises KIF20A's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.20× lower at baseline in the lines without PBK | 0.019 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises KIF20A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[CDCA3]] | C | CDCA3 activity raises KIF20A's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.23× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[SAPCD2]] | C | SAPCD2 activity raises KIF20A's level | lines that do not express SAPCD2 (3) vs lines expressing it (47) | 2.58× lower at baseline in the lines without SAPCD2 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[ACBD7]] | C | ACBD7 activity raises KIF20A's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without ACBD7 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.893). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -57.5); signed map (-51.3, -42.7). **Vector** length 151, 50.0% of its response variance represented; |z| ≥ 3 in 1,453 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.73 to 60); *Mitotic Prometaphase* (reactome, mean cos +0.67 to 48); *E2F targets* (hallmark, mean cos +0.70 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~80% of this change | +8.5 | +8.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +6.6 | +7.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.8 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +6.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +0.1 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.6 | +2.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -8.9 | -10.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | -8.3 | -10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -9.7 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -6.6 | -8.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~85% of this change | -6.5 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.9 | -4.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.9 | -7.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -4.8 | -5.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -4.6 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 20A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:138,178,719-138,187,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MKLP2; previously RAB6KIFL |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, GLYCOLYSIS |
| Reactome | 17 pathways, smallest: Mitotic Telophase/Cytokinesis; Kinesins; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [O95235](https://www.uniprot.org/uniprotkb/O95235) (Kinesin-like protein KIF20A):

> Mitotic kinesin required for chromosome passenger complex (CPC)-mediated cytokinesis. Following phosphorylation by PLK1, involved in recruitment of PLK1 to the central spindle. Interacts with guanosine triphosphate (GTP)-bound forms of RAB6A and RAB6B. May act as a motor required for the retrograde RAB6 regulated transport of Golgi membranes and associated vesicles along microtubules. Has a microtubule plus end-directed motility.

**Summary**, from NCBI Gene [10112](https://www.ncbi.nlm.nih.gov/gene/10112):

> Enables protein kinase binding activity. Involved in microtubule bundle formation; midbody abscission; and regulation of cytokinesis. Located in midbody and mitotic spindle. Implicated in familial restrictive cardiomyopathy 6. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:9787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9787) · Entrez [10112](https://www.ncbi.nlm.nih.gov/gene/10112) · UniProt [O95235](https://www.uniprot.org/uniprotkb/O95235) · Ensembl [ENSG00000112984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112984)

## Data

Gene col 3423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3423); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3423]; `tensor/DDL_lfc|DDL_z.npy` [3423]; `embed/gene_vectors.npy` [3423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3423 or target_col == 3423). Every well: [[KIF20A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF20A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
