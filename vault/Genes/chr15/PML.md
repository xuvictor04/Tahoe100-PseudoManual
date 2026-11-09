---
symbol: "PML"
type: "gene"
col: 6413
ensembl_id: "ENSG00000140464"
name: "PML nuclear body scaffold"
location: "15q24.1"
module: 32
arm: "+"
pooled_cpm: 64.42
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 33
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 84
direction_downstream: 27
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PML

*PML nuclear body scaffold* — 15q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.88× (z +5.9, q 2e-06, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.376× (z -17.0, q 0e+00, down in 31 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.466× (z -13.7, q 1e-40, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.86, fdr 7e-06), [[USP18]] (+0.85, fdr 7e-06), [[OAS1]] (+0.85, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[CD5L]] → it (grade B ⚠); 27 go from it, the strongest it → [[SAMHD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6413.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +5.9 | 2e-06 | 25/48 (RPMI-7951, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.2 | 7e-05 | 23/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.036 | 19/46 (RPMI-7951, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.16× | +3.6 | 0.048 | 15/47 (AsPC-1, CFPAC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.16× | +3.5 | 0.053 | 23/47 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.11 | 10/47 (SW48, SNU-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.2 | 0.11 | 22/47 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[venetoclax (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.11 | 14/47 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.11 | 8/47 (HS-578T, CFPAC-1, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.18× | +3.1 | 0.11 | 11/47 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.11 | 10/46 (PANC-1, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.11 | 18/46 (AsPC-1, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6413.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.376×** | -17.0 | 0e+00 | 31/39 (A498, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.419×** | -15.7 | 0e+00 | 38/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.466×** | -13.7 | 1e-40 | 41/47 (LoVo, SNU-423, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.553×** | -13.6 | 3e-40 | 33/47 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.540×** | -11.1 | 1e-26 | 37/48 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.524×** | -10.6 | 4e-24 | 34/47 (SNU-423, A498, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.625×** | -10.3 | 6e-23 | 32/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.589×** | -8.7 | 3e-16 | 32/48 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.725×** | -7.4 | 7e-12 | 29/46 (RKO, A549, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.652×** | -7.4 | 7e-12 | 25/46 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.642×** | -7.4 | 8e-12 | 28/42 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.662×** | -7.0 | 1e-10 | 30/47 (MIA PaCa-2, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.480×** | -6.9 | 2e-10 | 28/46 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.734×** | -6.7 | 6e-10 | 30/47 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -6.6 | 2e-09 | 27/47 (HS-578T, COLO 205, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.510×** | -6.3 | 8e-09 | 26/46 (RPMI-7951, SNU-423, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.703×** | -5.8 | 3e-07 | 30/47 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.776×** | -4.3 | 5e-04 | 24/46 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.838× | -4.2 | 7e-04 | 21/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.796×** | -4.1 | 0.001 | 21/47 (RPMI-7951, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6413. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 146 | 2 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +11.6) | [[Tofacitinib (drug)]] 5 µM 0.329× (z -13.2) |
| [[A498 (line)]] | wt | 187 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.339× (z -14.1) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0489× (z -24.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.188× (z -13.7) |
| [[A-172 (line)]] | wt | 127 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.32× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.454× (z -10.4) |
| [[A549 (line)]] | wt | 70.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.370× (z -11.1) |
| [[HS-578T (line)]] | alt | 77.2 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.68× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.233× (z -13.4) |
| [[LoVo (line)]] | wt | 102 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.148× (z -16.1) |
| [[NCI-H2347 (line)]] | alt | 102 | 2 (1 ⚠) | 5 (4 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.38× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -9.6) |
| [[SNU-423 (line)]] | alt | 102 | 0 | 7 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.196× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 0 | 6 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.199× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 126 | 1 (1 ⚠) | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 2.39× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.485× (z -10.1) |
| [[RKO (line)]] | wt | 75.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -21.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.334× (z -10.4) |
| [[BT-474 (line)]] | alt | 42.1 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0620× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.220× (z -9.1) |
| [[Hs 766T (line)]] | wt | 64.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 0.5 µM 0.301× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 45.9 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.389× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 97.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.8) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.383× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.266× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 82.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.368× (z -8.8) |
| [[C-33 A (line)]] | alt | 50.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -12.6) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 25.3 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +18.1) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[PANC-1 (line)]] | alt | 31.4 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.56× (z +9.9) | — |
| [[KATO III (line)]] | alt | 46.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.433× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 45.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +8.7) ⚠ cell-cycle shift, explains ~22% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 102 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.325× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 74.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.396× (z -9.8) |
| [[SW 900 (line)]] | alt | 56.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.285× (z -9.9) |
| [[SW1417 (line)]] | alt | 60.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -15.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 60.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.272× (z -8.5) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0782× (z -14.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 29.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +14.7) ⚠ cell-cycle shift, explains ~22% of this change | — |
| [[A-427 (line)]] | wt | 15.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6413), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.86 | +0.79 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[USP18]] | +0.85 | +0.77 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OAS1]] | +0.85 | +0.80 / +0.88 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[UBE2L6]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OAS3]] | +0.84 | +0.80 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OAS2]] | +0.83 | +0.75 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 411 |
| [[PARP9]] | +0.83 | +0.75 / +0.88 | both halves | 7e-06 |  |
| [[MX1]] | +0.83 | +0.74 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 544 |
| [[TRIM22]] | +0.82 | +0.75 / +0.88 | both halves | 7e-06 | same gene group; pathway: Interferon Signaling; STRING 712 |
| [[IFI35]] | +0.82 | +0.74 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 408 |
| [[IFI6]] | +0.82 | +0.71 / +0.85 | both halves | 7e-06 | pathway: Interferon Signaling |
| [[IFIT1]] | +0.81 | +0.73 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 60, C 24. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD5L]] | B | CD5L activity raises PML's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without CD5L | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[MX1]] | B | MX1 activity raises PML's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without MX1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[OAS2]] | B | OAS2 activity raises PML's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.21× lower at baseline in the lines without OAS2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[TRIM22]] | B | TRIM22 activity raises PML's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.12× lower at baseline in the lines without TRIM22 | 0.001 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[OAS2]] | B | OAS2 activity strengthens PML's drug response | lines that do not express OAS2 (13) vs lines expressing it (35) | the lines without OAS2 respond 0.30× as strongly (z diff +2.95); strongest at Auranofin 5 µM: 0.73x vs 0.38x (z diff +5.4) | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity raises PML's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.17× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises PML's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.94× lower at baseline in the lines without SAMD9L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[RASGRP3]] | B | RASGRP3 activity raises PML's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RASGRP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises PML's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.91× lower at baseline in the lines without OAS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SLC15A3]] | B | SLC15A3 activity raises PML's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 2.06× lower at baseline in the lines without SLC15A3 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[GBP4]] | B | GBP4 activity raises PML's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without GBP4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[SAMD9]] | B | SAMD9 activity raises PML's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without SAMD9 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMHD1]] | C | PML's natural level strengthens SAMHD1's drug response | PML's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.63; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | PML's natural level strengthens PARP10's drug response | PML's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.64; direction not clear | 3e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | PML's natural level strengthens USP18's drug response | PML's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.63; direction not clear | 6e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | PML's natural level strengthens IRF9's drug response | PML's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.70; direction not clear | 0.001 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | PML's natural level strengthens CMTR1's drug response | PML's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.57; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PSMB9]] | C | PML's natural level strengthens PSMB9's drug response | PML's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.37; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[PARP12]] | C | PML's natural level strengthens PARP12's drug response | PML's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.75; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | PML's natural level strengthens TDRD7's drug response | PML's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.65; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | PML's natural level strengthens IFIT1's drug response | PML's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.46; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | PML's natural level strengthens IFIT5's drug response | PML's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OASL]] | C | PML's natural level strengthens OASL's drug response | PML's natural level across 39 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.06; direction clear | 0.007 | ⚠ tissue can mimic it; precision caveat |
| [[HELZ2]] | C | PML's natural level strengthens HELZ2's drug response | PML's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.86; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.855). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.8, 54.3); signed map (66.2, 32.5). **Vector** length 149, 50.1% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.73 to 56); *interferon* (control, mean cos +0.78 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.77 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.9 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.4 | +3.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.1 | +1.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.0 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.3 | -13.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.7 | -10.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.6 | -10.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.6 | -11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -13.7 |

## What is on record

|  |  |
|---|---|
| Name | PML nuclear body scaffold |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q24.1 — chr15:73,994,673-74,047,827 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYL, TRIM19, RNF71 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | HEDGEHOG_SIGNALING, INTERFERON_GAMMA_RESPONSE, G2M_CHECKPOINT |
| Reactome | 23 pathways, smallest: Regulation of PTEN localization; Regulation of RUNX1 Expression and Activity; Dengue virus activates/modulates innate and adaptive immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [P29590](https://www.uniprot.org/uniprotkb/P29590) (Protein PML):

> Functions via its association with PML-nuclear bodies (PML-NBs) in a wide range of important cellular processes, including tumor suppression, transcriptional regulation, apoptosis, senescence, DNA damage response, and viral defense mechanisms. Acts as the scaffold of PML-NBs allowing other proteins to shuttle in and out, a process which is regulated by SUMO-mediated modifications and interactions. Inhibits EIF4E-mediated mRNA nuclear export by reducing EIF4E affinity for the 5' …

**Summary**, from NCBI Gene [5371](https://www.ncbi.nlm.nih.gov/gene/5371):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. This phosphoprotein localizes to nuclear bodies where it functions as a transcription factor and tumor suppressor. Its expression is cell-cycle related and it regulates the p53 response to oncogenic signals. The gene is often involved in the translocation with the retinoic acid receptor alpha …

**Accessions** — [HGNC:9113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9113) · Entrez [5371](https://www.ncbi.nlm.nih.gov/gene/5371) · UniProt [P29590](https://www.uniprot.org/uniprotkb/P29590) · Ensembl [ENSG00000140464](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140464)

## Data

Gene col 6413: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6413); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6413, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6413]; `tensor/DDL_lfc|DDL_z.npy` [6413]; `embed/gene_vectors.npy` [6413]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6413 or target_col == 6413). Every well: [[PML — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PML.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
