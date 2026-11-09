---
symbol: "ZFX"
type: "gene"
col: 92
ensembl_id: "ENSG00000005889"
name: "zinc finger protein X-linked"
location: "Xp22.11"
module: 95
arm: "+"
pooled_cpm: 78.18
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ZFX

*zinc finger protein X-linked* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.04× (z +19.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.127× (z -44.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INO80D]] (+0.80, fdr 7e-06), [[PCNX4-DT]] (+0.76, fdr 3e-05), [[ZNF747]] (+0.76, fdr 7e-06); moves opposite to [[F11R]] (-0.71, fdr 1e-05), [[UBA6]] (-0.68, fdr 4e-05), [[NBPF3]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TNFRSF11A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 92.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.04×** | +19.2 | 0e+00 | 48/49 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +17.6 | 0e+00 | 43/48 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.78×** | +15.4 | 0e+00 | 47/48 (BT-474, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +12.2 | 3e-32 | 44/48 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +12.0 | 2e-31 | 42/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +11.4 | 5e-28 | 42/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.59×** | +9.9 | 3e-21 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +9.8 | 1e-20 | 41/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +9.7 | 2e-20 | 38/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +8.9 | 4e-17 | 38/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.0 | 4e-05 | 29/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +4.9 | 4e-05 | 0/50 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +4.8 | 7e-05 | 25/47 (LOX-IMVI, SW48, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.002 | 23/47 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +4.1 | 0.002 | 22/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.0 | 0.080 | 4/48 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.15× | +3.0 | 0.080 | 9/48 (Hs 766T, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 92.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.127×** | -44.1 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.140×** | -42.1 | 0e+00 | 48/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.157×** | -39.6 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.328×** | -23.9 | 0e+00 | 48/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.457×** | -16.8 | 0e+00 | 47/48 (HOP62, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.614×** | -14.7 | 0e+00 | 44/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.518×** | -14.1 | 4e-43 | 41/48 (C-33 A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.536×** | -12.8 | 9e-36 | 38/44 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.651×** | -9.2 | 3e-18 | 42/49 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.411×** | -8.8 | 1e-16 | 44/49 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.738×** | -6.0 | 1e-07 | 28/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.05 µM |  | **0.810×** | -4.5 | 3e-04 | 25/48 (HS-578T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.839× | -3.6 | 0.013 | 19/48 (RKO, LOX-IMVI, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.816×** | -3.1 | 0.077 | 12/48 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 92. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 75.8 | 10 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.110× (z -29.5) |
| [[HEC-1-A (line)]] | alt | 130 | 7 | 8 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.129× (z -29.0) |
| [[SW480 (line)]] | alt | 116 | 6 | 9 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.00× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.0921× (z -33.6) |
| [[KATO III (line)]] | alt | 80.9 | 8 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.120× (z -26.1) |
| [[NCI-H2347 (line)]] | alt | 102 | 3 | 10 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.7) | [[Panobinostat (drug)]] 0.5 µM 0.0892× (z -34.5) |
| [[HOP62 (line)]] | alt | 73.7 | 4 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.5× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.108× (z -28.5) |
| [[HS-578T (line)]] | alt | 79.0 | 6 | 6 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.7) | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -27.4) |
| [[NCI-H1573 (line)]] | alt | 78.5 | 6 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 30.5× (z +20.6) | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -29.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.155× (z -24.5) |
| [[RKO (line)]] | wt | 89.0 | 5 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +14.3) | [[Belinostat (drug)]] 5 µM 0.174× (z -19.3) |
| [[SNU-423 (line)]] | alt | 109 | 3 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.1× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.0546× (z -35.6) |
| [[C32 (line)]] | wt | 78.2 | 2 | 8 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 12.7× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.0792× (z -24.8) |
| [[LoVo (line)]] | wt | 48.8 | 5 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.109× (z -25.2) |
| [[LOX-IMVI (line)]] | wt | 53.8 | 3 | 7 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.30× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -24.0) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 2 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 26.9× (z +19.3) | [[Panobinostat (drug)]] 5 µM 0.0517× (z -37.7) |
| [[NCI-H2030 (line)]] | alt | 64.2 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +17.3) | [[Panobinostat (drug)]] 5 µM 0.119× (z -22.6) |
| [[A-172 (line)]] | wt | 74.0 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.147× (z -19.3) |
| [[A549 (line)]] | wt | 57.6 | 5 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -20.1) |
| [[AN3 CA (line)]] | alt | 231 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -17.9) |
| [[LS 180 (line)]] | wt | 56.2 | 4 | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +12.8) | [[Belinostat (drug)]] 5 µM 0.0764× (z -26.2) |
| [[NCI-H1792 (line)]] | alt | 104 | 2 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.3× (z +13.8) | [[Belinostat (drug)]] 5 µM 0.121× (z -23.9) |
| [[PANC-1 (line)]] | alt | 51.7 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.141× (z -22.0) |
| [[SW1417 (line)]] | alt | 81.3 | 2 | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.130× (z -24.5) |
| [[C-33 A (line)]] | alt | 147 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.73× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.0818× (z -26.9) |
| [[CFPAC-1 (line)]] | alt | 61.5 | 3 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.161× (z -20.8) |
| [[COLO 205 (line)]] | alt | 64.3 | 3 | 5 | [[TAK-901 (drug)]] 5 µM 22.0× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.113× (z -18.5) |
| [[Hs 766T (line)]] | wt | 80.9 | 2 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.8× (z +12.6) | [[Panobinostat (drug)]] 0.5 µM 0.0938× (z -24.8) |
| [[J82 (line)]] | alt | 92.8 | 1 | 7 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +14.2) | [[Panobinostat (drug)]] 0.5 µM 0.106× (z -28.7) |
| [[A-427 (line)]] | wt | 64.4 | 2 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.138× (z -19.4) |
| [[HT-29 (line)]] | alt | 71.6 | 1 | 6 | [[TAK-901 (drug)]] 5 µM 8.00× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.0828× (z -28.8) |
| [[SW48 (line)]] | wt | 92.1 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.57× (z +11.2) | [[Belinostat (drug)]] 5 µM 0.105× (z -18.4) |
| [[A498 (line)]] | wt | 55.5 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.192× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 52.2 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.1× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.0748× (z -25.9) |
| [[BT-474 (line)]] | alt | 93.8 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 42.3× (z +17.6) | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -17.4) |
| [[hTERT-HPNE (line)]] | wt | 51.4 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 18.9× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.118× (z -16.5) |
| [[Panc 03.27 (line)]] | alt | 69.5 | 2 | 4 | [[TAK-901 (drug)]] 5 µM 12.2× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.101× (z -22.4) |
| [[RPMI-7951 (line)]] | alt | 84.5 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.95× (z +8.7) | [[Panobinostat (drug)]] 5 µM 0.143× (z -19.1) |
| [[SK-MEL-2 (line)]] | alt | 58.1 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.115× (z -20.2) |
| [[H4 (line)]] | wt | 52.1 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.0507× (z -19.4) |
| [[HCT15 (line)]] | alt | 79.9 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.135× (z -17.6) |
| [[NCI-H23 (line)]] | alt | 62.9 | 1 | 4 | [[TAK-901 (drug)]] 5 µM 6.88× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.174× (z -17.3) |
| [[SW 900 (line)]] | alt | 53.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0943× (z -21.7) |
| [[SNU-1 (line)]] | wt | 99.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0878× (z -21.4) |
| [[CHP-212 (line)]] | wt | 61.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0993× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 44.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.118× (z -15.1) |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0449× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.121× (z -11.1) |
| [[SHP-77 (line)]] | alt | 37.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -15.9) |
| [[SW 1088 (line)]] | alt | 61.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0524× (z -9.5) |
| [[NCI-H2122 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 92), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INO80D]] | +0.80 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.76 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[ZNF747]] | +0.76 | +0.58 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZFY]] | +0.76 | +0.64 / +0.65 | both halves | 7e-06 | same gene group; STRING 726 |
| [[ZNF629]] | +0.75 | +0.66 / +0.61 | both halves | 7e-06 | same gene group |
| [[ZNF644]] | +0.74 | +0.73 / +0.65 | both halves | 7e-06 | same gene group |
| [[CREBBP]] | +0.73 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[WDR33]] | +0.72 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ATXN7]] | +0.72 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[WARS2-AS1]] | +0.72 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[LATS1]] | +0.72 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ZMYND11]] | +0.72 | +0.73 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F11R]] | -0.71 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[UBA6]] | -0.68 | -0.68 / -0.42 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.68 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[COG5]] | -0.67 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[GET1]] | -0.66 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.65 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[PCMT1]] | -0.65 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[RGS10]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[SGTB]] | -0.64 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[LPCAT2]] | -0.64 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[FCHO1]] | -0.64 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CIB1]] | -0.64 | -0.68 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF11A]] | B | TNFRSF11A activity lowers ZFX's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without TNFRSF11A | 0.023 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[NAALADL2]] | B | NAALADL2 activity lowers ZFX's level | lines that do not express NAALADL2 (11) vs lines expressing it (39) | 1.40× higher at baseline in the lines without NAALADL2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CA3, PCNX2, CA13 |
| [[GALNT12]] | B | GALNT12 activity raises ZFX's level | lines that do not express GALNT12 (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GALNT12 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF4, TUBA4A, ALS2CL |
| [[RADX]] | B | RADX activity lowers ZFX's level | lines that do not express RADX (14) vs lines expressing it (36) | 1.15× higher at baseline in the lines without RADX | 0.069 | ⚠ within organs, on part of the lines; also absent: RNF128 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZFX's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ZFX's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF827]] | C | ZNF827 activity lowers ZFX's level | lines that do not express ZNF827 (4) vs lines expressing it (46) | 1.49× higher at baseline in the lines without ZNF827 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, ITGA2-AS1, RND3; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.818). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (1.6, 9.2); signed map (19.5, -23.3). **Vector** length 124, 42.8% of its response variance represented; |z| ≥ 3 in 1,382 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chromatin organization* (reactome, mean cos +0.63 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.9 | +17.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.6 | +11.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.1 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +9.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.0 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.8 | +15.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.1 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | +0.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -8.9 | -16.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.8 | -23.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.7 | -39.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -14.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -9.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.6 | -8.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.4 | +0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.2 | -0.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein X-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:24,149,173-24,216,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF926 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZFX transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [P17010](https://www.uniprot.org/uniprotkb/P17010) (Zinc finger X-chromosomal protein):

> Probable transcriptional activator.

**Summary**, from NCBI Gene [7543](https://www.ncbi.nlm.nih.gov/gene/7543):

> This gene on the X chromosome is structurally similar to a related gene on the Y chromosome. It encodes a member of the krueppel C2H2-type zinc-finger protein family. The full-length protein contains an acidic transcriptional activation domain (AD), a nuclear localization sequence (NLS) and a DNA binding domain (DBD) consisting of 13 C2H2-type zinc fingers. Studies in mouse embryonic and adult hematopoietic stem cells showed that this gene was required as a transcriptional regulator for …

**Accessions** — [HGNC:12869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12869) · Entrez [7543](https://www.ncbi.nlm.nih.gov/gene/7543) · UniProt [P17010](https://www.uniprot.org/uniprotkb/P17010) · Ensembl [ENSG00000005889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005889)

## Data

Gene col 92: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 92); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 92, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 92]; `tensor/DDL_lfc|DDL_z.npy` [92]; `embed/gene_vectors.npy` [92]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 92 or target_col == 92). Every well: [[ZFX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
