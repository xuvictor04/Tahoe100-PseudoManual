---
symbol: "COPG2IT1"
type: "gene"
col: 16210
ensembl_id: "ENSG00000286214"
name: "COPG2 imprinted transcript 1"
location: "7q32.2"
module: 33
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# COPG2IT1

*COPG2 imprinted transcript 1* — 7q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.83× (z +10.1, q 3e-21, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.60× (z +6.7, q 2e-09, up in 15 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.575× (z -5.6, q 1e-05, down in 11 of 34 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.310×, SW480 0.365×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0740×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.162×; ⚠ cell-cycle shift, explains ~83% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.142×); [[Naproxen (drug)]] 5 µM in 1 line (LoVo 0.140×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAH]] (+0.56, fdr 2e-05), [[MEST]] (+0.55, fdr 1e-05, ⚠ same locus), [[GPR143]] (+0.55, fdr 2e-05), [[GSTO2]] (+0.52, fdr 1e-05); moves opposite to [[C6orf62]] (-0.47, fdr 1e-04), [[SRGAP2C]] (-0.45, fdr 5e-04), [[PPP1CA]] (-0.44, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SORL1]] → it (grade B ⚠); 3 go from it, the strongest it → [[GSTO2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16210.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +10.1 | 3e-21 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.79×** | +9.6 | 2e-19 | 1/6 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.1 | 2e-17 | 5/13 (KATO III, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +7.7 | 2e-12 | 6/15 (SHP-77, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.60×** | +6.7 | 2e-09 | 15/34 (NCI-H23, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +6.1 | 1e-07 | 14/27 (AN3 CA, SW480, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.6 | 2e-06 | 15/34 (SW 900, LoVo, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.80×** | +5.4 | 4e-06 | 1/5 (NCI-H23) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.006 | 5/30 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.006 | 8/34 (NCI-H23, KATO III, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.010 | 5/18 (AN3 CA, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.95×** | +3.5 | 0.021 | 4/23 (SW480, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.023 | 7/34 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.053 | 3/25 (SHP-77, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.065 | 4/34 (J82, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.092 | 1/18 (A549) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.76×** | +3.0 | 0.092 | 0/24 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16210.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.310×, SW480 0.365×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (AN3 CA 0.0740×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.162×; ⚠ cell-cycle shift, explains ~83% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (SHP-77 0.142×); [[Naproxen (drug)]] 5 µM in 1 line (LoVo 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.575×** | -5.6 | 1e-05 | 11/34 (NCI-H460, KATO III, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.690×** | -3.8 | 0.044 | 14/34 (HCT15, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.551× | -3.2 | 0.23 | 8/30 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.734× | -3.1 | 0.23 | 3/34 (hTERT-HPNE, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16210. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 2 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0740× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 4.34 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.140× (z -8.5) |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.142× (z -8.8) |
| [[SW480 (line)]] | alt | 8.51 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.898 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.878 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.716 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.949 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16210), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAH]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[MEST]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 | ⚠ same locus (32.5 kb, same strand: neighbours can correlate without regulation) |
| [[GPR143]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[GSTO2]] | +0.52 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[LARGE2]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[EPHA10]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SFXN4]] | +0.51 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[UBE3D]] | +0.50 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[FGD3]] | +0.49 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[DUSP12]] | +0.49 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[PRPF39]] | +0.48 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[FXN]] | +0.48 | +0.31 / +0.56 | both halves | 2e-04 |  |
| [[SPIN3]] | +0.48 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SRGAP2C]] | -0.45 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[PPP1CA]] | -0.44 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[BZW1]] | -0.44 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SERPINB6]] | -0.44 | -0.26 / -0.48 | both halves | 4e-04 |  |
| [[CASP3]] | -0.44 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[PITPNC1]] | -0.43 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.42 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | SORL1 activity raises COPG2IT1's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 2.44× lower at baseline in the lines without SORL1 | 0.020 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[LINC00299]] | B | LINC00299 activity raises COPG2IT1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 2.27× lower at baseline in the lines without LINC00299 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[AXIN2]] | B | AXIN2 activity raises COPG2IT1's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without AXIN2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[LARGE2]] | B | LARGE2 activity raises COPG2IT1's level | lines that do not express LARGE2 (21) vs lines expressing it (29) | 1.36× lower at baseline in the lines without LARGE2 | 0.068 | ⚠ within organs, on part of the lines; also absent: EPHA10, YBX2, FBXO2 |
| [[DMKN]] | B | DMKN activity raises COPG2IT1's level | lines that do not express DMKN (24) vs lines expressing it (26) | 1.70× lower at baseline in the lines without DMKN | 0.081 | ⚠ within organs, on part of the lines; also absent: SPINT1, BSPRY, SMPDL3B |
| [[SMPDL3B]] | B | SMPDL3B activity raises COPG2IT1's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without SMPDL3B | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[MEST]] | C | MEST activity raises COPG2IT1's level | lines that do not express MEST (17) vs lines expressing it (33) | 3.02× lower at baseline in the lines without MEST | 8e-04 | ⚠ within organs, on part of the lines; also absent: COPG2IT1, CHDH, IL17RB; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSTO2]] | B | COPG2IT1 activity raises GSTO2's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 2.14× lower at baseline in the lines without COPG2IT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent |
| [[MEST]] | C | COPG2IT1 activity raises MEST's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 4.39× lower at baseline in the lines without COPG2IT1 | 0.012 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent; co-absent with the target |
| [[NMNAT3]] | C | COPG2IT1 activity raises NMNAT3's level | lines that do not express COPG2IT1 (12) vs lines expressing it (38) | 3.53× lower at baseline in the lines without COPG2IT1 | 0.026 | ⚠ within organs, on part of the lines; also absent: MEST, GLS2, NMNAT3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.394). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (0.9, 48.5); signed map (17.4, -48.8). **Vector** length 41.8, 5.56% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | +2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.8 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | COPG2 imprinted transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q32.2 — chr7:130,538,954-130,546,900 (+) |
| Ensembl biotype | lncRNA |
| Also known as | CIT1, NCRNA00170, COPG2AS |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:2238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2238) · Entrez [53844](https://www.ncbi.nlm.nih.gov/gene/53844) · Ensembl [ENSG00000286214](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000286214)

## Data

Gene col 16210: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16210); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16210, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16210]; `tensor/DDL_lfc|DDL_z.npy` [16210]; `embed/gene_vectors.npy` [16210]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16210 or target_col == 16210). Every well: [[COPG2IT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPG2IT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
