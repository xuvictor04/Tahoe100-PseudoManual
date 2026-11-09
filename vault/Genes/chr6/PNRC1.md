---
symbol: "PNRC1"
type: "gene"
col: 7081
ensembl_id: "ENSG00000146278"
name: "proline rich nuclear receptor coactivator 1"
location: "6q15"
module: 74
arm: "+"
pooled_cpm: 154.22
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PNRC1

*proline rich nuclear receptor coactivator 1* — 6q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.20× (z +11.2, q 2e-26, up in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.74× (z +5.1, q 8e-05, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.288× (z -12.5, q 3e-33, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.265× (z -7.0, q 3e-10, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPD]] (+0.72, fdr 7e-06), [[KMT2A]] (+0.70, fdr 7e-06), [[KLHL24]] (+0.68, fdr 7e-06); moves opposite to [[RPSA]] (-0.65, fdr 1e-05), [[CHID1]] (-0.65, fdr 7e-06), [[MACROH2A1]] (-0.64, fdr 7e-06).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7081.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **2.20×** | +11.2 | 2e-26 | 39/48 (LoVo, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.57×** | +8.4 | 2e-14 | 40/48 (HS-578T, A498, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.1 | 8e-05 | 36/48 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +4.8 | 3e-04 | 39/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.49×** | +4.0 | 0.007 | 31/48 (C32, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.9 | 0.011 | 34/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.055 | 32/49 (Hs 766T, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.058 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.058 | 32/49 (NCI-H460, A549, …) | two highest doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 1.36× | +3.1 | 0.12 | 31/49 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7081.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.288×** | -12.5 | 3e-33 | 48/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.311×** | -10.4 | 1e-22 | 42/44 (SHP-77, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.415×** | -8.1 | 1e-13 | 43/49 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.455×** | -7.9 | 4e-13 | 47/48 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.265×** | -7.0 | 3e-10 | 47/48 (HCT15, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.530×** | -6.4 | 2e-08 | 44/48 (HepG2/C3A, LOX-IMVI, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.301×** | -6.3 | 2e-08 | 46/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.539×** | -6.2 | 4e-08 | 46/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.326×** | -5.9 | 2e-07 | 46/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.546×** | -5.6 | 1e-06 | 39/45 (Panc 03.27, A-427, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.399×** | -4.8 | 7e-05 | 42/48 (SW48, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.411×** | -4.7 | 1e-04 | 34/38 (HS-578T, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.452×** | -4.2 | 0.001 | 37/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.533×** | -3.3 | 0.033 | 32/48 (NCI-H2030, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **0.796×** | -3.3 | 0.043 | 32/48 (HEC-1-A, RKO, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.727×** | -3.0 | 0.085 | 27/47 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -3.0 | 0.085 | 27/49 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.78 per unit of S-phase module lfc, +0.77 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7081. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 413 | 1 (1 ⚠) | 7 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 3.15× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -13.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 176 | 1 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 161 | 4 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.3) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 6.44× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 159 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.08× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -15.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 175 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 250 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +11.3) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.232× (z -11.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 145 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +19.7) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 199 | 0 | 6 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.195× (z -14.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 161 | 1 | 5 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.37× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.146× (z -15.7) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.126× (z -8.8) |
| [[A-172 (line)]] | wt | 109 | 3 (2 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.80× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -11.6) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 126 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +18.5) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.48× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.219× (z -12.5) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 232 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +12.4) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 5 µM 0.309× (z -9.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A549 (line)]] | wt | 217 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.96× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -10.3) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 168 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +18.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.98× (z +9.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.261× (z -10.6) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 161 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.9) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -11.0) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 228 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +11.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.123× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 150 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +10.5) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 155 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -13.8) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 162 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +12.6) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.279× (z -11.6) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 189 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +8.9) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.192× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 191 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 167 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.0) ⚠ cell-cycle shift, explains ~52% of this change | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.1) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H2030 (line)]] | alt | 140 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.289× (z -10.9) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.170× (z -14.3) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 126 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -13.1) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 212 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +11.9) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.314× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 200 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.7) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -8.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 115 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 109 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.4) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -14.0) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.4) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[LS 180 (line)]] | wt | 143 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +12.9) ⚠ cell-cycle shift, explains ~52% of this change | [[Dinaciclib (drug)]] 5 µM 0.215× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.9) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.265× (z -12.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 88.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.46× (z +9.1) ⚠ toxic | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -10.6) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 114 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 91.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.1) ⚠ cell-cycle shift, explains ~52% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -9.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 96.0 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -13.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +12.2) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[C-33 A (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -9.6) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 186 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -12.1) ⚠ unreliable plate only |
| [[COLO 205 (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +11.9) ⚠ cell-cycle shift, explains ~52% of this change | — |
| [[H4 (line)]] | wt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 159 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -8.6) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -13.4) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 359 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7081), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPD]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KMT2A]] | +0.70 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 445 |
| [[RSF1]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[SIRT1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[THAP1]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CEP350]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[TXNIP]] | +0.66 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ANKRD12]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[REST]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.64 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | -0.65 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[CHID1]] | -0.65 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[MACROH2A1]] | -0.64 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.64 | -0.58 / -0.65 | both halves | 7e-06 |  |
| [[GCN1]] | -0.63 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[NOC2L]] | -0.63 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[RNPS1]] | -0.63 | -0.57 / -0.63 | both halves | 9e-06 |  |
| [[NSUN2]] | -0.62 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[URB1]] | -0.62 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[NUP205]] | -0.61 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[EMC1]] | -0.61 | -0.46 / -0.67 | both halves | 2e-05 |  |
| [[TFDP1]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.8, -44.8); signed map (-7.3, 10.4). **Vector** length 173, 68.9% of its response variance represented; |z| ≥ 3 in 1,369 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +9.2 | +11.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +8.9 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +5.9 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.7 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.5 | +3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +5.5 | +1.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.1 | -12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -12.3 | -10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -11.6 | -8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -11.1 | -5.6 |
|  | [[EX229 (drug)]] 5 µM |  | -9.6 | -6.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.8 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.6 | -5.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.7 | -3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | proline rich nuclear receptor coactivator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q15 — chr6:89,080,751-89,085,160 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B4-2, PRR2; previously PROL2 |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12796](https://www.uniprot.org/uniprotkb/Q12796) (Proline-rich nuclear receptor coactivator 1):

> Nuclear receptor coactivator. May play a role in signal transduction.

**Summary**, from NCBI Gene [10957](https://www.ncbi.nlm.nih.gov/gene/10957):

> Predicted to be involved in DNA-templated transcription and mRNA metabolic process. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17278) · Entrez [10957](https://www.ncbi.nlm.nih.gov/gene/10957) · UniProt [Q12796](https://www.uniprot.org/uniprotkb/Q12796) · Ensembl [ENSG00000146278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146278)

## Data

Gene col 7081: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7081); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7081, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7081]; `tensor/DDL_lfc|DDL_z.npy` [7081]; `embed/gene_vectors.npy` [7081]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7081 or target_col == 7081). Every well: [[PNRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
