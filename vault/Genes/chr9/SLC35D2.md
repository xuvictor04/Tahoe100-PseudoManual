---
symbol: "SLC35D2"
type: "gene"
col: 5150
ensembl_id: "ENSG00000130958"
name: "solute carrier family 35 member D2"
location: "9q22.32"
module: 15
arm: "+"
pooled_cpm: 43.7
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SLC35D2

*solute carrier family 35 member D2* — 9q22.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Neratinib (maleate) (drug)]] 5 µM: 1.20× (z +5.6, q 1e-05, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.273× (z -27.7, q 0e+00, down in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.429× (z -25.6, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND10]] (+0.66, fdr 7e-06), [[SAP30L]] (+0.66, fdr 1e-05), [[ARL8A]] (+0.64, fdr 7e-06); moves opposite to [[EID1]] (-0.64, fdr 1e-05), [[ATP7A]] (-0.60, fdr 1e-05), [[AKAP11]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5150.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +5.6 | 1e-05 | 22/47 (SNU-423, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.31×** | +5.5 | 1e-05 | 26/46 (SW480, SNU-423, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 1e-04 | 19/46 (SW480, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.7 | 4e-04 | 18/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.004 | 17/47 (RKO, HT-29, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.5 | 0.038 | 12/47 (SW1417, SNU-423, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.044 | 12/46 (LOX-IMVI, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.17× | +3.3 | 0.058 | 13/46 (H4, LoVo, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.082 | 11/46 (NCI-H460, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.273×** | -27.7 | 0e+00 | 46/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.429×** | -25.6 | 0e+00 | 41/46 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.321×** | -24.3 | 0e+00 | 46/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.359×** | -21.9 | 0e+00 | 45/47 (SW480, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.454×** | -16.3 | 0e+00 | 40/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.531×** | -12.4 | 3e-33 | 38/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.592×** | -11.2 | 3e-27 | 39/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -10.8 | 3e-25 | 31/48 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **0.593×** | -10.8 | 3e-25 | 24/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.608×** | -10.7 | 9e-25 | 38/47 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **0.612×** | -10.5 | 4e-24 | 30/45 (SW480, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.732×** | -9.5 | 2e-19 | 34/47 (KATO III, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.674×** | -8.4 | 1e-15 | 30/47 (HOP62, NCI-H460, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **0.661×** | -8.2 | 1e-14 | 26/40 (SK-MEL-2, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.695×** | -7.5 | 2e-12 | 26/46 (A498, RKO, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -5.5 | 1e-06 | 24/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.764×** | -5.3 | 3e-06 | 21/46 (H4, HCT15, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.775×** | -5.0 | 2e-05 | 23/47 (KATO III, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.808×** | -4.5 | 1e-04 | 20/47 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.673×** | -4.4 | 2e-04 | 18/47 (A498, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.898× | -3.3 | 0.021 | 4/47 (SW 900, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.758×** | -3.1 | 0.034 | 12/47 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.877× | -2.8 | 0.084 | 6/47 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.61 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 68.4 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -28.8) |
| [[NCI-H460 (line)]] | wt | 35.9 | 0 | 13 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0676× (z -28.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.257× (z -20.9) |
| [[A498 (line)]] | wt | 66.9 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -19.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.342× (z -17.7) |
| [[A549 (line)]] | wt | 49.8 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.1) |
| [[LoVo (line)]] | wt | 41.6 | 4 (2 ⚠) | 4 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.24× (z +11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.01× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -15.6) |
| [[SW480 (line)]] | alt | 73.8 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -23.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.492× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 65.0 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -22.3) |
| [[HOP62 (line)]] | alt | 27.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.7) |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.0) |
| [[LS 180 (line)]] | wt | 52.9 | 1 (1 ⚠) | 6 (5 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.173× (z -16.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.121× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.188× (z -12.1) |
| [[SNU-423 (line)]] | alt | 43.2 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -16.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.345× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 68.4 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.138× (z -19.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.3) |
| [[J82 (line)]] | alt | 43.4 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.320× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 64.1 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -19.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 60.0 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -16.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.489× (z -9.9) |
| [[PANC-1 (line)]] | alt | 34.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -18.8) |
| [[RKO (line)]] | wt | 41.9 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -14.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.238× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 100 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.199× (z -15.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.390× (z -8.9) |
| [[Hs 766T (line)]] | wt | 58.0 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -14.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.282× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.5) |
| [[SW1417 (line)]] | alt | 65.0 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -17.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.466× (z -9.3) |
| [[COLO 205 (line)]] | alt | 63.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.7) |
| [[HT-29 (line)]] | alt | 53.1 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -17.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 43.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.1) |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 32.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.9) |
| [[SNU-1 (line)]] | wt | 51.4 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -13.9) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.8) |
| [[C32 (line)]] | wt | 31.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0970× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.7) |
| [[SW 1271 (line)]] | alt | 69.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.9) |
| [[SW48 (line)]] | wt | 44.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.162× (z -10.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.338× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[H4 (line)]] | wt | 18.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.127× (z -9.5) |
| [[A-427 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND10]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SAP30L]] | +0.66 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RP9P]] | +0.63 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[TMEM267]] | +0.63 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[PGLS-DT]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[DGKE]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ULK1]] | +0.60 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PPP1R26-AS1]] | +0.58 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.57 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[LARP6]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID1]] | -0.64 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[HNRNPC]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FAT1]] | -0.53 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[JUNB]] | -0.52 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[PRRC2A]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[YWHAE]] | -0.51 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[TTC30A]] | -0.51 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[NR4A3]] | -0.51 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CSRNP1]] | -0.51 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[IFT80]] | -0.50 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SLC35D2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.446). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-34.4, 18.5); signed map (-22.2, 6.6). **Vector** length 96.8, 25.9% of its response variance represented; |z| ≥ 3 in 1,251 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +4.9 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.6 | +4.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.2 | +3.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.8 | -11.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.6 | -10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -16.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -3.5 | -8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -9.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -5.3 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.4 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.32 — chr9:96,313,444-96,383,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UGTrel8, SQV7L |
| Gene groups (HGNC) | Solute carrier family 35 |
| Reactome | 14 pathways, smallest: Formation of the active cofactor, UDP-glucuronate; Transport of nucleotide sugars; Glucuronidation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q76EJ3](https://www.uniprot.org/uniprotkb/Q76EJ3) (Nucleotide sugar transporter SLC35D2):

> Nucleotide sugar antiporter transporting UDP-N-acetylglucosamine (UDP-GlcNAc) and UDP-glucose (UDP-Glc) from the cytosol into the lumen of the Golgi in exchange of UMP. By supplying UDP-N-acetylglucosamine, a donor substrate to heparan sulfate synthases, probably takes part in the synthesis of these glycoconjugates.

**Summary**, from NCBI Gene [11046](https://www.ncbi.nlm.nih.gov/gene/11046):

> Nucleotide sugars, which are synthesized in the cytosol or the nucleus, are high-energy donor substrates for glycosyltransferases located in the lumen of the endoplasmic reticulum and Golgi apparatus. Translocation of nucleotide sugars from the cytosol into the lumen compartment is mediated by specific nucleotide sugar transporters, such as SLC35D2 (Suda et al., 2004 [PubMed 15082721]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20799) · Entrez [11046](https://www.ncbi.nlm.nih.gov/gene/11046) · UniProt [Q76EJ3](https://www.uniprot.org/uniprotkb/Q76EJ3) · Ensembl [ENSG00000130958](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130958)

## Data

Gene col 5150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5150); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5150]; `tensor/DDL_lfc|DDL_z.npy` [5150]; `embed/gene_vectors.npy` [5150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5150 or target_col == 5150). Every well: [[SLC35D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
