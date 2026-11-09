---
symbol: "TCF3"
type: "gene"
col: 988
ensembl_id: "ENSG00000071564"
name: "transcription factor 3"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 51.93
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 15
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TCF3

*transcription factor 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.18× (z +16.1, q 0e+00, up in 40 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.29× (z +3.7, q 0.025, up in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 3.82×, SW480 2.84×, LoVo 2.79×, PANC-1 2.57×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 3.88×, KATO III 5.51×, NCI-H460 3.67×, SW480 2.79×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.425× (z -25.0, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.74, fdr 7e-06), [[CEP131]] (+0.73, fdr 1e-05), [[FBRSL1]] (+0.73, fdr 7e-06); moves opposite to [[FAM200A]] (-0.75, fdr 7e-06), [[TRMT1L]] (-0.70, fdr 7e-06), [[ZNF585A]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H460 3.82×, SW480 2.84×, LoVo 2.79×, PANC-1 2.57×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (LOX-IMVI 3.88×, KATO III 5.51×, NCI-H460 3.67×, SW480 2.79×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.18×** | +16.1 | 0e+00 | 40/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +15.8 | 0e+00 | 38/41 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +7.7 | 3e-12 | 28/45 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +4.0 | 0.008 | 20/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.025 | 14/47 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +3.3 | 0.100 | 16/47 (Panc 03.27, COLO 205, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.16× | +3.0 | 0.16 | 18/48 (LoVo, NCI-H1792, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | 1.16× | +3.0 | 0.16 | 14/47 (LoVo, SW1417, …) | top dose only |  |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.16× | +3.0 | 0.16 | 8/47 (A-172, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.425×** | -25.0 | 0e+00 | 44/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -15.7 | 0e+00 | 38/48 (A-427, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.490×** | -14.8 | 0e+00 | 41/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -10.4 | 6e-23 | 43/48 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.410×** | -9.6 | 7e-20 | 42/49 (Panc 03.27, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -8.0 | 1e-13 | 30/48 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.798×** | -6.6 | 3e-09 | 27/48 (HS-578T, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -5.9 | 2e-07 | 27/48 (HOP62, LS 180, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.752×** | -5.9 | 2e-07 | 28/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.819×** | -5.9 | 3e-07 | 24/48 (NCI-H2347, LS 180, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -5.4 | 3e-06 | 28/48 (LS 180, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.799×** | -4.7 | 2e-04 | 24/48 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.823×** | -4.0 | 0.002 | 21/48 (A-427, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.0 | 0.002 | 22/47 (HS-578T, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.698×** | -3.9 | 0.004 | 22/48 (hTERT-HPNE, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.852× | -3.2 | 0.047 | 13/47 (Hs 766T, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 72.1 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0531× (z -32.6) |
| [[LS 180 (line)]] | wt | 74.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.52× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -17.0) |
| [[MIA PaCa-2 (line)]] | alt | 99.2 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -18.9) |
| [[SW480 (line)]] | alt | 67.1 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -22.0) |
| [[A-172 (line)]] | wt | 111 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -20.2) |
| [[HS-578T (line)]] | alt | 72.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -16.2) |
| [[J82 (line)]] | alt | 51.1 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -15.3) |
| [[KATO III (line)]] | alt | 39.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 62.8 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -21.4) |
| [[SW1417 (line)]] | alt | 53.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.85× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.4) |
| [[A498 (line)]] | wt | 50.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.59× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 61.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -15.2) |
| [[HOP62 (line)]] | alt | 45.5 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -17.4) |
| [[HT-29 (line)]] | alt | 49.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -17.8) |
| [[LOX-IMVI (line)]] | wt | 59.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.88× (z +14.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 47.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -20.0) |
| [[PANC-1 (line)]] | alt | 42.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -8.7) |
| [[RKO (line)]] | wt | 62.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.7) |
| [[BT-474 (line)]] | alt | 60.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.1) |
| [[hTERT-HPNE (line)]] | wt | 49.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 32.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.3) |
| [[SNU-423 (line)]] | alt | 46.9 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -13.4) |
| [[A549 (line)]] | wt | 29.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 54.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +12.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.367× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 85.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.332× (z -11.5) |
| [[SHP-77 (line)]] | alt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.26× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 112 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -9.3) |
| [[C-33 A (line)]] | alt | 84.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.465× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.0) |
| [[HCT15 (line)]] | alt | 71.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -15.4) |
| [[Hs 766T (line)]] | wt | 34.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 31.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.38× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -10.2) |
| [[SW 900 (line)]] | alt | 34.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.269× (z -9.6) |
| [[AN3 CA (line)]] | alt | 86.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[CEP131]] | +0.73 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.73 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TBCD]] | +0.73 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.72 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[BRF1]] | +0.71 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[FAM20B]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[TRABD]] | +0.69 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[TPST2]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[TELO2]] | +0.69 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[AP2A2]] | +0.69 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[CORO7]] | +0.68 | +0.71 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM200A]] | -0.75 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[TRMT1L]] | -0.70 | -0.70 / -0.70 | both halves | 7e-06 |  |
| [[ZNF585A]] | -0.69 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[PPCS]] | -0.68 | -0.73 / -0.52 | both halves | 1e-05 |  |
| [[TIGD6]] | -0.68 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[METTL18]] | -0.68 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PATL2]] | -0.68 | -0.69 / -0.48 | both halves | 2e-05 |  |
| [[ZNF24]] | -0.67 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[HHLA3]] | -0.65 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[RPP25L]] | -0.65 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[SDSL]] | -0.65 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[DPH6-DT]] | -0.65 | -0.64 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TCF3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GNAZ]] | B | GNAZ activity raises TCF3's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.46× lower at baseline in the lines without GNAZ | 0.085 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.7, -23.6); signed map (-44.7, -8.9). **Vector** length 112, 30.6% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +16.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.2 | +3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.9 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -14.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -15.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.7 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,609,291-1,652,615 (-) |
| Ensembl biotype | protein_coding |
| Also known as | E2A, ITF1, MGC129647, MGC129648, bHLHb21, VDIR, E47, p75 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 23 pathways, smallest: TGFBR3 expression; Myogenesis; Signaling by TGFBR3 |
| Matched by | ensembl_id |

**Function**, from UniProt [P15923](https://www.uniprot.org/uniprotkb/P15923) (Transcription factor E2-alpha):

> Transcriptional regulator involved in the initiation of neuronal differentiation and mesenchymal to epithelial transition (By similarity). Heterodimers between TCF3 and tissue-specific basic helix-loop-helix (bHLH) proteins play major roles in determining tissue-specific cell fate during embryogenesis, like muscle or early B-cell differentiation (By similarity). Together with TCF15, required for the mesenchymal to epithelial transition (By similarity). Dimers bind DNA on E-box motifs: …

**Summary**, from NCBI Gene [6929](https://www.ncbi.nlm.nih.gov/gene/6929):

> This gene encodes a member of the E protein (class I) family of helix-loop-helix transcription factors. E proteins activate transcription by binding to regulatory E-box sequences on target genes as heterodimers or homodimers, and are inhibited by heterodimerization with inhibitor of DNA-binding (class IV) helix-loop-helix proteins. E proteins play a critical role in lymphopoiesis, and the encoded protein is required for B and T lymphocyte development. Deletion of this gene or diminished …

**Accessions** — [HGNC:11633](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11633) · Entrez [6929](https://www.ncbi.nlm.nih.gov/gene/6929) · UniProt [P15923](https://www.uniprot.org/uniprotkb/P15923) · Ensembl [ENSG00000071564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071564)

## Data

Gene col 988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 988); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 988]; `tensor/DDL_lfc|DDL_z.npy` [988]; `embed/gene_vectors.npy` [988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 988 or target_col == 988). Every well: [[TCF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
