---
symbol: "ACTN2"
type: "gene"
col: 1192
ensembl_id: "ENSG00000077522"
name: "actinin alpha 2"
location: "1q43"
module: 125
arm: "+"
pooled_cpm: 5.76
n_lines_expressing: 33
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 9
tags: ["gene", "module/125"]
generated_by: "tahoemap"
---

# ACTN2

*actinin alpha 2* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 13.4× (z +41.2, q 0e+00, up in 27 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.778× (z -4.0, q 0.040, down in 10 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35F1]] (+0.69, fdr 8e-06), [[LINC01828]] (+0.62, fdr 1e-05), [[GBP5]] (+0.62, fdr 7e-06); moves opposite to [[CLASP1]] (-0.52, fdr 1e-05), [[ZDHHC7]] (-0.52, fdr 1e-05), [[VPS26B]] (-0.50, fdr 8e-05).
> It is in [[Module 125]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PNLIPRP3]] → it (grade B ⚠); 9 go from it, the strongest it → [[B4GAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **13.4×** | +41.2 | 0e+00 | 27/27 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.06×** | +21.9 | 0e+00 | 22/25 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **6.69×** | +21.3 | 0e+00 | 22/28 (NCI-H460, C32, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.41×** | +19.5 | 0e+00 | 20/26 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **4.85×** | +17.1 | 0e+00 | 23/28 (NCI-H460, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.23×** | +12.7 | 3e-35 | 19/30 (C32, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.66×** | +11.0 | 3e-26 | 18/29 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.48×** | +10.2 | 1e-22 | 16/29 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.31×** | +9.4 | 4e-19 | 18/31 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +8.5 | 2e-15 | 6/11 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +8.2 | 1e-14 | 7/18 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.00×** | +7.8 | 3e-13 | 17/31 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +7.8 | 3e-13 | 17/29 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.92×** | +7.3 | 9e-12 | 13/29 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.89×** | +7.1 | 4e-11 | 10/28 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +6.5 | 3e-09 | 12/29 (A-427, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +6.0 | 6e-08 | 8/29 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -4.0 | 0.040 | 10/31 (A-172, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.704×** | -3.8 | 0.045 | 7/28 (J82, A-172, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.725×** | -3.6 | 0.059 | 8/29 (A549, A498, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.096 | 8/30 (A-172, A549, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | 0.577× | -3.2 | 0.14 | 4/19 (C32, A498, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.759× | -3.1 | 0.20 | 6/28 (A-172, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.0 | 19 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +34.6) | — |
| [[A-172 (line)]] | wt | 15.4 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.0501× (z -12.9) |
| [[A-427 (line)]] | wt | 12.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.75× (z +9.6) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -9.4) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 5.37 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.9× (z +14.5) | — |
| [[C32 (line)]] | wt | 11.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.8× (z +16.4) | — |
| [[hTERT-HPNE (line)]] | wt | 21.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +17.8) | — |
| [[A498 (line)]] | wt | 9.26 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +11.9) | [[Clobetasol propionate (drug)]] 0.05 µM 0.0589× (z -12.6) |
| [[H4 (line)]] | wt | 15.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 31.3× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 4.95 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.9× (z +17.2) | — |
| [[J82 (line)]] | alt | 5.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.3× (z +15.7) | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 93.8× (z +14.8) | — |
| [[PANC-1 (line)]] | alt | 3.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 6.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.9× (z +13.1) | — |
| [[SK-MEL-2 (line)]] | alt | 17.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.2× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 10.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 19.0× (z +11.3) | — |
| [[CFPAC-1 (line)]] | alt | 2.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 3.43 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.9× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 20.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +12.4) | — |
| [[A549 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.722 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.806 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.927 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.956 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.709 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35F1]] | +0.69 | +0.77 / +0.58 | both halves | 8e-06 |  |
| [[LINC01828]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[GBP5]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[C12orf50]] | +0.61 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[KCNIP1]] | +0.61 | +0.60 / +0.48 | both halves | 2e-05 | pathway: Muscle contraction |
| [[CACNA1E]] | +0.60 | +0.61 / +0.51 | both halves | 1e-05 | pathway: Neuronal System |
| [[NPHS1]] | +0.60 | +0.47 / +0.54 | both halves | 2e-05 | pathway: Cell-Cell communication; STRING 517 |
| [[GPR158]] | +0.59 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PLB1]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ZFPM2]] | +0.58 | +0.53 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[CTSS]] | +0.58 | +0.59 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[HDAC9]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLASP1]] | -0.52 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZDHHC7]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[VPS26B]] | -0.50 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[B4GAT1]] | -0.50 | -0.37 / -0.53 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNLIPRP3]] | B | PNLIPRP3 activity raises ACTN2's level | lines that do not express PNLIPRP3 (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without PNLIPRP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: RSPO3, ENSG00000225087, PDE1A |
| [[TRIML2]] | C | TRIML2 activity raises ACTN2's level | lines that do not express TRIML2 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without TRIML2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF471, LINC01010, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GAT1]] | B | ACTN2 activity raises B4GAT1's level | lines that do not express ACTN2 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without ACTN2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| [[KCNQ3]] | B | ACTN2 activity lowers KCNQ3's level | lines that do not express ACTN2 (17) vs lines expressing it (33) | 1.52× higher at baseline in the lines without ACTN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | ACTN2 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM | B | ACTN2 activity raises the cells' numbers under Sivelestat (sodium tetrahydrate) 5 µM (protects the cells) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 0.89× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 0.5 µM | B | ACTN2 activity lowers the cells' numbers under Peretinoin 0.5 µM (makes them more sensitive) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 1.34× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | ACTN2 activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 1.25× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | ACTN2 activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 0.87× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 0.05 µM | B | ACTN2 activity lowers the cells' numbers under Peretinoin 0.05 µM (makes them more sensitive) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 1.04× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | ACTN2 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express ACTN2 (17) vs lines expressing it (31) | the lines without ACTN2: 0.89× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |

## Where it sits

- **Module**: [[Module 125]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.2, 21.1); signed map (38.2, 21.2). **Vector** length 72.0, 15.4% of its response variance represented; |z| ≥ 3 in 887 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +41.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +21.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.6 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +12.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +0.7 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | actinin alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:236,664,141-236,764,631 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Actinins |
| Hallmark sets | MYOGENESIS, COMPLEMENT, APICAL_JUNCTION |
| Reactome | 22 pathways, smallest: Striated Muscle Contraction; Ras activation upon Ca2+ influx through NMDA receptor; Unblocking of NMDA receptors, glutamate binding and activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P35609](https://www.uniprot.org/uniprotkb/P35609) (Alpha-actinin-2):

> F-actin cross-linking protein which is thought to anchor actin to a variety of intracellular structures. This is a bundling protein.

**Summary**, from NCBI Gene [88](https://www.ncbi.nlm.nih.gov/gene/88):

> Alpha actinins belong to the spectrin gene superfamily which represents a diverse group of cytoskeletal proteins, including the alpha and beta spectrins and dystrophins. Alpha actinin is an actin-binding protein with multiple roles in different cell types. In nonmuscle cells, the cytoskeletal isoform is found along microfilament bundles and adherens-type junctions, where it is involved in binding actin to the membrane. In contrast, skeletal, cardiac, and smooth muscle isoforms are localized to …

**Accessions** — [HGNC:164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:164) · Entrez [88](https://www.ncbi.nlm.nih.gov/gene/88) · UniProt [P35609](https://www.uniprot.org/uniprotkb/P35609) · Ensembl [ENSG00000077522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077522)

## Data

Gene col 1192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1192); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1192]; `tensor/DDL_lfc|DDL_z.npy` [1192]; `embed/gene_vectors.npy` [1192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1192 or target_col == 1192). Every well: [[ACTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
