---
symbol: "SLC4A11"
type: "gene"
col: 1548
ensembl_id: "ENSG00000088836"
name: "solute carrier family 4 member 11"
location: "20p13"
module: 19
arm: "+"
pooled_cpm: 2.01
n_lines_expressing: 44
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLC4A11

*solute carrier family 4 member 11* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.83× (z +12.4, q 2e-32, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.57× (z +10.9, q 4e-25, up in 10 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.563× (z -4.7, q 0.001, down in 11 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.136×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.138×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABBR2]] (+0.60, fdr 2e-05), [[SCARA5]] (+0.54, fdr 8e-05), [[MMP15]] (+0.54, fdr 2e-05); moves opposite to [[SNX16]] (-0.41, fdr 7e-04), [[EIF1AY]] (-0.41, fdr 2e-04), [[PPP4R3B]] (-0.39, fdr 4e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LAMA5]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FZD4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.83×** | +12.4 | 2e-32 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +10.9 | 4e-25 | 10/18 (A549, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.55×** | +10.4 | 8e-23 | 24/37 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.45×** | +10.1 | 7e-22 | 2/5 (PANC-1, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.58×** | +9.6 | 7e-20 | 1/2 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.87×** | +8.6 | 7e-16 | 22/33 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +7.2 | 5e-11 | 19/34 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +5.2 | 1e-05 | 1/11 (Hs 766T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +4.8 | 1e-04 | 10/37 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.72×** | +4.3 | 0.001 | 2/6 (LS 180, SHP-77) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.66×** | +4.1 | 0.002 | 6/37 (A549, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.003 | 2/35 (HepG2/C3A, SHP-77) | top dose only | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Saquinavir (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.005 | 2/16 (HEC-1-A, SHP-77) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.009 | 2/14 (LoVo, PANC-1) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 4/34 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.009 | 4/34 (A-172, SW480, …) | inconsistent across doses | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.58×** | +3.5 | 0.018 | 2/12 (A-427, NCI-H460) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.032 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +3.1 | 0.060 | 0/27 | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.0 | 0.071 | 1/13 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Finasteride (drug)]] 5 µM |  | **1.46×** | +2.9 | 0.081 | 1/29 (NCI-H2347) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1548.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H460 0.136×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.138×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.563×** | -4.7 | 0.001 | 11/27 (LS 180, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.659× | -3.4 | 0.16 | 6/37 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.667× | -3.3 | 0.16 | 10/29 (LoVo, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 2 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.136× (z -9.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.138× (z -9.1) |
| [[A-172 (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.676 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.607 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.717 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.728 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.596 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.722 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.521 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.628 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.783 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.671 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.762 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABBR2]] | +0.60 | +0.56 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[SCARA5]] | +0.54 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[MMP15]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[SERPINB11]] | +0.53 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[PAX7]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ZG16B]] | +0.51 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[DPP10]] | +0.51 | +0.52 / +0.39 | both halves | 6e-05 |  |
| [[CBX2]] | +0.50 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[FZD4]] | +0.50 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[DDIT4L]] | +0.49 | +0.54 / +0.32 | both halves | 2e-04 |  |
| [[PHETA1]] | +0.49 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[CHL1]] | +0.49 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX16]] | -0.41 | -0.34 / -0.20 | both halves | 7e-04 |  |
| [[EIF1AY]] | -0.41 | -0.38 / -0.29 | both halves | 2e-04 |  |
| [[PPP4R3B]] | -0.39 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[GTF2H1]] | -0.39 | -0.20 / -0.39 | ⚠ not reproduced | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA5]] | B | LAMA5 activity raises SLC4A11's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.63× lower at baseline in the lines without LAMA5 | 0.067 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |
| [[NRCAM]] | B | NRCAM activity raises SLC4A11's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 1.34× lower at baseline in the lines without NRCAM | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG |
| [[UNC13A]] | B | UNC13A activity raises SLC4A11's level | lines that do not express UNC13A (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without UNC13A | 0.082 | ⚠ within organs, on part of the lines; also absent: CDH19, LINC02864, SCG3; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD4]] | C | SLC4A11's natural level weakens FZD4's drug response | SLC4A11's natural level across 35 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.49; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.436). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.8, 37.5); signed map (44.0, 45.9). **Vector** length 37.3, 4.60% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +10.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +0.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,227,417-3,239,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ794I6.2, BTR1, NaBC1, FECD4; previously CHED2, CDPD1 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBS3](https://www.uniprot.org/uniprotkb/Q8NBS3) (Solute carrier family 4 member 11):

> Multifunctional transporter with an impact in cell morphology and differentiation. In the presence of borate B(OH)4(-), acts as a voltage-dependent electrogenic Na(+)-coupled B(OH)4(-) cotransporter controlling boron homeostasis. At early stages of stem cell differentiation, participates in synergy with ITGA5-ITGB1 and ITGAV-ITGB3 integrins and BMPR1A to promote cell adhesion and contractility that drives differentiation toward osteogenic commitment while inhibiting adipogenesis (By …

**Summary**, from NCBI Gene [83959](https://www.ncbi.nlm.nih.gov/gene/83959):

> This gene encodes a voltage-regulated, electrogenic sodium-coupled borate cotransporter that is essential for borate homeostasis, cell growth and cell proliferation. Mutations in this gene have been associated with a number of endothelial corneal dystrophies including recessive corneal endothelial dystrophy 2, corneal dystrophy and perceptive deafness, and Fuchs endothelial corneal dystrophy. Multiple transcript variants encoding different isoforms have been described. [provided by RefSeq, Mar …

**Accessions** — [HGNC:16438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16438) · Entrez [83959](https://www.ncbi.nlm.nih.gov/gene/83959) · UniProt [Q8NBS3](https://www.uniprot.org/uniprotkb/Q8NBS3) · Ensembl [ENSG00000088836](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088836)

## Data

Gene col 1548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1548); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1548]; `tensor/DDL_lfc|DDL_z.npy` [1548]; `embed/gene_vectors.npy` [1548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1548 or target_col == 1548). Every well: [[SLC4A11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
