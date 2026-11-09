---
symbol: "MGAM"
type: "gene"
col: 15034
ensembl_id: "ENSG00000257335"
name: "maltase-glucoamylase"
location: "7q34"
module: 26
arm: "+"
pooled_cpm: 8.08
n_lines_expressing: 47
n_dd_up: 35
n_dd_down: 9
n_dd_up_clean: 30
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MGAM

*maltase-glucoamylase* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 10.1× (z +16.7, q 0e+00, up in 38 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.541× (z -4.5, q 0.005, down in 20 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.578× (z -4.0, q 0.016, down in 21 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.84, fdr 7e-06), [[CCDC30]] (+0.83, fdr 7e-06), [[HSD17B3]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LINC00504]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15034.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **10.1×** | +16.7 | 0e+00 | 38/42 (NCI-H23, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.83×** | +16.3 | 0e+00 | 36/39 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.40×** | +11.9 | 3e-30 | 32/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.54×** | +10.6 | 2e-24 | 30/39 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +10.1 | 9e-22 | 22/38 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.29×** | +8.6 | 1e-15 | 29/44 (SW1417, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.83×** | +7.6 | 2e-12 | 29/40 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **6.22×** | +7.0 | 2e-10 | 34/43 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.62×** | +6.8 | 8e-10 | 28/41 (LoVo, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.41×** | +6.3 | 1e-08 | 26/43 (LoVo, A498, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.81×** | +6.1 | 4e-08 | 24/44 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.61×** | +4.8 | 8e-05 | 20/44 (C32, SW48, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +4.4 | 4e-04 | 6/14 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.81×** | +4.3 | 6e-04 | 18/42 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.83×** | +4.3 | 6e-04 | 18/42 (A498, PANC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.61×** | +4.2 | 9e-04 | 13/44 (LoVo, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.79×** | +4.2 | 1e-03 | 14/44 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.541×** | -4.5 | 0.005 | 20/38 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.578×** | -4.0 | 0.016 | 21/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.591×** | -3.8 | 0.025 | 18/44 (SNU-1, HCT15, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.609×** | -3.6 | 0.044 | 17/44 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.621×** | -3.5 | 0.051 | 18/44 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.625×** | -3.5 | 0.051 | 15/44 (SW480, COLO 205, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.641×** | -3.3 | 0.086 | 21/43 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.650×** | -3.2 | 0.100 | 13/44 (SNU-423, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.439×** | -3.2 | 0.100 | 15/39 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.445× | -3.1 | 0.11 | 15/41 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Furosemide (drug)]] 5 µM |  | 0.747× | -3.0 | 0.12 | 10/45 (NCI-H1573, COLO 205, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.6 | 3 | 10 (7 ⚠) | [[Auranofin (drug)]] 5 µM 6.78× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0843× (z -13.4) ⚠ cell-cycle shift, explains ~96% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.114× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 3.34 | 5 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 22.7× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 11.2 | 3 | 1 | [[Auranofin (drug)]] 5 µM 19.2× (z +10.9) | [[Ixazomib citrate (drug)]] 5 µM 0.0744× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 8.68 | 3 | 1 | [[Auranofin (drug)]] 5 µM 33.1× (z +11.7) | [[Silodosin (drug)]] 5 µM 0.0629× (z -9.0) |
| [[SNU-1 (line)]] | wt | 47.8 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0835× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -9.5) |
| [[LoVo (line)]] | wt | 7.35 | 3 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0503× (z -11.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0738× (z -9.6) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.0946× (z -8.7) |
| [[HCT15 (line)]] | alt | 42.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0897× (z -9.1) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0998× (z -8.7) |
| [[HS-578T (line)]] | alt | 3.51 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 4.07 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.54× (z +9.0) | — |
| [[A-172 (line)]] | wt | 4.67 | 1 | 0 | [[Auranofin (drug)]] 5 µM 25.0× (z +9.5) | — |
| [[A498 (line)]] | wt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +9.5) | — |
| [[C32 (line)]] | wt | 64.4 | 0 | 1 | — | [[Ponatinib (drug)]] 5 µM 0.149× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 2.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 11.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.6× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.126× (z -8.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[HOP62 (line)]] | alt | 4.76 | 1 | 0 | [[Auranofin (drug)]] 5 µM 18.7× (z +8.8) | — |
| [[KATO III (line)]] | alt | 5.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.68× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.92 | 1 | 0 | [[Auranofin (drug)]] 5 µM 28.1× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 3.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +9.9) | — |
| [[RKO (line)]] | wt | 7.12 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 19.4× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.84 | +0.83 / +0.74 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.83 | +0.83 / +0.66 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.81 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.81 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[CASS4]] | +0.81 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.81 | +0.80 / +0.61 | both halves | 7e-06 |  |
| [[CHD1-DT]] | +0.80 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[NEB]] | +0.80 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.79 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[CXCL13]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[LINC02641]] | +0.79 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[SLC26A7]] | +0.78 | +0.77 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00504]] | B | LINC00504 activity raises MGAM's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.95× lower at baseline in the lines without LINC00504 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[LINC02398]] | B | LINC02398 activity raises MGAM's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without LINC02398 | 0.037 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MGAM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC01917]] | B | LINC01917 activity raises MGAM's level | lines that do not express LINC01917 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without LINC01917 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC00504, RMEL3, TEK; maybe low, not absent |
| [[GPC5]] | B | GPC5 activity raises MGAM's level | lines that do not express GPC5 (8) vs lines expressing it (42) | 1.84× lower at baseline in the lines without GPC5 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises MGAM's level | lines that do not express FRZB (4) vs lines expressing it (46) | 2.24× lower at baseline in the lines without FRZB | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.849). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.4, 17.1); signed map (23.4, -0.4). **Vector** length 110, 27.6% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.9 | +16.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | +7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +8.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +6.8 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -7.4 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -5.8 | -3.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.6 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.6 | -1.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.4 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | maltase-glucoamylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:141,907,813-142,106,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGA |
| Gene groups (HGNC) | Glycoside hydrolase family 31 |
| Reactome | 4 pathways, smallest: Digestion; Digestion and absorption; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [O43451](https://www.uniprot.org/uniprotkb/O43451) (Maltase-glucoamylase):

> Alpha-(1,4) exo-glucosidase involved in breakdown of dietary starch oligosaccharides in small intestine. Cleaves the non-reducing alpha-(1,4)-linked glucose residue in linear dextrins with retention of anomeric center stereochemistry. Mainly hydrolyzes short length oligomaltoses having two to seven glucose residues. Can cleave alpha-(1,2), alpha-(1,3) and alpha-(1,6) glycosidic linkages with lower efficiency, whereas beta glycosidic linkages are usually not hydrolyzed.

**Summary**, from NCBI Gene [8972](https://www.ncbi.nlm.nih.gov/gene/8972):

> This gene encodes maltase-glucoamylase, which is a brush border membrane enzyme that plays a role in the final steps of digestion of starch. The protein has two catalytic sites identical to those of sucrase-isomaltase, but the proteins are only 59% homologous. Both are members of glycosyl hydrolase family 31, which has a variety of substrate specificities. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7043) · Entrez [8972](https://www.ncbi.nlm.nih.gov/gene/8972) · UniProt [O43451](https://www.uniprot.org/uniprotkb/O43451) · Ensembl [ENSG00000257335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257335)

## Data

Gene col 15034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15034); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15034]; `tensor/DDL_lfc|DDL_z.npy` [15034]; `embed/gene_vectors.npy` [15034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15034 or target_col == 15034). Every well: [[MGAM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
