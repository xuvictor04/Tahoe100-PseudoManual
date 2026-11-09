---
symbol: "SP3"
type: "gene"
col: 10306
ensembl_id: "ENSG00000172845"
name: "Sp3 transcription factor"
location: "2q31.1"
module: 64
arm: "-"
pooled_cpm: 182.21
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# SP3

*Sp3 transcription factor* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.64× (z +7.3, q 1e-10, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.480× (z -13.7, q 4e-40, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOCS5]] (+0.61, fdr 1e-05), [[ZNF367]] (+0.57, fdr 1e-05), [[SKA2]] (+0.55, fdr 3e-05); moves opposite to [[TTC1]] (-0.54, fdr 8e-05), [[CYB5R1]] (-0.54, fdr 1e-04), [[CEP290]] (-0.52, fdr 4e-05).
> It sits in the **-** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.64×** | +7.3 | 1e-10 | 40/49 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.008 | 24/48 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.1 | 0.008 | 22/49 (LoVo, RKO, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.060 | 25/48 (A549, BT-474, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.085 | 27/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.480×** | -13.7 | 4e-40 | 47/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.517×** | -12.3 | 2e-32 | 46/48 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -11.7 | 3e-29 | 41/44 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.556×** | -11.0 | 7e-26 | 45/49 (RKO, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.576×** | -10.3 | 8e-23 | 44/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.612×** | -9.2 | 4e-18 | 44/48 (A-172, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -7.7 | 9e-13 | 34/45 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -6.4 | 1e-08 | 39/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.704×** | -6.2 | 4e-08 | 35/48 (A-172, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.737×** | -5.7 | 6e-07 | 35/48 (A-172, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.571×** | -4.2 | 0.001 | 30/45 (RPMI-7951, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.833× | -3.4 | 0.030 | 23/48 (A549, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | 0.839× | -3.3 | 0.043 | 21/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.845× | -3.2 | 0.062 | 21/48 (A-172, NCI-H1573, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.846× | -3.1 | 0.062 | 23/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.667×** | -3.1 | 0.071 | 20/47 (HEC-1-A, A549, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.0 | 0.075 | 19/47 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 321 | 0 | 16 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -13.1) |
| [[HOP62 (line)]] | alt | 231 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.292× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 237 | 0 | 10 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.440× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 198 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -10.8) |
| [[COLO 205 (line)]] | alt | 254 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.367× (z -9.8) |
| [[SW480 (line)]] | alt | 216 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.367× (z -14.5) |
| [[A549 (line)]] | wt | 223 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -13.0) |
| [[SW 900 (line)]] | alt | 203 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 221 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.347× (z -13.9) |
| [[HEC-1-A (line)]] | alt | 186 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.390× (z -14.7) |
| [[A498 (line)]] | wt | 312 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.422× (z -10.4) |
| [[HT-29 (line)]] | alt | 147 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 185 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.425× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 163 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.35× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.479× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 207 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 238 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.506× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 170 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.358× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.500× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.400× (z -10.7) |
| [[PANC-1 (line)]] | alt | 186 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -10.9) |
| [[SW1417 (line)]] | alt | 233 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.295× (z -17.3) |
| [[A-427 (line)]] | wt | 158 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -9.7) |
| [[HS-578T (line)]] | alt | 158 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -12.1) |
| [[LoVo (line)]] | wt | 117 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 173 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 174 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.445× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.6) |
| [[BT-474 (line)]] | alt | 131 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.476× (z -8.5) |
| [[C32 (line)]] | wt | 123 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.385× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 153 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.398× (z -9.4) |
| [[Hs 766T (line)]] | wt | 113 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -9.6) |
| [[J82 (line)]] | alt | 155 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.519× (z -9.0) |
| [[KATO III (line)]] | alt | 112 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.499× (z -9.2) |
| [[LS 180 (line)]] | wt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H1792 (line)]] | alt | 127 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.467× (z -8.8) |
| [[RKO (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 98.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0792× (z -29.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 162 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -13.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 129 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.368× (z -9.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 158 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 217 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 173 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS5]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ZNF367]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[SKA2]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[MEX3C]] | +0.55 | +0.39 / +0.51 | both halves | 5e-05 |  |
| [[LINC00938]] | +0.54 | +0.31 / +0.49 | both halves | 2e-04 |  |
| [[NIPBL-DT]] | +0.54 | +0.36 / +0.41 | both halves | 1e-04 |  |
| [[FBXO5]] | +0.53 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MSL2]] | +0.53 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[LEMD3]] | +0.53 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[HNRNPLL]] | +0.52 | +0.36 / +0.57 | both halves | 9e-05 |  |
| [[TAPT1]] | +0.52 | +0.26 / +0.51 | both halves | 4e-04 |  |
| [[GPR19]] | +0.51 | +0.30 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC1]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[CYB5R1]] | -0.54 | -0.36 / -0.49 | both halves | 1e-04 |  |
| [[CEP290]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[CALCOCO2]] | -0.52 | -0.26 / -0.49 | both halves | 3e-04 |  |
| [[STX8]] | -0.50 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[FAM241B]] | -0.50 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[DNAJB1]] | -0.49 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[ERC1]] | -0.48 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[HSPA9]] | -0.48 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[DFFA]] | -0.47 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[EXOC6B]] | -0.47 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[PSMD3]] | -0.47 | -0.38 / -0.46 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises SP3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises SP3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **-** arm (projection on the module's main direction -0.343). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-41.4, -41.1); signed map (-42.3, -51.7). **Vector** length 105, 35.2% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +11.4 | +4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.4 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -7.5 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.9 | -6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -9.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -3.9 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.4 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Sp3 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:173,880,850-173,965,373 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPR-2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Sp transcription factors |
| Reactome | 3 pathways, smallest: SUMOylation of transcription factors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02447](https://www.uniprot.org/uniprotkb/Q02447) (Transcription factor Sp3):

> Transcriptional factor that can act as an activator or repressor depending on isoform and/or post-translational modifications. Binds to GT and GC boxes promoter elements. Competes with SP1 for the GC-box promoters. Weak activator of transcription but can activate a number of genes involved in different processes such as cell-cycle regulation, hormone-induction and house-keeping.

**Summary**, from NCBI Gene [6670](https://www.ncbi.nlm.nih.gov/gene/6670):

> This gene belongs to a family of Sp1 related genes that encode transcription factors that regulate transcription by binding to consensus GC- and GT-box regulatory elements in target genes. This protein contains a zinc finger DNA-binding domain and several transactivation domains, and has been reported to function as a bifunctional transcription factor that either stimulates or represses the transcription of numerous genes. Transcript variants encoding different isoforms have been described for …

**Accessions** — [HGNC:11208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11208) · Entrez [6670](https://www.ncbi.nlm.nih.gov/gene/6670) · UniProt [Q02447](https://www.uniprot.org/uniprotkb/Q02447) · Ensembl [ENSG00000172845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172845)

## Data

Gene col 10306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10306); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10306]; `tensor/DDL_lfc|DDL_z.npy` [10306]; `embed/gene_vectors.npy` [10306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10306 or target_col == 10306). Every well: [[SP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
