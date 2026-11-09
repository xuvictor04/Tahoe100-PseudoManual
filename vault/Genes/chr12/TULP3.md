---
symbol: "TULP3"
type: "gene"
col: 1215
ensembl_id: "ENSG00000078246"
name: "TUB like protein 3"
location: "12p13.33"
module: 40
arm: "+"
pooled_cpm: 85.15
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# TULP3

*TUB like protein 3* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.09× (z +5.9, q 2e-06, up in 3 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.21× (z +4.0, q 0.015, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.29×; ⚠ position not correctable); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 2.92×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 1.93×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 1.91×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.438× (z -16.6, q 0e+00, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.583× (z -10.8, q 3e-25, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2]] (+0.74, fdr 7e-06), [[RAB6A]] (+0.73, fdr 7e-06), [[SLC17A5]] (+0.73, fdr 7e-06); moves opposite to [[TRIM44]] (-0.72, fdr 7e-06), [[YWHAE]] (-0.67, fdr 7e-06), [[TMEM185B]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM106A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1215.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.29×; ⚠ position not correctable); [[Auranofin (drug)]] 5 µM in 1 line (BT-474 2.92×); [[Belinostat (drug)]] 5 µM in 1 line (SW480 1.93×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SW480 1.91×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +5.9 | 2e-06 | 3/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.015 | 21/48 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.17× | +3.3 | 0.21 | 12/48 (C32, HOP62, …) | two highest doses | position effect removed |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.13× | +3.2 | 0.21 | 7/48 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.24 | 16/50 (SW480, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1215.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.438×** | -16.6 | 0e+00 | 38/44 (HCT15, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.483×** | -15.2 | 0e+00 | 43/49 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.511×** | -13.0 | 2e-36 | 40/45 (SNU-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.583×** | -10.8 | 3e-25 | 38/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -10.5 | 2e-23 | 45/49 (HS-578T, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.649×** | -9.1 | 1e-17 | 37/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.728×** | -8.2 | 2e-14 | 30/48 (HS-578T, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.705×** | -7.3 | 2e-11 | 34/48 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.737×** | -6.4 | 1e-08 | 35/48 (SNU-1, A-172, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -6.1 | 7e-08 | 28/48 (SNU-1, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -5.7 | 7e-07 | 31/48 (RPMI-7951, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.825×** | -5.4 | 3e-06 | 23/48 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | **0.793×** | -4.7 | 1e-04 | 25/47 (CHP-212, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.802×** | -4.6 | 1e-04 | 24/48 (CFPAC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.813×** | -4.2 | 0.001 | 21/47 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.821×** | -4.1 | 0.001 | 22/48 (AsPC-1, HOP62, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.833×** | -3.8 | 0.004 | 22/49 (A549, LoVo, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.831×** | -3.6 | 0.010 | 20/47 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.4 | 0.020 | 18/48 (NCI-H1573, LoVo, …) | top dose only |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.852× | -3.4 | 0.021 | 15/49 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.038 | 18/48 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.051 | 10/49 (NCI-H1573, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1215. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 107 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -25.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -14.8) |
| [[A498 (line)]] | wt | 113 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.379× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.470× (z -10.2) |
| [[HOP62 (line)]] | alt | 130 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.518× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 84.3 | 0 | 6 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.196× (z -10.5) |
| [[SW 900 (line)]] | alt | 122 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.359× (z -10.9) |
| [[SW480 (line)]] | alt | 102 | 2 (1 ⚠) | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 1.93× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.91× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -18.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 80.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -16.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.293× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 84.4 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.152× (z -12.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.317× (z -11.8) |
| [[SNU-423 (line)]] | alt | 70.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 171 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -21.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -9.3) |
| [[H4 (line)]] | wt | 139 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -16.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 146 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.279× (z -15.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 71.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.453× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 86.9 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.163× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 67.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 80.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.125× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.477× (z -9.0) |
| [[C32 (line)]] | wt | 58.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -16.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 169 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0410× (z -27.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 86.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 68.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 102 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -16.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 92.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -16.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 90.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -9.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 54.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.92× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -18.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 42.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.2) ⚠ unreliable plate only |
| [[CHP-212 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0945× (z -10.3) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[hTERT-HPNE (line)]] | wt | 75.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 75.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 72.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.165× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 60.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.357× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 52.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.472× (z -8.5) |
| [[RKO (line)]] | wt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -15.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 82.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1215), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | +0.74 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[RAB6A]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[PMM1]] | +0.73 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[SDHAP2]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[SWI5]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[CDK2AP2]] | +0.71 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ABHD18]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[IFT20]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 | STRING 571 |
| [[WIPI1]] | +0.70 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.70 | +0.68 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM44]] | -0.72 | -0.70 / -0.69 | both halves | 7e-06 |  |
| [[YWHAE]] | -0.67 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[TMEM185B]] | -0.66 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[FAT1]] | -0.65 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[ATIC]] | -0.64 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[UTP20]] | -0.63 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[MTMR2]] | -0.63 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[BTBD1]] | -0.63 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[DHX9]] | -0.63 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[HNRNPK]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[RRP15]] | -0.62 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[SRFBP1]] | -0.62 | -0.57 / -0.68 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM106A]] | B | TMEM106A activity raises TULP3's level | lines that do not express TMEM106A (5) vs lines expressing it (45) | 1.47× lower at baseline in the lines without TMEM106A | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (9.5, -34.5); signed map (-46.4, 12.7). **Vector** length 132, 40.3% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.5 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.8 | +2.9 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -13.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.0 | -10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.1 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.4 | -9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.3 | -15.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -6.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | TUB like protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:2,877,223-2,941,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TUBL3 |
| Reactome | 2 pathways, smallest: Hedgehog 'off' state; Signaling by Hedgehog |
| Matched by | ensembl_id |

**Function**, from UniProt [O75386](https://www.uniprot.org/uniprotkb/O75386) (Tubby-related protein 3):

> Protein-protein adapter that drives transport of G protein-coupled receptors into primary cilia by mediating association between the intraflagellar transport complex A (IFT-A) and G protein-coupled receptors FFAR4, GPR45 and GPR161. Acts as a negative regulator of the Shh signaling by promoting trafficking of GPR161 to cilia. During adipogenesis, regulates ciliary trafficking of FFAR4 in preadipocytes. Promotes transport of GPR45 into primary cilia of neurons in paraventricular nucleus (PVN) of …

**Summary**, from NCBI Gene [7289](https://www.ncbi.nlm.nih.gov/gene/7289):

> This gene encodes a member of the tubby gene family of bipartite transcription factors. Members of this family have been identified in plants, vertebrates, and invertebrates, and they share a conserved N-terminal transcription activation region and a conserved C-terminal DNA and phosphatidylinositol-phosphate binding region. The encoded protein binds to phosphoinositides in the plasma membrane via its C-terminal region and probably functions as a membrane-bound transcription regulator that …

**Accessions** — [HGNC:12425](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12425) · Entrez [7289](https://www.ncbi.nlm.nih.gov/gene/7289) · UniProt [O75386](https://www.uniprot.org/uniprotkb/O75386) · Ensembl [ENSG00000078246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078246)

## Data

Gene col 1215: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1215); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1215, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1215]; `tensor/DDL_lfc|DDL_z.npy` [1215]; `embed/gene_vectors.npy` [1215]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1215 or target_col == 1215). Every well: [[TULP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TULP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
