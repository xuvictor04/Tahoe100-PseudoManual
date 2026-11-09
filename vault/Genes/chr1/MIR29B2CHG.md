---
symbol: "MIR29B2CHG"
type: "gene"
col: 12779
ensembl_id: "ENSG00000203709"
name: "MIR29B2 and MIR29C host gene"
location: "1q32.2"
module: 30
arm: "+"
pooled_cpm: 47.49
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# MIR29B2CHG

*MIR29B2 and MIR29C host gene* — 1q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.68× (z +9.7, q 2e-19, up in 35 of 47 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.45× (z +4.9, q 1e-04, up in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 7 lines (LS 180 5.30×, LoVo 3.63×, HEC-1-A 3.22×, SW1417 3.15×, …; ⚠ cell-cycle shift, explains ~48% of this change); [[Selinexor (drug)]] 0.5 µM in 4 lines (LS 180 5.16×, HEC-1-A 3.74×, LoVo 3.34×, KATO III 4.07×; ⚠ cell-cycle shift, explains ~59% of this change); [[Selinexor (drug)]] 0.05 µM in 3 lines (LS 180 4.67×, LoVo 3.32×, HCT15 4.84×; ⚠ cell-cycle shift, explains ~33% of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.284× (z -16.1, q 0e+00, down in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.527× (z -11.9, q 3e-30, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN2]] (+0.65, fdr 1e-05), [[CAPN5]] (+0.64, fdr 7e-06), [[VPS37D]] (+0.62, fdr 1e-05); moves opposite to [[P2RY11]] (-0.55, fdr 2e-05), [[ERCC6L2]] (-0.54, fdr 2e-05), [[CDKN2B-AS1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 7 lines (LS 180 5.30×, LoVo 3.63×, HEC-1-A 3.22×, SW1417 3.15×, …; ⚠ cell-cycle shift, explains ~48% of this change); [[Selinexor (drug)]] 0.5 µM in 4 lines (LS 180 5.16×, HEC-1-A 3.74×, LoVo 3.34×, KATO III 4.07×; ⚠ cell-cycle shift, explains ~59% of this change); [[Selinexor (drug)]] 0.05 µM in 3 lines (LS 180 4.67×, LoVo 3.32×, HCT15 4.84×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.68×** | +9.7 | 2e-19 | 35/47 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.73×** | +7.3 | 1e-10 | 36/48 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.69×** | +7.0 | 6e-10 | 33/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.45×** | +4.9 | 1e-04 | 27/47 (LS 180, COLO 205, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.015 | 20/46 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.18× | +3.1 | 0.16 | 15/47 (COLO 205, J82, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.284×** | -16.1 | 0e+00 | 40/45 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.316×** | -14.6 | 1e-45 | 33/37 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.527×** | -11.9 | 3e-30 | 39/48 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.475×** | -9.0 | 2e-17 | 32/40 (NCI-H2347, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.503×** | -9.0 | 2e-17 | 30/47 (A549, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.511×** | -8.5 | 2e-15 | 39/44 (NCI-H2347, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.641×** | -8.2 | 2e-14 | 29/47 (A498, A549, …) | two highest doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.573×** | -7.3 | 2e-11 | 31/47 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.613×** | -6.4 | 8e-09 | 32/46 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.608×** | -6.3 | 2e-08 | 29/48 (NCI-H2347, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.623×** | -6.2 | 3e-08 | 32/45 (SNU-1, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.626×** | -6.1 | 4e-08 | 30/47 (J82, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.659×** | -5.5 | 2e-06 | 29/47 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.759×** | -5.1 | 1e-05 | 23/47 (HOP62, Hs 766T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.500×** | -4.8 | 7e-05 | 25/48 (COLO 205, MIA PaCa-2, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.509×** | -4.6 | 1e-04 | 27/44 (CHP-212, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 5 µM |  | **0.806×** | -4.0 | 0.002 | 25/47 (H4, MIA PaCa-2, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.605×** | -3.4 | 0.013 | 18/46 (SW 900, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.014 | 19/47 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.619×** | -3.3 | 0.020 | 22/44 (HT-29, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.622×** | -3.2 | 0.023 | 17/47 (SW 900, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.032 | 18/47 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.789×** | -3.1 | 0.035 | 17/48 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.804×** | -2.8 | 0.071 | 15/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.860× | -2.8 | 0.088 | 14/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.804×** | -2.7 | 0.095 | 14/48 (LS 180, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 71.8 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -12.5) |
| [[HOP62 (line)]] | alt | 49.2 | 0 | 10 (7 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.121× (z -15.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -15.1) |
| [[COLO 205 (line)]] | alt | 170 | 1 (1 ⚠) | 8 (7 ⚠) | [[Selinexor (drug)]] 5 µM 2.18× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -18.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -14.2) |
| [[A498 (line)]] | wt | 45.3 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -25.9) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 1 (1 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 2.56× (z +9.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 5 µM 0.0576× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0976× (z -16.7) |
| [[LoVo (line)]] | wt | 28.8 | 3 (3 ⚠) | 4 (4 ⚠) | [[Selinexor (drug)]] 5 µM 3.63× (z +14.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -15.0) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 122 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0612× (z -27.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -19.8) |
| [[A-172 (line)]] | wt | 37.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -14.6) |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -13.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -9.8) |
| [[A549 (line)]] | wt | 40.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -23.7) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 53.7 | 2 (2 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 3.22× (z +13.1) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0576× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 42.8 | 3 (3 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 5.30× (z +18.5) ⚠ cell-cycle shift, explains ~48% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -11.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SW1417 (line)]] | alt | 68.2 | 2 (2 ⚠) | 3 (3 ⚠) | [[Selinexor (drug)]] 5 µM 3.15× (z +13.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 96.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 48.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.5) |
| [[HCT15 (line)]] | alt | 33.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.97× (z +11.9) ⚠ cell-cycle shift, explains ~48% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -12.2) ⚠ cell-cycle shift, explains ~58% of this change |
| [[J82 (line)]] | alt | 78.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0933× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.440× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 58.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.5) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0927× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 40.8 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.2) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.7) |
| [[Panc 03.27 (line)]] | alt | 63.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.3) ⚠ cell-cycle shift, explains ~78% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.8) |
| [[A-427 (line)]] | wt | 27.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 46.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -8.6) |
| [[HT-29 (line)]] | alt | 40.8 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.59× (z +9.0) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[KATO III (line)]] | alt | 31.1 | 3 (3 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 3.65× (z +12.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 3 (2 ⚠) | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0575× (z -18.0) |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -8.9) |
| [[SW 900 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -8.5) |
| [[CHP-212 (line)]] | wt | 47.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +8.9) ⚠ cell-cycle shift, explains ~78% of this change | [[Docetaxel (drug)]] 0.05 µM 0.0932× (z -9.2) ⚠ transcription drop; cell-cycle shift, explains ~90% of this change |
| [[Hs 766T (line)]] | wt | 51.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.277× (z -8.5) |
| [[SNU-1 (line)]] | wt | 122 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0866× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[H4 (line)]] | wt | 13.1 | 0 | 1 | — | [[Thymol (drug)]] 5 µM 0.178× (z -9.4) |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.295× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0443× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -11.4) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SW480 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.67× (z +11.5) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[C-33 A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN2]] | +0.65 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[CAPN5]] | +0.64 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[VPS37D]] | +0.62 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF138]] | +0.62 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[TMEM185A]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[UNC119]] | +0.61 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TRPM4]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[NDFIP1]] | +0.59 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[RTCA]] | +0.59 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[FAM241B]] | +0.58 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[FBXO44]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[MAP4K2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RY11]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.54 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CDKN2B-AS1]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[USP34]] | -0.53 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PKP4]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[STAG1]] | -0.51 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[TUG1]] | -0.51 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[SECISBP2]] | -0.50 | -0.64 / -0.36 | both halves | 1e-04 |  |
| [[ASXL2]] | -0.50 | -0.62 / -0.36 | both halves | 1e-04 |  |
| [[RFX3]] | -0.49 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[BPTF]] | -0.49 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[MED1]] | -0.48 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MIR29B2CHG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (2.4, -8.2); signed map (-25.8, -6.1). **Vector** length 105, 29.4% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +11.5 | +9.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | +7.9 | +7.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.6 | +7.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +4.7 | +4.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.9 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.7 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -5.0 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.9 | -7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.5 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.8 | -6.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Thymol (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -2.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | MIR29B2 and MIR29C host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q32.2 — chr1:207,760,650-207,879,115 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ35650; previously C1orf132 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100128537](https://www.ncbi.nlm.nih.gov/gene/100128537):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32018](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32018) · Entrez [100128537](https://www.ncbi.nlm.nih.gov/gene/100128537) · Ensembl [ENSG00000203709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203709)

## Data

Gene col 12779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12779); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12779]; `tensor/DDL_lfc|DDL_z.npy` [12779]; `embed/gene_vectors.npy` [12779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12779 or target_col == 12779). Every well: [[MIR29B2CHG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR29B2CHG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
