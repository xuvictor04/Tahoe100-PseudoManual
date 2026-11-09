---
symbol: "MFSD10"
type: "gene"
col: 3075
ensembl_id: "ENSG00000109736"
name: "solute carrier family 75 member 1"
location: "4p16.3"
module: 136
arm: "+"
pooled_cpm: 13.97
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 20
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# MFSD10

*solute carrier family 75 member 1* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.35× (z +10.3, q 3e-22, up in 29 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.43× (z +4.1, q 0.005, up in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 3.53×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.562× (z -9.8, q 4e-20, down in 33 of 46 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL17RD]] (+0.61, fdr 1e-04), [[PLSCR3]] (+0.61, fdr 1e-05), [[ELOVL1]] (+0.58, fdr 1e-05); moves opposite to [[LINC01836]] (-0.58, fdr 1e-04), [[C14orf93]] (-0.57, fdr 1e-04), [[RPRD2]] (-0.57, fdr 2e-04).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PAQR5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-172 3.53×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.35×** | +10.3 | 3e-22 | 29/35 (A-172, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.3 | 7e-08 | 14/25 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +5.8 | 2e-06 | 18/30 (KATO III, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.005 | 19/45 (HT-29, PANC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +3.4 | 0.064 | 15/46 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | 1.48× | +3.2 | 0.15 | 5/43 (SW480, MIA PaCa-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3075.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.562×** | -9.8 | 4e-20 | 33/46 (HS-578T, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.607×** | -5.8 | 2e-06 | 26/43 (A498, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.631×** | -5.3 | 3e-05 | 27/46 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.760×** | -4.7 | 4e-04 | 22/43 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.678×** | -4.5 | 7e-04 | 20/42 (H4, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.699×** | -4.3 | 0.001 | 25/45 (HCT15, J82, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -4.2 | 0.002 | 22/42 (A-427, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.696×** | -4.1 | 0.002 | 22/42 (HOP62, SK-MEL-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.718×** | -4.0 | 0.004 | 19/46 (CFPAC-1, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.713×** | -3.9 | 0.005 | 21/44 (NCI-H460, A549, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.728×** | -3.8 | 0.006 | 18/42 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.810×** | -3.5 | 0.019 | 17/46 (SW480, AsPC-1, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.738×** | -3.5 | 0.023 | 15/44 (MIA PaCa-2, SW480, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.580×** | -3.4 | 0.023 | 13/46 (KATO III, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.765×** | -3.2 | 0.046 | 12/46 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.759×** | -3.2 | 0.047 | 12/45 (A-427, H4, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.741×** | -3.2 | 0.048 | 14/47 (MIA PaCa-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.773×** | -3.1 | 0.059 | 19/46 (SW 1271, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tadalafil (drug)]] 5 µM |  | **0.777×** | -2.9 | 0.097 | 8/44 (AsPC-1, NCI-H2030, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.2 | 0 | 3 (1 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0594× (z -15.2) |
| [[A-172 (line)]] | wt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.277× (z -8.6) |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0734× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -9.4) |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.8) |
| [[HS-578T (line)]] | alt | 9.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -10.9) |
| [[LoVo (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 6.95 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.121× (z -9.6) |
| [[SW480 (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.1) |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL17RD]] | +0.61 | +0.64 / +0.33 | both halves | 1e-04 |  |
| [[PLSCR3]] | +0.61 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CSGALNACT2]] | +0.57 | +0.57 / +0.30 | both halves | 2e-04 |  |
| [[LRRFIP1]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[KLC3]] | +0.57 | +0.40 / +0.38 | both halves | 7e-05 |  |
| [[ACTG1]] | +0.56 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[PAQR5]] | +0.56 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[DVL1]] | +0.56 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[ZFYVE28]] | +0.56 | +0.54 / +0.39 | both halves | 6e-05 |  |
| [[FLNB]] | +0.55 | +0.64 / +0.29 | both halves | 2e-04 |  |
| [[MYO9B]] | +0.55 | +0.61 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01836]] | -0.58 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[C14orf93]] | -0.57 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[RPRD2]] | -0.57 | -0.54 / -0.30 | both halves | 2e-04 |  |
| [[HFE]] | -0.55 | -0.50 / -0.23 | both halves | 5e-04 |  |
| [[C2orf42]] | -0.54 | -0.55 / -0.21 | both halves | 7e-04 |  |
| [[LUC7L2]] | -0.53 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[RMDN2]] | -0.52 | -0.59 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[ABCC6]] | -0.52 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[SMAD1]] | -0.52 | -0.57 / -0.20 | both halves | 7e-04 |  |
| [[BTN3A3]] | -0.51 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[SAFB]] | -0.51 | -0.36 / -0.27 | both halves | 3e-04 |  |
| [[ZNF618]] | -0.51 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[HMGN5]] | -0.50 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR5]] | B | PAQR5 activity raises MFSD10's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without PAQR5 | 0.029 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[S100A16]] | B | S100A16 activity raises MFSD10's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 1.53× lower at baseline in the lines without S100A16 | 0.050 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[BOK]] | B | BOK activity raises MFSD10's level | lines that do not express BOK (5) vs lines expressing it (45) | 1.60× lower at baseline in the lines without BOK | 0.069 | ⚠ within organs, on part of the lines; also absent: SLC35F2, PLEC, IL4R |
| [[TSPAN4]] | B | TSPAN4 activity raises MFSD10's level | lines that do not express TSPAN4 (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without TSPAN4 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: TRPC1, EMP3, PXDC1; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises MFSD10's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without SLCO4A1 | 0.093 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.1, -0.5); signed map (-18.0, 25.7). **Vector** length 63.3, 11.2% of its response variance represented; |z| ≥ 3 in 748 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.3 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.2 | -3.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +3.1 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 75 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:2,930,561-2,934,834 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IT10C3, TETRAN, SLC75A1; previously MFSD10 |
| Gene groups (HGNC) | Solute carrier family 75 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14728](https://www.uniprot.org/uniprotkb/Q14728) (Solute carrier family 75 member 1):

> Probable organic anion transporter which may serve as a transporter for some non-steroidal anti-inflammatory drugs (NSAIDs) as well as other organic anions across the luminal membranes of renal proximal tubules at the final excretion step into the urine.

**Summary**, from NCBI Gene [10227](https://www.ncbi.nlm.nih.gov/gene/10227):

> This gene encodes a member of the major facilitator superfamily of transporter proteins. The encoded protein likely functions in efflux of organic anions, including the non-steroidal anti-inflammatory drugs indomethacin and diclofenac. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:16894](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16894) · Entrez [10227](https://www.ncbi.nlm.nih.gov/gene/10227) · UniProt [Q14728](https://www.uniprot.org/uniprotkb/Q14728) · Ensembl [ENSG00000109736](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109736)

## Data

Gene col 3075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3075); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3075]; `tensor/DDL_lfc|DDL_z.npy` [3075]; `embed/gene_vectors.npy` [3075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3075 or target_col == 3075). Every well: [[MFSD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
