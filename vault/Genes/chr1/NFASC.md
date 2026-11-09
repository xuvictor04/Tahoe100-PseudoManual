---
symbol: "NFASC"
type: "gene"
col: 8711
ensembl_id: "ENSG00000163531"
name: "neurofascin"
location: "1q32.1"
module: 82
arm: "+"
pooled_cpm: 11.78
n_lines_expressing: 23
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 20
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# NFASC

*neurofascin* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.92× (z +20.6, q 0e+00, up in 19 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.687× (z -5.1, q 2e-04, down in 10 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RPMI-7951 0.278×, NCI-H23 0.291×, A-172 0.414×, SHP-77 0.375×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.0692×, A-427 0.102×, RPMI-7951 0.0778×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (C-33 A 0.0712×, RPMI-7951 0.168×, NCI-H23 0.199×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.204×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTNNA2]] (+0.60, fdr 3e-05), [[DISC1FP1]] (+0.59, fdr 1e-05), [[SOGA3]] (+0.57, fdr 2e-05).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[DISC1FP1]] → it (grade C ⚠); 20 go from it, the strongest it → [[SRRM3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +20.6 | 0e+00 | 19/21 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +17.8 | 0e+00 | 4/20 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.77×** | +13.9 | 1e-41 | 17/21 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.64×** | +13.2 | 8e-38 | 14/21 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +12.9 | 4e-36 | 3/18 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +12.8 | 1e-35 | 3/9 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.50×** | +12.5 | 7e-34 | 15/19 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +12.4 | 1e-33 | 14/21 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.46×** | +12.2 | 1e-32 | 19/21 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.6 | 2e-12 | 2/11 (H4, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.89×** | +7.6 | 2e-12 | 14/21 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 7e-10 | 9/18 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 7e-07 | 2/20 (PANC-1, A-427) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +5.6 | 7e-07 | 7/20 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +5.2 | 9e-06 | 8/18 (H4, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +5.0 | 2e-05 | 9/21 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 3e-05 | 9/21 (H4, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.001 | 3/21 (C32, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8711.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (RPMI-7951 0.278×, NCI-H23 0.291×, A-172 0.414×, SHP-77 0.375×, …); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.0692×, A-427 0.102×, RPMI-7951 0.0778×; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (C-33 A 0.0712×, RPMI-7951 0.168×, NCI-H23 0.199×; ⚠ toxic; cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.687×** | -5.1 | 2e-04 | 10/19 (PANC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.779× | -3.4 | 0.18 | 6/21 (PANC-1, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.47 | 6 | 1 | [[Tucidinostat (drug)]] 5 µM 4.71× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.8) |
| [[A-172 (line)]] | wt | 171 | 2 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 58.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0778× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -12.6) |
| [[C-33 A (line)]] | alt | 63.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0692× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 32.7 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.9) |
| [[A-427 (line)]] | wt | 52.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -18.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 22.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.1× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 4.46 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.4× (z +8.8) | — |
| [[C32 (line)]] | wt | 6.21 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.7× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.93× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 57.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -11.1) |
| [[SW1417 (line)]] | alt | 5.69 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.97× (z +9.6) | — |
| [[SW480 (line)]] | alt | 3.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.35× (z +13.0) | — |
| [[A498 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.863 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNA2]] | +0.60 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[DISC1FP1]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SOGA3]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[SYT14]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LRCH2]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[MAP6]] | +0.56 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[KIF1A]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[REEP1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SCN8A]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 | pathway: Interaction between L1 and Ankyrins; STRING 888 |
| [[TBC1D19]] | +0.54 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[FAM110B]] | +0.54 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[DPYSL5]] | +0.54 | +0.38 / +0.58 | both halves | 7e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DISC1FP1]] | C | DISC1FP1 activity raises NFASC's level | lines that do not express DISC1FP1 (29) vs lines expressing it (21) | 2.94× lower at baseline in the lines without DISC1FP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: FSTL5, ENSG00000250954, ENSG00000251574; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises NFASC's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.93× lower at baseline in the lines without SLC6A17 | 0.011 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[FSD1]] | C | FSD1 activity raises NFASC's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 3.50× lower at baseline in the lines without FSD1 | 0.016 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2; co-absent with the target |
| [[SCN8A]] | C | SCN8A activity raises NFASC's level | lines that do not express SCN8A (18) vs lines expressing it (32) | 2.95× lower at baseline in the lines without SCN8A | 0.024 | ⚠ within organs, on part of the lines; also absent: DPYSL5, PDZD4, STOX2; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises NFASC's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.27× lower at baseline in the lines without KIF1A | 0.030 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[SYT11]] | C | SYT11 activity raises NFASC's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.62× lower at baseline in the lines without SYT11 | 0.033 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[RET]] | C | RET activity raises NFASC's level | lines that do not express RET (28) vs lines expressing it (22) | 3.71× lower at baseline in the lines without RET | 0.037 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises NFASC's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 3.23× lower at baseline in the lines without FSTL5 | 0.038 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[RAB39A]] | C | RAB39A activity raises NFASC's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 3.32× lower at baseline in the lines without RAB39A | 0.061 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises NFASC's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 3.35× lower at baseline in the lines without DPYSL5 | 0.067 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[POTEF]] | C | POTEF activity raises NFASC's level | lines that do not express POTEF (29) vs lines expressing it (21) | 1.73× lower at baseline in the lines without POTEF | 0.068 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises NFASC's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.05× lower at baseline in the lines without JAKMIP1 | 0.086 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 6, C 14. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | NFASC activity raises SRRM3's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[CACNA2D2]] | B | NFASC activity raises CACNA2D2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.17× lower at baseline in the lines without NFASC | 0.004 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[PKIG]] | B | NFASC activity raises PKIG's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without NFASC | 0.008 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[EPHA10]] | B | NFASC activity raises EPHA10's level | lines that do not express NFASC (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without NFASC | 0.056 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[ATP1A3]] | B | NFASC activity raises ATP1A3's level | lines that do not express NFASC (27) vs lines expressing it (23) | 1.62× lower at baseline in the lines without NFASC | 0.056 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[SYN2]] | B | NFASC activity raises SYN2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without NFASC | 0.097 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[DPYSL5]] | C | NFASC activity raises DPYSL5's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.04× lower at baseline in the lines without NFASC | 0.001 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[RAB39A]] | C | NFASC activity raises RAB39A's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[MYT1]] | C | NFASC activity raises MYT1's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.28× lower at baseline in the lines without NFASC | 0.003 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[KIF1A]] | C | NFASC activity raises KIF1A's level | lines that do not express NFASC (27) vs lines expressing it (23) | 4.85× lower at baseline in the lines without NFASC | 0.006 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[KCNQ2]] | C | NFASC activity raises KCNQ2's level | lines that do not express NFASC (27) vs lines expressing it (23) | 2.41× lower at baseline in the lines without NFASC | 0.007 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[SYT11]] | C | NFASC activity raises SYT11's level | lines that do not express NFASC (27) vs lines expressing it (23) | 3.38× lower at baseline in the lines without NFASC | 0.009 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.4, 36.6); signed map (29.7, 28.9). **Vector** length 51.2, 11.5% of its response variance represented; |z| ≥ 3 in 559 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +20.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +4.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -1.5 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -0.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -0.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | neurofascin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,828,651-205,022,822 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NRCAML, KIAA0756, FLJ46866, NF |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 7 pathways, smallest: Neurofascin interactions; Interaction between L1 and Ankyrins; L1CAM interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [O94856](https://www.uniprot.org/uniprotkb/O94856) (Neurofascin):

> Cell adhesion, ankyrin-binding protein which may be involved in neurite extension, axonal guidance, synaptogenesis, myelination and neuron-glial cell interactions.

**Summary**, from NCBI Gene [23114](https://www.ncbi.nlm.nih.gov/gene/23114):

> This gene encodes an L1 family immunoglobulin cell adhesion molecule with multiple IGcam and fibronectin domains. The protein functions in neurite outgrowth, neurite fasciculation, and organization of the axon initial segment (AIS) and nodes of Ranvier on axons during early development. Both the AIS and nodes of Ranvier contain high densities of voltage-gated Na+ (Nav) channels which are clustered by interactions with cytoskeletal and scaffolding proteins including this protein, gliomedin, …

**Accessions** — [HGNC:29866](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29866) · Entrez [23114](https://www.ncbi.nlm.nih.gov/gene/23114) · UniProt [O94856](https://www.uniprot.org/uniprotkb/O94856) · Ensembl [ENSG00000163531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163531)

## Data

Gene col 8711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8711); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8711]; `tensor/DDL_lfc|DDL_z.npy` [8711]; `embed/gene_vectors.npy` [8711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8711 or target_col == 8711). Every well: [[NFASC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFASC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
