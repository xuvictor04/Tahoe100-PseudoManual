---
symbol: "CHRM5"
type: "gene"
col: 11600
ensembl_id: "ENSG00000184984"
name: "cholinergic receptor muscarinic 5"
location: "15q14"
module: 90
arm: "+"
pooled_cpm: 3.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 24
direction_downstream: 6
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# CHRM5

*cholinergic receptor muscarinic 5* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +14.8, q 0e+00, up in 29 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0644×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0485×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0632×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0704×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYT1L]] (+0.84, fdr 7e-06), [[GRIK1]] (+0.75, fdr 7e-06), [[CNTNAP5]] (+0.74, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 6 go from it, the strongest it → [[CLVS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11600.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +14.8 | 0e+00 | 29/30 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +11.2 | 7e-27 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +11.0 | 1e-25 | 8/9 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.32×** | +10.0 | 1e-21 | 2/3 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +7.2 | 7e-11 | 5/10 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.4 | 6e-06 | 7/21 (LoVo, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.8 | 1e-04 | 4/33 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 5e-04 | 10/42 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.5 | 5e-04 | 8/44 (PANC-1, H4, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.63×** | +4.4 | 6e-04 | 5/30 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.028 | 5/25 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.043 | 4/25 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.043 | 8/31 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.2 | 0.056 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.42×** | +3.2 | 0.057 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.0644×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SHP-77 0.0485×); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.0632×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.0704×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11600. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 94.7 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0644× (z -19.1) |
| [[LoVo (line)]] | wt | 2.42 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0579× (z -10.1) |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11600), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYT1L]] | +0.84 | +0.79 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.75 | +0.78 / +0.66 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.74 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[VENTXP1]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.72 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[GLRA3]] | +0.71 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.70 | +0.48 / +0.72 | both halves | 2e-05 |  |
| [[G2E3-AS1]] | +0.69 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CNTNAP4]] | +0.69 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[XIRP2]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.67 | +0.75 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 12, C 12. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises CHRM5's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.93× lower at baseline in the lines without CALCA | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[KCNB2]] | B | KCNB2 activity raises CHRM5's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without KCNB2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[SYT4]] | B | SYT4 activity raises CHRM5's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.44× lower at baseline in the lines without SYT4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[RIT2]] | B | RIT2 activity raises CHRM5's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 2.38× lower at baseline in the lines without RIT2 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[ASCL1]] | B | ASCL1 activity raises CHRM5's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 1.88× lower at baseline in the lines without ASCL1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[SRRM4]] | B | SRRM4 activity raises CHRM5's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 1.94× lower at baseline in the lines without SRRM4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[LINC02492]] | B | LINC02492 activity raises CHRM5's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 1.48× lower at baseline in the lines without LINC02492 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[CGA]] | B | CGA activity raises CHRM5's level | lines that do not express CGA (44) vs lines expressing it (6) | 2.44× lower at baseline in the lines without CGA | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[RUNX1T1]] | B | RUNX1T1 activity weakens CHRM5's drug response | lines that do not express RUNX1T1 (37) vs lines expressing it (7) | the lines without RUNX1T1 respond 1.94× as strongly (z diff -0.69); strongest at Dinaciclib 0.05 µM: 4.04x vs 0.88x (z diff -6.1) | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; target measured in part of the lines; artifact flags |
| [[PCSK1]] | B | PCSK1 activity raises CHRM5's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 1.85× lower at baseline in the lines without PCSK1 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2 |
| [[AK4P3]] | B | AK4P3 activity raises CHRM5's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.57× lower at baseline in the lines without AK4P3 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[LINC01287]] | B | LINC01287 activity raises CHRM5's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 1.70× lower at baseline in the lines without LINC01287 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLVS1]] | C | CHRM5's natural level weakens CLVS1's drug response | CHRM5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.82, reverse -0.80; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[MYT1L]] | C | CHRM5's natural level weakens MYT1L's drug response | CHRM5's natural level across 36 lines (lineage-adjusted; a glimpse) | r -0.74, reverse -0.87; direction not clear | 0.067 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLC4A10]] | C | CHRM5's natural level weakens SLC4A10's drug response | CHRM5's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.62; direction not clear | 0.080 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[C2CD5-AS1]] | C | CHRM5's natural level weakens C2CD5-AS1's drug response | CHRM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.12; direction clear | 0.090 | ⚠ tissue can mimic it; precision caveat |
| [[LINC02307]] | C | CHRM5's natural level weakens LINC02307's drug response | CHRM5's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.81; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CHRM5's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | CHRM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.081 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.1, 30.6); signed map (34.5, 15.6). **Vector** length 51.6, 6.65% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.8 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.4 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | cholinergic receptor muscarinic 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:33,968,497-34,067,458 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cholinergic receptors muscarinic |
| Reactome | 6 pathways, smallest: Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P08912](https://www.uniprot.org/uniprotkb/P08912) (Muscarinic acetylcholine receptor M5):

> The muscarinic acetylcholine receptor mediates various cellular responses, including inhibition of adenylate cyclase, breakdown of phosphoinositides and modulation of potassium channels through the action of G proteins. Primary transducing effect is Pi turnover.

**Summary**, from NCBI Gene [1133](https://www.ncbi.nlm.nih.gov/gene/1133):

> The muscarinic cholinergic receptors belong to a larger family of G protein-coupled receptors. The functional diversity of these receptors is defined by the binding of acetylcholine and includes cellular responses such as adenylate cyclase inhibition, phosphoinositide degeneration, and potassium channel mediation. Muscarinic receptors influence many effects of acetylcholine in the central and peripheral nervous system. The clinical implications of this receptor are unknown; however, stimulation …

**Accessions** — [HGNC:1954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1954) · Entrez [1133](https://www.ncbi.nlm.nih.gov/gene/1133) · UniProt [P08912](https://www.uniprot.org/uniprotkb/P08912) · Ensembl [ENSG00000184984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184984)

## Data

Gene col 11600: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11600); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11600, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11600]; `tensor/DDL_lfc|DDL_z.npy` [11600]; `embed/gene_vectors.npy` [11600]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11600 or target_col == 11600). Every well: [[CHRM5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHRM5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
