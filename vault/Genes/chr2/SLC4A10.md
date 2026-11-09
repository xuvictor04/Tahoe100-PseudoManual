---
symbol: "SLC4A10"
type: "gene"
col: 6862
ensembl_id: "ENSG00000144290"
name: "solute carrier family 4 member 10"
location: "2q24.2"
module: 53
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SLC4A10

*solute carrier family 4 member 10* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.48× (z +21.4, q 0e+00, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.651× (z -4.2, q 0.017, down in 6 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0509×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[L3MBTL2-AS1]] (+0.76, fdr 7e-06), [[FNDC7]] (+0.75, fdr 7e-06), [[SYT16]] (+0.75, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC01250]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6862.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.48×** | +21.4 | 0e+00 | 31/33 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.34×** | +21.1 | 0e+00 | 29/34 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.88×** | +12.1 | 4e-31 | 39/43 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.79×** | +11.8 | 3e-30 | 31/39 (A-172, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.50×** | +11.1 | 9e-27 | 22/33 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **7.25×** | +9.2 | 3e-18 | 26/38 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.79×** | +8.6 | 5e-16 | 28/40 (HEC-1-A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +7.3 | 2e-11 | 23/44 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.23×** | +6.9 | 5e-10 | 3/7 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +6.8 | 7e-10 | 14/34 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.00×** | +6.2 | 3e-08 | 4/17 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.1 | 5e-08 | 11/45 (A-172, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.51×** | +5.8 | 2e-07 | 17/34 (HOP62, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.94×** | +5.6 | 1e-06 | 15/42 (A-172, RKO, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +5.3 | 5e-06 | 14/45 (PANC-1, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +4.9 | 3e-05 | 14/40 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +4.7 | 9e-05 | 14/39 (SHP-77, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6862.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0509×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.651×** | -4.2 | 0.017 | 6/42 (RPMI-7951, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.614×** | -4.0 | 0.018 | 10/45 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.632× | -3.4 | 0.11 | 9/41 (LOX-IMVI, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.766× | -3.3 | 0.12 | 7/43 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.781× | -3.0 | 0.29 | 10/44 (SW480, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6862. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.50 | 2 | 0 | [[Auranofin (drug)]] 5 µM 19.5× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 2.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +10.8) | — |
| [[A498 (line)]] | wt | 2.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.49× (z +9.4) | — |
| [[A549 (line)]] | wt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.89× (z +8.8) | — |
| [[C32 (line)]] | wt | 2.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +8.7) | — |
| [[HS-578T (line)]] | alt | 3.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +9.4) | — |
| [[LoVo (line)]] | wt | 1.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +11.6) | — |
| [[LOX-IMVI (line)]] | wt | 9.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 1.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 2.83 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0509× (z -9.6) |
| [[PANC-1 (line)]] | alt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +8.8) | — |
| [[A-427 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6862), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[L3MBTL2-AS1]] | +0.76 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[SYT16]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[IL12RB2]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.74 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.73 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[PEBP4]] | +0.73 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.73 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.73 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[USP50]] | +0.73 | +0.75 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC4A10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MYT1L]] | C | MYT1L's natural level weakens SLC4A10's drug response | MYT1L's natural level across 38 lines (lineage-adjusted; a glimpse) | r -0.71, reverse -0.68; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CHRM5]] | C | CHRM5's natural level weakens SLC4A10's drug response | CHRM5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.62; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01250]] | C | SLC4A10's natural level weakens LINC01250's drug response | SLC4A10's natural level across 36 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.51; direction clear | 0.006 | ⚠ tissue can mimic it; precision caveat |
| [[LINC00578]] | C | SLC4A10's natural level weakens LINC00578's drug response | SLC4A10's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.40; direction clear | 0.069 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.2, -10.5); signed map (22.1, 10.5). **Vector** length 66.8, 10.9% of its response variance represented; |z| ≥ 3 in 1,046 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.0 | +21.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +21.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +6.4 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +6.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.4 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +5.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.8 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | -2.1 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:161,424,332-161,985,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBCn2, NCBE |
| Gene groups (HGNC) | Solute carrier family 4 |
| Reactome | 4 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6U841](https://www.uniprot.org/uniprotkb/Q6U841) (Sodium-driven chloride bicarbonate exchanger):

> Sodium/bicarbonate cotransporter which plays an important role in regulating intracellular pH. Has been shown to act as a sodium/bicarbonate cotransporter in exchange for intracellular chloride (By similarity). Has also been shown to act as a sodium/biocarbonate cotransporter which does not couple net influx of bicarbonate to net efflux of chloride, with the observed chloride efflux being due to chloride self-exchange. Controls neuronal pH and may contribute to the secretion of cerebrospinal …

**Summary**, from NCBI Gene [57282](https://www.ncbi.nlm.nih.gov/gene/57282):

> This gene belongs to a small family of sodium-coupled bicarbonate transporters (NCBTs) that regulate the intracellular pH of neurons, the secretion of bicarbonate ions across the choroid plexus, and the pH of the brain extracellular fluid. The protein encoded by this gene was initially identified as a sodium-driven chloride bicarbonate exchanger (NCBE) though there is now evidence that its sodium/bicarbonate cotransport activity is independent of any chloride ion countertransport under …

**Accessions** — [HGNC:13811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13811) · Entrez [57282](https://www.ncbi.nlm.nih.gov/gene/57282) · UniProt [Q6U841](https://www.uniprot.org/uniprotkb/Q6U841) · Ensembl [ENSG00000144290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144290)

## Data

Gene col 6862: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6862); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6862, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6862]; `tensor/DDL_lfc|DDL_z.npy` [6862]; `embed/gene_vectors.npy` [6862]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6862 or target_col == 6862). Every well: [[SLC4A10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
