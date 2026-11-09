---
symbol: "MYC"
type: "gene"
col: 5954
ensembl_id: "ENSG00000136997"
name: "MYC proto-oncogene, bHLH transcription factor"
location: "8q24.21"
module: 1
arm: "+"
pooled_cpm: 73.06
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MYC

*MYC proto-oncogene, bHLH transcription factor* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.50× (z +10.7, q 9e-24, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.249× (z -18.8, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BYSL]] (+0.72, fdr 7e-06), [[TWNK]] (+0.64, fdr 7e-06), [[DDX10]] (+0.63, fdr 7e-06); moves opposite to [[RAB6A]] (-0.55, fdr 4e-05), [[GPR107]] (-0.53, fdr 1e-04), [[SRP54-AS1]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.50×** | +10.7 | 9e-24 | 41/48 (PANC-1, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.94×** | +8.7 | 1e-15 | 26/47 (NCI-H1792, CFPAC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +8.6 | 2e-15 | 34/44 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +8.4 | 6e-15 | 33/47 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +8.3 | 9e-15 | 29/47 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +7.7 | 2e-12 | 31/46 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.64×** | +6.9 | 5e-10 | 26/46 (C-33 A, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +5.7 | 8e-07 | 28/47 (C32, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 1e-06 | 26/47 (PANC-1, NCI-H460, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.50×** | +5.5 | 2e-06 | 26/47 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.46×** | +5.1 | 1e-05 | 25/47 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +4.4 | 5e-04 | 25/46 (PANC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.33×** | +3.9 | 0.004 | 19/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.31×** | +3.7 | 0.010 | 23/45 (NCI-H460, A549, …) | two highest doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.043 | 19/46 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Rimonabant (drug)]] 5 µM |  | 1.18× | +3.2 | 0.045 | 11/47 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.045 | 16/47 (HT-29, LS 180, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.054 | 14/47 (LoVo, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.249×** | -18.8 | 0e+00 | 45/47 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.268×** | -17.8 | 0e+00 | 41/47 (LS 180, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.379×** | -13.1 | 4e-37 | 40/47 (LS 180, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.504×** | -13.1 | 5e-37 | 41/47 (MIA PaCa-2, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -8.5 | 1e-15 | 34/45 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -7.5 | 6e-12 | 29/40 (J82, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -7.1 | 8e-11 | 31/48 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.634×** | -6.2 | 5e-08 | 28/47 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.639×** | -6.1 | 9e-08 | 30/47 (LOX-IMVI, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.648×** | -5.9 | 3e-07 | 28/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.674×** | -5.1 | 2e-05 | 26/46 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.689×** | -4.8 | 6e-05 | 27/46 (COLO 205, HT-29, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -4.3 | 9e-04 | 4/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.569×** | -4.0 | 0.003 | 21/47 (SW48, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **0.737×** | -4.0 | 0.003 | 21/45 (SW480, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 206 | 5 (1 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.29× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 11.2× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -22.5) |
| [[SW48 (line)]] | wt | 164 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -22.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0472× (z -21.6) |
| [[NCI-H460 (line)]] | wt | 95.4 | 11 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 12.8× (z +19.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 3.76× (z +11.2) | — |
| [[A498 (line)]] | wt | 90.2 | 2 (2 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -16.0) |
| [[PANC-1 (line)]] | alt | 54.9 | 4 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.64× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 10.4× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.157× (z -17.4) |
| [[SW480 (line)]] | alt | 137 | 4 (1 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.94× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.226× (z -13.2) |
| [[LOX-IMVI (line)]] | wt | 155 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -16.5) |
| [[A549 (line)]] | wt | 64.4 | 5 (3 ⚠) | 2 | [[Harringtonine (drug)]] 0.5 µM 4.53× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -12.0) |
| [[LoVo (line)]] | wt | 62.0 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 64.7 | 4 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 5.24× (z +12.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.45× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.174× (z -12.6) |
| [[RKO (line)]] | wt | 172 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -24.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -18.3) |
| [[C-33 A (line)]] | alt | 78.5 | 1 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 13.7× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.0597× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.201× (z -10.5) |
| [[NCI-H23 (line)]] | alt | 78.3 | 2 (1 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.57× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -13.1) |
| [[SNU-1 (line)]] | wt | 85.2 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -14.3) |
| [[C32 (line)]] | wt | 26.5 | 1 (1 ⚠) | 4 | [[Niclosamide (olamine) (drug)]] 5 µM 4.80× (z +8.6) ⚠ toxic | [[Cobimetinib (drug)]] 0.5 µM 0.153× (z -10.6) |
| [[HOP62 (line)]] | alt | 28.1 | 2 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 4.35× (z +10.0) ⚠ cell-cycle shift, explains ~47% of this change | [[Panobinostat (drug)]] 5 µM 0.217× (z -10.4) |
| [[J82 (line)]] | alt | 68.4 | 2 (2 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.249× (z -12.5) |
| [[LS 180 (line)]] | wt | 71.8 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0345× (z -21.5) |
| [[SW1417 (line)]] | alt | 102 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -17.4) |
| [[A-172 (line)]] | wt | 18.4 | 4 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.51× (z +10.3) | — |
| [[CFPAC-1 (line)]] | alt | 62.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.57× (z +15.1) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[HS-578T (line)]] | alt | 47.7 | 1 (1 ⚠) | 3 | [[Harringtonine (drug)]] 5 µM 3.96× (z +8.6) ⚠ cell-cycle shift, explains ~34% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 46.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.223× (z -9.4) |
| [[COLO 205 (line)]] | alt | 50.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0878× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 49.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -16.0) |
| [[Hs 766T (line)]] | wt | 37.8 | 1 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +8.5) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.197× (z -9.5) |
| [[KATO III (line)]] | alt | 46.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 48.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.3× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 36.0 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 9.63× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -10.1) |
| [[BT-474 (line)]] | alt | 60.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -12.3) |
| [[hTERT-HPNE (line)]] | wt | 39.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.166× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 352 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.24× (z +14.5) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 7.73× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.33× (z +8.6) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 43.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.64× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 46.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.3) |
| [[AN3 CA (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BYSL]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[TWNK]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[DDX10]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RRS1]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 | STRING 428 |
| [[GRWD1]] | +0.61 | +0.67 / +0.58 | both halves | 8e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[HNRNPF]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 | STRING 403 |
| [[PPRC1]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 473 |
| [[MGA]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CASC19]] | +0.59 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[IRS1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 667 |
| [[UTP25]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[NOP16]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 551 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6A]] | -0.55 | -0.42 / -0.52 | both halves | 4e-05 | pathway: Signaling by NOTCH |
| [[GPR107]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[SRP54-AS1]] | -0.53 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[VDAC1P8]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[TULP3]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TMEM50B]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[APAF1]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 | STRING 527 |
| [[IFI27L1]] | -0.51 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[SEPTIN2]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[RAB18]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[HMCES]] | -0.50 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[MFSD8]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MYC's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.6, -37.7); signed map (-0.1, -44.8). **Vector** length 129, 42.3% of its response variance represented; |z| ≥ 3 in 1,419 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.8 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +6.0 | +5.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +10.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.7 | +5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.6 | +8.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +3.1 | +2.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.7 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.6 | -7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -7.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.8 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.3 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -4.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.9 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MYC proto-oncogene, bHLH transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.21 — chr8:127,735,434-127,742,951 (+) |
| Ensembl biotype | protein_coding |
| Also known as | c-Myc, bHLHe39, MYCC |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, MYC_TARGETS_V2, INFLAMMATORY_RESPONSE, UV_RESPONSE_DN, IL2_STAT5_SIGNALING, ESTROGEN_RESPONSE_EARLY, TNFA_SIGNALING_VIA_NFKB, G2M_CHECKPOINT, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 68 pathways, smallest: TFAP2 (AP-2) family regulates transcription of cell cycle factors; Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; RUNX3 regulates WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P01106](https://www.uniprot.org/uniprotkb/P01106) (Myc proto-oncogene protein):

> Transcription factor that binds DNA in a non-specific manner, yet also specifically recognizes the core sequence 5'-CAC[GA]TG-3'. Activates the transcription of growth-related genes. Binds to the VEGFA promoter, promoting VEGFA production and subsequent sprouting angiogenesis. Regulator of somatic reprogramming, controls self-renewal of embryonic stem cells (By similarity). Functions with TAF6L to activate target gene expression through RNA polymerase II pause release (By similarity). …

**Summary**, from NCBI Gene [4609](https://www.ncbi.nlm.nih.gov/gene/4609):

> This gene is a proto-oncogene and encodes a nuclear phosphoprotein that plays a role in cell cycle progression, apoptosis and cellular transformation. The encoded protein forms a heterodimer with the related transcription factor MAX. This complex binds to the E box DNA consensus sequence and regulates the transcription of specific target genes. Amplification of this gene is frequently observed in numerous human cancers. Translocations involving this gene are associated with Burkitt lymphoma and …

**Accessions** — [HGNC:7553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7553) · Entrez [4609](https://www.ncbi.nlm.nih.gov/gene/4609) · UniProt [P01106](https://www.uniprot.org/uniprotkb/P01106) · Ensembl [ENSG00000136997](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136997)

## Data

Gene col 5954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5954); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5954]; `tensor/DDL_lfc|DDL_z.npy` [5954]; `embed/gene_vectors.npy` [5954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5954 or target_col == 5954). Every well: [[MYC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
