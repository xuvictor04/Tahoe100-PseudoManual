---
symbol: "WDFY2"
type: "gene"
col: 6332
ensembl_id: "ENSG00000139668"
name: "WD repeat and FYVE domain containing 2"
location: "13q14.3"
module: 77
arm: "+"
pooled_cpm: 170.97
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# WDFY2

*WD repeat and FYVE domain containing 2* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.38× (z +7.5, q 3e-11, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.353× (z -23.5, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.522× (z -21.5, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABTB3]] (+0.71, fdr 7e-06), [[CSNK1E]] (+0.63, fdr 1e-05), [[APBB2]] (+0.62, fdr 1e-05); moves opposite to [[MED12]] (-0.64, fdr 3e-05), [[C11orf58]] (-0.64, fdr 3e-05), [[GTF2H1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ELL2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PDE4DIP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6332.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +7.5 | 3e-11 | 29/48 (COLO 205, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.29×** | +6.0 | 5e-07 | 24/48 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.26×** | +5.5 | 8e-06 | 26/48 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +5.2 | 3e-05 | 20/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.20×** | +4.2 | 0.004 | 19/49 (SNU-423, C-33 A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +4.1 | 0.004 | 13/48 (Hs 766T, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.19× | +4.0 | 0.004 | 23/48 (HEC-1-A, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.5 | 0.029 | 20/49 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.030 | 13/47 (Hs 766T, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6332.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.353×** | -23.5 | 0e+00 | 40/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.368×** | -23.4 | 0e+00 | 41/49 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.522×** | -21.5 | 0e+00 | 38/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.546×** | -14.1 | 3e-43 | 38/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.524×** | -14.0 | 2e-42 | 36/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.613×** | -11.0 | 3e-26 | 34/48 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.669×** | -9.4 | 4e-19 | 37/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.762×** | -9.0 | 2e-17 | 36/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.686×** | -8.5 | 1e-15 | 30/47 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.723×** | -7.6 | 2e-12 | 29/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.726×** | -7.5 | 4e-12 | 36/48 (SW 900, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -6.8 | 3e-10 | 24/49 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.768×** | -6.2 | 3e-08 | 31/48 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.777×** | -5.9 | 2e-07 | 30/49 (RKO, SW480, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.783×** | -5.7 | 4e-07 | 23/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.795×** | -5.4 | 3e-06 | 28/47 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.824×** | -5.2 | 6e-06 | 23/48 (RKO, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.796×** | -5.1 | 9e-06 | 27/48 (RKO, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.800×** | -4.8 | 4e-05 | 27/48 (RKO, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.809×** | -4.7 | 5e-05 | 23/47 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6332. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 295 | 19 | 9 (3 ⚠) | [[Dexamethasone (drug)]] 0.5 µM 2.73× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.279× (z -18.1) |
| [[RKO (line)]] | wt | 315 | 0 | 17 (3 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.299× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 419 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -23.0) |
| [[HOP62 (line)]] | alt | 297 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -24.0) |
| [[A-172 (line)]] | wt | 200 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -35.2) |
| [[HS-578T (line)]] | alt | 232 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -27.4) |
| [[Hs 766T (line)]] | wt | 184 | 2 (1 ⚠) | 6 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.81× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 321 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.9) |
| [[SW 900 (line)]] | alt | 225 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -15.1) |
| [[J82 (line)]] | alt | 186 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -17.5) |
| [[A549 (line)]] | wt | 154 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 218 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.471× (z -11.5) |
| [[C32 (line)]] | wt | 289 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -20.8) |
| [[PANC-1 (line)]] | alt | 152 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -20.5) |
| [[SW480 (line)]] | alt | 397 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -26.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.450× (z -11.6) |
| [[COLO 205 (line)]] | alt | 126 | 4 (3 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.94× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 178 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.1) |
| [[HT-29 (line)]] | alt | 96.0 | 4 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.72× (z +11.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.59× (z +10.4) | [[Selinexor (drug)]] 5 µM 0.578× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 222 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.3) |
| [[SW1417 (line)]] | alt | 95.2 | 2 (1 ⚠) | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.20× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.347× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 157 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -21.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 49.8 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.16× (z +11.2) | — |
| [[KATO III (line)]] | alt | 66.9 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.67× (z +10.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.59× (z +10.1) | [[Harringtonine (drug)]] 0.5 µM 0.399× (z -9.7) |
| [[LoVo (line)]] | wt | 58.0 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.2) | — |
| [[NCI-H1573 (line)]] | alt | 169 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 183 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -19.1) |
| [[Panc 03.27 (line)]] | alt | 96.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.43× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 83.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.517× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 83.2 | 1 | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.89× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.363× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 67.1 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.63× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +15.4) | — |
| [[SHP-77 (line)]] | alt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 77.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.6) |
| [[AN3 CA (line)]] | alt | 134 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.8) |
| [[C-33 A (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -14.8) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 150 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -11.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 64.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.87× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0729× (z -14.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 80.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.219× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 260 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6332), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABTB3]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.63 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[APBB2]] | +0.62 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[MYO9B]] | +0.62 | +0.63 / +0.46 | both halves | 2e-05 |  |
| [[GNA12]] | +0.62 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[HPCAL1]] | +0.62 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[OSTF1]] | +0.61 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[MPZL1]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[POGLUT2]] | +0.61 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[FYN]] | +0.60 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TIMP1]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MAP2K1]] | +0.58 | +0.62 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED12]] | -0.64 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[C11orf58]] | -0.64 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.62 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[LINC00857]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DDX6]] | -0.60 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[SLC9A8]] | -0.60 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[TAPBPL]] | -0.60 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[IQCH-AS1]] | -0.59 | -0.64 / -0.29 | both halves | 3e-04 |  |
| [[POLR3C]] | -0.59 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[ZNF564]] | -0.59 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[ZNF91]] | -0.58 | -0.65 / -0.37 | both halves | 7e-05 |  |
| [[PATL2]] | -0.58 | -0.64 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELL2]] | B | ELL2 activity raises WDFY2's level | lines that do not express ELL2 (12) vs lines expressing it (38) | 2.17× lower at baseline in the lines without ELL2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: RGS17, KMO, DAB2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers WDFY2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TESMIN]] | B | TESMIN activity lowers WDFY2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 1.43× higher at baseline in the lines without TESMIN | 0.046 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent |
| [[GLRX]] | B | GLRX activity raises WDFY2's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without GLRX | 0.079 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises WDFY2's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE4DIP]] | C | WDFY2's natural level strengthens PDE4DIP's drug response | WDFY2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.12; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (36.8, 6.5); signed map (-1.8, 50.9). **Vector** length 140, 46.7% of its response variance represented; |z| ≥ 3 in 1,647 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +7.5 | +7.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | +6.6 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.1 | +6.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.8 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +5.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.0 | -21.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.6 | -14.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.9 | -9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.4 | -9.4 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -6.8 | -6.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -7.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.2 | -5.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.1 | -4.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.6 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat and FYVE domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:51,584,455-51,767,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE22 |
| Gene groups (HGNC) | Zinc fingers FYVE-type; WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P53](https://www.uniprot.org/uniprotkb/Q96P53) (WD repeat and FYVE domain-containing protein 2):

> Acts in an adapter protein-like fashion to mediate the interaction between the kinase PRKCZ and its substrate VAMP2 and increases the PRKCZ-dependent phosphorylation of VAMP2. Positively regulates adipocyte differentiation, by facilitating the phosphorylation and thus inactivation of the anti-adipogenetic transcription factor FOXO1 by the kinase AKT1. Plays a role in endosomal control of AKT2 signaling; required for insulin-stimulated AKT2 phosphorylation and glucose uptake and …

**Summary**, from NCBI Gene [115825](https://www.ncbi.nlm.nih.gov/gene/115825):

> This gene encodes a protein that contains two WD domains and an FYVE zinc finger region. The function of this gene is unknown. An alternatively spliced transcript variant of this gene may exist. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20482) · Entrez [115825](https://www.ncbi.nlm.nih.gov/gene/115825) · UniProt [Q96P53](https://www.uniprot.org/uniprotkb/Q96P53) · Ensembl [ENSG00000139668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139668)

## Data

Gene col 6332: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6332); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6332, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6332]; `tensor/DDL_lfc|DDL_z.npy` [6332]; `embed/gene_vectors.npy` [6332]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6332 or target_col == 6332). Every well: [[WDFY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDFY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
