---
symbol: "KYNU"
type: "gene"
col: 3736
ensembl_id: "ENSG00000115919"
name: "kynureninase"
location: "2q22.2"
module: 167
arm: "+"
pooled_cpm: 201.83
n_lines_expressing: 21
n_dd_up: 28
n_dd_down: 24
n_dd_up_clean: 23
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 25
direction_downstream: 32
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# KYNU

*kynureninase* — 2q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.95× (z +8.4, q 2e-14, up in 1 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.41× (z +6.0, q 4e-07, up in 13 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.368× (z -12.7, q 4e-34, down in 19 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RSPO3]] (+0.74, fdr 7e-06), [[CSGALNACT1]] (+0.70, fdr 7e-06), [[CFH]] (+0.67, fdr 7e-06); moves opposite to [[HMOX2]] (-0.53, fdr 4e-05), [[ANKRD36B]] (-0.52, fdr 3e-05), [[IMPDH1]] (-0.50, fdr 1e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 32 go from it, the strongest it → [[ODF3B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +8.4 | 2e-14 | 1/20 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +6.0 | 4e-07 | 13/19 (HepG2/C3A, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.7 | 2e-06 | 9/19 (NCI-H1573, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 2e-06 | 16/19 (RPMI-7951, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.2 | 3e-05 | 1/17 (Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +5.0 | 5e-05 | 13/19 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.48×** | +4.9 | 5e-05 | 13/19 (NCI-H1573, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.9 | 5e-05 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +4.8 | 9e-05 | 15/19 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 4e-04 | 0/19 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +4.4 | 6e-04 | 11/19 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +4.3 | 7e-04 | 2/21 (RPMI-7951, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.36×** | +3.9 | 0.004 | 9/20 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.010 | 11/19 (HOP62, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.010 | 15/19 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.021 | 7/19 (NCI-H1792, Hs 766T, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.025 | 1/19 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.033 | 12/20 (HOP62, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.045 | 0/20 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3736.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.368×** | -12.7 | 4e-34 | 19/19 (NCI-H1573, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.432×** | -10.6 | 6e-24 | 19/19 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.443×** | -10.3 | 1e-22 | 19/19 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.617×** | -6.1 | 1e-07 | 15/19 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.514×** | -4.4 | 0.001 | 14/20 (HepG2/C3A, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.523×** | -4.3 | 0.002 | 16/19 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.723×** | -4.1 | 0.003 | 12/19 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.547×** | -4.0 | 0.004 | 17/19 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 5 µM |  | **0.584×** | -3.6 | 0.023 | 6/19 (LOX-IMVI, COLO 205, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.587×** | -3.5 | 0.023 | 8/19 (NCI-H1792, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.025 | 3/19 (NCI-H1573, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.764×** | -3.4 | 0.028 | 9/19 (COLO 205, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.765×** | -3.4 | 0.028 | 1/19 (NCI-H1573) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.829×** | -3.4 | 0.028 | 14/19 (COLO 205, LOX-IMVI, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.776×** | -3.2 | 0.046 | 9/19 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.763×** | -3.2 | 0.047 | 0/19 | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.047 | 9/19 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.790×** | -3.0 | 0.071 | 2/19 (NCI-H1573, A498) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.783×** | -3.0 | 0.071 | 4/19 (SNU-423, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 295 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0877× (z -20.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0946× (z -19.5) |
| [[NCI-H460 (line)]] | wt | 1,077 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 569 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.220× (z -11.2) |
| [[SNU-423 (line)]] | alt | 586 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.108× (z -13.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.152× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.186× (z -13.0) |
| [[H4 (line)]] | wt | 721 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.134× (z -11.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.136× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 347 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.134× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 645 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -14.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.182× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 166 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.110× (z -14.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.120× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 177 | 1 | 4 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.10× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.178× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.202× (z -9.6) |
| [[A549 (line)]] | wt | 1,154 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0913× (z -21.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -8.5) |
| [[COLO 205 (line)]] | alt | 214 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0608× (z -14.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0750× (z -13.5) |
| [[HepG2_C3A (line)]] | wt | 319 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.89× (z +10.4) ⚠ cell-cycle shift, explains ~35% of this change | [[Panobinostat (drug)]] 5 µM 0.139× (z -15.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -14.3) |
| [[A498 (line)]] | wt | 487 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 279 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -11.4) |
| [[HOP62 (line)]] | alt | 104 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.06× (z +11.7) | — |
| [[Hs 766T (line)]] | wt | 61.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +15.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.18× (z +10.7) | — |
| [[A-172 (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.5 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 19.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 690 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 412 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.1 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 43.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 13.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSPO3]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[CSGALNACT1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[CFH]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[IL6]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[LINC02015]] | +0.65 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[EYA4]] | +0.65 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[EBF1]] | +0.65 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[MYPN]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MSC]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IDO1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 983 |
| [[TNFAIP6]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[TCIM]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMOX2]] | -0.53 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ANKRD36B]] | -0.52 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[IMPDH1]] | -0.50 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[JAM3]] | -0.50 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[EIF4EBP1]] | -0.49 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[EPHB4]] | -0.49 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[RNF216P1]] | -0.49 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 4, C 21. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises KYNU's level | lines that do not express CTSS (15) vs lines expressing it (35) | 4.83× lower at baseline in the lines without CTSS | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises KYNU's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 4.17× lower at baseline in the lines without GBP1 | 0.026 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[DIO2]] | B | DIO2 activity raises KYNU's level | lines that do not express DIO2 (14) vs lines expressing it (36) | 2.85× lower at baseline in the lines without DIO2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LINC01725, ENSG00000226640, RNF150 |
| [[IL1R1]] | B | IL1R1 activity raises KYNU's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 4.82× lower at baseline in the lines without IL1R1 | 0.084 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[AKR1C2]] | C | AKR1C2 activity raises KYNU's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 4.99× lower at baseline in the lines without AKR1C2 | 0.004 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[LINC02057]] | C | LINC02057 activity raises KYNU's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 5.08× lower at baseline in the lines without LINC02057 | 0.006 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6; co-absent with the target |
| [[CFH]] | C | CFH activity raises KYNU's level | lines that do not express CFH (28) vs lines expressing it (22) | 4.73× lower at baseline in the lines without CFH | 0.009 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[TNIP3]] | C | TNIP3 activity raises KYNU's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 6.08× lower at baseline in the lines without TNIP3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises KYNU's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 5.59× lower at baseline in the lines without PAPPA | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[EBF1]] | C | EBF1 activity raises KYNU's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 5.96× lower at baseline in the lines without EBF1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4; co-absent with the target |
| [[CARD6]] | C | CARD6 activity raises KYNU's level | lines that do not express CARD6 (17) vs lines expressing it (33) | 6.17× lower at baseline in the lines without CARD6 | 0.015 | ⚠ within organs, on part of the lines; also absent: GPX3, GLRX, KYNU; co-absent with the target |
| [[KMO]] | C | KMO activity raises KYNU's level | lines that do not express KMO (18) vs lines expressing it (32) | 6.07× lower at baseline in the lines without KMO | 0.024 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 14, C 18. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ODF3B]] | B | KYNU activity raises ODF3B's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.98× lower at baseline in the lines without KYNU | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[DIO2]] | B | KYNU activity raises DIO2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without KYNU | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[IL1R1]] | B | KYNU activity raises IL1R1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 3.77× lower at baseline in the lines without KYNU | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[PLD1]] | B | KYNU activity raises PLD1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.67× lower at baseline in the lines without KYNU | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[SOD2]] | B | KYNU activity raises SOD2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.39× lower at baseline in the lines without KYNU | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[ALPK1]] | B | KYNU activity raises ALPK1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.65× lower at baseline in the lines without KYNU | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[TYMP]] | B | KYNU activity raises TYMP's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.79× lower at baseline in the lines without KYNU | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[FNDC3B]] | B | KYNU activity raises FNDC3B's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without KYNU | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[RIPK2-DT]] | B | KYNU activity raises RIPK2-DT's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without KYNU | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[GBP1]] | B | KYNU activity raises GBP1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.70× lower at baseline in the lines without KYNU | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[PDE4D]] | B | KYNU activity raises PDE4D's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.71× lower at baseline in the lines without KYNU | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[IFIT2]] | B | KYNU activity raises IFIT2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.30× lower at baseline in the lines without KYNU | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.6, 22.3); signed map (47.9, 23.6). **Vector** length 104, 36.2% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +3.7 | +5.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +3.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.8 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | kynureninase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q22.2 — chr2:142,877,657-143,055,833 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | XENOBIOTIC_METABOLISM, COMPLEMENT, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16719](https://www.uniprot.org/uniprotkb/Q16719) (Kynureninase):

> Catalyzes the cleavage of L-kynurenine (L-Kyn) and L-3-hydroxykynurenine (L-3OHKyn) into anthranilic acid (AA) and 3-hydroxyanthranilic acid (3-OHAA), respectively. Has a preference for the L-3-hydroxy form. Also has cysteine-conjugate-beta-lyase activity.

**Summary**, from NCBI Gene [8942](https://www.ncbi.nlm.nih.gov/gene/8942):

> Kynureninase is a pyridoxal-5'-phosphate (pyridoxal-P) dependent enzyme that catalyzes the cleavage of L-kynurenine and L-3-hydroxykynurenine into anthranilic and 3-hydroxyanthranilic acids, respectively. Kynureninase is involved in the biosynthesis of NAD cofactors from tryptophan through the kynurenine pathway. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2010]

**Accessions** — [HGNC:6469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6469) · Entrez [8942](https://www.ncbi.nlm.nih.gov/gene/8942) · UniProt [Q16719](https://www.uniprot.org/uniprotkb/Q16719) · Ensembl [ENSG00000115919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115919)

## Data

Gene col 3736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3736); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3736]; `tensor/DDL_lfc|DDL_z.npy` [3736]; `embed/gene_vectors.npy` [3736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3736 or target_col == 3736). Every well: [[KYNU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KYNU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
