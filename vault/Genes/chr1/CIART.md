---
symbol: "CIART"
type: "gene"
col: 8229
ensembl_id: "ENSG00000159208"
name: "circadian associated repressor of transcription"
location: "1q21.2"
module: 14
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 28
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CIART

*circadian associated repressor of transcription* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.17× (z +17.2, q 0e+00, up in 17 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Megestrol (drug)]] 5 µM: 0.672× (z -4.2, q 0.015, down in 12 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0507×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.122×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-423 0.0786×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF433]] (+0.60, fdr 1e-05), [[ZNF442]] (+0.60, fdr 1e-05), [[TRPM2-AS]] (+0.58, fdr 1e-05); moves opposite to [[SMC5]] (-0.50, fdr 1e-04), [[S100A16]] (-0.48, fdr 8e-05), [[NAPG]] (-0.46, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF442]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZCCHC17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8229.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.17×** | +17.2 | 0e+00 | 17/18 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.42×** | +12.9 | 2e-35 | 15/18 (KATO III, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **4.68×** | +11.0 | 7e-26 | 20/20 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.86×** | +10.0 | 2e-21 | 20/24 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +9.6 | 7e-20 | 16/16 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.94×** | +8.0 | 1e-13 | 17/19 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.49×** | +7.8 | 5e-13 | 20/20 (SW 900, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +6.4 | 1e-08 | 10/14 (C32, SHP-77, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.31×** | +6.2 | 4e-08 | 15/22 (KATO III, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +6.2 | 4e-08 | 12/23 (HS-578T, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.66×** | +6.0 | 1e-07 | 15/19 (NCI-H2347, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.15×** | +5.7 | 6e-07 | 17/23 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +5.2 | 1e-05 | 3/10 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.99×** | +5.1 | 1e-05 | 14/23 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.6 | 2e-04 | 1/5 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.74×** | +4.1 | 0.002 | 9/22 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.7 | 0.006 | 3/14 (CFPAC-1, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.010 | 6/15 (A-172, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +3.5 | 0.011 | 9/22 (A-172, H4, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8229.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.115×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.05 µM in 1 line (SHP-77 0.0507×); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.122×; ⚠ toxic; transcription drop); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (SNU-423 0.0786×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 5 µM |  | **0.672×** | -4.2 | 0.015 | 12/24 (A-172, SHP-77, …) | top dose only |  |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.597×** | -3.8 | 0.034 | 12/24 (SNU-423, PANC-1, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | 0.661× | -3.1 | 0.38 | 3/25 (AsPC-1, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8229. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +16.1) | — |
| [[C32 (line)]] | wt | 5.97 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 48.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 3.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 3.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 6.76 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 4.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 2.37 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 14.0 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.05 µM 0.0507× (z -10.5) |
| [[SNU-423 (line)]] | alt | 6.68 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0786× (z -8.5) |
| [[SW 900 (line)]] | alt | 9.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +11.6) | — |
| [[SW1417 (line)]] | alt | 3.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +11.5) | — |
| [[A-427 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.597 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.524 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.578 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.698 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.614 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.488 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8229), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF433]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ZNF442]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[TRPM2-AS]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.58 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[CSF1]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[SIAH1]] | +0.56 | +0.39 / +0.60 | both halves | 6e-05 |  |
| [[TNIP1]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[STAT5A]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[WTAP]] | +0.55 | +0.29 / +0.68 | both halves | 2e-04 |  |
| [[SMPD2]] | +0.54 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TIFA]] | +0.54 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[HDGF]] | +0.54 | +0.46 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMC5]] | -0.50 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[S100A16]] | -0.48 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[NAPG]] | -0.46 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[WDR37]] | -0.45 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[TIMP1]] | -0.45 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[COL5A1]] | -0.45 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[MANCR]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[ZCCHC17]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[GON4L]] | -0.44 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PCYT1A]] | -0.44 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[ITGA2]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ZCCHC24]] | -0.44 | -0.35 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF442]] | B | ZNF442 activity raises CIART's level | lines that do not express ZNF442 (7) vs lines expressing it (43) | 2.30× lower at baseline in the lines without ZNF442 | 0.079 | ⚠ within organs, on part of the lines; also absent: ZNF563, ENSG00000286098, ENSG00000268870 |
| [[ZNF433]] | B | ZNF433 activity raises CIART's level | lines that do not express ZNF433 (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without ZNF433 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF563, ZNF442 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZCCHC17]] | B | CIART activity raises ZCCHC17's level | lines that do not express CIART (22) vs lines expressing it (28) | 1.25× lower at baseline in the lines without CIART | 0.008 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |
| [[ZNF441]] | B | CIART activity raises ZNF441's level | lines that do not express CIART (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without CIART | 0.008 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |
| [[ZNF20]] | B | CIART activity raises ZNF20's level | lines that do not express CIART (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without CIART | 0.013 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |
| [[ZNF433]] | B | CIART activity raises ZNF433's level | lines that do not express CIART (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without CIART | 0.048 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |
| [[ZNF844]] | B | CIART activity raises ZNF844's level | lines that do not express CIART (22) vs lines expressing it (28) | 2.02× lower at baseline in the lines without CIART | 0.075 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, PTN, PPP2R2B |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.9, 4.6); signed map (42.4, 4.6). **Vector** length 44.5, 8.78% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +4.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +0.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.3 | +0.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | circadian associated repressor of transcription |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,282,543-150,287,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BC017397, CHRONO; previously C1orf51 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N365](https://www.uniprot.org/uniprotkb/Q8N365) (Circadian-associated transcriptional repressor):

> Transcriptional repressor which forms a negative regulatory component of the circadian clock and acts independently of the circadian transcriptional repressors: CRY1, CRY2 and BHLHE41. In a histone deacetylase-dependent manner represses the transcriptional activator activity of the CLOCK-BMAL1 heterodimer. Abrogates the interaction of BMAL1 with the transcriptional coactivator CREBBP and can repress the histone acetyl-transferase activity of the CLOCK-BMAL1 heterodimer, reducing histone …

**Summary**, from NCBI Gene [148523](https://www.ncbi.nlm.nih.gov/gene/148523):

> Predicted to enable E-box binding activity. Predicted to be involved in circadian regulation of gene expression; locomotor rhythm; and negative regulation of DNA-templated transcription. Predicted to be located in PML body. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25200) · Entrez [148523](https://www.ncbi.nlm.nih.gov/gene/148523) · UniProt [Q8N365](https://www.uniprot.org/uniprotkb/Q8N365) · Ensembl [ENSG00000159208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159208)

## Data

Gene col 8229: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8229); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8229, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8229]; `tensor/DDL_lfc|DDL_z.npy` [8229]; `embed/gene_vectors.npy` [8229]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8229 or target_col == 8229). Every well: [[CIART — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIART.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
