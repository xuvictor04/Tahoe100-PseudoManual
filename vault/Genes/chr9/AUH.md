---
symbol: "AUH"
type: "gene"
col: 7241
ensembl_id: "ENSG00000148090"
name: "AU RNA binding methylglutaconyl-CoA hydratase"
location: "9q22.31"
module: 76
arm: "+"
pooled_cpm: 156.38
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# AUH

*AU RNA binding methylglutaconyl-CoA hydratase* — 9q22.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 2.15×; ⚠ cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (15 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.289× (z -21.0, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.466× (z -18.0, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC28A]] (+0.80, fdr 7e-06), [[COQ8A]] (+0.73, fdr 7e-06), [[MED30]] (+0.73, fdr 7e-06); moves opposite to [[CYREN]] (-0.58, fdr 3e-05), [[NIPAL1]] (-0.57, fdr 1e-05), [[PRORP]] (-0.57, fdr 1e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7241.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (BT-474 2.15×; ⚠ cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.25× | +3.5 | 0.12 | 26/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +3.5 | 0.12 | 18/48 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.22× | +3.4 | 0.12 | 23/48 (KATO III, LoVo, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.15× | +3.3 | 0.13 | 8/48 (A498, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7241.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.289×** | -21.0 | 0e+00 | 48/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.466×** | -18.0 | 0e+00 | 45/49 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.485×** | -17.1 | 0e+00 | 41/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.468×** | -12.6 | 2e-34 | 45/49 (SHP-77, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.471×** | -12.3 | 2e-32 | 41/44 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.530×** | -10.7 | 7e-25 | 47/48 (C32, A-172, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.273×** | -10.1 | 5e-22 | 47/48 (SW1417, A498, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.291×** | -9.6 | 8e-20 | 47/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.577×** | -9.3 | 9e-19 | 41/48 (C32, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.323×** | -8.8 | 1e-16 | 48/48 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.591×** | -8.6 | 6e-16 | 39/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.346×** | -8.2 | 9e-15 | 46/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.379×** | -7.5 | 2e-12 | 45/48 (Hs 766T, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -6.9 | 2e-10 | 41/47 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.653×** | -6.7 | 1e-09 | 34/45 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.727×** | -5.4 | 2e-06 | 38/48 (A498, NCI-H1573, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.515×** | -5.1 | 8e-06 | 42/47 (HepG2/C3A, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.766×** | -4.5 | 2e-04 | 28/48 (NCI-H2347, A498, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.5 | 2e-04 | 28/48 (HOP62, SNU-1, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.755×** | -4.5 | 2e-04 | 37/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.602×** | -4.4 | 3e-04 | 37/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.619×** | -4.1 | 8e-04 | 36/49 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7241. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 149 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.242× (z -15.1) |
| [[HOP62 (line)]] | alt | 153 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.307× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 209 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -14.9) |
| [[SNU-423 (line)]] | alt | 214 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -26.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -17.8) |
| [[A-172 (line)]] | wt | 120 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -22.9) |
| [[NCI-H1792 (line)]] | alt | 226 | 0 | 8 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.184× (z -21.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -15.4) |
| [[SW 900 (line)]] | alt | 184 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -18.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.311× (z -13.1) |
| [[A498 (line)]] | wt | 221 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -20.1) |
| [[NCI-H1573 (line)]] | alt | 113 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -16.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 155 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -21.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -16.7) |
| [[CFPAC-1 (line)]] | alt | 97.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 261 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 185 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -16.4) |
| [[Panc 03.27 (line)]] | alt | 173 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -15.7) |
| [[RPMI-7951 (line)]] | alt | 152 | 0 | 6 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.242× (z -15.2) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 130 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -18.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -16.2) |
| [[PANC-1 (line)]] | alt | 102 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -17.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -12.3) |
| [[SNU-1 (line)]] | wt | 260 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -19.4) |
| [[SW480 (line)]] | alt | 168 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -15.6) |
| [[AsPC-1 (line)]] | alt | 123 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -15.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -12.8) |
| [[COLO 205 (line)]] | alt | 163 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.381× (z -9.5) |
| [[H4 (line)]] | wt | 144 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -14.1) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.256× (z -15.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -10.5) |
| [[Hs 766T (line)]] | wt | 161 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.209× (z -15.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.126× (z -9.3) |
| [[HS-578T (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -16.8) |
| [[HT-29 (line)]] | alt | 147 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.188× (z -17.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.376× (z -10.4) |
| [[J82 (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 132 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 177 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -16.5) |
| [[SW1417 (line)]] | alt | 159 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -16.5) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -11.3) |
| [[A549 (line)]] | wt | 141 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -20.4) |
| [[CHP-212 (line)]] | wt | 261 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.0) |
| [[HCT15 (line)]] | alt | 184 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.3) |
| [[RKO (line)]] | wt | 158 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -14.0) |
| [[SHP-77 (line)]] | alt | 227 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[BT-474 (line)]] | alt | 102 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +10.3) ⚠ cell-cycle shift, explains ~26% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.5) |
| [[C-33 A (line)]] | alt | 133 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 181 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.278× (z -11.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 144 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.304× (z -14.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.492× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW48 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -15.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.363× (z -8.9) |
| [[A-427 (line)]] | wt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LS 180 (line)]] | wt | 209 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -9.0) |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -11.1) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0870× (z -11.0) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 222 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -9.1) |
| [[AN3 CA (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 178 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7241), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC28A]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[COQ8A]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[MED30]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[HACL1]] | +0.70 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[FBXO3]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[KIZ]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[YPEL2]] | +0.67 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[ELP2]] | +0.65 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[USP33]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[YPEL3]] | +0.64 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | -0.58 | -0.70 / -0.44 | both halves | 3e-05 |  |
| [[NIPAL1]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[PRORP]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[E2F3]] | -0.56 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[ZNF562]] | -0.56 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[TUBA1C]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[NACC1]] | -0.55 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[MPDU1]] | -0.55 | -0.58 / -0.44 | both halves | 3e-05 | pathway: Diseases of metabolism |
| [[DHX37]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[MYH15]] | -0.54 | -0.60 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises AUH's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.755). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.7, -46.6); signed map (-18.8, 8.8). **Vector** length 127, 49.9% of its response variance represented; |z| ≥ 3 in 1,459 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.4 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.3 | -21.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.8 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -9.3 | -17.1 |
|  | [[EX229 (drug)]] 5 µM |  | -8.9 | -8.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.6 | -10.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.3 | -8.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -7.8 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | AU RNA binding methylglutaconyl-CoA hydratase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.31 — chr9:91,213,815-91,361,918 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Carbon-oxygen lyases |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 4 pathways, smallest: Diseases of branched-chain amino acid catabolism; Branched-chain amino acid catabolism; Diseases of metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13825](https://www.uniprot.org/uniprotkb/Q13825) (Methylglutaconyl-CoA hydratase, mitochondrial):

> Catalyzes the fifth step in the leucine degradation pathway, the reversible hydration of 3-methylglutaconyl-CoA (3-MG-CoA) to 3-hydroxy-3-methylglutaryl-CoA (HMG-CoA). Can catalyze the reverse reaction but at a much lower rate in vitro. HMG-CoA is then quickly degraded by another enzyme (such as HMG-CoA lyase) to give acetyl-CoA and acetoacetate. Uses other substrates such as (2E)-glutaconyl-CoA efficiently in vitro, and to a lesser extent 3-methylcrotonyl-CoA (3-methyl-(2E)-butenoyl-CoA), …

**Summary**, from NCBI Gene [549](https://www.ncbi.nlm.nih.gov/gene/549):

> This gene encodes bifunctional mitochondrial protein that has both RNA-binding and hydratase activities. The encoded protein is a methylglutaconyl-CoA hydratase that catalyzes the hydration of 3-methylglutaconyl-CoA to 3-hydroxy-3-methyl-glutaryl-CoA, a critical step in the leucine degradation pathway. This protein also binds AU-rich elements (AREs) found in the 3' UTRs of rapidly decaying mRNAs including c-fos, c-myc and granulocyte/ macrophage colony stimulating factor. ARE elements are …

**Accessions** — [HGNC:890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:890) · Entrez [549](https://www.ncbi.nlm.nih.gov/gene/549) · UniProt [Q13825](https://www.uniprot.org/uniprotkb/Q13825) · Ensembl [ENSG00000148090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148090)

## Data

Gene col 7241: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7241); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7241, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7241]; `tensor/DDL_lfc|DDL_z.npy` [7241]; `embed/gene_vectors.npy` [7241]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7241 or target_col == 7241). Every well: [[AUH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AUH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
