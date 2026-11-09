---
symbol: "CCT3"
type: "gene"
col: 8695
ensembl_id: "ENSG00000163468"
name: "chaperonin containing TCP1 subunit 3"
location: "1q22"
module: 60
arm: "+"
pooled_cpm: 104.15
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 1
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CCT3

*chaperonin containing TCP1 subunit 3* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +19.3, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.45× (z +12.9, q 1e-35, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.784× (z -5.0, q 4e-04, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.369×, SNU-1 0.375×, C-33 A 0.396×, NCI-H23 0.506×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.317×, A-427 0.422×; ⚠ cell-cycle shift, explains ~88% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.530×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT5]] (+0.90, fdr 7e-06), [[CCT6A]] (+0.87, fdr 7e-06), [[HSPD1]] (+0.84, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.72, fdr 7e-06), [[TERF2IP]] (-0.68, fdr 7e-06), [[YY1AP1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SEL1L3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8695.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.83×** | +19.3 | 0e+00 | 48/49 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.41×** | +16.9 | 0e+00 | 44/44 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.45×** | +12.9 | 1e-35 | 48/48 (A-172, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.41×** | +12.6 | 2e-34 | 48/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +12.1 | 2e-31 | 43/45 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.14×** | +11.0 | 6e-26 | 48/48 (C32, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.03×** | +9.6 | 5e-20 | 47/48 (A-172, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.83×** | +8.4 | 4e-15 | 42/47 (A-172, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.40×** | +6.6 | 3e-09 | 40/44 (NCI-H2347, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.3 | 2e-08 | 41/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **2.24×** | +6.1 | 7e-08 | 45/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.45×** | +5.3 | 4e-06 | 37/48 (A-172, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.44×** | +5.2 | 8e-06 | 31/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **1.41×** | +4.9 | 3e-05 | 40/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.40×** | +4.8 | 6e-05 | 30/48 (A-172, AsPC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.73×** | +4.1 | 0.001 | 35/48 (NCI-H460, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 31/48 (NCI-H1792, C32, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.66×** | +3.8 | 0.004 | 32/48 (CFPAC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.004 | 34/47 (NCI-H460, HOP62, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.63×** | +3.7 | 0.006 | 27/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +3.4 | 0.013 | 26/48 (AsPC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.016 | 25/49 (A-172, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.028 | 24/48 (SW 900, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.031 | 20/48 (A549, C-33 A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.032 | 21/47 (HOP62, SW 900, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8695.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-427 0.369×, SNU-1 0.375×, C-33 A 0.396×, NCI-H23 0.506×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SNU-1 0.317×, A-427 0.422×; ⚠ cell-cycle shift, explains ~88% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.530×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.784×** | -5.0 | 4e-04 | 28/48 (A-427, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Baicalin (drug)]] 5 µM |  | 0.850× | -3.3 | 0.27 | 14/49 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8695. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 117 | 10 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +12.9) | — |
| [[C32 (line)]] | wt | 80.8 | 8 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +12.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 117 | 7 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.85× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.7) |
| [[A-427 (line)]] | wt | 153 | 4 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.35× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 50.6 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.99× (z +10.8) | — |
| [[HOP62 (line)]] | alt | 56.2 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.95× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 73.2 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.45× (z +11.2) | — |
| [[LoVo (line)]] | wt | 96.5 | 5 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.46× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 99.6 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.63× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 94.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.66× (z +9.8) | — |
| [[A498 (line)]] | wt | 145 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.66× (z +17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 83.7 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 61.7 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +9.1) | — |
| [[NCI-H1792 (line)]] | alt | 65.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 62.9 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.68× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 121 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +19.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 62.9 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.87× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.11× (z +8.9) | — |
| [[SW480 (line)]] | alt | 107 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.36× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 49.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.36× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 75.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.54× (z +9.1) | — |
| [[KATO III (line)]] | alt | 64.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.79× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 70.4 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +10.4) | — |
| [[A549 (line)]] | wt | 92.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AsPC-1 (line)]] | alt | 61.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.96× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.8) |
| [[H4 (line)]] | wt | 56.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +8.6) | — |
| [[J82 (line)]] | alt | 95.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LOX-IMVI (line)]] | wt | 106 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 308 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 146 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 87.9 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.47× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 75.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.26× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 143 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.59× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 89.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.34× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 78.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.41× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 199 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 165 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.26× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 57.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 151 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.4) |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0815× (z -8.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8695), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT5]] | +0.90 | +0.92 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT6A]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[HSPD1]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 755 |
| [[CCT4]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT2]] | +0.79 | +0.76 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[TCP1]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSPA8]] | +0.76 | +0.72 / +0.74 | both halves | 7e-06 | STRING 880 |
| [[CCT7]] | +0.75 | +0.80 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[NUDC]] | +0.75 | +0.76 / +0.73 | both halves | 7e-06 | STRING 581 |
| [[PTGES3]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 936 |
| [[AHSA1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 | STRING 675 |
| [[STIP1]] | +0.74 | +0.72 / +0.74 | both halves | 7e-06 | STRING 976 |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.72 | -0.72 / -0.62 | both halves | 7e-06 | pathway: Cilium Assembly |
| [[TERF2IP]] | -0.68 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[YY1AP1]] | -0.64 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.63 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[POLR1H]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.62 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.61 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[MINDY2]] | -0.60 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[ACAP1]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEL1L3]] | B | SEL1L3 activity lowers CCT3's level | lines that do not express SEL1L3 (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without SEL1L3 | 0.062 | ⚠ within organs, on part of the lines; also absent: RDH10, JDP2 |
| [[PLAG1]] | B | PLAG1 activity lowers CCT3's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.43× higher at baseline in the lines without PLAG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |
| [[H2AJ]] | B | H2AJ activity lowers CCT3's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.33× higher at baseline in the lines without H2AJ | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.781). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.0, -12.0); signed map (-26.4, -29.6). **Vector** length 102, 38.7% of its response variance represented; |z| ≥ 3 in 1,234 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand* (reactome, mean cos +0.52 to 12); *mTORC1 signaling* (hallmark, mean cos +0.58 to 13); *AUF1 (hnRNP D0) binds and destabilizes mRNA* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +10.3 | +12.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.0 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.5 | +12.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.5 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +11.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | -0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.0 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.3 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.3 | +0.3 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.2 | +0.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,308,968-156,367,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cctg; previously TRIC5 |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P49368](https://www.uniprot.org/uniprotkb/P49368) (T-complex protein 1 subunit gamma):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [7203](https://www.ncbi.nlm.nih.gov/gene/7203):

> The protein encoded by this gene is a molecular chaperone that is a member of the chaperonin containing TCP1 complex (CCT), also known as the TCP1 ring complex (TRiC). This complex consists of two identical stacked rings, each containing eight different proteins. Unfolded polypeptides enter the central cavity of the complex and are folded in an ATP-dependent manner. The complex folds various proteins, including actin and tubulin. Alternate transcriptional splice variants have been characterized …

**Accessions** — [HGNC:1616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1616) · Entrez [7203](https://www.ncbi.nlm.nih.gov/gene/7203) · UniProt [P49368](https://www.uniprot.org/uniprotkb/P49368) · Ensembl [ENSG00000163468](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163468)

## Data

Gene col 8695: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8695); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8695, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8695]; `tensor/DDL_lfc|DDL_z.npy` [8695]; `embed/gene_vectors.npy` [8695]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8695 or target_col == 8695). Every well: [[CCT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
