---
symbol: "TCOF1"
type: "gene"
col: 968
ensembl_id: "ENSG00000070814"
name: "treacle ribosome biogenesis factor 1"
location: "5q32-q33.1"
module: 18
arm: "+"
pooled_cpm: 66.81
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TCOF1

*treacle ribosome biogenesis factor 1* — 5q32-q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +15.8, q 0e+00, up in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.59× (z +6.0, q 2e-07, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.598× (z -9.4, q 2e-18, down in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.277×, A-427 0.298×, SW48 0.215×, RKO 0.310×, …); [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.326×, LS 180 0.310×; ⚠ cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.154×, A-427 0.313×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.324×, SW48 0.320×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DKC1]] (+0.82, fdr 7e-06), [[LETM1]] (+0.79, fdr 7e-06), [[MYBBP1A]] (+0.77, fdr 7e-06); moves opposite to [[NDUFV2-AS1]] (-0.69, fdr 7e-06), [[ZNF821]] (-0.68, fdr 7e-06), [[ZMYM5]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LAMC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 968.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.39×** | +15.8 | 0e+00 | 46/47 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.97×** | +13.6 | 1e-39 | 43/43 (SW480, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.34×** | +9.6 | 1e-19 | 43/45 (SNU-423, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +8.2 | 3e-14 | 46/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.71×** | +6.7 | 2e-09 | 40/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +6.0 | 2e-07 | 35/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.3 | 8e-06 | 34/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +4.9 | 5e-05 | 29/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.45×** | +4.9 | 7e-05 | 36/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +4.1 | 0.002 | 31/47 (NCI-H460, HOP62, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.0 | 0.004 | 29/48 (SW480, HCT15, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.005 | 30/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.008 | 29/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +3.7 | 0.008 | 32/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.32×** | +3.6 | 0.013 | 25/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.024 | 23/48 (A-172, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +3.3 | 0.024 | 26/48 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.041 | 24/48 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.047 | 18/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.56×** | +3.0 | 0.057 | 19/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +2.9 | 0.076 | 15/48 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.29×** | +2.9 | 0.077 | 19/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +2.8 | 0.099 | 15/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 968.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 13 lines (NCI-H23 0.277×, A-427 0.298×, SW48 0.215×, RKO 0.310×, …); [[Selinexor (drug)]] 5 µM in 2 lines (A498 0.326×, LS 180 0.310×; ⚠ cell-cycle shift, explains ~58% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.154×, A-427 0.313×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.324×, SW48 0.320×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -9.4 | 2e-18 | 33/48 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.702×** | -6.5 | 2e-08 | 33/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.816×** | -3.7 | 0.034 | 24/48 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.777× | -3.2 | 0.22 | 23/47 (HEC-1-A, AN3 CA, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.777× | -3.0 | 0.23 | 23/49 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 968. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 67.3 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 4 (4 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.2) |
| [[NCI-H460 (line)]] | wt | 62.7 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.6) |
| [[A498 (line)]] | wt | 89.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Selinexor (drug)]] 5 µM 0.326× (z -16.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[J82 (line)]] | alt | 99.3 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 35.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.48× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -8.9) |
| [[SW1417 (line)]] | alt | 92.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.449× (z -10.9) |
| [[SW480 (line)]] | alt | 77.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.66× (z +18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.5) |
| [[A-427 (line)]] | wt | 104 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -16.7) |
| [[HCT15 (line)]] | alt | 55.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.04× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -10.7) |
| [[HOP62 (line)]] | alt | 48.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 36.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.40× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 58.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 24.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.74× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 67.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 172 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -9.7) |
| [[SNU-423 (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.77× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW48 (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -16.1) |
| [[A549 (line)]] | wt | 60.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[H4 (line)]] | wt | 38.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.59× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 39.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Selinexor (drug)]] 5 µM 0.310× (z -11.3) ⚠ cell-cycle shift, explains ~58% of this change |
| [[NCI-H23 (line)]] | alt | 123 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 77.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.8) |
| [[BT-474 (line)]] | alt | 56.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.4) |
| [[C32 (line)]] | wt | 45.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Hs 766T (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.62× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RPMI-7951 (line)]] | alt | 65.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.3) |
| [[SW 900 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-172 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 968), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DKC1]] | +0.82 | +0.81 / +0.81 | both halves | 7e-06 | STRING 612 |
| [[LETM1]] | +0.79 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[TMEM201]] | +0.76 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[MDN1]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[PGAM5]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[URB2]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 | same gene group |
| [[NOM1]] | +0.74 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[BOP1]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[NOC2L]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV2-AS1]] | -0.69 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[ZNF821]] | -0.68 | -0.66 / -0.61 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.68 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[OSER1-DT]] | -0.67 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[ATOSA]] | -0.66 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[RNASEK]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[TERF2IP]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[RSRP1]] | -0.65 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ABCA5]] | -0.64 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[ZNF490]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[WBP1]] | -0.63 | -0.70 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMC3]] | B | LAMC3 activity raises TCOF1's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.44× lower at baseline in the lines without LAMC3 | 0.022 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[TERT]] | B | TERT activity raises TCOF1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.44× lower at baseline in the lines without TERT | 0.029 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[GNAZ]] | B | GNAZ activity raises TCOF1's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without GNAZ | 0.051 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[ADCY3]] | B | ADCY3 activity raises TCOF1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without ADCY3 | 0.053 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |
| [[LGALS3]] | B | LGALS3 activity lowers TCOF1's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.51× higher at baseline in the lines without LGALS3 | 0.073 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[GALNT14]] | B | GALNT14 activity lowers TCOF1's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.26× higher at baseline in the lines without GALNT14 | 0.087 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TSEN2]] | C | TSEN2 activity raises TCOF1's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 2.34× lower at baseline in the lines without TSEN2 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent |
| [[PPARGC1B]] | C | PPARGC1B activity raises TCOF1's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without PPARGC1B | 0.090 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.778). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.5, -37.7); signed map (-5.2, -51.2). **Vector** length 105, 36.0% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.57 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.8 | +8.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.2 | +6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.2 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -6.3 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -1.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | treacle ribosome biogenesis factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32-q33.1 — chr5:150,357,629-150,400,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | treacle, TCS |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Hallmark sets | MYC_TARGETS_V2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13428](https://www.uniprot.org/uniprotkb/Q13428) (Treacle protein):

> Nucleolar protein that acts as a regulator of RNA polymerase I by connecting RNA polymerase I with enzymes responsible for ribosomal processing and modification. Required for neural crest specification: following monoubiquitination by the BCR(KBTBD8) complex, associates with NOLC1 and acts as a platform to connect RNA polymerase I with enzymes responsible for ribosomal processing and modification, leading to remodel the translational program of differentiating cells in favor of neural crest …

**Summary**, from NCBI Gene [6949](https://www.ncbi.nlm.nih.gov/gene/6949):

> This gene encodes a nucleolar protein with a LIS1 homology domain. The protein is involved in ribosomal DNA gene transcription through its interaction with upstream binding factor (UBF). Mutations in this gene have been associated with Treacher Collins syndrome, a disorder which includes abnormal craniofacial development. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:11654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11654) · Entrez [6949](https://www.ncbi.nlm.nih.gov/gene/6949) · UniProt [Q13428](https://www.uniprot.org/uniprotkb/Q13428) · Ensembl [ENSG00000070814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070814)

## Data

Gene col 968: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 968); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 968, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 968]; `tensor/DDL_lfc|DDL_z.npy` [968]; `embed/gene_vectors.npy` [968]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 968 or target_col == 968). Every well: [[TCOF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCOF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
