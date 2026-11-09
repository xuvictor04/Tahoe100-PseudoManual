---
symbol: "DIP2C-AS1"
type: "gene"
col: 11112
ensembl_id: "ENSG00000180525"
name: "DIP2C antisense RNA 1"
location: "10p15.3"
module: 27
arm: "+"
pooled_cpm: 2.35
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 1
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DIP2C-AS1

*DIP2C antisense RNA 1* — 10p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.01× (z +9.9, q 2e-20, up in 4 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +6.5, q 2e-08, up in 13 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.859× (z -4.9, q 6e-04, down in 13 of 45 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.152×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.107×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKHD1]] (+0.74, fdr 7e-06), [[BANK1]] (+0.70, fdr 7e-06), [[LINC01091]] (+0.67, fdr 1e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[HNF1A-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CNKSR3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11112.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.01×** | +9.9 | 2e-20 | 4/11 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +8.8 | 5e-16 | 2/2 (HT-29, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.1 | 1e-13 | 1/4 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.5 | 2e-08 | 13/26 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +6.0 | 3e-07 | 10/28 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.5 | 6e-04 | 12/41 (HT-29, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.8 | 0.012 | 1/10 (CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.014 | 3/39 (A-172, A498, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.73×** | +3.5 | 0.027 | 2/11 (SK-MEL-2, HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.050 | 1/11 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.42×** | +3.2 | 0.078 | 10/32 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.1 | 0.085 | 0/9 | top dose only | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Orlistat (drug)]] 0.05 µM |  | **1.47×** | +3.1 | 0.085 | 1/17 (MIA PaCa-2) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.085 | 1/18 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.085 | 5/38 (RPMI-7951, AsPC-1, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11112.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.152×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.154×); [[Digitoxin (drug)]] 5 µM in 1 line (CFPAC-1 0.107×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.859× | -4.9 | 6e-04 | 13/45 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.671×** | -3.6 | 0.068 | 10/41 (SHP-77, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.671×** | -3.6 | 0.068 | 9/38 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.691× | -3.3 | 0.14 | 4/43 (HT-29, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11112. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 19.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -10.1) |
| [[A-172 (line)]] | wt | 2.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.26 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -9.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 0.757 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.954 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.771 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.842 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.622 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.842 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.955 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11112), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKHD1]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[BANK1]] | +0.70 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[LINC01091]] | +0.67 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[LINC00299]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[LINC02254]] | +0.63 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TSPEAR]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[FGD3]] | +0.62 | +0.57 / +0.61 | both halves | 8e-06 |  |
| [[LINC00578]] | +0.62 | +0.69 / +0.38 | both halves | 6e-05 |  |
| [[LINC02253]] | +0.62 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LINC01814]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MYO3B]] | +0.61 | +0.57 / +0.37 | both halves | 7e-05 |  |
| [[PLUT]] | +0.61 | +0.57 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF1A-AS1]] | B | HNF1A-AS1 activity raises DIP2C-AS1's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without HNF1A-AS1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises DIP2C-AS1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without LINC01814 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[SPINK5]] | B | SPINK5 activity raises DIP2C-AS1's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.68× lower at baseline in the lines without SPINK5 | 0.007 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588 |
| [[F5]] | B | F5 activity raises DIP2C-AS1's level | lines that do not express F5 (39) vs lines expressing it (11) | 1.94× lower at baseline in the lines without F5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPX2, FGA, CPLX2 |
| [[RASSF6]] | B | RASSF6 activity raises DIP2C-AS1's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 1.62× lower at baseline in the lines without RASSF6 | 0.013 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[LINC00299]] | B | LINC00299 activity raises DIP2C-AS1's level | lines that do not express LINC00299 (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without LINC00299 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC01814, TNNT2, ATP2C2 |
| [[RORC]] | B | RORC activity raises DIP2C-AS1's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.68× lower at baseline in the lines without RORC | 0.017 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[FAAH2]] | B | FAAH2 activity raises DIP2C-AS1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without FAAH2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[LINC02058]] | B | LINC02058 activity raises DIP2C-AS1's level | lines that do not express LINC02058 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without LINC02058 | 0.044 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[GNGT1]] | B | GNGT1 activity raises DIP2C-AS1's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 1.43× lower at baseline in the lines without GNGT1 | 0.045 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[FGL1]] | B | FGL1 activity raises DIP2C-AS1's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 1.52× lower at baseline in the lines without FGL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[ANO9]] | B | ANO9 activity raises DIP2C-AS1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.49× lower at baseline in the lines without ANO9 | 0.051 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNKSR3]] | C | DIP2C-AS1's natural level weakens CNKSR3's drug response | DIP2C-AS1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.11; direction clear | 0.064 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 44.5); signed map (58.2, 16.5). **Vector** length 46.1, 6.21% of its response variance represented; |z| ≥ 3 in 878 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.1 | -3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.9 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.6 | -3.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | DIP2C antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10p15.3 — chr10:649,948-669,581 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ38681; previously C10orf108, PRR26 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q8N8Z3](https://www.uniprot.org/uniprotkb/Q8N8Z3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30724) · Entrez [414235](https://www.ncbi.nlm.nih.gov/gene/414235) · UniProt [Q8N8Z3](https://www.uniprot.org/uniprotkb/Q8N8Z3) · Ensembl [ENSG00000180525](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180525)

## Data

Gene col 11112: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11112); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11112, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11112]; `tensor/DDL_lfc|DDL_z.npy` [11112]; `embed/gene_vectors.npy` [11112]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11112 or target_col == 11112). Every well: [[DIP2C-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DIP2C-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
