---
symbol: "NR2F2-AS1"
type: "gene"
col: 14506
ensembl_id: "ENSG00000247809"
name: "NR2F2 antisense RNA 1"
location: "15q26.2"
module: 144
arm: "+"
pooled_cpm: 96.88
n_lines_expressing: 42
n_dd_up: 21
n_dd_down: 64
n_dd_up_clean: 20
n_dd_down_clean: 40
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# NR2F2-AS1

*NR2F2 antisense RNA 1* — 15q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.83× (z +7.0, q 2e-09, up in 32 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (24 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.185× (z -28.9, q 0e+00, down in 39 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MEF2C-AS1]] (+0.63, fdr 1e-05), [[C4orf47]] (+0.59, fdr 9e-06), [[NR2F2]] (+0.58, fdr 1e-05, ⚠ same locus), [[TMEM45A]] (+0.57, fdr 1e-05); moves opposite to [[CRACD]] (-0.50, fdr 3e-05), [[JMJD7]] (-0.49, fdr 3e-05), [[PTPN3]] (-0.48, fdr 5e-05).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ADAMTS9-AS2]] → it (grade B ⚠); 8 go from it, the strongest it → [[FUT11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14506.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.83×** | +7.0 | 2e-09 | 32/39 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.59×** | +5.6 | 5e-06 | 30/40 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.56×** | +5.4 | 1e-05 | 28/40 (LoVo, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 8e-05 | 30/39 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.42×** | +4.1 | 0.005 | 19/40 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.012 | 17/40 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.026 | 26/41 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.029 | 16/40 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.035 | 20/41 (NCI-H1792, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.035 | 23/40 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.035 | 16/40 (A549, RPMI-7951, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 16/40 (RPMI-7951, hTERT-HPNE, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.035 | 17/40 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.036 | 17/41 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.036 | 19/41 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 66 in all, 24 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14506.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.185×** | -28.9 | 0e+00 | 39/40 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.186×** | -20.3 | 0e+00 | 40/40 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.194×** | -19.8 | 0e+00 | 37/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.196×** | -18.7 | 0e+00 | 40/40 (H4, A549, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.222×** | -18.2 | 0e+00 | 39/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.235×** | -17.5 | 0e+00 | 40/40 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.238×** | -17.4 | 0e+00 | 40/40 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.247×** | -16.9 | 0e+00 | 38/40 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.259×** | -16.3 | 0e+00 | 40/40 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.270×** | -15.8 | 0e+00 | 40/40 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.265×** | -15.2 | 0e+00 | 37/39 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.298×** | -14.6 | 0e+00 | 37/40 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.311×** | -14.1 | 2e-43 | 37/40 (PANC-1, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.381×** | -10.9 | 4e-26 | 34/41 (HCT15, HOP62, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.421×** | -9.9 | 2e-21 | 27/36 (C32, HOP62, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.427×** | -9.7 | 1e-20 | 37/40 (HCT15, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.578×** | -9.3 | 4e-19 | 32/40 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.473×** | -8.7 | 7e-17 | 34/40 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.493×** | -8.0 | 4e-14 | 27/40 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -7.6 | 8e-13 | 36/41 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.534×** | -7.3 | 6e-12 | 29/39 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.323×** | -7.1 | 2e-11 | 34/40 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.75 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14506. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 177 | 0 | 25 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0734× (z -27.6) |
| [[H4 (line)]] | wt | 168 | 0 | 25 (11 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0161× (z -27.1) |
| [[HOP62 (line)]] | alt | 337 | 0 | 22 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -25.3) |
| [[HEC-1-A (line)]] | alt | 345 | 0 | 21 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -29.0) |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 20 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0521× (z -37.0) |
| [[SNU-423 (line)]] | alt | 217 | 0 | 19 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -27.1) |
| [[CFPAC-1 (line)]] | alt | 195 | 0 | 18 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0773× (z -27.5) |
| [[HCT15 (line)]] | alt | 337 | 0 | 18 (9 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0642× (z -21.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.126× (z -16.9) |
| [[J82 (line)]] | alt | 103 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -22.7) |
| [[NCI-H460 (line)]] | wt | 53.0 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -17.4) |
| [[PANC-1 (line)]] | alt | 90.9 | 0 | 18 (7 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0820× (z -24.3) |
| [[RPMI-7951 (line)]] | alt | 242 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -24.4) |
| [[NCI-H23 (line)]] | alt | 106 | 2 (1 ⚠) | 14 (7 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +12.4) ⚠ position not correctable · without an alert: [[Cobimetinib (drug)]] 5 µM 3.28× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -25.0) |
| [[A-427 (line)]] | wt | 92.8 | 0 | 15 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 15 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -23.5) |
| [[A549 (line)]] | wt | 93.7 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0713× (z -26.5) |
| [[HT-29 (line)]] | alt | 78.8 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -17.6) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 14 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.121× (z -16.2) |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.3) |
| [[hTERT-HPNE (line)]] | wt | 193 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -22.0) |
| [[A-172 (line)]] | wt | 139 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -26.3) |
| [[Hs 766T (line)]] | wt | 37.7 | 0 | 10 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -10.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -10.3) |
| [[SW 900 (line)]] | alt | 60.9 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.1) |
| [[LoVo (line)]] | wt | 33.9 | 5 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +12.9) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 4.67× (z +10.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 69.7 | 1 (1 ⚠) | 7 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.53× (z +11.2) ⚠ position not correctable | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 56.1 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -17.5) |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 8 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -13.2) |
| [[CHP-212 (line)]] | wt | 124 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -12.5) |
| [[HS-578T (line)]] | alt | 83.4 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -18.8) |
| [[SW 1271 (line)]] | alt | 131 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0207× (z -15.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0375× (z -13.5) |
| [[A498 (line)]] | wt | 57.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -18.2) |
| [[NCI-H2030 (line)]] | alt | 63.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -12.4) |
| [[SW 1088 (line)]] | alt | 187 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0303× (z -18.4) |
| [[SW480 (line)]] | alt | 24.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.8) |
| [[AN3 CA (line)]] | alt | 70.8 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 44.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.8) |
| [[BT-474 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +9.0) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[AsPC-1 (line)]] | alt | 22.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14506), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MEF2C-AS1]] | +0.63 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[C4orf47]] | +0.59 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[NR2F2]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TMEM45A]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ZNF439]] | +0.54 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[LRRC7]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[MAGI2]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ZNF292]] | +0.51 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[SLC8A1]] | +0.51 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[LINC01013]] | +0.51 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[NOL3]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[NREP]] | +0.50 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[SMAD9]] | +0.50 | +0.46 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACD]] | -0.50 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[JMJD7]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PTPN3]] | -0.48 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[MFSD6]] | -0.47 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[CDYL]] | -0.46 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ADAMTSL5]] | -0.46 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[FERMT1]] | -0.46 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[TMCO6]] | -0.45 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[KLHL2]] | -0.45 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MTAP]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[BLACAT1]] | -0.44 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[TMEM181]] | -0.44 | -0.54 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS9-AS2]] | B | ADAMTS9-AS2 activity raises NR2F2-AS1's level | lines that do not express ADAMTS9-AS2 (30) vs lines expressing it (20) | 2.98× lower at baseline in the lines without ADAMTS9-AS2 | 0.019 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ENSG00000233539, NID2 |
| [[JAM2]] | B | JAM2 activity raises NR2F2-AS1's level | lines that do not express JAM2 (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without JAM2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ITGA4, RORB, IL7R |
| [[DNAH11]] | B | DNAH11 activity raises NR2F2-AS1's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.82× lower at baseline in the lines without DNAH11 | 0.031 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[MAGI2]] | B | MAGI2 activity raises NR2F2-AS1's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 2.68× lower at baseline in the lines without MAGI2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1 |
| [[OR9Q1]] | B | OR9Q1 activity raises NR2F2-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 2.89× lower at baseline in the lines without OR9Q1 | 0.050 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[MAP2K1]] | B | MAP2K1 activity lowers NR2F2-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[SLC8A1]] | B | SLC8A1 activity raises NR2F2-AS1's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without SLC8A1 | 0.088 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |
| [[RUNX3]] | B | RUNX3 activity raises NR2F2-AS1's level | lines that do not express RUNX3 (29) vs lines expressing it (21) | 2.14× lower at baseline in the lines without RUNX3 | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC6A15, IGF2BP1, ENSG00000286385 |
| [[C4orf47]] | C | C4orf47 activity raises NR2F2-AS1's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 5.09× lower at baseline in the lines without C4orf47 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FUT11]] | B | NR2F2-AS1 activity raises FUT11's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without NR2F2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[C4orf47]] | B | NR2F2-AS1 activity raises C4orf47's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.90× lower at baseline in the lines without NR2F2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[TMEM181]] | B | NR2F2-AS1 activity lowers TMEM181's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.83× higher at baseline in the lines without NR2F2-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[NR2F2]] | B | NR2F2-AS1 activity raises NR2F2's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without NR2F2-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[CCDC18-AS1]] | B | NR2F2-AS1 activity raises CCDC18-AS1's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without NR2F2-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[LMLN]] | B | NR2F2-AS1 activity raises LMLN's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 2.08× lower at baseline in the lines without NR2F2-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[DPY19L2P2]] | B | NR2F2-AS1 activity raises DPY19L2P2's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.99× lower at baseline in the lines without NR2F2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[GOLGA8N]] | B | NR2F2-AS1 activity raises GOLGA8N's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without NR2F2-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.1, 29.6); signed map (-32.3, 31.2). **Vector** length 92.6, 36.2% of its response variance represented; |z| ≥ 3 in 1,812 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +4.3 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +1.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.7 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -4.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.2 | -9.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | -5.5 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | -4.2 | -9.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.2 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | NR2F2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.2 — chr15:96,110,040-96,327,361 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44222) · Entrez [644192](https://www.ncbi.nlm.nih.gov/gene/644192) · Ensembl [ENSG00000247809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247809)

## Data

Gene col 14506: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14506); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14506, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14506]; `tensor/DDL_lfc|DDL_z.npy` [14506]; `embed/gene_vectors.npy` [14506]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14506 or target_col == 14506). Every well: [[NR2F2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2F2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
