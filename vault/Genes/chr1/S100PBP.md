---
symbol: "S100PBP"
type: "gene"
col: 3800
ensembl_id: "ENSG00000116497"
name: "S100P binding protein"
location: "1p35.1"
module: 71
arm: "+"
pooled_cpm: 42.42
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# S100PBP

*S100P binding protein* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +10.1, q 3e-21, up in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 2.37×, SW480 2.27×, HT-29 2.68×, CFPAC-1 3.10×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.16×).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.311× (z -27.7, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.296× (z -20.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRR1]] (+0.61, fdr 1e-05), [[NR2C2]] (+0.58, fdr 3e-05), [[C21orf58]] (+0.57, fdr 2e-05); moves opposite to [[TTC3P1]] (-0.57, fdr 5e-05), [[CCNC]] (-0.51, fdr 3e-05), [[RPAP3]] (-0.51, fdr 7e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PWWP3B]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Menadione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 2.37×, SW480 2.27×, HT-29 2.68×, CFPAC-1 3.10×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 2.16×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +10.1 | 3e-21 | 36/47 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.26×** | +3.8 | 0.044 | 17/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.2 | 0.21 | 19/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.24× | +3.2 | 0.21 | 10/48 (SW480, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.22 | 11/48 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.22 | 17/48 (hTERT-HPNE, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3800.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.311×** | -27.7 | 0e+00 | 45/47 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.296×** | -20.4 | 0e+00 | 47/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.348×** | -17.7 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.362×** | -17.0 | 0e+00 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.402×** | -14.7 | 0e+00 | 42/48 (NCI-H460, COLO 205, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.470×** | -11.3 | 2e-27 | 40/48 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.471×** | -11.2 | 2e-27 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -10.7 | 1e-24 | 43/48 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.594×** | -8.7 | 2e-16 | 36/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -8.1 | 2e-14 | 34/48 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.622×** | -7.5 | 3e-12 | 37/48 (HEC-1-A, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -7.3 | 1e-11 | 31/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.652×** | -7.2 | 3e-11 | 30/48 (HEC-1-A, J82, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -7.1 | 5e-11 | 36/48 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -7.0 | 1e-10 | 33/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.646×** | -6.5 | 2e-09 | 32/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -4.9 | 2e-05 | 25/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.720×** | -3.9 | 0.002 | 25/48 (KATO III, J82, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.7 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -29.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -21.3) |
| [[PANC-1 (line)]] | alt | 65.8 | 1 | 10 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.61× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -24.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -19.6) |
| [[SW480 (line)]] | alt | 36.8 | 2 | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -24.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 57.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 37.8 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 69.1 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -23.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -12.6) |
| [[LoVo (line)]] | wt | 36.0 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.169× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -19.2) |
| [[SNU-1 (line)]] | wt | 45.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -17.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -12.4) |
| [[C32 (line)]] | wt | 37.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -14.3) |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -12.7) |
| [[HT-29 (line)]] | alt | 35.5 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -26.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.215× (z -13.0) |
| [[J82 (line)]] | alt | 71.0 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.203× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 42.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -14.8) |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -12.1) |
| [[COLO 205 (line)]] | alt | 41.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -25.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -13.7) |
| [[HOP62 (line)]] | alt | 46.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -12.6) |
| [[KATO III (line)]] | alt | 34.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.177× (z -11.8) |
| [[LS 180 (line)]] | wt | 32.5 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -19.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.1) |
| [[RKO (line)]] | wt | 43.0 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.155× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 53.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 27.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.128× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 36.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -24.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -8.8) |
| [[C-33 A (line)]] | alt | 76.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -9.2) |
| [[HCT15 (line)]] | alt | 45.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.239× (z -12.5) |
| [[SW1417 (line)]] | alt | 28.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.6) |
| [[A-172 (line)]] | wt | 39.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 61.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -23.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.330× (z -10.7) |
| [[A549 (line)]] | wt | 37.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -16.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 24.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.10× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 26.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 53.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -10.4) |
| [[SW 900 (line)]] | alt | 27.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.242× (z -8.5) |
| [[A498 (line)]] | wt | 38.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.106× (z -9.9) |
| [[H4 (line)]] | wt | 42.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -8.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -10.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0741× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRR1]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.58 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[C21orf58]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[MSL1]] | +0.57 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[UBL7-DT]] | +0.56 | +0.39 / +0.55 | both halves | 6e-05 |  |
| [[DBF4B]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[NUP153]] | +0.55 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[EIF4ENIF1]] | +0.55 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ZNF367]] | +0.54 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[NDOR1]] | +0.54 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZNF718]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC3P1]] | -0.57 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[CCNC]] | -0.51 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[RPAP3]] | -0.51 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[PWWP3B]] | -0.51 | -0.40 / -0.53 | both halves | 4e-05 |  |
| [[SRRD]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ULBP3]] | -0.49 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[AFF4]] | -0.49 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[ARMCX5]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[DHRS2]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[MRFAP1]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[C1orf226]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[CYP3A5]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PWWP3B]] | B | PWWP3B activity lowers S100PBP's level | lines that do not express PWWP3B (31) vs lines expressing it (19) | 1.22× higher at baseline in the lines without PWWP3B | 0.031 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, SLC15A5, GTF2I-AS1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Menadione (drug)]] 0.5 µM | C | S100PBP's natural level lowers the cells' numbers under Menadione 0.5 µM (makes them more sensitive) | S100PBP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.011 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | S100PBP's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | S100PBP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.018 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | S100PBP's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | S100PBP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.60 | 0.458 over the table, 0.077 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.9, -42.2); signed map (-40.5, -51.1). **Vector** length 78.0, 20.1% of its response variance represented; |z| ≥ 3 in 1,230 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +10.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | -7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.7 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | -0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -3.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.7 | -27.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | -4.5 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | -4.4 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -8.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | S100P binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,816,767-32,858,875 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12903, S100PBPR |
| Matched by | ensembl_id |

UniProt [Q96BU1](https://www.uniprot.org/uniprotkb/Q96BU1) carries no function annotation.

**Summary**, from NCBI Gene [64766](https://www.ncbi.nlm.nih.gov/gene/64766):

> This gene encodes a protein that was originally identified by its interaction with S100 calcium-binding protein P. Expression of this protein has been reported to be associated with pancreatic ductal adenocarcinoma. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:25768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25768) · Entrez [64766](https://www.ncbi.nlm.nih.gov/gene/64766) · UniProt [Q96BU1](https://www.uniprot.org/uniprotkb/Q96BU1) · Ensembl [ENSG00000116497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116497)

## Data

Gene col 3800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3800); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3800]; `tensor/DDL_lfc|DDL_z.npy` [3800]; `embed/gene_vectors.npy` [3800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3800 or target_col == 3800). Every well: [[S100PBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/S100PBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
