---
symbol: "RSBN1"
type: "gene"
col: 1301
ensembl_id: "ENSG00000081019"
name: "round spermatid basic protein 1"
location: "1p13.2"
module: 144
arm: "+"
pooled_cpm: 47.87
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# RSBN1

*round spermatid basic protein 1* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 8.40× (z +21.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.354× (z -20.4, q 0e+00, down in 43 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.769× (z -5.0, q 1e-04, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPMK]] (+0.72, fdr 7e-06), [[ZNF654]] (+0.67, fdr 1e-05), [[C4orf47]] (+0.65, fdr 1e-05); moves opposite to [[IPO9]] (-0.62, fdr 1e-05), [[SAE1]] (-0.62, fdr 1e-05), [[EFTUD2]] (-0.60, fdr 4e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **8.40×** | +21.9 | 0e+00 | 48/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +13.9 | 2e-41 | 44/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.53×** | +13.0 | 3e-36 | 40/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +11.6 | 8e-29 | 40/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +9.8 | 1e-20 | 34/48 (A498, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +9.5 | 2e-19 | 40/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.3 | 7e-19 | 37/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.54×** | +8.5 | 2e-15 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.7 | 1e-09 | 30/49 (RKO, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +6.7 | 1e-09 | 29/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.41×** | +6.5 | 4e-09 | 29/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +6.2 | 3e-08 | 29/48 (LoVo, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.0 | 8e-08 | 26/48 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +6.0 | 1e-07 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.34×** | +5.8 | 3e-07 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.5 | 3e-04 | 19/47 (A-172, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 22/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.16× | +4.1 | 0.001 | 9/48 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.005 | 20/48 (LOX-IMVI, H4, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.006 | 17/48 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.354×** | -20.4 | 0e+00 | 43/49 (RPMI-7951, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.368×** | -18.9 | 0e+00 | 35/41 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -5.0 | 1e-04 | 27/48 (NCI-H1573, AsPC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.763×** | -4.9 | 1e-04 | 22/42 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.811×** | -3.8 | 0.016 | 18/48 (HOP62, NCI-H2347, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.813×** | -3.8 | 0.016 | 15/48 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.826×** | -3.5 | 0.042 | 18/49 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.4 | 0.051 | 19/43 (NCI-H661, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.832×** | -3.3 | 0.055 | 14/48 (NCI-H661, LOX-IMVI, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.842× | -3.3 | 0.059 | 12/48 (NCI-H2347, NCI-H2030, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.845× | -3.0 | 0.12 | 16/48 (NCI-H661, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.8 | 11 (6 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.2× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -16.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 55.7 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.41× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.0759× (z -29.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 63.6 | 4 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +14.9) | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 105 | 5 (4 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.6× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -22.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.0 | 6 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.6 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.40× (z +11.7) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 72.4 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.170× (z -15.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 47.1 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.98× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -12.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 36.8 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 13.0× (z +15.5) | — |
| [[RKO (line)]] | wt | 51.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -12.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 40.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.76× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 66.3 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.6× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -16.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 46.7 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +17.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -15.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.4 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.26× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.134× (z -19.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 27.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.1) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 13.3× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 35.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 82.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.19× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 64.1 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 16.4× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.228× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 41.3 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.60× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -8.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 96.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.96× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.409× (z -10.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 32.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +15.6) ⚠ cell-cycle shift, explains ~60% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -9.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 80.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -11.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 54.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 10.7× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -19.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 45.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 49.3 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.43× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -9.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.18× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -15.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 33.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 59.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0787× (z -20.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 59.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.49× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.377× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 54.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 52.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.0× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.5) | — |
| [[A-427 (line)]] | wt | 26.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +16.6) | — |
| [[BT-474 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.221× (z -11.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 68.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.1× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 29.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -11.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.111× (z -14.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.121× (z -9.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPMK]] | +0.72 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[C4orf47]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RBPJ]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[PURA]] | +0.63 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[BET1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[KDM5B]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DNASE1]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[NIFK-AS1]] | +0.62 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[CCNG2]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[TBX19]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[TTC9C]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | -0.62 | -0.51 / -0.62 | both halves | 1e-05 |  |
| [[SAE1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.60 | -0.41 / -0.66 | both halves | 4e-05 |  |
| [[RBBP8]] | -0.57 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[DELE1]] | -0.56 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[GFM1]] | -0.56 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[NUP188]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[MTG1]] | -0.55 | -0.31 / -0.60 | both halves | 2e-04 |  |
| [[CTPS1]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[INTS7]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PTPN11]] | -0.53 | -0.43 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RSBN1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.2, -38.2); signed map (-32.4, 26.0). **Vector** length 107, 30.5% of its response variance represented; |z| ≥ 3 in 1,056 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +13.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +13.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.1 | +0.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.7 | -20.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.9 | -18.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.2 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | round spermatid basic protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,761,832-113,812,476 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11220, ROSBIN, KDM9 |
| Gene groups (HGNC) | Round spermatid basic protein 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VWQ0](https://www.uniprot.org/uniprotkb/Q5VWQ0) (Lysine-specific demethylase 9):

> Histone demethylase that specifically demethylates dimethylated 'Lys-20' of histone H4 (H4K20me2) and trimethylated 'Lys-20' of histone H4 (H4K20me3) into monomethyl H4K20 (H4K20me1) thereby modulating chromosome architecture. May play a critical role in regulating H4K20 methylation during spermatogenesis.

**Summary**, from NCBI Gene [54665](https://www.ncbi.nlm.nih.gov/gene/54665):

> Predicted to enable histone H4K20 demethylase activity. Predicted to be involved in spermatogenesis. Predicted to be located in perinuclear region of cytoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25642) · Entrez [54665](https://www.ncbi.nlm.nih.gov/gene/54665) · UniProt [Q5VWQ0](https://www.uniprot.org/uniprotkb/Q5VWQ0) · Ensembl [ENSG00000081019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081019)

## Data

Gene col 1301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1301); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1301]; `tensor/DDL_lfc|DDL_z.npy` [1301]; `embed/gene_vectors.npy` [1301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1301 or target_col == 1301). Every well: [[RSBN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSBN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
