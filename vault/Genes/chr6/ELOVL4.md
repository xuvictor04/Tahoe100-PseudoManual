---
symbol: "ELOVL4"
type: "gene"
col: 3985
ensembl_id: "ENSG00000118402"
name: "ELOVL fatty acid elongase 4"
location: "6q14.1"
module: 9
arm: "+"
pooled_cpm: 6.46
n_lines_expressing: 28
n_dd_up: 37
n_dd_down: 1
n_dd_up_clean: 26
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ELOVL4

*ELOVL fatty acid elongase 4* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.72× (z +26.1, q 0e+00, up in 21 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.830× (z -8.7, q 2e-15, down in 12 of 26 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.242×, NCI-H460 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0599×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT11]] (+0.61, fdr 7e-06), [[SSTR2]] (+0.59, fdr 3e-05), [[B3GALT1]] (+0.58, fdr 8e-06); moves opposite to [[NDUFA10]] (-0.47, fdr 2e-04), [[ACO2]] (-0.47, fdr 2e-04), [[PARN]] (-0.45, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.72×** | +26.1 | 0e+00 | 21/23 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **5.29×** | +23.4 | 0e+00 | 25/25 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.90×** | +22.4 | 0e+00 | 25/25 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.79×** | +22.0 | 0e+00 | 25/25 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.01×** | +22.0 | 0e+00 | 24/26 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.59×** | +18.0 | 0e+00 | 25/25 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.08×** | +15.8 | 0e+00 | 23/24 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.77×** | +13.8 | 3e-41 | 19/24 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.58×** | +13.3 | 1e-38 | 21/25 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.45×** | +12.6 | 9e-35 | 22/25 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.10×** | +10.5 | 6e-24 | 19/25 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +9.9 | 2e-21 | 19/26 (NCI-H460, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.20×** | +8.6 | 5e-16 | 19/26 (NCI-H460, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +8.4 | 2e-15 | 12/20 (SNU-423, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +8.1 | 2e-14 | 9/24 (J82, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.75×** | +7.9 | 1e-13 | 15/25 (SNU-423, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +7.5 | 2e-12 | 14/25 (LOX-IMVI, A-427, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SHP-77 0.242×, NCI-H460 0.373×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0599×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.830×** | -8.7 | 2e-15 | 12/26 (NCI-H23, HS-578T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.780× | -3.5 | 0.14 | 8/22 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 27.6 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 8.47 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.84× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 2.82× (z +11.9) | — |
| [[SNU-423 (line)]] | alt | 15.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 6.86 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.78 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.44× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.66× (z +9.4) | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0599× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 5.60 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.2× (z +9.7) | — |
| [[HS-578T (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.9) | — |
| [[J82 (line)]] | alt | 4.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 6.75 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.562 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.638 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.711 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.480 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT11]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[SSTR2]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[B3GALT1]] | +0.58 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[WDR17]] | +0.58 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TMEFF2]] | +0.56 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[HMSD]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SH3GL2]] | +0.54 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[GPR37]] | +0.53 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[SLAIN1]] | +0.53 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[PCDH17]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[INA]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[PRKAR2B]] | +0.51 | +0.48 / +0.56 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA10]] | -0.47 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[ACO2]] | -0.47 | -0.32 / -0.55 | both halves | 2e-04 |  |
| [[PARN]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[MEF2B]] | -0.44 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[NDOR1]] | -0.44 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[VPS51]] | -0.44 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[GANC]] | -0.44 | -0.08 / -0.57 | ⚠ one half (not replicated) | 0.003 |  |
| [[CWF19L1]] | -0.43 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[ERVK13-1]] | -0.43 | -0.09 / -0.52 | ⚠ one half (not replicated) | 0.003 |  |
| [[DZANK1]] | -0.42 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[RECQL5]] | -0.42 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[RABL2A]] | -0.42 | -0.13 / -0.54 | ⚠ one half (not replicated) | 0.002 |  |
| [[RABL2B]] | -0.42 | -0.21 / -0.47 | both halves | 6e-04 |  |
| [[IFT140]] | -0.42 | -0.35 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ELOVL4's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MANSC1]] | B | MANSC1 activity lowers ELOVL4's level | lines that do not express MANSC1 (16) vs lines expressing it (34) | 2.73× higher at baseline in the lines without MANSC1 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[IQGAP2]] | B | IQGAP2 activity lowers ELOVL4's level | lines that do not express IQGAP2 (25) vs lines expressing it (25) | 1.40× higher at baseline in the lines without IQGAP2 | 0.046 | ⚠ within organs, on part of the lines; also absent: KLHL13, KCNQ2, CHD5; maybe low, not absent |
| [[NCAM2]] | C | NCAM2 activity raises ELOVL4's level | lines that do not express NCAM2 (24) vs lines expressing it (26) | 4.47× lower at baseline in the lines without NCAM2 | 0.077 | ⚠ within organs, on part of the lines; also absent: MMP16, ADGRB3, FAP; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.351). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.4, 29.5); signed map (36.6, 29.9). **Vector** length 55.6, 11.6% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +22.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.5 | +13.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +18.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.5 | +15.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +7.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.3 | +8.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.9 | +0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ELOVL fatty acid elongase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:79,914,814-79,947,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CT118; previously STGD2, STGD3, SCA34 |
| Gene groups (HGNC) | ELOVL fatty acid elongase family |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZR5](https://www.uniprot.org/uniprotkb/Q9GZR5) (Very long chain fatty acid elongase 4):

> Catalyzes the first and rate-limiting reaction of the four reactions that constitute the long-chain fatty acids elongation cycle. This endoplasmic reticulum-bound enzymatic process allows the addition of 2 carbons to the chain of long- and very long-chain fatty acids (VLCFAs) per cycle. Condensing enzyme that catalyzes the synthesis of very long chain saturated (VLC-SFA) and polyunsaturated (PUFA) fatty acids that are involved in multiple biological processes as precursors of membrane lipids …

**Summary**, from NCBI Gene [6785](https://www.ncbi.nlm.nih.gov/gene/6785):

> This gene encodes a membrane-bound protein which is a member of the ELO family, proteins which participate in the biosynthesis of fatty acids. Consistent with the expression of the encoded protein in photoreceptor cells of the retina, mutations and small deletions in this gene are associated with Stargardt-like macular dystrophy (STGD3) and autosomal dominant Stargardt-like macular dystrophy (ADMD), also referred to as autosomal dominant atrophic macular degeneration. [provided by RefSeq, Jul …

**Accessions** — [HGNC:14415](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14415) · Entrez [6785](https://www.ncbi.nlm.nih.gov/gene/6785) · UniProt [Q9GZR5](https://www.uniprot.org/uniprotkb/Q9GZR5) · Ensembl [ENSG00000118402](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118402)

## Data

Gene col 3985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3985); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3985]; `tensor/DDL_lfc|DDL_z.npy` [3985]; `embed/gene_vectors.npy` [3985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3985 or target_col == 3985). Every well: [[ELOVL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELOVL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
