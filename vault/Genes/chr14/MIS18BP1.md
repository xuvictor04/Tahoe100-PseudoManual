---
symbol: "MIS18BP1"
type: "gene"
col: 4985
ensembl_id: "ENSG00000129534"
name: "MIS18 binding protein 1"
location: "14q21.2"
module: 67
arm: "+"
pooled_cpm: 165.71
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# MIS18BP1

*MIS18 binding protein 1* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.69× (z +10.1, q 3e-21, up in 45 of 48 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 1.41× (z +3.4, q 0.037, up in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 7 lines (NCI-H460 2.91×, LS 180 3.08×, LoVo 2.89×, KATO III 2.92×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.58×, LS 180 3.30×, LoVo 3.03×, PANC-1 2.44×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 2.36×; ⚠ cell-cycle shift, explains ~40% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -11.7, q 4e-29, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTK]] (+0.84, fdr 7e-06), [[NUF2]] (+0.81, fdr 7e-06), [[CDC25C]] (+0.78, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Digitoxin (drug)]] 5 µM in 7 lines (NCI-H460 2.91×, LS 180 3.08×, LoVo 2.89×, KATO III 2.92×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (KATO III 3.58×, LS 180 3.30×, LoVo 3.03×, PANC-1 2.44×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 2.36×; ⚠ cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.69×** | +10.1 | 3e-21 | 45/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.66×** | +9.8 | 5e-20 | 44/48 (KATO III, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.44×** | +7.0 | 4e-10 | 39/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.43×** | +6.9 | 6e-10 | 37/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.85×** | +6.2 | 6e-08 | 41/47 (SW48, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.43×** | +5.4 | 7e-06 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.39×** | +5.0 | 4e-05 | 27/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.30×** | +4.8 | 1e-04 | 30/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.037 | 20/48 (A498, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.13× | +3.4 | 0.043 | 8/48 (CFPAC-1, SW48, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.3 | 0.050 | 16/49 (HT-29, SW1417, …) | top dose only |  |
| [[Naproxen (drug)]] 5 µM |  | 1.18× | +3.1 | 0.095 | 15/48 (A-172, NCI-H460, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4985.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -11.7 | 4e-29 | 42/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.549×** | -11.6 | 2e-28 | 48/48 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.717×** | -9.1 | 2e-17 | 39/48 (A498, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.669×** | -7.4 | 1e-11 | 30/44 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **0.780×** | -6.8 | 2e-09 | 31/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.907× | -6.4 | 2e-08 | 1/50 (SW 1088) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.694×** | -5.6 | 2e-06 | 29/49 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -5.2 | 1e-05 | 28/48 (LS 180, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.766×** | -5.1 | 2e-05 | 30/48 (A-427, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.767×** | -5.1 | 2e-05 | 33/48 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.756×** | -5.1 | 2e-05 | 31/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.609×** | -5.0 | 3e-05 | 34/48 (HEC-1-A, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.609×** | -5.0 | 3e-05 | 33/48 (NCI-H2347, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.772×** | -4.8 | 6e-05 | 29/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.787×** | -4.6 | 2e-04 | 28/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.641×** | -4.5 | 3e-04 | 28/48 (HEC-1-A, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.646×** | -4.4 | 3e-04 | 27/48 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.2 | 9e-04 | 25/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.662×** | -4.2 | 9e-04 | 27/48 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.679×** | -3.9 | 0.002 | 27/47 (AsPC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.819×** | -3.8 | 0.003 | 24/49 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.003 | 21/48 (SHP-77, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 123 | 0 | 9 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 118 | 4 (4 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -15.2) |
| [[A-172 (line)]] | wt | 84.8 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -12.4) |
| [[A-427 (line)]] | wt | 219 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.406× (z -15.0) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.569× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 290 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 227 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.409× (z -14.2) ⚠ unreliable plate only · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.650× (z -9.6) |
| [[KATO III (line)]] | alt | 129 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +14.4) ⚠ cell-cycle shift, explains ~45% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.421× (z -9.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 195 | 2 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.8) ⚠ cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.454× (z -12.6) ⚠ cell-cycle shift, explains ~94% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.6) |
| [[LS 180 (line)]] | wt | 150 | 2 (2 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +13.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 217 | 3 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.57× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -12.4) |
| [[SHP-77 (line)]] | alt | 358 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -9.9) |
| [[SW1417 (line)]] | alt | 140 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.93× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -11.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 251 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.357× (z -11.5) ⚠ unreliable plate only · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.538× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 177 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 63.4 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.29× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[LoVo (line)]] | wt | 95.8 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +12.8) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 261 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.74× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[PANC-1 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.2) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RKO (line)]] | wt | 258 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -9.4) |
| [[SW 900 (line)]] | alt | 214 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -12.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 195 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +8.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -10.9) |
| [[A549 (line)]] | wt | 161 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -10.0) |
| [[C32 (line)]] | wt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -8.8) |
| [[H4 (line)]] | wt | 105 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -11.3) |
| [[HCT15 (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 245 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 81.3 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.39× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H2030 (line)]] | alt | 249 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.390× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 297 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.414× (z -11.8) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 227 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.587× (z -10.6) ⚠ cell-cycle shift, explains ~94% of this change |
| [[SK-MEL-2 (line)]] | alt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.8) |
| [[SNU-1 (line)]] | wt | 190 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.2) |
| [[BT-474 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 168 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 97.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 266 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTK]] | +0.84 | +0.80 / +0.81 | both halves | 7e-06 | STRING 844 |
| [[NUF2]] | +0.81 | +0.78 / +0.80 | both halves | 7e-06 | STRING 708 |
| [[CDC25C]] | +0.78 | +0.80 / +0.79 | both halves | 7e-06 | pathway: Cyclin A/B1/B2 associated events during G2/M transition |
| [[PARPBP]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[OIP5]] | +0.77 | +0.76 / +0.78 | both halves | 7e-06 | pathway: Chromosome Maintenance; STRING 999 |
| [[NDC80]] | +0.77 | +0.72 / +0.79 | both halves | 7e-06 | STRING 615 |
| [[STIL]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PBK]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[CIT]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[CEP152]] | +0.76 | +0.77 / +0.69 | both halves | 7e-06 | pathway: G2/M Transition |
| [[CDCA3]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[KIF22]] | +0.75 | +0.76 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIS18BP1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.830). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.2, -54.6); signed map (-47.3, -40.2). **Vector** length 149, 55.8% of its response variance represented; |z| ≥ 3 in 1,333 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.70 to 12); *G2/M checkpoint* (hallmark, mean cos +0.69 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.68 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +1.3 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +6.0 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.9 | +10.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -2.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.3 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -11.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -4.2 |
|  | [[EX229 (drug)]] 5 µM |  | -6.4 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | -6.4 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.3 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.2 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -9.1 |

## What is on record

|  |  |
|---|---|
| Name | MIS18 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:45,203,190-45,253,540 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M18BP1, FLJ11186, KIAA1903, KNL2; previously C14orf106 |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Reactome | 8 pathways, smallest: Cyclin A/B1/B2 associated events during G2/M transition; Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P0N0](https://www.uniprot.org/uniprotkb/Q6P0N0) (Mis18-binding protein 1):

> Required for recruitment of CENPA to centromeres and normal chromosome segregation during mitosis.

**Summary**, from NCBI Gene [55320](https://www.ncbi.nlm.nih.gov/gene/55320):

> Predicted to enable DNA binding activity. Predicted to be involved in CENP-A containing chromatin assembly and obsolete pericentric heterochromatin organization. Predicted to be located in nucleoplasm. Predicted to be part of CENP-A recruiting complex. Predicted to be active in chromosome, centromeric region. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20190) · Entrez [55320](https://www.ncbi.nlm.nih.gov/gene/55320) · UniProt [Q6P0N0](https://www.uniprot.org/uniprotkb/Q6P0N0) · Ensembl [ENSG00000129534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129534)

## Data

Gene col 4985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4985); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4985]; `tensor/DDL_lfc|DDL_z.npy` [4985]; `embed/gene_vectors.npy` [4985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4985 or target_col == 4985). Every well: [[MIS18BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIS18BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
