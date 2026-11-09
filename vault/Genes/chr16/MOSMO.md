---
symbol: "MOSMO"
type: "gene"
col: 11719
ensembl_id: "ENSG00000185716"
name: "modulator of smoothened"
location: "16p12.2"
module: 147
arm: "+"
pooled_cpm: 94.54
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# MOSMO

*modulator of smoothened* — 16p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.38× (z +9.8, q 7e-20, up in 32 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.466× (z -16.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POC1B-AS1]] (+0.66, fdr 1e-05), [[SPRY4-AS1]] (+0.63, fdr 8e-06), [[GNG12-AS1]] (+0.63, fdr 1e-05); moves opposite to [[MAPRE2]] (-0.63, fdr 1e-05), [[CAT]] (-0.59, fdr 2e-05), [[TUFT1]] (-0.57, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11719.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.8 | 7e-20 | 32/49 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +5.7 | 4e-06 | 30/49 (AsPC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.17× | +4.7 | 5e-04 | 18/48 (SW480, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.002 | 21/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.20× | +3.9 | 0.013 | 21/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.020 | 16/48 (SW480, LS 180, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.025 | 20/48 (KATO III, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.5 | 0.036 | 16/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.3 | 0.054 | 21/48 (SW480, LS 180, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +3.3 | 0.058 | 22/48 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.091 | 19/47 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.0 | 0.11 | 20/47 (LS 180, HEC-1-A, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11719.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.466×** | -16.5 | 0e+00 | 44/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -15.5 | 0e+00 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.555×** | -12.7 | 7e-35 | 41/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -11.4 | 5e-28 | 40/49 (NCI-H23, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -11.4 | 7e-28 | 35/44 (C-33 A, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.684×** | -7.6 | 3e-12 | 27/45 (C-33 A, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -6.9 | 4e-10 | 31/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.746×** | -6.3 | 2e-08 | 35/48 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.826×** | -5.9 | 3e-07 | 25/48 (AsPC-1, C32, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.801×** | -5.9 | 3e-07 | 26/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.766×** | -5.8 | 4e-07 | 26/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -5.7 | 6e-07 | 32/47 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.800×** | -5.6 | 1e-06 | 29/50 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.790×** | -5.1 | 1e-05 | 26/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **0.802×** | -4.8 | 7e-05 | 28/48 (SW48, KATO III, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.814×** | -4.4 | 3e-04 | 25/49 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.830×** | -4.4 | 3e-04 | 21/48 (AsPC-1, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.837× | -4.4 | 3e-04 | 22/49 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.830×** | -4.0 | 0.002 | 22/47 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.826×** | -3.9 | 0.002 | 21/48 (AsPC-1, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11719. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 189 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -15.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -13.0) |
| [[C32 (line)]] | wt | 124 | 5 (4 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.37× (z +9.7) | [[Cobimetinib (drug)]] 5 µM 0.334× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.313× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -12.3) |
| [[PANC-1 (line)]] | alt | 166 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.231× (z -16.2) |
| [[SW480 (line)]] | alt | 72.3 | 4 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -19.5) |
| [[LoVo (line)]] | wt | 97.9 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.182× (z -20.5) |
| [[HOP62 (line)]] | alt | 69.3 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 177 | 4 (4 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +10.4) ⚠ cell-cycle shift, explains ~19% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 119 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -16.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -14.6) |
| [[H4 (line)]] | wt | 109 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.237× (z -12.6) |
| [[KATO III (line)]] | alt | 103 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -16.5) |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.3) | [[AZD2858 (drug)]] 0.5 µM 0.179× (z -12.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 78.5 | 2 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -27.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.518× (z -8.5) |
| [[RKO (line)]] | wt | 71.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.312× (z -11.7) |
| [[SW1417 (line)]] | alt | 140 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -10.9) |
| [[A498 (line)]] | wt | 92.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.415× (z -12.1) |
| [[HCT15 (line)]] | alt | 83.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +14.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 78.7 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.333× (z -13.1) |
| [[NCI-H1792 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.404× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 86.6 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -16.0) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 75.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.370× (z -12.1) |
| [[SW 900 (line)]] | alt | 56.1 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.374× (z -8.9) |
| [[C-33 A (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -20.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 78.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -15.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 70.5 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -9.9) |
| [[J82 (line)]] | alt | 78.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.456× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -11.2) |
| [[SNU-1 (line)]] | wt | 95.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -15.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 64.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.294× (z -12.5) ⚠ toxic; cell-cycle shift, explains ~19% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -9.2) |
| [[A-427 (line)]] | wt | 95.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -9.2) |
| [[BT-474 (line)]] | alt | 73.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -8.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.196× (z -9.0) |
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 70.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H661 (line)]] | alt | 57.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.123× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 70.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -8.9) |
| [[SW 1271 (line)]] | alt | 81.2 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0845× (z -10.1) |
| [[SW48 (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.245× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[A-172 (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 88.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11719), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POC1B-AS1]] | +0.66 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[GNG12-AS1]] | +0.63 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[HMGA2]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[ZNF26]] | +0.61 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ZNF41]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ADAMTS9]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[BCL2L1]] | +0.58 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.58 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[C11orf91]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MSANTD2]] | +0.58 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[STXBP5-AS1]] | +0.58 | +0.46 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE2]] | -0.63 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[CAT]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[TUFT1]] | -0.57 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[AMOT]] | -0.57 | -0.43 / -0.59 | both halves | 3e-05 |  |
| [[CXADR]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[GPRC5B]] | -0.57 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[USP2]] | -0.56 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[KIF16B]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[GPI]] | -0.55 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ARHGAP35]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[STARD5]] | -0.53 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[IFT57]] | -0.53 | -0.36 / -0.62 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises MOSMO's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[SLC26A2]] | C | SLC26A2 activity raises MOSMO's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without SLC26A2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.623). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.5, 0.8); signed map (11.1, 36.6). **Vector** length 134, 40.7% of its response variance represented; |z| ≥ 3 in 1,526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.5 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.4 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +6.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.6 | +4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +4.8 | +3.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.9 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.6 | -5.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.4 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.3 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.2 | -5.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | modulator of smoothened |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.2 — chr16:22,007,638-22,087,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATTHOG, BC030336; previously C16orf52 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NHV5](https://www.uniprot.org/uniprotkb/Q8NHV5) (Modulator of smoothened protein):

> Component of the MMM ubiquitin ligase complex, a multiprotein complex that acts as a negative regulator of smoothened signaling pathway by mediating the ubiquitination and degradation of smoothened (SMO) in primary cilia. Plays a role in sonic hedgehog (SHH)-induced spinal neural progenitor cells differentiation (By similarity).

**Summary**, from NCBI Gene [730094](https://www.ncbi.nlm.nih.gov/gene/730094):

> Predicted to be involved in negative regulation of smoothened signaling pathway; regulation of neuron differentiation; and regulation of protein stability. Predicted to act upstream of or within several processes, including chordate embryonic development; embryonic limb morphogenesis; and smoothened signaling pathway. Predicted to be located in plasma membrane. Predicted to be active in Golgi apparatus and ciliary membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27087) · Entrez [730094](https://www.ncbi.nlm.nih.gov/gene/730094) · UniProt [Q8NHV5](https://www.uniprot.org/uniprotkb/Q8NHV5) · Ensembl [ENSG00000185716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185716)

## Data

Gene col 11719: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11719); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11719, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11719]; `tensor/DDL_lfc|DDL_z.npy` [11719]; `embed/gene_vectors.npy` [11719]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11719 or target_col == 11719). Every well: [[MOSMO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOSMO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
