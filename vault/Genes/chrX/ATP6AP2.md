---
symbol: "ATP6AP2"
type: "gene"
col: 11261
ensembl_id: "ENSG00000182220"
name: "ATPase H+ transporting accessory protein 2"
location: "Xp11.4"
module: 42
arm: "+"
pooled_cpm: 65.15
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ATP6AP2

*ATPase H+ transporting accessory protein 2* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +17.2, q 0e+00, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +14.7, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.632× (z -11.0, q 2e-25, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED4]] (+0.72, fdr 7e-06), [[PDIA6]] (+0.71, fdr 7e-06), [[TMED10]] (+0.70, fdr 7e-06); moves opposite to [[ZNF480]] (-0.64, fdr 1e-05), [[NSRP1]] (-0.64, fdr 7e-06), [[TRIM47]] (-0.63, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11261.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.78×** | +17.2 | 0e+00 | 45/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +15.4 | 0e+00 | 41/41 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +14.7 | 0e+00 | 45/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +12.3 | 2e-32 | 44/45 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +11.7 | 1e-29 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.90×** | +10.8 | 4e-25 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.76×** | +9.5 | 1e-19 | 46/48 (SW480, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +9.2 | 2e-18 | 42/50 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +6.7 | 1e-09 | 39/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.4 | 1e-08 | 44/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.40×** | +5.7 | 8e-07 | 36/47 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.31×** | +4.5 | 3e-04 | 28/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +4.4 | 5e-04 | 26/48 (C-33 A, SK-MEL-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.006 | 26/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.007 | 22/37 (HOP62, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.0 | 0.077 | 16/49 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.632×** | -11.0 | 2e-25 | 40/48 (RPMI-7951, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.682×** | -6.2 | 1e-07 | 34/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -5.8 | 1e-06 | 30/48 (H4, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.778×** | -4.3 | 0.003 | 26/48 (NCI-H2347, SW 1088, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.812×** | -3.5 | 0.046 | 21/48 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **0.819×** | -3.4 | 0.067 | 20/48 (SNU-1, SHP-77, …) | inconsistent across doses |  |
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.17 | 16/48 (NCI-H1573, A498, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 67.7 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +15.5) | — |
| [[A-172 (line)]] | wt | 89.5 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 47.2 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 144 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 63.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 66.0 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -11.1) |
| [[KATO III (line)]] | alt | 106 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.89× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.22× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -10.1) |
| [[HS-578T (line)]] | alt | 89.4 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.00× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.2) |
| [[H4 (line)]] | wt | 95.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 46.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.6) | — |
| [[J82 (line)]] | alt | 109 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 32.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 55.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 72.9 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.594× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 60.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 51.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +12.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 143 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -16.4) |
| [[SW1417 (line)]] | alt | 82.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.0) | — |
| [[A498 (line)]] | wt | 68.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.6) | — |
| [[A549 (line)]] | wt | 77.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.6) | — |
| [[C32 (line)]] | wt | 80.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 47.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.06× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 60.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 43.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 69.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.627× (z -8.6) |
| [[SNU-1 (line)]] | wt | 43.5 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.123× (z -9.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.1) |
| [[SW48 (line)]] | wt | 39.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.4) |
| [[BT-474 (line)]] | alt | 65.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.55× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 39.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 50.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.9) | — |
| [[RKO (line)]] | wt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.53× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.05× (z +9.3) | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0761× (z -10.2) |
| [[A-427 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED4]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.71 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TMED10]] | +0.70 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[FUCA1]] | +0.69 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[LAPTM4A]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DDOST]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NDUFV1]] | +0.67 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[SUMF2]] | +0.67 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[MLEC]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PDIA3]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[GINM1]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF480]] | -0.64 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[TRIM47]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[RTL6]] | -0.62 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[NEPRO-AS1]] | -0.61 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.61 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[CCDC137]] | -0.61 | -0.58 / -0.61 | both halves | 7e-06 |  |
| [[ZNF620]] | -0.61 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RPL7L1]] | -0.61 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[SURF6]] | -0.61 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[KCNMB3]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[ERCC4]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP6AP2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.9, -18.6); signed map (-50.8, -6.5). **Vector** length 114, 35.7% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +4.8 | +6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +14.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +11.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.9 | -0.4 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +1.9 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.4 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.0 | -11.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.8 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | +0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting accessory protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:40,579,372-40,606,848 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRR, M8-9, RENR, (P)RR, APT6M8-9, ATP6M8-9; previously ATP6IP2 |
| Reactome | 7 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O75787](https://www.uniprot.org/uniprotkb/O75787) (Renin receptor):

> Multifunctional protein which functions as a renin, prorenin cellular receptor and is involved in the assembly of the lysosomal proton-transporting V-type ATPase (V-ATPase) and the acidification of the endo-lysosomal system. May mediate renin-dependent cellular responses by activating ERK1 and ERK2. By increasing the catalytic efficiency of renin in AGT/angiotensinogen conversion to angiotensin I, may also play a role in the renin-angiotensin system (RAS). Through its function in V-type ATPase …

**Summary**, from NCBI Gene [10159](https://www.ncbi.nlm.nih.gov/gene/10159):

> This gene encodes a protein that is associated with adenosine triphosphatases (ATPases). Proton-translocating ATPases have fundamental roles in energy conservation, secondary active transport, acidification of intracellular compartments, and cellular pH homeostasis. There are three classes of ATPases- F, P, and V. The vacuolar (V-type) ATPases have a transmembrane proton-conducting sector and an extramembrane catalytic sector. The encoded protein has been found associated with the transmembrane …

**Accessions** — [HGNC:18305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18305) · Entrez [10159](https://www.ncbi.nlm.nih.gov/gene/10159) · UniProt [O75787](https://www.uniprot.org/uniprotkb/O75787) · Ensembl [ENSG00000182220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182220)

## Data

Gene col 11261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11261); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11261]; `tensor/DDL_lfc|DDL_z.npy` [11261]; `embed/gene_vectors.npy` [11261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11261 or target_col == 11261). Every well: [[ATP6AP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6AP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
