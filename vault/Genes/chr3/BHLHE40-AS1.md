---
symbol: "BHLHE40-AS1"
type: "gene"
col: 14040
ensembl_id: "ENSG00000235831"
name: "BHLHE40 antisense RNA 1"
location: "3p26.1"
module: 80
arm: "+"
pooled_cpm: 11.56
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 16
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# BHLHE40-AS1

*BHLHE40 antisense RNA 1* — 3p26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.16× (z +45.4, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.613× (z -8.0, q 9e-13, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL10-AS1]] (+0.70, fdr 1e-05), [[LRP2BP]] (+0.69, fdr 3e-05), [[CCDC200]] (+0.69, fdr 7e-06); moves opposite to [[WRAP73]] (-0.67, fdr 4e-05), [[GPATCH11]] (-0.66, fdr 1e-04), [[PUSL1]] (-0.65, fdr 4e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.16×** | +45.4 | 0e+00 | 43/43 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.72×** | +28.5 | 0e+00 | 30/31 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.02×** | +27.1 | 0e+00 | 26/26 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.11×** | +22.2 | 0e+00 | 18/20 (LoVo, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.43×** | +20.5 | 0e+00 | 36/47 (A-172, HS-578T, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +18.4 | 0e+00 | 34/39 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +16.2 | 0e+00 | 34/41 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.72×** | +12.5 | 3e-34 | 29/44 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +10.2 | 2e-22 | 25/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +9.9 | 3e-21 | 18/34 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.88×** | +9.0 | 8e-18 | 8/20 (NCI-H1573, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +8.7 | 1e-16 | 25/44 (HS-578T, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.7 | 7e-10 | 19/47 (NCI-H1573, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +5.6 | 1e-06 | 13/43 (HS-578T, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.82×** | +5.1 | 1e-05 | 8/41 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +4.9 | 4e-05 | 14/46 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.36×** | +4.9 | 4e-05 | 16/46 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.031 | 6/39 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.037 | 6/45 (KATO III, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.071 | 7/45 (Hs 766T, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -8.0 | 9e-13 | 23/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.660×** | -6.8 | 3e-09 | 20/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[NG25 (drug)]] 5 µM |  | **0.456×** | -6.7 | 4e-09 | 17/37 (NCI-H1792, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.687×** | -6.1 | 1e-07 | 18/46 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.708×** | -5.6 | 2e-06 | 12/46 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.726×** | -5.2 | 2e-05 | 18/45 (NCI-H460, A498, …) | all doses, flat |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.803×** | -5.0 | 4e-05 | 19/48 (Hs 766T, A-172, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.748×** | -4.7 | 2e-04 | 10/45 (H4, Panc 03.27, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.761×** | -4.4 | 6e-04 | 12/47 (NCI-H460, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.766×** | -4.3 | 8e-04 | 14/45 (HOP62, SW 1271, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.758×** | -4.2 | 0.002 | 11/43 (H4, LS 180, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.776×** | -4.1 | 0.002 | 14/46 (A498, SW 900, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.839× | -4.0 | 0.002 | 11/47 (J82, SK-MEL-2, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.782×** | -3.8 | 0.005 | 14/44 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.815×** | -3.3 | 0.032 | 11/42 (HCT15, HS-578T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 15.5 | 7 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +20.5) | — |
| [[HS-578T (line)]] | alt | 9.31 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.5× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.89× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 45.0 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.242× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 11.4 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +19.4) | — |
| [[J82 (line)]] | alt | 7.11 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 13.9× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +9.7) | — |
| [[LoVo (line)]] | wt | 18.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 49.9× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.5) | — |
| [[NCI-H1573 (line)]] | alt | 22.5 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +22.0) | — |
| [[PANC-1 (line)]] | alt | 21.4 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.264× (z -10.0) |
| [[A498 (line)]] | wt | 7.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 13.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +17.8) | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.116× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.77× (z +13.7) | — |
| [[A549 (line)]] | wt | 34.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 6.61 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 3.68 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.6× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 5.67 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +15.3) | — |
| [[SW 900 (line)]] | alt | 5.65 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.4× (z +12.3) | — |
| [[SW480 (line)]] | alt | 9.24 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +15.5) | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0142× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 3.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 37.6× (z +14.2) | — |
| [[CFPAC-1 (line)]] | alt | 14.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 7.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 4.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.07× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 17.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 7.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.2× (z +11.3) | — |
| [[HT-29 (line)]] | alt | 4.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.46× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 4.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +11.1) | — |
| [[KATO III (line)]] | alt | 8.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 6.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.77× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 7.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.74× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 5.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +14.2) | — |
| [[RKO (line)]] | wt | 4.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +11.4) | — |
| [[SHP-77 (line)]] | alt | 14.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.26× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 5.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 5.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.09× (z +10.5) | — |
| [[A-427 (line)]] | wt | 7.10 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL10-AS1]] | +0.70 | +0.60 / +0.55 | both halves | 1e-05 | same gene group |
| [[LRP2BP]] | +0.69 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[CCDC200]] | +0.69 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TBCE-1]] | +0.68 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[STARD4-AS1]] | +0.68 | +0.58 / +0.43 | both halves | 4e-05 | same gene group |
| [[HCG20]] | +0.67 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[HSDL2-AS1]] | +0.67 | +0.59 / +0.42 | both halves | 4e-05 | same gene group |
| [[CCNT2-AS1]] | +0.67 | +0.55 / +0.52 | both halves | 1e-05 | same gene group |
| [[MKLN1-AS]] | +0.67 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[LINC01090]] | +0.67 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LRRC8C-DT]] | +0.67 | +0.57 / +0.38 | both halves | 6e-05 |  |
| [[ZNF213-AS1]] | +0.66 | +0.60 / +0.36 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.67 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GPATCH11]] | -0.66 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[PUSL1]] | -0.65 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[CAPN7]] | -0.62 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[ISCA2]] | -0.61 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[MRPS34]] | -0.61 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[RRP1B]] | -0.61 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[PET117]] | -0.59 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[LSM2]] | -0.59 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TTC38]] | -0.58 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BHLHE40-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C1]] | B | NR3C1 activity lowers BHLHE40-AS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, 19.2); signed map (27.6, -1.8). **Vector** length 101, 22.5% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.5 | +45.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +27.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +18.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +20.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +16.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +5.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | -0.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.1 | -8.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.3 | -6.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.8 | -5.2 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.5 | -2.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.2 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BHLHE40 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p26.1 — chr3:4,896,806-4,980,414 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100507582](https://www.ncbi.nlm.nih.gov/gene/100507582):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:44471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44471) · Entrez [100507582](https://www.ncbi.nlm.nih.gov/gene/100507582) · Ensembl [ENSG00000235831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235831)

## Data

Gene col 14040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14040); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14040]; `tensor/DDL_lfc|DDL_z.npy` [14040]; `embed/gene_vectors.npy` [14040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14040 or target_col == 14040). Every well: [[BHLHE40-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BHLHE40-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
