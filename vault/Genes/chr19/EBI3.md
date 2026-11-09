---
symbol: "EBI3"
type: "gene"
col: 2569
ensembl_id: "ENSG00000105246"
name: "Epstein-Barr virus induced 3"
location: "19p13.3"
module: 14
arm: "+"
pooled_cpm: 3.24
n_lines_expressing: 38
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# EBI3

*Epstein-Barr virus induced 3* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 23.3× (z +33.8, q 0e+00, up in 27 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.581× (z -4.1, q 0.024, down in 7 of 30 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 2 lines (A549 0.0507×, NCI-H23 0.0829×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF3]] (+0.78, fdr 7e-06), [[CCL20]] (+0.72, fdr 7e-06), [[S100A3]] (+0.69, fdr 1e-05); moves opposite to [[GDAP2]] (-0.57, fdr 1e-05), [[TIMM10B]] (-0.56, fdr 1e-05), [[AHSA1]] (-0.55, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CXCL2]] → it (grade B ⚠); 7 go from it, the strongest it → [[NKX3-1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **23.3×** | +33.8 | 0e+00 | 27/28 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **28.6×** | +24.5 | 0e+00 | 27/28 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **8.66×** | +16.4 | 0e+00 | 23/25 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.90×** | +14.6 | 0e+00 | 33/35 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.34×** | +11.2 | 8e-27 | 20/24 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.26×** | +11.0 | 3e-26 | 26/34 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.07×** | +10.7 | 1e-24 | 27/30 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.66×** | +7.4 | 7e-12 | 5/14 (PANC-1, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +7.2 | 3e-11 | 4/8 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.47×** | +6.9 | 3e-10 | 21/35 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.23×** | +5.9 | 2e-07 | 2/8 (NCI-H2347, HS-578T) | all doses, flat | composition shift |
| [[Amsacrine (drug)]] 5 µM |  | **1.72×** | +5.9 | 2e-07 | 13/35 (A498, SK-MEL-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +4.9 | 4e-05 | 9/31 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.78×** | +4.2 | 9e-04 | 11/17 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.1 | 0.002 | 4/16 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.70×** | +4.0 | 0.002 | 10/35 (A498, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.72×** | +4.0 | 0.002 | 13/31 (A-172, HS-578T, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.012 | 10/30 (HS-578T, A-172, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.016 | 11/32 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.044 | 7/30 (HS-578T, RPMI-7951, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +3.1 | 0.050 | 11/29 (PANC-1, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2569.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 2 lines (A549 0.0507×, NCI-H23 0.0829×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.581×** | -4.1 | 0.024 | 7/30 (HEC-1-A, SW 900, …) | two highest doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.631× | -3.5 | 0.10 | 9/34 (RPMI-7951, LOX-IMVI, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.632× | -3.5 | 0.10 | 11/34 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.1 | 0.26 | 8/36 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.669× | -3.0 | 0.26 | 9/36 (NCI-H1573, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.34 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +14.0) | — |
| [[A498 (line)]] | wt | 11.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.9× (z +27.5) | — |
| [[A549 (line)]] | wt | 7.41 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 31.7× (z +18.2) | [[Cobimetinib (drug)]] 5 µM 0.0507× (z -10.6) |
| [[A-172 (line)]] | wt | 7.85 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.6× (z +21.7) | — |
| [[PANC-1 (line)]] | alt | 7.44 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 76.3× (z +30.5) | — |
| [[BT-474 (line)]] | alt | 4.04 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 53.4× (z +12.9) | — |
| [[HEC-1-A (line)]] | alt | 2.03 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.1× (z +13.9) | — |
| [[J82 (line)]] | alt | 4.32 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 94.3× (z +18.6) | — |
| [[NCI-H2347 (line)]] | alt | 2.44 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 76.9× (z +17.4) | — |
| [[CFPAC-1 (line)]] | alt | 2.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 146× (z +19.1) | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.7× (z +16.3) | — |
| [[HOP62 (line)]] | alt | 1.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 70.4× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 3.76 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 4.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 1.63 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.3× (z +14.4) | — |
| [[Panc 03.27 (line)]] | alt | 1.79 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 130× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 3.87 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 82.8× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 4.68 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 63.5× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 9.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.3× (z +22.1) | — |
| [[C32 (line)]] | wt | 1.000 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.2× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 3.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.8× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 3.60 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +9.4) | — |
| [[NCI-H1792 (line)]] | alt | 2.06 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 60.6× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 7.11 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0829× (z -9.0) |
| [[A-427 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.624 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.821 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.748 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF3]] | +0.78 | +0.72 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[CCL20]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[S100A3]] | +0.69 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[ZC3H12A]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[IRAK2]] | +0.64 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[TNFAIP3]] | +0.64 | +0.58 / +0.65 | both halves | 8e-06 |  |
| [[CX3CL1]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[STX11]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[NFKBIA]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE |
| [[PTX3]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[BIRC3]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF385C]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDAP2]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[TIMM10B]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VPS53]] | -0.54 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[HACD3]] | -0.54 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[VTI1A]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[NIPA2]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL2]] | B | CXCL2 activity raises EBI3's level | lines that do not express CXCL2 (14) vs lines expressing it (36) | 1.03× lower at baseline in the lines without CXCL2 | 0.028 | ⚠ within organs, on part of the lines; also absent: TENT5A, GPR39, CXCL3 |
| [[STX11]] | B | STX11 activity raises EBI3's level | lines that do not express STX11 (8) vs lines expressing it (42) | 2.14× lower at baseline in the lines without STX11 | 0.049 | ⚠ within organs, on part of the lines; also absent: TSPAN4 |
| [[SLC35F1]] | B | SLC35F1 activity raises EBI3's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without SLC35F1 | 0.063 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[CSF1]] | B | CSF1 activity raises EBI3's level | lines that do not express CSF1 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without CSF1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SERPINE1, TNFRSF9, ROR1-AS1 |
| [[IKBKE]] | C | IKBKE activity lowers EBI3's level | lines that do not express IKBKE (4) vs lines expressing it (46) | 1.81× higher at baseline in the lines without IKBKE | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SP100, NAT1, NDRG1; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NKX3-1]] | B | EBI3 activity raises NKX3-1's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.77× lower at baseline in the lines without EBI3 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[CD40]] | B | EBI3 activity raises CD40's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 4.50× lower at baseline in the lines without EBI3 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[NFKBIE]] | B | EBI3 activity raises NFKBIE's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without EBI3 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[NFKB2]] | B | EBI3 activity raises NFKB2's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without EBI3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | B | EBI3 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express EBI3 (12) vs lines expressing it (36) | the lines without EBI3: 0.82× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[STX11]] | B | EBI3 activity raises STX11's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without EBI3 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |
| [[IRX3]] | C | EBI3 activity raises IRX3's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.86× lower at baseline in the lines without EBI3 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 9.1); signed map (13.1, 28.7). **Vector** length 85.3, 21.3% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.51 to 12); *IkBA variant leads to EDA-ID* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +24.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.7 | +33.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +14.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.9 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +16.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +4.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +3.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.5 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -1.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | Epstein-Barr virus induced 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,229,523-4,237,528 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IL27B, IL35B |
| Gene groups (HGNC) | Fibronectin type III domain containing; Minor histocompatibility antigens; Interleukin 12 type subunits |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INFLAMMATORY_RESPONSE |
| Reactome | 5 pathways, smallest: Interleukin-27 signaling; Interleukin-35 Signalling; Interleukin-12 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14213](https://www.uniprot.org/uniprotkb/Q14213) (Interleukin-27 subunit beta):

> Associates with IL27 to form the IL-27 interleukin, a heterodimeric cytokine which functions in innate immunity. IL-27 has pro- and anti-inflammatory properties, that can regulate T-helper cell development, suppress T-cell proliferation, stimulate cytotoxic T-cell activity, induce isotype switching in B-cells, and that has diverse effects on innate immune cells. Among its target cells are CD4 T-helper cells which can differentiate in type 1 effector cells (TH1), type 2 effector cells (TH2) and …

**Summary**, from NCBI Gene [10148](https://www.ncbi.nlm.nih.gov/gene/10148):

> This gene was identified by its induced expression in B lymphocytes in response Epstein-Barr virus infection. It encodes a secreted glycoprotein belonging to the hematopoietin receptor family, and heterodimerizes with a 28 kDa protein to form interleukin 27 (IL-27). IL-27 regulates T cell and inflammatory responses, in part by activating the Jak/STAT pathway of CD4+ T cells. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:3129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3129) · Entrez [10148](https://www.ncbi.nlm.nih.gov/gene/10148) · UniProt [Q14213](https://www.uniprot.org/uniprotkb/Q14213) · Ensembl [ENSG00000105246](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105246)

## Data

Gene col 2569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2569); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2569]; `tensor/DDL_lfc|DDL_z.npy` [2569]; `embed/gene_vectors.npy` [2569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2569 or target_col == 2569). Every well: [[EBI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
