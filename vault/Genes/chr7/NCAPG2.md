---
symbol: "NCAPG2"
type: "gene"
col: 7133
ensembl_id: "ENSG00000146918"
name: "non-SMC condensin II complex subunit G2"
location: "7q36.3"
module: 6
arm: "+"
pooled_cpm: 105.88
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NCAPG2

*non-SMC condensin II complex subunit G2* — 7q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.53× (z +7.4, q 6e-11, up in 32 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change. The strongest without an alert is [[Methotrexate (drug)]] 5 µM: 1.25× (z +3.9, q 0.004, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.529× (z -11.2, q 3e-26, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPK]] (+0.91, fdr 7e-06), [[MELK]] (+0.90, fdr 7e-06), [[POLQ]] (+0.89, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 18 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.53×** | +7.4 | 6e-11 | 32/49 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.49×** | +6.7 | 6e-09 | 30/44 (HT-29, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.44×** | +6.4 | 3e-08 | 31/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +6.1 | 2e-07 | 29/48 (RKO, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +5.9 | 3e-07 | 30/48 (NCI-H2347, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.35×** | +5.3 | 1e-05 | 29/48 (C32, SNU-423, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.23×** | +5.2 | 2e-05 | 27/48 (HT-29, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +4.9 | 5e-05 | 28/45 (RKO, C32, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +4.9 | 5e-05 | 27/48 (A549, RKO, …) | top dose only |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 1.19× | +4.4 | 8e-04 | 22/49 (HT-29, SW480, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.28×** | +4.3 | 8e-04 | 28/48 (MIA PaCa-2, SW48, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.26×** | +4.1 | 0.002 | 22/47 (H4, SNU-423, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.26×** | +4.1 | 0.002 | 22/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose |  |
| [[Methotrexate (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.004 | 20/48 (SW480, LoVo, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.004 | 22/48 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.018 | 17/48 (SW480, KATO III, …) | rises with dose | plate-row cell shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.20× | +3.0 | 0.077 | 16/48 (MIA PaCa-2, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.529×** | -11.2 | 3e-26 | 36/48 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.652×** | -10.6 | 1e-23 | 40/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.590×** | -9.3 | 3e-18 | 38/48 (H4, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -8.5 | 2e-15 | 34/49 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.620×** | -7.9 | 2e-13 | 41/48 (KATO III, A-427, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.716×** | -5.9 | 4e-07 | 27/48 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.720×** | -5.4 | 5e-06 | 28/48 (A-427, MIA PaCa-2, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.739×** | -5.3 | 8e-06 | 27/48 (RKO, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.743×** | -5.2 | 1e-05 | 31/48 (HEC-1-A, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.813×** | -5.1 | 1e-05 | 26/48 (LoVo, HCT15, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.575×** | -5.1 | 2e-05 | 33/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.739×** | -5.0 | 3e-05 | 32/49 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.756×** | -4.9 | 4e-05 | 29/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.607×** | -4.6 | 2e-04 | 28/45 (SHP-77, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.841× | -4.3 | 7e-04 | 14/48 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.852× | -4.0 | 0.002 | 15/49 (LoVo, Hs 766T, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.004 | 23/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.753×** | -3.6 | 0.011 | 15/48 (NCI-H661, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -3.5 | 0.011 | 13/48 (COLO 205, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.868× | -3.5 | 0.011 | 21/48 (A-427, SW48, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.812×** | -3.5 | 0.011 | 23/48 (HEC-1-A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.65 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 132 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -15.2) |
| [[LS 180 (line)]] | wt | 68.3 | 0 | 7 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -13.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.355× (z -10.3) |
| [[SW48 (line)]] | wt | 153 | 0 | 6 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.240× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.427× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 167 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -18.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.304× (z -13.9) |
| [[LoVo (line)]] | wt | 95.7 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.424× (z -11.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.327× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 77.4 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.297× (z -11.3) |
| [[A-172 (line)]] | wt | 76.8 | 0 | 4 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.235× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.262× (z -10.9) |
| [[H4 (line)]] | wt | 100 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.142× (z -12.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.172× (z -10.9) |
| [[HT-29 (line)]] | alt | 93.9 | 1 (1 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.73× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.410× (z -12.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[KATO III (line)]] | alt | 125 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.299× (z -11.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -10.7) |
| [[A498 (line)]] | wt | 147 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.360× (z -12.4) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.251× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.281× (z -10.8) |
| [[PANC-1 (line)]] | alt | 90.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.04× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 83.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -21.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.0) |
| [[HOP62 (line)]] | alt | 114 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -11.0) |
| [[Hs 766T (line)]] | wt | 84.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 236 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.425× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 96.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -10.3) |
| [[SW480 (line)]] | alt | 155 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.418× (z -10.2) |
| [[A549 (line)]] | wt | 83.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.348× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 52.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -9.0) |
| [[BT-474 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -9.2) |
| [[C32 (line)]] | wt | 144 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.343× (z -9.4) |
| [[HCT15 (line)]] | alt | 124 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -9.4) |
| [[HS-578T (line)]] | alt | 78.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 113 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.338× (z -10.4) |
| [[RKO (line)]] | wt | 89.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.83× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -14.5) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.463× (z -9.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[AN3 CA (line)]] | alt | 173 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPK]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 568 |
| [[MELK]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | STRING 728 |
| [[POLQ]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 |  |
| [[RRM2]] | +0.89 | +0.89 / +0.85 | both halves | 7e-06 | STRING 757 |
| [[MYBL2]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[SPC24]] | +0.88 | +0.88 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SPC25]] | +0.88 | +0.89 / +0.88 | both halves | 7e-06 | STRING 556 |
| [[ATAD2]] | +0.88 | +0.85 / +0.87 | both halves | 7e-06 | STRING 502 |
| [[EXO1]] | +0.88 | +0.87 / +0.85 | both halves | 7e-06 | STRING 613 |
| [[FANCI]] | +0.86 | +0.87 / +0.86 | both halves | 7e-06 | STRING 816 |
| [[FANCB]] | +0.86 | +0.87 / +0.81 | both halves | 7e-06 |  |
| [[TK1]] | +0.86 | +0.87 / +0.84 | both halves | 7e-06 | STRING 424 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 6, C 10. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises NCAPG2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.12× lower at baseline in the lines without TCF19 | 0.025 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises NCAPG2's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Temsirolimus) | 62% of the class's compounds vs 5.6% of all compounds | 0.028 | ⚠ off-target possible; 5 compounds |
| [[E2F8]] | B | E2F8 activity raises NCAPG2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.91× lower at baseline in the lines without E2F8 | 0.029 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises NCAPG2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without CDC25A | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises NCAPG2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without CDCA7 | 0.038 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises NCAPG2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without E2F2 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NCAPG2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without PBK | 0.004 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises NCAPG2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.97× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CENPP]] | C | CENPP activity raises NCAPG2's level | lines that do not express CENPP (4) vs lines expressing it (46) | 1.90× lower at baseline in the lines without CENPP | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ALDH1B1, EID2, ENSG00000284691; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NCAPG2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.11× lower at baseline in the lines without AURKB | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises NCAPG2's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.45× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises NCAPG2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.898). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.7, -46.6); signed map (-39.6, -43.8). **Vector** length 169, 62.6% of its response variance represented; |z| ≥ 3 in 1,502 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.67 to 65); *DNA strand elongation* (reactome, mean cos +0.70 to 28); *DNA Replication* (reactome, mean cos +0.69 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.3 | +5.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | +4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +6.1 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +5.2 | +4.4 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.1 | +5.2 |
|  | [[Methotrexate (drug)]] 5 µM |  | +3.8 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | +3.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +3.1 | +2.6 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.0 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -11.2 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.1 | -11.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -9.0 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -8.1 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.0 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -5.6 | -5.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin II complex subunit G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.3 — chr7:158,631,169-158,704,804 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20311, MTB, CAP-G2, hCAP-G2; previously LUZP5 |
| Gene groups (HGNC) | Condensin II subunits; Armadillo like helical domain containing |
| Reactome | 5 pathways, smallest: Condensation of Prophase Chromosomes; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XI2](https://www.uniprot.org/uniprotkb/Q86XI2) (Condensin-2 complex subunit G2):

> Regulatory subunit of the condensin-2 complex, a complex which establishes mitotic chromosome architecture and is involved in physical rigidity of the chromatid axis.

**Summary**, from NCBI Gene [54892](https://www.ncbi.nlm.nih.gov/gene/54892):

> This gene encodes a protein that belongs to the Condensin2nSMC family of proteins. The encoded protein is a regulatory subunit of the condensin II complex which, along with the condensin I complex, plays a role in chromosome assembly and segregation during mitosis. A similar protein in mouse is required for early development of the embryo. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:21904](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21904) · Entrez [54892](https://www.ncbi.nlm.nih.gov/gene/54892) · UniProt [Q86XI2](https://www.uniprot.org/uniprotkb/Q86XI2) · Ensembl [ENSG00000146918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146918)

## Data

Gene col 7133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7133); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7133]; `tensor/DDL_lfc|DDL_z.npy` [7133]; `embed/gene_vectors.npy` [7133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7133 or target_col == 7133). Every well: [[NCAPG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
