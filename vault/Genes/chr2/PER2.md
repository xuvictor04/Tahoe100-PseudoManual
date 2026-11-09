---
symbol: "PER2"
type: "gene"
col: 5299
ensembl_id: "ENSG00000132326"
name: "period circadian regulator 2"
location: "2q37.3"
module: 14
arm: "+"
pooled_cpm: 67.52
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 40
n_dd_up_clean: 12
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PER2

*period circadian regulator 2* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.69× (z +25.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM: 0.265× (z -18.4, q 0e+00, down in 48 of 49 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Megestrol (drug)]] 5 µM: 0.430× (z -16.5, q 0e+00, down in 48 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HES1]] (+0.67, fdr 7e-06), [[NR4A3]] (+0.64, fdr 7e-06), [[REL]] (+0.64, fdr 7e-06); moves opposite to [[OTULIN]] (-0.61, fdr 1e-05), [[AHSA1]] (-0.59, fdr 1e-05), [[LSP1P4]] (-0.59, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5299.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.69×** | +25.6 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.11×** | +15.1 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.67×** | +13.6 | 9e-40 | 47/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.3 | 6e-23 | 37/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.99×** | +9.5 | 2e-19 | 42/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.60×** | +9.3 | 2e-18 | 44/49 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +9.2 | 2e-18 | 36/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +9.2 | 3e-18 | 43/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.5 | 4e-12 | 35/48 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +6.5 | 6e-09 | 34/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +5.2 | 1e-05 | 32/48 (BT-474, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.015 | 25/48 (A-172, A-427, …) | all doses, stronger at high dose | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.64×** | +3.6 | 0.015 | 23/48 (SNU-423, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.4 | 0.024 | 19/48 (SHP-77, HS-578T, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.099 | 17/48 (NCI-H1792, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5299.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.265×** | -18.4 | 0e+00 | 48/49 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Megestrol (drug)]] 5 µM |  | **0.430×** | -16.5 | 0e+00 | 48/49 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.357×** | -14.2 | 9e-44 | 43/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.491×** | -9.8 | 1e-20 | 39/48 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -9.6 | 1e-19 | 35/48 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.554×** | -8.2 | 3e-14 | 38/48 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -7.8 | 6e-13 | 36/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.673×** | -7.8 | 6e-13 | 34/48 (PANC-1, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -7.7 | 1e-12 | 26/39 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.594×** | -7.2 | 3e-11 | 33/48 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.585×** | -7.0 | 1e-10 | 35/48 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -6.8 | 5e-10 | 34/48 (SNU-423, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -6.1 | 4e-08 | 30/49 (SW1417, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.645×** | -6.1 | 5e-08 | 30/48 (NCI-H1573, LS 180, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.626×** | -6.0 | 7e-08 | 30/43 (RKO, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.668×** | -5.6 | 8e-07 | 34/48 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.666×** | -5.4 | 2e-06 | 32/50 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.590×** | -5.2 | 6e-06 | 32/48 (LS 180, HT-29, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.777×** | -4.9 | 2e-05 | 28/49 (NCI-H1573, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.702×** | -4.9 | 3e-05 | 32/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.702×** | -4.9 | 3e-05 | 24/47 (NCI-H460, LS 180, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -4.5 | 1e-04 | 26/48 (Hs 766T, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5299. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 197 | 3 | 13 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.3) | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -14.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.262× (z -13.1) |
| [[HOP62 (line)]] | alt | 111 | 4 | 11 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +16.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.113× (z -19.2) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.319× (z -14.2) |
| [[PANC-1 (line)]] | alt | 37.0 | 8 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +30.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.164× (z -18.2) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.394× (z -13.3) |
| [[HEC-1-A (line)]] | alt | 56.2 | 7 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +26.4) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.136× (z -19.5) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.322× (z -15.7) |
| [[LoVo (line)]] | wt | 76.5 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +15.7) | [[Auranofin (drug)]] 5 µM 0.371× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 86.3 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +16.2) | [[Auranofin (drug)]] 5 µM 0.290× (z -11.3) |
| [[SNU-423 (line)]] | alt | 76.0 | 1 | 8 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.9) | [[Megestrol (drug)]] 5 µM 0.279× (z -14.5) |
| [[SW1417 (line)]] | alt | 70.9 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +21.1) | [[Megestrol (drug)]] 5 µM 0.341× (z -14.7) |
| [[A549 (line)]] | wt | 119 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.380× (z -10.7) |
| [[A-172 (line)]] | wt | 41.5 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +21.9) | [[Megestrol (drug)]] 5 µM 0.251× (z -14.9) |
| [[SHP-77 (line)]] | alt | 112 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.1) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.196× (z -14.3) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.300× (z -10.6) |
| [[KATO III (line)]] | alt | 71.5 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +9.8) | [[Auranofin (drug)]] 5 µM 0.312× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +17.7) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.204× (z -12.3) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.332× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 21.7 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +22.3) | — |
| [[SW480 (line)]] | alt | 63.6 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.2) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.337× (z -8.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -8.6) |
| [[A498 (line)]] | wt | 43.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.170× (z -15.0) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.330× (z -13.2) |
| [[H4 (line)]] | wt | 77.0 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +16.8) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.105× (z -15.1) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.281× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 58.1 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +10.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.103× (z -14.8) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.304× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 35.1 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +17.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.128× (z -14.9) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.349× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 70.5 | 2 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.52× (z +10.5) | [[Megestrol (drug)]] 5 µM 0.270× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 36.5 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.02× (z +22.4) | [[Megestrol (drug)]] 5 µM 0.318× (z -13.2) |
| [[HT-29 (line)]] | alt | 94.2 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +11.8) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.265× (z -9.1) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.265× (z -9.1) |
| [[LS 180 (line)]] | wt | 115 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.230× (z -10.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.247× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 93.3 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +15.1) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.116× (z -16.5) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.279× (z -13.9) |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +13.6) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.0626× (z -16.9) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.259× (z -11.6) |
| [[A-427 (line)]] | wt | 19.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +10.5) | [[Megestrol (drug)]] 5 µM 0.337× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 74.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +15.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.252× (z -9.0) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.398× (z -8.5) |
| [[C-33 A (line)]] | alt | 40.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +15.1) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 29.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +9.3) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.191× (z -10.7) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.344× (z -9.7) |
| [[COLO 205 (line)]] | alt | 114 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +14.9) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.230× (z -9.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 69.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +15.5) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.240× (z -10.2) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.421× (z -8.8) |
| [[HS-578T (line)]] | alt | 37.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +14.4) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.137× (z -14.3) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.256× (z -13.9) |
| [[SNU-1 (line)]] | wt | 55.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +18.0) | — |
| [[SW 1088 (line)]] | alt | 71.1 | 0 | 3 (1 ⚠) | — | [[Megestrol (drug)]] 5 µM 0.107× (z -9.9) |
| [[SW 900 (line)]] | alt | 76.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.1) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.195× (z -10.2) ⚠ unreliable plate only · without an alert: [[Megestrol (drug)]] 5 µM 0.371× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.245× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +12.5) | [[Auranofin (drug)]] 5 µM 0.278× (z -8.8) |
| [[Hs 766T (line)]] | wt | 94.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.162× (z -13.4) |
| [[J82 (line)]] | alt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +16.1) | — |
| [[Panc 03.27 (line)]] | alt | 72.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.221× (z -10.5) |
| [[RKO (line)]] | wt | 46.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.9) | [[Dinaciclib (drug)]] 0.05 µM 0.235× (z -11.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 47.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +16.0) | [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM 0.187× (z -9.3) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 80.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 74.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.7) | — |
| [[CHP-212 (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 91.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5299), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[NR4A3]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[REL]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[BHLHE41]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 | pathway: Circadian clock; STRING 999 |
| [[KLF10]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[MAK]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FOS]] | +0.59 | +0.63 / +0.57 | both halves | 1e-05 | STRING 656 |
| [[MEF2C]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 | pathway: Circadian clock |
| [[VDR]] | +0.58 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[BCL3]] | +0.57 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[TEF]] | +0.57 | +0.55 / +0.52 | both halves | 1e-05 | STRING 772 |
| [[GATA6]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTULIN]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.59 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[LSP1P4]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[DIP2A]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[ATP2C1]] | -0.58 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RNF13]] | -0.58 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[CACYBP]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[SLC38A9]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TANGO2]] | -0.55 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[CHORDC1]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TPD52L2]] | -0.54 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA9]] | B | CA9 activity raises PER2's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without CA9 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[GATA6]] | B | GATA6 activity raises PER2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without GATA6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[TXNIP]] | B | TXNIP activity raises PER2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.88× lower at baseline in the lines without TXNIP | 0.012 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PER2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LGALS3]] | B | LGALS3 activity raises PER2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without LGALS3 | 0.063 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[NR4A2]] | B | NR4A2 activity raises PER2's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without NR4A2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SOX9]] | B | SOX9 activity raises PER2's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without SOX9 | 0.066 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[SPINK5]] | B | SPINK5 activity raises PER2's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without SPINK5 | 0.069 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[RUSC2]] | C | RUSC2 activity lowers PER2's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 1.66× higher at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |
| [[IKBKE]] | C | IKBKE activity raises PER2's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without IKBKE | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.3, 1.9); signed map (6.6, 26.6). **Vector** length 128, 42.8% of its response variance represented; |z| ≥ 3 in 1,669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.2 | +25.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.3 | +15.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.5 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.7 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +0.5 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | -0.2 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -9.2 | -4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.9 | -14.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -8.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.7 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -7.7 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -7.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | period circadian regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,244,044-238,290,102 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0347 |
| Gene groups (HGNC) | PAS domain containing; Period circadian regulator family |
| Reactome | 9 pathways, smallest: AMP and AMPK regulate the circadian clock; Phosphorylation of CLOCK, acetylation of BMAL1 (ARNTL) at target gene promoters; Phosphorylation and nuclear translocation of the CRY:PER:kinase complex |
| Matched by | ensembl_id |

**Function**, from UniProt [O15055](https://www.uniprot.org/uniprotkb/O15055) (Period circadian protein homolog 2):

> Transcriptional repressor which forms a core component of the circadian clock. The circadian clock, an internal time-keeping system, regulates various physiological processes through the generation of approximately 24 hour circadian rhythms in gene expression, which are translated into rhythms in metabolism and behavior. It is derived from the Latin roots 'circa' (about) and 'diem' (day) and acts as an important regulator of a wide array of physiological functions including metabolism, sleep, …

**Summary**, from NCBI Gene [8864](https://www.ncbi.nlm.nih.gov/gene/8864):

> This gene is a member of the Period family of genes and is expressed in a circadian pattern in the suprachiasmatic nucleus, the primary circadian pacemaker in the mammalian brain. Genes in this family encode components of the circadian rhythms of locomotor activity, metabolism, and behavior. This gene is upregulated by CLOCK/ARNTL heterodimers but then represses this upregulation in a feedback loop using PER/CRY heterodimers to interact with CLOCK/ARNTL. Polymorphisms in this gene may increase …

**Accessions** — [HGNC:8846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8846) · Entrez [8864](https://www.ncbi.nlm.nih.gov/gene/8864) · UniProt [O15055](https://www.uniprot.org/uniprotkb/O15055) · Ensembl [ENSG00000132326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132326)

## Data

Gene col 5299: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5299); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5299, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5299]; `tensor/DDL_lfc|DDL_z.npy` [5299]; `embed/gene_vectors.npy` [5299]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5299 or target_col == 5299). Every well: [[PER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PER2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
