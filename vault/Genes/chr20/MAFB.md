---
symbol: "MAFB"
type: "gene"
col: 12811
ensembl_id: "ENSG00000204103"
name: "MAF bZIP transcription factor B"
location: "20q12"
module: 98
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 31
n_dd_up: 37
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 6
direction_downstream: 12
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# MAFB

*MAF bZIP transcription factor B* — 20q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.3× (z +23.5, q 0e+00, up in 24 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.0951×, SW1417 0.120×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0198×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0447×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT5]] (+0.66, fdr 1e-05), [[SNAI2]] (+0.65, fdr 7e-06), [[ZFP36L2]] (+0.64, fdr 7e-06); moves opposite to [[NEK4]] (-0.47, fdr 1e-04).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[EFNB2]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZMYND8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.3×** | +23.5 | 0e+00 | 24/24 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **4.85×** | +15.9 | 0e+00 | 20/23 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.46×** | +11.6 | 6e-29 | 1/6 (HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.75×** | +9.4 | 7e-19 | 17/26 (SW480, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.70×** | +9.0 | 4e-17 | 9/19 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.31×** | +8.4 | 3e-15 | 19/26 (SW1417, Panc 03.27, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.99×** | +7.5 | 6e-12 | 13/23 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.84×** | +7.4 | 8e-12 | 6/14 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.78×** | +7.3 | 2e-11 | 13/22 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.86×** | +7.2 | 4e-11 | 13/17 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.78×** | +7.0 | 1e-10 | 15/24 (HS-578T, SW1417, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.64×** | +6.9 | 2e-10 | 19/26 (SW1417, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **2.62×** | +6.9 | 3e-10 | 17/27 (SW1417, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.50×** | +6.0 | 7e-08 | 2/10 (SW480, AsPC-1) | all doses, stronger at high dose | composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.22×** | +5.7 | 5e-07 | 13/23 (HS-578T, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.04×** | +5.0 | 2e-05 | 10/25 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Budesonide (drug)]] 0.05 µM |  | **1.96×** | +4.8 | 6e-05 | 12/24 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +4.6 | 2e-04 | 13/27 (Panc 03.27, NCI-H1573, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.84×** | +4.3 | 4e-04 | 14/25 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.86×** | +4.2 | 6e-04 | 15/23 (HS-578T, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.90×** | +4.2 | 6e-04 | 12/21 (HS-578T, NCI-H1573, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HT-29 0.0951×, SW1417 0.120×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (HT-29 0.0198×; ⚠ toxic; cell-cycle shift, explains ~47% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0447×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.618× | -3.5 | 0.30 | 14/27 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.743× | -3.0 | 0.66 | 13/26 (Panc 03.27, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 21.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.95× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.6× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 36.6 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0198× (z -18.5) ⚠ toxic; cell-cycle shift, explains ~47% of this change |
| [[SW1417 (line)]] | alt | 25.6 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 5.25× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.120× (z -11.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 1.49 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.3× (z +10.4) | — |
| [[J82 (line)]] | alt | 6.76 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +13.9) | — |
| [[SW480 (line)]] | alt | 4.74 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.3× (z +15.1) | — |
| [[A-172 (line)]] | wt | 4.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +12.5) | — |
| [[A549 (line)]] | wt | 1.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 58.5× (z +10.8) | — |
| [[C32 (line)]] | wt | 1.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 56.5× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 4.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +8.5) | — |
| [[LoVo (line)]] | wt | 2.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +12.0) | — |
| [[RPMI-7951 (line)]] | alt | 8.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.69× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.04 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.37× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +9.0) | — |
| [[A-427 (line)]] | wt | 0.406 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.525 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.667 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT5]] | +0.66 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[SNAI2]] | +0.65 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[ZFP36L2]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[IRX3]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[VSTM2L]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FSTL3]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[MT1M]] | +0.63 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[CSNK1D]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DUSP1]] | +0.62 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[KLF9]] | +0.61 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ZFP36L1]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.59 | +0.58 / +0.62 | both halves | 7e-06 | STRING 522 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEK4]] | -0.47 | -0.36 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNB2]] | B | EFNB2 activity raises MAFB's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without EFNB2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[MAOA]] | B | MAOA activity raises MAFB's level | lines that do not express MAOA (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without MAOA | 0.056 | ⚠ within organs, on part of the lines; also absent: OAS1, CKB; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MAFB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises MAFB's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 2.29× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.060 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[NR3C1]] | B | NR3C1 activity raises MAFB's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.7% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[C3]] | C | C3 activity raises MAFB's level | lines that do not express C3 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without C3 | 0.064 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMYND8]] | B | MAFB activity raises ZMYND8's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without MAFB | 0.008 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[ZFAND5]] | B | MAFB activity raises ZFAND5's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.24× lower at baseline in the lines without MAFB | 0.037 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[LINC03036]] | B | MAFB activity lowers LINC03036's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.38× higher at baseline in the lines without MAFB | 0.063 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[CEBPB]] | B | MAFB activity raises CEBPB's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without MAFB | 0.068 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[MAOA]] | B | MAFB activity raises MAOA's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.96× lower at baseline in the lines without MAFB | 0.073 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[ENOX1]] | B | MAFB activity raises ENOX1's level | lines that do not express MAFB (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without MAFB | 0.073 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[B4GALT1]] | B | MAFB activity raises B4GALT1's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without MAFB | 0.073 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[NEK4]] | B | MAFB activity lowers NEK4's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.29× higher at baseline in the lines without MAFB | 0.076 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[ZC3H12A]] | B | MAFB activity raises ZC3H12A's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.87× lower at baseline in the lines without MAFB | 0.080 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[C11orf96]] | B | MAFB activity raises C11orf96's level | lines that do not express MAFB (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without MAFB | 0.089 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG |
| [[ZNF438]] | B | MAFB activity weakens ZNF438's drug response | lines that do not express MAFB (18) vs lines expressing it (30) | the lines without MAFB respond 1.22× as strongly (z diff -0.71); strongest at Doxorubicin (hydrochloride) 5 µM: 0.40x vs 0.58x (z diff -2.9) | 0.094 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG; target measured in part of the lines; artifact flags |
| [[C3]] | C | MAFB activity raises C3's level | lines that do not express MAFB (19) vs lines expressing it (31) | 2.97× lower at baseline in the lines without MAFB | 0.047 | ⚠ within organs, on part of the lines; also absent: LBH, TREM1, IL2RG; co-absent with the target |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 14.0); signed map (16.0, 30.9). **Vector** length 71.4, 17.8% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +15.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +23.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +9.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +8.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.0 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.7 | +5.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.7 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | -1.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | MAF bZIP transcription factor B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q12 — chr20:40,685,848-40,689,236 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KRML |
| Gene groups (HGNC) | Large MAF bZIP transcription factor family |
| Hallmark sets | PANCREAS_BETA_CELLS, KRAS_SIGNALING_UP |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Q3](https://www.uniprot.org/uniprotkb/Q9Y5Q3) (Transcription factor MafB):

> Acts as a transcriptional activator or repressor. Plays a pivotal role in regulating lineage-specific hematopoiesis by repressing ETS1-mediated transcription of erythroid-specific genes in myeloid cells. Required for monocytic, macrophage, osteoclast, podocyte and islet beta cell differentiation. Involved in renal tubule survival and F4/80 maturation. Activates the insulin and glucagon promoters. Together with PAX6, transactivates weakly the glucagon gene promoter through the G1 element. SUMO …

**Summary**, from NCBI Gene [9935](https://www.ncbi.nlm.nih.gov/gene/9935):

> The protein encoded by this gene is a basic leucine zipper (bZIP) transcription factor that plays an important role in the regulation of lineage-specific hematopoiesis. The encoded nuclear protein represses ETS1-mediated transcription of erythroid-specific genes in myeloid cells. This gene contains no introns. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6408](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6408) · Entrez [9935](https://www.ncbi.nlm.nih.gov/gene/9935) · UniProt [Q9Y5Q3](https://www.uniprot.org/uniprotkb/Q9Y5Q3) · Ensembl [ENSG00000204103](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204103)

## Data

Gene col 12811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12811); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12811]; `tensor/DDL_lfc|DDL_z.npy` [12811]; `embed/gene_vectors.npy` [12811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12811 or target_col == 12811). Every well: [[MAFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
