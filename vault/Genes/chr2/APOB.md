---
symbol: "APOB"
type: "gene"
col: 1405
ensembl_id: "ENSG00000084674"
name: "apolipoprotein B"
location: "2p24.1"
module: 27
arm: "+"
pooled_cpm: 21.26
n_lines_expressing: 3
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 22
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# APOB

*apolipoprotein B* — 2p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 8.56× (z +12.5, q 4e-33, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +5.2, q 3e-05, up in 0 of 1 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.182×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.186×).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PEG3]] (+0.82, fdr 1e-05), [[AFP]] (+0.79, fdr 7e-06), [[FGL1]] (+0.69, fdr 1e-05); moves opposite to [[IFT88]] (-0.34, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[UGT2B7]] → it (grade C ⚠); 22 go from it, the strongest it → [[ALB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1405.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **8.56×** | +12.5 | 4e-33 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.45×** | +9.7 | 1e-19 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.87×** | +7.4 | 3e-11 | 1/1 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.2 | 3e-05 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.02×** | +4.3 | 0.002 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.91×** | +3.7 | 0.023 | 1/1 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.81×** | +3.4 | 0.048 | 0/1 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +3.3 | 0.065 | 0/1 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.71× | +3.0 | 0.15 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1405.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.182×); [[Verteporfin (drug)]] 5 µM in 1 line (HepG2/C3A 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | 0.562× | -3.4 | 0.33 | 1/1 (HepG2/C3A) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1405. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 1,707 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -13.0) |
| [[A-172 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.98 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1405), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PEG3]] | +0.82 | +0.90 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[AFP]] | +0.79 | +0.86 / +0.62 | both halves | 7e-06 | pathway: Post-translational protein phosphorylation; STRING 844 |
| [[FGL1]] | +0.69 | +0.80 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LNCAROD]] | +0.63 | +0.68 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[APOA2]] | +0.56 | +0.90 / +0.08 | ⚠ one half (not replicated) | 0.003 | same gene group; pathway: Chylomicron assembly; STRING 999 |
| [[PHYHIPL]] | +0.56 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[PLA2G2A]] | +0.53 | +0.58 / +0.53 | both halves | 1e-05 | STRING 442 |
| [[NKD1]] | +0.51 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[LGR5]] | +0.49 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[TNFSF14]] | +0.47 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[A1CF]] | +0.47 | +0.38 / +0.55 | both halves | 6e-05 | STRING 856 |
| [[LINC01622]] | +0.47 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[UGT2B7]] | +0.47 | +0.54 / +0.28 | both halves | 3e-04 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT88]] | -0.34 | -0.27 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT2B7]] | C | UGT2B7 activity raises APOB's level | lines that do not express UGT2B7 (37) vs lines expressing it (13) | 2.51× lower at baseline in the lines without UGT2B7 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A1, AFP, RHEX; co-absent with the target |
| [[PEG3]] | C | PEG3 activity raises APOB's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 3.55× lower at baseline in the lines without PEG3 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[LINC02008]] | C | LINC02008 activity raises APOB's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 2.44× lower at baseline in the lines without LINC02008 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363; co-absent with the target |
| [[LINC01622]] | C | LINC01622 activity raises APOB's level | lines that do not express LINC01622 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without LINC01622 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GJB1, LINC02008, PROX1-AS1; maybe low, not absent; co-absent with the target |
| [[KRT5]] | C | KRT5 activity raises APOB's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 2.29× lower at baseline in the lines without KRT5 | 0.021 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[SERPINF1]] | C | SERPINF1 activity raises APOB's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.84× lower at baseline in the lines without SERPINF1 | 0.027 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent; co-absent with the target |
| [[APOA2]] | C | APOA2 activity raises APOB's level | lines that do not express APOA2 (46) vs lines expressing it (4) | 15.44× lower at baseline in the lines without APOA2 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, AFP, BMP10; co-absent with the target; its own permutation p |
| [[AFP]], [[ALB]] | C | AFP, ALB activity raises APOB's level | lines that do not express AFP, ALB (45) vs lines expressing them (5) | 10.19× lower at baseline in the lines without AFP, ALB | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APOA2, APOB, CALCA; co-absent with the target; co-absent genes |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 0, C 22. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ALB]] | C | APOB activity raises ALB's level | lines that do not express APOB (47) vs lines expressing it (3) | 26.84× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[AFP]] | C | APOB activity raises AFP's level | lines that do not express APOB (47) vs lines expressing it (3) | 26.65× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[APOA2]] | C | APOB activity raises APOA2's level | lines that do not express APOB (47) vs lines expressing it (3) | 20.92× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[NKD1]] | C | APOB activity raises NKD1's level | lines that do not express APOB (47) vs lines expressing it (3) | 11.06× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[TNFSF14]] | C | APOB activity raises TNFSF14's level | lines that do not express APOB (47) vs lines expressing it (3) | 10.58× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[HNF1A-AS1]] | C | APOB activity raises HNF1A-AS1's level | lines that do not express APOB (47) vs lines expressing it (3) | 3.65× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[VSNL1]] | C | APOB activity raises VSNL1's level | lines that do not express APOB (47) vs lines expressing it (3) | 3.50× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[PROM1]] | C | APOB activity raises PROM1's level | lines that do not express APOB (47) vs lines expressing it (3) | 3.47× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[LINC01622]] | C | APOB activity raises LINC01622's level | lines that do not express APOB (47) vs lines expressing it (3) | 3.39× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[SLC30A10]] | C | APOB activity raises SLC30A10's level | lines that do not express APOB (47) vs lines expressing it (3) | 3.07× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; its own permutation p |
| [[APCDD1]] | C | APOB activity raises APCDD1's level | lines that do not express APOB (47) vs lines expressing it (3) | 2.84× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |
| [[LINC02058]] | C | APOB activity raises LINC02058's level | lines that do not express APOB (47) vs lines expressing it (3) | 2.05× lower at baseline in the lines without APOB | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: APOA2, BMP10, TBXT; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.399). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, 54.0); signed map (65.6, 19.8). **Vector** length 9.23, 6.82% of its response variance represented; |z| ≥ 3 in 30 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.4 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.4 | +12.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.3 | +9.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.2 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +0.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.2 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.2 | +0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.2 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.2 | +2.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.2 | +2.1 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.2 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.2 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.2 | -1.8 |
|  | [[Neratinib (drug)]] 5 µM |  | -0.1 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.1 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p24.1 — chr2:21,001,429-21,044,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ApoB-100 |
| Gene groups (HGNC) | Apolipoproteins |
| Reactome | 36 pathways, smallest: VLDL assembly; Chylomicron remodeling; VLDL clearance |
| Matched by | ensembl_id |

**Function**, from UniProt [P04114](https://www.uniprot.org/uniprotkb/P04114) (Apolipoprotein B-100):

> Apolipoprotein B is a major protein constituent of chylomicrons (apo B-48), LDL (apo B-100) and VLDL (apo B-100). Apo B-100 functions as a recognition signal for the cellular binding and internalization of LDL particles by the apoB/E receptor.

**Summary**, from NCBI Gene [338](https://www.ncbi.nlm.nih.gov/gene/338):

> This gene product is the main apolipoprotein of chylomicrons and low density lipoproteins (LDL), and is the ligand for the LDL receptor. It occurs in plasma as two main isoforms, apoB-48 and apoB-100: the former is synthesized exclusively in the gut and the latter in the liver. The intestinal and the hepatic forms of apoB are encoded by a single gene from a single, very long mRNA. The two isoforms share a common N-terminal sequence. The shorter apoB-48 protein is produced after RNA editing of …

**Accessions** — [HGNC:603](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:603) · Entrez [338](https://www.ncbi.nlm.nih.gov/gene/338) · UniProt [P04114](https://www.uniprot.org/uniprotkb/P04114) · Ensembl [ENSG00000084674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000084674)

## Data

Gene col 1405: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1405); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1405, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1405]; `tensor/DDL_lfc|DDL_z.npy` [1405]; `embed/gene_vectors.npy` [1405]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1405 or target_col == 1405). Every well: [[APOB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
