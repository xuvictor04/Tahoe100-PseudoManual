---
symbol: "EOLA2-DT"
type: "gene"
col: 14032
ensembl_id: "ENSG00000235703"
name: "EOLA2 divergent transcript"
location: "Xq28"
module: 26
arm: "+"
pooled_cpm: 85.14
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 45
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# EOLA2-DT

*EOLA2 divergent transcript* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.09× (z +3.7, q 0.071, up in 1 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.34× (z +3.5, q 0.071, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 45 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.367× (z -17.0, q 0e+00, down in 42 of 45 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.213× (z -15.4, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZF1]] (+0.67, fdr 7e-06), [[MUC20-OT1]] (+0.66, fdr 7e-06), [[DNHD1]] (+0.65, fdr 2e-05); moves opposite to [[NEK3]] (-0.57, fdr 5e-05), [[SLC25A12]] (-0.57, fdr 1e-05), [[AADAT]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SLC35D1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.7 | 0.071 | 1/48 (NCI-H23) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.071 | 28/47 (LS 180, NCI-H2347, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.75×** | +3.5 | 0.071 | 27/48 (NCI-H596, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.74×** | +3.5 | 0.071 | 27/47 (NCI-H23, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.075 | 26/46 (AsPC-1, A498, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.088 | 24/45 (NCI-H23, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.14 | 24/45 (NCI-H23, A-427, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 24 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 45 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.367×** | -17.0 | 0e+00 | 42/45 (PANC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.213×** | -15.4 | 0e+00 | 45/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.367×** | -12.0 | 7e-31 | 44/46 (NCI-H1573, HCT15, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.420×** | -10.4 | 4e-23 | 42/45 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.431×** | -10.1 | 8e-22 | 44/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.431×** | -9.6 | 5e-20 | 39/46 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.464×** | -9.2 | 3e-18 | 44/46 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.499×** | -8.3 | 6e-15 | 39/46 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **0.491×** | -8.1 | 2e-14 | 34/47 (RPMI-7951, COLO 205, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.531×** | -7.6 | 2e-12 | 40/46 (HT-29, H4, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.475×** | -7.4 | 6e-12 | 38/45 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.542×** | -7.3 | 1e-11 | 40/46 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.580×** | -6.5 | 3e-09 | 37/46 (H4, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **0.596×** | -6.2 | 2e-08 | 38/46 (PANC-1, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.568×** | -5.6 | 7e-07 | 33/45 (SNU-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.667×** | -4.8 | 4e-05 | 33/46 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.754×** | -4.8 | 5e-05 | 28/46 (Panc 03.27, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.666×** | -4.6 | 1e-04 | 28/46 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -4.3 | 4e-04 | 31/47 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.718×** | -4.0 | 0.002 | 28/47 (HT-29, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.754×** | -3.4 | 0.013 | 24/46 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.754×** | -3.4 | 0.013 | 23/46 (HOP62, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -3.3 | 0.018 | 22/45 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.019 | 23/46 (HT-29, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.62 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 135 | 0 | 14 (11 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0895× (z -14.7) |
| [[HT-29 (line)]] | alt | 221 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -26.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.7) |
| [[NCI-H1573 (line)]] | alt | 175 | 0 | 12 (11 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.177× (z -15.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.203× (z -11.5) |
| [[PANC-1 (line)]] | alt | 127 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -27.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -20.8) |
| [[RPMI-7951 (line)]] | alt | 139 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.171× (z -11.8) |
| [[SNU-1 (line)]] | wt | 95.8 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.144× (z -12.3) |
| [[HCT15 (line)]] | alt | 168 | 0 | 7 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.170× (z -13.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.142× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 90.9 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -18.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -12.0) |
| [[MIA PaCa-2 (line)]] | alt | 57.6 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -18.6) |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.273× (z -11.4) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.352× (z -9.1) |
| [[SNU-423 (line)]] | alt | 156 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.112× (z -15.1) |
| [[A549 (line)]] | wt | 81.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -20.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -14.3) |
| [[A-427 (line)]] | wt | 84.2 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 91.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -12.3) |
| [[COLO 205 (line)]] | alt | 144 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -19.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HOP62 (line)]] | alt | 128 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -12.4) |
| [[KATO III (line)]] | alt | 68.4 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0655× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.186× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 55.2 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -10.8) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.297× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.154× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.263× (z -12.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.208× (z -12.6) |
| [[SW480 (line)]] | alt | 62.8 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -15.1) |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -10.7) |
| [[SW 900 (line)]] | alt | 79.8 | 0 | 4 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0393× (z -11.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.139× (z -11.1) |
| [[A498 (line)]] | wt | 71.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -16.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -12.7) |
| [[BT-474 (line)]] | alt | 64.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 60.2 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.334× (z -10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.369× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 69.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -13.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.345× (z -11.1) |
| [[A-172 (line)]] | wt | 91.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.307× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 44.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.193× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 77.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.173× (z -9.1) |
| [[J82 (line)]] | alt | 52.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.363× (z -10.4) |
| [[LS 180 (line)]] | wt | 51.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.183× (z -11.7) |
| [[SW 1271 (line)]] | alt | 194 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0803× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change |
| [[CHP-212 (line)]] | wt | 57.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 84.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -9.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 53.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.229× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 42.7 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.221× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 35.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.177× (z -9.4) |
| [[SW1417 (line)]] | alt | 47.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW48 (line)]] | wt | 38.0 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0506× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZF1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MUC20-OT1]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ALOX12-AS1]] | +0.63 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[TNXB]] | +0.60 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PDC-AS1]] | +0.60 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SLC25A53]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[IL18BP]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[LINC02646]] | +0.60 | +0.34 / +0.58 | both halves | 1e-04 |  |
| [[FTX]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[NEK11]] | +0.59 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[ANKMY1]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK3]] | -0.57 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SLC25A12]] | -0.57 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[AADAT]] | -0.56 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SAAL1]] | -0.56 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[PAX9]] | -0.55 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ZNF30]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[BBS5]] | -0.55 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[TFB1M]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[ADH5]] | -0.54 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[TM7SF3]] | -0.53 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.52 | -0.32 / -0.56 | both halves | 1e-04 |  |
| [[MRPS31P4]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35D1]] | C | EOLA2-DT's natural level weakens SLC35D1's drug response | EOLA2-DT's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.49; direction not clear | 0.086 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (28.0, -19.8); signed map (10.6, 7.3). **Vector** length 87.4, 30.6% of its response variance represented; |z| ≥ 3 in 1,338 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.2 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.6 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.4 | -6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +3.4 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.7 | -4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.5 | -8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.9 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | EOLA2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | Xq28 — chrX:149,938,613-150,224,580 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously LINC00894 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48579](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48579) · Entrez [100272228](https://www.ncbi.nlm.nih.gov/gene/100272228) · Ensembl [ENSG00000235703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235703)

## Data

Gene col 14032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14032); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14032]; `tensor/DDL_lfc|DDL_z.npy` [14032]; `embed/gene_vectors.npy` [14032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14032 or target_col == 14032). Every well: [[EOLA2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EOLA2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
