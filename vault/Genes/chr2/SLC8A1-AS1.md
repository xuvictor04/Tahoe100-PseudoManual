---
symbol: "SLC8A1-AS1"
type: "gene"
col: 13567
ensembl_id: "ENSG00000227028"
name: "SLC8A1 antisense RNA 1"
location: "2p22.1"
module: 165
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# SLC8A1-AS1

*SLC8A1 antisense RNA 1* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.18× (z +26.1, q 0e+00, up in 27 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[OTS514 (drug)]] 0.05 µM in 1 line (PANC-1 0.0632×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01500]] (+0.80, fdr 7e-06), [[OPCML]] (+0.78, fdr 7e-06), [[DLGAP2]] (+0.77, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[APBB1IP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13567.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.18×** | +26.1 | 0e+00 | 27/31 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +14.1 | 2e-42 | 24/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.12×** | +12.8 | 5e-35 | 31/40 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.07×** | +12.1 | 2e-31 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.97×** | +10.7 | 1e-24 | 26/45 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.51×** | +10.3 | 7e-23 | 3/14 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +9.9 | 2e-21 | 21/39 (A-172, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +9.3 | 7e-19 | 2/6 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +8.1 | 4e-14 | 12/31 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +7.4 | 7e-12 | 14/45 (HOP62, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.92×** | +7.3 | 2e-11 | 22/45 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +6.7 | 8e-10 | 21/38 (SW480, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.7 | 8e-10 | 14/35 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +6.7 | 9e-10 | 13/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +6.1 | 3e-08 | 14/44 (A-427, SHP-77, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +5.3 | 5e-06 | 17/43 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +5.0 | 2e-05 | 11/38 (SK-MEL-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.005 | 5/36 (SW1417, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13567.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[OTS514 (drug)]] 0.05 µM in 1 line (PANC-1 0.0632×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ranolazine (drug)]] 0.5 µM |  | 0.735× | -3.5 | 0.25 | 4/43 (NCI-H1573, CFPAC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.747× | -3.3 | 0.25 | 2/45 (AN3 CA, COLO 205) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.2 | 0.25 | 10/46 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[IQ 1 (drug)]] 0.05 µM |  | 0.755× | -3.0 | 0.35 | 3/42 (HOP62, SW48, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13567. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.24 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +10.1) | [[OTS514 (drug)]] 0.05 µM 0.0632× (z -10.1) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 2.00 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 10.8× (z +12.1) | — |
| [[A498 (line)]] | wt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 2.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 4.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.5× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 2.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.51× (z +10.5) | — |
| [[A-172 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13567), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01500]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[OPCML]] | +0.78 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[KCNAB1]] | +0.74 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.74 | +0.63 / +0.82 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.74 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.74 | +0.54 / +0.83 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.72 | +0.58 / +0.79 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.72 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[RELN]] | +0.72 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[LINC01483]] | +0.71 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[USH2A]] | +0.71 | +0.62 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APBB1IP]] | B | APBB1IP activity raises SLC8A1-AS1's level | lines that do not express APBB1IP (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without APBB1IP | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000254337, TMPRSS15, ENSG00000235749 |
| [[PHACTR1]] | B | PHACTR1 activity raises SLC8A1-AS1's level | lines that do not express PHACTR1 (35) vs lines expressing it (15) | 1.58× lower at baseline in the lines without PHACTR1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, MMP2, APCDD1L |
| [[PSG5]] | B | PSG5 activity raises SLC8A1-AS1's level | lines that do not express PSG5 (40) vs lines expressing it (10) | 1.73× lower at baseline in the lines without PSG5 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, PSG9, ENSG00000243486 |
| [[TOP2A]] | B | TOP2A activity lowers SLC8A1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GRIA1]] | B | GRIA1 activity raises SLC8A1-AS1's level | lines that do not express GRIA1 (17) vs lines expressing it (33) | 1.32× lower at baseline in the lines without GRIA1 | 0.056 | ⚠ within organs, on part of the lines; also absent: RAMP1, ENSG00000263745, ENSG00000285534; maybe low, not absent |
| [[LINC01435]] | B | LINC01435 activity raises SLC8A1-AS1's level | lines that do not express LINC01435 (37) vs lines expressing it (13) | 1.48× lower at baseline in the lines without LINC01435 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000203434, TMPRSS15, ENSG00000224865 |
| [[SRRM3]] | B | SRRM3 activity lowers SLC8A1-AS1's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.42× higher at baseline in the lines without SRRM3 | 0.073 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises SLC8A1-AS1's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 1.42× lower at baseline in the lines without ADAM7-AS1 | 0.075 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[OR9Q1]] | B | OR9Q1 activity raises SLC8A1-AS1's level | lines that do not express OR9Q1 (26) vs lines expressing it (24) | 1.54× lower at baseline in the lines without OR9Q1 | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01583, ADAM12, APCDD1L |
| [[LINC00922]] | B | LINC00922 activity raises SLC8A1-AS1's level | lines that do not express LINC00922 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without LINC00922 | 0.083 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[SLC8A1]] | B | SLC8A1 activity raises SLC8A1-AS1's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without SLC8A1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.844). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.9, 30.0); signed map (30.4, 15.7). **Vector** length 57.5, 7.94% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +26.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +14.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +7.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +0.7 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SLC8A1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p22.1 — chr2:39,786,453-40,255,209 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44102) · Entrez [100128590](https://www.ncbi.nlm.nih.gov/gene/100128590) · Ensembl [ENSG00000227028](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227028)

## Data

Gene col 13567: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13567); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13567, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13567]; `tensor/DDL_lfc|DDL_z.npy` [13567]; `embed/gene_vectors.npy` [13567]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13567 or target_col == 13567). Every well: [[SLC8A1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC8A1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
