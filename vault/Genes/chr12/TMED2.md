---
symbol: "TMED2"
type: "gene"
col: 1465
ensembl_id: "ENSG00000086598"
name: "transmembrane p24 trafficking protein 2"
location: "12q24.31"
module: 42
arm: "+"
pooled_cpm: 133.41
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMED2

*transmembrane p24 trafficking protein 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.48× (z +14.7, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.66× (z +8.2, q 3e-14, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.707× (z -7.9, q 1e-12, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED7]] (+0.80, fdr 7e-06), [[SEL1L]] (+0.77, fdr 7e-06), [[SEC61A1]] (+0.76, fdr 7e-06); moves opposite to [[EID2]] (-0.57, fdr 1e-05), [[GPATCH8]] (-0.57, fdr 2e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GALNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +14.7 | 0e+00 | 48/49 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +12.7 | 1e-34 | 44/44 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +9.7 | 4e-20 | 41/45 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +8.2 | 3e-14 | 45/48 (LOX-IMVI, RKO, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.58×** | +7.4 | 1e-11 | 40/48 (SW480, SHP-77, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.48×** | +6.4 | 2e-08 | 40/48 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +6.0 | 2e-07 | 39/48 (SHP-77, SW480, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.30×** | +6.0 | 2e-07 | 32/49 (NCI-H2347, PANC-1, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +5.6 | 1e-06 | 40/48 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.005 | 36/48 (A498, LS 180, …) | two highest doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.009 | 32/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.26×** | +3.7 | 0.012 | 27/50 (LOX-IMVI, SK-MEL-2, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.6 | 0.016 | 20/38 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Isocorydine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.055 | 6/49 (COLO 205, NCI-H23, …) | inconsistent across doses |  |
| [[Lipoic acid (drug)]] 5 µM |  | 1.15× | +3.2 | 0.055 | 8/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.062 | 22/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.14× | +3.0 | 0.077 | 11/49 (SW 900, RKO, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.707×** | -7.9 | 1e-12 | 37/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -4.7 | 7e-04 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.754×** | -4.4 | 0.002 | 32/48 (KATO III, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.800×** | -3.5 | 0.073 | 24/49 (HepG2/C3A, NCI-H2030, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.867× | -3.3 | 0.13 | 12/48 (BT-474, CFPAC-1, …) | top dose only | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 0.819× | -3.1 | 0.17 | 21/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 105 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.30× (z +9.2) | — |
| [[A549 (line)]] | wt | 114 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.17× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 133 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -10.3) |
| [[NCI-H2347 (line)]] | alt | 168 | 2 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.0) ⚠ cell-cycle shift, explains ~17% of this change | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -15.8) |
| [[PANC-1 (line)]] | alt | 118 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +15.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 96.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.05× (z +8.6) | — |
| [[A-427 (line)]] | wt | 85.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.58× (z +12.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.448× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 198 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.586× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 144 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -16.0) |
| [[HS-578T (line)]] | alt | 134 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +12.1) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 130 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -11.3) |
| [[KATO III (line)]] | alt | 196 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 84.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -10.5) |
| [[SHP-77 (line)]] | alt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 96.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +13.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 91.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.36× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 146 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -9.7) |
| [[C-33 A (line)]] | alt | 83.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +10.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +12.1) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 146 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.28× (z +8.8) ⚠ toxic; transcription drop | [[Verteporfin (drug)]] 5 µM 0.294× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +13.2) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 118 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +13.4) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 138 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.41× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.1) |
| [[SW 900 (line)]] | alt | 140 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -10.5) |
| [[SW1417 (line)]] | alt | 126 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.29× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.6) |
| [[A-172 (line)]] | wt | 97.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.2) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -10.9) |
| [[C32 (line)]] | wt | 79.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.3) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.8) |
| [[HT-29 (line)]] | alt | 155 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 179 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 144 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.47× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 90.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.6) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 108 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 215 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7]] | +0.80 | +0.72 / +0.81 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 969 |
| [[SEL1L]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 412 |
| [[SEC61A1]] | +0.76 | +0.78 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 445 |
| [[RPN1]] | +0.76 | +0.81 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 698 |
| [[HDLBP]] | +0.76 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[HYOU1]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[STT3A]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CANX]] | +0.75 | +0.74 / +0.80 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 538 |
| [[SSR1]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 | STRING 536 |
| [[LMAN1]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 850 |
| [[COPG1]] | +0.72 | +0.72 / +0.76 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 629 |
| [[SLC39A7]] | +0.71 | +0.77 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[GPATCH8]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity weakens TMED2's drug response | lines that do not express GALNT3 (30) vs lines expressing it (19) | the lines without GALNT3 respond 1.17× as strongly (z diff -0.93); strongest at Belinostat 5 µM: 1.62x vs 1.27x (z diff -2.4) | 0.075 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.4, -30.3); signed map (-55.4, 7.7). **Vector** length 134, 45.9% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.65 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.64 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.65 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +12.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +6.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +3.7 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +2.9 | +1.0 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | +2.8 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.8 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -7.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.7 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -1.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -1.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.2 | -2.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.1 | -2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,584,533-123,598,582 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNP24, P24A, p24beta1, p24b1 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Hallmark sets | PROTEIN_SECRETION, DNA_REPAIR |
| Reactome | 14 pathways, smallest: Pre-NOTCH Processing in Golgi; Cargo concentration in the ER; COPII-mediated vesicle transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15363](https://www.uniprot.org/uniprotkb/Q15363) (Transmembrane emp24 domain-containing protein 2):

> Involved in vesicular protein trafficking. Mainly functions in the early secretory pathway but also in post-Golgi membranes. Thought to act as cargo receptor at the lumenal side for incorporation of secretory cargo molecules into transport vesicles and to be involved in vesicle coat formation at the cytoplasmic side. In COPII vesicle-mediated anterograde transport involved in the transport of GPI-anchored proteins and proposed to act together with TMED10 as their cargo receptor; the function …

**Summary**, from NCBI Gene [10959](https://www.ncbi.nlm.nih.gov/gene/10959):

> Predicted to enable frizzled binding activity and smoothened binding activity. Involved in several processes, including negative regulation of GTPase activity; protein localization to plasma membrane; and regulation of cargo loading into COPII-coated vesicle. Located in Golgi apparatus; endoplasmic reticulum; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16996) · Entrez [10959](https://www.ncbi.nlm.nih.gov/gene/10959) · UniProt [Q15363](https://www.uniprot.org/uniprotkb/Q15363) · Ensembl [ENSG00000086598](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086598)

## Data

Gene col 1465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1465); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1465]; `tensor/DDL_lfc|DDL_z.npy` [1465]; `embed/gene_vectors.npy` [1465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1465 or target_col == 1465). Every well: [[TMED2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
