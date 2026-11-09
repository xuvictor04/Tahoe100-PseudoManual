---
symbol: "EPDR1"
type: "gene"
col: 1458
ensembl_id: "ENSG00000086289"
name: "ependymin related 1"
location: "7p14.1"
module: 72
arm: "+"
pooled_cpm: 25.41
n_lines_expressing: 36
n_dd_up: 24
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# EPDR1

*ependymin related 1* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.16× (z +16.4, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.412× (z -13.2, q 3e-37, down in 27 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.421× (z -12.9, q 9e-36, down in 31 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMA1]] (+0.69, fdr 1e-05), [[GNPDA2]] (+0.67, fdr 7e-06), [[TYW3]] (+0.66, fdr 7e-06); moves opposite to [[MNT]] (-0.57, fdr 2e-05), [[MIDN]] (-0.54, fdr 3e-05), [[TNRC6C]] (-0.53, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[DLX6-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1458.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **2.16×** | +16.4 | 0e+00 | 31/34 (PANC-1, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.17×** | +11.6 | 8e-29 | 30/34 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.16×** | +11.6 | 1e-28 | 30/34 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.14×** | +10.8 | 5e-25 | 28/34 (LoVo, H4, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.79×** | +8.7 | 3e-16 | 27/34 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +8.0 | 1e-13 | 16/25 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.68×** | +7.8 | 4e-13 | 27/34 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.6 | 1e-06 | 18/34 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +5.3 | 6e-06 | 19/34 (PANC-1, SW1417, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.39×** | +4.9 | 5e-05 | 21/34 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 15/34 (SW 900, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +4.5 | 3e-04 | 12/33 (A498, SW480, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.4 | 5e-04 | 13/33 (SW480, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.0 | 0.002 | 13/29 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.009 | 9/34 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +3.7 | 0.009 | 9/34 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.5 | 0.013 | 9/34 (COLO 205, AsPC-1, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.5 | 0.016 | 10/34 (RPMI-7951, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1458.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.412×** | -13.2 | 3e-37 | 27/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -12.9 | 9e-36 | 31/34 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -10.8 | 5e-25 | 28/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.512×** | -10.0 | 3e-21 | 27/34 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -9.4 | 9e-19 | 22/34 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.656×** | -8.9 | 6e-17 | 21/34 (NCI-H460, RPMI-7951, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.560×** | -8.6 | 4e-16 | 22/34 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.564×** | -8.5 | 1e-15 | 25/34 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -7.5 | 3e-12 | 22/34 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.695×** | -5.4 | 3e-06 | 17/34 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -5.4 | 4e-06 | 19/33 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.750×** | -4.3 | 9e-04 | 14/33 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.756×** | -4.2 | 0.001 | 17/34 (H4, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **0.791×** | -3.4 | 0.032 | 13/33 (CHP-212, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.655×** | -3.3 | 0.037 | 12/34 (HCT15, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.855× | -3.3 | 0.039 | 9/34 (PANC-1, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1458. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.2 | 1 | 10 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -21.1) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.210× (z -13.7) |
| [[LoVo (line)]] | wt | 17.9 | 4 | 3 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.66× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.207× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.268× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 51.0 | 2 | 4 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.79× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -11.7) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.342× (z -10.7) |
| [[SW480 (line)]] | alt | 59.5 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.280× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.301× (z -12.5) |
| [[HOP62 (line)]] | alt | 14.5 | 3 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.01× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.167× (z -11.3) |
| [[H4 (line)]] | wt | 69.3 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.57× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.0238× (z -26.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H2030 (line)]] | alt | 36.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.0) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.351× (z -8.8) |
| [[PANC-1 (line)]] | alt | 37.6 | 1 | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.36× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.388× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -9.8) |
| [[A-172 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 16.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0715× (z -18.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-427 (line)]] | wt | 25.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[A498 (line)]] | wt | 102 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.433× (z -9.8) |
| [[A549 (line)]] | wt | 40.2 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.19× (z +9.0) | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0993× (z -10.9) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.4) ⚠ cell-cycle shift, explains ~63% of this change |
| [[HepG2_C3A (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -11.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[J82 (line)]] | alt | 29.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.332× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 6.46 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0669× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -14.0) ⚠ cell-cycle shift, explains ~63% of this change |
| [[AN3 CA (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1458), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMA1]] | +0.69 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.67 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[TYW3]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[HSPA4L]] | +0.66 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[UBQLN1]] | +0.66 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[CASP6]] | +0.65 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[OSBPL1A]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[FECH]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[NIT2]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GPN1]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MRPL9]] | +0.60 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[SPR]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MNT]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[MIDN]] | -0.54 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.53 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[TOM1L2]] | -0.52 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[ING1]] | -0.51 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[PPFIA1]] | -0.50 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[INAFM1]] | -0.50 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[DCAF11]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[GPX4]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CRAMP1]] | -0.49 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[PPP1R14B]] | -0.49 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[GCAT]] | -0.49 | -0.43 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLX6-AS1]] | B | EPDR1 activity raises DLX6-AS1's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.43× lower at baseline in the lines without EPDR1 | 0.053 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |
| [[TMEM116]] | B | EPDR1 activity raises TMEM116's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.42× lower at baseline in the lines without EPDR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |
| [[CASP6]] | B | EPDR1 activity lowers CASP6's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.33× higher at baseline in the lines without EPDR1 | 0.086 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |
| [[SMARCAL1]] | B | EPDR1 activity raises SMARCAL1's level | lines that do not express EPDR1 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without EPDR1 | 0.088 | ⚠ within organs, on part of the lines; also absent: RBM24, BEX2, GATA3 |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, -7.9); signed map (-26.7, -22.4). **Vector** length 98.7, 24.9% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.7 | +16.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.7 | +11.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +10.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.6 | +11.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.1 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -10.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -10.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ependymin related 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:37,920,640-37,951,936 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MERP-1, MERP1, UCC1, EPDR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM22](https://www.uniprot.org/uniprotkb/Q9UM22) (Mammalian ependymin-related protein 1):

> Binds anionic lipids and gangliosides at acidic pH.

**Summary**, from NCBI Gene [54749](https://www.ncbi.nlm.nih.gov/gene/54749):

> The protein encoded by this gene is a type II transmembrane protein that is similar to two families of cell adhesion molecules, the protocadherins and ependymins. This protein may play a role in calcium-dependent cell adhesion. This protein is glycosylated, and the orthologous mouse protein is localized to the lysosome. Alternative splicing results in multiple transcript variants. A related pseudogene has been identified on chromosome 8. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17572) · Entrez [54749](https://www.ncbi.nlm.nih.gov/gene/54749) · UniProt [Q9UM22](https://www.uniprot.org/uniprotkb/Q9UM22) · Ensembl [ENSG00000086289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086289)

## Data

Gene col 1458: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1458); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1458, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1458]; `tensor/DDL_lfc|DDL_z.npy` [1458]; `embed/gene_vectors.npy` [1458]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1458 or target_col == 1458). Every well: [[EPDR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPDR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
