---
symbol: "CLVS1"
type: "gene"
col: 10800
ensembl_id: "ENSG00000177182"
name: "clavesin 1"
location: "8q12.2-q12.3"
module: 90
arm: "+"
pooled_cpm: 5.89
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 5
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CLVS1

*clavesin 1* — 8q12.2-q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.51× (z +22.5, q 0e+00, up in 33 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0612×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.242×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.173×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0754×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPP6]] (+0.86, fdr 7e-06), [[LINC02208]] (+0.83, fdr 7e-06), [[GRM8]] (+0.82, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[CHRM5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10800.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.51×** | +22.5 | 0e+00 | 33/36 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +12.2 | 5e-32 | 18/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +11.4 | 5e-28 | 4/7 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +10.4 | 5e-23 | 26/44 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +9.8 | 9e-21 | 4/9 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +8.8 | 9e-17 | 24/44 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.8 | 1e-16 | 16/36 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +8.5 | 1e-15 | 11/22 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.7 | 1e-12 | 24/44 (SW480, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.5 | 4e-12 | 13/35 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +5.7 | 8e-07 | 11/33 (NCI-H2347, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +4.4 | 5e-04 | 4/42 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.3 | 9e-04 | 13/46 (A498, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.001 | 7/43 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.003 | 9/44 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.029 | 8/36 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.32×** | +3.3 | 0.035 | 4/32 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.0 | 0.069 | 3/24 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 1.18× | +3.0 | 0.083 | 1/42 (HCT15) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10800.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.0612×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.242×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (COLO 205 0.173×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0754×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.751× | -3.6 | 0.17 | 10/43 (A-172, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.782× | -3.1 | 0.41 | 4/45 (HCT15, NCI-H661, …) | two highest doses | position effect removed |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.787× | -3.1 | 0.41 | 8/43 (hTERT-HPNE, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10800. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -10.4) |
| [[SHP-77 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0612× (z -21.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 2.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.02× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.26 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0754× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 3.52 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 3.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 2.53 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 10.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.74× (z +9.0) | — |
| [[SW480 (line)]] | alt | 3.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.8) | — |
| [[A-172 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10800), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP6]] | +0.86 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[LINC02208]] | +0.83 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[GRM8]] | +0.82 | +0.74 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_SPERMATOGENESIS |
| [[GRM7]] | +0.81 | +0.64 / +0.84 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.81 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[CNBD1]] | +0.80 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.79 | +0.67 / +0.81 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.78 | +0.74 / +0.80 | both halves | 7e-06 |  |
| [[LINC00298]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.78 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.76 | +0.57 / +0.75 | both halves | 8e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 4, C 19. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CLVS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[F11-AS1]] | B | F11-AS1 activity weakens CLVS1's drug response | lines that do not express F11-AS1 (34) vs lines expressing it (11) | the lines without F11-AS1 respond 2.71× as strongly (z diff -1.50); strongest at Dinaciclib 5 µM: 2.73x vs 0.35x (z diff -7.7) | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[F11-AS1]] | B | F11-AS1 activity raises CLVS1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without F11-AS1 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |
| [[SLC24A3]] | B | SLC24A3 activity raises CLVS1's level | lines that do not express SLC24A3 (37) vs lines expressing it (13) | 1.69× lower at baseline in the lines without SLC24A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: CGA, LINC01456, CALCA; maybe low, not absent |
| [[GLRA3]] | C | GLRA3's natural level weakens CLVS1's drug response | GLRA3's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.47; direction clear | 1e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CNTNAP5]] | C | CNTNAP5's natural level weakens CLVS1's drug response | CNTNAP5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.83, reverse -0.30; direction clear | 1e-04 | ⚠ tissue can mimic it; precision caveat |
| [[CHRM5]] | C | CHRM5's natural level weakens CLVS1's drug response | CHRM5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.82, reverse -0.80; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYT1L]] | C | MYT1L's natural level weakens CLVS1's drug response | MYT1L's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.86, reverse -0.75; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CIBAR1-DT]] | C | CIBAR1-DT's natural level weakens CLVS1's drug response | CIBAR1-DT's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.82, reverse -0.46; direction clear | 2e-04 | ⚠ tissue can mimic it; precision caveat |
| [[PTPRT]] | C | PTPRT's natural level weakens CLVS1's drug response | PTPRT's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.79, reverse -0.67; direction clear | 9e-04 | ⚠ tissue can mimic it; precision caveat |
| [[NOS1]] | C | NOS1's natural level weakens CLVS1's drug response | NOS1's natural level across 42 lines (lineage-adjusted; a glimpse) | r -0.78, reverse -0.44; direction clear | 0.004 | ⚠ tissue can mimic it; precision caveat |
| [[SLC35F4]] | C | SLC35F4's natural level weakens CLVS1's drug response | SLC35F4's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.80, reverse -0.49; direction clear | 0.005 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHRM5]] | C | CLVS1's natural level weakens CHRM5's drug response | CLVS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.80, reverse -0.82; direction not clear | 9e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[C2CD5-AS1]] | C | CLVS1's natural level weakens C2CD5-AS1's drug response | CLVS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.71, reverse +0.22; direction clear | 0.009 | ⚠ tissue can mimic it; precision caveat |
| [[LINC00907]] | C | CLVS1's natural level weakens LINC00907's drug response | CLVS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69, reverse -0.67; direction not clear | 0.036 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PTPRT]] | C | CLVS1's natural level weakens PTPRT's drug response | CLVS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.67, reverse -0.79; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYT1L]] | C | CLVS1's natural level weakens MYT1L's drug response | CLVS1's natural level across 36 lines (lineage-adjusted; a glimpse) | r -0.75, reverse -0.86; direction not clear | 0.063 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.905). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, 28.5); signed map (34.3, 14.5). **Vector** length 53.5, 6.72% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +22.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | clavesin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.2-q12.3 — chr8:61,057,158-61,501,645 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC34646, CRALBPL, C6orf212L; previously RLBP1L1 |
| Gene groups (HGNC) | CRAL-TRIO lipid binding domain containing |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 4 pathways, smallest: Lysosome Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUQ0](https://www.uniprot.org/uniprotkb/Q8IUQ0) (Clavesin-1):

> Required for normal morphology of late endosomes and/or lysosomes in neurons (By similarity). Binds phosphatidylinositol 3,5-bisphosphate (PtdIns(3,5)P2).

**Summary**, from NCBI Gene [157807](https://www.ncbi.nlm.nih.gov/gene/157807):

> Enables phosphatidylinositol-3,5-bisphosphate binding activity. Predicted to be involved in lysosome organization. Located in endosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23139) · Entrez [157807](https://www.ncbi.nlm.nih.gov/gene/157807) · UniProt [Q8IUQ0](https://www.uniprot.org/uniprotkb/Q8IUQ0) · Ensembl [ENSG00000177182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177182)

## Data

Gene col 10800: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10800); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10800, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10800]; `tensor/DDL_lfc|DDL_z.npy` [10800]; `embed/gene_vectors.npy` [10800]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10800 or target_col == 10800). Every well: [[CLVS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLVS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
