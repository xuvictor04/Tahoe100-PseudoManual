---
symbol: "RHBDL3"
type: "gene"
col: 6502
ensembl_id: "ENSG00000141314"
name: "rhomboid like 3"
location: "17q11.2"
module: 102
arm: "+"
pooled_cpm: 3.77
n_lines_expressing: 41
n_dd_up: 39
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 11
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# RHBDL3

*rhomboid like 3* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (20 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.65× (z +20.8, q 0e+00, up in 24 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.228×, A-427 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.135×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.115×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.117×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH23]] (+0.69, fdr 7e-06), [[CACNA2D2]] (+0.64, fdr 7e-06), [[EBF4]] (+0.58, fdr 2e-05); moves opposite to [[PTCD2]] (-0.49, fdr 4e-04), [[GALK2]] (-0.46, fdr 1e-04), [[ELP3]] (-0.45, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 11 go from it, the strongest it → [[PTCD2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +20.8 | 0e+00 | 24/27 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +17.2 | 0e+00 | 28/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.91×** | +14.7 | 0e+00 | 2/4 (HS-578T, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.44×** | +14.0 | 2e-42 | 26/36 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **3.25×** | +13.4 | 1e-38 | 27/37 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +12.7 | 4e-35 | 16/27 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.90×** | +12.1 | 1e-31 | 21/35 (PANC-1, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.87×** | +11.9 | 5e-31 | 21/29 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.75×** | +11.5 | 1e-28 | 21/34 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.72×** | +11.3 | 6e-28 | 6/15 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +10.9 | 4e-26 | 4/5 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.04×** | +7.6 | 1e-12 | 13/25 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.95×** | +7.5 | 2e-12 | 13/25 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **2.00×** | +7.4 | 4e-12 | 8/15 (LoVo, SW480, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.82×** | +6.7 | 6e-10 | 16/35 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.76×** | +6.0 | 6e-08 | 13/32 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +5.8 | 2e-07 | 12/32 (HOP62, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.4 | 2e-06 | 9/35 (J82, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +4.4 | 3e-04 | 13/33 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.4 | 3e-04 | 9/31 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.30×** | +4.1 | 8e-04 | 7/35 (J82, MIA PaCa-2, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.002 | 2/27 (SHP-77, SW1417) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.6 | 0.006 | 7/33 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.012 | 2/36 (SW480, HCT15) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6502.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.228×, A-427 0.278×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.135×); [[Harringtonine (drug)]] 0.5 µM in 1 line (A-172 0.115×; ⚠ cell-cycle shift, explains ~18% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-172 0.117×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.573× | -3.3 | 0.25 | 11/32 (A-427, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | 0.820× | -3.2 | 0.25 | 3/34 (AN3 CA, COLO 205, …) | top dose only |  |
| [[Pentagastrin (drug)]] 5 µM |  | 0.825× | -3.1 | 0.25 | 2/39 (SW 1271, Panc 03.27) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.763× | -3.1 | 0.25 | 12/36 (A-172, A-427, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 0.05 µM |  | 0.767× | -3.1 | 0.25 | 5/30 (A498, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.71 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 3.25 | 6 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 16.1× (z +10.9) | [[Docetaxel (drug)]] 0.05 µM 0.0941× (z -9.9) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.6 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.115× (z -10.8) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.117× (z -10.7) |
| [[A-427 (line)]] | wt | 21.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -12.9) |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.163× (z -10.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.107× (z -8.5) |
| [[A549 (line)]] | wt | 5.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.0× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 4.02 | 0 | 1 | — | [[Mifepristone (drug)]] 0.05 µM 0.0824× (z -8.9) |
| [[HOP62 (line)]] | alt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.69× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.51 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0592× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 2.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +12.4) | — |
| [[SW480 (line)]] | alt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +8.5) | — |
| [[A498 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.942 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.987 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH23]] | +0.69 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[CACNA2D2]] | +0.64 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[EBF4]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[KCNG3]] | +0.58 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[LINC00937]] | +0.57 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[WIPF3]] | +0.57 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[TLE2]] | +0.57 | +0.40 / +0.61 | both halves | 5e-05 |  |
| [[NTN1]] | +0.57 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[GRID1]] | +0.56 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MED12L]] | +0.55 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.54 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[PLD5]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD2]] | -0.49 | -0.25 / -0.41 | both halves | 4e-04 |  |
| [[GALK2]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[ELP3]] | -0.45 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[ERMARD]] | -0.43 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises RHBDL3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 2.10× lower at baseline in the lines without MSI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[LRRC4B]] | B | LRRC4B activity raises RHBDL3's level | lines that do not express LRRC4B (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without LRRC4B | 0.009 | ⚠ within organs, on part of the lines; also absent: CHRNA7, PDZD4, GNG4; maybe low, not absent |
| [[PAX2]] | B | PAX2 activity raises RHBDL3's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without PAX2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[TOP2A]] | B | TOP2A activity lowers RHBDL3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[EBF4]] | B | EBF4 activity raises RHBDL3's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 1.71× lower at baseline in the lines without EBF4 | 0.010 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[NTN1]] | B | NTN1 activity raises RHBDL3's level | lines that do not express NTN1 (17) vs lines expressing it (33) | 2.29× lower at baseline in the lines without NTN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC00466, MCOLN3, ZMAT1; maybe low, not absent |
| [[CECR2]] | B | CECR2 activity raises RHBDL3's level | lines that do not express CECR2 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without CECR2 | 0.021 | ⚠ within organs, on part of the lines; also absent: LHX2, NPTX1, PDZD4; maybe low, not absent |
| [[MED12L]] | B | MED12L activity raises RHBDL3's level | lines that do not express MED12L (18) vs lines expressing it (32) | 1.88× lower at baseline in the lines without MED12L | 0.044 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2 |
| [[OLFM2]] | B | OLFM2 activity raises RHBDL3's level | lines that do not express OLFM2 (14) vs lines expressing it (36) | 1.93× lower at baseline in the lines without OLFM2 | 0.068 | ⚠ within organs, on part of the lines; also absent: MGAT5B, JAM3, ANKS1B; maybe low, not absent |
| [[RASGEF1C]] | B | RASGEF1C activity raises RHBDL3's level | lines that do not express RASGEF1C (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without RASGEF1C | 0.071 | ⚠ within organs, on part of the lines; also absent: FAM124A, RAB6B, STOX2; maybe low, not absent |
| [[SCD5]] | B | SCD5 activity raises RHBDL3's level | lines that do not express SCD5 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without SCD5 | 0.074 | ⚠ within organs, on part of the lines; also absent: TCF7L1, FOXD1, KLF9 |
| [[TMEM150C]] | B | TMEM150C activity strengthens RHBDL3's drug response | lines that do not express TMEM150C (7) vs lines expressing it (31) | the lines without TMEM150C respond 0.74× as strongly (z diff +1.04); strongest at Tucidinostat 5 µM: 1.42x vs 3.39x (z diff +3.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTCD2]] | B | RHBDL3 activity raises PTCD2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without RHBDL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[DONSON]] | B | RHBDL3 activity raises DONSON's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.47× lower at baseline in the lines without RHBDL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[SDK2]] | B | RHBDL3 activity raises SDK2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without RHBDL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[CCDC136]] | B | RHBDL3 activity raises CCDC136's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.05× lower at baseline in the lines without RHBDL3 | 0.047 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[NTN1]] | B | RHBDL3 activity raises NTN1's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.13× lower at baseline in the lines without RHBDL3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[MED12L]] | B | RHBDL3 activity raises MED12L's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 3.77× lower at baseline in the lines without RHBDL3 | 0.071 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[TLE2]] | B | RHBDL3 activity raises TLE2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.04× lower at baseline in the lines without RHBDL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[LRRC4B]] | B | RHBDL3 activity raises LRRC4B's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without RHBDL3 | 0.085 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[ZBTB46]] | B | RHBDL3 activity raises ZBTB46's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.92× lower at baseline in the lines without RHBDL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[MYO1F]] | B | RHBDL3 activity raises MYO1F's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.30× lower at baseline in the lines without RHBDL3 | 0.093 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[NKAIN1]] | B | RHBDL3 activity raises NKAIN1's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 1.78× lower at baseline in the lines without RHBDL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.667). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 37.1); signed map (27.8, 24.6). **Vector** length 61.4, 10.5% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +17.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +20.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.7 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.6 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -1.9 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -1.3 | +3.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | +3.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | rhomboid like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:32,265,832-32,324,659 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VRHO; previously RHBDL4 |
| Gene groups (HGNC) | EF-hand domain containing; Rhomboid family |
| Matched by | ensembl_id |

**Function**, from UniProt [P58872](https://www.uniprot.org/uniprotkb/P58872) (Rhomboid-related protein 3):

> May be involved in regulated intramembrane proteolysis and the subsequent release of functional polypeptides from their membrane anchors.

**Summary**, from NCBI Gene [162494](https://www.ncbi.nlm.nih.gov/gene/162494):

> Predicted to enable serine-type endopeptidase activity. Predicted to be involved in proteolysis. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16502](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16502) · Entrez [162494](https://www.ncbi.nlm.nih.gov/gene/162494) · UniProt [P58872](https://www.uniprot.org/uniprotkb/P58872) · Ensembl [ENSG00000141314](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141314)

## Data

Gene col 6502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6502); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6502]; `tensor/DDL_lfc|DDL_z.npy` [6502]; `embed/gene_vectors.npy` [6502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6502 or target_col == 6502). Every well: [[RHBDL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RHBDL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
