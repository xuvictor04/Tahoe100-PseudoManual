---
symbol: "ST7"
type: "gene"
col: 56
ensembl_id: "ENSG00000004866"
name: "suppression of tumorigenicity 7"
location: "7q31.2"
module: 137
arm: "+"
pooled_cpm: 165.08
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/137"]
generated_by: "tahoemap"
---

# ST7

*suppression of tumorigenicity 7* — 7q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.50× (z +9.5, q 9e-19, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.374× (z -16.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (55 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 45 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A21]] (+0.70, fdr 4e-04), [[KLHL42]] (+0.69, fdr 5e-05), [[ARSB]] (+0.66, fdr 1e-04); moves opposite to [[RAB40B]] (-0.67, fdr 3e-05), [[MAST3]] (-0.64, fdr 8e-04, ⚠ one half only (not replicated)), [[DNAAF3]] (-0.61, fdr 7e-04), [[FN3KRP]] (-0.60, fdr 5e-04).
> It sits in the **+** arm of [[Module 137]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 56.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +9.5 | 9e-19 | 34/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +8.2 | 5e-14 | 38/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +7.4 | 2e-11 | 41/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +5.5 | 5e-06 | 28/49 (Hs 766T, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 2e-05 | 32/48 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.6 | 4e-04 | 26/49 (RPMI-7951, SW 900, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +4.3 | 0.001 | 25/48 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.1 | 0.003 | 22/48 (RPMI-7951, C32, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.0 | 0.004 | 30/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.005 | 26/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.008 | 27/49 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.008 | 26/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.009 | 24/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.25×** | +3.7 | 0.010 | 25/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.019 | 24/48 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.019 | 20/48 (C32, NCI-H1573, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.022 | 22/47 (SW48, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 56.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.374×** | -16.6 | 0e+00 | 43/48 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.443×** | -13.7 | 2e-40 | 41/48 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.480×** | -12.4 | 5e-33 | 44/48 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.457×** | -12.2 | 7e-32 | 42/49 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.511×** | -10.9 | 1e-25 | 38/44 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.562×** | -9.0 | 2e-17 | 33/45 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.681×** | -6.5 | 7e-09 | 38/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -6.2 | 5e-08 | 32/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.748×** | -4.9 | 6e-05 | 28/48 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -3.9 | 0.006 | 28/48 (SK-MEL-2, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 56. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 160 | 6 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.216× (z -17.5) |
| [[SW48 (line)]] | wt | 234 | 6 | 5 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.54× (z +12.7) | [[Belinostat (drug)]] 5 µM 0.207× (z -14.1) |
| [[SW1417 (line)]] | alt | 307 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -16.5) |
| [[A498 (line)]] | wt | 143 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -18.8) |
| [[Hs 766T (line)]] | wt | 67.3 | 3 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -11.7) |
| [[HT-29 (line)]] | alt | 109 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.190× (z -17.4) |
| [[SW480 (line)]] | alt | 289 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.342× (z -13.7) |
| [[LoVo (line)]] | wt | 238 | 1 | 4 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.43× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.258× (z -16.5) |
| [[NCI-H1573 (line)]] | alt | 679 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.344× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 106 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +13.4) | [[Panobinostat (drug)]] 0.5 µM 0.408× (z -10.5) |
| [[SNU-1 (line)]] | wt | 162 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.0947× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.256× (z -12.5) |
| [[C32 (line)]] | wt | 221 | 4 | 0 | [[Ponatinib (drug)]] 5 µM 3.78× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 97.2 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.264× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 106 | 2 | 2 | [[Ponatinib (drug)]] 5 µM 3.11× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.6) |
| [[KATO III (line)]] | alt | 166 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.347× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 109 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -13.9) |
| [[RKO (line)]] | wt | 273 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -14.3) |
| [[A-427 (line)]] | wt | 72.3 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -8.6) |
| [[H4 (line)]] | wt | 136 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 157 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -16.4) |
| [[HS-578T (line)]] | alt | 125 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.372× (z -11.1) |
| [[J82 (line)]] | alt | 135 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 109 | 1 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.55× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -9.5) |
| [[SHP-77 (line)]] | alt | 189 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -10.6) |
| [[C-33 A (line)]] | alt | 117 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 248 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -14.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 187 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -9.9) |
| [[A-172 (line)]] | wt | 76.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.395× (z -9.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 89.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.37× (z +8.5) ⚠ unreliable plate only | — |
| [[CFPAC-1 (line)]] | alt | 82.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.06× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 130 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.9) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.338× (z -9.9) |
| [[PANC-1 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.8) | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -11.2) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 88.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.102× (z -9.5) |
| [[SW 900 (line)]] | alt | 103 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -9.4) |
| [[AN3 CA (line)]] | alt | 313 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 235 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 56), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 34 of them with an alert (⚠; 34 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A21]] | +0.70 | +0.62 / +0.26 | both halves | 4e-04 | same gene group |
| [[KLHL42]] | +0.69 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[ARSB]] | +0.66 | +0.62 / +0.35 | both halves | 1e-04 |  |
| [[FAIM]] | +0.66 | +0.51 / +0.27 | both halves | 3e-04 |  |
| [[GTF3C6]] | +0.63 | +0.53 / +0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[RCBTB2]] | +0.63 | +0.48 / +0.24 | both halves | 5e-04 |  |
| [[GRIP1]] | +0.63 | +0.50 / +0.32 | both halves | 2e-04 |  |
| [[ADCK1]] | +0.62 | +0.51 / +0.39 | both halves | 6e-05 |  |
| [[WNT3]] | +0.61 | +0.43 / +0.25 | both halves | 4e-04 |  |
| [[ANKRD18B]] | +0.60 | +0.45 / +0.26 | both halves | 3e-04 |  |
| [[PARD3B]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[TMEM117]] | +0.60 | +0.60 / +0.27 | both halves | 3e-04 |  |
| [[RXYLT1]] | +0.60 | +0.49 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB40B]] | -0.67 | -0.51 / -0.44 | both halves | 3e-05 | same gene group |
| [[MAST3]] | -0.64 | -0.54 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DNAAF3]] | -0.61 | -0.35 / -0.20 | both halves | 7e-04 |  |
| [[FN3KRP]] | -0.60 | -0.44 / -0.23 | both halves | 5e-04 |  |
| [[SLC27A1]] | -0.59 | -0.46 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[EFNA3]] | -0.57 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[EFNA4]] | -0.57 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[GNAI2]] | -0.56 | -0.35 / -0.11 | ⚠ not reproduced | 0.002 | same gene group |
| [[DHTKD1]] | -0.56 | -0.41 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[CABLES2]] | -0.56 | -0.40 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[KIAA1328]] | -0.55 | -0.47 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[TSC2]] | -0.55 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[MIGA2]] | -0.55 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[CBX7]] | -0.54 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MOSPD3]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[GMCL1]] | -0.53 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[HSPB11]] | -0.53 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[GET1]] | -0.53 | -0.39 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ST7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 137]]; 34 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-5.7, 9.0); signed map (24.6, -27.4). **Vector** length 118, 36.9% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.8 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.7 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +4.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.7 | +0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.5 | -12.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.2 | -16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.4 | -13.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -6.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -2.5 | -0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.4 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -2.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | suppression of tumorigenicity 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.2 — chr7:116,953,238-117,230,176 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSG7, SEN4, ETS7q, HELG, RAY1, FAM4A; previously FAM4A1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRC1](https://www.uniprot.org/uniprotkb/Q9NRC1) (Suppressor of tumorigenicity 7 protein):

> May act as a tumor suppressor.

**Summary**, from NCBI Gene [7982](https://www.ncbi.nlm.nih.gov/gene/7982):

> The gene for this product maps to a region on chromosome 7 identified as an autism-susceptibility locus. Mutation screening of the entire coding region in autistic individuals failed to identify phenotype-specific variants, suggesting that coding mutations for this gene are unlikely to be involved in the etiology of autism. The function of this gene product has not been determined. Transcript variants encoding different isoforms of this protein have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11351) · Entrez [7982](https://www.ncbi.nlm.nih.gov/gene/7982) · UniProt [Q9NRC1](https://www.uniprot.org/uniprotkb/Q9NRC1) · Ensembl [ENSG00000004866](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004866)

## Data

Gene col 56: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 56); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 56, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 56]; `tensor/DDL_lfc|DDL_z.npy` [56]; `embed/gene_vectors.npy` [56]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 56 or target_col == 56). Every well: [[ST7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ST7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
