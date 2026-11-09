---
symbol: "DHX32"
type: "gene"
col: 1603
ensembl_id: "ENSG00000089876"
name: "DEAH-box helicase 32 (putative)"
location: "10q26.2"
module: 144
arm: "+"
pooled_cpm: 105.42
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# DHX32

*DEAH-box helicase 32 (putative)* — 10q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.30× (z +11.1, q 1e-25, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.411× (z -26.3, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ING2-DT]] (+0.63, fdr 2e-05), [[NDUFC1]] (+0.62, fdr 3e-05), [[HMGCL]] (+0.60, fdr 1e-05); moves opposite to [[SRRT]] (-0.57, fdr 1e-05), [[SPIN1]] (-0.53, fdr 3e-05), [[THRAP3]] (-0.52, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +11.1 | 1e-25 | 31/49 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +7.7 | 5e-12 | 29/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +7.6 | 7e-12 | 24/48 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +6.9 | 8e-10 | 26/50 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.010 | 14/49 (A-172, NCI-H2347, …) | top dose only |  |
| [[Adenosine (drug)]] 5 µM |  | 1.09× | +3.5 | 0.042 | 1/48 (SHP-77) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +3.5 | 0.042 | 14/48 (NCI-H2347, A-427, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.064 | 12/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ranolazine (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.083 | 4/48 (SW1417, Panc 03.27, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.083 | 7/48 (KATO III, LS 180, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.12× | +3.1 | 0.086 | 12/47 (A-172, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.411×** | -26.3 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.567×** | -23.7 | 0e+00 | 37/48 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.449×** | -23.7 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.513×** | -19.7 | 0e+00 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.508×** | -19.3 | 0e+00 | 37/43 (NCI-H1573, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.560×** | -17.1 | 0e+00 | 38/49 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.572×** | -16.5 | 0e+00 | 42/48 (C32, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.353×** | -16.1 | 0e+00 | 44/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.574×** | -15.8 | 0e+00 | 41/47 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -13.5 | 1e-39 | 37/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.447×** | -12.4 | 8e-34 | 41/48 (SNU-423, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.662×** | -12.2 | 2e-32 | 37/48 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.666×** | -11.1 | 6e-27 | 30/45 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -8.1 | 2e-14 | 28/48 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.765×** | -7.9 | 1e-13 | 31/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.829×** | -7.8 | 2e-13 | 23/48 (PANC-1, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.829×** | -5.3 | 3e-06 | 22/48 (C32, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.866× | -4.0 | 0.001 | 15/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.890× | -3.4 | 0.012 | 7/48 (C-33 A, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 296 | 0 | 27 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -27.0) |
| [[NCI-H460 (line)]] | wt | 106 | 0 | 18 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -19.7) |
| [[SNU-423 (line)]] | alt | 151 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -30.7) |
| [[C32 (line)]] | wt | 120 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0892× (z -36.3) |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -28.6) |
| [[HEC-1-A (line)]] | alt | 98.8 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -24.9) |
| [[HOP62 (line)]] | alt | 101 | 1 | 9 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -21.2) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 91.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -16.4) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -13.7) |
| [[LS 180 (line)]] | wt | 101 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -25.0) |
| [[SW 900 (line)]] | alt | 140 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.310× (z -12.0) |
| [[A549 (line)]] | wt | 100 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -12.4) |
| [[HCT15 (line)]] | alt | 134 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.7) |
| [[J82 (line)]] | alt | 56.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -22.2) |
| [[LoVo (line)]] | wt | 68.3 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 73.8 | 1 | 6 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.4) |
| [[HT-29 (line)]] | alt | 88.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.354× (z -13.2) |
| [[NCI-H1573 (line)]] | alt | 252 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.9) |
| [[SW480 (line)]] | alt | 81.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.300× (z -19.2) |
| [[C-33 A (line)]] | alt | 94.2 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.309× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 51.1 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -11.4) |
| [[A-172 (line)]] | wt | 66.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.431× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 76.9 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.175× (z -12.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.607× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 75.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.3) |
| [[SW1417 (line)]] | alt | 85.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.462× (z -9.8) |
| [[A498 (line)]] | wt | 67.8 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.633× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 82.8 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +12.7) | [[Panobinostat (drug)]] 0.5 µM 0.365× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.358× (z -9.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -9.6) |
| [[HS-578T (line)]] | alt | 39.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 75.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.412× (z -9.6) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.282× (z -9.4) |
| [[H4 (line)]] | wt | 137 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -12.8) |
| [[Hs 766T (line)]] | wt | 71.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 78.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.440× (z -8.9) |
| [[SW48 (line)]] | wt | 92.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.174× (z -15.2) |
| [[A-427 (line)]] | wt | 65.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.270× (z -8.7) |
| [[CHP-212 (line)]] | wt | 85.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -11.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.477× (z -9.2) |
| [[SW 1271 (line)]] | alt | 71.0 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0895× (z -9.0) |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2-DT]] | +0.63 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[NDUFC1]] | +0.62 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[HMGCL]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[DARS1-AS1]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NMNAT1]] | +0.58 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MAP2K4]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MFSD8]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[METTL21A]] | +0.53 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[ZSWIM5]] | +0.52 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[TUBGCP5]] | +0.52 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[C4orf47]] | +0.52 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TAF12]] | +0.52 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRRT]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SPIN1]] | -0.53 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[THRAP3]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.52 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ZNF527]] | -0.51 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[EHMT2]] | -0.51 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[AGPS]] | -0.51 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.51 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[DHX9]] | -0.50 | -0.48 / -0.53 | both halves | 2e-05 | same gene group |
| [[TPM1]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[DLD]] | -0.49 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[SOAT1]] | -0.49 | -0.27 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHX32's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.6, 17.0); signed map (-3.8, 3.4). **Vector** length 117, 36.0% of its response variance represented; |z| ≥ 3 in 1,455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +11.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +7.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.1 | -19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -8.5 | -17.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.7 | -11.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.1 | -26.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | -12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.4 | -16.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -8.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 32 (putative) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.2 — chr10:125,836,337-125,896,436 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10889, FLJ10694, DHLP1; previously DDX32 |
| Gene groups (HGNC) | DEAH-box helicases |
| Matched by | ensembl_id |

UniProt [Q7L7V1](https://www.uniprot.org/uniprotkb/Q7L7V1) carries no function annotation.

**Summary**, from NCBI Gene [55760](https://www.ncbi.nlm.nih.gov/gene/55760):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:16717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16717) · Entrez [55760](https://www.ncbi.nlm.nih.gov/gene/55760) · UniProt [Q7L7V1](https://www.uniprot.org/uniprotkb/Q7L7V1) · Ensembl [ENSG00000089876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089876)

## Data

Gene col 1603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1603); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1603]; `tensor/DDL_lfc|DDL_z.npy` [1603]; `embed/gene_vectors.npy` [1603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1603 or target_col == 1603). Every well: [[DHX32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
