---
symbol: "KIZ"
type: "gene"
col: 1555
ensembl_id: "ENSG00000088970"
name: "kizuna centrosomal protein"
location: "20p11.23"
module: 76
arm: "+"
pooled_cpm: 107.69
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 38
n_dd_up_clean: 5
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# KIZ

*kizuna centrosomal protein* — 20p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.25× (z +6.4, q 9e-08, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.408× (z -18.4, q 0e+00, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.584× (z -11.0, q 1e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SARAF]] (+0.70, fdr 7e-06), [[ELP2]] (+0.70, fdr 7e-06), [[IFT20]] (+0.70, fdr 7e-06); moves opposite to [[ADAT1]] (-0.62, fdr 1e-05), [[EIF4G1]] (-0.58, fdr 1e-05), [[PSME3]] (-0.55, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.4 | 9e-08 | 29/48 (SW1417, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.29×** | +5.0 | 2e-04 | 25/50 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.9 | 2e-04 | 26/48 (HOP62, J82, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.9 | 0.013 | 17/48 (A-427, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.20× | +3.8 | 0.020 | 22/49 (NCI-H2347, C32, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.21×** | +3.7 | 0.020 | 15/49 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.7 | 0.020 | 13/49 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.028 | 16/50 (LoVo, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.5 | 0.034 | 11/49 (SW480, SW48, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.062 | 13/48 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 1.12× | +3.2 | 0.075 | 10/48 (RKO, NCI-H1573, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.10 | 13/47 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.11 | 17/48 (SK-MEL-2, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.408×** | -18.4 | 0e+00 | 46/48 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.584×** | -11.0 | 1e-25 | 41/48 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.567×** | -10.7 | 1e-24 | 34/45 (RKO, SW480, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.580×** | -10.7 | 1e-24 | 41/48 (A498, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.596×** | -10.6 | 5e-24 | 31/49 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.691×** | -10.4 | 4e-23 | 33/48 (HepG2/C3A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -9.5 | 2e-19 | 32/49 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.629×** | -9.5 | 2e-19 | 35/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.432×** | -9.0 | 2e-17 | 44/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -8.9 | 4e-17 | 38/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.438×** | -8.8 | 5e-17 | 41/48 (LOX-IMVI, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.455×** | -8.4 | 2e-15 | 43/48 (RPMI-7951, SW 1271, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.468×** | -8.1 | 2e-14 | 40/48 (SNU-1, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.764×** | -7.7 | 8e-13 | 33/48 (SW480, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.489×** | -7.6 | 8e-13 | 35/48 (RPMI-7951, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.665×** | -7.5 | 2e-12 | 34/48 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.554×** | -6.3 | 8e-09 | 32/47 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.566×** | -6.1 | 3e-08 | 28/48 (A549, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.725×** | -6.1 | 3e-08 | 33/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.788×** | -4.7 | 7e-05 | 27/48 (HS-578T, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 535 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -22.9) |
| [[A498 (line)]] | wt | 106 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -20.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.278× (z -17.5) |
| [[HepG2_C3A (line)]] | wt | 337 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -22.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -15.7) |
| [[HOP62 (line)]] | alt | 153 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.299× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.565× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.409× (z -12.4) |
| [[HCT15 (line)]] | alt | 166 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -11.7) |
| [[LoVo (line)]] | wt | 177 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -18.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -10.2) |
| [[HS-578T (line)]] | alt | 90.4 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -17.4) |
| [[NCI-H460 (line)]] | wt | 66.7 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.389× (z -12.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -10.6) |
| [[SNU-423 (line)]] | alt | 89.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.370× (z -10.9) |
| [[HT-29 (line)]] | alt | 105 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.213× (z -13.5) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -8.5) |
| [[LS 180 (line)]] | wt | 145 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -16.2) |
| [[SNU-1 (line)]] | wt | 114 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.332× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 83.4 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -10.0) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.359× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 141 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -15.1) |
| [[PANC-1 (line)]] | alt | 45.0 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.331× (z -12.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.458× (z -8.9) |
| [[SW48 (line)]] | wt | 149 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -12.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -8.7) |
| [[A-172 (line)]] | wt | 54.0 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -11.6) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.405× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 57.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.170× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 88.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.464× (z -10.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[RKO (line)]] | wt | 94.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 67.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.408× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.320× (z -9.7) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 36.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.6) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[C-33 A (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.328× (z -9.0) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 41.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[COLO 205 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[HEC-1-A (line)]] | alt | 62.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.361× (z -9.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 53.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -11.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 84.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -10.4) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.146× (z -8.6) ⚠ toxic |
| [[SW1417 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.4) |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARAF]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[ELP2]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[IFT20]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[KIZ-AS1]] ⚠ | +0.68 | +0.64 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation); ⚠ in the vector space only through flagged drug-doses |
| [[AUH]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.63 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.62 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MCEE]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.62 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[SLC17A5]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[HACL1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[COG6]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT1]] | -0.62 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PSME3]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.55 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[UBE2N]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PURB]] | -0.55 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[E2F3]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[DHX37]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZC3H4]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[KRT8P12]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[PRORP]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PIGW]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.635). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.1, -45.9); signed map (-46.3, 14.4). **Vector** length 121, 37.7% of its response variance represented; |z| ≥ 3 in 1,519 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.9 | +2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.2 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.6 | -18.4 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -8.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.5 | -8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -7.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.2 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -9.0 |

## What is on record

|  |  |
|---|---|
| Name | kizuna centrosomal protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.23 — chr20:21,125,983-21,246,622 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT013; previously NCRNA00153, C20orf19, PLK1S1 |
| Gene groups (HGNC) | Centriolar satellite proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M2Z5](https://www.uniprot.org/uniprotkb/Q2M2Z5) (Centrosomal protein kizuna):

> Centrosomal protein required for establishing a robust mitotic centrosome architecture that can endure the forces that converge on the centrosomes during spindle formation. Required for stabilizing the expanded pericentriolar material around the centriole.

**Summary**, from NCBI Gene [55857](https://www.ncbi.nlm.nih.gov/gene/55857):

> The protein encoded by this gene localizes to centrosomes, strengthening and stabilizing the pericentriolar region prior to spindle formation. The encoded protein usually remains with the mother centrosome after centrosomal duplication. Sevral transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:15865](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15865) · Entrez [55857](https://www.ncbi.nlm.nih.gov/gene/55857) · UniProt [Q2M2Z5](https://www.uniprot.org/uniprotkb/Q2M2Z5) · Ensembl [ENSG00000088970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088970)

## Data

Gene col 1555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1555); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1555]; `tensor/DDL_lfc|DDL_z.npy` [1555]; `embed/gene_vectors.npy` [1555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1555 or target_col == 1555). Every well: [[KIZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
