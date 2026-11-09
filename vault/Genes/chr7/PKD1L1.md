---
symbol: "PKD1L1"
type: "gene"
col: 8180
ensembl_id: "ENSG00000158683"
name: "polycystin 1 like 1, transient receptor potential channel interacting"
location: "7p12.3"
module: 53
arm: "+"
pooled_cpm: 6.05
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# PKD1L1

*polycystin 1 like 1, transient receptor potential channel interacting* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.36× (z +26.6, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.352× (z -5.2, q 1e-04, down in 14 of 33 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.100×, HOP62 0.0956×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0921×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEB]] (+0.86, fdr 7e-06), [[DNAH10]] (+0.84, fdr 7e-06), [[DNAH12]] (+0.84, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PYROXD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.36×** | +26.6 | 0e+00 | 37/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **12.6×** | +23.9 | 0e+00 | 44/47 (SW480, A-172, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.24×** | +17.3 | 0e+00 | 37/38 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.64×** | +17.2 | 0e+00 | 40/42 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.16×** | +10.8 | 3e-25 | 40/47 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +10.2 | 1e-22 | 6/11 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +9.2 | 3e-18 | 36/47 (SW480, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.46×** | +8.5 | 2e-15 | 34/47 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +8.3 | 4e-15 | 11/16 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.7 | 1e-12 | 22/48 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +7.1 | 6e-11 | 12/23 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +6.2 | 3e-08 | 18/41 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +6.1 | 4e-08 | 23/44 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.84×** | +5.7 | 4e-07 | 25/47 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.84×** | +5.7 | 4e-07 | 22/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.78×** | +5.4 | 2e-06 | 17/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +5.4 | 2e-06 | 21/45 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.77×** | +5.4 | 3e-06 | 18/48 (SW480, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8180.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.100×, HOP62 0.0956×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0921×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.352×** | -5.2 | 1e-04 | 14/33 (RKO, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.686× | -3.6 | 0.10 | 17/47 (NCI-H23, SW480, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.700× | -3.0 | 0.49 | 10/44 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.97 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +17.3) | — |
| [[HOP62 (line)]] | alt | 5.13 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +13.5) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0921× (z -9.2) |
| [[HS-578T (line)]] | alt | 3.76 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +12.1) | — |
| [[NCI-H460 (line)]] | wt | 4.63 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +17.0) | — |
| [[C32 (line)]] | wt | 4.08 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +10.6) | — |
| [[LoVo (line)]] | wt | 4.47 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.3× (z +21.1) | — |
| [[NCI-H1573 (line)]] | alt | 6.76 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.100× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change |
| [[NCI-H23 (line)]] | alt | 13.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 5.88 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.9) | — |
| [[Hs 766T (line)]] | wt | 5.15 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +10.8) | — |
| [[LOX-IMVI (line)]] | wt | 4.73 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 7.85 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +13.3) | — |
| [[NCI-H2347 (line)]] | alt | 4.15 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 8.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +11.3) | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.29× (z +14.5) | — |
| [[A-172 (line)]] | wt | 3.46 | 1 | 0 | [[Auranofin (drug)]] 5 µM 49.5× (z +13.0) | — |
| [[A-427 (line)]] | wt | 5.50 | 1 | 0 | [[Auranofin (drug)]] 5 µM 22.7× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 4.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.4× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 16.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.7× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 2.34 | 1 | 0 | [[Auranofin (drug)]] 5 µM 38.4× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 2.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.21× (z +8.7) | — |
| [[RKO (line)]] | wt | 16.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 4.69 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.65× (z +8.5) | — |
| [[A498 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEB]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.84 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.84 | +0.85 / +0.75 | both halves | 7e-06 |  |
| [[LINC00486]] | +0.81 | +0.88 / +0.63 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.80 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.80 | +0.82 / +0.67 | both halves | 7e-06 |  |
| [[TG]] | +0.79 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[LINC02646]] | +0.79 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[ST8SIA5]] | +0.79 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.78 | +0.78 / +0.65 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.77 | +0.79 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYROXD2]] | B | PYROXD2 activity lowers PKD1L1's level | lines that do not express PYROXD2 (7) vs lines expressing it (43) | 1.86× higher at baseline in the lines without PYROXD2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[LINC01226]] | B | LINC01226 activity lowers PKD1L1's level | lines that do not express LINC01226 (16) vs lines expressing it (34) | 1.56× higher at baseline in the lines without LINC01226 | 0.012 | ⚠ within organs, on part of the lines; also absent: LASTR, TRIM29, ENSG00000287003; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PKD1L1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02456]] | B | LINC02456 activity raises PKD1L1's level | lines that do not express LINC02456 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without LINC02456 | 0.078 | ⚠ within organs, on part of the lines; also absent: GUCY1A2, OLFM2, ZNF610; maybe low, not absent |
| [[ZNF382]] | B | ZNF382 activity raises PKD1L1's level | lines that do not express ZNF382 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without ZNF382 | 0.084 | ⚠ within organs, on part of the lines; also absent: AFF3, DZIP1, MMP16 |
| [[DDR2]] | B | DDR2 activity raises PKD1L1's level | lines that do not express DDR2 (9) vs lines expressing it (41) | 1.65× lower at baseline in the lines without DDR2 | 0.089 | ⚠ within organs, on part of the lines; also absent: PCDH15, CCDC102B, ACOT12; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, -9.6); signed map (22.0, 8.2). **Vector** length 79.1, 14.9% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.2 | +23.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +26.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.2 | +5.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.1 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.7 | -5.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.7 | -0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 1 like 1, transient receptor potential channel interacting |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p12.3 — chr7:47,740,202-47,948,466 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO19563 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDX9](https://www.uniprot.org/uniprotkb/Q8TDX9) (Polycystin-1-like protein 1):

> Component of a calcium-permeant ion channel formed by PKD1L2 and PKD1L1 in primary cilia, where it controls cilium calcium concentration, without affecting cytoplasmic calcium concentration, and regulates sonic hedgehog/SHH signaling and GLI2 transcription. The PKD1L1:PKD2L1 channel complex is mechanosensitive only at high pressures and is highly temperature sensitive. Also involved in left/right axis specification downstream of nodal flow by forming a complex with PKD2 in cilia to facilitate …

**Summary**, from NCBI Gene [168507](https://www.ncbi.nlm.nih.gov/gene/168507):

> This gene encodes a member of the polycystin protein family containing 11 transmembrane domains, a receptor for egg jelly (REJ) domain, and a polycystin-1, lipoxygenase, alpha-toxin (PLAT) domain. The encoded protein may play a role in the male reproductive system. Alternative splice variants have been described but their biological nature has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18053](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18053) · Entrez [168507](https://www.ncbi.nlm.nih.gov/gene/168507) · UniProt [Q8TDX9](https://www.uniprot.org/uniprotkb/Q8TDX9) · Ensembl [ENSG00000158683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158683)

## Data

Gene col 8180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8180); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8180]; `tensor/DDL_lfc|DDL_z.npy` [8180]; `embed/gene_vectors.npy` [8180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8180 or target_col == 8180). Every well: [[PKD1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
