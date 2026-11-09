---
symbol: "PHC2-AS1"
type: "gene"
col: 13896
ensembl_id: "ENSG00000233246"
name: "PHC2 antisense RNA 1"
location: "1p35.1"
module: 15
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PHC2-AS1

*PHC2 antisense RNA 1* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.10× (z +27.3, q 0e+00, up in 32 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.352× (z -10.7, q 5e-24, down in 25 of 38 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.504× (z -7.3, q 5e-11, down in 20 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DARS1-AS1]] (+0.71, fdr 1e-05), [[SAP30L-AS1]] (+0.67, fdr 3e-05), [[CDNF]] (+0.67, fdr 1e-05); moves opposite to [[COMMD2]] (-0.61, fdr 5e-05), [[RPAP3]] (-0.60, fdr 1e-04), [[STAM2]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.10×** | +27.3 | 0e+00 | 32/33 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.03×** | +16.6 | 0e+00 | 22/26 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.28×** | +12.2 | 5e-32 | 27/33 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +6.3 | 3e-08 | 6/42 (SW480, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.2 | 5e-08 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.5 | 3e-06 | 1/12 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 3e-04 | 7/42 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +4.4 | 7e-04 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.44×** | +3.8 | 0.008 | 4/41 (AsPC-1, H4, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.024 | 6/37 (SHP-77, HT-29, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.13 | 0/42 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13896.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.352×** | -10.7 | 5e-24 | 25/38 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.506×** | -10.2 | 4e-22 | 23/33 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.504×** | -7.3 | 5e-11 | 20/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -7.2 | 7e-11 | 14/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.535×** | -6.7 | 3e-09 | 20/40 (PANC-1, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.538×** | -6.6 | 4e-09 | 18/43 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.580×** | -5.6 | 2e-06 | 13/18 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -5.5 | 3e-06 | 18/40 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.620×** | -5.1 | 2e-05 | 16/44 (PANC-1, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -4.5 | 3e-04 | 15/36 (NCI-H23, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.641×** | -4.5 | 4e-04 | 15/38 (PANC-1, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -4.1 | 0.002 | 15/40 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.691×** | -3.9 | 0.004 | 12/40 (PANC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.687×** | -3.8 | 0.005 | 9/41 (HepG2/C3A, J82, …) | top dose only | plate-row cell shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.009 | 7/42 (MIA PaCa-2, CFPAC-1, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.583×** | -3.0 | 0.089 | 7/38 (HS-578T, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cinacalcet (drug)]] 0.5 µM |  | **0.756×** | -3.0 | 0.089 | 11/37 (A-427, SHP-77, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | **0.821×** | -3.0 | 0.089 | 5/42 (RKO, H4, …) | rises with dose | position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.758×** | -2.9 | 0.089 | 3/42 (C32, SW1417, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.758×** | -2.9 | 0.089 | 6/44 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0553× (z -23.5) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0772× (z -14.4) |
| [[SK-MEL-2 (line)]] | alt | 7.54 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0501× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0914× (z -9.3) |
| [[HOP62 (line)]] | alt | 5.10 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 3.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.47× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 1.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +9.5) | — |
| [[J82 (line)]] | alt | 1.85 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -9.0) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.36 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0876× (z -8.7) |
| [[NCI-H2030 (line)]] | alt | 3.41 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -8.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -9.5) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW480 (line)]] | alt | 3.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.1) | — |
| [[A-172 (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DARS1-AS1]] | +0.71 | +0.64 / +0.55 | both halves | 1e-05 | same gene group |
| [[SAP30L-AS1]] | +0.67 | +0.62 / +0.44 | both halves | 3e-05 | same gene group |
| [[CDNF]] | +0.67 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PTGR3]] | +0.66 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GNG12-AS1]] | +0.65 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[LEMD3]] | +0.65 | +0.53 / +0.30 | both halves | 2e-04 |  |
| [[SIAH2-AS1]] | +0.64 | +0.44 / +0.51 | both halves | 3e-05 | same gene group |
| [[FKBP14-AS1]] | +0.64 | +0.49 / +0.50 | both halves | 1e-05 | same gene group |
| [[PNISR-AS1]] | +0.64 | +0.48 / +0.50 | both halves | 2e-05 | same gene group |
| [[ZNF460-AS1]] | +0.64 | +0.44 / +0.50 | both halves | 3e-05 | same gene group |
| [[POC1B-AS1]] | +0.63 | +0.39 / +0.56 | both halves | 5e-05 | same gene group |
| [[HSDL2-AS1]] | +0.63 | +0.46 / +0.48 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD2]] | -0.61 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RPAP3]] | -0.60 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[STAM2]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PIP4P1]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CYB5R1]] | -0.58 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[WDR7]] | -0.58 | -0.24 / -0.60 | both halves | 5e-04 |  |
| [[TUBB2B]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TTBK2]] | -0.57 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[RMC1]] | -0.57 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[MYH14]] | -0.57 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[NSFL1C]] | -0.56 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[FAM50A]] | -0.54 | -0.38 / -0.46 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PHC2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BDKRB2]] | B | BDKRB2 activity lowers PHC2-AS1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without BDKRB2 | 0.094 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[TOP2B]] | B | TOP2B activity lowers PHC2-AS1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PKIG]] | B | PKIG activity raises PHC2-AS1's level | lines that do not express PKIG (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without PKIG | 0.095 | ⚠ within organs, on part of the lines; also absent: GPR155, TTC7B, CIBAR1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.4, 20.5); signed map (18.0, -5.0). **Vector** length 62.7, 9.58% of its response variance represented; |z| ≥ 3 in 1,123 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +27.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +16.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +12.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.3 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.0 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.2 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -10.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.9 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.4 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.1 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | PHC2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p35.1 — chr1:33,350,352-33,363,245 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40205) · Entrez [101929464](https://www.ncbi.nlm.nih.gov/gene/101929464) · Ensembl [ENSG00000233246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233246)

## Data

Gene col 13896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13896); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13896]; `tensor/DDL_lfc|DDL_z.npy` [13896]; `embed/gene_vectors.npy` [13896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13896 or target_col == 13896). Every well: [[PHC2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PHC2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
