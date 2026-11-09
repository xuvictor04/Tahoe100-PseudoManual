---
symbol: "DET1"
type: "gene"
col: 6428
ensembl_id: "ENSG00000140543"
name: "DET1 partner of COP1 E3 ubiquitin ligase"
location: "15q26.1"
module: 170
arm: "+"
pooled_cpm: 17.32
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# DET1

*DET1 partner of COP1 E3 ubiquitin ligase* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.03× (z +5.1, q 1e-04, up in 19 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.222× (z -20.8, q 0e+00, down in 44 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.227× (z -20.5, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN8]] (+0.64, fdr 7e-06), [[WDR89]] (+0.60, fdr 1e-05), [[MTERF4]] (+0.60, fdr 1e-05); moves opposite to [[GLA]] (-0.53, fdr 3e-05), [[MAGI3]] (-0.52, fdr 2e-05), [[ATP1B3]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[FBXL9P]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +5.1 | 1e-04 | 19/47 (RKO, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.065 | 13/46 (CFPAC-1, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.065 | 17/47 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.073 | 16/47 (LoVo, PANC-1, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.073 | 7/47 (SK-MEL-2, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.079 | 13/47 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.097 | 8/47 (SK-MEL-2, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.222×** | -20.8 | 0e+00 | 44/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.227×** | -20.5 | 0e+00 | 47/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.317×** | -15.9 | 0e+00 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.442×** | -11.3 | 2e-27 | 41/46 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.405×** | -11.2 | 7e-27 | 31/44 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.575×** | -10.8 | 4e-25 | 29/45 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.467×** | -10.5 | 6e-24 | 36/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.482×** | -10.1 | 5e-22 | 33/47 (PANC-1, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.486×** | -8.9 | 3e-17 | 34/46 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **0.541×** | -8.5 | 1e-15 | 24/37 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.576×** | -7.2 | 4e-11 | 28/46 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.619×** | -6.6 | 2e-09 | 29/46 (C32, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -6.5 | 3e-09 | 24/46 (HOP62, SHP-77, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.650×** | -5.8 | 3e-07 | 26/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.651×** | -5.5 | 2e-06 | 19/31 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.719×** | -4.5 | 2e-04 | 23/45 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.571×** | -4.0 | 0.001 | 17/46 (NCI-H460, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.715×** | -3.3 | 0.024 | 7/47 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.025 | 6/47 (SK-MEL-2, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.803×** | -2.9 | 0.072 | 6/47 (J82, SNU-423, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.808×** | -2.9 | 0.086 | 6/47 (J82, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.1 | 0 | 14 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0650× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -19.0) |
| [[PANC-1 (line)]] | alt | 29.4 | 0 | 14 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0660× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0702× (z -25.1) |
| [[HOP62 (line)]] | alt | 26.2 | 0 | 9 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0706× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -13.1) |
| [[A549 (line)]] | wt | 31.2 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -9.3) |
| [[J82 (line)]] | alt | 15.0 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0329× (z -20.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.166× (z -10.7) |
| [[SW480 (line)]] | alt | 16.2 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0599× (z -21.7) |
| [[LoVo (line)]] | wt | 17.8 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.257× (z -10.5) |
| [[SHP-77 (line)]] | alt | 17.3 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.139× (z -10.2) |
| [[SNU-423 (line)]] | alt | 17.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0804× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -13.7) |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0381× (z -19.8) |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.304× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 21.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -15.2) |
| [[HT-29 (line)]] | alt | 28.0 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -12.6) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 4 (3 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0287× (z -13.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -12.1) |
| [[C32 (line)]] | wt | 18.1 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0534× (z -16.4) |
| [[HepG2_C3A (line)]] | wt | 9.70 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0603× (z -10.5) |
| [[KATO III (line)]] | alt | 28.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0531× (z -20.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -11.8) |
| [[BT-474 (line)]] | alt | 15.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0885× (z -12.5) |
| [[H4 (line)]] | wt | 17.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0644× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0941× (z -10.1) |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -11.1) |
| [[A-427 (line)]] | wt | 8.05 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -9.1) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 7.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.168× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.238× (z -8.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.129× (z -9.5) |
| [[HS-578T (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0292× (z -18.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 9.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0894× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.49 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0530× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.211× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 9.91 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.149× (z -8.9) |
| [[RKO (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -10.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0809× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW 900 (line)]] | alt | 11.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.103× (z -11.4) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN8]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[WDR89]] | +0.60 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[MTERF4]] | +0.60 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[LINC00412]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MTRES1]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[ZNF333]] | +0.55 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PEX7]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TAMM41]] | +0.55 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TUT1]] | +0.55 | +0.57 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLA]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[MAGI3]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ATP1B3]] | -0.49 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[CHRNA5]] | -0.48 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[DPY19L1]] | -0.48 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[ELOVL5]] | -0.47 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PEAK1]] | -0.46 | -0.49 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXL9P]] | C | DET1's natural level strengthens FBXL9P's drug response | DET1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.14; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-49.1, 7.0); signed map (-12.6, -16.0). **Vector** length 71.1, 14.6% of its response variance represented; |z| ≥ 3 in 1,131 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.1 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.4 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.3 | -11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.8 | -11.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -20.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -15.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -20.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -3.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DET1 partner of COP1 E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:88,494,440-88,546,681 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10103 |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5Y6](https://www.uniprot.org/uniprotkb/Q7L5Y6) (DET1 homolog):

> Component of the E3 ubiquitin ligase DCX DET1-COP1 complex, which is required for ubiquitination and subsequent degradation of target proteins. The complex is involved in JUN ubiquitination and degradation.

**Summary**, from NCBI Gene [55070](https://www.ncbi.nlm.nih.gov/gene/55070):

> Enables ubiquitin protein ligase binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in positive regulation of proteasomal ubiquitin-dependent protein catabolic process; protein ubiquitination; and protein-containing complex assembly. Part of Cul4A-RING E3 ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25477) · Entrez [55070](https://www.ncbi.nlm.nih.gov/gene/55070) · UniProt [Q7L5Y6](https://www.uniprot.org/uniprotkb/Q7L5Y6) · Ensembl [ENSG00000140543](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140543)

## Data

Gene col 6428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6428); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6428]; `tensor/DDL_lfc|DDL_z.npy` [6428]; `embed/gene_vectors.npy` [6428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6428 or target_col == 6428). Every well: [[DET1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DET1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
