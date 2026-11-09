---
symbol: "FAM72A"
type: "gene"
col: 12235
ensembl_id: "ENSG00000196550"
name: "regulator of UNG2 and MKLN1 interacting yippee protein 1"
location: "1q32.1"
module: 22
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# FAM72A

*regulator of UNG2 and MKLN1 interacting yippee protein 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.06× (z +16.7, q 0e+00, up in 22 of 28 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.90× (z +16.2, q 0e+00, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Cytarabine (hydrochloride) (drug)]] 0.5 µM: 0.614× (z -4.2, q 0.019, down in 12 of 41 measured lines) ⚠ cell-cycle shift, explains ~46% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.0305×; ⚠ cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0677×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0473×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (C32 0.0603×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM72D]] (+0.91, fdr 7e-06), [[FAM72B]] (+0.88, fdr 7e-06), [[PIF1]] (+0.82, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 21 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12235.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **4.06×** | +16.7 | 0e+00 | 22/28 (PANC-1, NCI-H2030, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.90×** | +16.2 | 0e+00 | 26/31 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +10.0 | 5e-21 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **3.05×** | +9.4 | 1e-18 | 32/44 (PANC-1, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.95×** | +9.1 | 1e-17 | 15/23 (PANC-1, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **2.41×** | +7.4 | 1e-11 | 2/12 (SHP-77, SW480) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.40×** | +7.3 | 2e-11 | 19/32 (PANC-1, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.99×** | +5.8 | 6e-07 | 15/37 (KATO III, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.7 | 7e-07 | 8/41 (RPMI-7951, J82, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.36×** | +5.6 | 2e-06 | 12/40 (PANC-1, C32, …) | top dose only | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.90×** | +5.4 | 4e-06 | 13/26 (A498, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.89×** | +5.3 | 5e-06 | 13/43 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.82×** | +5.0 | 3e-05 | 2/12 (SW480, C32) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.12×** | +4.8 | 5e-05 | 0/3 | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.73×** | +4.6 | 2e-04 | 10/34 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +4.3 | 7e-04 | 9/43 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.003 | 11/38 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.52×** | +3.5 | 0.012 | 4/26 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.036 | 7/44 (A-427, SW480, …) | rises with dose | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.40×** | +2.8 | 0.096 | 2/28 (PANC-1, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.0305×; ⚠ cell-cycle shift, would explain all of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (SW480 0.0677×); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0473×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (C32 0.0603×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.614×** | -4.2 | 0.019 | 12/41 (C-33 A, HOP62, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.617× | -3.2 | 0.27 | 7/35 (HEC-1-A, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | 0.674× | -3.1 | 0.27 | 7/37 (HCT15, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.695× | -3.1 | 0.27 | 10/32 (A-427, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.95 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.79 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +9.5) ⚠ cell-cycle shift, explains ~49% of this change | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0603× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 3.26 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.72× (z +10.4) ⚠ cell-cycle shift, explains ~49% of this change | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0747× (z -8.8) |
| [[A-427 (line)]] | wt | 5.19 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0305× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 5.24 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +8.9) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 4.68 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +10.4) ⚠ cell-cycle shift, explains ~49% of this change | — |
| [[SHP-77 (line)]] | alt | 5.87 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0473× (z -9.7) |
| [[SW480 (line)]] | alt | 2.63 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0677× (z -10.4) |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.723 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.628 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.961 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM72D]] | +0.91 | +0.83 / +0.92 | both halves | 7e-06 | STRING 478 |
| [[FAM72B]] | +0.88 | +0.85 / +0.86 | both halves | 7e-06 | STRING 636 |
| [[PIF1]] | +0.82 | +0.70 / +0.84 | both halves | 7e-06 |  |
| [[SGO2]] | +0.80 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[CDCA8]] | +0.78 | +0.71 / +0.80 | both halves | 7e-06 | STRING 472 |
| [[AURKA]] | +0.78 | +0.68 / +0.82 | both halves | 7e-06 |  |
| [[PTTG1]] | +0.78 | +0.72 / +0.79 | both halves | 7e-06 | STRING 403 |
| [[TACC3]] | +0.77 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[KIF2C]] | +0.77 | +0.69 / +0.79 | both halves | 7e-06 | STRING 454 |
| [[KIF18A]] | +0.76 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[TROAP]] | +0.76 | +0.69 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises FAM72A's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without PIMREG | 0.039 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[FAM72B]] | B | FAM72B activity raises FAM72A's level | lines that do not express FAM72B (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FAM72B | 0.089 | ⚠ within organs, on part of the lines; also absent: LINC02798, SRGAP2C, ZNF512B |
| [[CDC20]] | C | CDC20 activity raises FAM72A's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.80× lower at baseline in the lines without CDC20 | 0.067 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises FAM72A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.62× lower at baseline in the lines without AURKB | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises FAM72A's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without CDCA3 | 0.086 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.750). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.0, -58.5); signed map (-52.3, -42.1). **Vector** length 50.6, 7.49% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.59 to 60); *DREAM G2/M down* (control, mean cos +0.70 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.54 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +16.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +3.7 | +16.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | +2.3 | +9.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | +2.1 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.0 | +7.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | -0.0 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +0.8 | +1.7 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +0.8 | +1.5 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +0.7 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +5.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.9 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.9 | -0.1 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | +1.9 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.5 | -3.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.2 | -2.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of UNG2 and MKLN1 interacting yippee protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,186,179-206,204,414 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC57827, RP11-312O7.1, UGENE, LMPIP, p17; previously FAM72A |
| Gene groups (HGNC) | CTLH complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TYM5](https://www.uniprot.org/uniprotkb/Q5TYM5) (Protein FAM72A):

> May play a role in the regulation of cellular reactive oxygen species metabolism. May participate in cell growth regulation.

**Summary**, from NCBI Gene [729533](https://www.ncbi.nlm.nih.gov/gene/729533):

> Predicted to act upstream of or within positive regulation of apoptotic process. Predicted to be located in membrane. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24044](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24044) · Entrez [729533](https://www.ncbi.nlm.nih.gov/gene/729533) · UniProt [Q5TYM5](https://www.uniprot.org/uniprotkb/Q5TYM5) · Ensembl [ENSG00000196550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196550)

## Data

Gene col 12235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12235); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12235]; `tensor/DDL_lfc|DDL_z.npy` [12235]; `embed/gene_vectors.npy` [12235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12235 or target_col == 12235). Every well: [[FAM72A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM72A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
