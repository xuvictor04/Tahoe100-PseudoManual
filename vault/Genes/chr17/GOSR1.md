---
symbol: "GOSR1"
type: "gene"
col: 2970
ensembl_id: "ENSG00000108587"
name: "golgi SNAP receptor complex member 1"
location: "17q11.2"
module: 114
arm: "+"
pooled_cpm: 140.51
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# GOSR1

*golgi SNAP receptor complex member 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.68× (z +16.9, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.396× (z -21.2, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC174]] (+0.77, fdr 7e-06), [[NFX1]] (+0.75, fdr 7e-06), [[TRIM4]] (+0.74, fdr 7e-06); moves opposite to [[METAP1]] (-0.67, fdr 7e-06), [[STRN]] (-0.66, fdr 1e-05), [[XPR1]] (-0.63, fdr 1e-05).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDHR3]] → it (grade C ⚠); 6 go from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +16.9 | 0e+00 | 46/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +12.1 | 2e-31 | 45/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +7.8 | 1e-12 | 38/48 (A-172, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +4.4 | 0.001 | 26/49 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.005 | 26/48 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.026 | 19/48 (SW 900, AsPC-1, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.35×** | +3.6 | 0.028 | 21/49 (HEC-1-A, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.20× | +3.0 | 0.17 | 12/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.396×** | -21.2 | 0e+00 | 48/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.402×** | -20.8 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.404×** | -20.7 | 0e+00 | 48/48 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.451×** | -18.2 | 0e+00 | 45/49 (A-427, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.445×** | -17.8 | 0e+00 | 42/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.562×** | -13.2 | 1e-37 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.539×** | -13.1 | 3e-37 | 41/45 (A-427, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.596×** | -11.8 | 2e-30 | 40/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.634×** | -10.4 | 1e-23 | 44/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.623×** | -10.4 | 1e-23 | 41/47 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -10.1 | 3e-22 | 43/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.531×** | -7.6 | 2e-12 | 44/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.738×** | -6.9 | 2e-10 | 30/48 (NCI-H460, SW1417, …) | rises with dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.735×** | -6.8 | 5e-10 | 35/48 (A-427, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.747×** | -6.7 | 1e-09 | 30/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.783×** | -5.4 | 2e-06 | 28/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.806×** | -4.9 | 2e-05 | 28/49 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.837× | -4.1 | 0.001 | 21/48 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.892× | -3.7 | 0.006 | 12/48 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.872× | -3.1 | 0.043 | 11/48 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.910× | -3.0 | 0.059 | 3/48 (J82, CHP-212, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.915× | -2.9 | 0.090 | 7/48 (A498, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 144 | 4 | 15 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.7) | [[Digitoxin (drug)]] 0.5 µM 0.322× (z -19.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.323× (z -18.9) |
| [[SW480 (line)]] | alt | 135 | 2 | 11 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.345× (z -17.1) |
| [[H4 (line)]] | wt | 210 | 0 | 11 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -14.4) |
| [[PANC-1 (line)]] | alt | 193 | 2 | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -13.8) |
| [[HOP62 (line)]] | alt | 168 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -14.4) |
| [[KATO III (line)]] | alt | 217 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.23× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 148 | 1 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.256× (z -16.1) |
| [[A-172 (line)]] | wt | 144 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.448× (z -11.7) |
| [[A549 (line)]] | wt | 206 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.370× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 148 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.328× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 8 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.354× (z -13.4) |
| [[A498 (line)]] | wt | 217 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.51× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.341× (z -17.4) |
| [[CFPAC-1 (line)]] | alt | 111 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.349× (z -14.2) |
| [[LoVo (line)]] | wt | 142 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.347× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 121 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.9) | [[Belinostat (drug)]] 5 µM 0.441× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 163 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.430× (z -11.3) |
| [[SW 900 (line)]] | alt | 148 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.1) |
| [[SW1417 (line)]] | alt | 116 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -16.0) |
| [[A-427 (line)]] | wt | 112 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.0804× (z -31.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.323× (z -13.7) |
| [[COLO 205 (line)]] | alt | 180 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.362× (z -11.2) |
| [[Hs 766T (line)]] | wt | 113 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.374× (z -11.5) |
| [[HS-578T (line)]] | alt | 145 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.332× (z -13.7) |
| [[HT-29 (line)]] | alt | 123 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -11.5) |
| [[J82 (line)]] | alt | 138 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -14.5) |
| [[SNU-423 (line)]] | alt | 122 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -11.5) ⚠ toxic · without an alert: [[Belinostat (drug)]] 5 µM 0.421× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 155 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 88.8 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.424× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 122 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 95.9 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 135 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.323× (z -15.1) |
| [[HCT15 (line)]] | alt | 155 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -10.8) |
| [[RKO (line)]] | wt | 127 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.4) | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -12.4) |
| [[C32 (line)]] | wt | 110 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.411× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 92.4 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.360× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.433× (z -8.8) |
| [[LS 180 (line)]] | wt | 115 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 85.1 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.1) | [[Panobinostat (drug)]] 5 µM 0.377× (z -11.1) |
| [[BT-474 (line)]] | alt | 110 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.4) | [[Belinostat (drug)]] 5 µM 0.499× (z -8.5) |
| [[SNU-1 (line)]] | wt | 134 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -8.9) |
| [[AN3 CA (line)]] | alt | 105 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.269× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 110 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -8.6) |
| [[NCI-H661 (line)]] | alt | 89.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0686× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 83.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.372× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 100 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC174]] | +0.77 | +0.83 / +0.64 | both halves | 7e-06 |  |
| [[NFX1]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.74 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[SEC23IP]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[BMS1P4-1]] | +0.70 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.70 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[RBM23]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[NME6]] | +0.69 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[HELQ]] | +0.69 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[HMGXB4]] | +0.68 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[MYSM1]] | +0.68 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TRIP11]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 502 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.67 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[STRN]] | -0.66 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[XPR1]] | -0.63 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[MAPK1]] | -0.61 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[DPY19L1]] | -0.61 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[HDAC1]] | -0.61 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PTK2]] | -0.60 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[EXT2]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[HACD3]] | -0.59 | -0.62 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDHR3]] | C | CDHR3 activity raises GOSR1's level | lines that do not express CDHR3 (3) vs lines expressing it (47) | 1.28× lower at baseline in the lines without CDHR3 | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MMP25, MPP4, ABCA10 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | GOSR1's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.360 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Adagrasib (drug)]] 0.5 µM | C | GOSR1's natural level lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | GOSR1's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.057 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hydroxyurea (drug)]] 0.5 µM | C | GOSR1's natural level lowers the cells' numbers under Hydroxyurea 0.5 µM (makes them more sensitive) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.416 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | GOSR1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.483 over the table, 0.094 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | GOSR1's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | GOSR1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.510 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.9, 5.1); signed map (-3.8, -13.5). **Vector** length 141, 51.8% of its response variance represented; |z| ≥ 3 in 1,355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +15.5 | +16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +14.6 | +12.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.4 | +7.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.6 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +2.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.8 | +3.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.5 | -0.3 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +1.5 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -8.8 | -13.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | -8.6 | -11.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.0 | -10.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -7.6 | -6.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -7.6 | -10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.9 | -7.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.9 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | golgi SNAP receptor complex member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:30,477,362-30,527,592 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GOS28, P28, GS28, GOS-28, GOLIM2 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 8 pathways, smallest: Intra-Golgi traffic; COPI-mediated anterograde transport; ER to Golgi Anterograde Transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O95249](https://www.uniprot.org/uniprotkb/O95249) (Golgi SNAP receptor complex member 1):

> Involved in transport from the ER to the Golgi apparatus as well as in intra-Golgi transport. It belongs to a super-family of proteins called t-SNAREs or soluble NSF (N-ethylmaleimide-sensitive factor) attachment protein receptor. May play a protective role against hydrogen peroxide induced cytotoxicity under glutathione depleted conditions in neuronal cells by regulating the intracellular ROS levels via inhibition of p38 MAPK (MAPK11, MAPK12, MAPK13 and MAPK14). Participates in docking and …

**Summary**, from NCBI Gene [9527](https://www.ncbi.nlm.nih.gov/gene/9527):

> This gene encodes a trafficking membrane protein which transports proteins among the endoplasmic reticulum and the Golgi and between Golgi compartments. This protein is considered an essential component of the Golgi SNAP receptor (SNARE) complex. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4430) · Entrez [9527](https://www.ncbi.nlm.nih.gov/gene/9527) · UniProt [O95249](https://www.uniprot.org/uniprotkb/O95249) · Ensembl [ENSG00000108587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108587)

## Data

Gene col 2970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2970); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2970]; `tensor/DDL_lfc|DDL_z.npy` [2970]; `embed/gene_vectors.npy` [2970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2970 or target_col == 2970). Every well: [[GOSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
