---
symbol: "COL23A1"
type: "gene"
col: 571
ensembl_id: "ENSG00000050767"
name: "collagen type XXIII alpha 1 chain"
location: "5q35.3"
module: 165
arm: "+"
pooled_cpm: 4.27
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# COL23A1

*collagen type XXIII alpha 1 chain* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.89× (z +24.4, q 0e+00, up in 30 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.730× (z -4.0, q 0.034, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0620×, hTERT-HPNE 0.0469×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 0.0677×, PANC-1 0.116×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (H4 0.0159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RYR3]] (+0.73, fdr 7e-06), [[DLGAP2]] (+0.73, fdr 7e-06), [[TMEM132B]] (+0.71, fdr 7e-06).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[COL6A2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.89×** | +24.4 | 0e+00 | 30/36 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.90×** | +19.1 | 0e+00 | 28/38 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.46×** | +15.2 | 0e+00 | 4/6 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.07×** | +13.0 | 1e-36 | 27/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.75×** | +12.9 | 8e-36 | 27/46 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.33×** | +10.7 | 7e-25 | 13/19 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +10.3 | 7e-23 | 24/44 (NCI-H460, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +8.6 | 6e-16 | 3/11 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +8.4 | 4e-15 | 16/47 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +8.3 | 6e-15 | 20/45 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +7.8 | 3e-13 | 17/41 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 8e-10 | 14/43 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.7 | 9e-10 | 9/45 (HEC-1-A, NCI-H23, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +5.6 | 7e-07 | 17/46 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 1e-04 | 10/36 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.004 | 4/40 (KATO III, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.018 | 0/29 | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.021 | 3/43 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 571.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 16 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0620×, hTERT-HPNE 0.0469×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 2 lines (hTERT-HPNE 0.0677×, PANC-1 0.116×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (H4 0.0159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -4.0 | 0.034 | 12/46 (H4, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Pimozide (drug)]] 0.05 µM |  | 0.767× | -3.4 | 0.21 | 11/33 (A549, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | 0.768× | -3.2 | 0.22 | 10/43 (C-33 A, HS-578T, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 0.05 µM |  | 0.768× | -3.1 | 0.26 | 9/42 (A549, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 61.6 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0159× (z -17.1) |
| [[PANC-1 (line)]] | alt | 2.74 | 6 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 20.5× (z +12.7) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.116× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 8.20 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.20× (z +11.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~20% of this change |
| [[HOP62 (line)]] | alt | 6.37 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 37.0× (z +15.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0469× (z -10.4) |
| [[LoVo (line)]] | wt | 2.49 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +12.1) | [[Bexarotene (drug)]] 0.5 µM 0.0567× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 5.39 | 0 | 2 (1 ⚠) | — | [[Methotrexate (drug)]] 0.05 µM 0.0805× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 2.49 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.38× (z +10.4) | — |
| [[SW480 (line)]] | alt | 1.40 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +9.6) | — |
| [[A-427 (line)]] | wt | 5.14 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0986× (z -8.7) |
| [[A498 (line)]] | wt | 1.60 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.45× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 4.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.1× (z +11.9) | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0902× (z -8.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2347 (line)]] | alt | 3.55 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.40× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 5.12 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.84× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 3.07 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.2× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 1.98 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 59.2× (z +9.3) | — |
| [[SW48 (line)]] | wt | 1.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +8.9) | — |
| [[A-172 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYR3]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[TMEM132B]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.70 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[LINC01500]] | +0.69 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[SLC8A1-AS1]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[GPR84-AS1]] | +0.68 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[SAMD14]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ATP8A2]] | +0.67 | +0.52 / +0.73 | both halves | 1e-05 |  |
| [[PAMR1]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[DISP3]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[RYR1]] | +0.65 | +0.47 / +0.72 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL6A2]] | B | COL6A2 activity raises COL23A1's level | lines that do not express COL6A2 (28) vs lines expressing it (22) | 1.99× lower at baseline in the lines without COL6A2 | 0.026 | ⚠ within organs, on part of the lines; also absent: COL6A1, DKK3, ADAMTS2 |
| [[EVC2]] | B | EVC2 activity raises COL23A1's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 2.16× lower at baseline in the lines without EVC2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[DENND2A]] | B | DENND2A activity raises COL23A1's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without DENND2A | 0.055 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent |
| [[FLT1]] | B | FLT1 activity raises COL23A1's level | lines that do not express FLT1 (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without FLT1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF365, COL19A1, PDGFRB |
| [[LINC01950]] | B | LINC01950 activity lowers COL23A1's level | lines that do not express LINC01950 (13) vs lines expressing it (37) | 1.01× higher at baseline in the lines without LINC01950 | 0.094 | ⚠ within organs, on part of the lines; also absent: EFNA5, TLR1, ENSG00000289526; maybe low, not absent |
| [[SSC5D]] | B | SSC5D activity raises COL23A1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without SSC5D | 0.095 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.797). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.6, 31.4); signed map (29.5, 16.6). **Vector** length 66.7, 9.90% of its response variance represented; |z| ≥ 3 in 1,233 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.4 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.4 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +24.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.4 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXIII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,237,476-178,590,393 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434K0621 |
| Gene groups (HGNC) | Membrane associated collagens with interrupted triple helices |
| Reactome | 7 pathways, smallest: Collagen chain trimerization; Collagen degradation; Collagen biosynthesis and modifying enzymes |
| Matched by | ensembl_id |

UniProt [Q86Y22](https://www.uniprot.org/uniprotkb/Q86Y22) carries no function annotation.

**Summary**, from NCBI Gene [91522](https://www.ncbi.nlm.nih.gov/gene/91522):

> COL23A1 is a member of the transmembrane collagens, a subfamily of the nonfibrillar collagens that contain a single pass hydrophobic transmembrane domain (Banyard et al., 2003 [PubMed 12644459]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:22990](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22990) · Entrez [91522](https://www.ncbi.nlm.nih.gov/gene/91522) · UniProt [Q86Y22](https://www.uniprot.org/uniprotkb/Q86Y22) · Ensembl [ENSG00000050767](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050767)

## Data

Gene col 571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 571); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 571]; `tensor/DDL_lfc|DDL_z.npy` [571]; `embed/gene_vectors.npy` [571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 571 or target_col == 571). Every well: [[COL23A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL23A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
