---
symbol: "MYL9"
type: "gene"
col: 2116
ensembl_id: "ENSG00000101335"
name: "myosin light chain 9"
location: "20q11.23"
module: 66
arm: "+"
pooled_cpm: 13.58
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 14
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 17
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# MYL9

*myosin light chain 9* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.12× (z +20.0, q 0e+00, up in 20 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.77× (z +8.9, q 9e-17, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.580× (z -6.1, q 8e-07, down in 17 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXRA8]] (+0.73, fdr 7e-06), [[NME4]] (+0.65, fdr 1e-05), [[POSTN]] (+0.62, fdr 1e-05); moves opposite to [[PWP2]] (-0.47, fdr 1e-04), [[FBXO45]] (-0.47, fdr 2e-04), [[NUDT22]] (-0.45, fdr 9e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MXRA8]] → it (grade B ⚠); 17 go from it, the strongest it → [[LAMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.12×** | +20.0 | 0e+00 | 20/21 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.24×** | +19.5 | 0e+00 | 15/16 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.35×** | +15.0 | 0e+00 | 16/19 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +8.9 | 9e-17 | 17/26 (RKO, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.4 | 9e-06 | 9/25 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.5 | 6e-04 | 11/24 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 8e-04 | 15/25 (RKO, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 9e-04 | 12/26 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.48×** | +4.3 | 9e-04 | 12/26 (SW480, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 9e-04 | 14/25 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +4.2 | 0.001 | 5/16 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +4.2 | 0.001 | 8/24 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.005 | 12/24 (RKO, A-172, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.5 | 0.016 | 8/22 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.021 | 8/22 (CFPAC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.021 | 7/25 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.021 | 9/24 (A-172, HS-578T, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.075 | 4/26 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.082 | 5/26 (RKO, SW480, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +2.9 | 0.082 | 11/25 (SW480, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +2.9 | 0.094 | 10/26 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -6.1 | 8e-07 | 17/25 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.630×** | -5.1 | 8e-05 | 9/25 (SNU-1, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.659×** | -4.6 | 5e-04 | 14/25 (RPMI-7951, J82, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.662×** | -4.6 | 5e-04 | 13/25 (SNU-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.662×** | -4.6 | 5e-04 | 12/24 (SNU-1, RKO, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.662×** | -4.4 | 8e-04 | 13/24 (SNU-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -4.4 | 8e-04 | 11/25 (HepG2/C3A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.002 | 15/24 (HepG2/C3A, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[BAY1125976 (drug)]] 5 µM |  | **0.505×** | -4.0 | 0.005 | 7/26 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.717×** | -3.7 | 0.012 | 8/25 (HepG2/C3A, SW480, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.551×** | -3.5 | 0.028 | 7/26 (HS-578T, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.655×** | -3.2 | 0.063 | 1/26 (A-427) | two highest doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.760×** | -3.1 | 0.095 | 9/24 (Hs 766T, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 122 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.23× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 34.9 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.51× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.3) |
| [[A498 (line)]] | wt | 31.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.45× (z +15.8) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 22.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.95× (z +11.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 18.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +10.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 10.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.32× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.8) |
| [[PANC-1 (line)]] | alt | 15.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.08× (z +12.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 74.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 84.0 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.279× (z -13.1) |
| [[SNU-423 (line)]] | alt | 12.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.6× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 9.29 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.12× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +8.7) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 5.04 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0781× (z -8.5) |
| [[RKO (line)]] | wt | 16.1 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.66× (z +9.0) | — |
| [[A549 (line)]] | wt | 0.924 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.864 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.950 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 89.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXRA8]] | +0.73 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NME4]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[POSTN]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[OLFML2A]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[EFEMP1]] | +0.55 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[COL3A1]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 408 |
| [[MATN3]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[SUSD5]] | +0.53 | +0.31 / +0.63 | both halves | 2e-04 |  |
| [[ANAPC15]] | +0.53 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[LUM]] | +0.53 | +0.40 / +0.48 | both halves | 4e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[MMP2]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION |
| [[FSTL1]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PWP2]] | -0.47 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[FBXO45]] | -0.47 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[NUDT22]] | -0.45 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[GAN]] | -0.45 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ZNF415]] | -0.43 | -0.46 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MXRA8]] | B | MXRA8 activity raises MYL9's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.44× lower at baseline in the lines without MXRA8 | 0.022 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[MRAS]] | B | MRAS activity raises MYL9's level | lines that do not express MRAS (11) vs lines expressing it (39) | 2.36× lower at baseline in the lines without MRAS | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[COL3A1]] | B | COL3A1 activity raises MYL9's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.15× lower at baseline in the lines without COL3A1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[KLHL5]] | B | KLHL5 activity raises MYL9's level | lines that do not express KLHL5 (7) vs lines expressing it (43) | 2.25× lower at baseline in the lines without KLHL5 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: SLC36A4, CCDC3, CSRP2 |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 17, C 0. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB2]] | B | MYL9 activity raises LAMB2's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.68× lower at baseline in the lines without MYL9 | 0.004 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[MRAS]] | B | MYL9 activity raises MRAS's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.71× lower at baseline in the lines without MYL9 | 0.020 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CNN3]] | B | MYL9 activity raises CNN3's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without MYL9 | 0.026 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[TMEM14C]] | B | MYL9 activity raises TMEM14C's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.41× lower at baseline in the lines without MYL9 | 0.027 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[PRCP]] | B | MYL9 activity raises PRCP's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without MYL9 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[AGPAT1]] | B | MYL9 activity raises AGPAT1's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.39× lower at baseline in the lines without MYL9 | 0.039 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CFL2]] | B | MYL9 activity raises CFL2's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.82× lower at baseline in the lines without MYL9 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[MATN3]] | B | MYL9 activity raises MATN3's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without MYL9 | 0.045 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[COL1A1]] | B | MYL9 activity raises COL1A1's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without MYL9 | 0.049 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[ZNF428]] | B | MYL9 activity raises ZNF428's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.11× lower at baseline in the lines without MYL9 | 0.052 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CCDC50]] | B | MYL9 activity raises CCDC50's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without MYL9 | 0.069 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[CRTAP]] | B | MYL9 activity raises CRTAP's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.51× lower at baseline in the lines without MYL9 | 0.071 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.6, 23.0); signed map (45.6, -9.8). **Vector** length 65.9, 17.5% of its response variance represented; |z| ≥ 3 in 531 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +19.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +20.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.7 | +8.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.3 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.6 | -4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,541,497-36,551,447 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYRL2, MLC2, LC20, MRLC1 |
| Gene groups (HGNC) | Myosin light chains, class 2 |
| Hallmark sets | APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 18 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P24844](https://www.uniprot.org/uniprotkb/P24844) (Myosin regulatory light polypeptide 9):

> Myosin regulatory subunit that plays an important role in regulation of both smooth muscle and nonmuscle cell contractile activity via its phosphorylation. Implicated in cytokinesis, receptor capping, and cell locomotion. In myoblasts, may regulate PIEZO1-dependent cortical actomyosin assembly involved in myotube formation (By similarity).

**Summary**, from NCBI Gene [10398](https://www.ncbi.nlm.nih.gov/gene/10398):

> Myosin, a structural component of muscle, consists of two heavy chains and four light chains. The protein encoded by this gene is a myosin light chain that may regulate muscle contraction by modulating the ATPase activity of myosin heads. The encoded protein binds calcium and is activated by myosin light chain kinase. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:15754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15754) · Entrez [10398](https://www.ncbi.nlm.nih.gov/gene/10398) · UniProt [P24844](https://www.uniprot.org/uniprotkb/P24844) · Ensembl [ENSG00000101335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101335)

## Data

Gene col 2116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2116); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2116]; `tensor/DDL_lfc|DDL_z.npy` [2116]; `embed/gene_vectors.npy` [2116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2116 or target_col == 2116). Every well: [[MYL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
