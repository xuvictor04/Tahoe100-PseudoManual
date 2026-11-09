---
symbol: "PLCL1"
type: "gene"
col: 3733
ensembl_id: "ENSG00000115896"
name: "phospholipase C like 1 (inactive)"
location: "2q33.1"
module: 61
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 50
n_dd_up: 45
n_dd_down: 0
n_dd_up_clean: 38
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PLCL1

*phospholipase C like 1 (inactive)* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.22× (z +29.5, q 0e+00, up in 33 of 37 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.108×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEFF2]] (+0.69, fdr 7e-06), [[SGCZ]] (+0.68, fdr 7e-06), [[HULC]] (+0.68, fdr 7e-06); moves opposite to [[GLMN]] (-0.53, fdr 4e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC00457]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3733.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.22×** | +29.5 | 0e+00 | 33/37 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **16.2×** | +29.4 | 0e+00 | 42/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.85×** | +28.7 | 0e+00 | 32/36 (A498, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **13.1×** | +27.2 | 0e+00 | 38/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **10.7×** | +25.0 | 0e+00 | 39/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **7.04×** | +20.6 | 0e+00 | 36/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.52×** | +18.8 | 0e+00 | 41/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.93×** | +14.5 | 1e-45 | 32/42 (A-172, BT-474, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.33×** | +12.7 | 4e-35 | 35/42 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.28×** | +12.5 | 3e-34 | 23/34 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +11.8 | 3e-30 | 4/7 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **7.99×** | +11.5 | 8e-29 | 32/42 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +11.3 | 4e-28 | 22/34 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.5 | 8e-20 | 9/23 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.43×** | +9.4 | 3e-19 | 26/40 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.78×** | +8.6 | 2e-16 | 20/46 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +8.1 | 1e-14 | 21/41 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 0.108×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.803× | -3.3 | 0.55 | 10/44 (MIA PaCa-2, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.05 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 31.1× (z +14.6) | — |
| [[SW480 (line)]] | alt | 3.64 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +15.0) | — |
| [[A-172 (line)]] | wt | 4.69 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +14.9) | — |
| [[A498 (line)]] | wt | 2.18 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 2.39 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.4× (z +15.6) | — |
| [[LoVo (line)]] | wt | 4.29 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 2.97 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.9× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 2.29 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 76.1× (z +11.1) | — |
| [[J82 (line)]] | alt | 9.53 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.80× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 5.98 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.1× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 1.58 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 89.1× (z +13.3) | — |
| [[A-427 (line)]] | wt | 1.50 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 83.4× (z +9.6) | — |
| [[C32 (line)]] | wt | 7.51 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.2× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 3.00 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 44.2× (z +10.3) | — |
| [[BT-474 (line)]] | alt | 6.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 3.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +9.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.06 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.2× (z +9.7) | — |
| [[A549 (line)]] | wt | 3.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 1.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.9× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 2.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 3.61 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 21.1× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 6.04 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 1.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 19.2× (z +9.4) | — |
| [[AN3 CA (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEFF2]] | +0.69 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.68 | +0.66 / +0.75 | both halves | 7e-06 |  |
| [[HULC]] | +0.68 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[MIR325HG]] | +0.67 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.66 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[CNTN4]] | +0.65 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.65 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[GPM6A]] | +0.65 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[LUZP2]] | +0.64 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.64 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[SLC9C1]] | +0.64 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[XKR4]] | +0.64 | +0.65 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMN]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00457]] | B | LINC00457 activity raises PLCL1's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without LINC00457 | 6e-04 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[KCND3]] | B | KCND3 activity raises PLCL1's level | lines that do not express KCND3 (21) vs lines expressing it (29) | 1.24× lower at baseline in the lines without KCND3 | 0.039 | ⚠ within organs, on part of the lines; also absent: TAFA5, LINC01257, ENSG00000259692; maybe low, not absent |
| [[PCSK2]] | B | PCSK2 activity raises PLCL1's level | lines that do not express PCSK2 (27) vs lines expressing it (23) | 1.60× lower at baseline in the lines without PCSK2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PGR, UNC5D, PDE3A; maybe low, not absent |
| [[TP63]] | B | TP63 activity raises PLCL1's level | lines that do not express TP63 (39) vs lines expressing it (11) | 1.68× lower at baseline in the lines without TP63 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, ENSG00000241168, TYR |
| [[TOP2A]] | B | TOP2A activity lowers PLCL1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[UNC80]] | B | UNC80 activity raises PLCL1's level | lines that do not express UNC80 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without UNC80 | 0.081 | ⚠ within organs, on part of the lines; also absent: PPFIA2, GAS7, COP1-DT; maybe low, not absent |
| [[LYPD1]] | B | LYPD1 activity raises PLCL1's level | lines that do not express LYPD1 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without LYPD1 | 0.092 | ⚠ within organs, on part of the lines; also absent: SETBP1, FRMPD4, NCKAP5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 30.4); signed map (33.3, 17.5). **Vector** length 62.3, 10.2% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.8 | +18.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +8.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase C like 1 (inactive) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,804,593-198,572,581 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLC-L, PLCL, PRIP, PPP1R127; previously PLCE |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; C2 domain containing phospholipases |
| Hallmark sets | UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15111](https://www.uniprot.org/uniprotkb/Q15111) (Inactive phospholipase C-like protein 1):

> Involved in an inositol phospholipid-based intracellular signaling cascade. Shows no PLC activity to phosphatidylinositol 4,5-bisphosphate and phosphatidylinositol. Component in the phospho-dependent endocytosis process of GABA A receptor (By similarity). Regulates the turnover of receptors and thus contributes to the maintenance of GABA-mediated synaptic inhibition. Its aberrant expression could contribute to the genesis and progression of lung carcinoma. Acts as an inhibitor of PPP1C.

**Summary**, from NCBI Gene [5334](https://www.ncbi.nlm.nih.gov/gene/5334):

> Predicted to enable GABA receptor binding activity and phosphatidylinositol-4,5-bisphosphate phospholipase C activity. Predicted to be involved in several processes, including gamma-aminobutyric acid signaling pathway; negative regulation of cold-induced thermogenesis; and phosphatidylinositol-mediated signaling. Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9063](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9063) · Entrez [5334](https://www.ncbi.nlm.nih.gov/gene/5334) · UniProt [Q15111](https://www.uniprot.org/uniprotkb/Q15111) · Ensembl [ENSG00000115896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115896)

## Data

Gene col 3733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3733); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3733]; `tensor/DDL_lfc|DDL_z.npy` [3733]; `embed/gene_vectors.npy` [3733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3733 or target_col == 3733). Every well: [[PLCL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLCL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
