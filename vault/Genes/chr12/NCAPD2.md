---
symbol: "NCAPD2"
type: "gene"
col: 205
ensembl_id: "ENSG00000010292"
name: "non-SMC condensin I complex subunit D2"
location: "12p13.31"
module: 22
arm: "+"
pooled_cpm: 106.66
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 28
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# NCAPD2

*non-SMC condensin I complex subunit D2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.80× (z +11.3, q 8e-27, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.562× (z -11.1, q 8e-26, down in 44 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.440× (z -8.2, q 2e-14, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOP2A]] (+0.91, fdr 7e-06), [[BUB1]] (+0.91, fdr 7e-06), [[DLGAP5]] (+0.90, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.80×** | +11.3 | 8e-27 | 41/48 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +11.0 | 1e-25 | 40/48 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.72×** | +10.4 | 3e-23 | 40/48 (KATO III, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.36×** | +8.3 | 1e-14 | 30/48 (NCI-H2030, RKO, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.53×** | +8.1 | 5e-14 | 34/49 (A549, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **1.46×** | +7.0 | 2e-10 | 31/44 (A-172, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.28×** | +6.6 | 3e-09 | 33/48 (RKO, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.40×** | +6.5 | 7e-09 | 34/48 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.3 | 2e-08 | 26/48 (NCI-H2347, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | **1.37×** | +6.1 | 5e-08 | 30/48 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.37×** | +6.0 | 9e-08 | 33/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +5.9 | 2e-07 | 29/48 (LoVo, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.66×** | +5.1 | 2e-05 | 29/49 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.30×** | +4.9 | 4e-05 | 23/48 (RKO, Panc 03.27, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.27×** | +4.6 | 2e-04 | 27/48 (KATO III, SHP-77, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +4.2 | 7e-04 | 22/48 (RKO, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 21/48 (A549, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.033 | 19/47 (HOP62, NCI-H23, …) | all doses, flat | low cells (technical?) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.12× | +3.0 | 0.054 | 10/48 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Furosemide (drug)]] 0.5 µM |  | 1.16× | +2.8 | 0.088 | 15/48 (LS 180, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.562×** | -11.1 | 8e-26 | 44/48 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.584×** | -10.3 | 1e-22 | 43/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.646×** | -8.4 | 9e-15 | 38/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.440×** | -8.2 | 2e-14 | 38/48 (PANC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.749×** | -7.9 | 4e-13 | 35/48 (A-427, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.618×** | -7.8 | 7e-13 | 36/48 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -7.7 | 8e-13 | 37/48 (NCI-H23, A-427, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.513×** | -6.7 | 1e-09 | 38/48 (NCI-H1792, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -6.7 | 1e-09 | 34/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.732×** | -6.0 | 1e-07 | 33/48 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.569×** | -5.7 | 7e-07 | 32/48 (H4, KATO III, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.748×** | -5.4 | 4e-06 | 28/48 (NCI-H1573, A549, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.590×** | -5.3 | 5e-06 | 31/48 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.762×** | -5.2 | 7e-06 | 31/48 (SW48, SNU-1, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.754×** | -5.2 | 7e-06 | 29/48 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.830×** | -5.1 | 1e-05 | 20/48 (RKO, Hs 766T, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.619×** | -4.8 | 4e-05 | 28/48 (NCI-H2030, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.791×** | -4.5 | 2e-04 | 26/48 (A-427, A498, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.854× | -4.3 | 4e-04 | 21/48 (A498, SW48, …) | top dose only | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.741×** | -4.1 | 1e-03 | 22/48 (NCI-H1792, A498, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.863× | -4.0 | 0.001 | 19/48 (A-427, H4, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 5 µM |  | 0.863× | -4.0 | 0.001 | 16/49 (Panc 03.27, HEC-1-A, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.004 | 20/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.721×** | -3.3 | 0.021 | 15/48 (HOP62, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 99.3 | 7 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.30× (z +19.5) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.35× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.433× (z -8.8) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 165 | 4 (3 ⚠) | 2 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.5) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -14.1) |
| [[A498 (line)]] | wt | 98.4 | 2 (2 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.22× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | [[Selinexor (drug)]] 5 µM 0.321× (z -18.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.560× (z -9.6) |
| [[A549 (line)]] | wt | 96.1 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.66× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 150 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.576× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 106 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.491× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 128 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +22.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.15× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 358 | 1 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.72× (z +9.0) ⚠ cell-cycle shift, explains ~49% of this change | [[Selinexor (drug)]] 5 µM 0.553× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.515× (z -8.7) |
| [[RKO (line)]] | wt | 116 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.58× (z +22.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.76× (z +10.4) | — |
| [[A-172 (line)]] | wt | 49.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | — |
| [[A-427 (line)]] | wt | 420 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.340× (z -19.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 66.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.69× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 39.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.297× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 116 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 122 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.508× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 62.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.265× (z -9.5) |
| [[HCT15 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.297× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.405× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 66.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.521× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 89.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.389× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 93.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.295× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 165 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.487× (z -9.5) |
| [[AN3 CA (line)]] | alt | 142 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 106 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 85.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 75.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP2A]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 686 |
| [[BUB1]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 683 |
| [[DLGAP5]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 763 |
| [[TPX2]] | +0.90 | +0.91 / +0.87 | both halves | 7e-06 | STRING 600 |
| [[PRR11]] | +0.89 | +0.91 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[BIRC5]] | +0.88 | +0.90 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 581 |
| [[MKI67]] | +0.88 | +0.90 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 453 |
| [[KIF11]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | STRING 860 |
| [[NUSAP1]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 654 |
| [[KIF18A]] | +0.88 | +0.89 / +0.84 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[INCENP]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 685 |
| [[KIF2C]] | +0.87 | +0.92 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 619 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises NCAPD2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without NEURL1B | 0.058 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIMREG]] | B | PIMREG activity raises NCAPD2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without PIMREG | 0.088 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72D]] | C | FAM72D activity raises NCAPD2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.57× lower at baseline in the lines without FAM72D | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent; its own permutation p |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises NCAPD2's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.40× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent genes |
| [[AURKB]] | C | AURKB activity raises NCAPD2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without AURKB | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity strengthens NCAPD2's drug response | lines that do not express NDC80 (3) vs lines expressing it (46) | the lines without NDC80 respond 0.73× as strongly (z diff +1.28); strongest at Selinexor 5 µM: 0.99x vs 0.67x (z diff +4.8) | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.917). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.2, -55.6); signed map (-49.5, -43.0). **Vector** length 161, 58.5% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.73 to 60); *DREAM G2/M down* (control, mean cos +0.81 to 28); *Mitotic Metaphase and Anaphase* (reactome, mean cos +0.71 to 41).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.9 | +5.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +4.9 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~92% of this change | +4.8 | +6.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | +4.8 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | +4.7 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.2 | +4.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +3.1 | +3.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.8 | +1.9 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.6 | +2.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -10.5 | -10.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.4 | -11.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | -10.2 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -9.7 | -7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.3 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -8.1 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -6.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.2 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.0 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin I complex subunit D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,493,356-6,531,955 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CNAP1, hCAP-D2, CAP-D2, KIAA0159 |
| Gene groups (HGNC) | Condensin I subunits; Armadillo like helical domain containing |
| Hallmark sets | E2F_TARGETS |
| Reactome | 5 pathways, smallest: Condensation of Prometaphase Chromosomes; Mitotic Prometaphase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15021](https://www.uniprot.org/uniprotkb/Q15021) (Condensin complex subunit 1):

> Regulatory subunit of the condensin complex, a complex required for conversion of interphase chromatin into mitotic-like condense chromosomes. The condensin complex probably introduces positive supercoils into relaxed DNA in the presence of type I topoisomerases and converts nicked DNA into positive knotted forms in the presence of type II topoisomerases. May target the condensin complex to DNA via its C-terminal domain. May promote the resolution of double-strand DNA catenanes (intertwines) …

**Summary**, from NCBI Gene [9918](https://www.ncbi.nlm.nih.gov/gene/9918):

> Enables histone binding activity. Involved in mitotic chromosome condensation and positive regulation of chromosome condensation. Located in condensed chromosome; cytosol; and nuclear lumen. Part of condensin complex. Implicated in primary autosomal recessive microcephaly 21. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24305) · Entrez [9918](https://www.ncbi.nlm.nih.gov/gene/9918) · UniProt [Q15021](https://www.uniprot.org/uniprotkb/Q15021) · Ensembl [ENSG00000010292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010292)

## Data

Gene col 205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 205); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 205]; `tensor/DDL_lfc|DDL_z.npy` [205]; `embed/gene_vectors.npy` [205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 205 or target_col == 205). Every well: [[NCAPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
