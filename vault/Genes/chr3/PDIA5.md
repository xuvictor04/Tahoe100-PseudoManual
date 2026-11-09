---
symbol: "PDIA5"
type: "gene"
col: 788
ensembl_id: "ENSG00000065485"
name: "protein disulfide isomerase family A member 5"
location: "3q21.1"
module: 49
arm: "+"
pooled_cpm: 162.12
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# PDIA5

*protein disulfide isomerase family A member 5* — 3q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.33× (z +5.0, q 3e-04, up in 34 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.385× (z -19.8, q 0e+00, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.489× (z -12.6, q 4e-34, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GORASP2]] (+0.83, fdr 7e-06), [[SSR2]] (+0.81, fdr 7e-06), [[TXNDC11]] (+0.80, fdr 7e-06); moves opposite to [[BAZ2B]] (-0.65, fdr 1e-05), [[ATF7IP]] (-0.63, fdr 4e-05), [[C11orf58]] (-0.62, fdr 1e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 788.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +5.0 | 3e-04 | 34/49 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +4.3 | 0.005 | 25/48 (SNU-423, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.2 | 0.005 | 27/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.25 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.25 | 15/49 (MIA PaCa-2, CHP-212, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 18 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 788.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.385×** | -19.8 | 0e+00 | 45/48 (A498, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.426×** | -15.0 | 0e+00 | 45/49 (NCI-H23, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.416×** | -14.8 | 0e+00 | 41/44 (Panc 03.27, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.417×** | -14.8 | 0e+00 | 47/48 (A498, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -12.6 | 4e-34 | 42/48 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.509×** | -11.8 | 2e-30 | 42/48 (HOP62, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.512×** | -11.8 | 5e-30 | 41/48 (HOP62, H4, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.490×** | -11.6 | 4e-29 | 43/45 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -9.2 | 2e-18 | 41/48 (A-172, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.639×** | -7.9 | 2e-13 | 42/48 (NCI-H1573, H4, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -7.0 | 1e-10 | 35/48 (HS-578T, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.733×** | -6.8 | 4e-10 | 41/48 (HS-578T, J82, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.670×** | -6.8 | 5e-10 | 34/47 (CFPAC-1, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **0.694×** | -6.4 | 6e-09 | 35/48 (SW 1088, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.695×** | -6.4 | 6e-09 | 34/48 (A-172, H4, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -6.2 | 2e-08 | 32/49 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -5.4 | 2e-06 | 33/48 (H4, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.803×** | -3.8 | 0.003 | 24/48 (HT-29, HEC-1-A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.808×** | -3.7 | 0.004 | 27/48 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.668×** | -3.7 | 0.005 | 24/49 (HS-578T, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.809×** | -3.4 | 0.012 | 23/47 (A549, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ixazomib (drug)]] 5 µM |  | **0.688×** | -3.4 | 0.012 | 23/48 (hTERT-HPNE, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.829×** | -3.3 | 0.019 | 21/49 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.830×** | -3.3 | 0.020 | 22/49 (HT-29, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 788. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 188 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -26.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -16.1) |
| [[A-172 (line)]] | wt | 138 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -18.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -16.0) |
| [[HS-578T (line)]] | alt | 385 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -25.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -18.2) |
| [[H4 (line)]] | wt | 243 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -20.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -11.6) |
| [[SW 900 (line)]] | alt | 124 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.243× (z -14.1) |
| [[A549 (line)]] | wt | 188 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -20.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -17.7) |
| [[J82 (line)]] | alt | 145 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -15.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -14.3) |
| [[KATO III (line)]] | alt | 164 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.403× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 215 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -25.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -19.3) |
| [[AsPC-1 (line)]] | alt | 127 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 161 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -21.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -15.5) |
| [[NCI-H2347 (line)]] | alt | 207 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.445× (z -11.5) |
| [[SW1417 (line)]] | alt | 191 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.6) |
| [[A498 (line)]] | wt | 227 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -29.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -20.5) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.282× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 110 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.362× (z -11.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.376× (z -10.6) |
| [[SNU-423 (line)]] | alt | 90.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.439× (z -8.8) |
| [[SW480 (line)]] | alt | 119 | 0 | 6 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -14.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C32 (line)]] | wt | 101 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.175× (z -15.2) |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.436× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 165 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.368× (z -10.2) |
| [[SNU-1 (line)]] | wt | 165 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0618× (z -25.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 174 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.343× (z -15.3) |
| [[LoVo (line)]] | wt | 191 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 167 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -28.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.435× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 184 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -20.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 122 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.361× (z -8.8) |
| [[SW48 (line)]] | wt | 226 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.388× (z -10.0) |
| [[Hs 766T (line)]] | wt | 151 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.3) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LS 180 (line)]] | wt | 164 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.294× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[PANC-1 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.404× (z -12.8) |
| [[C-33 A (line)]] | alt | 120 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.340× (z -11.2) |
| [[COLO 205 (line)]] | alt | 173 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW 1088 (line)]] | alt | 223 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.121× (z -9.8) ⚠ transcription drop; cell-cycle shift, explains ~49% of this change |
| [[BT-474 (line)]] | alt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 170 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 191 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.323× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AN3 CA (line)]] | alt | 91.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 77.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 788), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP2]] | +0.83 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[SSR2]] | +0.81 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.80 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[HM13]] | +0.79 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.77 | +0.85 / +0.68 | both halves | 7e-06 |  |
| [[TMED9]] | +0.77 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.76 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[COG6]] | +0.76 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[OSTC]] | +0.76 | +0.82 / +0.70 | both halves | 7e-06 |  |
| [[TMED3]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.75 | +0.79 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | -0.65 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[ATF7IP]] | -0.63 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[C11orf58]] | -0.62 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, -33.7); signed map (-50.8, 9.3). **Vector** length 137, 54.4% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +4.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.1 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.4 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.2 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -9.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.1 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.4 | -19.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -6.8 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.0 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein disulfide isomerase family A member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.1 — chr3:123,067,025-123,225,227 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PDIR, FLJ30401 |
| Gene groups (HGNC) | Protein disulfide isomerases; MicroRNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 5 pathways, smallest: XBP1(S) activates chaperone genes; IRE1alpha activates chaperones; Unfolded Protein Response (UPR) |
| Matched by | ensembl_id |

UniProt [Q14554](https://www.uniprot.org/uniprotkb/Q14554) carries no function annotation.

**Summary**, from NCBI Gene [10954](https://www.ncbi.nlm.nih.gov/gene/10954):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The encoded protein has an N-terminal ER-signal sequence, three catalytically active thioredoxin (TRX) domains, a TRX-like domain, and a C-terminal ER-retention sequence. The N-terminal TRX-like domain is the primary binding site for the major ER chaperone calreticulin and possibly other proteins and substrates as …

**Accessions** — [HGNC:24811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24811) · Entrez [10954](https://www.ncbi.nlm.nih.gov/gene/10954) · UniProt [Q14554](https://www.uniprot.org/uniprotkb/Q14554) · Ensembl [ENSG00000065485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065485)

## Data

Gene col 788: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 788); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 788, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 788]; `tensor/DDL_lfc|DDL_z.npy` [788]; `embed/gene_vectors.npy` [788]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 788 or target_col == 788). Every well: [[PDIA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
