---
symbol: "COIL"
type: "gene"
col: 4248
ensembl_id: "ENSG00000121058"
name: "coilin"
location: "17q22"
module: 12
arm: "+"
pooled_cpm: 37.68
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 13
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# COIL

*coilin* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.88× (z +14.1, q 2e-42, up in 41 of 47 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.14× (z +12.1, q 5e-31, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.479× (z -11.6, q 2e-28, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHAX]] (+0.84, fdr 7e-06), [[CCDC174]] (+0.79, fdr 7e-06), [[C1orf131]] (+0.79, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.68, fdr 7e-06), [[BCAP31]] (-0.68, fdr 7e-06), [[TXNDC5]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.88×** | +14.1 | 2e-42 | 41/47 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.14×** | +12.1 | 5e-31 | 44/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.72×** | +10.9 | 4e-25 | 42/49 (PANC-1, A498, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.98×** | +10.4 | 4e-23 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +9.4 | 4e-19 | 41/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.77×** | +9.1 | 1e-17 | 39/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.72×** | +8.6 | 8e-16 | 42/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.55×** | +7.7 | 7e-13 | 35/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.7 | 8e-13 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +5.9 | 2e-07 | 30/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.7 | 5e-07 | 33/47 (SNU-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.1 | 2e-05 | 31/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.6 | 2e-04 | 26/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.6 | 0.012 | 15/35 (NCI-H1573, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.24×** | +3.5 | 0.021 | 19/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.081 | 14/48 (KATO III, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.479×** | -11.6 | 2e-28 | 45/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.481×** | -11.1 | 4e-26 | 27/39 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.556×** | -9.3 | 4e-18 | 42/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -8.5 | 3e-15 | 43/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.684×** | -8.5 | 3e-15 | 37/48 (A-172, BT-474, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -6.3 | 3e-08 | 33/45 (HepG2/C3A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -5.6 | 2e-06 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.701×** | -5.2 | 2e-05 | 25/44 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.720×** | -5.0 | 4e-05 | 25/48 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.721×** | -5.0 | 4e-05 | 28/47 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.809×** | -4.7 | 1e-04 | 21/48 (A-172, BT-474, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.772×** | -4.1 | 0.002 | 24/47 (AN3 CA, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.027 | 16/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -3.4 | 0.027 | 19/48 (NCI-H2030, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 57.9 | 11 (6 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +17.4) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.98× (z +14.0) | [[Panobinostat (drug)]] 5 µM 0.392× (z -12.0) |
| [[A498 (line)]] | wt | 45.7 | 2 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +13.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.45× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.343× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 52.0 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.11× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0503× (z -30.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.359× (z -10.8) |
| [[SW480 (line)]] | alt | 35.5 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.392× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 32.7 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.15× (z +8.8) | — |
| [[A-172 (line)]] | wt | 31.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -10.3) |
| [[A549 (line)]] | wt | 38.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +13.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -10.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 40.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.54× (z +11.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Dinaciclib (drug)]] 5 µM 0.0927× (z -20.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 42.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.05× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 47.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.363× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 35.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -8.6) |
| [[SNU-423 (line)]] | alt | 38.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.12× (z +9.1) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0449× (z -16.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 28.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 35.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 38.0 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0870× (z -10.8) |
| [[BT-474 (line)]] | alt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -9.3) |
| [[C32 (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[CFPAC-1 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.112× (z -11.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -10.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HT-29 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LS 180 (line)]] | wt | 39.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0842× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 51.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.73× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 35.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 41.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +9.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 900 (line)]] | alt | 34.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -8.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 35.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.383× (z -8.8) |
| [[A-427 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHAX]] | +0.84 | +0.79 / +0.88 | both halves | 7e-06 | STRING 734 |
| [[CCDC174]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 |  |
| [[MRPS18B]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.77 | +0.68 / +0.80 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[PPP4R2]] | +0.76 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[CLK4]] | +0.76 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[THUMPD2]] | +0.76 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[SETDB1]] | +0.76 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.76 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[EPC1]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.68 | -0.69 / -0.67 | both halves | 7e-06 |  |
| [[BCAP31]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.67 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[AKT1]] | -0.65 | -0.61 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises COIL's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.2% of all compounds | 0.007 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers COIL's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 1.13× higher at baseline in the lines without TXNIP | 0.053 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | C | COIL's natural level lowers the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (makes them more sensitive) | COIL's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.9, 4.1); signed map (1.1, -19.3). **Vector** length 101, 28.0% of its response variance represented; |z| ≥ 3 in 1,071 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.52 to 17); *mRNA Splicing* (reactome, mean cos +0.52 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +8.2 | +14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +12.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.2 | +5.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.9 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +1.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.7 | -6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -5.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.8 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | coilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:56,938,199-56,961,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLN80, p80-coilin |
| Hallmark sets | SPERMATOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [P38432](https://www.uniprot.org/uniprotkb/P38432) (Coilin):

> Component of nuclear coiled bodies, also known as Cajal bodies or CBs, which are involved in the modification and assembly of nucleoplasmic snRNPs.

**Summary**, from NCBI Gene [8161](https://www.ncbi.nlm.nih.gov/gene/8161):

> The protein encoded by this gene is an integral component of Cajal bodies (also called coiled bodies). Cajal bodies are nuclear suborganelles of varying number and composition that are involved in the post-transcriptional modification of small nuclear and small nucleolar RNAs. The N-terminus of the coilin protein directs its self-oligomerization while the C-terminus influences the number of nuclear bodies assembled per cell. Differential methylation and phosphorylation of coilin likely …

**Accessions** — [HGNC:2184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2184) · Entrez [8161](https://www.ncbi.nlm.nih.gov/gene/8161) · UniProt [P38432](https://www.uniprot.org/uniprotkb/P38432) · Ensembl [ENSG00000121058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121058)

## Data

Gene col 4248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4248); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4248]; `tensor/DDL_lfc|DDL_z.npy` [4248]; `embed/gene_vectors.npy` [4248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4248 or target_col == 4248). Every well: [[COIL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COIL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
