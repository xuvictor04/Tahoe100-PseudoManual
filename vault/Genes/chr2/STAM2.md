---
symbol: "STAM2"
type: "gene"
col: 3627
ensembl_id: "ENSG00000115145"
name: "signal transducing adaptor molecule 2"
location: "2q23.3"
module: 49
arm: "+"
pooled_cpm: 76.0
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# STAM2

*signal transducing adaptor molecule 2* — 2q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.26× (z +4.3, q 0.008, up in 26 of 48 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[GSK1059615 (drug)]] 5 µM: 1.43× (z +3.7, q 0.071, up in 21 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 1.67×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.92×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.472× (z -20.9, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC1LI2]] (+0.68, fdr 7e-06), [[IFT52]] (+0.66, fdr 1e-05), [[POLR2C]] (+0.65, fdr 1e-05); moves opposite to [[PHC2-AS1]] (-0.60, fdr 3e-05), [[TLCD3A]] (-0.58, fdr 3e-05), [[ZNF876P]] (-0.58, fdr 9e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3627.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 1.67×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SK-MEL-2 2.92×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +4.3 | 0.008 | 26/48 (PANC-1, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.071 | 21/49 (A498, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -20.9 | 0e+00 | 47/49 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.559×** | -11.0 | 9e-26 | 43/50 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -10.8 | 5e-25 | 39/48 (HS-578T, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -9.4 | 7e-19 | 37/47 (NCI-H460, H4, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.644×** | -8.7 | 5e-16 | 36/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.737×** | -8.5 | 2e-15 | 32/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.646×** | -8.0 | 1e-13 | 30/45 (NCI-H1792, RPMI-7951, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.701×** | -7.0 | 2e-10 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -5.9 | 2e-07 | 31/47 (HepG2/C3A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -5.9 | 2e-07 | 0/50 | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.741×** | -5.9 | 2e-07 | 28/49 (AsPC-1, LS 180, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.583×** | -5.6 | 1e-06 | 29/49 (HS-578T, AsPC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.767×** | -5.2 | 8e-06 | 29/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.795×** | -4.5 | 2e-04 | 27/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.645×** | -4.5 | 2e-04 | 27/48 (RPMI-7951, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.824×** | -3.6 | 0.010 | 22/47 (RPMI-7951, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **0.788×** | -2.9 | 0.097 | 7/48 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 73.2 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.324× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 79.0 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -16.4) |
| [[HOP62 (line)]] | alt | 74.9 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -18.8) |
| [[HS-578T (line)]] | alt | 108 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -15.0) |
| [[A-172 (line)]] | wt | 72.8 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -16.5) |
| [[H4 (line)]] | wt | 95.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -14.5) |
| [[LS 180 (line)]] | wt | 92.9 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -11.8) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -9.2) |
| [[SW1417 (line)]] | alt | 97.0 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.3) |
| [[PANC-1 (line)]] | alt | 84.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -12.5) |
| [[SNU-1 (line)]] | wt | 91.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.356× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 51.1 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 82.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.5) |
| [[J82 (line)]] | alt | 68.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 77.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 64.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -18.6) |
| [[Panc 03.27 (line)]] | alt | 73.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 102 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 69.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -10.5) |
| [[SW 900 (line)]] | alt | 69.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.9) |
| [[SW48 (line)]] | wt | 80.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -11.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[A498 (line)]] | wt | 97.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -19.2) |
| [[A549 (line)]] | wt | 87.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -14.0) |
| [[C32 (line)]] | wt | 69.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 48.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -14.0) |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.4) |
| [[COLO 205 (line)]] | alt | 82.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -11.9) |
| [[HT-29 (line)]] | alt | 69.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -10.7) |
| [[hTERT-HPNE (line)]] | wt | 76.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[KATO III (line)]] | alt | 68.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -13.3) |
| [[LoVo (line)]] | wt | 79.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 78.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 58.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -13.9) |
| [[SHP-77 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.334× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SNU-423 (line)]] | alt | 68.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -16.0) |
| [[SW 1088 (line)]] | alt | 127 | 0 | 1 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0933× (z -8.7) |
| [[A-427 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1LI2]] | +0.68 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[IFT52]] | +0.66 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[POLR2C]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[COMMD2]] | +0.64 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[ARL1]] | +0.63 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[ACTR10]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[MED8]] | +0.62 | +0.67 / +0.29 | both halves | 2e-04 |  |
| [[MOCS2]] | +0.60 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[RPAP3]] | +0.59 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[UFSP2]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[VAMP7]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 | pathway: Cargo recognition for clathrin-mediated endocytosis; STRING 602 |
| [[ASCC2]] | +0.57 | +0.50 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TLCD3A]] | -0.58 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF876P]] | -0.58 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[TYSND1]] | -0.58 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[SAXO1]] | -0.56 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[MRM1]] | -0.55 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC14]] | -0.55 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[LEMD3]] | -0.54 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[SIAH2-AS1]] | -0.54 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[MBD3]] | -0.54 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[PRRC2B]] | -0.54 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[ARID1A]] | -0.54 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises STAM2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | STAM2's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | STAM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.526). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.5, -0.9); signed map (-23.7, -20.6). **Vector** length 107, 30.2% of its response variance represented; |z| ≥ 3 in 986 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.5 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.2 | +4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | +1.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -20.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.3 | -10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.5 | -8.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -5.0 | -8.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -3.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | signal transducing adaptor molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q23.3 — chr2:152,116,801-152,175,763 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Hbp |
| Gene groups (HGNC) | ESCRT-0; SH3 domain containing |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, SPERMATOGENESIS |
| Reactome | 19 pathways, smallest: InlB-mediated entry of Listeria monocytogenes into host cell; Listeria monocytogenes entry into host cells; Negative regulation of MET activity |
| Matched by | ensembl_id |

**Function**, from UniProt [O75886](https://www.uniprot.org/uniprotkb/O75886) (Signal transducing adapter molecule 2):

> Involved in intracellular signal transduction mediated by cytokines and growth factors. Upon IL-2 and GM-CSL stimulation, it plays a role in signaling leading to DNA synthesis and MYC induction. May also play a role in T-cell development. Involved in down-regulation of receptor tyrosine kinase via multivesicular body (MVBs) when complexed with HGS (ESCRT-0 complex). The ESCRT-0 complex binds ubiquitin and acts as a sorting machinery that recognizes ubiquitinated receptors and transfers them to …

**Summary**, from NCBI Gene [10254](https://www.ncbi.nlm.nih.gov/gene/10254):

> The protein encoded by this gene is closely related to STAM, an adaptor protein involved in the downstream signaling of cytokine receptors, both of which contain a SH3 domain and the immunoreceptor tyrosine-based activation motif (ITAM). Similar to STAM, this protein acts downstream of JAK kinases, and is phosphorylated in response to cytokine stimulation. This protein and STAM thus are thought to exhibit compensatory effects on the signaling pathway downstream of JAK kinases upon cytokine …

**Accessions** — [HGNC:11358](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11358) · Entrez [10254](https://www.ncbi.nlm.nih.gov/gene/10254) · UniProt [O75886](https://www.uniprot.org/uniprotkb/O75886) · Ensembl [ENSG00000115145](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115145)

## Data

Gene col 3627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3627); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3627]; `tensor/DDL_lfc|DDL_z.npy` [3627]; `embed/gene_vectors.npy` [3627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3627 or target_col == 3627). Every well: [[STAM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
