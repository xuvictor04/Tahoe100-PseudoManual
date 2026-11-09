---
symbol: "PLB1"
type: "gene"
col: 8780
ensembl_id: "ENSG00000163803"
name: "phospholipase B1"
location: "2p23.2"
module: 75
arm: "+"
pooled_cpm: 4.03
n_lines_expressing: 48
n_dd_up: 40
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PLB1

*phospholipase B1* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.24× (z +31.5, q 0e+00, up in 31 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.0934×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW480 0.230×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA1E]] (+0.80, fdr 7e-06), [[LINC01033]] (+0.73, fdr 7e-06), [[LINC01933]] (+0.71, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8780.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.24×** | +31.5 | 0e+00 | 31/34 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.37×** | +29.5 | 0e+00 | 28/32 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.6×** | +26.6 | 0e+00 | 11/16 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.6×** | +26.5 | 0e+00 | 6/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **10.6×** | +24.6 | 0e+00 | 8/10 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **7.25×** | +22.3 | 0e+00 | 31/36 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.93×** | +18.0 | 0e+00 | 21/32 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.61×** | +15.3 | 0e+00 | 35/41 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.67×** | +10.6 | 1e-24 | 11/21 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.37×** | +9.7 | 2e-20 | 17/39 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.76×** | +9.0 | 1e-17 | 13/41 (HOP62, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.20×** | +8.9 | 3e-17 | 24/35 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.19×** | +8.8 | 6e-17 | 23/42 (PANC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.99×** | +8.1 | 2e-14 | 5/9 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.06×** | +7.8 | 2e-13 | 21/38 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +5.9 | 1e-07 | 15/39 (NCI-H2347, HEC-1-A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.1 | 1e-05 | 10/39 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.8 | 5e-05 | 7/38 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.004 | 5/40 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +3.5 | 0.009 | 6/38 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.012 | 4/41 (NCI-H2347, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8780.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.0934×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW480 0.230×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ferulic acid (drug)]] 5 µM |  | 0.737× | -3.3 | 0.20 | 7/36 (SW1417, A549, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.747× | -3.3 | 0.20 | 10/40 (NCI-H2030, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.750× | -3.3 | 0.20 | 6/39 (SW 900, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8780. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.44 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 99.2× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 23.5× (z +14.8) | — |
| [[A498 (line)]] | wt | 2.22 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 109× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.3× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 1.80 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.4× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 3.64 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 50.6× (z +13.4) | — |
| [[NCI-H2347 (line)]] | alt | 5.85 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.7× (z +9.2) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 1.36 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +11.5) | — |
| [[A-172 (line)]] | wt | 2.66 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +11.0) | — |
| [[LoVo (line)]] | wt | 1.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.7× (z +13.2) | — |
| [[SNU-423 (line)]] | alt | 3.42 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +12.4) | — |
| [[A549 (line)]] | wt | 1.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.6× (z +9.6) | — |
| [[C32 (line)]] | wt | 1.58 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 82.8× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0934× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 2.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 79.5× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 2.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 41.6× (z +8.9) | — |
| [[J82 (line)]] | alt | 3.34 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 41.8× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 73.9× (z +10.0) | — |
| [[NCI-H2030 (line)]] | alt | 2.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.4× (z +10.5) | — |
| [[SW480 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.230× (z -8.9) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.810 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8780), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA1E]] | +0.80 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[LINC01933]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[DPP6]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[DNAH3]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[LINC01811]] | +0.69 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[FER1L6]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[MTUS2]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[GRM8]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RBFOX3]] | +0.68 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLB1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.1% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MILR1]] | B | MILR1 activity raises PLB1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without MILR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[ALDH1A2]] | B | ALDH1A2 activity raises PLB1's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without ALDH1A2 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[ICAM2]] | B | ICAM2 activity raises PLB1's level | lines that do not express ICAM2 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without ICAM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: TINAGL1, GALNT5, PCSK9; maybe low, not absent |
| [[CD22]] | B | CD22 activity raises PLB1's level | lines that do not express CD22 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without CD22 | 0.067 | ⚠ within organs, on part of the lines; also absent: CX3CL1, SHROOM4, CFB; maybe low, not absent |
| [[VAV1]] | B | VAV1 activity raises PLB1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without VAV1 | 0.073 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[LINC03042]] | B | LINC03042 activity raises PLB1's level | lines that do not express LINC03042 (16) vs lines expressing it (34) | 1.49× lower at baseline in the lines without LINC03042 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC00960, CORO2B, DNAH17; maybe low, not absent |
| [[LINC02964]] | B | LINC02964 activity raises PLB1's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 1.75× lower at baseline in the lines without LINC02964 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3 |
| [[NCALD]] | B | NCALD activity raises PLB1's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without NCALD | 0.085 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[BTBD16]] | B | BTBD16 activity lowers PLB1's level | lines that do not express BTBD16 (11) vs lines expressing it (39) | 1.17× higher at baseline in the lines without BTBD16 | 0.097 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.9, 26.7); signed map (30.3, 13.6). **Vector** length 71.4, 12.4% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.4 | +26.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.8 | +26.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +24.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +31.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.9 | +22.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.4 | +15.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.4 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.1 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.3 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | phospholipase B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.2 — chr2:28,457,145-28,644,142 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLB, FLJ30866 |
| Gene groups (HGNC) | Phospholipases |
| Reactome | 9 pathways, smallest: Acyl chain remodelling of PC; Retinoid metabolism and transport; Metabolism of fat-soluble vitamins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P1J6](https://www.uniprot.org/uniprotkb/Q6P1J6) (Phospholipase B1, membrane-associated):

> Calcium-independent membrane-associated phospholipase that catalyzes complete diacylation of phospholipids by hydrolyzing both sn-1 and sn-2 fatty acyl chains attached to the glycerol backbone (phospholipase B activity) (By similarity). Has dual phospholipase and lysophospholipase activities toward diacylphospholipids. Preferentially cleaves sn-2 ester bonds over sn-1 bonds. Acts as a lipase toward glycerolipid substrates (By similarity). Hydrolyzes fatty acyl chains of diacylglycerols with …

**Summary**, from NCBI Gene [151056](https://www.ncbi.nlm.nih.gov/gene/151056):

> This gene encodes a membrane-associated phospholipase that displays lysophospholipase and phospholipase A2 activities through removal of sn-1 and sn-2 fatty acids of glycerophospholipids. In addition, it displays lipase and retinyl ester hydrolase activities. The encoded protein is highly conserved and is composed of a large, glycosylated extracellular domain composed of four tandem homologous domains, followed by a hydrophobic segment that anchors the enzyme to the membrane and a short …

**Accessions** — [HGNC:30041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30041) · Entrez [151056](https://www.ncbi.nlm.nih.gov/gene/151056) · UniProt [Q6P1J6](https://www.uniprot.org/uniprotkb/Q6P1J6) · Ensembl [ENSG00000163803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163803)

## Data

Gene col 8780: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8780); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8780, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8780]; `tensor/DDL_lfc|DDL_z.npy` [8780]; `embed/gene_vectors.npy` [8780]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8780 or target_col == 8780). Every well: [[PLB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
