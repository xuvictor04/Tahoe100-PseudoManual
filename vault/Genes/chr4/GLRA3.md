---
symbol: "GLRA3"
type: "gene"
col: 6995
ensembl_id: "ENSG00000145451"
name: "glycine receptor alpha 3"
location: "4q34.1"
module: 90
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 3
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# GLRA3

*glycine receptor alpha 3* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.19× (z +14.1, q 2e-42, up in 19 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.227×); [[Carbamazepine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0789×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.221×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD1]] (+0.80, fdr 7e-06), [[MYT1L]] (+0.78, fdr 7e-06), [[CNTNAP5]] (+0.77, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 3 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6995.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.19×** | +14.1 | 2e-42 | 19/21 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +13.6 | 1e-39 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.46×** | +10.7 | 3e-24 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.41×** | +9.7 | 3e-20 | 1/1 (SHP-77) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +6.7 | 2e-09 | 8/23 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.7 | 1e-06 | 11/37 (C32, BT-474, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.84×** | +4.7 | 2e-04 | 1/2 (NCI-H460) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +4.5 | 4e-04 | 6/26 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.3 | 9e-04 | 0/2 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.3 | 9e-04 | 1/9 (HOP62) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 3/37 (SHP-77, SW480, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.004 | 7/34 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.7 | 0.010 | 0/8 | top dose only |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.010 | 0/6 | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.52×** | +3.6 | 0.012 | 1/12 (Hs 766T) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.033 | 2/23 (Hs 766T, SHP-77) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.059 | 1/10 (CFPAC-1) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.060 | 2/11 (NCI-H460, HOP62) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.065 | 1/24 (NCI-H1573) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Talc (drug)]] 0.05 µM |  | **1.42×** | +3.0 | 0.078 | 0/20 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6995.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.227×); [[Carbamazepine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0789×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.221×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dorzolamide (hydrochloride) (drug)]] 5 µM |  | 0.667× | -3.3 | 0.47 | 5/34 (SW 900, A498, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6995. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 64.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 1.67 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0789× (z -8.9) |
| [[A-172 (line)]] | wt | 0.963 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.707 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.896 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.820 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.917 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.853 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.987 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.798 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.782 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.761 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.681 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.740 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.897 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.750 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6995), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD1]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MYT1L]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP5]] | +0.77 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 |  |
| [[SEMA6D]] | +0.76 | +0.67 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP4]] | +0.76 | +0.66 / +0.78 | both halves | 7e-06 |  |
| [[UNC80]] | +0.75 | +0.65 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[VENTXP1]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[NELL1]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[XIRP2]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[NRXN1]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 | pathway: Neuronal System |
| [[CNTN5]] | +0.72 | +0.65 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises GLRA3's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.91× lower at baseline in the lines without CALCA | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[LINC01320]] | B | LINC01320 activity raises GLRA3's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 1.88× lower at baseline in the lines without LINC01320 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[SYT4]] | B | SYT4 activity raises GLRA3's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.40× lower at baseline in the lines without SYT4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[RIT2]] | B | RIT2 activity raises GLRA3's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.43× lower at baseline in the lines without RIT2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[KCNB2]] | B | KCNB2 activity raises GLRA3's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.16× lower at baseline in the lines without KCNB2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[ASCL1]] | B | ASCL1 activity raises GLRA3's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.93× lower at baseline in the lines without ASCL1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[CGA]] | B | CGA activity raises GLRA3's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.54× lower at baseline in the lines without CGA | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[LINC02492]] | B | LINC02492 activity raises GLRA3's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.42× lower at baseline in the lines without LINC02492 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[SRRM4]] | B | SRRM4 activity raises GLRA3's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 1.95× lower at baseline in the lines without SRRM4 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[AK4P3]] | B | AK4P3 activity raises GLRA3's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.48× lower at baseline in the lines without AK4P3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[POU6F2]] | B | POU6F2 activity raises GLRA3's level | lines that do not express POU6F2 (37) vs lines expressing it (13) | 1.62× lower at baseline in the lines without POU6F2 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC01287, ENSG00000250421, RIT2; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | GLRA3's natural level weakens CLVS1's drug response | GLRA3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.47; direction clear | 1e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | GLRA3's natural level weakens CHRM5's drug response | GLRA3's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.48; direction clear | 2e-04 | ⚠ tissue can mimic it; precision caveat |
| [[PTPRT]] | C | GLRA3's natural level weakens PTPRT's drug response | GLRA3's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.45; direction clear | 0.045 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.829). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 30.2); signed map (34.0, 15.8). **Vector** length 31.2, 3.19% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +14.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.2 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | glycine receptor alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:174,636,920-174,829,247 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycine receptors |
| Reactome | 3 pathways, smallest: Neurotransmitter receptors and postsynaptic signal transmission; Transmission across Chemical Synapses; Neuronal System |
| Matched by | ensembl_id |

**Function**, from UniProt [O75311](https://www.uniprot.org/uniprotkb/O75311) (Glycine receptor subunit alpha-3):

> Glycine receptors are ligand-gated chloride channels. Channel opening is triggered by extracellular glycine. Channel characteristics depend on the subunit composition; heteropentameric channels display faster channel closure (By similarity). Plays an important role in the down-regulation of neuronal excitability (By similarity). Contributes to the generation of inhibitory postsynaptic currents (By similarity). Contributes to increased pain perception in response to increased prostaglandin E2 …

**Summary**, from NCBI Gene [8001](https://www.ncbi.nlm.nih.gov/gene/8001):

> This gene encodes a member of the ligand-gated ion channel protein family. The encoded protein is a member of the glycine receptor subfamily. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:4328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4328) · Entrez [8001](https://www.ncbi.nlm.nih.gov/gene/8001) · UniProt [O75311](https://www.uniprot.org/uniprotkb/O75311) · Ensembl [ENSG00000145451](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145451)

## Data

Gene col 6995: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6995); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6995, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6995]; `tensor/DDL_lfc|DDL_z.npy` [6995]; `embed/gene_vectors.npy` [6995]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6995 or target_col == 6995). Every well: [[GLRA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLRA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
