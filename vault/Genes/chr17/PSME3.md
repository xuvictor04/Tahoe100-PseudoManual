---
symbol: "PSME3"
type: "gene"
col: 5212
ensembl_id: "ENSG00000131467"
name: "proteasome activator subunit 3"
location: "17q21.31"
module: 3
arm: "-"
pooled_cpm: 33.56
n_lines_expressing: 50
n_dd_up: 40
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PSME3

*proteasome activator subunit 3* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.99× (z +21.8, q 0e+00, up in 40 of 40 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.82× (z +8.4, q 3e-15, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.717× (z -4.7, q 0.002, down in 29 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.808× (z -4.3, q 0.006, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.366×); [[Lonafarnib (drug)]] 5 µM in 1 line (SK-MEL-2 0.154×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABCF2]] (+0.87, fdr 7e-06), [[WDR77]] (+0.81, fdr 7e-06), [[NUP188]] (+0.75, fdr 7e-06); moves opposite to [[DCTN6-DT]] (-0.76, fdr 7e-06), [[UBE2B]] (-0.76, fdr 7e-06), [[ATP5MC2]] (-0.75, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CAMSAP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 25 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.99×** | +21.8 | 0e+00 | 40/40 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **4.39×** | +20.8 | 0e+00 | 44/44 (SW480, RKO, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.25×** | +15.4 | 0e+00 | 41/44 (SW480, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.91×** | +12.9 | 7e-36 | 44/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.89×** | +8.9 | 4e-17 | 41/48 (PANC-1, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.84×** | +8.6 | 1e-15 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +8.4 | 3e-15 | 38/48 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.80×** | +8.0 | 1e-13 | 38/47 (NCI-H1792, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.9 | 2e-13 | 32/47 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.8 | 3e-13 | 41/48 (CFPAC-1, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.73×** | +7.7 | 5e-13 | 41/48 (HOP62, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.76×** | +7.6 | 1e-12 | 36/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.70×** | +7.5 | 3e-12 | 39/48 (HOP62, SW480, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.70×** | +7.5 | 4e-12 | 43/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.71×** | +7.3 | 1e-11 | 36/47 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +7.2 | 2e-11 | 36/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +7.0 | 1e-10 | 36/48 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +6.8 | 3e-10 | 41/47 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.58×** | +6.4 | 3e-09 | 33/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.4 | 5e-09 | 31/47 (A498, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +5.1 | 6e-06 | 31/47 (NCI-H1792, A549, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +5.1 | 7e-06 | 28/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 2e-05 | 28/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.002 | 22/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.67×** | +3.8 | 0.003 | 18/47 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.026 | 13/47 (NCI-H460, SW480, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.037 | 10/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5212.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.366×); [[Lonafarnib (drug)]] 5 µM in 1 line (SK-MEL-2 0.154×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.717×** | -4.7 | 0.002 | 29/47 (KATO III, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.808×** | -4.3 | 0.006 | 23/48 (BT-474, KATO III, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.848× | -3.3 | 0.19 | 18/48 (A-427, SW1417, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.856× | -3.1 | 0.27 | 17/48 (SW480, C-33 A, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.807× | -3.0 | 0.27 | 17/48 (A498, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 48.7 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.5) | — |
| [[PANC-1 (line)]] | alt | 24.2 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.65× (z +8.9) | — |
| [[SW480 (line)]] | alt | 36.5 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.80× (z +19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.41× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 24.8 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.60× (z +9.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.0 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.38× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 17.7 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.4× (z +15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.20× (z +10.2) | — |
| [[A-172 (line)]] | wt | 27.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.21× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.15× (z +11.5) | — |
| [[A549 (line)]] | wt | 30.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.56× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 22.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.69× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 30.1 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 18.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 19.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[J82 (line)]] | alt | 42.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.80× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[KATO III (line)]] | alt | 42.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.27× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 30.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.96× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Panc 03.27 (line)]] | alt | 43.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.47× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RPMI-7951 (line)]] | alt | 24.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 56.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.40× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Lonafarnib (drug)]] 5 µM 0.154× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 58.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.90× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[C32 (line)]] | wt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HEC-1-A (line)]] | alt | 39.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[Hs 766T (line)]] | wt | 19.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 33.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 31.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 41.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[RKO (line)]] | wt | 53.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.4) |
| [[SW48 (line)]] | wt | 38.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.80× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[AsPC-1 (line)]] | alt | 20.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.82× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HCT15 (line)]] | alt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.74× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H23 (line)]] | alt | 56.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.95× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[AN3 CA (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCF2]] | +0.87 | +0.81 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[WDR77]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[NUP188]] | +0.75 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[EIF4G1]] | +0.75 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[MOB1A]] | +0.74 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[TARDBP]] | +0.73 | +0.63 / +0.71 | both halves | 7e-06 | STRING 506 |
| [[SF3B4]] | +0.72 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MFN2]] | +0.72 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[DARS2]] | +0.72 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[TOR1A]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.71 | +0.67 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | -0.76 | -0.67 / -0.80 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.76 | -0.68 / -0.74 | both halves | 7e-06 |  |
| [[ATP5MC2]] | -0.75 | -0.63 / -0.76 | both halves | 7e-06 |  |
| [[RPL18]] ⚠ | -0.75 | -0.58 / -0.79 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36]] | -0.75 | -0.63 / -0.77 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.74 | -0.62 / -0.68 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.74 | -0.62 / -0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | -0.74 | -0.65 / -0.81 | both halves | 7e-06 |  |
| [[TOMM7]] | -0.74 | -0.62 / -0.77 | both halves | 7e-06 |  |
| [[MARCHF9]] | -0.74 | -0.54 / -0.77 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.74 | -0.64 / -0.75 | both halves | 7e-06 |  |
| [[CAMLG]] | -0.73 | -0.63 / -0.79 | both halves | 7e-06 |  |
| [[SNHG7]] | -0.73 | -0.53 / -0.76 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.72 | -0.63 / -0.72 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMSAP3]] | B | CAMSAP3 activity raises PSME3's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CAMSAP3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PSME3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNNI3]] | B | TNNI3 activity raises PSME3's level | lines that do not express TNNI3 (11) vs lines expressing it (39) | 1.08× lower at baseline in the lines without TNNI3 | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADM]] | B | ADM activity lowers PSME3's level | lines that do not express ADM (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without ADM | 0.098 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.4, -29.8); signed map (-8.5, -39.4). **Vector** length 101, 31.2% of its response variance represented; |z| ≥ 3 in 1,305 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.7 | +20.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +5.6 | +21.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.9 | +15.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.7 | +2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.3 | +2.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.4 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome activator subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,824,385-42,843,760 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Ki, PA28-gamma, REG-GAMMA, PA28G |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [P61289](https://www.uniprot.org/uniprotkb/P61289) (Proteasome activator complex subunit 3):

> Subunit of the 11S REG-gamma (also called PA28-gamma) proteasome regulator, a doughnut-shaped homoheptamer which associates with the proteasome. 11S REG-gamma activates the trypsin-like catalytic subunit of the proteasome but inhibits the chymotrypsin-like and postglutamyl-preferring (PGPH) subunits. Facilitates the MDM2-p53/TP53 interaction which promotes ubiquitination- and MDM2-dependent proteasomal degradation of p53/TP53, limiting its accumulation and resulting in inhibited apoptosis after …

**Summary**, from NCBI Gene [10197](https://www.ncbi.nlm.nih.gov/gene/10197):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9570](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9570) · Entrez [10197](https://www.ncbi.nlm.nih.gov/gene/10197) · UniProt [P61289](https://www.uniprot.org/uniprotkb/P61289) · Ensembl [ENSG00000131467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131467)

## Data

Gene col 5212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5212); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5212]; `tensor/DDL_lfc|DDL_z.npy` [5212]; `embed/gene_vectors.npy` [5212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5212 or target_col == 5212). Every well: [[PSME3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSME3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
