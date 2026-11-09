---
symbol: "SLCO1C1"
type: "gene"
col: 6266
ensembl_id: "ENSG00000139155"
name: "solute carrier organic anion transporter family member 1C1"
location: "12p12.2"
module: 19
arm: "+"
pooled_cpm: 2.58
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SLCO1C1

*solute carrier organic anion transporter family member 1C1* — 12p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.80× (z +11.4, q 3e-27, up in 2 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +10.7, q 4e-24, up in 14 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0298×; ⚠ cell-cycle shift, explains ~36% of this change); [[Budesonide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0335×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDE3A]] (+0.75, fdr 7e-06, ⚠ read-through risk), [[KCNE4]] (+0.69, fdr 7e-06), [[ANO3]] (+0.67, fdr 7e-06), [[PAMR1]] (+0.66, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[PDE3A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CSMD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6266.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.80×** | +11.4 | 3e-27 | 2/7 (NCI-H2347, A498) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +10.7 | 4e-24 | 14/19 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.62×** | +10.6 | 9e-24 | 0/3 | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.62×** | +9.7 | 5e-20 | 0/3 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.52×** | +6.4 | 2e-08 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +5.5 | 4e-06 | 0/11 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.66×** | +5.2 | 2e-05 | 5/23 (LoVo, NCI-H2030, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.92×** | +4.7 | 2e-04 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +4.4 | 8e-04 | 1/15 (Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.3 | 0.001 | 3/22 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.83×** | +3.9 | 0.004 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.8 | 0.006 | 1/9 (CFPAC-1) | top dose only | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.47×** | +3.4 | 0.026 | 3/22 (A498, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.69×** | +3.3 | 0.039 | 1/8 (LoVo) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.039 | 1/7 (LOX-IMVI) | inconsistent across doses | low cells (technical?) |
| [[Oxaprozin (drug)]] 0.05 µM |  | **1.58×** | +3.3 | 0.039 | 1/19 (NCI-H2347) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.042 | 0/14 | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +3.0 | 0.096 | 0/5 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6266.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0298×; ⚠ cell-cycle shift, explains ~36% of this change); [[Budesonide (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0335×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.586× | -3.7 | 0.11 | 11/38 (HCT15, H4, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.634× | -3.3 | 0.26 | 11/38 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6266. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 36.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0298× (z -12.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.0335× (z -8.5) |
| [[A-172 (line)]] | wt | 0.962 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.975 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.937 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.683 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.901 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.694 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.978 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.678 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.815 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.677 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.708 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.663 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.580 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6266), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDE3A]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 | STRING 565; ⚠ **readthrough risk**: this gene lies 6.7 kb 3′ of PDE3A on the same strand (can correlate by spillover, not regulation) |
| [[KCNE4]] | +0.69 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ANO3]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[PAMR1]] | +0.66 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[BAALC]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CDH7]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[BMPER]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LINC01257]] | +0.59 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS6]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PART1]] | +0.58 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC14A2]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[AQP4-AS1]] | +0.57 | +0.49 / +0.54 | both halves | 2e-05 |  |
| [[SPDYE10]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 24, C 0. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3A]] | B | PDE3A activity raises SLCO1C1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without PDE3A | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1 |
| [[GREM2]] | B | GREM2 activity raises SLCO1C1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.41× lower at baseline in the lines without GREM2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[PDGFRB]] | B | PDGFRB activity raises SLCO1C1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.19× lower at baseline in the lines without PDGFRB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[TTTY10]] | B | TTTY10 activity raises SLCO1C1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 1.65× lower at baseline in the lines without TTTY10 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY |
| [[GDNF-AS1]] | B | GDNF-AS1 activity raises SLCO1C1's level | lines that do not express GDNF-AS1 (23) vs lines expressing it (27) | 1.61× lower at baseline in the lines without GDNF-AS1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SDC2, COLEC12, DAAM2; maybe low, not absent |
| [[CDH13]] | B | CDH13 activity raises SLCO1C1's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.08× lower at baseline in the lines without CDH13 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[CCDC120]] | B | CCDC120 activity lowers SLCO1C1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.80× higher at baseline in the lines without CCDC120 | 0.013 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[LINC03000]] | B | LINC03000 activity raises SLCO1C1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.64× lower at baseline in the lines without LINC03000 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[KCNE4]] | B | KCNE4 activity raises SLCO1C1's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 2.02× lower at baseline in the lines without KCNE4 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN |
| [[EPB41L3]] | B | EPB41L3 activity raises SLCO1C1's level | lines that do not express EPB41L3 (34) vs lines expressing it (16) | 1.88× lower at baseline in the lines without EPB41L3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PAX3, ROBO2, PTH2R |
| [[PAPPA]] | B | PAPPA activity raises SLCO1C1's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.04× lower at baseline in the lines without PAPPA | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[GLP2R]] | B | GLP2R activity raises SLCO1C1's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 1.73× lower at baseline in the lines without GLP2R | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CSMD1]] | C | SLCO1C1 activity lowers CSMD1's level | lines that do not express SLCO1C1 (4) vs lines expressing it (46) | 1.90× higher at baseline in the lines without SLCO1C1 | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: GNA14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.6, 21.1); signed map (36.6, 44.0). **Vector** length 37.6, 5.31% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +2.7 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier organic anion transporter family member 1C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.2 — chr12:20,695,332-20,753,386 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OATP-F, OATP1C1, OATP1; previously SLC21A14 |
| Gene groups (HGNC) | Solute carrier organic anion transporter family |
| Reactome | 4 pathways, smallest: Organic anion transport by SLCO transporters; SLC-mediated transport of organic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYB5](https://www.uniprot.org/uniprotkb/Q9NYB5) (Solute carrier organic anion transporter family member 1C1):

> Mediates the Na(+)-independent high affinity transport of organic anions such as the thyroid hormones L-thyroxine (T4), L-thyroxine sulfate (T4S), and 3,3',5'-triiodo-L-thyronine (reverse T3, rT3) at the plasma membrane. Regulates T4 levels in different brain regions by transporting T4, and also by serving as an export pump for T4S, which is a source of T4 after hydrolysis by local sulfatases. Increases the access of these substrates to the intracellular sites where they are metabolized by the …

**Summary**, from NCBI Gene [53919](https://www.ncbi.nlm.nih.gov/gene/53919):

> This gene encodes a member of the organic anion transporter family. The encoded protein is a transmembrane receptor that mediates the sodium-independent uptake of thyroid hormones in brain tissues. This protein has particularly high affinity for the thyroid hormones thyroxine, tri-iodothyronine and reverse tri-iodothyronine. Polymorphisms in the gene encoding this protein may be associated with fatigue and depression in patients suffering from hyperthyroidism. Alternative splicing results in …

**Accessions** — [HGNC:13819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13819) · Entrez [53919](https://www.ncbi.nlm.nih.gov/gene/53919) · UniProt [Q9NYB5](https://www.uniprot.org/uniprotkb/Q9NYB5) · Ensembl [ENSG00000139155](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139155)

## Data

Gene col 6266: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6266); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6266, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6266]; `tensor/DDL_lfc|DDL_z.npy` [6266]; `embed/gene_vectors.npy` [6266]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6266 or target_col == 6266). Every well: [[SLCO1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLCO1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
