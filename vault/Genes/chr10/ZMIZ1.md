---
symbol: "ZMIZ1"
type: "gene"
col: 2921
ensembl_id: "ENSG00000108175"
name: "zinc finger MIZ-type containing 1"
location: "10q22.3"
module: 154
arm: "+"
pooled_cpm: 183.61
n_lines_expressing: 46
n_dd_up: 3
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 13
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# ZMIZ1

*zinc finger MIZ-type containing 1* — 10q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.20× (z +4.7, q 0.002, up in 21 of 44 measured lines) ⚠ cell-cycle shift, explains ~3% of this change. The strongest without an alert is [[Fumaric acid (drug)]] 5 µM: 1.25× (z +3.9, q 0.023, up in 23 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (H4 3.34×, HS-578T 2.37×, HEC-1-A 2.33×, J82 2.07×, …; ⚠ cell-cycle shift, explains ~3% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1573 2.29×, LoVo 1.92×, SW48 2.33×, LS 180 1.76×; ⚠ cell-cycle shift, explains ~37% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.22×; ⚠ cell-cycle shift, explains ~54% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (H4 2.48×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.03×).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.297× (z -21.1, q 0e+00, down in 38 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.582× (z -9.7, q 2e-20, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDC42EP4]] (+0.63, fdr 1e-05), [[IFFO2]] (+0.62, fdr 1e-05), [[LFNG]] (+0.59, fdr 3e-05); moves opposite to [[MTREX]] (-0.51, fdr 4e-05), [[BTF3L4]] (-0.50, fdr 1e-04), [[SDHC]] (-0.49, fdr 9e-05).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAF]] → it (grade B ⚠); 13 go from it, the strongest it → [[FAM102A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2921.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (H4 3.34×, HS-578T 2.37×, HEC-1-A 2.33×, J82 2.07×, …; ⚠ cell-cycle shift, explains ~3% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (NCI-H1573 2.29×, LoVo 1.92×, SW48 2.33×, LS 180 1.76×; ⚠ cell-cycle shift, explains ~37% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 2.22×; ⚠ cell-cycle shift, explains ~54% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (H4 2.48×); [[Auranofin (drug)]] 5 µM in 1 line (SW480 2.03×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.20×** | +4.7 | 0.002 | 21/44 (H4, HS-578T, …) | top dose only | composition shift; position effect removed |
| [[Fumaric acid (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.023 | 23/45 (NCI-H2347, CFPAC-1, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.7 | 0.037 | 21/43 (H4, hTERT-HPNE, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.3 | 0.15 | 22/44 (SW48, LS 180, …) | rises with dose | composition shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.19× | +3.0 | 0.26 | 15/44 (A-172, HOP62, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2921.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.297×** | -21.1 | 0e+00 | 38/41 (SNU-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.347×** | -19.0 | 0e+00 | 40/45 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.378×** | -16.9 | 0e+00 | 43/43 (Hs 766T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.390×** | -15.7 | 0e+00 | 38/41 (LS 180, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.582×** | -9.7 | 2e-20 | 40/44 (CFPAC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.613×** | -8.8 | 1e-16 | 36/44 (A-172, SNU-423, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.654×** | -7.7 | 2e-12 | 31/44 (A-172, SNU-423, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.470×** | -7.1 | 8e-11 | 39/44 (MIA PaCa-2, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -7.0 | 2e-10 | 32/44 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.772×** | -6.6 | 2e-09 | 24/45 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.510×** | -6.3 | 1e-08 | 36/44 (SNU-423, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.513×** | -6.3 | 2e-08 | 34/44 (SNU-423, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.700×** | -6.2 | 3e-08 | 28/44 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.536×** | -5.9 | 2e-07 | 34/44 (SNU-423, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.745×** | -5.3 | 5e-06 | 25/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.747×** | -5.3 | 5e-06 | 28/44 (HOP62, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.747×** | -5.3 | 5e-06 | 30/44 (HOP62, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.815×** | -5.2 | 6e-06 | 22/44 (Panc 03.27, AN3 CA, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.625×** | -4.4 | 3e-04 | 28/43 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -4.4 | 3e-04 | 22/44 (A-172, AN3 CA, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.794×** | -4.1 | 8e-04 | 27/44 (H4, HOP62, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.656×** | -4.0 | 0.002 | 25/45 (HOP62, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.807×** | -3.7 | 0.004 | 22/45 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.817×** | -3.6 | 0.006 | 22/45 (HOP62, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2921. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 314 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.436× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 193 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.305× (z -11.1) |
| [[SNU-423 (line)]] | alt | 634 | 0 | 10 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -19.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.451× (z -9.0) |
| [[C32 (line)]] | wt | 329 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.341× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 265 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.240× (z -8.8) |
| [[A-172 (line)]] | wt | 367 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.541× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 281 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.312× (z -11.7) |
| [[LoVo (line)]] | wt | 131 | 1 (1 ⚠) | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.9) ⚠ cell-cycle shift, explains ~37% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.349× (z -12.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.249× (z -8.7) |
| [[LS 180 (line)]] | wt | 138 | 4 (4 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +9.8) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.149× (z -22.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 147 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.490× (z -9.0) |
| [[A549 (line)]] | wt | 207 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.213× (z -9.2) |
| [[H4 (line)]] | wt | 178 | 3 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +16.9) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.48× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.412× (z -8.7) |
| [[Hs 766T (line)]] | wt | 334 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -19.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 234 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.1) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 5 µM 0.235× (z -16.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 234 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.378× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 163 | 0 | 6 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0907× (z -13.2) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.531× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 190 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -13.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 439 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 217 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -12.5) ⚠ cell-cycle shift, explains ~3% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.377× (z -10.8) |
| [[SW 900 (line)]] | alt | 276 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.229× (z -15.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.414× (z -9.7) |
| [[A498 (line)]] | wt | 196 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +9.9) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 5 µM 0.204× (z -14.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 339 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -12.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 144 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +10.4) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -11.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 237 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -15.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.468× (z -9.2) |
| [[HT-29 (line)]] | alt | 221 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -14.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 180 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.379× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 115 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -13.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 135 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.301× (z -12.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 2 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.4) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.302× (z -9.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 144 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -21.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.8) ⚠ cell-cycle shift, explains ~3% of this change | [[Dinaciclib (drug)]] 5 µM 0.270× (z -13.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -12.5) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 59.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -15.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 219 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0715× (z -24.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 334 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 141 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.9) ⚠ cell-cycle shift, explains ~3% of this change | — |
| [[LOX-IMVI (line)]] | wt | 97.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 63.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW 1088 (line)]] | alt | 336 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -10.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.9 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 83.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2921), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42EP4]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[IFFO2]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[LFNG]] | +0.59 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[TLE3]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 | STRING 471 |
| [[VASN]] | +0.58 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[GRK5]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[HSPG2]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PIM1]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SSBP3]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[SLC6A6]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[FNBP1]] | +0.56 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[EML1]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTREX]] | -0.51 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[BTF3L4]] | -0.50 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[SDHC]] | -0.49 | -0.36 / -0.48 | both halves | 9e-05 |  |
| [[ARMC8]] | -0.49 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SMN2]] | -0.46 | -0.24 / -0.54 | both halves | 4e-04 |  |
| [[MRRF]] | -0.46 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[PIGB]] | -0.45 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PSMF1]] | -0.45 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[DNAJC24]] | -0.45 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PEX7]] | -0.44 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[DTWD1]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SHLD1]] | -0.44 | -0.32 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAF]] | B | MAF activity raises ZMIZ1's level | lines that do not express MAF (27) vs lines expressing it (23) | 1.88× lower at baseline in the lines without MAF | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFAIP6, PLPP4, FN1 |
| [[SHISAL1]] | B | SHISAL1 activity raises ZMIZ1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 1.74× lower at baseline in the lines without SHISAL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[TIMP3]] | B | TIMP3 activity raises ZMIZ1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 1.91× lower at baseline in the lines without TIMP3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1 |
| [[RRAD]] | B | RRAD activity raises ZMIZ1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without RRAD | 0.064 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[FAM102A]] | C | FAM102A activity raises ZMIZ1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without FAM102A | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM102A]] | C | ZMIZ1 activity raises FAM102A's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.61× lower at baseline in the lines without ZMIZ1 | 0.015 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[CDC42EP4]] | C | ZMIZ1 activity raises CDC42EP4's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without ZMIZ1 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[NDRG1]] | C | ZMIZ1 activity raises NDRG1's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 3.79× lower at baseline in the lines without ZMIZ1 | 0.024 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[SOX9]] | C | ZMIZ1 activity raises SOX9's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 5.88× lower at baseline in the lines without ZMIZ1 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[PDGFB]] | C | ZMIZ1 activity raises PDGFB's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 5.09× lower at baseline in the lines without ZMIZ1 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[CXXC5]] | C | ZMIZ1 activity raises CXXC5's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 4.28× lower at baseline in the lines without ZMIZ1 | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[TUBB2A]] | C | ZMIZ1 activity strengthens TUBB2A's drug response | lines that do not express ZMIZ1 (4) vs lines expressing it (44) | the lines without ZMIZ1 respond 0.76× as strongly (z diff +1.30); strongest at Homoharringtonine 5 µM: 2.77x vs 6.00x (z diff +3.9) | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[RND1]] | C | ZMIZ1 activity raises RND1's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without ZMIZ1 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[BTF3L4]] | C | ZMIZ1 activity lowers BTF3L4's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 1.43× higher at baseline in the lines without ZMIZ1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[TMEM209]] | C | ZMIZ1 activity lowers TMEM209's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ZMIZ1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| cells under [[Doxorubicin (hydrochloride) (drug)]] 5 µM | C | ZMIZ1 activity raises the cells' numbers under Doxorubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ZMIZ1 (4) vs lines expressing it (44) | the lines without ZMIZ1: 0.45× the cells of the other lines | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[LMNA]] | C | ZMIZ1 activity raises LMNA's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 2.06× lower at baseline in the lines without ZMIZ1 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.533). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.5, 32.5); signed map (-4.6, 27.6). **Vector** length 125, 42.0% of its response variance represented; |z| ≥ 3 in 1,604 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.3 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | +4.2 | +4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.8 | -0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +0.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -6.7 | -4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.0 | -9.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.6 | -7.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.0 | -5.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -6.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.6 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger MIZ-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.3 — chr10:79,068,966-79,316,519 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-519K18.1, KIAA1224, FLJ13541, hZIMP10, Zimp10, MIZ; previously RAI17 |
| Gene groups (HGNC) | Zinc fingers MIZ-type |
| Hallmark sets | ANDROGEN_RESPONSE, UV_RESPONSE_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9ULJ6](https://www.uniprot.org/uniprotkb/Q9ULJ6) (Zinc finger MIZ domain-containing protein 1):

> Acts as a transcriptional coactivator. Increases ligand-dependent transcriptional activity of AR and promotes AR sumoylation. The stimulation of AR activity is dependent upon sumoylation. Also functions as a transcriptional coactivator in the TGF-beta signaling pathway by increasing the activity of the SMAD3/SMAD4 transcriptional complex. Involved in transcriptional activation of a subset of NOTCH1 target genes including MYC. Involved in thymocyte and T cell development (By similarity). …

**Summary**, from NCBI Gene [57178](https://www.ncbi.nlm.nih.gov/gene/57178):

> This gene encodes a member of the PIAS (protein inhibitor of activated STAT) family of proteins. The encoded protein regulates the activity of various transcription factors, including the androgen receptor, Smad3/4, and p53. The encoded protein may also play a role in sumoylation. A translocation between this locus on chromosome 10 and the protein tyrosine kinase ABL1 locus on chromosome 9 has been associated with acute lymphoblastic leukemia. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:16493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16493) · Entrez [57178](https://www.ncbi.nlm.nih.gov/gene/57178) · UniProt [Q9ULJ6](https://www.uniprot.org/uniprotkb/Q9ULJ6) · Ensembl [ENSG00000108175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108175)

## Data

Gene col 2921: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2921); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2921, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2921]; `tensor/DDL_lfc|DDL_z.npy` [2921]; `embed/gene_vectors.npy` [2921]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2921 or target_col == 2921). Every well: [[ZMIZ1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZMIZ1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
