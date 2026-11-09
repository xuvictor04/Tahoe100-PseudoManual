---
symbol: "FOXN3"
type: "gene"
col: 591
ensembl_id: "ENSG00000053254"
name: "forkhead box N3"
location: "14q31.3-q32.11"
module: 225
arm: "+"
pooled_cpm: 128.15
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 35
n_dd_up_clean: 17
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# FOXN3

*forkhead box N3* — 14q31.3-q32.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.27× (z +8.9, q 3e-16, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.557× (z -22.0, q 0e+00, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.67, fdr 7e-06), [[SAP30]] (+0.62, fdr 1e-05), [[TNRC6B]] (+0.61, fdr 1e-05); moves opposite to [[GTF2H3]] (-0.51, fdr 3e-05), [[CDC42EP2]] (-0.50, fdr 3e-05), [[TTLL11]] (-0.48, fdr 7e-05).
> It is in [[Module 225]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +8.9 | 3e-16 | 28/46 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +6.5 | 2e-08 | 25/46 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +6.5 | 2e-08 | 30/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +6.2 | 7e-08 | 29/45 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +6.1 | 2e-07 | 24/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +5.9 | 4e-07 | 23/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.57×** | +5.6 | 2e-06 | 30/48 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +5.4 | 4e-06 | 26/47 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 2e-05 | 21/46 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +5.1 | 2e-05 | 23/47 (BT-474, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.51×** | +5.1 | 2e-05 | 21/47 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.21×** | +5.0 | 3e-05 | 21/47 (LoVo, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **1.49×** | +4.9 | 5e-05 | 23/47 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.13× | +4.8 | 8e-05 | 9/46 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +4.7 | 8e-05 | 15/46 (LoVo, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.19× | +4.7 | 8e-05 | 17/45 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +4.5 | 3e-04 | 9/46 (NCI-H2347, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 19 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 591.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.557×** | -22.0 | 0e+00 | 36/46 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.455×** | -20.9 | 0e+00 | 41/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.516×** | -17.6 | 0e+00 | 43/46 (SW1417, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.506×** | -16.7 | 0e+00 | 33/43 (RKO, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.543×** | -15.6 | 0e+00 | 38/46 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.668×** | -10.3 | 5e-23 | 33/45 (C32, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.679×** | -10.3 | 6e-23 | 32/46 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.669×** | -10.3 | 6e-23 | 26/42 (C32, SHP-77, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.449×** | -9.8 | 5e-21 | 36/47 (SHP-77, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **0.692×** | -9.8 | 7e-21 | 30/47 (SNU-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -9.7 | 2e-20 | 33/46 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.472×** | -9.2 | 2e-18 | 39/46 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.710×** | -9.1 | 4e-18 | 34/46 (C32, HepG2/C3A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.490×** | -8.8 | 7e-17 | 38/46 (MIA PaCa-2, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.490×** | -8.7 | 8e-17 | 39/46 (MIA PaCa-2, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -8.5 | 4e-16 | 32/46 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.663×** | -7.8 | 2e-13 | 36/46 (SW1417, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.751×** | -7.2 | 2e-11 | 29/46 (HT-29, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -6.9 | 2e-10 | 32/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.586×** | -6.5 | 1e-09 | 29/45 (HCT15, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 177 | 0 | 17 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -22.7) |
| [[MIA PaCa-2 (line)]] | alt | 240 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 102 | 0 | 15 (9 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -25.5) |
| [[HepG2_C3A (line)]] | wt | 366 | 0 | 14 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.207× (z -20.1) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.343× (z -14.2) |
| [[SHP-77 (line)]] | alt | 280 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.524× (z -12.8) |
| [[SW48 (line)]] | wt | 210 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.7) |
| [[HT-29 (line)]] | alt | 152 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -13.6) |
| [[NCI-H1792 (line)]] | alt | 266 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -23.3) |
| [[SNU-1 (line)]] | wt | 165 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0552× (z -28.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.241× (z -14.1) |
| [[J82 (line)]] | alt | 239 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.457× (z -18.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.560× (z -13.5) |
| [[LoVo (line)]] | wt | 143 | 2 (1 ⚠) | 6 (3 ⚠) | [[Trametinib (drug)]] 0.5 µM 1.61× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 134 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.0) |
| [[SW480 (line)]] | alt | 165 | 0 | 8 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.284× (z -15.4) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -13.7) |
| [[HEC-1-A (line)]] | alt | 134 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -21.6) |
| [[RKO (line)]] | wt | 82.7 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.3) |
| [[SK-MEL-2 (line)]] | alt | 178 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -19.8) |
| [[A549 (line)]] | wt | 87.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -23.0) |
| [[RPMI-7951 (line)]] | alt | 186 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -18.1) |
| [[A-427 (line)]] | wt | 156 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -15.9) |
| [[KATO III (line)]] | alt | 140 | 1 | 3 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 1.99× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -12.8) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 209 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -12.4) |
| [[SW1417 (line)]] | alt | 113 | 1 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.68× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -19.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.194× (z -9.1) |
| [[AN3 CA (line)]] | alt | 290 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -15.5) |
| [[LS 180 (line)]] | wt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.348× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 97.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 82.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -26.7) |
| [[PANC-1 (line)]] | alt | 38.3 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.00× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -9.4) |
| [[C-33 A (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.341× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[COLO 205 (line)]] | alt | 149 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -14.8) |
| [[HOP62 (line)]] | alt | 78.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.77× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.555× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 88.5 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.06× (z +10.6) | — |
| [[A-172 (line)]] | wt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 44.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 191 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[H4 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.363× (z -8.6) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 79.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -8.6) |
| [[SW 900 (line)]] | alt | 123 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.388× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 23.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 141 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[SAP30]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[TNRC6B]] | +0.61 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[CNNM2]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[BRWD1]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RORA]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.57 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LCORL]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB44]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MXI1]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PDPR]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[IPMK]] | +0.53 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.51 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[CDC42EP2]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TTLL11]] | -0.48 | -0.52 / -0.38 | both halves | 7e-05 |  |
| [[ZNF621]] | -0.48 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[IKBKG]] | -0.46 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[LINC00941]] | -0.46 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[ZPR1]] | -0.46 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[C1RL-AS1]] | -0.45 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SZT2]] | -0.45 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[PSMD12]] | -0.45 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[CAPN2]] | -0.44 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[HAS3]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers FOXN3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[SPRY1]] | C | SPRY1 activity raises FOXN3's level | lines that do not express SPRY1 (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without SPRY1 | 0.023 | ⚠ few lines (4 vs 46); across organs; also absent: ARG2, ZNF385C, ENSG00000290927; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.823). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (1.4, -41.9); signed map (-16.1, 12.7). **Vector** length 124, 42.3% of its response variance represented; |z| ≥ 3 in 1,851 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +7.5 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +8.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +6.4 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | -1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.9 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +6.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +3.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.4 | -17.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -9.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.3 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.2 | -20.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -3.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.5 | -6.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box N3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3-q32.11 — chr14:89,124,871-89,619,149 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C14orf116, CHES1 |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | G2M_CHECKPOINT |
| Matched by | ensembl_id |

**Function**, from UniProt [O00409](https://www.uniprot.org/uniprotkb/O00409) (Forkhead box protein N3):

> Acts as a transcriptional repressor. May be involved in DNA damage-inducible cell cycle arrests (checkpoints).

**Summary**, from NCBI Gene [1112](https://www.ncbi.nlm.nih.gov/gene/1112):

> This gene is a member of the forkhead/winged helix transcription factor family. Checkpoints are eukaryotic DNA damage-inducible cell cycle arrests at G1 and G2. Checkpoint suppressor 1 suppresses multiple yeast checkpoint mutations including mec1, rad9, rad53 and dun1 by activating a MEC1-independent checkpoint pathway. Alternative splicing is observed at the locus, resulting in distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1928) · Entrez [1112](https://www.ncbi.nlm.nih.gov/gene/1112) · UniProt [O00409](https://www.uniprot.org/uniprotkb/O00409) · Ensembl [ENSG00000053254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000053254)

## Data

Gene col 591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 591); `tables/drug_effects.parquet` (97 rows, flagged included); `relations/gene_relations.parquet` (col_a == 591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 591]; `tensor/DDL_lfc|DDL_z.npy` [591]; `embed/gene_vectors.npy` [591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 591 or target_col == 591). Every well: [[FOXN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
