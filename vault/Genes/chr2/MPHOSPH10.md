---
symbol: "MPHOSPH10"
type: "gene"
col: 4526
ensembl_id: "ENSG00000124383"
name: "M-phase phosphoprotein 10"
location: "2p13.3"
module: 12
arm: "+"
pooled_cpm: 76.76
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MPHOSPH10

*M-phase phosphoprotein 10* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.10× (z +9.4, q 5e-18, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.364× (z -12.2, q 2e-31, down in 37 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -7.4, q 3e-11, down in 37 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (AsPC-1 0.0447×, A-427 0.109×, A549 0.113×, SHP-77 0.137×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.389×, A-172 0.359×, AsPC-1 0.378×, RKO 0.396×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.521×); [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM in 1 line (SW 1088 0.0978×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUS3]] (+0.79, fdr 7e-06), [[CINP]] (+0.77, fdr 7e-06), [[NOL7]] (+0.76, fdr 7e-06, ⚠ NOL7 in the vector space only through flagged drug-doses), [[RIOK2]] (+0.76, fdr 7e-06); moves opposite to [[MOB1A]] (-0.68, fdr 1e-05), [[SUMO3]] (-0.63, fdr 2e-05), [[GNG12]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.10×** | +9.4 | 5e-18 | 45/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.04×** | +9.0 | 9e-17 | 47/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.52×** | +7.5 | 1e-11 | 35/48 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.83×** | +7.2 | 8e-11 | 41/48 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +7.1 | 1e-10 | 45/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.60×** | +5.9 | 4e-07 | 42/48 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 9e-07 | 38/48 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +5.7 | 1e-06 | 35/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +5.5 | 2e-06 | 39/48 (NCI-H1573, A-427, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.54×** | +5.3 | 7e-06 | 35/48 (NCI-H1792, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +4.5 | 3e-04 | 30/48 (LS 180, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.2 | 0.001 | 32/47 (NCI-H2030, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.39×** | +4.2 | 0.001 | 30/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.002 | 34/48 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.006 | 29/48 (SW480, SNU-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +3.6 | 0.011 | 29/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.51×** | +3.2 | 0.042 | 26/49 (HOP62, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 11 lines (AsPC-1 0.0447×, A-427 0.109×, A549 0.113×, SHP-77 0.137×, …; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.389×, A-172 0.359×, AsPC-1 0.378×, RKO 0.396×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.521×); [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM in 1 line (SW 1088 0.0978×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.364×** | -12.2 | 2e-31 | 37/43 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -7.4 | 3e-11 | 37/49 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -4.5 | 0.001 | 32/49 (RPMI-7951, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.7 | 0.027 | 32/48 (A-172, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 73.7 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.298× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 46.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.6) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.93× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 81.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.19× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 70.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.5) | — |
| [[A-172 (line)]] | wt | 73.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -14.5) |
| [[A498 (line)]] | wt | 157 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -14.6) |
| [[A549 (line)]] | wt | 106 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 65.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 100.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.16× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 46.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.16× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0447× (z -27.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -12.5) |
| [[CHP-212 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -9.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 57.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.31× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 69.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.7) |
| [[LS 180 (line)]] | wt | 72.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 97.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.63× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 102 | 0 | 2 | — | [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM 0.0978× (z -8.5) |
| [[SW480 (line)]] | alt | 89.9 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.48× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -11.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 85.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -20.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.73× (z +8.5) | — |
| [[LoVo (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -12.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 81.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 85.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.70× (z +9.7) ⚠ toxic | — |
| [[NCI-H2347 (line)]] | alt | 76.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0808× (z -10.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 70.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +9.3) | — |
| [[RKO (line)]] | wt | 78.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -11.8) |
| [[SHP-77 (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -16.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 88.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -13.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 93.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 85.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS3]] | +0.79 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[CINP]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | +0.76 | +0.74 / +0.70 | both halves | 7e-06 | STRING 833; ⚠ in the vector space only through flagged drug-doses |
| [[RIOK2]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 924 |
| [[RBMX2]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.74 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[VIRMA]] | +0.74 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[MRPL21]] | +0.73 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[DHX57]] | +0.73 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RP9]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[LEO1]] | +0.70 | +0.62 / +0.67 | both halves | 7e-06 | STRING 604 |
| [[TARS2]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SDE2]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.68 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.63 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[GNG12]] | -0.62 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[CERS2]] | -0.62 | -0.46 / -0.56 | both halves | 3e-05 |  |
| [[CD164]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.60 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[CYB561A3]] | -0.60 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[EDEM1]] | -0.60 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[NEMP1]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41L2]] | B | EPB41L2 activity raises MPHOSPH10's level | lines that do not express EPB41L2 (6) vs lines expressing it (44) | 1.25× lower at baseline in the lines without EPB41L2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC26A2, CRTAP, FAM216A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.8, -8.7); signed map (-16.1, -8.9). **Vector** length 134, 48.1% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.7 | +9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.2 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +4.2 |
|  | [[Saquinavir (drug)]] 5 µM |  | +2.1 | +1.2 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -10.9 | -12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -10.4 | -4.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.5 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.1 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.0 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.1 | -1.8 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | M-phase phosphoprotein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:71,130,310-71,150,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MPP10, MPP10P, CT90, PPP1R106 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MPP10 subcomplex |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [O00566](https://www.uniprot.org/uniprotkb/O00566) (U3 small nucleolar ribonucleoprotein protein MPP10):

> Component of the 60-80S U3 small nucleolar ribonucleoprotein (U3 snoRNP). Required for the early cleavages during pre-18S ribosomal RNA processing. Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and …

**Summary**, from NCBI Gene [10199](https://www.ncbi.nlm.nih.gov/gene/10199):

> This gene encodes a protein that is phosphorylated during mitosis. The protein localizes to the nucleolus during interphase and to the chromosomes during M phase. The protein associates with the U3 small nucleolar ribonucleoprotein 60-80S complexes and may be involved in pre-rRNA processing. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:7213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7213) · Entrez [10199](https://www.ncbi.nlm.nih.gov/gene/10199) · UniProt [O00566](https://www.uniprot.org/uniprotkb/O00566) · Ensembl [ENSG00000124383](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124383)

## Data

Gene col 4526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4526); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4526]; `tensor/DDL_lfc|DDL_z.npy` [4526]; `embed/gene_vectors.npy` [4526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4526 or target_col == 4526). Every well: [[MPHOSPH10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPHOSPH10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
