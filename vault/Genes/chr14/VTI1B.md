---
symbol: "VTI1B"
type: "gene"
col: 1987
ensembl_id: "ENSG00000100568"
name: "vesicle transport through interaction with t-SNAREs 1B"
location: "14q24.1"
module: 171
arm: "+"
pooled_cpm: 44.93
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# VTI1B

*vesicle transport through interaction with t-SNAREs 1B* — 14q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +25.6, q 0e+00, up in 43 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 2.49×, HOP62 3.47×, PANC-1 2.98×, HEC-1-A 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 3.97×, PANC-1 3.26×, SNU-423 3.45×, A498 3.11×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.27×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.573× (z -25.0, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIZ1]] (+0.69, fdr 7e-06), [[PRPF8]] (+0.68, fdr 7e-06), [[TSN]] (+0.68, fdr 7e-06); moves opposite to [[ERVK3-1]] (-0.65, fdr 1e-05), [[FOXA2]] (-0.64, fdr 3e-05), [[TUBB4B]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 2.49×, HOP62 3.47×, PANC-1 2.98×, HEC-1-A 3.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H1573 3.97×, PANC-1 3.26×, SNU-423 3.45×, A498 3.11×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.27×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +25.6 | 0e+00 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +24.7 | 0e+00 | 37/41 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +17.4 | 0e+00 | 35/44 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +8.1 | 6e-14 | 28/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +4.6 | 4e-04 | 14/48 (KATO III, CFPAC-1, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.12× | +3.6 | 0.033 | 10/48 (CFPAC-1, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.11× | +3.2 | 0.11 | 5/48 (SNU-423, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -25.0 | 0e+00 | 44/47 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.595×** | -16.4 | 0e+00 | 44/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.601×** | -15.5 | 0e+00 | 42/48 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -14.8 | 0e+00 | 38/47 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -12.8 | 2e-35 | 39/48 (SW 900, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -11.6 | 3e-29 | 35/48 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -11.5 | 7e-29 | 33/47 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.709×** | -10.9 | 1e-25 | 32/48 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.821×** | -8.9 | 5e-17 | 26/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -8.6 | 7e-16 | 30/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -7.7 | 1e-12 | 26/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.793×** | -7.3 | 1e-11 | 23/48 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.815×** | -6.5 | 4e-09 | 21/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.834× | -5.8 | 3e-07 | 16/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.859× | -4.8 | 5e-05 | 14/48 (SW 900, BT-474, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.911× | -4.2 | 0.001 | 12/48 (A-427, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 0.873× | -4.0 | 0.002 | 13/47 (J82, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.884× | -3.9 | 0.003 | 10/48 (SNU-1, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 66.8 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.05× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -17.0) |
| [[PANC-1 (line)]] | alt | 37.8 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +15.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 55.0 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -16.2) |
| [[SW480 (line)]] | alt | 58.0 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +14.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.508× (z -11.0) |
| [[HOP62 (line)]] | alt | 36.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -12.8) |
| [[LoVo (line)]] | wt | 41.4 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -16.0) |
| [[SNU-423 (line)]] | alt | 36.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.1) |
| [[A549 (line)]] | wt | 42.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.7) |
| [[H4 (line)]] | wt | 48.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.6) ⚠ toxic; transcription drop | [[Hydroxyfasudil (drug)]] 5 µM 0.0806× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 40.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +13.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 33.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +13.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 48.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.97× (z +15.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 78.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 38.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.98× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -9.7) |
| [[A498 (line)]] | wt | 28.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +12.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 42.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.8) |
| [[BT-474 (line)]] | alt | 44.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.370× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -9.3) |
| [[COLO 205 (line)]] | alt | 37.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.2) |
| [[HS-578T (line)]] | alt | 35.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -8.7) |
| [[KATO III (line)]] | alt | 41.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 47.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 42.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 43.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 87.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 62.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -9.6) |
| [[RKO (line)]] | wt | 52.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -8.8) |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.289× (z -10.5) |
| [[A-172 (line)]] | wt | 25.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -11.2) |
| [[C32 (line)]] | wt | 42.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 30.0 | 0 | 1 | — | [[Berbamine (drug)]] 0.5 µM 0.0690× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.19× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 53.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.410× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0903× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 48.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIZ1]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[PRPF8]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[TSN]] | +0.68 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[AGO1]] | +0.68 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TMEM183A]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[OPA1]] | +0.67 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.66 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SAMM50]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Protein localization |
| [[API5]] | +0.65 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[TSFM]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[LONP2]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 | pathway: Protein localization |
| [[RTF2]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERVK3-1]] | -0.65 | -0.69 / -0.57 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.64 | -0.45 / -0.65 | both halves | 3e-05 |  |
| [[TUBB4B]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[IRX5]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[TOPORS]] | -0.55 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[METTL23]] | -0.55 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RBX1]] | -0.54 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[TSC22D1]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[SERTAD1]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[ERF]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises VTI1B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-21.4, -15.4); signed map (-32.2, -26.9). **Vector** length 87.2, 18.9% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +25.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +24.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +17.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +1.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +1.6 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.2 | -7.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | vesicle transport through interaction with t-SNAREs 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.1 — chr14:67,647,085-67,674,820 (-) |
| Ensembl biotype | protein_coding |
| Also known as | VTI2 |
| Gene groups (HGNC) | SNAREs |
| Reactome | 6 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UEU0](https://www.uniprot.org/uniprotkb/Q9UEU0) (Vesicle transport through interaction with t-SNAREs homolog 1B):

> SNAREs (soluble N-ethylmaleimide-sensitive factor-attachment protein receptors) are essential proteins for intracellular membrane fusion. SNAREs localized on opposing membranes assemble to form a trans-SNARE complex, an extended, parallel four-helix bundle whose assembly releases energy that drives membrane fusion. The core SNARE complex typically consists of four alpha-helical domains, three from target membrane SNAREs (t-SNAREs) and one from a vesicle SNARE (v-SNARE). On late endosomes, …

**Summary**, from NCBI Gene [10490](https://www.ncbi.nlm.nih.gov/gene/10490):

> Enables SNARE binding activity and chloride channel inhibitor activity. Involved in regulation of protein localization to plasma membrane. Located in several cellular components, including endosome membrane; lysosomal membrane; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17793](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17793) · Entrez [10490](https://www.ncbi.nlm.nih.gov/gene/10490) · UniProt [Q9UEU0](https://www.uniprot.org/uniprotkb/Q9UEU0) · Ensembl [ENSG00000100568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100568)

## Data

Gene col 1987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1987); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1987]; `tensor/DDL_lfc|DDL_z.npy` [1987]; `embed/gene_vectors.npy` [1987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1987 or target_col == 1987). Every well: [[VTI1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VTI1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
