---
symbol: "CSNK1G3"
type: "gene"
col: 7503
ensembl_id: "ENSG00000151292"
name: "casein kinase 1 gamma 3"
location: "5q23.2"
module: 188
arm: "+"
pooled_cpm: 133.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# CSNK1G3

*casein kinase 1 gamma 3* — 5q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.45× (z +10.9, q 1e-24, up in 35 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.28× (z +7.7, q 4e-12, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.873× (z -14.6, q 1e-45, down in 6 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.820× (z -4.5, q 8e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF2A]] (+0.61, fdr 1e-05), [[RNF2]] (+0.59, fdr 2e-05), [[MACIR]] (+0.58, fdr 3e-05); moves opposite to [[OPA3]] (-0.57, fdr 2e-05), [[CTNS]] (-0.46, fdr 4e-05), [[SCAMP4]] (-0.45, fdr 2e-04).
> It is in [[Module 188]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +10.9 | 1e-24 | 35/47 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +7.7 | 4e-12 | 33/48 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.25×** | +7.1 | 2e-10 | 28/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +6.8 | 2e-09 | 15/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +6.3 | 4e-08 | 26/49 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +6.0 | 2e-07 | 32/48 (SK-MEL-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +5.8 | 5e-07 | 27/45 (SNU-423, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.8 | 9e-05 | 19/48 (SNU-423, HT-29, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.16× | +4.8 | 9e-05 | 18/49 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +4.8 | 9e-05 | 5/49 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.09× | +4.0 | 0.003 | 3/48 (C32, AN3 CA, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.004 | 14/49 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 5 µM |  | 1.13× | +3.6 | 0.016 | 9/48 (A-427, LOX-IMVI, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.5 | 0.018 | 9/48 (NCI-H460, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 1.08× | +3.3 | 0.042 | 2/48 (CHP-212, SW 1088) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | 1.11× | +3.2 | 0.051 | 13/47 (NCI-H2030, SNU-423, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.15× | +3.1 | 0.054 | 14/49 (C32, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.07× | +3.1 | 0.054 | 0/49 | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.076 | 6/48 (HOP62, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 1.10× | +2.9 | 0.093 | 3/48 (NCI-H460, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7503.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -14.6 | 1e-45 | 6/50 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.770×** | -7.7 | 4e-12 | 26/44 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.809×** | -6.7 | 4e-09 | 23/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.864× | -4.6 | 5e-04 | 17/48 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.820×** | -4.5 | 8e-04 | 24/48 (RPMI-7951, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.870× | -4.4 | 0.001 | 14/48 (SHP-77, J82, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.874× | -4.2 | 0.002 | 15/48 (BT-474, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.780×** | -4.1 | 0.003 | 19/48 (RKO, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.916× | -3.9 | 0.005 | 15/49 (A-172, A549, …) | top dose only |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.872× | -3.9 | 0.005 | 13/47 (SK-MEL-2, SW48, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.887× | -3.8 | 0.008 | 16/48 (LOX-IMVI, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.888× | -3.7 | 0.008 | 18/48 (LOX-IMVI, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change | 0.892× | -3.6 | 0.014 | 19/49 (SK-MEL-2, SNU-1, …) | rises with dose | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.896× | -3.5 | 0.020 | 10/48 (RKO, HepG2/C3A, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.020 | 20/48 (A-427, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.891× | -3.4 | 0.022 | 5/48 (NCI-H23, A498, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.928× | -3.3 | 0.027 | 1/48 (CHP-212) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.818×** | -3.3 | 0.027 | 15/48 (MIA PaCa-2, A-172, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.477× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 157 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.500× (z -10.3) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 207 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.26× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 165 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.79× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.280× (z -20.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 147 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.20× (z +19.0) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 1.57× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 144 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +10.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.07× (z +10.6) | — |
| [[NCI-H1573 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.574× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 195 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.41× (z +11.9) ⚠ toxic | — |
| [[PANC-1 (line)]] | alt | 130 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.56× (z +8.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.619× (z -9.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 63.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.54× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 96.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.58× (z +8.5) | — |
| [[H4 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.437× (z -8.6) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 154 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.22× (z +8.8) ⚠ toxic | — |
| [[HOP62 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.501× (z -10.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 131 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.430× (z -10.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 155 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.496× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 172 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.365× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW 1088 (line)]] | alt | 118 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.113× (z -9.6) |
| [[A-172 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 227 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 185 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 128 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF2A]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RNF2]] | +0.59 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[MACIR]] | +0.58 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[L3MBTL3]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[LRP12]] | +0.54 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[DYNC1LI1]] | +0.54 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MBD2]] | +0.54 | +0.58 / +0.37 | both halves | 9e-05 |  |
| [[REPS1]] | +0.54 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[CHORDC1]] | +0.54 | +0.62 / +0.42 | both halves | 4e-05 |  |
| [[CASP6]] | +0.53 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[CDC40]] | +0.53 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SPOPL]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA3]] | -0.57 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[CTNS]] | -0.46 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SCAMP4]] | -0.45 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[DMWD]] | -0.45 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[CACTIN]] | -0.45 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[ENSA]] | -0.44 | -0.58 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[TNPO2]] | -0.44 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[FNIP1]] | -0.44 | -0.51 / -0.28 | both halves | 3e-04 |  |
| [[CTDNEP1]] | -0.44 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[TM9SF4]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SEC23B]] | -0.44 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[RFX1]] | -0.43 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[SEC16A]] | -0.43 | -0.38 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers CSNK1G3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.7, -4.1); signed map (-36.2, -18.4). **Vector** length 113, 29.2% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +6.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +6.5 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | +2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +10.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.2 | +4.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -8.6 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.9 | -4.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.3 | -4.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.1 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 gamma 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q23.2 — chr5:123,512,177-123,617,049 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Casein kinase 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6M4](https://www.uniprot.org/uniprotkb/Q9Y6M4) (Casein kinase I isoform gamma-3):

> Serine/threonine-protein kinase. Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. It can phosphorylate a large number of proteins. Participates in Wnt signaling. Regulates fast synaptic transmission mediated by glutamate (By similarity).

**Summary**, from NCBI Gene [1456](https://www.ncbi.nlm.nih.gov/gene/1456):

> This gene encodes a member of a family of serine/threonine protein kinases that phosphorylate caseins and other acidic proteins. A related protein in the African clawed frog participates in the transmission of Wnt/beta-catenin signaling. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:2456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2456) · Entrez [1456](https://www.ncbi.nlm.nih.gov/gene/1456) · UniProt [Q9Y6M4](https://www.uniprot.org/uniprotkb/Q9Y6M4) · Ensembl [ENSG00000151292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151292)

## Data

Gene col 7503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7503); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7503]; `tensor/DDL_lfc|DDL_z.npy` [7503]; `embed/gene_vectors.npy` [7503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7503 or target_col == 7503). Every well: [[CSNK1G3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1G3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
