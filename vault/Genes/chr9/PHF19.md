---
symbol: "PHF19"
type: "gene"
col: 4063
ensembl_id: "ENSG00000119403"
name: "PHD finger protein 19"
location: "9q33.2"
module: 22
arm: "+"
pooled_cpm: 16.47
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# PHF19

*PHD finger protein 19* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 9.19× (z +48.5, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.325× (z -17.4, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESPL1]] (+0.78, fdr 7e-06), [[CYREN]] (+0.72, fdr 7e-06), [[REXO5]] (+0.71, fdr 7e-06); moves opposite to [[RNF149]] (-0.66, fdr 1e-05), [[NDUFAF7]] (-0.65, fdr 1e-05), [[GAPVD1]] (-0.63, fdr 3e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FMNL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **9.19×** | +48.5 | 0e+00 | 43/47 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.80×** | +15.9 | 0e+00 | 32/46 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +12.5 | 3e-33 | 26/27 (HT-29, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +12.4 | 5e-33 | 30/39 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.07×** | +10.8 | 3e-25 | 29/46 (A-172, J82, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +10.1 | 6e-22 | 26/33 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~87% of this change | **1.44×** | +5.7 | 1e-06 | 22/44 (SW 900, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.41×** | +5.1 | 2e-05 | 14/42 (A498, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.19× | +3.9 | 0.007 | 11/48 (HT-29, HCT15, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.018 | 9/48 (A498, BT-474, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.030 | 8/41 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.078 | 8/45 (NCI-H23, BT-474, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.23×** | +3.1 | 0.078 | 9/48 (A498, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.325×** | -17.4 | 0e+00 | 45/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.375×** | -15.2 | 0e+00 | 43/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.417×** | -13.5 | 2e-39 | 44/47 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.514×** | -10.3 | 9e-23 | 37/48 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.708×** | -7.6 | 4e-12 | 24/48 (A-172, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.598×** | -7.5 | 5e-12 | 29/47 (SW480, A-427, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.643×** | -6.9 | 6e-10 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.661×** | -6.4 | 9e-09 | 26/47 (SW480, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.661×** | -6.4 | 9e-09 | 23/45 (SHP-77, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.477×** | -6.0 | 1e-07 | 24/48 (SHP-77, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -5.7 | 6e-07 | 21/48 (SW1417, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.694×** | -5.7 | 7e-07 | 25/47 (NCI-H460, SNU-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **0.521×** | -5.3 | 6e-06 | 17/38 (J82, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.722×** | -5.1 | 2e-05 | 18/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -5.0 | 2e-05 | 19/46 (SK-MEL-2, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.722×** | -4.9 | 4e-05 | 17/47 (LS 180, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.833×** | -4.0 | 0.002 | 17/48 (LoVo, A-172, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.769×** | -3.9 | 0.003 | 12/46 (SNU-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.770×** | -3.8 | 0.005 | 11/47 (SK-MEL-2, SW480, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.795×** | -3.6 | 0.009 | 9/47 (MIA PaCa-2, CFPAC-1, …) | all doses, flat |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.859× | -3.3 | 0.020 | 10/48 (HepG2/C3A, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 14.9 | 4 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 29.3× (z +25.2) | [[Selinexor (drug)]] 5 µM 0.265× (z -9.8) ⚠ cell-cycle shift, explains ~90% of this change · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.151× (z -9.1) |
| [[SHP-77 (line)]] | alt | 51.0 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0737× (z -18.1) |
| [[SW480 (line)]] | alt | 21.1 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.217× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 19.4 | 2 | 4 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +23.3) | [[Panobinostat (drug)]] 5 µM 0.279× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 29.5 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +23.1) | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -9.8) |
| [[A498 (line)]] | wt | 24.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +20.3) | [[Selinexor (drug)]] 5 µM 0.428× (z -9.3) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HOP62 (line)]] | alt | 18.5 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 54.8× (z +38.4) | [[Panobinostat (drug)]] 5 µM 0.248× (z -9.5) |
| [[H4 (line)]] | wt | 18.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +18.3) | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -8.7) |
| [[HT-29 (line)]] | alt | 10.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +10.7) | [[Selinexor (drug)]] 5 µM 0.272× (z -9.4) ⚠ cell-cycle shift, explains ~90% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.9× (z +21.4) | — |
| [[J82 (line)]] | alt | 24.2 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +31.0) | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 8.22 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +19.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +22.1) | — |
| [[PANC-1 (line)]] | alt | 14.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +28.0) | — |
| [[SW48 (line)]] | wt | 15.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +16.4) | [[Belinostat (drug)]] 0.5 µM 0.104× (z -9.2) |
| [[COLO 205 (line)]] | alt | 8.90 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +10.9) | [[Pimozide (drug)]] 0.05 µM 0.0541× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 18.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +14.0) | [[Belinostat (drug)]] 5 µM 0.272× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 7.75 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 33.7× (z +16.4) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0685× (z -8.8) |
| [[Hs 766T (line)]] | wt | 16.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 34.2× (z +25.1) | [[Selinexor (drug)]] 5 µM 0.281× (z -9.1) ⚠ cell-cycle shift, explains ~90% of this change |
| [[HS-578T (line)]] | alt | 10.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +24.2) | — |
| [[LoVo (line)]] | wt | 5.31 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +21.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +26.6) | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +24.0) | — |
| [[NCI-H2347 (line)]] | alt | 19.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +15.7) | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -11.2) |
| [[RKO (line)]] | wt | 24.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 17.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +19.1) | — |
| [[SNU-423 (line)]] | alt | 16.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +25.0) | — |
| [[SW 900 (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +20.5) | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -9.1) |
| [[A549 (line)]] | wt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +13.1) | — |
| [[AsPC-1 (line)]] | alt | 5.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +14.2) | — |
| [[C32 (line)]] | wt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.22× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 7.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.1× (z +25.8) | — |
| [[LOX-IMVI (line)]] | wt | 14.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +19.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.4) | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +19.1) | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -9.7) ⚠ cell-cycle shift, explains ~90% of this change |
| [[SW 1088 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESPL1]] | +0.78 | +0.81 / +0.74 | both halves | 7e-06 |  |
| [[CYREN]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[REXO5]] | +0.71 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[GEN1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CIP2A]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[MDC1]] | +0.69 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ASPM]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[SPDL1]] | +0.66 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SGO1]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[THOC6]] | +0.66 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[BAHCC1]] | +0.65 | +0.64 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF149]] | -0.66 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[NDUFAF7]] | -0.65 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[GAPVD1]] | -0.63 | -0.73 / -0.43 | both halves | 3e-05 |  |
| [[RPS24]] | -0.63 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[KLHDC10]] | -0.62 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[FTL]] | -0.61 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[MYPOP]] | -0.61 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[LMTK2]] | -0.61 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[UNC45A]] | -0.61 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RPS14]] | -0.60 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[RPS5]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMNL3]] | B | FMNL3 activity raises PHF19's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without FMNL3 | 0.052 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[CDC42EP1]] | B | CDC42EP1 activity lowers PHF19's level | lines that do not express CDC42EP1 (5) vs lines expressing it (45) | 1.60× higher at baseline in the lines without CDC42EP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZFP36, IQCN, SLC22A20P; its own permutation p |
| [[HYLS1]] | B | HYLS1 activity raises PHF19's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.78× lower at baseline in the lines without HYLS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises PHF19's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.75× lower at baseline in the lines without MYBL1 | 0.086 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.554). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.3, -48.8); signed map (-44.6, -48.1). **Vector** length 107, 27.5% of its response variance represented; |z| ≥ 3 in 1,143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Condensation of Prometaphase Chromosomes* (reactome, mean cos +0.51 to 8); *Processing of antigen in germinal center B cells* (reactome, mean cos +0.50 to 9); *Activation of NIMA Kinases NEK9, NEK6, NEK7* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +16.8 | +48.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +15.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +9.2 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +10.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.5 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | -5.3 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | -5.2 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -5.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.6 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | -17.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -2.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | PHD finger protein 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:120,855,651-120,894,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP727G051, PCL3, MTF2L1, TDRD19B |
| Gene groups (HGNC) | PHD finger proteins; Tudor domain containing |
| Reactome | 2 pathways, smallest: PRC2 methylates histones and DNA; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6S3](https://www.uniprot.org/uniprotkb/Q5T6S3) (PHD finger protein 19):

> Polycomb group (PcG) protein that specifically binds histone H3 trimethylated at 'Lys-36' (H3K36me3) and recruits the PRC2 complex, thus enhancing PRC2 H3K27me3 methylation activity. Probably involved in the transition from an active state to a repressed state in embryonic stem cells: acts by binding to H3K36me3, a mark for transcriptional activation, and recruiting H3K36me3 histone demethylases RIOX1 or KDM2B, leading to demethylation of H3K36 and recruitment of the PRC2 complex that mediates …

**Summary**, from NCBI Gene [26147](https://www.ncbi.nlm.nih.gov/gene/26147):

> Enables histone H3K36me3 reader activity. Involved in negative regulation of gene expression, epigenetic. Part of ESC/E(Z) complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24566) · Entrez [26147](https://www.ncbi.nlm.nih.gov/gene/26147) · UniProt [Q5T6S3](https://www.uniprot.org/uniprotkb/Q5T6S3) · Ensembl [ENSG00000119403](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119403)

## Data

Gene col 4063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4063); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4063]; `tensor/DDL_lfc|DDL_z.npy` [4063]; `embed/gene_vectors.npy` [4063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4063 or target_col == 4063). Every well: [[PHF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
