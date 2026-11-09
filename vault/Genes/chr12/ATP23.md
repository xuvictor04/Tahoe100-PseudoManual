---
symbol: "ATP23"
type: "gene"
col: 9381
ensembl_id: "ENSG00000166896"
name: "ATP23 metallopeptidase and ATP synthase assembly factor homolog"
location: "12q14.1"
module: 14
arm: "+"
pooled_cpm: 5.23
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ATP23

*ATP23 metallopeptidase and ATP synthase assembly factor homolog* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.72× (z +21.4, q 0e+00, up in 39 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.107×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-172 0.108×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIFA]] (+0.74, fdr 7e-06), [[ZNF821]] (+0.70, fdr 7e-06), [[FAM200B]] (+0.66, fdr 1e-05); moves opposite to [[HERC2]] (-0.71, fdr 7e-06), [[HERC2P3]] (-0.71, fdr 1e-05), [[HERC2P9]] (-0.65, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.72×** | +21.4 | 0e+00 | 39/40 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.33×** | +19.6 | 0e+00 | 37/41 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.49×** | +10.1 | 1e-21 | 37/44 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +8.9 | 1e-16 | 23/38 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +8.6 | 1e-15 | 19/28 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.02×** | +7.7 | 9e-13 | 21/37 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.95×** | +7.7 | 1e-12 | 26/47 (PANC-1, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +7.6 | 2e-12 | 27/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.93×** | +7.5 | 3e-12 | 27/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +7.2 | 3e-11 | 21/46 (NCI-H2347, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.8 | 5e-10 | 18/39 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +6.3 | 1e-08 | 24/47 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +6.0 | 1e-07 | 19/47 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.9 | 2e-07 | 21/48 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.60×** | +5.2 | 9e-06 | 5/9 (SW480, NCI-H2030, …) | all doses, flat | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +4.8 | 5e-05 | 13/46 (HepG2/C3A, C32, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 9/46 (J82, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +3.5 | 0.015 | 3/46 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.71×** | +3.2 | 0.028 | 3/44 (A-427, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.059 | 10/46 (BT-474, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9381.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (SNU-423 0.107×); [[Naproxen (drug)]] 0.05 µM in 1 line (A-172 0.108×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.760× | -3.2 | 0.63 | 11/46 (SNU-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.31 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.4) | [[Naproxen (drug)]] 0.05 µM 0.108× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 5.92 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.72× (z +13.1) | — |
| [[PANC-1 (line)]] | alt | 6.23 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +13.1) | — |
| [[A498 (line)]] | wt | 7.81 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +10.8) | — |
| [[A549 (line)]] | wt | 3.66 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +8.9) | — |
| [[LoVo (line)]] | wt | 3.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.57× (z +8.6) | — |
| [[J82 (line)]] | alt | 4.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 5.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +10.8) | — |
| [[NCI-H460 (line)]] | wt | 4.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.94× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 6.51 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.107× (z -8.7) |
| [[SW480 (line)]] | alt | 7.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +8.5) | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIFA]] | +0.74 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[ZNF821]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[FAM200B]] | +0.66 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[STAP2]] | +0.66 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[ZNF563]] | +0.65 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[FAM111A-DT]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MITD1]] | +0.64 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[CDKN1B]] | +0.63 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[GAD1]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[BCOR]] | +0.63 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[ABCA5]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC2]] | -0.71 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[HERC2P3]] | -0.71 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.65 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HERC2P2]] | -0.64 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[RPRD1A]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[STK25]] | -0.60 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[RSU1]] | -0.59 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[ZNF731P]] | -0.59 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[HERC2P9-1]] | -0.59 | -0.30 / -0.62 | both halves | 2e-04 |  |
| [[VKORC1L1]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[FBXW2]] | -0.58 | -0.73 / -0.36 | both halves | 1e-04 |  |
| [[SPATA5]] | -0.58 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP23's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LHFPL6]] | B | LHFPL6 activity raises ATP23's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without LHFPL6 | 0.035 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[GIHCG]] | B | GIHCG activity raises ATP23's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without GIHCG | 0.093 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |
| [[ICAM5]] | B | ICAM5 activity raises ATP23's level | lines that do not express ICAM5 (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without ICAM5 | 0.096 | ⚠ within organs, on part of the lines; also absent: MDFIC, VIM, CAV1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.672). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.6, -26.0); signed map (-7.1, 4.0). **Vector** length 58.0, 8.50% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +19.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +21.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +10.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +7.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.4 | +8.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.4 | +2.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.9 | +7.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.8 | +7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | ATP23 metallopeptidase and ATP synthase assembly factor homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,906,039-57,959,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KUB3; previously XRCC6BP1 |
| Gene groups (HGNC) | M76 metallopeptidase family |
| Matched by | ensembl_id |

UniProt [Q9Y6H3](https://www.uniprot.org/uniprotkb/Q9Y6H3) carries no function annotation.

**Summary**, from NCBI Gene [91419](https://www.ncbi.nlm.nih.gov/gene/91419):

> The protein encoded by this gene is amplified in glioblastomas and interacts with the DNA binding subunit of DNA-dependent protein kinase. This kinase is involved in double-strand break repair (DSB), and higher expression of the encoded protein increases the efficiency of DSB. In addition, comparison to orthologous proteins strongly suggests that this protein is a metalloprotease important in the biosynthesis of mitochondrial ATPase. Several transcript variants encoding different isoforms have …

**Accessions** — [HGNC:29452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29452) · Entrez [91419](https://www.ncbi.nlm.nih.gov/gene/91419) · UniProt [Q9Y6H3](https://www.uniprot.org/uniprotkb/Q9Y6H3) · Ensembl [ENSG00000166896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166896)

## Data

Gene col 9381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9381); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9381]; `tensor/DDL_lfc|DDL_z.npy` [9381]; `embed/gene_vectors.npy` [9381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9381 or target_col == 9381). Every well: [[ATP23 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP23.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
