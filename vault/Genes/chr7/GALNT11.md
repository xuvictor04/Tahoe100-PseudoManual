---
symbol: "GALNT11"
type: "gene"
col: 10912
ensembl_id: "ENSG00000178234"
name: "polypeptide N-acetylgalactosaminyltransferase 11"
location: "7q36.1"
module: 30
arm: "+"
pooled_cpm: 101.86
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 25
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# GALNT11

*polypeptide N-acetylgalactosaminyltransferase 11* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.07× (z +4.9, q 6e-04, up in 0 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.97×, NCI-H1573 2.61×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.470× (z -21.1, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXL2]] (+0.64, fdr 7e-06), [[HSDL1]] (+0.63, fdr 1e-05), [[MCRIP1]] (+0.62, fdr 1e-05); moves opposite to [[DLG2]] (-0.56, fdr 4e-05), [[HNRNPA2B1]] (-0.55, fdr 1e-05), [[TASOR]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 1.97×, NCI-H1573 2.61×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.9 | 6e-04 | 0/48 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.5 | 0.002 | 27/46 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.17× | +4.5 | 0.002 | 18/46 (RKO, A498, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.22×** | +3.8 | 0.021 | 25/45 (C32, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.18× | +3.3 | 0.10 | 16/46 (RKO, A498, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.21× | +3.2 | 0.13 | 12/48 (NCI-H460, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.16 | 17/45 (RKO, H4, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 5 µM |  | 1.12× | +3.0 | 0.16 | 8/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.34× | +3.0 | 0.16 | 15/47 (RKO, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 17 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10912.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.470×** | -21.1 | 0e+00 | 43/47 (SW1417, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.452×** | -15.1 | 0e+00 | 36/42 (NCI-H1573, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.621×** | -13.3 | 4e-38 | 35/46 (A549, C32, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.641×** | -12.4 | 3e-33 | 37/46 (SW1417, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.518×** | -12.0 | 3e-31 | 37/43 (RKO, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.564×** | -11.3 | 1e-27 | 39/47 (Panc 03.27, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.617×** | -9.5 | 1e-19 | 39/46 (SW480, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -9.5 | 1e-19 | 39/46 (A549, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.648×** | -8.3 | 1e-14 | 38/46 (HS-578T, A498, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.657×** | -8.0 | 9e-14 | 32/48 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.699×** | -6.8 | 6e-10 | 30/45 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -6.6 | 2e-09 | 34/46 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.718×** | -6.5 | 3e-09 | 34/46 (A549, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -6.2 | 2e-08 | 34/46 (HOP62, CFPAC-1, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.561×** | -6.0 | 9e-08 | 27/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.763×** | -5.4 | 3e-06 | 27/46 (CFPAC-1, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.817×** | -3.8 | 0.004 | 23/46 (HOP62, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.704×** | -3.6 | 0.006 | 20/46 (HS-578T, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.852× | -3.0 | 0.049 | 17/47 (HS-578T, RPMI-7951, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 88.2 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -21.0) |
| [[HOP62 (line)]] | alt | 101 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 207 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -18.5) |
| [[C32 (line)]] | wt | 196 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -21.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -14.6) |
| [[A549 (line)]] | wt | 125 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -21.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.208× (z -18.5) |
| [[SW480 (line)]] | alt | 84.3 | 0 | 7 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.321× (z -15.7) |
| [[CFPAC-1 (line)]] | alt | 79.3 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -18.7) |
| [[PANC-1 (line)]] | alt | 128 | 1 (1 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -18.2) |
| [[SNU-423 (line)]] | alt | 98.2 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -17.8) |
| [[SW1417 (line)]] | alt | 109 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -22.9) |
| [[A-172 (line)]] | wt | 114 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.355× (z -11.5) |
| [[Hs 766T (line)]] | wt | 117 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 100 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -20.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -13.9) |
| [[RKO (line)]] | wt | 122 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 96.4 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -14.5) |
| [[J82 (line)]] | alt | 79.2 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 79.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -18.8) |
| [[RPMI-7951 (line)]] | alt | 85.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.306× (z -10.7) |
| [[SW48 (line)]] | wt | 146 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.354× (z -9.7) |
| [[A498 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -19.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 95.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -17.1) |
| [[C-33 A (line)]] | alt | 174 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -9.3) |
| [[LoVo (line)]] | wt | 117 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -15.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1573 (line)]] | alt | 49.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.5) |
| [[NCI-H2030 (line)]] | alt | 91.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -17.3) |
| [[NCI-H23 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -12.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 121 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.407× (z -12.0) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 84.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -16.3) |
| [[BT-474 (line)]] | alt | 102 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -14.0) |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.415× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 86.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -18.8) |
| [[NCI-H2347 (line)]] | alt | 76.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -16.3) |
| [[SNU-1 (line)]] | wt | 138 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.482× (z -10.0) |
| [[SW 1088 (line)]] | alt | 183 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0565× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 82.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HT-29 (line)]] | alt | 78.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -10.1) |
| [[LS 180 (line)]] | wt | 77.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.374× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SK-MEL-2 (line)]] | alt | 97.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 1271 (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[AN3 CA (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 50.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL2]] | +0.64 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[HSDL1]] | +0.63 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[MCRIP1]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[STARD9]] | +0.62 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC15A4]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[KCTD7]] | +0.61 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[SNN]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[IAH1]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[DENND6A]] | +0.57 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[GNPTAB]] | +0.56 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[IL17RD]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PKN1]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLG2]] | -0.56 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[TASOR]] | -0.54 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[MYH15]] | -0.51 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[LIX1-AS1]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ADAMTS3]] | -0.50 | -0.61 / -0.32 | both halves | 2e-04 | pathway: O-linked glycosylation |
| [[CHD4]] | -0.50 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[KLHL3]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[MZF1-AS1]] | -0.49 | -0.61 / -0.23 | both halves | 5e-04 |  |
| [[SON]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CAPS2]] | -0.48 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[SLFN12]] | -0.48 | -0.52 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GALNT11's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[STARD9]] | B | STARD9 activity strengthens GALNT11's drug response | lines that do not express STARD9 (7) vs lines expressing it (41) | the lines without STARD9 respond 0.60× as strongly (z diff +2.30); strongest at Homoharringtonine 5 µM: 1.11x vs 0.56x (z diff +8.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: DZIP1L, FMNL3, HEG1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-3.3, -2.1); signed map (-37.8, -2.6). **Vector** length 101, 30.8% of its response variance represented; |z| ≥ 3 in 1,115 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | +5.3 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.1 | -2.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +1.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +0.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.3 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.9 | -8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -12.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -6.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:152,025,674-152,122,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T11 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCW6](https://www.uniprot.org/uniprotkb/Q8NCW6) (Polypeptide N-acetylgalactosaminyltransferase 11):

> Polypeptide N-acetylgalactosaminyltransferase that catalyzes the initiation of protein O-linked glycosylation and is involved in left/right asymmetry by mediating O-glycosylation of NOTCH1. O-glycosylation of NOTCH1 promotes activation of NOTCH1, modulating the balance between motile and immotile (sensory) cilia at the left-right organiser (LRO). Polypeptide N-acetylgalactosaminyltransferases catalyze the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the …

**Summary**, from NCBI Gene [63917](https://www.ncbi.nlm.nih.gov/gene/63917):

> Enables Notch binding activity and polypeptide N-acetylgalactosaminyltransferase activity. Predicted to be involved in several processes, including Notch receptor processing; Notch signaling involved in heart development; and regulation of Notch signaling pathway. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19875) · Entrez [63917](https://www.ncbi.nlm.nih.gov/gene/63917) · UniProt [Q8NCW6](https://www.uniprot.org/uniprotkb/Q8NCW6) · Ensembl [ENSG00000178234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178234)

## Data

Gene col 10912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10912); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10912]; `tensor/DDL_lfc|DDL_z.npy` [10912]; `embed/gene_vectors.npy` [10912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10912 or target_col == 10912). Every well: [[GALNT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
