---
symbol: "TANGO6"
type: "gene"
col: 2311
ensembl_id: "ENSG00000103047"
name: "transport and golgi organization 6 homolog"
location: "16q22.1"
module: 4
arm: "+"
pooled_cpm: 51.81
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TANGO6

*transport and golgi organization 6 homolog* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.51× (z +7.1, q 9e-10, up in 24 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.23× (z +3.5, q 0.050, up in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 4.22×, SHP-77 6.54×, HEC-1-A 3.14×, CFPAC-1 4.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 3.71×, SHP-77 4.66×, SW 900 4.31×, CFPAC-1 3.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 3.12×, RPMI-7951 4.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 3.26×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.555× (z -15.0, q 0e+00, down in 39 of 47 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.347× (z -9.9, q 5e-21, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LARS2]] (+0.71, fdr 7e-06), [[POLR1A]] (+0.70, fdr 7e-06), [[NAA25]] (+0.68, fdr 7e-06); moves opposite to [[CDKN1B]] (-0.62, fdr 7e-06), [[LNX2]] (-0.61, fdr 1e-05), [[MMUT]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TTC28]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2311.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 6 lines (A498 4.22×, SHP-77 6.54×, HEC-1-A 3.14×, CFPAC-1 4.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 3.71×, SHP-77 4.66×, SW 900 4.31×, CFPAC-1 3.26×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A498 3.12×, RPMI-7951 4.60×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 3.26×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.1 | 9e-10 | 24/42 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +5.6 | 6e-06 | 25/47 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.24×** | +3.8 | 0.031 | 21/46 (A-427, HepG2/C3A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.48×** | +3.7 | 0.035 | 11/42 (CFPAC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.050 | 16/46 (NCI-H460, RPMI-7951, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.4 | 0.055 | 20/46 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.055 | 12/47 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.20×** | +3.3 | 0.064 | 11/46 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.10 | 13/46 (LoVo, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.555×** | -15.0 | 0e+00 | 39/47 (NCI-H460, HOP62, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.545×** | -10.5 | 2e-23 | 34/47 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.347×** | -9.9 | 5e-21 | 42/48 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -9.1 | 2e-17 | 35/47 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.598×** | -8.9 | 7e-17 | 32/46 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.647×** | -7.8 | 5e-13 | 28/47 (MIA PaCa-2, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.459×** | -7.3 | 2e-11 | 31/47 (HOP62, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.696×** | -6.5 | 5e-09 | 30/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -6.0 | 1e-07 | 27/47 (MIA PaCa-2, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.755×** | -4.9 | 7e-05 | 19/46 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.780×** | -4.5 | 4e-04 | 22/47 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.627×** | -4.4 | 6e-04 | 24/47 (MIA PaCa-2, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | **0.788×** | -4.3 | 8e-04 | 22/45 (NCI-H2030, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.652×** | -4.0 | 0.002 | 17/46 (H4, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.800×** | -4.0 | 0.002 | 21/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.809×** | -3.8 | 0.005 | 17/47 (NCI-H2030, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.006 | 19/47 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.808×** | -3.7 | 0.007 | 23/46 (SW 1271, SNU-1, …) | top dose only |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.026 | 11/47 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.840× | -3.1 | 0.048 | 15/47 (A498, KATO III, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 114 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -24.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 82.2 | 0 | 14 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -21.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.202× (z -10.1) |
| [[SW480 (line)]] | alt | 122 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.299× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.436× (z -10.6) |
| [[PANC-1 (line)]] | alt | 45.3 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.191× (z -10.7) |
| [[HOP62 (line)]] | alt | 42.6 | 1 (1 ⚠) | 7 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -20.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -9.3) |
| [[J82 (line)]] | alt | 38.2 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -17.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.175× (z -15.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.274× (z -12.2) |
| [[RKO (line)]] | wt | 93.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -12.8) |
| [[A498 (line)]] | wt | 71.5 | 3 (3 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.22× (z +15.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.0) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 76.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.302× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 56.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -11.3) |
| [[A549 (line)]] | wt | 67.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -17.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[CFPAC-1 (line)]] | alt | 20.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +8.5) | — |
| [[A-427 (line)]] | wt | 74.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.8) |
| [[C-33 A (line)]] | alt | 58.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -10.3) |
| [[C32 (line)]] | wt | 39.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -10.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -11.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 40.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.14× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -11.3) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SHP-77 (line)]] | alt | 42.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.54× (z +13.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 35.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.6) |
| [[KATO III (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.275× (z -11.0) ⚠ toxic |
| [[LoVo (line)]] | wt | 45.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -9.6) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.60× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SNU-1 (line)]] | wt | 54.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -9.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW 1271 (line)]] | alt | 52.7 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0693× (z -8.8) |
| [[SW 900 (line)]] | alt | 25.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -9.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARS2]] | +0.71 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[NAA25]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[WDR4]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZP3]] | +0.66 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.66 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PUS1]] | +0.66 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TSEN2]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[METTL8]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[CLPB]] | +0.65 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[LETM1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ERCC8]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN1B]] | -0.62 | -0.60 / -0.71 | both halves | 7e-06 |  |
| [[LNX2]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[MMUT]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[PJA2]] | -0.58 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[ARID4A]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ING1]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ILK]] | -0.57 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[RAB33B]] | -0.56 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[DBP]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[RAB11A]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[CCNG2]] | -0.55 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[MXI1]] | -0.55 | -0.45 / -0.59 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC28]] | B | TTC28 activity raises TANGO6's level | lines that do not express TTC28 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without TTC28 | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[LAMC3]] | B | LAMC3 activity raises TANGO6's level | lines that do not express LAMC3 (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without LAMC3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DLL3, ADD2, CNKSR2 |
| [[LDLRAD3]] | B | LDLRAD3 activity raises TANGO6's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 1.70× lower at baseline in the lines without LDLRAD3 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PARVB]] | B | PARVB activity raises TANGO6's level | lines that do not express PARVB (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.3, -34.4); signed map (-1.8, -49.7). **Vector** length 115, 31.8% of its response variance represented; |z| ≥ 3 in 991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.1 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +5.5 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +5.1 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~60% of this change | -4.8 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.3 | -9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.9 | -15.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -6.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -1.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -1.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.4 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | transport and golgi organization 6 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:68,843,531-69,085,182 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12688, KIAA1746; previously TMCO7 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Matched by | ensembl_id |

UniProt [Q9C0B7](https://www.uniprot.org/uniprotkb/Q9C0B7) carries no function annotation.

**Summary**, from NCBI Gene [79613](https://www.ncbi.nlm.nih.gov/gene/79613):

> Predicted to be involved in protein secretion. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25749) · Entrez [79613](https://www.ncbi.nlm.nih.gov/gene/79613) · UniProt [Q9C0B7](https://www.uniprot.org/uniprotkb/Q9C0B7) · Ensembl [ENSG00000103047](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103047)

## Data

Gene col 2311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2311); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2311]; `tensor/DDL_lfc|DDL_z.npy` [2311]; `embed/gene_vectors.npy` [2311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2311 or target_col == 2311). Every well: [[TANGO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TANGO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
