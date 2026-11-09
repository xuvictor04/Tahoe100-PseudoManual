---
symbol: "IRF2BP2"
type: "gene"
col: 9620
ensembl_id: "ENSG00000168264"
name: "interferon regulatory factor 2 binding protein 2"
location: "1q42.3"
module: 123
arm: "+"
pooled_cpm: 150.21
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/123"]
generated_by: "tahoemap"
---

# IRF2BP2

*interferon regulatory factor 2 binding protein 2* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.51× (z +6.3, q 2e-07, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.305× (z -18.1, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL4A]] (+0.65, fdr 1e-05), [[PIM3]] (+0.65, fdr 1e-05), [[REST]] (+0.65, fdr 1e-05); moves opposite to [[NPLOC4]] (-0.54, fdr 2e-05), [[MACROH2A1]] (-0.53, fdr 4e-05), [[LY6G5B]] (-0.53, fdr 1e-04).
> It is in [[Module 123]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.3 | 2e-07 | 34/47 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.29×** | +5.5 | 1e-05 | 36/47 (SHP-77, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +4.5 | 0.001 | 28/47 (LS 180, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.33×** | +4.3 | 0.002 | 30/47 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +4.2 | 0.003 | 28/47 (SHP-77, MIA PaCa-2, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.082 | 26/47 (SHP-77, SW48, …) | rises with dose | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.15 | 22/47 (LoVo, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.305×** | -18.1 | 0e+00 | 44/47 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.434×** | -18.0 | 0e+00 | 45/48 (MIA PaCa-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -13.5 | 3e-39 | 45/47 (SW1417, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.425×** | -12.0 | 3e-31 | 46/47 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.506×** | -10.4 | 4e-23 | 41/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -9.4 | 4e-19 | 44/49 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.534×** | -8.8 | 1e-16 | 38/42 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.602×** | -7.7 | 9e-13 | 38/47 (hTERT-HPNE, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.590×** | -7.6 | 2e-12 | 36/47 (HT-29, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.631×** | -7.0 | 1e-10 | 43/47 (MIA PaCa-2, SW1417, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.639×** | -6.8 | 5e-10 | 32/48 (SNU-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.446×** | -6.4 | 6e-09 | 36/44 (Panc 03.27, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **0.634×** | -6.4 | 7e-09 | 36/46 (CFPAC-1, HT-29, …) | two highest doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.766×** | -5.7 | 5e-07 | 31/47 (AN3 CA, A-172, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.731×** | -4.8 | 8e-05 | 33/47 (A498, SW1417, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -4.2 | 7e-04 | 29/47 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.001 | 27/47 (NCI-H1792, A549, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.757×** | -4.0 | 0.002 | 28/46 (BT-474, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.771×** | -3.9 | 0.002 | 27/47 (hTERT-HPNE, HT-29, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.654×** | -3.4 | 0.018 | 27/47 (MIA PaCa-2, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.803×** | -3.3 | 0.021 | 26/47 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[Dapagliflozin (drug)]] 0.05 µM |  | **0.819×** | -3.0 | 0.055 | 20/47 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Meloxicam (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.057 | 18/47 (J82, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 178 | 3 (1 ⚠) | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.67× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.165× (z -18.2) |
| [[SW1417 (line)]] | alt | 223 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -20.2) |
| [[BT-474 (line)]] | alt | 133 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.177× (z -15.6) |
| [[HT-29 (line)]] | alt | 184 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -17.4) |
| [[COLO 205 (line)]] | alt | 191 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.243× (z -14.1) |
| [[HOP62 (line)]] | alt | 145 | 1 | 7 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.11× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 94.0 | 8 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.86× (z +16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.28× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 215 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -18.3) |
| [[SW 900 (line)]] | alt | 249 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -17.4) |
| [[SW480 (line)]] | alt | 134 | 1 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.255× (z -16.7) |
| [[A-172 (line)]] | wt | 293 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.76× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 138 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.238× (z -14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.289× (z -12.3) |
| [[PANC-1 (line)]] | alt | 169 | 1 | 6 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.27× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.257× (z -17.8) |
| [[C32 (line)]] | wt | 161 | 0 | 6 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.253× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -17.3) |
| [[MIA PaCa-2 (line)]] | alt | 170 | 2 (1 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.76× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -19.1) |
| [[NCI-H1792 (line)]] | alt | 136 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -16.8) |
| [[A498 (line)]] | wt | 179 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.2) |
| [[SNU-423 (line)]] | alt | 237 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -18.2) |
| [[SW48 (line)]] | wt | 164 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.82× (z +9.2) | [[Selinexor (drug)]] 5 µM 0.420× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 152 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.35× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.355× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 262 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -12.9) |
| [[Hs 766T (line)]] | wt | 265 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.298× (z -12.3) |
| [[HS-578T (line)]] | alt | 162 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -18.5) |
| [[J82 (line)]] | alt | 118 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.314× (z -13.3) |
| [[KATO III (line)]] | alt | 100.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 115 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.377× (z -10.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.383× (z -10.0) |
| [[SHP-77 (line)]] | alt | 97.1 | 1 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.56× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -9.9) |
| [[SNU-1 (line)]] | wt | 189 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -14.3) |
| [[AN3 CA (line)]] | alt | 250 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.292× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 91.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 93.2 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.458× (z -11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 157 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.343× (z -13.4) |
| [[RKO (line)]] | wt | 116 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.371× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 125 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -12.5) |
| [[A549 (line)]] | wt | 134 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -11.9) |
| [[CHP-212 (line)]] | wt | 233 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -11.8) |
| [[LoVo (line)]] | wt | 167 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.297× (z -13.8) |
| [[H4 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 90.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 269 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.229× (z -8.8) |
| [[SW 1271 (line)]] | alt | 141 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.9) |
| [[A-427 (line)]] | wt | 35.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 121 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL4A]] | +0.65 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[PIM3]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[REST]] | +0.65 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[BTG1]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R3B]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[TXNIP]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[BCOR]] | +0.60 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.59 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PHF3]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[NR1D1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[THAP1]] | +0.58 | +0.48 / +0.76 | both halves | 2e-05 |  |
| [[TMEM251]] | +0.58 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPLOC4]] | -0.54 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[MACROH2A1]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[LY6G5B]] | -0.53 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ADPGK]] | -0.53 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[CTSZ]] | -0.53 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[FAM20B]] | -0.53 | -0.36 / -0.65 | both halves | 1e-04 |  |
| [[NUP205]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CAPN1]] | -0.51 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[NDUFA10]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[CHID1]] | -0.51 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[MFSD14B]] | -0.51 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises IRF2BP2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 123]] — TNF-alpha signaling via NF-kB; 40 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.0, -4.4); signed map (-3.7, 11.9). **Vector** length 130, 44.1% of its response variance represented; |z| ≥ 3 in 1,478 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.1 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.3 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.2 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.5 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +2.6 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.4 | +2.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.8 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -6.6 | -7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.1 | -7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.0 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.1 | -4.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.8 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 2 binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:234,604,269-234,610,178 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LRIR2, IRF-2BP2 |
| Gene groups (HGNC) | RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5L9](https://www.uniprot.org/uniprotkb/Q7Z5L9) (Interferon regulatory factor 2-binding protein 2):

> Acts as a transcriptional corepressor in a IRF2-dependent manner; this repression is not mediated by histone deacetylase activities. Represses the NFAT1-dependent transactivation of NFAT-responsive promoters. Acts as a coactivator of VEGFA expression in cardiac and skeletal muscles. Plays a role in immature B-cell differentiation.

**Summary**, from NCBI Gene [359948](https://www.ncbi.nlm.nih.gov/gene/359948):

> This gene encodes an interferon regulatory factor-2 (IRF2) binding protein that interacts with the C-terminal transcriptional repression domain of IRF2. Alternative splicing results in multiple transcript variants encoding distinct isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21729) · Entrez [359948](https://www.ncbi.nlm.nih.gov/gene/359948) · UniProt [Q7Z5L9](https://www.uniprot.org/uniprotkb/Q7Z5L9) · Ensembl [ENSG00000168264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168264)

## Data

Gene col 9620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9620); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9620]; `tensor/DDL_lfc|DDL_z.npy` [9620]; `embed/gene_vectors.npy` [9620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9620 or target_col == 9620). Every well: [[IRF2BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF2BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
