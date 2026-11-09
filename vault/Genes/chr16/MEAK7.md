---
symbol: "MEAK7"
type: "gene"
col: 6469
ensembl_id: "ENSG00000140950"
name: "MTOR associated protein MEAK7"
location: "16q24.1"
module: 206
arm: "+"
pooled_cpm: 49.45
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# MEAK7

*MTOR associated protein MEAK7* — 16q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.31× (z +7.9, q 2e-12, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.489× (z -14.8, q 0e+00, down in 34 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.659× (z -12.2, q 7e-32, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP2C2-AS1]] (+0.60, fdr 7e-06, ⚠ read-through risk), [[SMS]] (+0.60, fdr 2e-05), [[MSANTD3]] (+0.59, fdr 7e-06), [[SMIM29]] (+0.59, fdr 1e-05); moves opposite to [[CMPK1]] (-0.55, fdr 4e-05), [[PON2]] (-0.55, fdr 2e-05), [[GTF2I]] (-0.54, fdr 5e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CLDN14-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.9 | 2e-12 | 23/47 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.22×** | +4.2 | 0.007 | 21/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.1 | 0.007 | 15/48 (LS 180, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +3.9 | 0.011 | 16/47 (AsPC-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.21×** | +3.9 | 0.011 | 17/48 (LS 180, NCI-H2030, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 1.19× | +3.7 | 0.023 | 12/48 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.043 | 11/48 (CFPAC-1, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.085 | 10/48 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.098 | 14/48 (A-427, A-172, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.1 | 0.098 | 17/48 (LoVo, LS 180, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.12 | 8/48 (NCI-H460, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.489×** | -14.8 | 0e+00 | 34/47 (A549, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.505×** | -13.6 | 1e-39 | 24/37 (A549, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -12.2 | 7e-32 | 38/47 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.557×** | -12.1 | 2e-31 | 38/48 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.566×** | -10.9 | 1e-25 | 29/40 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.640×** | -9.2 | 3e-18 | 30/48 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.658×** | -8.7 | 4e-16 | 31/48 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.693×** | -7.3 | 2e-11 | 29/48 (A-172, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.719×** | -6.5 | 4e-09 | 31/47 (J82, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.732×** | -6.2 | 3e-08 | 24/46 (MIA PaCa-2, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.749×** | -6.0 | 1e-07 | 26/48 (HOP62, H4, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.759×** | -5.7 | 6e-07 | 27/48 (HEC-1-A, HOP62, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -4.8 | 6e-05 | 21/48 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.800×** | -4.4 | 4e-04 | 22/48 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.817×** | -4.2 | 0.001 | 18/48 (J82, NCI-H2030, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.826×** | -3.9 | 0.003 | 22/48 (A549, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.879× | -3.7 | 0.006 | 17/48 (J82, A-172, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.024 | 15/48 (A549, HOP62, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.747×** | -3.2 | 0.037 | 10/48 (CFPAC-1, J82, …) | top dose only | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.863× | -3.0 | 0.051 | 8/48 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 81.3 | 1 | 9 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.173× (z -18.6) ⚠ toxic; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -8.6) |
| [[A-172 (line)]] | wt | 109 | 3 (2 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +24.1) | [[Dinaciclib (drug)]] 0.05 µM 0.243× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 81.3 | 1 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 80.7 | 0 | 9 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 94.7 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -13.1) |
| [[H4 (line)]] | wt | 87.4 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 55.1 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -9.3) |
| [[HS-578T (line)]] | alt | 70.2 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.8) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 53.7 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +26.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.167× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 68.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 59.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.3) |
| [[A549 (line)]] | wt | 74.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -21.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 30.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -10.3) |
| [[BT-474 (line)]] | alt | 25.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.8× (z +25.3) | — |
| [[C32 (line)]] | wt | 25.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +26.0) | — |
| [[HCT15 (line)]] | alt | 73.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 68.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 39.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.305× (z -8.7) |
| [[KATO III (line)]] | alt | 39.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -11.6) |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -11.3) |
| [[PANC-1 (line)]] | alt | 37.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 28.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.364× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 16.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0696× (z -15.1) |
| [[SNU-423 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -9.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.2) | — |
| [[SW480 (line)]] | alt | 26.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.407× (z -9.0) |
| [[AN3 CA (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2C2-AS1]] | +0.60 | +0.71 / +0.61 | both halves | 7e-06 | ⚠ **readthrough risk**: ATP2C2-AS1 lies 9.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SMS]] | +0.60 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[MSANTD3]] | +0.59 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SMIM29]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PIK3CD]] | +0.58 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[EML2]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CTTNBP2NL]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[KCNN4]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[ZNF23]] | +0.57 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[DRAP1]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ZNF185]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[VEZT]] | +0.56 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[METTL23]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK1]] | -0.55 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[PON2]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[GTF2I]] | -0.54 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.52 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[MFSD14A]] | -0.52 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FUCA2]] | -0.51 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[GPC4]] | -0.49 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[RPN1]] | -0.49 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[STT3B]] | -0.49 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ADI1]] | -0.48 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[DDX3X]] | -0.48 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[TMED10]] | -0.48 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises MEAK7's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 2.02× lower at baseline in the lines without CLDN14-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[PLAUR]] | B | PLAUR activity raises MEAK7's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 1.90× lower at baseline in the lines without PLAUR | 0.016 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[KCNN4]] | B | KCNN4 activity raises MEAK7's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without KCNN4 | 0.054 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[UPP1]] | B | UPP1 activity raises MEAK7's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without UPP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[ATP2C2-AS1]] | C | ATP2C2-AS1's natural level strengthens MEAK7's drug response | ATP2C2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.27; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | MEAK7's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | MEAK7's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.61 | 0.437 over the table, 0.068 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.1, -2.3); signed map (-2.8, 43.5). **Vector** length 109, 28.6% of its response variance represented; |z| ≥ 3 in 1,254 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.7 | +4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +3.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.9 | +2.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +2.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.2 | +3.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -4.2 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -4.2 | -14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.2 | -13.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -12.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.6 | -3.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -2.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | MTOR associated protein MEAK7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:84,476,355-84,554,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | mEAK-7; previously KIAA1609, TLDC1 |
| Gene groups (HGNC) | TLDc domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P9B6](https://www.uniprot.org/uniprotkb/Q6P9B6) (MTOR-associated protein MEAK7):

> Activates an alternative mTOR signaling pathway through RPS6KB2 activation and EIF4EBP1 repression to regulate cell proliferation and migration. Recruits MTOR at the lysosome, essential for MTOR signaling at the lysosome. Binds to the vacuolar-type ATPase (V-ATPase) complex, triggering a conformational change and is likely to regulate its activity. No effect on V-ATPase activity was observed in vitro in one study although it was suggested that it may have inhibitory activity in vivo. However, …

**Summary**, from NCBI Gene [57707](https://www.ncbi.nlm.nih.gov/gene/57707):

> Involved in several processes, including TOR signaling; positive regulation of protein localization to lysosome; and response to insulin. Located in cytosol and lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29325) · Entrez [57707](https://www.ncbi.nlm.nih.gov/gene/57707) · UniProt [Q6P9B6](https://www.uniprot.org/uniprotkb/Q6P9B6) · Ensembl [ENSG00000140950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140950)

## Data

Gene col 6469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6469); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6469]; `tensor/DDL_lfc|DDL_z.npy` [6469]; `embed/gene_vectors.npy` [6469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6469 or target_col == 6469). Every well: [[MEAK7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEAK7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
