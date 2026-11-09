---
symbol: "MYH15"
type: "gene"
col: 6933
ensembl_id: "ENSG00000144821"
name: "myosin heavy chain 15"
location: "3q13.13"
module: 39
arm: "+"
pooled_cpm: 8.13
n_lines_expressing: 40
n_dd_up: 22
n_dd_down: 15
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MYH15

*myosin heavy chain 15* — 3q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.67× (z +19.6, q 0e+00, up in 29 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.560× (z -5.2, q 9e-05, down in 19 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.77, fdr 7e-06), [[SSUH2]] (+0.75, fdr 7e-06), [[MYLK2]] (+0.74, fdr 7e-06); moves opposite to [[ARNT]] (-0.62, fdr 1e-05), [[CCZ1B]] (-0.61, fdr 1e-05), [[FLYWCH2]] (-0.61, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[FAM76A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.67×** | +19.6 | 0e+00 | 29/32 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.99×** | +17.6 | 0e+00 | 24/33 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +12.5 | 1e-33 | 22/32 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.24×** | +10.6 | 7e-24 | 26/36 (HOP62, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.97×** | +9.8 | 2e-20 | 23/32 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +9.7 | 2e-20 | 25/33 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.90×** | +8.1 | 3e-14 | 21/37 (NCI-H2347, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.51×** | +8.0 | 1e-13 | 5/11 (A-427, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.53×** | +7.7 | 9e-13 | 8/13 (A-427, NCI-H2030, …) | all doses, flat | composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.99×** | +6.2 | 4e-08 | 22/37 (A498, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +5.8 | 4e-07 | 19/36 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.88×** | +5.6 | 8e-07 | 20/37 (PANC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.75×** | +5.0 | 2e-05 | 10/19 (A-427, AsPC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.72×** | +4.8 | 5e-05 | 12/37 (A498, RKO, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.8 | 5e-05 | 14/36 (SW1417, AsPC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +4.3 | 6e-04 | 13/36 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.64×** | +4.2 | 9e-04 | 11/35 (A-427, A498, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **2.02×** | +3.3 | 0.025 | 6/31 (AsPC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.97×** | +3.2 | 0.036 | 7/33 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.560×** | -5.2 | 9e-05 | 19/37 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.589×** | -4.8 | 5e-04 | 18/36 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.630×** | -4.2 | 0.005 | 16/36 (H4, A498, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.659×** | -3.8 | 0.020 | 9/37 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.661×** | -3.8 | 0.020 | 16/33 (LS 180, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.669×** | -3.6 | 0.026 | 9/37 (A-427, PANC-1, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | **0.760×** | -3.5 | 0.031 | 13/36 (SK-MEL-2, LoVo, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.475×** | -3.5 | 0.031 | 11/29 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.682×** | -3.3 | 0.052 | 15/36 (PANC-1, A-427, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.613×** | -3.2 | 0.088 | 5/38 (A498, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.093 | 3/37 (J82, A-427, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.788×** | -3.1 | 0.093 | 6/37 (AN3 CA, A498, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.093 | 14/36 (A-427, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.717×** | -3.0 | 0.098 | 13/37 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **0.791×** | -3.0 | 0.098 | 7/36 (A498, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 44.3 | 4 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.23× (z +10.4) | — |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0388× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.151× (z -8.6) |
| [[RKO (line)]] | wt | 14.5 | 0 | 3 | — | [[Ligustrazine (drug)]] 5 µM 0.0679× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.0367× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Radotinib (drug)]] 5 µM 0.211× (z -9.2) |
| [[C-33 A (line)]] | alt | 22.6 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0659× (z -10.1) |
| [[LoVo (line)]] | wt | 5.12 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +12.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0678× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 5.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 5.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 2.78 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.45× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 4.80 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0682× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 7.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.49× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.200× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 3.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.90× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 2.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 5.78 | 0 | 1 | — | [[Gallic acid (drug)]] 0.05 µM 0.0576× (z -8.5) |
| [[A-172 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.77 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[MYLK2]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.74 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[MMP25]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[NEK10]] | +0.71 | +0.74 / +0.60 | both halves | 7e-06 |  |
| [[TRIM59]] | +0.70 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[CHADL]] | +0.70 | +0.75 / +0.61 | both halves | 7e-06 |  |
| [[LINC01204]] | +0.68 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CYREN]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[DPYS]] | +0.67 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[PHEX]] | +0.66 | +0.75 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARNT]] | -0.62 | -0.70 / -0.50 | both halves | 1e-05 |  |
| [[CCZ1B]] | -0.61 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[FLYWCH2]] | -0.61 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC24]] | -0.61 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[CRYZL1]] | -0.60 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[PRUNE1]] | -0.60 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[LAMTOR2]] | -0.59 | -0.62 / -0.38 | both halves | 7e-05 |  |
| [[NCK1]] | -0.59 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[CCZ1]] | -0.57 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[DPY30]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[MALSU1]] | -0.57 | -0.63 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYH15's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM76A]] | B | MYH15 activity lowers FAM76A's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.30× higher at baseline in the lines without MYH15 | 0.020 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IDI2-AS1]] | B | MYH15 activity raises IDI2-AS1's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without MYH15 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GPATCH2L]] | B | MYH15 activity raises GPATCH2L's level | lines that do not express MYH15 (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without MYH15 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -11.4); signed map (19.8, 8.9). **Vector** length 86.9, 18.5% of its response variance represented; |z| ≥ 3 in 1,091 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +19.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +17.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +4.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +4.2 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | myosin heavy chain 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.13 — chr3:108,380,368-108,529,322 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1000 |
| Gene groups (HGNC) | Myosin heavy chains, class II |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2K3](https://www.uniprot.org/uniprotkb/Q9Y2K3) (Myosin-15):

> Muscle contraction.

**Summary**, from NCBI Gene [22989](https://www.ncbi.nlm.nih.gov/gene/22989):

> Predicted to enable actin filament binding activity and microfilament motor activity. Predicted to be involved in extraocular skeletal muscle development. Predicted to be located in myofibril. Predicted to be part of myosin II complex. Predicted to be active in cytoplasm and myosin filament. Implicated in stroke. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31073) · Entrez [22989](https://www.ncbi.nlm.nih.gov/gene/22989) · UniProt [Q9Y2K3](https://www.uniprot.org/uniprotkb/Q9Y2K3) · Ensembl [ENSG00000144821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144821)

## Data

Gene col 6933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6933); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6933]; `tensor/DDL_lfc|DDL_z.npy` [6933]; `embed/gene_vectors.npy` [6933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6933 or target_col == 6933). Every well: [[MYH15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYH15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
