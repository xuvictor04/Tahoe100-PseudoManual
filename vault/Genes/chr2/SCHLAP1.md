---
symbol: "SCHLAP1"
type: "gene"
col: 15978
ensembl_id: "ENSG00000281131"
name: "SWI/SNF complex antagonist associated with prostate cancer 1"
location: "2q31.3"
module: 140
arm: "+"
pooled_cpm: 4.85
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SCHLAP1

*SWI/SNF complex antagonist associated with prostate cancer 1* — 2q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 9.58× (z +22.6, q 0e+00, up in 28 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0684×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0734×; ⚠ toxic); [[Hexylresorcinol (drug)]] 5 µM in 1 line (SHP-77 0.243×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USH2A]] (+0.88, fdr 7e-06), [[CNTNAP5]] (+0.85, fdr 7e-06), [[MIR4300HG]] (+0.84, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01320]] → it (grade B ⚠); 2 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15978.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.58×** | +22.6 | 0e+00 | 28/30 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **5.72×** | +17.4 | 0e+00 | 23/32 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.49×** | +10.2 | 4e-22 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.77×** | +10.2 | 4e-22 | 31/42 (SW480, SW1417, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.47×** | +9.6 | 1e-19 | 28/46 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.87×** | +9.5 | 1e-19 | 31/39 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.09×** | +8.0 | 1e-13 | 9/14 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.66×** | +6.9 | 3e-10 | 15/29 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +5.8 | 3e-07 | 1/5 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +5.7 | 9e-07 | 19/39 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.21×** | +5.6 | 1e-06 | 22/45 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **2.14×** | +5.4 | 3e-06 | 15/41 (CFPAC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +5.2 | 8e-06 | 2/12 (HEC-1-A, HT-29) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.2 | 9e-06 | 9/42 (A498, NCI-H1792, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +5.1 | 1e-05 | 10/26 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +5.1 | 1e-05 | 12/33 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +4.7 | 7e-05 | 14/41 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +4.1 | 0.002 | 8/37 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.73×** | +3.9 | 0.003 | 10/36 (SK-MEL-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.065 | 10/42 (A-172, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.069 | 6/38 (NCI-H1573, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15978.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0684×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.0734×; ⚠ toxic); [[Hexylresorcinol (drug)]] 5 µM in 1 line (SHP-77 0.243×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Uridine (drug)]] 0.5 µM |  | 0.640× | -3.2 | 0.92 | 3/43 (SW48, NCI-H2030, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15978. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.99 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 134× (z +17.8) | — |
| [[SW480 (line)]] | alt | 1.66 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 120 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0684× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Hexylresorcinol (drug)]] 5 µM 0.243× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 2.14 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 31.2× (z +13.0) | — |
| [[PANC-1 (line)]] | alt | 1.34 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.0× (z +10.2) | — |
| [[A549 (line)]] | wt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +9.0) | — |
| [[BT-474 (line)]] | alt | 3.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +8.6) | — |
| [[C32 (line)]] | wt | 1.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.7× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.0× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 2.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 36.5× (z +11.3) | — |
| [[J82 (line)]] | alt | 2.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +8.6) | — |
| [[LoVo (line)]] | wt | 1.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 2.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 4.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +13.0) | — |
| [[A-427 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15978), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USH2A]] | +0.88 | +0.80 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CNTNAP5]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[MIR4300HG]] | +0.84 | +0.81 / +0.84 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.81 | +0.72 / +0.86 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.80 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[IL1RAPL2]] | +0.79 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.79 | +0.71 / +0.82 | both halves | 7e-06 |  |
| [[LINC02755]] | +0.79 | +0.76 / +0.79 | both halves | 7e-06 |  |
| [[SGCZ]] | +0.79 | +0.63 / +0.88 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.79 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[CNTNAP4]] | +0.78 | +0.70 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises SCHLAP1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.26× lower at baseline in the lines without LINC01320 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[TOP2A]] | B | TOP2A activity lowers SCHLAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | SCHLAP1's natural level weakens CLVS1's drug response | SCHLAP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.73, reverse -0.38; direction clear | 0.013 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | SCHLAP1's natural level weakens CHRM5's drug response | SCHLAP1's natural level across 43 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.45; direction clear | 0.024 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.880). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.2, 29.1); signed map (32.9, 14.7). **Vector** length 55.7, 8.23% of its response variance represented; |z| ≥ 3 in 999 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.3 | +22.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +17.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +8.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | +9.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -0.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | SWI/SNF complex antagonist associated with prostate cancer 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q31.3 — chr2:180,692,104-180,916,939 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PCAT11; previously LINC00913 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48603) · Entrez [101669767](https://www.ncbi.nlm.nih.gov/gene/101669767) · Ensembl [ENSG00000281131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000281131)

## Data

Gene col 15978: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15978); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15978, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15978]; `tensor/DDL_lfc|DDL_z.npy` [15978]; `embed/gene_vectors.npy` [15978]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15978 or target_col == 15978). Every well: [[SCHLAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCHLAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
