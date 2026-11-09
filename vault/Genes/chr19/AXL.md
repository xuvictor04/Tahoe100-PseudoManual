---
symbol: "AXL"
type: "gene"
col: 9497
ensembl_id: "ENSG00000167601"
name: "AXL receptor tyrosine kinase"
location: "19q13.2"
module: 116
arm: "+"
pooled_cpm: 137.87
n_lines_expressing: 36
n_dd_up: 11
n_dd_down: 47
n_dd_up_clean: 2
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# AXL

*AXL receptor tyrosine kinase* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.25× (z +14.5, q 4e-45, up in 26 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.20× (z +4.8, q 1e-04, up in 15 of 34 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CFPAC-1 3.49×, A-172 2.79×, A549 3.46×, Panc 03.27 2.93×, …; ⚠ cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (CFPAC-1 3.24×, Panc 03.27 3.94×, HS-578T 3.37×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 4.27×, HS-578T 3.59×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 2.63×, A-172 1.86×); [[PH-797804 (drug)]] 5 µM in 1 line (RPMI-7951 5.36×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SW480 1.76×).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.261× (z -25.1, q 0e+00, down in 33 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LTBP2]] (+0.65, fdr 7e-06), [[PHF19]] (+0.63, fdr 1e-05), [[RGS20]] (+0.62, fdr 7e-06); moves opposite to [[NDUFAF7]] (-0.61, fdr 1e-05), [[ARMH3]] (-0.58, fdr 1e-05), [[MRPL34]] (-0.56, fdr 1e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[PGM5P2-1]] → it (grade B ⚠); 18 go from it, the strongest it → [[PARVA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9497.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (CFPAC-1 3.49×, A-172 2.79×, A549 3.46×, Panc 03.27 2.93×, …; ⚠ cell-cycle shift, explains ~74% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (CFPAC-1 3.24×, Panc 03.27 3.94×, HS-578T 3.37×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (Panc 03.27 4.27×, HS-578T 3.59×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.05 µM in 2 lines (NCI-H460 2.63×, A-172 1.86×); [[PH-797804 (drug)]] 5 µM in 1 line (RPMI-7951 5.36×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (SW480 1.76×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +14.5 | 4e-45 | 26/30 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.72×** | +14.3 | 1e-43 | 25/34 (CFPAC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +13.8 | 8e-41 | 31/35 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.62×** | +8.6 | 8e-16 | 25/34 (A-172, NCI-H1792, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +7.1 | 2e-10 | 24/32 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.45×** | +7.0 | 3e-10 | 22/34 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.74×** | +5.4 | 5e-06 | 22/35 (RPMI-7951, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.8 | 1e-04 | 15/34 (SW 900, SNU-423, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.002 | 14/35 (SW480, SW 900, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.22×** | +3.7 | 0.011 | 17/34 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.012 | 15/34 (RPMI-7951, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.014 | 15/34 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.015 | 5/34 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.21×** | +3.5 | 0.019 | 13/33 (SW480, SW 900, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.069 | 15/33 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.069 | 13/33 (SW480, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.085 | 15/34 (SW480, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 68 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9497.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.261×** | -25.1 | 0e+00 | 33/34 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.288×** | -23.2 | 0e+00 | 33/34 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.348×** | -19.7 | 0e+00 | 33/34 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.424×** | -16.0 | 0e+00 | 30/34 (HOP62, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.342×** | -15.8 | 0e+00 | 32/34 (HOP62, RKO, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.464×** | -14.3 | 1e-44 | 31/34 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.600×** | -13.4 | 3e-39 | 29/34 (RKO, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.507×** | -12.7 | 6e-35 | 32/34 (HOP62, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.318×** | -11.2 | 4e-27 | 27/31 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.568×** | -10.5 | 3e-24 | 30/34 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.373×** | -9.6 | 3e-20 | 33/34 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.396×** | -9.0 | 8e-18 | 31/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.401×** | -8.9 | 2e-17 | 31/34 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.728×** | -8.4 | 3e-15 | 20/35 (MIA PaCa-2, A549, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.441×** | -8.0 | 6e-14 | 29/34 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.485×** | -7.1 | 5e-11 | 26/34 (NCI-H460, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.694×** | -6.8 | 3e-10 | 26/34 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -6.5 | 3e-09 | 23/34 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.534×** | -6.1 | 2e-08 | 25/35 (A549, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | **0.743×** | -5.5 | 8e-07 | 22/34 (HOP62, A498, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9497. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 462 | 1 (1 ⚠) | 15 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.44× (z +11.6) ⚠ cell-cycle shift, explains ~63% of this change | [[Panobinostat (drug)]] 5 µM 0.124× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 89.6 | 2 (1 ⚠) | 14 (2 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.63× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.0918× (z -28.0) |
| [[A549 (line)]] | wt | 497 | 4 (4 ⚠) | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +21.5) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.141× (z -23.9) |
| [[A-172 (line)]] | wt | 254 | 5 (4 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +22.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 1.86× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.252× (z -21.5) |
| [[PANC-1 (line)]] | alt | 193 | 4 (4 ⚠) | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.4) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.261× (z -18.4) |
| [[RKO (line)]] | wt | 203 | 0 | 12 (6 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.144× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 242 | 5 (4 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +14.7) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.36× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -14.2) |
| [[J82 (line)]] | alt | 259 | 2 (2 ⚠) | 9 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.65× (z +9.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.213× (z -16.2) |
| [[SW480 (line)]] | alt | 80.5 | 3 (2 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +9.8) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.76× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -22.7) |
| [[hTERT-HPNE (line)]] | wt | 217 | 2 (2 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.4) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.201× (z -14.1) |
| [[Panc 03.27 (line)]] | alt | 169 | 4 (4 ⚠) | 6 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +16.9) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -15.9) |
| [[SW 900 (line)]] | alt | 116 | 5 (5 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +12.7) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.293× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 232 | 6 (6 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +23.1) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -17.9) |
| [[H4 (line)]] | wt | 197 | 3 (3 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.25× (z +10.4) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.254× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.241× (z -10.3) |
| [[SNU-423 (line)]] | alt | 154 | 3 (3 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +16.3) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.237× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 285 | 0 | 8 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.439× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.320× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 106 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +8.9) ⚠ cell-cycle shift, explains ~63% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -17.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.194× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 153 | 1 (1 ⚠) | 7 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.75× (z +14.3) ⚠ cell-cycle shift, explains ~63% of this change | [[Panobinostat (drug)]] 5 µM 0.252× (z -15.4) |
| [[HS-578T (line)]] | alt | 301 | 4 (4 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +14.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.430× (z -10.0) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.369× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 205 | 0 | 7 (2 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.186× (z -14.1) |
| [[A498 (line)]] | wt | 131 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +14.6) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.353× (z -10.1) |
| [[Hs 766T (line)]] | wt | 109 | 1 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 5 µM 0.180× (z -16.8) |
| [[SW1417 (line)]] | alt | 57.9 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 48.5 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.6) ⚠ cell-cycle shift, explains ~74% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0683× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.121× (z -19.6) |
| [[AsPC-1 (line)]] | alt | 158 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -21.1) |
| [[C32 (line)]] | wt | 38.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.114× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 68.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 41.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0939× (z -12.6) |
| [[SW 1271 (line)]] | alt | 186 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -9.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.173× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 169 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.448× (z -8.6) |
| [[A-427 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9497), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBP2]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PHF19]] | +0.63 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[RGS20]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[EGFR]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 | STRING 792 |
| [[FRMD6]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MYO1C]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ETS1]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[AP1B1]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[DDAH1]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CTNNAL1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.58 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[HNRNPUL1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 | ⚠ same locus (0.7 kb, same strand: neighbours can correlate without regulation) |
| [[OXTR]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.61 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ARMH3]] | -0.58 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[MRPL34]] | -0.56 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CDC42SE2]] | -0.55 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MAPKAPK5-AS1]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[IQSEC2]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[MKRN2]] | -0.52 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[INTS10]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[RNF149]] | -0.51 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[MCU]] | -0.50 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[CLPP]] | -0.50 | -0.40 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGM5P2-1]] | B | PGM5P2-1 activity raises AXL's level | lines that do not express PGM5P2-1 (12) vs lines expressing it (38) | 5.14× lower at baseline in the lines without PGM5P2-1 | 0.008 | ⚠ within organs, on part of the lines; also absent: PGM5P2, MAMLD1, HRH1; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises AXL's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 5.11× lower at baseline in the lines without MYBL1 | 0.058 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[PARVA]] | B | PARVA activity raises AXL's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.75× lower at baseline in the lines without PARVA | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[ZNF462]] | B | ZNF462 activity raises AXL's level | lines that do not express ZNF462 (5) vs lines expressing it (45) | 1.90× lower at baseline in the lines without ZNF462 | 0.097 | ⚠ within organs, on part of the lines; also absent: PDE11A, ENSG00000214803 |
| [[FRMD4A]] | C | FRMD4A activity raises AXL's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 5.50× lower at baseline in the lines without FRMD4A | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[ETS1]] | C | ETS1 activity raises AXL's level | lines that do not express ETS1 (11) vs lines expressing it (39) | 8.51× lower at baseline in the lines without ETS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: AXL, ENSG00000289526, PRSS23; co-absent with the target |
| [[LTBP2]] | C | LTBP2 activity raises AXL's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 7.13× lower at baseline in the lines without LTBP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526; co-absent with the target |
| [[PRSS23]] | C | PRSS23 activity raises AXL's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 5.17× lower at baseline in the lines without PRSS23 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent; co-absent with the target |
| [[LINC00973]] | C | LINC00973 activity raises AXL's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 4.19× lower at baseline in the lines without LINC00973 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1; co-absent with the target |
| [[COL4A2]] | C | COL4A2 activity raises AXL's level | lines that do not express COL4A2 (25) vs lines expressing it (25) | 4.31× lower at baseline in the lines without COL4A2 | 0.093 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, ROR1-AS1; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 12, C 6. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARVA]] | B | AXL activity raises PARVA's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.66× lower at baseline in the lines without AXL | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MSANTD3]] | B | AXL activity raises MSANTD3's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.64× lower at baseline in the lines without AXL | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[PTPN14]] | B | AXL activity raises PTPN14's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without AXL | 0.014 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[TSPAN4]] | B | AXL activity raises TSPAN4's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without AXL | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[CCDC50]] | B | AXL activity raises CCDC50's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.46× lower at baseline in the lines without AXL | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[CTNNAL1]] | B | AXL activity raises CTNNAL1's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without AXL | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MSANTD3-TMEFF1]] | B | AXL activity raises MSANTD3-TMEFF1's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without AXL | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[FMNL3]] | B | AXL activity raises FMNL3's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.81× lower at baseline in the lines without AXL | 0.063 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[MKRN2]] | B | AXL activity raises MKRN2's level | lines that do not express AXL (14) vs lines expressing it (36) | 1.17× lower at baseline in the lines without AXL | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[DCBLD2]] | B | AXL activity raises DCBLD2's level | lines that do not express AXL (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without AXL | 0.089 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[CAVIN1]] | B | AXL activity raises CAVIN1's level | lines that do not express AXL (14) vs lines expressing it (36) | 3.66× lower at baseline in the lines without AXL | 0.097 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| cells under [[Erdafitinib (drug)]] 5 µM | B | AXL activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express AXL (14) vs lines expressing it (34) | the lines without AXL: 1.19× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.1, 13.1); signed map (-4.5, 34.8). **Vector** length 137, 45.5% of its response variance represented; |z| ≥ 3 in 1,513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +11.6 | +14.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +9.1 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +9.1 | +7.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +14.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.8 | +3.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.2 | -14.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.7 | -16.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -8.6 | -15.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -7.8 | -13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -7.6 | -12.7 |
|  | [[EX229 (drug)]] 5 µM |  | -7.5 | -9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.9 | -8.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.7 | -8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.2 | -9.6 |

## What is on record

|  |  |
|---|---|
| Name | AXL receptor tyrosine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:41,219,223-41,261,766 (+) |
| Ensembl biotype | protein_coding |
| Also known as | UFO, JTK11, Tyro7, ARK |
| Gene groups (HGNC) | Fibronectin type III domain containing; V-set domain containing; AXL receptor tyrosine kinase family |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 6 pathways, smallest: Dengue Virus Attachment and Entry; VEGFA-VEGFR2 Pathway; Signaling by VEGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P30530](https://www.uniprot.org/uniprotkb/P30530) (Tyrosine-protein kinase receptor UFO):

> Receptor tyrosine kinase that transduces signals from the extracellular matrix into the cytoplasm by binding growth factors GAS6 and PROS1, and which is thus regulating many physiological processes including cell survival, cell proliferation, migration and differentiation. Ligand binding at the cell surface induces dimerization and autophosphorylation of AXL. Following activation by ligand, AXL binds and induces tyrosine phosphorylation of PI3-kinase subunits PIK3R1, PIK3R2 and PIK3R3; but also …

**Summary**, from NCBI Gene [558](https://www.ncbi.nlm.nih.gov/gene/558):

> The protein encoded by this gene is a member of the Tyro3-Axl-Mer (TAM) receptor tyrosine kinase subfamily. The encoded protein possesses an extracellular domain which is composed of two immunoglobulin-like motifs at the N-terminal, followed by two fibronectin type-III motifs. It transduces signals from the extracellular matrix into the cytoplasm by binding to the vitamin K-dependent protein growth arrest-specific 6 (Gas6). This gene may be involved in several cellular functions including …

**Accessions** — [HGNC:905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:905) · Entrez [558](https://www.ncbi.nlm.nih.gov/gene/558) · UniProt [P30530](https://www.uniprot.org/uniprotkb/P30530) · Ensembl [ENSG00000167601](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167601)

## Data

Gene col 9497: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9497); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9497, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9497]; `tensor/DDL_lfc|DDL_z.npy` [9497]; `embed/gene_vectors.npy` [9497]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9497 or target_col == 9497). Every well: [[AXL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AXL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
