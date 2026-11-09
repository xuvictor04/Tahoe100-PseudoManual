---
symbol: "GTF2B"
type: "gene"
col: 6097
ensembl_id: "ENSG00000137947"
name: "general transcription factor IIB"
location: "1p22.2"
module: 93
arm: "+"
pooled_cpm: 81.27
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# GTF2B

*general transcription factor IIB* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.07× (z +23.0, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.244× (z -15.7, q 0e+00, down in 41 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.609× (z -5.5, q 5e-06, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (AsPC-1 0.106×, SK-MEL-2 0.115×, HS-578T 0.109×, NCI-H2347 0.131×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0938×, A-427 0.0628×, RKO 0.0808×, CFPAC-1 0.159×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.156×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM53C]] (+0.85, fdr 7e-06), [[POLR2A]] (+0.76, fdr 7e-06), [[SPTY2D1]] (+0.69, fdr 7e-06); moves opposite to [[TMEM33]] (-0.64, fdr 1e-05), [[ZC3H14]] (-0.62, fdr 3e-05), [[LARP1]] (-0.62, fdr 1e-05).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.07×** | +23.0 | 0e+00 | 48/49 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +12.0 | 1e-30 | 44/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +7.9 | 5e-13 | 45/50 (SK-MEL-2, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.84×** | +7.1 | 2e-10 | 42/48 (SW480, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.66×** | +5.9 | 5e-07 | 40/48 (NCI-H23, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.7 | 1e-06 | 39/48 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +5.4 | 6e-06 | 36/48 (AsPC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.55×** | +5.1 | 3e-05 | 30/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 3e-05 | 37/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +4.7 | 1e-04 | 35/48 (AsPC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +4.5 | 3e-04 | 32/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.003 | 31/48 (A-172, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.051 | 20/48 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.051 | 24/49 (MIA PaCa-2, J82, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.051 | 21/48 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6097.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (AsPC-1 0.106×, SK-MEL-2 0.115×, HS-578T 0.109×, NCI-H2347 0.131×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H2347 0.0938×, A-427 0.0628×, RKO 0.0808×, CFPAC-1 0.159×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.156×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.244×** | -15.7 | 0e+00 | 41/42 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.281×** | -14.7 | 0e+00 | 47/49 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.381×** | -10.3 | 9e-23 | 39/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.609×** | -5.5 | 5e-06 | 34/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.699×** | -4.1 | 0.004 | 33/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.830× | -3.1 | 0.21 | 18/48 (H4, LoVo, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.772× | -3.0 | 0.22 | 26/48 (SW 1271, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 63.0 | 6 (3 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -16.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 111 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.106× (z -21.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.7 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +18.8) | — |
| [[A-427 (line)]] | wt | 80.7 | 3 (2 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.67× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0628× (z -22.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 140 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -17.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 83.0 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.08× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.109× (z -18.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 80.0 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.197× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 109 | 1 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +14.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -22.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 124 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 90.9 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.171× (z -15.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 80.3 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -19.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 109 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -17.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -16.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 70.4 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -11.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 93.4 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.09× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -13.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 96.1 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 77.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -15.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 73.3 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -11.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 87.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 89.0 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.0803× (z -17.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 90.6 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.50× (z +21.0) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 70.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.83× (z +15.8) | — |
| [[NCI-H2030 (line)]] | alt | 79.2 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +13.9) | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 62.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.48× (z +17.3) | — |
| [[NCI-H460 (line)]] | wt | 50.4 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +20.0) | — |
| [[RPMI-7951 (line)]] | alt | 75.1 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -9.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 39.5 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.27× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 89.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.223× (z -10.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 52.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.23× (z +15.5) | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 108 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 84.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +16.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 80.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -15.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +15.0) | — |
| [[C32 (line)]] | wt | 120 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 67.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 59.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 87.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +13.8) | — |
| [[AN3 CA (line)]] | alt | 68.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +12.9) | — |
| [[NCI-H661 (line)]] | alt | 65.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.6) | — |
| [[SHP-77 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 51.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.49× (z +16.2) | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0711× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 72.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 86.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM53C]] | +0.85 | +0.81 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[POLR2A]] | +0.76 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 999 |
| [[SPTY2D1]] | +0.69 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[POR]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[DALRD3]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.67 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[RAB5A]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[STX5-DT]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[INTS6L]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[DPM1]] | +0.67 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[SLC9A1]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM33]] | -0.64 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[ZC3H14]] | -0.62 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[LARP1]] | -0.62 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[GFM1]] | -0.61 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.61 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD52]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[COA7]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.59 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[AGPS]] | -0.58 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ANAPC7]] | -0.57 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[OCRL]] | -0.56 | -0.32 / -0.62 | both halves | 2e-04 |  |
| [[CAPRIN1]] | -0.56 | -0.46 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GTF2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINI1]] | C | SERPINI1 activity raises GTF2B's level | lines that do not express SERPINI1 (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without SERPINI1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.777). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.9, -26.2); signed map (3.1, 16.3). **Vector** length 123, 44.8% of its response variance represented; |z| ≥ 3 in 1,064 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +23.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.1 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.2 | +3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.4 | +1.1 |
|  | [[Demeclocycline (drug)]] 0.05 µM |  | +2.4 | +2.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.6 | -2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.3 | -10.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | +1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.8 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -4.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.1 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | +3.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIB |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p22.2 — chr1:88,852,633-88,891,944 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFIIB |
| Gene groups (HGNC) | General transcription factors; Acyltransferases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 13 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00403](https://www.uniprot.org/uniprotkb/Q00403) (Transcription initiation factor IIB):

> General transcription factor that plays a role in transcription initiation by RNA polymerase II (Pol II). Involved in the pre-initiation complex (PIC) formation and Pol II recruitment at promoter DNA. Together with the TATA box-bound TBP forms the core initiation complex and provides a bridge between TBP and the Pol II-TFIIF complex. Released from the PIC early following the onset of transcription during the initiation and elongation transition and reassociates with TBP during the next …

**Summary**, from NCBI Gene [2959](https://www.ncbi.nlm.nih.gov/gene/2959):

> This gene encodes the general transcription factor IIB, one of the ubiquitous factors required for transcription initiation by RNA polymerase II. The protein localizes to the nucleus where it forms a complex (the DAB complex) with transcription factors IID and IIA. Transcription factor IIB serves as a bridge between IID, the factor which initially recognizes the promoter sequence, and RNA polymerase II. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4648) · Entrez [2959](https://www.ncbi.nlm.nih.gov/gene/2959) · UniProt [Q00403](https://www.uniprot.org/uniprotkb/Q00403) · Ensembl [ENSG00000137947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137947)

## Data

Gene col 6097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6097); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6097]; `tensor/DDL_lfc|DDL_z.npy` [6097]; `embed/gene_vectors.npy` [6097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6097 or target_col == 6097). Every well: [[GTF2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
