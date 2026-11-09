---
symbol: "KLRK1-AS1"
type: "gene"
col: 14437
ensembl_id: "ENSG00000245648"
name: "KLRK1 antisense RNA 1"
location: "12p13.2"
module: 23
arm: "+"
pooled_cpm: 5.03
n_lines_expressing: 39
n_dd_up: 34
n_dd_down: 1
n_dd_up_clean: 27
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 11
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KLRK1-AS1

*KLRK1 antisense RNA 1* — 12p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.4× (z +30.0, q 0e+00, up in 25 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.582× (z -4.9, q 5e-04, down in 13 of 35 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.154×, SNU-1 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.193×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.238×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0526×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX17-DT]] (+0.77, fdr 1e-05), [[EFCAB5]] (+0.75, fdr 3e-05), [[KLRD1]] (+0.74, fdr 7e-06, ⚠ same locus), [[TBCE-1]] (+0.72, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[KLRD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.4×** | +30.0 | 0e+00 | 25/27 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.08×** | +15.7 | 0e+00 | 20/25 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **5.24×** | +14.4 | 7e-45 | 21/29 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.55×** | +12.0 | 6e-31 | 16/35 (HOP62, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +9.9 | 4e-21 | 15/29 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **4.83×** | +7.5 | 8e-12 | 23/31 (NCI-H1573, NCI-H2030, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +6.7 | 1e-09 | 16/30 (C32, H4, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.9 | 3e-07 | 13/35 (A498, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.7 | 7e-07 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.6 | 2e-06 | 7/19 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.4 | 3e-06 | 6/23 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +5.4 | 3e-06 | 1/11 (A-427) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.3 | 5e-06 | 14/28 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +5.1 | 2e-05 | 5/15 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.0 | 2e-05 | 10/27 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.70×** | +4.8 | 5e-05 | 17/35 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +4.3 | 6e-04 | 8/35 (A-427, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +4.3 | 6e-04 | 15/35 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +4.2 | 9e-04 | 8/33 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.011 | 11/28 (AsPC-1, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.011 | 6/34 (HOP62, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14437.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.154×, SNU-1 0.177×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (A-427 0.193×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (A-427 0.238×; ⚠ cell-cycle shift, explains ~57% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0526×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.582×** | -4.9 | 5e-04 | 13/35 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.49 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.1× (z +14.4) | — |
| [[A-427 (line)]] | wt | 56.4 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 2.47 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.0× (z +13.7) | — |
| [[A498 (line)]] | wt | 1.76 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 27.3× (z +11.7) | — |
| [[NCI-H23 (line)]] | alt | 39.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.8) | [[Daptomycin (drug)]] 0.5 µM 0.177× (z -8.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 6.77 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.6× (z +12.6) | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0526× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 3.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.4× (z +10.6) | — |
| [[C32 (line)]] | wt | 3.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 1.70 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.8× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 11.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.58× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 1.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.4× (z +9.3) | — |
| [[A-172 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.956 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX17-DT]] | +0.77 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[EFCAB5]] | +0.75 | +0.70 / +0.46 | both halves | 3e-05 |  |
| [[KLRD1]] | +0.74 | +0.69 / +0.65 | both halves | 7e-06 | ⚠ same locus (34.0 kb, same strand: neighbours can correlate without regulation) |
| [[TBCE-1]] | +0.72 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[UPK2]] | +0.72 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[CHODL]] | +0.71 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.71 | +0.64 / +0.36 | both halves | 1e-04 | same gene group |
| [[FAM184B]] | +0.71 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[AHI1-DT]] | +0.71 | +0.65 / +0.38 | both halves | 6e-05 |  |
| [[CASS4]] | +0.70 | +0.66 / +0.40 | both halves | 5e-05 |  |
| [[KANSL1L]] | +0.70 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | +0.70 | +0.62 / +0.38 | both halves | 7e-05 | same gene group |
| [[DNAI4]] | +0.70 | +0.67 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLRK1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRD1]] | B | KLRK1-AS1 activity raises KLRD1's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without KLRK1-AS1 | 0.005 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[FAM151B-DT]] | B | KLRK1-AS1 activity raises FAM151B-DT's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.38× lower at baseline in the lines without KLRK1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[EPHX1]] | B | KLRK1-AS1 activity raises EPHX1's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without KLRK1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[Ralimetinib dimesylate (drug)]] 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under Ralimetinib dimesylate 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[Erdafitinib (drug)]] 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.96× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[BI-78D3 (drug)]] 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.87× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[OOEP]] | B | KLRK1-AS1 activity lowers OOEP's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.46× higher at baseline in the lines without KLRK1-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[Celecoxib (drug)]] 0.05 µM | B | KLRK1-AS1 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.92× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.87× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[LINC01725]] | B | KLRK1-AS1 activity raises LINC01725's level | lines that do not express KLRK1-AS1 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without KLRK1-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| cells under [[OTS514 (drug)]] 0.05 µM | B | KLRK1-AS1 activity raises the cells' numbers under OTS514 0.05 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.92× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (9.6, 22.9); signed map (29.1, -4.1). **Vector** length 65.8, 12.1% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +30.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +15.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +14.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -0.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -3.0 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | KLRK1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.2 — chr12:10,363,638-10,398,506 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LOC101928100, TP53LC04 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54868) · Entrez [101928100](https://www.ncbi.nlm.nih.gov/gene/101928100) · Ensembl [ENSG00000245648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245648)

## Data

Gene col 14437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14437); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14437]; `tensor/DDL_lfc|DDL_z.npy` [14437]; `embed/gene_vectors.npy` [14437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14437 or target_col == 14437). Every well: [[KLRK1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLRK1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
