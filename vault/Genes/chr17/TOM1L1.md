---
symbol: "TOM1L1"
type: "gene"
col: 6493
ensembl_id: "ENSG00000141198"
name: "target of myb1 like 1 membrane trafficking protein"
location: "17q22"
module: 63
arm: "+"
pooled_cpm: 82.13
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 19
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TOM1L1

*target of myb1 like 1 membrane trafficking protein* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.58× (z +13.2, q 8e-37, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.426× (z -36.8, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMKLR2]] (+0.64, fdr 1e-05), [[SLC22A15]] (+0.62, fdr 7e-06), [[LINC00662]] (+0.62, fdr 1e-05); moves opposite to [[EP300]] (-0.53, fdr 1e-05), [[NR4A3]] (-0.52, fdr 3e-05), [[CFL1]] (-0.51, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.58×** | +13.2 | 8e-37 | 38/48 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +12.8 | 4e-35 | 39/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +9.5 | 4e-19 | 32/48 (A498, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +9.4 | 1e-18 | 38/49 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +9.3 | 2e-18 | 28/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.30×** | +8.1 | 6e-14 | 26/48 (A-172, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +6.7 | 2e-09 | 29/48 (SNU-423, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +6.4 | 9e-09 | 23/48 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +6.2 | 4e-08 | 19/49 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.22×** | +6.1 | 5e-08 | 22/48 (HOP62, LoVo, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.21×** | +5.8 | 3e-07 | 18/48 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +5.5 | 2e-06 | 18/48 (MIA PaCa-2, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.13× | +5.2 | 7e-06 | 17/48 (SNU-1, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.17× | +4.8 | 8e-05 | 18/48 (A498, H4, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | 1.17× | +4.7 | 1e-04 | 18/48 (H4, NCI-H460, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.33×** | +4.5 | 3e-04 | 17/48 (LOX-IMVI, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.14× | +3.9 | 0.003 | 16/47 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 9/48 (SNU-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Baicalin (drug)]] 5 µM |  | 1.09× | +3.7 | 0.007 | 2/49 (SW 900, C32) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.09× | +3.6 | 0.008 | 4/49 (KATO III, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6493.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.426×** | -36.8 | 0e+00 | 45/49 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.563×** | -24.8 | 0e+00 | 42/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.489×** | -21.8 | 0e+00 | 45/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.516×** | -20.1 | 0e+00 | 44/48 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.596×** | -15.8 | 0e+00 | 42/48 (A549, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -15.0 | 0e+00 | 40/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.629×** | -13.6 | 3e-40 | 37/50 (HEC-1-A, SNU-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.637×** | -13.2 | 4e-38 | 40/47 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.683×** | -11.2 | 3e-27 | 35/48 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -10.2 | 1e-22 | 27/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.793×** | -7.1 | 7e-11 | 25/48 (A549, KATO III, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.809×** | -6.5 | 5e-09 | 27/48 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.823×** | -5.7 | 5e-07 | 21/47 (RKO, KATO III, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.831×** | -5.7 | 6e-07 | 22/48 (A-172, NCI-H1792, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~66% of this change | **0.831×** | -5.6 | 7e-07 | 22/47 (BT-474, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -5.2 | 5e-06 | 20/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.857× | -4.4 | 3e-04 | 19/47 (A549, CHP-212, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.768×** | -4.2 | 6e-04 | 19/48 (MIA PaCa-2, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.771×** | -4.1 | 8e-04 | 16/48 (AN3 CA, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.883× | -3.8 | 0.003 | 11/48 (SW48, BT-474, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.922× | -3.5 | 0.009 | 4/48 (A549, NCI-H1792, …) | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | 0.841× | -3.5 | 0.011 | 10/48 (LoVo, KATO III, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.833×** | -2.9 | 0.065 | 9/48 (A-172, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 606 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 87.2 | 2 | 9 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.78× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -22.0) |
| [[A498 (line)]] | wt | 95.1 | 2 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.75× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -20.7) |
| [[NCI-H1792 (line)]] | alt | 88.6 | 0 | 8 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -18.7) |
| [[SW480 (line)]] | alt | 70.4 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -20.4) |
| [[KATO III (line)]] | alt | 127 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -18.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -18.0) |
| [[RKO (line)]] | wt | 102 | 0 | 7 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.161× (z -21.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -20.4) |
| [[LS 180 (line)]] | wt | 110 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.335× (z -12.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.346× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -17.6) |
| [[A549 (line)]] | wt | 111 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -26.7) |
| [[LoVo (line)]] | wt | 69.0 | 1 | 4 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.05× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -15.7) |
| [[A-427 (line)]] | wt | 102 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -10.6) |
| [[J82 (line)]] | alt | 54.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -12.3) |
| [[PANC-1 (line)]] | alt | 84.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -21.4) |
| [[SNU-1 (line)]] | wt | 123 | 1 | 3 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.41× (z +12.1) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.9) |
| [[SW1417 (line)]] | alt | 63.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -14.2) |
| [[CFPAC-1 (line)]] | alt | 61.3 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -19.2) |
| [[CHP-212 (line)]] | wt | 107 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0986× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -11.5) |
| [[HCT15 (line)]] | alt | 113 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -17.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 73.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -18.3) |
| [[Panc 03.27 (line)]] | alt | 71.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -15.5) |
| [[SK-MEL-2 (line)]] | alt | 89.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.9) |
| [[SW48 (line)]] | wt | 113 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -19.2) |
| [[A-172 (line)]] | wt | 53.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.9) |
| [[HT-29 (line)]] | alt | 65.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 65.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -21.7) |
| [[NCI-H23 (line)]] | alt | 74.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -15.0) |
| [[AsPC-1 (line)]] | alt | 46.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -10.8) |
| [[C32 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 72.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 54.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -10.5) |
| [[HOP62 (line)]] | alt | 40.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.3) |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -12.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 68.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0859× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0941× (z -10.6) |
| [[SNU-423 (line)]] | alt | 35.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -8.7) |
| [[SW 1271 (line)]] | alt | 84.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.115× (z -9.5) |
| [[SW 900 (line)]] | alt | 55.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.7) |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 74.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SLC22A15]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[LINC00662]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[XPOT]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[SEL1L3]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[ZFAND1]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[CNIH1]] | +0.59 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[HSPA9]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[ANK2]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[TMEM161A]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EP300]] | -0.53 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NR4A3]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[CFL1]] | -0.51 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZNF318]] | -0.51 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[KLF10]] | -0.50 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SCLT1]] | -0.49 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[BAHCC1]] | -0.49 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ATRIP]] | -0.48 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[ETV6]] | -0.48 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TOM1L1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM241B]] | C | FAM241B activity raises TOM1L1's level | lines that do not express FAM241B (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without FAM241B | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP8, EPHB2, LRP5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.583). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.9, 49.3); signed map (-10.3, 25.8). **Vector** length 116, 33.4% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.7 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.0 | +12.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.2 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.0 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.5 | +6.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.1 | +9.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.4 | +5.5 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -13.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.1 | -7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -13.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -36.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | target of myb1 like 1 membrane trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:54,899,387-54,961,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRCASM |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [O75674](https://www.uniprot.org/uniprotkb/O75674) (TOM1-like protein 1):

> Probable adapter protein involved in signaling pathways. Interacts with the SH2 and SH3 domains of various signaling proteins when it is phosphorylated. May promote FYN activation, possibly by disrupting intramolecular SH3-dependent interactions (By similarity).

**Summary**, from NCBI Gene [10040](https://www.ncbi.nlm.nih.gov/gene/10040):

> Enables clathrin binding activity and protein kinase binding activity. Involved in negative regulation of mitotic nuclear division; positive regulation of protein phosphorylation; and signal transduction. Located in cytosol and endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11983) · Entrez [10040](https://www.ncbi.nlm.nih.gov/gene/10040) · UniProt [O75674](https://www.uniprot.org/uniprotkb/O75674) · Ensembl [ENSG00000141198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141198)

## Data

Gene col 6493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6493); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6493]; `tensor/DDL_lfc|DDL_z.npy` [6493]; `embed/gene_vectors.npy` [6493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6493 or target_col == 6493). Every well: [[TOM1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOM1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
