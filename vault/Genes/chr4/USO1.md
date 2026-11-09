---
symbol: "USO1"
type: "gene"
col: 6232
ensembl_id: "ENSG00000138768"
name: "USO1 vesicle transport factor"
location: "4q21.1"
module: 42
arm: "+"
pooled_cpm: 144.08
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 28
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# USO1

*USO1 vesicle transport factor* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.45× (z +8.1, q 3e-13, up in 30 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SNU-423 2.43×, NCI-H2347 2.41×, RKO 2.27×, HepG2/C3A 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 2.81×, PANC-1 1.80×, C-33 A 2.20×, A549 2.14×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.31×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.399× (z -20.8, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.479× (z -16.7, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP72]] (+0.76, fdr 7e-06), [[ARCN1]] (+0.72, fdr 7e-06), [[HDLBP]] (+0.69, fdr 7e-06); moves opposite to [[CARHSP1]] (-0.50, fdr 1e-04), [[CDAN1]] (-0.49, fdr 4e-05), [[MFSD14CP]] (-0.49, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6232.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SNU-423 2.43×, NCI-H2347 2.41×, RKO 2.27×, HepG2/C3A 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 2.81×, PANC-1 1.80×, C-33 A 2.20×, A549 2.14×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H1573 2.31×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +8.1 | 3e-13 | 30/44 (Panc 03.27, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +5.3 | 3e-05 | 29/49 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +4.1 | 0.009 | 21/48 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.34 | 10/48 (A549, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6232.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.399×** | -20.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.479×** | -16.7 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -13.4 | 7e-39 | 43/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.572×** | -12.7 | 1e-34 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.575×** | -12.5 | 6e-34 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.596×** | -11.7 | 7e-30 | 46/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.698×** | -11.5 | 7e-29 | 31/48 (J82, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -10.7 | 5e-25 | 42/48 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.627×** | -10.6 | 2e-24 | 43/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -9.4 | 3e-19 | 44/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.661×** | -9.4 | 4e-19 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -8.4 | 2e-15 | 36/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.697×** | -7.9 | 1e-13 | 38/47 (HCT15, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.801×** | -7.1 | 5e-11 | 29/49 (A549, CHP-212, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.757×** | -6.3 | 1e-08 | 29/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.652×** | -5.1 | 1e-05 | 30/48 (SW 1271, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.794×** | -4.9 | 2e-05 | 29/48 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.792×** | -4.5 | 2e-04 | 24/47 (SNU-423, SW480, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -4.3 | 4e-04 | 15/48 (RKO, PANC-1, …) | top dose only |  |
| [[Flutamide (drug)]] 0.5 µM |  | **0.832×** | -4.2 | 7e-04 | 21/48 (AsPC-1, Hs 766T, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.712×** | -4.0 | 0.001 | 24/49 (NCI-H1573, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.002 | 26/48 (C32, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.857× | -3.5 | 0.010 | 18/48 (A549, SNU-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 221 | 2 (2 ⚠) | 11 (7 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.31× (z +11.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.239× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.342× (z -14.3) |
| [[PANC-1 (line)]] | alt | 142 | 2 (2 ⚠) | 10 (5 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.80× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.306× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -18.0) |
| [[KATO III (line)]] | alt | 243 | 0 | 11 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.318× (z -12.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.366× (z -11.2) |
| [[SW480 (line)]] | alt | 170 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.270× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -18.6) |
| [[H4 (line)]] | wt | 208 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.159× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.273× (z -13.5) |
| [[SW48 (line)]] | wt | 187 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.349× (z -10.9) |
| [[BT-474 (line)]] | alt | 338 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.346× (z -13.8) |
| [[HS-578T (line)]] | alt | 146 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -15.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.480× (z -9.5) |
| [[SNU-1 (line)]] | wt | 140 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.377× (z -10.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 81.1 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -17.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.437× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.418× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.479× (z -11.1) |
| [[RKO (line)]] | wt | 152 | 1 (1 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.236× (z -9.0) |
| [[HCT15 (line)]] | alt | 216 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -12.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[LoVo (line)]] | wt | 214 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 204 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.309× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 140 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.416× (z -10.1) |
| [[A549 (line)]] | wt | 114 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.14× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[AsPC-1 (line)]] | alt | 118 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.415× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.433× (z -9.0) |
| [[SHP-77 (line)]] | alt | 96.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -13.0) |
| [[HOP62 (line)]] | alt | 145 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.288× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.414× (z -11.4) |
| [[HT-29 (line)]] | alt | 197 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.347× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.486× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 187 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.298× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.458× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 109 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.81× (z +12.5) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.379× (z -11.7) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 138 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.418× (z -9.6) |
| [[SW 900 (line)]] | alt | 123 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.360× (z -11.2) |
| [[SW1417 (line)]] | alt | 108 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.378× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -9.7) |
| [[C-33 A (line)]] | alt | 144 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +9.1) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.453× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[C32 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -8.8) |
| [[CHP-212 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -10.4) ⚠ cell-cycle shift, explains ~23% of this change |
| [[Hs 766T (line)]] | wt | 172 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.421× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 153 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.02× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.479× (z -9.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 100 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -10.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 80.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +10.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.320× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -11.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[A-427 (line)]] | wt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.88× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -8.6) ⚠ cell-cycle shift, explains ~23% of this change |
| [[CFPAC-1 (line)]] | alt | 94.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.468× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[HepG2_C3A (line)]] | wt | 110 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +8.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 74.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.403× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.132× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 119 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 138 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP72]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[ARCN1]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 721 |
| [[HDLBP]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[YIPF6]] | +0.69 | +0.61 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[SRPRA]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[GOLGA3]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 | STRING 734 |
| [[COPB2]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 726 |
| [[SLC30A9]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ZBTB41]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SSR1]] | +0.61 | +0.59 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[CANX]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HSPA13]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[CDAN1]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MFSD14CP]] | -0.49 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[DCAF15]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[SMPD4BP]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NR2F6]] | -0.47 | -0.23 / -0.49 | both halves | 5e-04 |  |
| [[CYBA]] | -0.46 | -0.29 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.441). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.7, -17.0); signed map (-57.4, 10.1). **Vector** length 120, 42.2% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +6.7 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +1.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.1 | -5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.6 | +1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.2 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.1 | +1.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.7 | +2.1 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -20.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.4 | -13.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.3 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.9 | -4.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.8 | -4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.6 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | USO1 vesicle transport factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,724,577-75,814,286 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TAP, VDP, p115 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | PROTEIN_SECRETION, MTORC1_SIGNALING |
| Reactome | 12 pathways, smallest: Golgi Cisternae Pericentriolar Stack Reorganization; COPII-mediated vesicle transport; COPI-mediated anterograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O60763](https://www.uniprot.org/uniprotkb/O60763) (General vesicular transport factor p115):

> General vesicular transport factor required for intercisternal transport in the Golgi stack; it is required for transcytotic fusion and/or subsequent binding of the vesicles to the target membrane. May well act as a vesicular anchor by interacting with the target membrane and holding the vesicular and target membranes in proximity.

**Summary**, from NCBI Gene [8615](https://www.ncbi.nlm.nih.gov/gene/8615):

> The protein encoded by this gene is a peripheral membrane protein which recycles between the cytosol and the Golgi apparatus during interphase. It is regulated by phosphorylation: dephosphorylated protein associates with the Golgi membrane and dissociates from the membrane upon phosphorylation. Ras-associated protein 1 recruits this protein to coat protein complex II (COPII) vesicles during budding from the endoplasmic reticulum, where it interacts with a set of COPII vesicle-associated SNAREs …

**Accessions** — [HGNC:30904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30904) · Entrez [8615](https://www.ncbi.nlm.nih.gov/gene/8615) · UniProt [O60763](https://www.uniprot.org/uniprotkb/O60763) · Ensembl [ENSG00000138768](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138768)

## Data

Gene col 6232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6232); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6232]; `tensor/DDL_lfc|DDL_z.npy` [6232]; `embed/gene_vectors.npy` [6232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6232 or target_col == 6232). Every well: [[USO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
