---
symbol: "HDAC4"
type: "gene"
col: 877
ensembl_id: "ENSG00000068024"
name: "histone deacetylase 4"
location: "2q37.3"
module: 5
arm: "+"
pooled_cpm: 142.37
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# HDAC4

*histone deacetylase 4* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +6.8, q 7e-09, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -16.0, q 0e+00, down in 45 of 47 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.356× (z -12.6, q 6e-34, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRG]] (+0.59, fdr 7e-06), [[SPRY4-AS1]] (+0.59, fdr 1e-05), [[TOMM40]] (+0.58, fdr 1e-05); moves opposite to [[MOSPD2]] (-0.57, fdr 7e-06), [[KPNA5]] (-0.57, fdr 1e-05), [[SECISBP2L]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 877.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.8 | 7e-09 | 33/48 (LoVo, RKO, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.6 | 0.001 | 33/47 (A549, RKO, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.5 | 0.084 | 25/47 (A-172, A549, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.30× | +3.2 | 0.20 | 25/47 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 1.29× | +3.1 | 0.22 | 26/47 (A-172, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.30× | +3.0 | 0.22 | 23/49 (LS 180, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 877.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.395×** | -16.0 | 0e+00 | 45/47 (A549, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.327×** | -12.9 | 1e-35 | 45/47 (NCI-H460, A549, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.356×** | -12.6 | 6e-34 | 43/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.390×** | -11.4 | 3e-28 | 43/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.430×** | -10.3 | 1e-22 | 39/47 (SW 900, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -8.1 | 4e-14 | 42/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -8.1 | 5e-14 | 35/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.295×** | -7.8 | 6e-13 | 41/48 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -6.8 | 7e-10 | 38/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.683×** | -6.5 | 3e-09 | 39/47 (SK-MEL-2, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.585×** | -6.5 | 4e-09 | 37/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.563×** | -6.4 | 5e-09 | 30/44 (C-33 A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.547×** | -6.1 | 4e-08 | 36/48 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -5.7 | 5e-07 | 33/46 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.667×** | -4.9 | 3e-05 | 28/47 (LS 180, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.638×** | -4.6 | 2e-04 | 27/47 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.775×** | -4.4 | 4e-04 | 29/48 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.746×** | -3.6 | 0.011 | 26/47 (KATO III, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.022 | 27/47 (SW480, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.738×** | -3.1 | 0.054 | 19/47 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.788×** | -2.9 | 0.099 | 25/47 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 877. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 551 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.231× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 291 | 0 | 13 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -18.0) |
| [[PANC-1 (line)]] | alt | 143 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 241 | 0 | 10 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -14.7) |
| [[C32 (line)]] | wt | 129 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.189× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 131 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 202 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -17.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -10.4) |
| [[LS 180 (line)]] | wt | 149 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.174× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -15.1) |
| [[A-427 (line)]] | wt | 116 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -11.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 123 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -19.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -10.6) |
| [[NCI-H1792 (line)]] | alt | 219 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.215× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 122 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -11.5) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.288× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 250 | 0 | 6 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -12.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0973× (z -10.6) |
| [[A549 (line)]] | wt | 104 | 1 | 4 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -20.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.257× (z -10.7) |
| [[BT-474 (line)]] | alt | 95.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -14.9) |
| [[COLO 205 (line)]] | alt | 320 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -20.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -8.6) |
| [[LoVo (line)]] | wt | 89.2 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 62.1 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.333× (z -9.2) |
| [[J82 (line)]] | alt | 65.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.257× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.274× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 57.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -12.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.272× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 56.6 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -14.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.312× (z -8.6) |
| [[RKO (line)]] | wt | 78.0 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.428× (z -8.9) |
| [[SW 900 (line)]] | alt | 68.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -13.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW1417 (line)]] | alt | 183 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -15.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -11.2) |
| [[A-172 (line)]] | wt | 78.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -11.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[H4 (line)]] | wt | 173 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HEC-1-A (line)]] | alt | 70.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.1) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HT-29 (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 59.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.2) | [[Harringtonine (drug)]] 5 µM 0.272× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[KATO III (line)]] | alt | 83.8 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -15.6) |
| [[SHP-77 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -10.6) |
| [[SNU-1 (line)]] | wt | 72.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 222 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.243× (z -10.3) |
| [[A498 (line)]] | wt | 76.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.6) ⚠ cell-cycle shift, explains ~41% of this change |
| [[C-33 A (line)]] | alt | 158 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0791× (z -18.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 82.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -15.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.398× (z -8.6) |
| [[CHP-212 (line)]] | wt | 129 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[RMC-6236 (drug)]] 5 µM 0.0464× (z -9.0) |
| [[HS-578T (line)]] | alt | 76.0 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.243× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 91.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SNU-423 (line)]] | alt | 55.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.8) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -9.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 57.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +11.3) | — |
| [[SW 1271 (line)]] | alt | 89.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.103× (z -8.7) |
| [[AN3 CA (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 90.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 877), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRG]] | +0.59 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[TOMM40]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[TRAPPC9]] | +0.58 | +0.57 / +0.62 | both halves | 8e-06 |  |
| [[WDR27]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EHBP1]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[NPAS2]] | +0.57 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[MAD1L1]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 | same gene group |
| [[LINC01844]] | +0.56 | +0.43 / +0.60 | both halves | 4e-05 |  |
| [[FBXW7]] | +0.55 | +0.49 / +0.58 | both halves | 1e-05 | same gene group; pathway: Constitutive Signaling by NOTCH1 HD+PEST Domain Mutants; STRING 441 |
| [[PDCD6]] | +0.55 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[XXYLT1]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*38 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD2]] | -0.57 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[KPNA5]] | -0.57 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SECISBP2L]] | -0.55 | -0.60 / -0.50 | both halves | 1e-05 |  |
| [[APBB1]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.54 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[TAB2]] | -0.54 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[RNFT1]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[ASB8]] | -0.53 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.53 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ACTR10]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FPGT]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ARMCX1]] | -0.51 | -0.41 / -0.55 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HDAC4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers HDAC4's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.535). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.2, -32.8); signed map (-17.0, -55.3). **Vector** length 114, 41.4% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +7.0 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +3.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | -1.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.0 | +0.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Olanzapine (drug)]] 5 µM |  | +1.7 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.9 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.3 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.1 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.0 | -16.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -1.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.8 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:239,048,168-239,401,654 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0288, HDAC-A, HDACA, HD4, HA6116, HDAC-4; previously BDMR |
| Gene groups (HGNC) | Histone deacetylases, class IIA; MicroRNA protein coding host genes; NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 23 pathways, smallest: RUNX2 regulates chondrocyte maturation; RUNX3 regulates p14-ARF; RUNX2 regulates bone development |
| Matched by | ensembl_id |

**Function**, from UniProt [P56524](https://www.uniprot.org/uniprotkb/P56524) (Histone deacetylase 4):

> Responsible for the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes. Involved in muscle maturation via its interaction with the myocyte enhancer factors such as MEF2A, MEF2C and MEF2D. Involved in the …

**Summary**, from NCBI Gene [9759](https://www.ncbi.nlm.nih.gov/gene/9759):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to class II of the histone deacetylase/acuc/apha family. It possesses histone deacetylase activity and represses transcription when tethered to a promoter. This protein does not bind DNA directly, but through transcription factors MEF2C …

**Accessions** — [HGNC:14063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14063) · Entrez [9759](https://www.ncbi.nlm.nih.gov/gene/9759) · UniProt [P56524](https://www.uniprot.org/uniprotkb/P56524) · Ensembl [ENSG00000068024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068024)

## Data

Gene col 877: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 877); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 877, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 877]; `tensor/DDL_lfc|DDL_z.npy` [877]; `embed/gene_vectors.npy` [877]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 877 or target_col == 877). Every well: [[HDAC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
