---
symbol: "PSAT1"
type: "gene"
col: 5645
ensembl_id: "ENSG00000135069"
name: "phosphoserine aminotransferase 1"
location: "9q21.2"
module: 63
arm: "+"
pooled_cpm: 47.41
n_lines_expressing: 42
n_dd_up: 48
n_dd_down: 32
n_dd_up_clean: 39
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 3
direction_downstream: 17
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PSAT1

*phosphoserine aminotransferase 1* — 9q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +15.9, q 0e+00, up in 26 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Artesunate (drug)]] 5 µM: 2.13× (z +13.7, q 1e-40, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.346× (z -19.3, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHGDH]] (+0.92, fdr 7e-06), [[MTHFD2]] (+0.90, fdr 7e-06), [[ASNS]] (+0.88, fdr 7e-06); moves opposite to [[TOPORS]] (-0.50, fdr 2e-05), [[NFAT5]] (-0.50, fdr 6e-05), [[TBCC]] (-0.49, fdr 3e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 17 go from it, the strongest it → [[IARS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.44×** | +15.9 | 0e+00 | 26/35 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +15.6 | 0e+00 | 25/32 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Artesunate (drug)]] 5 µM |  | **2.13×** | +13.7 | 1e-40 | 37/40 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **3.17×** | +13.4 | 8e-39 | 38/40 (NCI-H460, A498, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.74×** | +12.9 | 3e-36 | 38/40 (C-33 A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.73×** | +12.9 | 4e-36 | 38/40 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.95×** | +12.1 | 6e-32 | 37/40 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.43×** | +11.0 | 3e-26 | 31/39 (RKO, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.31×** | +9.9 | 2e-21 | 21/33 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Neratinib (drug)]] 5 µM |  | **2.08×** | +9.4 | 3e-19 | 35/39 (C-33 A, RKO, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.97×** | +8.7 | 1e-16 | 34/40 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.91×** | +8.3 | 6e-15 | 29/39 (C-33 A, Hs 766T, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.51×** | +7.5 | 3e-12 | 28/41 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.71×** | +6.9 | 2e-10 | 27/39 (HEC-1-A, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.59×** | +6.0 | 9e-08 | 19/40 (SNU-423, J82, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.57×** | +5.8 | 2e-07 | 26/40 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.7 | 3e-07 | 24/40 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 2e-06 | 23/40 (C-33 A, A-172, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.34×** | +5.2 | 5e-06 | 26/38 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.33×** | +5.2 | 5e-06 | 26/40 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 2e-05 | 19/40 (HEC-1-A, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5645.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.346×** | -19.3 | 0e+00 | 37/39 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.285×** | -15.5 | 0e+00 | 31/40 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.357×** | -13.2 | 1e-37 | 34/40 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.452×** | -10.2 | 3e-22 | 30/39 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.443×** | -9.7 | 5e-20 | 34/39 (SNU-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.517×** | -8.5 | 2e-15 | 28/40 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.624×** | -6.1 | 1e-07 | 24/39 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.631×** | -5.9 | 2e-07 | 24/40 (LS 180, RKO, …) | all doses, flat | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.634×** | -5.8 | 3e-07 | 26/38 (A498, HS-578T, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -5.7 | 7e-07 | 20/39 (PANC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | **0.745×** | -5.4 | 4e-06 | 22/40 (A498, LoVo, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.663×** | -5.3 | 7e-06 | 26/39 (A-172, H4, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.687×** | -4.8 | 6e-05 | 19/40 (HS-578T, SW480, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.686×** | -4.6 | 2e-04 | 18/40 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.610×** | -4.5 | 2e-04 | 18/40 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.611×** | -4.5 | 2e-04 | 14/40 (H4, HS-578T, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 96.5 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -38.7) |
| [[SW1417 (line)]] | alt | 72.6 | 1 (1 ⚠) | 10 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.07× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -23.5) |
| [[SW480 (line)]] | alt | 90.8 | 1 | 10 (2 ⚠) | [[Neratinib (maleate) (drug)]] 5 µM 1.83× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -24.4) |
| [[A-427 (line)]] | wt | 48.6 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0765× (z -19.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 40.6 | 5 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 5.00× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Neratinib (maleate) (drug)]] 5 µM 2.98× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.6) |
| [[SW48 (line)]] | wt | 159 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.3) |
| [[RKO (line)]] | wt | 51.9 | 3 (1 ⚠) | 5 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.40× (z +9.4) ⚠ toxic · without an alert: [[Artesunate (drug)]] 5 µM 2.68× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.126× (z -13.3) |
| [[SNU-1 (line)]] | wt | 130 | 2 | 6 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.80× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -18.4) |
| [[H4 (line)]] | wt | 115 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0202× (z -33.2) |
| [[HT-29 (line)]] | alt | 91.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0700× (z -33.7) |
| [[LoVo (line)]] | wt | 125 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0610× (z -25.0) |
| [[A-172 (line)]] | wt | 37.4 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -14.8) |
| [[A498 (line)]] | wt | 69.8 | 1 (1 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.95× (z +9.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.6) |
| [[C-33 A (line)]] | alt | 78.1 | 4 | 1 | [[Neratinib (maleate) (drug)]] 5 µM 2.81× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 60.4 | 4 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 3.00× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.5) |
| [[C32 (line)]] | wt | 15.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.28× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 4.22× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 33.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.35× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) |
| [[LS 180 (line)]] | wt | 137 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.141× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 42.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.75× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -15.6) |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -9.1) |
| [[A549 (line)]] | wt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.2× (z +11.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.1) |
| [[Hs 766T (line)]] | wt | 34.7 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.43× (z +10.1) | — |
| [[J82 (line)]] | alt | 48.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 21.4 | 1 | 1 | [[Ponatinib (drug)]] 5 µM 5.01× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.5) |
| [[SNU-423 (line)]] | alt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.56× (z +9.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0600× (z -12.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.0) |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.191× (z -8.5) |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHGDH]] | +0.92 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[MTHFD2]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 763 |
| [[ASNS]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 864 |
| [[MARS1]] | +0.87 | +0.89 / +0.85 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 520 |
| [[AARS1]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | STRING 560 |
| [[IARS1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 440 |
| [[XPOT]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[YARS1]] | +0.85 | +0.84 / +0.85 | both halves | 7e-06 | STRING 498 |
| [[TCEA1]] | +0.84 | +0.77 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[TARS1]] | +0.81 | +0.80 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[GARS1]] | +0.81 | +0.81 / +0.80 | both halves | 7e-06 | STRING 456 |
| [[NARS1]] | +0.80 | +0.75 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOPORS]] | -0.50 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[NFAT5]] | -0.50 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[TBCC]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[ZNF440]] | -0.49 | -0.50 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity raises PSAT1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 4.5% of all compounds | 0.017 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ASNSP1]] | B | ASNSP1 activity raises PSAT1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without ASNSP1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[SLC1A4]] | C | SLC1A4 activity raises PSAT1's level | lines that do not express SLC1A4 (4) vs lines expressing it (46) | 3.35× lower at baseline in the lines without SLC1A4 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCNP, PSAT1, KAZN; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IARS1]] | B | PSAT1 activity raises IARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without PSAT1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[GARS1]] | B | PSAT1 activity raises GARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without PSAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[SARS1]] | B | PSAT1 activity raises SARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.47× lower at baseline in the lines without PSAT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[PHGDH]] | B | PSAT1 activity raises PHGDH's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 3.45× lower at baseline in the lines without PSAT1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[TMEM268]] | B | PSAT1 activity raises TMEM268's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without PSAT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[EPRS1]] | B | PSAT1 activity raises EPRS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without PSAT1 | 0.053 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[LONP1]] | B | PSAT1 activity raises LONP1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.44× lower at baseline in the lines without PSAT1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[ANK2]] | B | PSAT1 activity raises ANK2's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 3.30× lower at baseline in the lines without PSAT1 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[NARS1]] | B | PSAT1 activity raises NARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without PSAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[LARS1]] | B | PSAT1 activity raises LARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without PSAT1 | 0.060 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[SESN2]] | B | PSAT1 activity raises SESN2's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without PSAT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[YARS1]] | B | PSAT1 activity raises YARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without PSAT1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.887). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 47.6); signed map (-13.8, 24.2). **Vector** length 150, 49.2% of its response variance represented; |z| ≥ 3 in 1,516 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.82 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.82 to 9); *Response of EIF2AK1 (HRI) to heme deficiency* (reactome, mean cos +0.65 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.4 | +13.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.2 | +12.9 |
|  | [[Artesunate (drug)]] 5 µM |  | +7.7 | +13.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.5 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.4 | +11.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.0 | +8.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.4 | +8.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +5.7 | +9.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -9.1 | -15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -19.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -8.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.0 | -9.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -4.6 | -5.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.0 | -5.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.9 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphoserine aminotransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.2 — chr9:78,297,125-78,330,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PSA, PSAT |
| Gene groups (HGNC) | Transaminases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y617](https://www.uniprot.org/uniprotkb/Q9Y617) (Phosphoserine aminotransferase):

> Involved in L-serine biosynthesis via the phosphorylated pathway, a three-step pathway converting the glycolytic intermediate 3-phospho-D-glycerate into L-serine. Catalyzes the second step, that is the pyridoxal 5'-phosphate-dependent transamination of 3-phosphohydroxypyruvate and L-glutamate to O-phosphoserine (OPS) and alpha-ketoglutarate. Acts as an inhibitor of ferroptosis in response to interferon-gamma (IFNG) by promoting GPX4 stability: following phosphorylation by CAMK2A, PSAT1 …

**Summary**, from NCBI Gene [29968](https://www.ncbi.nlm.nih.gov/gene/29968):

> This gene encodes a member of the class-V pyridoxal-phosphate-dependent aminotransferase family. The encoded protein is a phosphoserine aminotransferase and decreased expression may be associated with schizophrenia. Mutations in this gene are also associated with phosphoserine aminotransferase deficiency. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene have been defined on chromosomes 1, 3, and 8. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:19129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19129) · Entrez [29968](https://www.ncbi.nlm.nih.gov/gene/29968) · UniProt [Q9Y617](https://www.uniprot.org/uniprotkb/Q9Y617) · Ensembl [ENSG00000135069](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135069)

## Data

Gene col 5645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5645); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5645]; `tensor/DDL_lfc|DDL_z.npy` [5645]; `embed/gene_vectors.npy` [5645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5645 or target_col == 5645). Every well: [[PSAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
