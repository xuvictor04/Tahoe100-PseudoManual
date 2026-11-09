---
symbol: "DDX50"
type: "gene"
col: 2864
ensembl_id: "ENSG00000107625"
name: "DExD-box helicase 50"
location: "10q22.1"
module: 52
arm: "+"
pooled_cpm: 114.67
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DDX50

*DExD-box helicase 50* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.46× (z +8.1, q 3e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.505× (z -13.9, q 2e-41, down in 45 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.633× (z -9.7, q 5e-20, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKAG1]] (+0.67, fdr 7e-06), [[ESCO1]] (+0.64, fdr 1e-05), [[UBE2V2]] (+0.63, fdr 7e-06); moves opposite to [[NCKAP1]] (-0.59, fdr 1e-05), [[CTSZ]] (-0.57, fdr 2e-05), [[PLPP2]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FOXD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.1 | 3e-13 | 31/48 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +5.9 | 1e-06 | 30/48 (NCI-H1573, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 0.001 | 26/48 (LOX-IMVI, RKO, …) | all doses, flat |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.005 | 26/48 (C32, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | 1.14× | +4.1 | 0.005 | 21/48 (LoVo, Hs 766T, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.505×** | -13.9 | 2e-41 | 45/47 (BT-474, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -10.5 | 2e-23 | 35/44 (SK-MEL-2, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.633×** | -9.7 | 5e-20 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -8.6 | 8e-16 | 34/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.697×** | -7.7 | 2e-12 | 30/49 (H4, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -7.3 | 2e-11 | 36/48 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.743×** | -6.3 | 3e-08 | 28/48 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.811×** | -6.3 | 3e-08 | 28/48 (C32, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.749×** | -5.8 | 5e-07 | 34/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.755×** | -5.5 | 2e-06 | 28/45 (J82, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -5.2 | 1e-05 | 31/48 (LoVo, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.850× | -4.9 | 5e-05 | 22/49 (AN3 CA, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -4.8 | 6e-05 | 26/48 (C32, SW48, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -4.8 | 8e-05 | 4/50 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.794×** | -4.6 | 2e-04 | 30/48 (AsPC-1, C32, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.862× | -4.4 | 3e-04 | 18/48 (J82, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.812×** | -4.4 | 4e-04 | 23/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.692×** | -4.1 | 0.001 | 26/47 (RKO, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.002 | 25/48 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.831×** | -3.9 | 0.003 | 23/48 (RKO, C32, …) | top dose only |  |
| [[crizotinib (drug)]] 5 µM |  | 0.837× | -3.6 | 0.008 | 17/48 (HS-578T, C32, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.838× | -3.6 | 0.008 | 22/48 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.846× | -3.5 | 0.010 | 22/49 (RKO, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.841× | -3.4 | 0.016 | 19/48 (RKO, AsPC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 112 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.370× (z -14.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.462× (z -11.8) |
| [[PANC-1 (line)]] | alt | 204 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +8.6) ⚠ cell-cycle shift, explains ~85% of this change | [[Digitoxin (drug)]] 5 µM 0.465× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.480× (z -10.4) |
| [[RKO (line)]] | wt | 210 | 0 | 6 (3 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.502× (z -11.4) |
| [[H4 (line)]] | wt | 123 | 0 | 5 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 132 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.18× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.281× (z -13.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 125 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.304× (z -11.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.384× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 121 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.423× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 122 | 2 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.542× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.366× (z -11.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.240× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 105 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +9.9) | — |
| [[LoVo (line)]] | wt | 81.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +12.4) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.04× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.505× (z -8.9) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 154 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.420× (z -9.3) |
| [[A549 (line)]] | wt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 66.7 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.183× (z -16.3) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 146 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.4) ⚠ cell-cycle shift, explains ~85% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.454× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 109 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.387× (z -10.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 65.3 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.343× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 97.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -21.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 117 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 124 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -8.7) ⚠ cell-cycle shift, explains ~1% of this change |
| [[A-427 (line)]] | wt | 114 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.179× (z -10.8) |
| [[A498 (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.499× (z -9.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 218 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -10.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[C-33 A (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.405× (z -9.6) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 55.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -9.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 72.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.427× (z -9.3) |
| [[KATO III (line)]] | alt | 50.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.38× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.402× (z -10.6) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 163 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.370× (z -10.5) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 88.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -13.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.383× (z -9.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 94.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -14.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 73.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.478× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 91.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 99.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKAG1]] | +0.67 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ESCO1]] | +0.64 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[UBE2V2]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GOLGA1]] | +0.62 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[GCAT]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[FBXO45]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DIABLO]] | +0.60 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MAP7D3]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[METTL23]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[ZNF397]] | +0.58 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SRA1]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[MRPL2]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP1]] | -0.59 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PLPP2]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[FUCA2]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[APP]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.53 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.52 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[NPEPPSP1]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[SMG7]] | -0.52 | -0.46 / -0.60 | both halves | 3e-05 |  |
| [[ANKRD10]] | -0.51 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ERBB2]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[VSIG10]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXD1]] | B | FOXD1 activity raises DDX50's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.55× lower at baseline in the lines without FOXD1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.439). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-24.7, 17.6); signed map (8.6, -16.0). **Vector** length 150, 49.2% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.3 | +8.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | +7.2 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.7 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.7 | +1.8 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -12.0 | -13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.6 | -10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.1 | -7.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.0 | -6.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.1 | -8.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.0 | -4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | DExD-box helicase 50 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:68,901,286-68,946,847 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GU2, MGC3199, GUB, RH-II/GuB |
| Gene groups (HGNC) | DEAD-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ39](https://www.uniprot.org/uniprotkb/Q9BQ39) (ATP-dependent RNA helicase DDX50):

> ATP-dependent RNA helicase that may play a role in various aspects of RNA metabolism including pre-mRNA splicing or ribosomal RNA production. Also acts as a viral restriction factor and promotes the activation of the NF-kappa-B and IRF3 signaling pathways following its stimulation with viral RNA or infection with RNA and DNA viruses. For instance, decreases vaccinia virus, herpes simplex virus, Zika virus or dengue virus replication during the early stage of infection. Mechanistically, acts via …

**Summary**, from NCBI Gene [79009](https://www.ncbi.nlm.nih.gov/gene/79009):

> DEAD box proteins, characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. …

**Accessions** — [HGNC:17906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17906) · Entrez [79009](https://www.ncbi.nlm.nih.gov/gene/79009) · UniProt [Q9BQ39](https://www.uniprot.org/uniprotkb/Q9BQ39) · Ensembl [ENSG00000107625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107625)

## Data

Gene col 2864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2864); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2864]; `tensor/DDL_lfc|DDL_z.npy` [2864]; `embed/gene_vectors.npy` [2864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2864 or target_col == 2864). Every well: [[DDX50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
