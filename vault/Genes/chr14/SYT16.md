---
symbol: "SYT16"
type: "gene"
col: 6360
ensembl_id: "ENSG00000139973"
name: "synaptotagmin 16"
location: "14q23.2"
module: 53
arm: "+"
pooled_cpm: 3.26
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 32
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SYT16

*synaptotagmin 16* — 14q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 14.8× (z +33.5, q 0e+00, up in 30 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0658×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00393]] (+0.83, fdr 7e-06), [[LINC02955]] (+0.83, fdr 7e-06), [[FER1L6]] (+0.78, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[C12orf50]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6360.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **14.8×** | +33.5 | 0e+00 | 30/31 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **12.1×** | +31.0 | 0e+00 | 32/33 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **8.10×** | +17.7 | 0e+00 | 20/26 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.99×** | +17.1 | 0e+00 | 30/33 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.70×** | +16.1 | 0e+00 | 30/34 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +11.3 | 2e-27 | 3/7 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.61×** | +11.3 | 2e-27 | 27/40 (SW480, NCI-H23, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.35×** | +10.6 | 2e-24 | 31/44 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.24×** | +10.0 | 9e-22 | 18/45 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.15×** | +9.3 | 7e-19 | 4/10 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.95×** | +9.1 | 3e-18 | 9/20 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.79×** | +9.0 | 9e-18 | 29/41 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +8.0 | 4e-14 | 4/17 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.39×** | +7.7 | 4e-13 | 20/34 (NCI-H460, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +7.3 | 1e-11 | 15/44 (CFPAC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.25×** | +7.1 | 4e-11 | 18/45 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.58×** | +5.8 | 2e-07 | 10/27 (NCI-H460, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.92×** | +5.5 | 1e-06 | 17/37 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.84×** | +5.4 | 2e-06 | 13/38 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6360.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (hTERT-HPNE 0.0658×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.707× | -3.0 | 0.68 | 2/44 (A549, SW48) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6360. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 7.15 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.2× (z +12.0) | — |
| [[A498 (line)]] | wt | 3.71 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.4× (z +18.7) | — |
| [[HOP62 (line)]] | alt | 1.75 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.4× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 3.21 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 103× (z +17.7) | — |
| [[SW 900 (line)]] | alt | 6.82 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +12.1) | — |
| [[C32 (line)]] | wt | 1.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.2× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +13.1) | — |
| [[NCI-H2030 (line)]] | alt | 8.06 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.8× (z +13.5) | — |
| [[PANC-1 (line)]] | alt | 1.99 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.2× (z +11.9) | — |
| [[RPMI-7951 (line)]] | alt | 9.35 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.4× (z +11.8) | — |
| [[A-172 (line)]] | wt | 1.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 34.6× (z +10.1) | — |
| [[A549 (line)]] | wt | 1.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +8.8) | — |
| [[C-33 A (line)]] | alt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 95.0× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 5.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0658× (z -9.3) |
| [[J82 (line)]] | alt | 3.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.38× (z +8.6) | — |
| [[LoVo (line)]] | wt | 1.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.0× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.4× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 47.1× (z +12.2) | — |
| [[SNU-423 (line)]] | alt | 9.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +13.8) | — |
| [[SW1417 (line)]] | alt | 0.990 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.4× (z +9.1) | — |
| [[A-427 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.823 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.880 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.928 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6360), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | +0.83 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.83 | +0.84 / +0.73 | both halves | 7e-06 |  |
| [[FER1L6]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[NEB]] | +0.77 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[LINC00880]] | +0.76 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[ELAPOR1]] | +0.76 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.75 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[SLC4A10]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.75 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[RELN]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[BTG3-AS1]] | +0.74 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R36]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C12orf50]] | B | C12orf50 activity raises SYT16's level | lines that do not express C12orf50 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without C12orf50 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195, LYPLAL1-AS1, ENSG00000237153; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SYT16's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02932]] | B | LINC02932 activity raises SYT16's level | lines that do not express LINC02932 (5) vs lines expressing it (45) | 1.72× lower at baseline in the lines without LINC02932 | 0.060 | ⚠ within organs, on part of the lines; also absent: RBFOX1, DNAH6, ESRRB; maybe low, not absent; its own permutation p |
| [[PAMR1]] | B | PAMR1 activity raises SYT16's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without PAMR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[ZFPM2]] | B | ZFPM2 activity raises SYT16's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without ZFPM2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[SLC2A14]] | B | SLC2A14 activity raises SYT16's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 1.87× lower at baseline in the lines without SLC2A14 | 0.089 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.5, -10.8); signed map (23.6, 9.9). **Vector** length 68.2, 11.1% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +33.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +31.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.2 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +11.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.9 | +10.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.3 | +5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.8 | +3.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | synaptotagmin 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.2 — chr14:61,811,974-62,112,550 (+) |
| Ensembl biotype | protein_coding |
| Also known as | yt14r, CHR14SYT, Strep14; previously SYT14L |
| Gene groups (HGNC) | Synaptotagmins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q17RD7](https://www.uniprot.org/uniprotkb/Q17RD7) (Synaptotagmin-16):

> May be involved in the trafficking and exocytosis of secretory vesicles in non-neuronal tissues. Is Ca(2+)-independent.

**Summary**, from NCBI Gene [83851](https://www.ncbi.nlm.nih.gov/gene/83851):

> Predicted to enable phospholipid binding activity. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23142) · Entrez [83851](https://www.ncbi.nlm.nih.gov/gene/83851) · UniProt [Q17RD7](https://www.uniprot.org/uniprotkb/Q17RD7) · Ensembl [ENSG00000139973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139973)

## Data

Gene col 6360: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6360); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6360, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6360]; `tensor/DDL_lfc|DDL_z.npy` [6360]; `embed/gene_vectors.npy` [6360]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6360 or target_col == 6360). Every well: [[SYT16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYT16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
