---
symbol: "VAX2"
type: "gene"
col: 3754
ensembl_id: "ENSG00000116035"
name: "ventral anterior homeobox 2"
location: "2p13.3"
module: 15
arm: "+"
pooled_cpm: 6.08
n_lines_expressing: 38
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# VAX2

*ventral anterior homeobox 2* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +17.9, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.600× (z -6.4, q 1e-07, down in 19 of 35 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 27 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF2]] (+0.58, fdr 8e-05), [[SETD1B]] (+0.57, fdr 4e-05), [[ATAD2B]] (+0.57, fdr 1e-04); moves opposite to [[EDA]] (-0.47, fdr 0.001, ⚠ not reproduced), [[RGL1]] (-0.46, fdr 2e-04), [[VEZT]] (-0.46, fdr 0.002, ⚠ one half only (not replicated)), [[NME7]] (-0.45, fdr 4e-04), [[PSMB1]] (-0.45, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PTPN18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +17.9 | 0e+00 | 30/32 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.16×** | +9.2 | 1e-17 | 22/33 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +7.0 | 6e-10 | 18/36 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.32×** | +4.8 | 2e-04 | 10/36 (HT-29, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.6 | 5e-04 | 13/35 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.43×** | +4.4 | 9e-04 | 10/36 (SW1417, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.010 | 9/34 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +3.7 | 0.012 | 4/35 (BT-474, HEC-1-A, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +3.7 | 0.012 | 8/35 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.33×** | +3.5 | 0.023 | 11/35 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.032 | 5/35 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.068 | 4/36 (SW480, BT-474, …) | inconsistent across doses | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.068 | 5/35 (Panc 03.27, RPMI-7951, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.095 | 4/35 (SW480, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.600×** | -6.4 | 1e-07 | 19/35 (HepG2/C3A, C32, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -5.6 | 8e-06 | 16/34 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -4.6 | 8e-04 | 15/35 (HT-29, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -4.2 | 0.003 | 13/31 (HOP62, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.526×** | -4.2 | 0.003 | 8/28 (LOX-IMVI, A549, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.712×** | -4.1 | 0.004 | 10/28 (NCI-H2030, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.756×** | -3.5 | 0.036 | 5/36 (A549, HOP62, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.738×** | -3.5 | 0.036 | 8/35 (A-172, SW 1271, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.764×** | -3.2 | 0.092 | 8/34 (SHP-77, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.784× | -3.0 | 0.12 | 4/36 (LOX-IMVI, Hs 766T, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.05 µM |  | 0.784× | -3.0 | 0.12 | 5/36 (HepG2/C3A, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 12.0 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0894× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.0728× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 15.3 | 2 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.49× (z +16.0) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 10.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[HOP62 (line)]] | alt | 7.32 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +10.1) | [[TAK-901 (drug)]] 5 µM 0.0263× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 11.9 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.175× (z -9.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 9.23 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -8.9) |
| [[C32 (line)]] | wt | 12.0 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.117× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 7.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +11.8) | — |
| [[Hs 766T (line)]] | wt | 4.57 | 0 | 1 | — | [[Darinaparsin (drug)]] 0.5 µM 0.0771× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 4.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.24× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 9.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0928× (z -8.7) |
| [[SW480 (line)]] | alt | 8.14 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.592 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.975 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF2]] | +0.58 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[SETD1B]] | +0.57 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[ATAD2B]] | +0.57 | +0.63 / +0.33 | both halves | 1e-04 |  |
| [[CRTC3]] | +0.55 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[CCNJ]] | +0.55 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[FBXW4]] | +0.53 | +0.54 / +0.26 | both halves | 4e-04 |  |
| [[MLYCD]] | +0.53 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[DHX35]] | +0.52 | +0.39 / +0.35 | both halves | 1e-04 |  |
| [[DHRS11]] | +0.51 | +0.33 / +0.44 | both halves | 1e-04 |  |
| [[PTGR3]] | +0.51 | +0.50 / +0.25 | both halves | 4e-04 |  |
| [[UBTF]] | +0.50 | +0.47 / +0.33 | both halves | 1e-04 |  |
| [[ARHGEF11]] | +0.50 | +0.51 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDA]] | -0.47 | -0.42 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[RGL1]] | -0.46 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[VEZT]] | -0.46 | -0.51 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[NME7]] | -0.45 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[PSMB1]] | -0.45 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[RADX]] | -0.44 | -0.36 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[SLC27A1]] | -0.43 | -0.43 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[MOCS2]] | -0.43 | -0.18 / -0.30 | ⚠ not reproduced | 9e-04 |  |
| [[CD99P1-1]] | -0.42 | -0.24 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[TBC1D17]] | -0.42 | -0.34 / -0.21 | both halves | 6e-04 |  |
| [[DHX40]] | -0.42 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[CYB5R1]] | -0.41 | -0.38 / -0.16 | ⚠ not reproduced | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VAX2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN18]] | B | VAX2 activity raises PTPN18's level | lines that do not express VAX2 (12) vs lines expressing it (38) | 1.09× lower at baseline in the lines without VAX2 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with RNF43; also absent: ZNF512B, WHAMMP2, HLTF |
| [[KCTD1]] | B | VAX2 activity lowers KCTD1's level | lines that do not express VAX2 (12) vs lines expressing it (38) | 1.01× higher at baseline in the lines without VAX2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with RNF43; also absent: ZNF512B, WHAMMP2, HLTF |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.5, 13.8); signed map (25.6, -23.5). **Vector** length 45.0, 5.93% of its response variance represented; |z| ≥ 3 in 767 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +17.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.5 | +4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.5 | -5.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +1.7 |

## What is on record

|  |  |
|---|---|
| Name | ventral anterior homeobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,900,576-70,965,373 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DRES93 |
| Gene groups (HGNC) | NKL subclass homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIW0](https://www.uniprot.org/uniprotkb/Q9UIW0) (Ventral anterior homeobox 2):

> Transcription factor that may function in dorsoventral specification of the forebrain. Regulates the expression of Wnt signaling antagonists including the expression of a truncated TCF7L2 isoform that cannot bind CTNNB1 and acts therefore as a potent dominant-negative Wnt antagonist. Plays a crucial role in eye development and, in particular, in the specification of the ventral optic vesicle (By similarity). May be a regulator of axial polarization in the retina.

**Summary**, from NCBI Gene [25806](https://www.ncbi.nlm.nih.gov/gene/25806):

> This gene encodes a homeobox protein and is almost exclusively expressed in the ventral portion of the retina during development. In mouse studies, this gene was found to be required for the correct formation of the optic fissure and other aspects of retinal development. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:12661](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12661) · Entrez [25806](https://www.ncbi.nlm.nih.gov/gene/25806) · UniProt [Q9UIW0](https://www.uniprot.org/uniprotkb/Q9UIW0) · Ensembl [ENSG00000116035](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116035)

## Data

Gene col 3754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3754); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3754]; `tensor/DDL_lfc|DDL_z.npy` [3754]; `embed/gene_vectors.npy` [3754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3754 or target_col == 3754). Every well: [[VAX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VAX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
