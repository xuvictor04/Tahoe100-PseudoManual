---
symbol: "TUBD1"
type: "gene"
col: 2944
ensembl_id: "ENSG00000108423"
name: "tubulin delta 1"
location: "17q23.1"
module: 54
arm: "+"
pooled_cpm: 25.0
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 24
n_dd_up_clean: 6
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TUBD1

*tubulin delta 1* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.79× (z +9.2, q 1e-17, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.495× (z -10.7, q 5e-24, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.643× (z -9.9, q 1e-20, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRGAP2D]] (+0.64, fdr 9e-06), [[SMYD4]] (+0.63, fdr 1e-05), [[DTX2P1-UPK3BP1-PMS2P11]] (+0.62, fdr 1e-05); moves opposite to [[EIF4G2]] (-0.57, fdr 3e-05), [[RAP2C]] (-0.56, fdr 3e-05), [[SCRN1]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2944.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +9.2 | 1e-17 | 38/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.7 | 3e-09 | 31/48 (A549, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 3e-09 | 29/48 (C32, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +5.8 | 9e-07 | 26/48 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.5 | 6e-06 | 27/47 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.7 | 3e-04 | 22/45 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.064 | 7/47 (C32, HEC-1-A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.22× | +3.1 | 0.12 | 14/47 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | 1.43× | +3.0 | 0.15 | 10/48 (HOP62, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2944.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.495×** | -10.7 | 5e-24 | 37/47 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -9.9 | 1e-20 | 28/44 (C32, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.643×** | -9.9 | 1e-20 | 35/47 (SW 900, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.566×** | -9.0 | 3e-17 | 35/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.573×** | -8.8 | 2e-16 | 32/47 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.573×** | -8.5 | 2e-15 | 25/37 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -7.7 | 1e-12 | 33/47 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.632×** | -7.3 | 3e-11 | 37/47 (SW 900, HEC-1-A, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -6.7 | 1e-09 | 23/43 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.657×** | -6.4 | 9e-09 | 27/48 (SW 900, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.677×** | -6.2 | 3e-08 | 29/48 (A498, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -6.0 | 9e-08 | 27/48 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.711×** | -5.4 | 3e-06 | 23/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -4.0 | 0.003 | 18/48 (NCI-H23, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.618×** | -4.0 | 0.003 | 22/48 (Panc 03.27, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.642×** | -3.7 | 0.008 | 17/47 (Panc 03.27, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.654×** | -3.5 | 0.014 | 12/46 (SW 900, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.673×** | -3.3 | 0.030 | 10/47 (Panc 03.27, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.815×** | -3.2 | 0.036 | 16/47 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -3.0 | 0.068 | 18/47 (SW 1271, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.829×** | -2.9 | 0.078 | 8/48 (BT-474, SW 1088, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2944. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.310× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.359× (z -9.8) |
| [[SNU-1 (line)]] | wt | 30.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.109× (z -11.5) |
| [[SW 900 (line)]] | alt | 29.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -16.5) |
| [[A-427 (line)]] | wt | 45.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.364× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 20.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -15.1) |
| [[A498 (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.236× (z -9.8) |
| [[BT-474 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0831× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -8.7) |
| [[C-33 A (line)]] | alt | 60.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.240× (z -11.7) ⚠ toxic |
| [[HOP62 (line)]] | alt | 27.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.307× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.496× (z -8.5) |
| [[LoVo (line)]] | wt | 24.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 23.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -8.6) |
| [[SW480 (line)]] | alt | 26.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.427× (z -8.7) |
| [[A-172 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.4) |
| [[A549 (line)]] | wt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -12.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 42.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0838× (z -10.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -8.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0921× (z -10.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0959× (z -12.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 19.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -8.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.8) |
| [[SW1417 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.4) |
| [[SW48 (line)]] | wt | 23.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0670× (z -12.4) |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2944), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRGAP2D]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[SMYD4]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DTX2P1-UPK3BP1-PMS2P11]] | +0.62 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[UBE2R2]] | +0.61 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[FAM222B]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[GTF3C2]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SNRPD2]] | +0.58 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[NR2C1]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[QRICH1]] | +0.57 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[ANAPC11]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[NUP160]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[AURKAIP1]] | +0.57 | +0.42 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[RAP2C]] | -0.56 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[SEPTIN8]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[HNRNPK]] | -0.53 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[PARP3]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PRKAR1A]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[LIN7C]] | -0.52 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[SEPTIN11]] | -0.52 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[ZNF664]] | -0.51 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[PIEZO1]] | -0.51 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[GMFB]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TUBD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.638). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-51.7, -23.9); signed map (-39.0, 4.9). **Vector** length 88.0, 19.4% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.6 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +2.9 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +9.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -2.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Decitabine (drug)]] 0.5 µM |  | +1.5 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.0 | -6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.5 | -8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.4 | -9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.8 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -6.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | +0.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | tubulin delta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,859,479-59,892,945 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12709, TUBD |
| Gene groups (HGNC) | Tubulin delta family |
| Hallmark sets | MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJT1](https://www.uniprot.org/uniprotkb/Q9UJT1) (Tubulin delta chain):

> Acts as a positive regulator of hedgehog signaling and regulates ciliary function.

**Summary**, from NCBI Gene [51174](https://www.ncbi.nlm.nih.gov/gene/51174):

> Predicted to enable GTP binding activity. Predicted to be a structural constituent of cytoskeleton. Involved in microtubule cytoskeleton organization. Located in centrosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16811) · Entrez [51174](https://www.ncbi.nlm.nih.gov/gene/51174) · UniProt [Q9UJT1](https://www.uniprot.org/uniprotkb/Q9UJT1) · Ensembl [ENSG00000108423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108423)

## Data

Gene col 2944: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2944); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2944, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2944]; `tensor/DDL_lfc|DDL_z.npy` [2944]; `embed/gene_vectors.npy` [2944]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2944 or target_col == 2944). Every well: [[TUBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
