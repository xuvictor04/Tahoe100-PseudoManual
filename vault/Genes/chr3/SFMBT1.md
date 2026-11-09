---
symbol: "SFMBT1"
type: "gene"
col: 8815
ensembl_id: "ENSG00000163935"
name: "Scm like with four mbt domains 1"
location: "3p21.1"
module: 18
arm: "+"
pooled_cpm: 67.64
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# SFMBT1

*Scm like with four mbt domains 1* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +11.8, q 4e-29, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.538× (z -15.4, q 0e+00, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.627× (z -12.1, q 2e-31, down in 34 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF11]] (+0.71, fdr 1e-05), [[JADE3]] (+0.63, fdr 1e-05), [[CHD7]] (+0.63, fdr 1e-05); moves opposite to [[RAB3A]] (-0.56, fdr 1e-04), [[PJA2]] (-0.52, fdr 5e-05), [[RARA]] (-0.51, fdr 5e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8815.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +11.8 | 4e-29 | 27/47 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +11.3 | 3e-27 | 33/46 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +10.5 | 2e-23 | 29/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +10.4 | 6e-23 | 35/45 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +10.1 | 8e-22 | 32/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +10.1 | 8e-22 | 36/45 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +9.4 | 4e-19 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +8.6 | 5e-16 | 32/46 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +7.2 | 5e-11 | 26/46 (PANC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +7.0 | 1e-10 | 29/46 (NCI-H460, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +6.2 | 3e-08 | 21/46 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.25×** | +5.7 | 6e-07 | 25/45 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +5.4 | 3e-06 | 20/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.3 | 6e-06 | 21/45 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.1 | 1e-05 | 22/42 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.3 | 5e-04 | 14/45 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 19/46 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.006 | 14/47 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.5 | 0.014 | 10/46 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8815.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.538×** | -15.4 | 0e+00 | 28/42 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -15.0 | 0e+00 | 33/45 (A-427, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.627×** | -12.1 | 2e-31 | 34/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.610×** | -11.8 | 4e-30 | 26/43 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.667×** | -10.5 | 1e-23 | 29/46 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.677×** | -10.1 | 6e-22 | 31/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -5.9 | 3e-07 | 19/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.810×** | -5.5 | 3e-06 | 21/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.825×** | -5.0 | 4e-05 | 22/45 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -4.0 | 0.004 | 17/46 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.761×** | -3.7 | 0.012 | 15/44 (LS 180, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.874× | -3.5 | 0.024 | 10/47 (AsPC-1, NCI-H2122, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.058 | 12/46 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.886× | -3.1 | 0.068 | 10/46 (HEC-1-A, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8815. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 91.6 | 6 (2 ⚠) | 8 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 4.12× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.388× (z -15.9) |
| [[SW480 (line)]] | alt | 119 | 5 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.360× (z -16.3) |
| [[KATO III (line)]] | alt | 98.1 | 2 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.96× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 2 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.91× (z +10.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.290× (z -11.5) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.331× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 44.5 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +24.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.60× (z +16.1) | — |
| [[A-427 (line)]] | wt | 101 | 1 | 6 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.05× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -12.4) |
| [[C-33 A (line)]] | alt | 120 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.332× (z -12.6) |
| [[SHP-77 (line)]] | alt | 66.5 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -12.0) |
| [[SNU-1 (line)]] | wt | 207 | 1 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.24× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0787× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.255× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.578× (z -9.1) |
| [[HT-29 (line)]] | alt | 85.7 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.348× (z -12.9) |
| [[J82 (line)]] | alt | 89.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.395× (z -12.8) |
| [[LoVo (line)]] | wt | 81.4 | 2 (1 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.52× (z +13.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.566× (z -8.8) |
| [[AN3 CA (line)]] | alt | 129 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 71.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.11× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.398× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 86.4 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.220× (z -17.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 79.3 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -13.4) |
| [[SW48 (line)]] | wt | 108 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 54.3 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.50× (z +13.7) | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 83.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 77.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.408× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -24.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 28.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 37.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 68.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -15.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 97.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -22.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0694× (z -20.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 23.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 37.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +11.8) | — |
| [[A-172 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8815), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF11]] | +0.71 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[JADE3]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CHD7]] | +0.63 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.62 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[FANCC]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PKN3]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[TCF12]] | +0.58 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[POU6F1]] | +0.58 | +0.52 / +0.34 | both halves | 1e-04 |  |
| [[GABPB1]] | +0.58 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[MEMO1]] | +0.57 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[ZNF346]] | +0.57 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[TCF20]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | -0.56 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[PJA2]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[RARA]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[HPS3]] | -0.51 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[MAP3K13]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[DAD1]] | -0.50 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[LRP1]] | -0.49 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SPAG9]] | -0.49 | -0.35 / -0.30 | both halves | 2e-04 |  |
| [[ACADSB]] | -0.49 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TBC1D23]] | -0.48 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[LTN1]] | -0.48 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[TBC1D10A]] | -0.47 | -0.41 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises SFMBT1's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.26× lower at baseline in the lines without MSI1 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[HDAC6]] | B | HDAC6 activity raises SFMBT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.469). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.9, 11.3); signed map (7.9, -3.0). **Vector** length 119, 32.7% of its response variance represented; |z| ≥ 3 in 1,215 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +11.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +5.7 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +4.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | -10.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -1.1 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | -1.8 | -2.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Scm like with four mbt domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,903,572-53,046,750 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RU1, DKFZp434L243, SFMBT |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MBT domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHJ3](https://www.uniprot.org/uniprotkb/Q9UHJ3) (Scm-like with four MBT domains protein 1):

> Histone-binding protein, which is part of various corepressor complexes. Mediates the recruitment of corepressor complexes to target genes, followed by chromatin compaction and repression of transcription. Plays a role during myogenesis: required for the maintenance of undifferentiated states of myogenic progenitor cells via interaction with MYOD1. Interaction with MYOD1 leads to the recruitment of associated corepressors and silencing of MYOD1 target genes. Part of the SLC complex in germ …

**Summary**, from NCBI Gene [51460](https://www.ncbi.nlm.nih.gov/gene/51460):

> This gene shares high similarity with the Drosophila Scm (sex comb on midleg) gene. It encodes a protein which contains four malignant brain tumor repeat (mbt) domains and may be involved in antigen recognition. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:20255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20255) · Entrez [51460](https://www.ncbi.nlm.nih.gov/gene/51460) · UniProt [Q9UHJ3](https://www.uniprot.org/uniprotkb/Q9UHJ3) · Ensembl [ENSG00000163935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163935)

## Data

Gene col 8815: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8815); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8815, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8815]; `tensor/DDL_lfc|DDL_z.npy` [8815]; `embed/gene_vectors.npy` [8815]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8815 or target_col == 8815). Every well: [[SFMBT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFMBT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
