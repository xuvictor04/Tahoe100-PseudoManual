---
symbol: "BTBD19"
type: "gene"
col: 13331
ensembl_id: "ENSG00000222009"
name: "BTB domain containing 19"
location: "1p34.1"
module: 109
arm: "+"
pooled_cpm: 6.97
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# BTBD19

*BTB domain containing 19* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +9.6, q 7e-19, up in 25 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM: 0.489× (z -5.2, q 9e-05, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLK3]] (+0.78, fdr 7e-06, ⚠ same locus), [[EGR3]] (+0.70, fdr 7e-06), [[ERCC1]] (+0.67, fdr 7e-06), [[EGR1]] (+0.65, fdr 7e-06); moves opposite to [[UBA3]] (-0.54, fdr 3e-05), [[JKAMP]] (-0.54, fdr 1e-05), [[ZNF148]] (-0.52, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SYNE3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +9.6 | 7e-19 | 25/38 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.97×** | +5.0 | 2e-04 | 22/43 (SK-MEL-2, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.84×** | +4.3 | 0.003 | 5/21 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.61×** | +3.5 | 0.074 | 12/42 (LS 180, LoVo, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.090 | 12/46 (A498, NCI-H460, …) | top dose only | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.090 | 8/46 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +3.1 | 0.18 | 6/46 (HT-29, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.489×** | -5.2 | 9e-05 | 24/41 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.543×** | -5.1 | 1e-04 | 25/45 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.533×** | -4.6 | 7e-04 | 20/39 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.558×** | -4.5 | 0.001 | 25/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.564×** | -4.4 | 0.001 | 19/44 (KATO III, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.668×** | -4.4 | 0.001 | 21/44 (SK-MEL-2, HT-29, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.343×** | -4.3 | 0.002 | 23/34 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.680×** | -4.1 | 0.003 | 19/44 (SW480, KATO III, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.646×** | -4.0 | 0.004 | 17/44 (SW480, NCI-H1573, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.693×** | -4.0 | 0.004 | 17/44 (HT-29, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.606×** | -3.5 | 0.021 | 18/45 (COLO 205, SW480, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.697× | -3.1 | 0.11 | 15/47 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.25 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +10.4) | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.151× (z -8.6) ⚠ toxic |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -8.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.92 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0799× (z -9.7) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0695× (z -9.7) |
| [[HOP62 (line)]] | alt | 8.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0602× (z -10.1) |
| [[HS-578T (line)]] | alt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +9.1) | — |
| [[J82 (line)]] | alt | 4.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.30× (z +10.3) | — |
| [[LoVo (line)]] | wt | 13.4 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.106× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0581× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 2.62 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0986× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.03 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0706× (z -8.7) |
| [[A-172 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLK3]] | +0.78 | +0.82 / +0.80 | both halves | 7e-06 | ⚠ same locus (2.5 kb, same strand: neighbours can correlate without regulation) |
| [[EGR3]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[ERCC1]] | +0.67 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[EGR1]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FOS]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SEMA4A]] | +0.65 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[EGR2]] | +0.65 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[NOP14-AS1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ASTL]] | +0.63 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[FOSB]] | +0.63 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[EPHA2]] | +0.62 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MAFF]] | +0.61 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[MYEOV]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA3]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[JKAMP]] | -0.54 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.52 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[CISD1]] | -0.52 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[FHIP2A]] | -0.52 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[FBXO9]] | -0.52 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[RNPC3]] | -0.51 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[TENT2]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[TRIT1]] | -0.50 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RBM27]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNE3]] | B | SYNE3 activity raises BTBD19's level | lines that do not express SYNE3 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without SYNE3 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INPP1]] | B | INPP1 activity raises BTBD19's level | lines that do not express INPP1 (12) vs lines expressing it (38) | 1.46× lower at baseline in the lines without INPP1 | 0.044 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ABL1]] | B | ABL1 activity raises BTBD19's level | compounds that target ABL1: 3 of 6 lower it (NG25, Ponatinib, Radotinib) | 50% of the class's compounds vs 1.7% of all compounds | 0.047 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TGFA]] | B | TGFA activity raises BTBD19's level | lines that do not express TGFA (17) vs lines expressing it (33) | 1.44× lower at baseline in the lines without TGFA | 0.056 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[SEMA4A]] | B | SEMA4A activity raises BTBD19's level | lines that do not express SEMA4A (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without SEMA4A | 0.089 | ⚠ within organs, on part of the lines; also absent: EPAS1, IER3, ATP1B1 |
| [[TNFRSF6B]] | B | TNFRSF6B activity raises BTBD19's level | lines that do not express TNFRSF6B (33) vs lines expressing it (17) | 1.34× lower at baseline in the lines without TNFRSF6B | 0.091 | ⚠ within organs, on part of the lines; also absent: WFDC2, GABRP, FGF19 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.740). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.7, -0.7); signed map (5.6, 30.1). **Vector** length 100, 22.6% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.60 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.58 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.57 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.6 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +2.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +3.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.7 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.6 | -3.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.4 | -5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.2 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,808,523-44,815,585 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [C9JJ37](https://www.uniprot.org/uniprotkb/C9JJ37) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27145) · Entrez [149478](https://www.ncbi.nlm.nih.gov/gene/149478) · UniProt [C9JJ37](https://www.uniprot.org/uniprotkb/C9JJ37) · Ensembl [ENSG00000222009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000222009)

## Data

Gene col 13331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13331); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13331]; `tensor/DDL_lfc|DDL_z.npy` [13331]; `embed/gene_vectors.npy` [13331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13331 or target_col == 13331). Every well: [[BTBD19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
