---
symbol: "PRAG1"
type: "gene"
col: 15848
ensembl_id: "ENSG00000275342"
name: "PEAK1 related, kinase-activating pseudokinase 1"
location: "8p23.1"
module: 34
arm: "+"
pooled_cpm: 131.84
n_lines_expressing: 34
n_dd_up: 14
n_dd_down: 39
n_dd_up_clean: 10
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 17
direction_downstream: 31
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PRAG1

*PEAK1 related, kinase-activating pseudokinase 1* — 8p23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.42× (z +12.0, q 4e-30, up in 22 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.457× (z -18.8, q 0e+00, down in 30 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.621× (z -16.1, q 0e+00, down in 28 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA6]] (+0.68, fdr 7e-06), [[SHB]] (+0.66, fdr 7e-06), [[LINC00659]] (+0.66, fdr 7e-06); moves opposite to [[TSR2]] (-0.48, fdr 2e-04), [[ADI1]] (-0.48, fdr 6e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[B3GNT3]] → it (grade B ⚠); 31 go from it, the strongest it → [[OSBPL10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15848.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +12.0 | 4e-30 | 22/32 (HEC-1-A, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.87×** | +7.9 | 8e-13 | 20/33 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +7.2 | 2e-10 | 19/32 (KATO III, SW 900, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +6.6 | 4e-09 | 17/33 (HEC-1-A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.30×** | +6.3 | 3e-08 | 13/32 (J82, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.27×** | +5.8 | 7e-07 | 10/32 (J82, SW 900, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.3 | 8e-06 | 15/32 (A498, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.23×** | +4.9 | 5e-05 | 9/32 (J82, SW 900, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 9/33 (AsPC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.008 | 7/32 (AsPC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.017 | 2/32 (HT-29, LS 180) | all doses, flat |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.11× | +3.5 | 0.020 | 8/33 (BT-474, Panc 03.27, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.020 | 14/32 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.10× | +3.4 | 0.027 | 5/33 (Panc 03.27, HepG2/C3A, …) | rises with dose |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.031 | 8/32 (CFPAC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.032 | 10/32 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.15× | +3.3 | 0.033 | 8/32 (NCI-H2347, A549, …) | top dose only | plate-row cell shift |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.038 | 6/32 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15848.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -18.8 | 0e+00 | 30/33 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.482×** | -16.8 | 0e+00 | 26/30 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -16.1 | 0e+00 | 28/33 (SW1417, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.521×** | -14.4 | 4e-45 | 28/30 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.590×** | -12.6 | 1e-34 | 26/33 (HepG2/C3A, HCT15, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.608×** | -11.5 | 2e-28 | 23/32 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.680×** | -11.4 | 6e-28 | 26/32 (A549, HepG2/C3A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -10.1 | 4e-22 | 21/31 (HepG2/C3A, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.638×** | -10.0 | 2e-21 | 23/32 (HepG2/C3A, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.654×** | -9.8 | 7e-21 | 25/32 (HepG2/C3A, HCT15, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.695×** | -9.3 | 5e-19 | 23/34 (HepG2/C3A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.738×** | -8.8 | 1e-16 | 22/32 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.698×** | -8.6 | 3e-16 | 20/32 (HCT15, SW480, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.731×** | -8.4 | 2e-15 | 22/33 (PANC-1, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.789×** | -8.0 | 4e-14 | 23/32 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.719×** | -7.9 | 1e-13 | 21/32 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -7.6 | 1e-12 | 21/32 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.803×** | -7.3 | 7e-12 | 21/32 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15848. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 435 | 0 | 25 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0835× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.234× (z -22.7) |
| [[SW480 (line)]] | alt | 412 | 2 | 22 (10 ⚠) | [[TAK-901 (drug)]] 5 µM 6.50× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -28.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -24.6) |
| [[MIA PaCa-2 (line)]] | alt | 229 | 1 | 22 (9 ⚠) | [[TAK-901 (drug)]] 5 µM 6.35× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -25.5) |
| [[PANC-1 (line)]] | alt | 159 | 0 | 23 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -37.2) |
| [[A549 (line)]] | wt | 280 | 0 | 19 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -28.3) |
| [[HCT15 (line)]] | alt | 334 | 0 | 18 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0655× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.127× (z -19.9) |
| [[Hs 766T (line)]] | wt | 122 | 1 | 12 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.69× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.9) |
| [[HOP62 (line)]] | alt | 55.2 | 0 | 9 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.666× (z -12.2) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 96.1 | 1 | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.93× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -14.5) |
| [[SW1417 (line)]] | alt | 207 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -27.2) |
| [[AsPC-1 (line)]] | alt | 219 | 1 (1 ⚠) | 5 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +9.3) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -15.0) |
| [[KATO III (line)]] | alt | 233 | 1 (1 ⚠) | 5 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.24× (z +10.7) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.197× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.478× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 202 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0806× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -18.8) |
| [[SW48 (line)]] | wt | 185 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.288× (z -9.6) |
| [[A498 (line)]] | wt | 70.3 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.07× (z +13.8) ⚠ unreliable plate only | [[Harringtonine (drug)]] 5 µM 0.348× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 101 | 1 | 4 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.86× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 190 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -19.5) |
| [[LoVo (line)]] | wt | 254 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.324× (z -10.7) |
| [[LS 180 (line)]] | wt | 323 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -21.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 83.5 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.173× (z -12.7) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -8.6) |
| [[HT-29 (line)]] | alt | 123 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -17.3) |
| [[A-172 (line)]] | wt | 75.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.4) |
| [[BT-474 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 39.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.390× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 302 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 29.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 31.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 81.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 29.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.6 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 72.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15848), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA6]] | +0.68 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[SHB]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[LINC00659]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TINAGL1]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ONECUT3]] | +0.62 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[EPHA2]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 | pathway: RND2 GTPase cycle |
| [[NTSR1]] | +0.62 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[KRT15]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SPRED2]] | +0.60 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[DUSP6]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[CDCP1]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR2]] | -0.48 | -0.53 / -0.31 | both halves | 2e-04 |  |
| [[ADI1]] | -0.48 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 12, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | B3GNT3 activity raises PRAG1's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.35× lower at baseline in the lines without B3GNT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[TGFA]] | B | TGFA activity raises PRAG1's level | lines that do not express TGFA (17) vs lines expressing it (33) | 2.55× lower at baseline in the lines without TGFA | 0.032 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[LINC02320]] | B | LINC02320 activity raises PRAG1's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 2.63× lower at baseline in the lines without LINC02320 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[TMC6]] | B | TMC6 activity raises PRAG1's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 2.64× lower at baseline in the lines without TMC6 | 0.046 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[GOLT1A]] | B | GOLT1A activity raises PRAG1's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without GOLT1A | 0.049 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[LEMD1]] | B | LEMD1 activity raises PRAG1's level | lines that do not express LEMD1 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without LEMD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: BLACAT1, MPZL3, SULT1C2 |
| [[LINC02964]] | B | LINC02964 activity raises PRAG1's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 3.79× lower at baseline in the lines without LINC02964 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3 |
| [[EEPD1]] | B | EEPD1 activity raises PRAG1's level | lines that do not express EEPD1 (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without EEPD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: KCNK5, RHOD, LAMP3; maybe low, not absent |
| [[LAMC2]] | B | LAMC2 activity raises PRAG1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.77× lower at baseline in the lines without LAMC2 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[BLACAT1]] | B | BLACAT1 activity raises PRAG1's level | lines that do not express BLACAT1 (21) vs lines expressing it (29) | 2.45× lower at baseline in the lines without BLACAT1 | 0.085 | ⚠ within organs, on part of the lines; also absent: LEMD1, MPZL3, SULT1C2 |
| [[LCK]] | B | LCK activity raises PRAG1's level | lines that do not express LCK (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without LCK | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KRT23, ENSG00000260573, RBP1; maybe low, not absent |
| [[ACOT11]] | B | ACOT11 activity raises PRAG1's level | lines that do not express ACOT11 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without ACOT11 | 0.098 | ⚠ within organs, on part of the lines; also absent: GALM, GALNT6, MROH7; maybe low, not absent |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 26, C 5. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL10]] | B | PRAG1 activity raises OSBPL10's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without PRAG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[TMC6]] | B | PRAG1 activity raises TMC6's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.86× lower at baseline in the lines without PRAG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[B3GNT3]] | B | PRAG1 activity raises B3GNT3's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.52× lower at baseline in the lines without PRAG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[GPR35]] | B | PRAG1 activity raises GPR35's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PRAG1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[LAMC2]] | B | PRAG1 activity raises LAMC2's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without PRAG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SH2D3A]] | B | PRAG1 activity raises SH2D3A's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.30× lower at baseline in the lines without PRAG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[TGFA]] | B | PRAG1 activity raises TGFA's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without PRAG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[CARD10]] | B | PRAG1 activity raises CARD10's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without PRAG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[CD320]] | B | PRAG1 activity lowers CD320's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.55× higher at baseline in the lines without PRAG1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[PTGS1]] | B | PRAG1 activity raises PTGS1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without PRAG1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[SLC25A25]] | B | PRAG1 activity raises SLC25A25's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 1.75× lower at baseline in the lines without PRAG1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[LEMD1]] | B | PRAG1 activity raises LEMD1's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.62× lower at baseline in the lines without PRAG1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.9, 3.2); signed map (3.3, 41.8). **Vector** length 128, 38.1% of its response variance represented; |z| ≥ 3 in 1,408 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.5 | +12.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.0 | +7.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.7 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.4 | +4.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +4.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +2.4 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -7.8 | -9.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.9 | -11.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.7 | -12.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.4 | -10.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -6.4 | -9.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.9 | -8.4 |

## What is on record

|  |  |
|---|---|
| Name | PEAK1 related, kinase-activating pseudokinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p23.1 — chr8:8,317,736-8,386,439 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761P0423, SgK223, PRAGMIN, PEAK2, NACK |
| Gene groups (HGNC) | Pseudokinases; PEAK pseudokinase family |
| Reactome | 4 pathways, smallest: RND2 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YV5](https://www.uniprot.org/uniprotkb/Q86YV5) (Inactive tyrosine-protein kinase PRAG1):

> Catalytically inactive protein kinase that acts as a scaffold protein. Functions as an effector of the small GTPase RND2, which stimulates RhoA activity and inhibits NGF-induced neurite outgrowth (By similarity). Promotes Src family kinase (SFK) signaling by regulating the subcellular localization of CSK, a negative regulator of these kinases, leading to the regulation of cell morphology and motility by a CSK-dependent mechanism (By similarity). Acts as a critical coactivator of Notch signaling …

**Summary**, from NCBI Gene [157285](https://www.ncbi.nlm.nih.gov/gene/157285):

> This gene encodes an enzyme that belongs to the tyrosine protein kinase family. A similar protein in rat binds to Rho family GTPase 2 (Rnd2) and regulates neurite outgrowth via activation of Ras homolog gene family, member A (RhoA). [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:25438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25438) · Entrez [157285](https://www.ncbi.nlm.nih.gov/gene/157285) · UniProt [Q86YV5](https://www.uniprot.org/uniprotkb/Q86YV5) · Ensembl [ENSG00000275342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275342)

## Data

Gene col 15848: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15848); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15848, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15848]; `tensor/DDL_lfc|DDL_z.npy` [15848]; `embed/gene_vectors.npy` [15848]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15848 or target_col == 15848). Every well: [[PRAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
