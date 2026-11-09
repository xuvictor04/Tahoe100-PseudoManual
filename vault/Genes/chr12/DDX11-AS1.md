---
symbol: "DDX11-AS1"
type: "gene"
col: 14436
ensembl_id: "ENSG00000245614"
name: "DDX11 antisense RNA 1"
location: "12p11.21"
module: 6
arm: "+"
pooled_cpm: 8.0
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DDX11-AS1

*DDX11 antisense RNA 1* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.87× (z +6.7, q 2e-08, up in 24 of 44 measured lines) ⚠ cell-cycle shift, explains ~52% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.44× (z +3.9, q 0.008, up in 15 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.332× (z -11.7, q 8e-29, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RANBP1]] (+0.71, fdr 7e-06), [[CDC7]] (+0.70, fdr 7e-06), [[MCM3]] (+0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.87×** | +6.7 | 2e-08 | 24/44 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.80×** | +6.0 | 7e-07 | 4/10 (CFPAC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.66×** | +5.2 | 5e-05 | 18/36 (SW480, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.51×** | +4.4 | 0.002 | 10/25 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.53×** | +4.2 | 0.003 | 4/15 (SW 900, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.48×** | +4.0 | 0.006 | 8/42 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.008 | 15/44 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.28×** | +3.7 | 0.017 | 9/39 (SW480, NCI-H1792, …) | top dose only | position effect removed |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.023 | 5/43 (SW1417, LoVo, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +3.5 | 0.023 | 5/42 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +3.5 | 0.024 | 13/44 (SW 900, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.38×** | +3.4 | 0.033 | 10/40 (SW48, SW 900, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.4 | 0.033 | 8/44 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.36×** | +3.3 | 0.041 | 9/44 (SW480, RKO, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.24×** | +3.2 | 0.053 | 12/43 (J82, PANC-1, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.332×** | -11.7 | 8e-29 | 38/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.526×** | -9.6 | 2e-19 | 24/40 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.443×** | -8.6 | 1e-15 | 24/43 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.446×** | -8.6 | 1e-15 | 29/44 (KATO III, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.485×** | -7.7 | 2e-12 | 26/43 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.539×** | -6.5 | 5e-09 | 23/38 (SW480, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.565×** | -6.1 | 1e-07 | 24/43 (LoVo, A-427, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.555×** | -5.9 | 3e-07 | 23/41 (Hs 766T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.583×** | -5.7 | 7e-07 | 20/39 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.585×** | -5.5 | 3e-06 | 23/42 (A-427, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.604×** | -5.3 | 5e-06 | 21/45 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.630×** | -4.9 | 5e-05 | 21/43 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.735×** | -4.6 | 2e-04 | 16/44 (SW480, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.651×** | -4.2 | 0.001 | 10/44 (C-33 A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -4.1 | 0.002 | 13/41 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.498×** | -3.9 | 0.004 | 14/39 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM |  | **0.608×** | -3.8 | 0.006 | 9/45 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~5% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, -0.72 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.8 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -13.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -11.2) |
| [[SW480 (line)]] | alt | 15.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -12.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.288× (z -8.6) |
| [[A-427 (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -11.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[J82 (line)]] | alt | 12.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.188× (z -8.9) |
| [[LoVo (line)]] | wt | 15.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 5.22 | 0 | 2 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.0687× (z -10.4) |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.197× (z -9.0) |
| [[A498 (line)]] | wt | 4.53 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0796× (z -8.8) |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0844× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 3.31 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0516× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -10.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[KATO III (line)]] | alt | 8.35 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.137× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 3.83 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0692× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -9.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[RKO (line)]] | wt | 8.11 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -8.7) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-172 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP1]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[CDC7]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MCM3]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[E2F2]] | +0.70 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[E2F1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[MCM4]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.68 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[FAM111B]] | +0.68 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[UHRF1]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[EXO1]] | +0.68 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.68 | +0.58 / +0.76 | both halves | 8e-06 |  |
| [[DTL]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises DDX11-AS1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without E2F2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[LYPD6]] | B | LYPD6 activity raises DDX11-AS1's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without LYPD6 | 0.071 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[PDE3B]] | B | PDE3B activity raises DDX11-AS1's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.55× lower at baseline in the lines without PDE3B | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.1, -43.2); signed map (-35.5, -45.3). **Vector** length 68.1, 11.5% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 65); *DNA strand elongation* (reactome, mean cos +0.56 to 28); *DNA Replication* (reactome, mean cos +0.54 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +3.7 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | -1.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +1.8 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +1.0 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.2 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -5.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -3.5 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.5 | -7.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -4.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | DDX11 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p11.21 — chr12:31,019,434-31,073,847 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CONCR, SCAT4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44176](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44176) · Entrez [100506660](https://www.ncbi.nlm.nih.gov/gene/100506660) · Ensembl [ENSG00000245614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245614)

## Data

Gene col 14436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14436); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14436]; `tensor/DDL_lfc|DDL_z.npy` [14436]; `embed/gene_vectors.npy` [14436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14436 or target_col == 14436). Every well: [[DDX11-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX11-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
