---
symbol: "TFDP1"
type: "gene"
col: 12547
ensembl_id: "ENSG00000198176"
name: "transcription factor Dp-1"
location: "13q34"
module: 6
arm: "+"
pooled_cpm: 42.34
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TFDP1

*transcription factor Dp-1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.89× (z +24.5, q 0e+00, up in 39 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.46× (z +5.8, q 6e-07, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 5.52×, NCI-H1573 7.00×, SW480 4.81×, Panc 03.27 5.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 8.81×, NCI-H1573 9.12×, SW480 6.06×, Panc 03.27 6.87×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -21.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM3]] (+0.82, fdr 7e-06), [[RANBP1]] (+0.80, fdr 7e-06), [[MTHFD1]] (+0.80, fdr 7e-06); moves opposite to [[NKAP]] (-0.72, fdr 7e-06), [[TERF2IP]] (-0.72, fdr 7e-06), [[ZMYM5]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CELSR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12547.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (PANC-1 5.52×, NCI-H1573 7.00×, SW480 4.81×, Panc 03.27 5.59×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (A-427 8.81×, NCI-H1573 9.12×, SW480 6.06×, Panc 03.27 6.87×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.89×** | +24.5 | 0e+00 | 39/39 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +23.5 | 0e+00 | 45/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.22×** | +17.4 | 0e+00 | 42/44 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.54×** | +6.7 | 4e-09 | 27/45 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +6.3 | 3e-08 | 26/46 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +5.8 | 6e-07 | 29/48 (NCI-H2347, PANC-1, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +5.7 | 1e-06 | 29/48 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.30×** | +4.2 | 0.002 | 20/47 (SW480, HCT15, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.22×** | +3.2 | 0.079 | 12/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.083 | 11/46 (NCI-H460, J82, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.14× | +3.0 | 0.14 | 7/49 (SW480, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12547.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -21.5 | 0e+00 | 45/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.636×** | -10.3 | 3e-22 | 37/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -9.9 | 7e-21 | 39/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -8.9 | 8e-17 | 32/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.634×** | -6.9 | 6e-10 | 33/48 (LoVo, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.763×** | -6.1 | 8e-08 | 33/48 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.9 | 2e-07 | 25/48 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.726×** | -5.1 | 2e-05 | 26/48 (BT-474, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.733×** | -5.0 | 4e-05 | 27/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.638×** | -3.8 | 0.009 | 20/48 (SNU-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.802×** | -3.5 | 0.020 | 23/46 (BT-474, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.657×** | -3.5 | 0.020 | 19/41 (MIA PaCa-2, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.4 | 0.025 | 16/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.808×** | -3.4 | 0.025 | 15/48 (SW480, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.808×** | -3.4 | 0.025 | 20/48 (A-427, LS 180, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.036 | 14/48 (KATO III, HCT15, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -3.3 | 0.036 | 22/48 (KATO III, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12547. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 104 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.8) |
| [[KATO III (line)]] | alt | 60.3 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.4) |
| [[A-427 (line)]] | wt | 48.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 8.81× (z +18.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0789× (z -22.8) |
| [[MIA PaCa-2 (line)]] | alt | 35.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.2) |
| [[NCI-H460 (line)]] | wt | 29.3 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +13.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.5) |
| [[PANC-1 (line)]] | alt | 27.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +15.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.7) |
| [[SW480 (line)]] | alt | 58.9 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 6.06× (z +17.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -20.0) |
| [[A498 (line)]] | wt | 38.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -20.5) |
| [[A549 (line)]] | wt | 22.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.8) |
| [[HOP62 (line)]] | alt | 30.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.5) |
| [[HT-29 (line)]] | alt | 52.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.95× (z +15.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.6) |
| [[LoVo (line)]] | wt | 56.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 26.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.46× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.8) |
| [[LS 180 (line)]] | wt | 55.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.96× (z +11.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.1) |
| [[SNU-1 (line)]] | wt | 62.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.6) |
| [[SW1417 (line)]] | alt | 29.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -10.7) |
| [[A-172 (line)]] | wt | 57.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -17.4) |
| [[C32 (line)]] | wt | 33.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 16.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +11.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 20.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 14.9× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0524× (z -13.0) |
| [[Hs 766T (line)]] | wt | 50.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.07× (z +13.5) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 18.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.35× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 8.46× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 44.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.12× (z +17.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 22.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 35.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 56.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +16.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.78× (z +13.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.101× (z -13.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 19.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.66× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 27.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.88× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 40.5 | 0 | 2 | — | [[LJI308 (drug)]] 0.05 µM 0.0479× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 18.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.26× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -10.2) |
| [[J82 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 41.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +13.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.4) |
| [[SW48 (line)]] | wt | 79.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.5) |
| [[BT-474 (line)]] | alt | 47.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.7) |
| [[C-33 A (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +9.1) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 35.3 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0859× (z -10.4) |
| [[HCT15 (line)]] | alt | 70.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.6) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0865× (z -10.5) |
| [[SHP-77 (line)]] | alt | 70.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -16.1) |
| [[COLO 205 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12547), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3]] | +0.82 | +0.82 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 417 |
| [[RANBP1]] | +0.80 | +0.85 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[MTHFD1]] | +0.80 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[ICMT]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[POLA1]] | +0.77 | +0.76 / +0.77 | both halves | 7e-06 | pathway: E2F mediated regulation of DNA replication; STRING 555 |
| [[NUP155]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 |  |
| [[XRCC2]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[POLE]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |
| [[CAD]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[FANCA]] | +0.75 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[MCM4]] | +0.75 | +0.78 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 422 |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NKAP]] | -0.72 | -0.70 / -0.70 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.72 | -0.70 / -0.68 | both halves | 7e-06 | pathway: Cellular Senescence |
| [[ZMYM5]] | -0.71 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[SYF2]] | -0.70 | -0.70 / -0.68 | both halves | 7e-06 |  |
| [[RNF181]] | -0.70 | -0.60 / -0.76 | both halves | 7e-06 |  |
| [[ZKSCAN1]] | -0.69 | -0.65 / -0.65 | both halves | 7e-06 |  |
| [[EAPP]] | -0.68 | -0.68 / -0.66 | both halves | 7e-06 |  |
| [[ADPRM]] | -0.68 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.69 / -0.68 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[CIR1]] | -0.67 | -0.70 / -0.63 | both halves | 7e-06 |  |
| [[HMGCL]] | -0.67 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[MITD1]] | -0.67 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[RRAGC]] | -0.66 | -0.63 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises TFDP1's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without CELSR2 | 0.096 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[CDC45]] | C | CDC45 activity raises TFDP1's level | lines that do not express CDC45 (3) vs lines expressing it (47) | 2.41× lower at baseline in the lines without CDC45 | 0.092 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-29.8, -33.1); signed map (-32.9, -45.5). **Vector** length 124, 37.0% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.56 to 65); *DNA strand elongation* (reactome, mean cos +0.58 to 28); *DNA Replication* (reactome, mean cos +0.57 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +24.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +17.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +23.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.3 | +4.2 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.5 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.9 | -10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.3 | -21.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -8.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.8 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -9.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.6 | -1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.4 | -1.0 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -3.3 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor Dp-1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,584,721-113,641,473 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dp-1, DRTF1, DP1, DILC |
| Gene groups (HGNC) | Transcription factor Dp family; DREAM complex subunits |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 46 pathways, smallest: Activation of NOXA and translocation to mitochondria; Activation of PUMA and translocation to mitochondria; Inhibition of replication initiation of damaged DNA by RB1/E2F1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14186](https://www.uniprot.org/uniprotkb/Q14186) (Transcription factor Dp-1):

> Can stimulate E2F-dependent transcription. Binds DNA cooperatively with E2F family members through the E2 recognition site, 5'-TTTC[CG]CGC-3', found in the promoter region of a number of genes whose products are involved in cell cycle regulation or in DNA replication. The E2F1:DP complex appears to mediate both cell proliferation and apoptosis. Blocks adipocyte differentiation by repressing CEBPA binding to its target gene promoters.

**Summary**, from NCBI Gene [7027](https://www.ncbi.nlm.nih.gov/gene/7027):

> This gene encodes a member of a family of transcription factors that heterodimerize with E2F proteins to enhance their DNA-binding activity and promote transcription from E2F target genes. The encoded protein functions as part of this complex to control the transcriptional activity of numerous genes involved in cell cycle progression from G1 to S phase. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 1, 15, and X.[provided by …

**Accessions** — [HGNC:11749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11749) · Entrez [7027](https://www.ncbi.nlm.nih.gov/gene/7027) · UniProt [Q14186](https://www.uniprot.org/uniprotkb/Q14186) · Ensembl [ENSG00000198176](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198176)

## Data

Gene col 12547: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12547); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12547, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12547]; `tensor/DDL_lfc|DDL_z.npy` [12547]; `embed/gene_vectors.npy` [12547]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12547 or target_col == 12547). Every well: [[TFDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
