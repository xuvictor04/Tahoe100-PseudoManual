---
symbol: "CUL1"
type: "gene"
col: 621
ensembl_id: "ENSG00000055130"
name: "cullin 1"
location: "7q36.1"
module: 7
arm: "+"
pooled_cpm: 124.95
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CUL1

*cullin 1* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.46× (z +17.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.137× (z -56.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF3C4]] (+0.68, fdr 1e-05), [[ZFX]] (+0.68, fdr 1e-05), [[DNAJB12]] (+0.67, fdr 1e-05); moves opposite to [[NPTN]] (-0.58, fdr 3e-05), [[EFHC1]] (-0.58, fdr 1e-04), [[ARRB2]] (-0.58, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +17.0 | 0e+00 | 48/49 (SW480, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.67×** | +13.8 | 4e-41 | 44/48 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +12.2 | 4e-32 | 42/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +9.3 | 2e-18 | 34/48 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +6.5 | 9e-09 | 26/48 (NCI-H460, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +6.1 | 1e-07 | 25/48 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.2 | 1e-05 | 24/45 (HT-29, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +4.4 | 8e-04 | 19/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +4.4 | 8e-04 | 21/49 (NCI-H460, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.5 | 0.032 | 18/48 (CFPAC-1, A549, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.137×** | -56.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.151×** | -53.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.200×** | -45.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.456×** | -22.4 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.461×** | -21.5 | 0e+00 | 43/49 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -20.3 | 0e+00 | 39/44 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.530×** | -16.8 | 0e+00 | 38/45 (SNU-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.693×** | -14.8 | 0e+00 | 43/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -14.6 | 0e+00 | 44/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.530×** | -8.7 | 2e-16 | 42/49 (SW480, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.777×** | -7.2 | 3e-11 | 30/49 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.862× | -4.3 | 1e-03 | 12/48 (AsPC-1, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.904× | -4.1 | 0.002 | 13/48 (RKO, SK-MEL-2, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.5 | 0.016 | 8/49 (SW480, SNU-423, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.891× | -3.3 | 0.039 | 7/49 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.857× | -3.1 | 0.052 | 15/48 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.057 | 7/49 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.898× | -3.0 | 0.080 | 3/48 (HT-29, BT-474, …) | inconsistent across doses |  |
| [[Bendamustine (drug)]] 5 µM |  | 0.897× | -3.0 | 0.080 | 14/48 (SW 1088, BT-474, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 0.899× | -2.9 | 0.089 | 6/48 (SNU-423, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 162 | 6 (3 ⚠) | 11 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +15.0) | [[Panobinostat (drug)]] 0.5 µM 0.0804× (z -49.8) |
| [[NCI-H460 (line)]] | wt | 138 | 6 | 9 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.36× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.0961× (z -46.2) |
| [[C32 (line)]] | wt | 360 | 4 | 7 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 5.15× (z +13.1) | [[Panobinostat (drug)]] 5 µM 0.217× (z -25.5) |
| [[LoVo (line)]] | wt | 150 | 3 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.94× (z +12.7) | [[Panobinostat (drug)]] 5 µM 0.0997× (z -38.2) |
| [[LS 180 (line)]] | wt | 123 | 4 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.78× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.127× (z -31.1) |
| [[SNU-423 (line)]] | alt | 109 | 2 (1 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.24× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.122× (z -29.8) |
| [[LOX-IMVI (line)]] | wt | 85.1 | 2 | 8 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.36× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.123× (z -27.3) |
| [[A-172 (line)]] | wt | 100 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -30.2) |
| [[HOP62 (line)]] | alt | 107 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0845× (z -35.3) |
| [[HT-29 (line)]] | alt | 137 | 3 | 6 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.0795× (z -36.4) |
| [[SK-MEL-2 (line)]] | alt | 135 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.133× (z -27.1) |
| [[A498 (line)]] | wt | 160 | 1 | 7 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 1.84× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -33.5) |
| [[HEC-1-A (line)]] | alt | 97.9 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.175× (z -28.5) |
| [[HS-578T (line)]] | alt | 136 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -32.1) |
| [[MIA PaCa-2 (line)]] | alt | 177 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.59× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.0701× (z -39.5) |
| [[NCI-H23 (line)]] | alt | 150 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -27.8) |
| [[PANC-1 (line)]] | alt | 94.4 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.02× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -27.4) |
| [[SW1417 (line)]] | alt | 172 | 3 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.64× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -27.9) |
| [[SW48 (line)]] | wt | 173 | 1 | 7 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.60× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.0976× (z -25.7) |
| [[AsPC-1 (line)]] | alt | 125 | 1 | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.01× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.112× (z -29.1) |
| [[Hs 766T (line)]] | wt | 95.2 | 1 | 6 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.28× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -25.9) |
| [[hTERT-HPNE (line)]] | wt | 102 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -21.0) |
| [[J82 (line)]] | alt | 82.2 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -25.9) |
| [[NCI-H1573 (line)]] | alt | 62.1 | 3 | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.229× (z -19.2) |
| [[NCI-H1792 (line)]] | alt | 137 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.84× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -32.3) |
| [[RKO (line)]] | wt | 214 | 1 | 6 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.69× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.0892× (z -33.3) |
| [[A-427 (line)]] | wt | 99.2 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.97× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.177× (z -22.7) |
| [[A549 (line)]] | wt | 94.5 | 1 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +12.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -31.0) |
| [[BT-474 (line)]] | alt | 130 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.33× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -23.0) |
| [[KATO III (line)]] | alt | 156 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0749× (z -35.2) |
| [[NCI-H2030 (line)]] | alt | 107 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.26× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.279× (z -18.4) |
| [[SNU-1 (line)]] | wt | 141 | 1 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.02× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.0806× (z -26.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.167× (z -20.0) |
| [[SW 900 (line)]] | alt | 144 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -24.6) |
| [[AN3 CA (line)]] | alt | 213 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0457× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.148× (z -15.9) |
| [[C-33 A (line)]] | alt | 126 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.139× (z -23.0) |
| [[CHP-212 (line)]] | wt | 189 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0960× (z -15.9) |
| [[COLO 205 (line)]] | alt | 73.1 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 8.98× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.219× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 66.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +18.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -17.6) |
| [[H4 (line)]] | wt | 98.7 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.110× (z -21.3) |
| [[HCT15 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -22.6) |
| [[HepG2_C3A (line)]] | wt | 95.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -22.9) |
| [[NCI-H2347 (line)]] | alt | 84.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -27.4) |
| [[Panc 03.27 (line)]] | alt | 97.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0976× (z -27.3) |
| [[RPMI-7951 (line)]] | alt | 93.9 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -17.4) |
| [[SHP-77 (line)]] | alt | 78.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -19.2) |
| [[SW 1088 (line)]] | alt | 152 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0605× (z -13.2) |
| [[SW 1271 (line)]] | alt | 117 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0884× (z -13.0) |
| [[NCI-H661 (line)]] | alt | 93.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3C4]] | +0.68 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[ZFX]] | +0.68 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DNAJB12]] | +0.67 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.67 | +0.54 / +0.50 | both halves | 1e-05 | pathway: Neddylation |
| [[PRCC]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[KEAP1]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 918 |
| [[TLCD3A]] | +0.65 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[TSSC4]] | +0.65 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[DNAJB14]] | +0.65 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[ZNF689]] | +0.63 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[FIZ1]] | +0.63 | +0.52 / +0.37 | both halves | 8e-05 |  |
| [[USP7]] | +0.63 | +0.50 / +0.47 | both halves | 2e-05 | STRING 609 |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPTN]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EFHC1]] | -0.58 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[ARRB2]] | -0.58 | -0.34 / -0.44 | both halves | 1e-04 | pathway: Signaling by Hedgehog |
| [[SPAG9]] | -0.58 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[RGS9]] | -0.58 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[FCHO1]] | -0.56 | -0.32 / -0.37 | both halves | 2e-04 |  |
| [[F11R]] | -0.56 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[RFX2]] | -0.55 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[PJA2]] | -0.55 | -0.44 / -0.33 | both halves | 1e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[AHDC1]] | -0.54 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PIGH]] | -0.54 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CUL1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises CUL1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers CUL1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.9, 9.6); signed map (19.7, -23.2). **Vector** length 114, 35.3% of its response variance represented; |z| ≥ 3 in 1,300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.5 | +1.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.3 | +13.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.1 | +9.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.6 | +5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.5 | +12.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.1 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | -2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.9 | -22.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.3 | -45.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.3 | -8.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.1 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.6 | -0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | cullin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:148,697,914-148,801,110 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cullins; SCF complex core subunits |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING, G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 112 pathways, smallest: FBXW7 Mutants and NOTCH1 in Cancer; Loss of Function of FBXW7 in Cancer and NOTCH1 Signaling; Viral strategies to evade IFIT action |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13616](https://www.uniprot.org/uniprotkb/Q13616) (Cullin-1):

> Core component of multiple cullin-RING-based SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complexes, which mediate the ubiquitination of proteins involved in cell cycle progression, signal transduction and transcription. SCF complexes and ARIH1 collaborate in tandem to mediate ubiquitination of target proteins. In the SCF complex, serves as a rigid scaffold that organizes the SKP1-F-box protein and RBX1 subunits. May contribute to catalysis through positioning of the substrate and …

**Summary**, from NCBI Gene [8454](https://www.ncbi.nlm.nih.gov/gene/8454):

> Enables ubiquitin protein ligase binding activity. Contributes to ubiquitin ligase complex scaffold activity. Involved in several processes, including SCF-dependent proteasomal ubiquitin-dependent protein catabolic process; positive regulation of canonical NF-kappaB signal transduction; and protein K48-linked ubiquitination. Located in plasma membrane. Part of Parkin-FBXW7-Cul1 ubiquitin ligase complex and SCF ubiquitin ligase complex. Is active in nucleus. [provided by Alliance of Genome …

**Accessions** — [HGNC:2551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2551) · Entrez [8454](https://www.ncbi.nlm.nih.gov/gene/8454) · UniProt [Q13616](https://www.uniprot.org/uniprotkb/Q13616) · Ensembl [ENSG00000055130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055130)

## Data

Gene col 621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 621); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 621]; `tensor/DDL_lfc|DDL_z.npy` [621]; `embed/gene_vectors.npy` [621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 621 or target_col == 621). Every well: [[CUL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
