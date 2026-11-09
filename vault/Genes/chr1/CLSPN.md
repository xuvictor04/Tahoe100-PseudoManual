---
symbol: "CLSPN"
type: "gene"
col: 1710
ensembl_id: "ENSG00000092853"
name: "claspin"
location: "1p34.3"
module: 6
arm: "+"
pooled_cpm: 42.7
n_lines_expressing: 46
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 13
direction_downstream: 27
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CLSPN

*claspin* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (30 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.51× (z +15.5, q 0e+00, up in 41 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.60× (z +6.1, q 5e-08, up in 27 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[palbociclib (drug)]] 0.5 µM: 0.377× (z -6.3, q 1e-07, down in 34 of 44 measured lines) ⚠ cell-cycle shift, explains ~69% of this change. The strongest without an alert is [[AZD-8055 (drug)]] 0.5 µM: 0.477× (z -4.8, q 3e-04, down in 29 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM10]] (+0.92, fdr 7e-06), [[CDC45]] (+0.91, fdr 7e-06), [[EXO1]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 27 go from it, the strongest it → [[RRM2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 30 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 30 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **5.51×** | +15.5 | 0e+00 | 41/41 (PANC-1, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | **4.95×** | +14.0 | 4e-42 | 36/38 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **3.77×** | +12.1 | 3e-31 | 40/44 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **2.30×** | +10.7 | 9e-25 | 40/44 (A549, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **3.06×** | +10.2 | 3e-22 | 39/44 (SW480, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.98×** | +9.9 | 3e-21 | 40/44 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **3.25×** | +9.9 | 3e-21 | 36/40 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **2.48×** | +7.9 | 1e-13 | 36/43 (SW480, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.34×** | +7.5 | 5e-12 | 38/44 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **2.27×** | +7.4 | 5e-12 | 35/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **2.05×** | +6.6 | 3e-09 | 33/43 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **2.05×** | +6.3 | 2e-08 | 30/43 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~85% of this change | **2.04×** | +6.2 | 2e-08 | 28/43 (C32, HS-578T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.1 | 5e-08 | 27/44 (SW480, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.95×** | +6.1 | 5e-08 | 33/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.002 | 23/44 (SW480, HOP62, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.035 | 15/44 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.067 | 15/44 (A-172, NCI-H23, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.36×** | +2.8 | 0.090 | 15/44 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.35×** | +2.7 | 0.096 | 17/44 (SW480, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.377×** | -6.3 | 1e-07 | 34/44 (HT-29, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.657×** | -5.4 | 2e-05 | 34/44 (COLO 205, KATO III, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.477×** | -4.8 | 3e-04 | 29/44 (A498, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.596×** | -4.7 | 4e-04 | 25/44 (A498, COLO 205, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.509×** | -4.4 | 0.001 | 28/44 (NCI-H23, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.604×** | -4.3 | 0.001 | 28/44 (A498, NCI-H23, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.733×** | -4.0 | 0.006 | 25/44 (HCT15, Hs 766T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.650×** | -3.9 | 0.007 | 22/44 (A498, COLO 205, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.744×** | -3.8 | 0.009 | 22/44 (A498, A-427, …) | all doses, flat | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.584×** | -3.5 | 0.029 | 20/44 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.055 | 19/44 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.706×** | -3.2 | 0.070 | 20/43 (COLO 205, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.777×** | -3.1 | 0.070 | 12/44 (A-427, SW480, …) | all doses, flat |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.709×** | -3.1 | 0.070 | 13/44 (SW480, SNU-423, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.784×** | -3.1 | 0.070 | 17/44 (A-427, NCI-H460, …) | top dose only |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.427×** | -3.0 | 0.088 | 16/44 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +2.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 56.8 | 12 (11 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.25× (z +12.2) ⚠ toxic; cell-cycle shift, explains ~87% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[A549 (line)]] | wt | 18.5 | 6 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.44× (z +12.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[J82 (line)]] | alt | 154 | 6 (4 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 3.11× (z +10.9) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.2) | — |
| [[A-427 (line)]] | wt | 106 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.2) |
| [[A498 (line)]] | wt | 44.8 | 1 (1 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | [[Selinexor (drug)]] 5 µM 0.124× (z -20.7) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 37.0 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.19× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[PANC-1 (line)]] | alt | 54.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.72× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[HS-578T (line)]] | alt | 25.7 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +12.2) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HOP62 (line)]] | alt | 38.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.80× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +10.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SNU-423 (line)]] | alt | 18.2 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.33× (z +10.3) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[SW1417 (line)]] | alt | 34.8 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +9.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[A-172 (line)]] | wt | 37.0 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.186× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 28.3 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +8.6) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[LoVo (line)]] | wt | 20.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.69× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +10.3) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[HCT15 (line)]] | alt | 49.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.234× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.99× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +9.7) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[LS 180 (line)]] | wt | 26.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.140× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 13.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.02× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[NCI-H23 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 19.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 59.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.08× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change | — |
| [[AN3 CA (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.12 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM10]] | +0.92 | +0.92 / +0.92 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 977 |
| [[CDC45]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 995 |
| [[EXO1]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 773 |
| [[FAM111B]] | +0.90 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[E2F1]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: Apoptosis; STRING 404 |
| [[WDR76]] | +0.90 | +0.90 / +0.87 | both halves | 7e-06 | STRING 513 |
| [[DTL]] | +0.89 | +0.89 / +0.88 | both halves | 7e-06 | STRING 566 |
| [[MCM4]] | +0.89 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 971 |
| [[MYBL2]] | +0.89 | +0.86 / +0.88 | both halves | 7e-06 | STRING 411 |
| [[CHAF1A]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 493 |
| [[GINS1]] | +0.87 | +0.83 / +0.86 | both halves | 7e-06 | STRING 874 |
| [[XRCC3]] | +0.86 | +0.88 / +0.84 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises CLSPN's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.49× lower at baseline in the lines without E2F2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises CLSPN's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.92× lower at baseline in the lines without CDC25A | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CLSPN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises CLSPN's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without FAM111B | 0.057 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TP73]] | B | TP73 activity raises CLSPN's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.90× lower at baseline in the lines without TP73 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[TCF19]] | C | TCF19 activity raises CLSPN's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 3.65× lower at baseline in the lines without TCF19 | 0.015 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[E2F8]] | C | E2F8 activity raises CLSPN's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.92× lower at baseline in the lines without E2F8 | 0.029 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises CLSPN's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.98× lower at baseline in the lines without DSCC1 | 0.048 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises CLSPN's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 3.82× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises CLSPN's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.30× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises CLSPN's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.16× lower at baseline in the lines without MYBL2 | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises CLSPN's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.66× lower at baseline in the lines without MCM10 | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRM2]] | C | CLSPN activity raises RRM2's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 3.83× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SKA3]] | C | CLSPN activity raises SKA3's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 3.01× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[GINS1]] | C | CLSPN activity raises GINS1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.89× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[MND1]] | C | CLSPN activity raises MND1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.58× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[VRK1]] | C | CLSPN activity raises VRK1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[CENPM]] | C | CLSPN activity raises CENPM's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.32× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target; its own permutation p |
| [[NASP]] | C | CLSPN activity raises NASP's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without CLSPN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; its own permutation p |
| [[CDC6]] | C | CLSPN activity raises CDC6's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without CLSPN | 0.061 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[TK1]] | C | CLSPN activity raises TK1's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.45× lower at baseline in the lines without CLSPN | 0.062 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[XRCC3]] | C | CLSPN activity raises XRCC3's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without CLSPN | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[PSMC3IP]] | C | CLSPN activity raises PSMC3IP's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without CLSPN | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |
| [[SPC25]] | C | CLSPN activity raises SPC25's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.63× lower at baseline in the lines without CLSPN | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.906). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.7, -44.7); signed map (-38.1, -45.6). **Vector** length 138, 57.6% of its response variance represented; |z| ≥ 3 in 1,541 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.68 to 65); *DNA strand elongation* (reactome, mean cos +0.74 to 28); *DNA Replication* (reactome, mean cos +0.74 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +6.9 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +5.8 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.5 | +7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +5.3 | +5.7 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.3 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +2.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.3 | +2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.2 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.9 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -6.3 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.7 | -4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -5.3 | -5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.2 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | claspin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:35,720,218-35,769,978 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 15 pathways, smallest: Apoptotic cleavage of cellular proteins; Activation of ATR in response to replication stress; Apoptotic execution phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAW4](https://www.uniprot.org/uniprotkb/Q9HAW4) (Claspin):

> Required for checkpoint mediated cell cycle arrest in response to inhibition of DNA replication or to DNA damage induced by both ionizing and UV irradiation. Adapter protein which binds to BRCA1 and the checkpoint kinase CHEK1 and facilitates the ATR-dependent phosphorylation of both proteins. Also required to maintain normal rates of replication fork progression during unperturbed DNA replication. Binds directly to DNA, with particular affinity for branched or forked molecules and interacts …

**Summary**, from NCBI Gene [63967](https://www.ncbi.nlm.nih.gov/gene/63967):

> The product of this gene is an essential upstream regulator of checkpoint kinase 1 and triggers a checkpoint arrest of the cell cycle in response to replicative stress or DNA damage. The protein is also required for efficient DNA replication during a normal S phase. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:19715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19715) · Entrez [63967](https://www.ncbi.nlm.nih.gov/gene/63967) · UniProt [Q9HAW4](https://www.uniprot.org/uniprotkb/Q9HAW4) · Ensembl [ENSG00000092853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092853)

## Data

Gene col 1710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1710); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1710]; `tensor/DDL_lfc|DDL_z.npy` [1710]; `embed/gene_vectors.npy` [1710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1710 or target_col == 1710). Every well: [[CLSPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLSPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
