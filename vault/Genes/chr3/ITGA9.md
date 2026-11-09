---
symbol: "ITGA9"
type: "gene"
col: 6912
ensembl_id: "ENSG00000144668"
name: "integrin subunit alpha 9"
location: "3p22.2"
module: 53
arm: "+"
pooled_cpm: 5.77
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# ITGA9

*integrin subunit alpha 9* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.81× (z +24.5, q 0e+00, up in 33 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (C32 0.153×, LoVo 0.269×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0691×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.0809×); [[Silodosin (drug)]] 5 µM in 1 line (SW480 0.0804×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.281×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP50]] (+0.78, fdr 7e-06), [[PEBP4]] (+0.76, fdr 7e-06), [[ALDH8A1]] (+0.76, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6912.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.81×** | +24.5 | 0e+00 | 33/36 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.26×** | +15.0 | 0e+00 | 37/42 (A-172, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +13.7 | 4e-40 | 31/37 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.11×** | +10.3 | 1e-22 | 21/35 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +7.9 | 4e-13 | 3/7 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +7.3 | 2e-11 | 10/22 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +6.5 | 6e-09 | 3/7 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +5.1 | 3e-05 | 10/44 (C-33 A, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +4.9 | 7e-05 | 17/43 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.8 | 1e-04 | 10/33 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.4 | 6e-04 | 14/34 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +4.2 | 0.001 | 10/45 (RPMI-7951, SW 900, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.61×** | +4.1 | 0.002 | 11/41 (A-172, A549, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.003 | 9/44 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.8 | 0.006 | 5/26 (NCI-H460, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.028 | 6/45 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.058 | 12/43 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.92×** | +3.1 | 0.066 | 0/43 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.069 | 6/43 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6912.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 11 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 2 lines (C32 0.153×, LoVo 0.269×; ⚠ cell-cycle shift, would explain all of this change); [[Ixazomib citrate (drug)]] 5 µM in 1 line (C32 0.0691×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (C32 0.0809×); [[Silodosin (drug)]] 5 µM in 1 line (SW480 0.0804×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.281×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.680× | -3.5 | 0.12 | 13/45 (C32, RPMI-7951, …) | rises with dose | composition shift |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.673× | -3.5 | 0.12 | 10/41 (HepG2/C3A, C-33 A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | 0.492× | -3.4 | 0.12 | 13/32 (HT-29, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.678× | -3.3 | 0.12 | 9/39 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.784× | -3.1 | 0.19 | 9/43 (SK-MEL-2, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6912. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 66.8 | 0 | 10 (9 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0691× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0809× (z -13.1) |
| [[LoVo (line)]] | wt | 32.2 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +19.2) | [[Belinostat (drug)]] 5 µM 0.213× (z -10.6) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -8.7) |
| [[A-172 (line)]] | wt | 2.46 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +16.4) | — |
| [[SW480 (line)]] | alt | 2.38 | 1 | 1 | [[Auranofin (drug)]] 5 µM 10.6× (z +8.6) | [[Silodosin (drug)]] 5 µM 0.0804× (z -8.9) |
| [[HCT15 (line)]] | alt | 8.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.3× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.14× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 2.91 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +11.6) | — |
| [[hTERT-HPNE (line)]] | wt | 8.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.0× (z +10.3) | — |
| [[J82 (line)]] | alt | 2.65 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 3.11 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 4.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0727× (z -9.0) ⚠ toxic; unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 5.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 3.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +11.2) | — |
| [[A-427 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6912), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP50]] | +0.78 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.76 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.75 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[PKD1L1]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.73 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.73 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[NEB]] | +0.72 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.72 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.72 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SLC8A2]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITGA9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RMEL3]] | B | RMEL3 activity raises ITGA9's level | lines that do not express RMEL3 (26) vs lines expressing it (24) | 1.70× lower at baseline in the lines without RMEL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC00698, COL19A1, AEBP1; maybe low, not absent |
| [[DDR2]] | B | DDR2 activity raises ITGA9's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without DDR2 | 0.058 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |
| [[ABCA6]] | B | ABCA6 activity raises ITGA9's level | lines that do not express ABCA6 (26) vs lines expressing it (24) | 1.47× lower at baseline in the lines without ABCA6 | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC02154, IGF2, LYPLAL1-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.3, -9.5); signed map (21.5, 7.3). **Vector** length 81.8, 14.7% of its response variance represented; |z| ≥ 3 in 1,162 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.9 | +15.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +24.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +10.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +4.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -3.6 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.5 | -3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.5 | -3.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:37,452,115-37,823,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RLC, ITGA4L, ALPHA-RLC |
| Gene groups (HGNC) | Integrin alpha subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: Signal transduction by L1; ECM proteoglycans; Integrin cell surface interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13797](https://www.uniprot.org/uniprotkb/Q13797) (Integrin alpha-9):

> Integrin alpha-9/beta-1 (ITGA9:ITGB1) is a receptor for VCAM1, cytotactin and osteopontin. It recognizes the sequence A-E-I-D-G-I-E-L in cytotactin. ITGA9:ITGB1 may play a crucial role in SVEP1/polydom-mediated myoblast cell adhesion (By similarity). Integrin ITGA9:ITGB1 represses PRKCA-mediated L-type voltage-gated channel Ca(2+) influx and ROCK-mediated calcium sensitivity in vascular smooth muscle cells via its interaction with SVEP1, thereby inhibiting vasocontraction.

**Summary**, from NCBI Gene [3680](https://www.ncbi.nlm.nih.gov/gene/3680):

> This gene encodes an alpha integrin. Integrins are heterodimeric integral membrane glycoproteins composed of an alpha chain and a beta chain that mediate cell-cell and cell-matrix adhesion. The protein encoded by this gene, when bound to the beta 1 chain, forms an integrin that is a receptor for VCAM1, cytotactin and osteopontin. Expression of this gene has been found to be upregulated in small cell lung cancers. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6145) · Entrez [3680](https://www.ncbi.nlm.nih.gov/gene/3680) · UniProt [Q13797](https://www.uniprot.org/uniprotkb/Q13797) · Ensembl [ENSG00000144668](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144668)

## Data

Gene col 6912: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6912); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6912, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6912]; `tensor/DDL_lfc|DDL_z.npy` [6912]; `embed/gene_vectors.npy` [6912]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6912 or target_col == 6912). Every well: [[ITGA9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
