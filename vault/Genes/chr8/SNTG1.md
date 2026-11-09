---
symbol: "SNTG1"
type: "gene"
col: 7190
ensembl_id: "ENSG00000147481"
name: "syntrophin gamma 1"
location: "8q11.21"
module: 9
arm: "+"
pooled_cpm: 14.32
n_lines_expressing: 12
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 33
direction_downstream: 26
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# SNTG1

*syntrophin gamma 1* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.75× (z +20.0, q 0e+00, up in 4 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.152×; ⚠ cell-cycle shift, explains ~67% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.147×; ⚠ cell-cycle shift, explains ~53% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.206×; ⚠ cell-cycle shift, explains ~38% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.330×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIK1]] (+0.84, fdr 7e-06), [[RIT2]] (+0.80, fdr 7e-06), [[ASCL1]] (+0.79, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[ASCL1]] → it (grade C ⚠); 26 go from it, the strongest it → [[RALYL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.75×** | +20.0 | 0e+00 | 4/7 (LOX-IMVI, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +8.4 | 9e-15 | 2/6 (SHP-77, LOX-IMVI) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +8.4 | 1e-14 | 1/5 (SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +8.1 | 7e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.45×** | +7.2 | 6e-11 | 2/8 (LOX-IMVI, SW 900) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +6.8 | 1e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.13×** | +6.1 | 9e-08 | 4/8 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +5.0 | 5e-05 | 1/7 (LOX-IMVI) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.73×** | +4.4 | 6e-04 | 0/9 | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +4.4 | 7e-04 | 2/10 (LOX-IMVI, SW 900) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.07×** | +4.2 | 0.001 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.45×** | +3.8 | 0.007 | 0/2 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.93×** | +3.8 | 0.007 | 2/4 (LOX-IMVI, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.010 | 2/8 (LOX-IMVI, H4) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.4 | 0.022 | 1/6 (LOX-IMVI) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.056 | 2/8 (SHP-77, hTERT-HPNE) | rises with dose | position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.082 | 1/6 (LOX-IMVI) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7190.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.152×; ⚠ cell-cycle shift, explains ~67% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.147×; ⚠ cell-cycle shift, explains ~53% of this change); [[Belinostat (drug)]] 5 µM in 1 line (SHP-77 0.206×; ⚠ cell-cycle shift, explains ~38% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.330×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.632× | -3.7 | 0.11 | 2/9 (SHP-77, SW 900) | rises with dose |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.643× | -3.3 | 0.26 | 0/9 | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.668× | -3.1 | 0.32 | 3/8 (H4, SHP-77, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.689× | -3.0 | 0.32 | 1/8 (SHP-77) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 642 | 0 | 9 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -12.2) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.2) |
| [[A-172 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIK1]] | +0.84 | +0.77 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.80 | +0.78 / +0.82 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.79 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[SYT4]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[SRRM4]] | +0.77 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[KCNB2]] | +0.74 | +0.72 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[PCSK1]] | +0.70 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[RUNX1T1]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[NRXN1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[PEX5L]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 0, C 33. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCL1]] | C | ASCL1 activity raises SNTG1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 3.87× lower at baseline in the lines without ASCL1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4; co-absent with the target |
| [[CALCA]] | C | CALCA activity raises SNTG1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 7.30× lower at baseline in the lines without CALCA | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2; co-absent with the target |
| [[NAA11]] | C | NAA11 activity raises SNTG1's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without NAA11 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises SNTG1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 5.37× lower at baseline in the lines without SYT4 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[RIT2]] | C | RIT2 activity raises SNTG1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 5.44× lower at baseline in the lines without RIT2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4; co-absent with the target |
| [[SRRM4]] | C | SRRM4 activity raises SNTG1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 3.83× lower at baseline in the lines without SRRM4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises SNTG1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 4.31× lower at baseline in the lines without KCNB2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[RMST]] | C | RMST activity raises SNTG1's level | lines that do not express RMST (35) vs lines expressing it (15) | 2.65× lower at baseline in the lines without RMST | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, ENSG00000287923; maybe low, not absent; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises SNTG1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.33× lower at baseline in the lines without AK4P3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[RUNX1T1]] | C | RUNX1T1 activity raises SNTG1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without RUNX1T1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises SNTG1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.45× lower at baseline in the lines without F11-AS1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[DGKB]] | C | DGKB activity raises SNTG1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.86× lower at baseline in the lines without DGKB | 0.035 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 4, C 22. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALYL]] | B | SNTG1 activity raises RALYL's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.03× lower at baseline in the lines without SNTG1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[NRXN1]] | B | SNTG1 activity raises NRXN1's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without SNTG1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| cells under [[Pralsetinib (drug)]] 5 µM | B | SNTG1 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express SNTG1 (38) vs lines expressing it (10) | the lines without SNTG1: 0.64× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[NYAP2]] | B | SNTG1 activity raises NYAP2's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.84× lower at baseline in the lines without SNTG1 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[RUNX1T1]] | C | SNTG1 activity raises RUNX1T1's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 7.15× lower at baseline in the lines without SNTG1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[ESRRG]] | C | SNTG1 activity raises ESRRG's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.31× lower at baseline in the lines without SNTG1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[TSHZ2]] | C | SNTG1 activity raises TSHZ2's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 4.15× lower at baseline in the lines without SNTG1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[SLC4A4]] | C | SNTG1 activity raises SLC4A4's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.65× lower at baseline in the lines without SNTG1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[PPARGC1A]] | C | SNTG1 activity raises PPARGC1A's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.10× lower at baseline in the lines without SNTG1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[KHDRBS2]] | C | SNTG1 activity raises KHDRBS2's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without SNTG1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[LINC02197]] | C | SNTG1 activity raises LINC02197's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.51× lower at baseline in the lines without SNTG1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[ST18]] | C | SNTG1 activity raises ST18's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.41× lower at baseline in the lines without SNTG1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 36.9); signed map (44.8, 34.0). **Vector** length 28.5, 9.88% of its response variance represented; |z| ≥ 3 in 174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +20.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | syntrophin gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:49,909,789-50,796,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYN4, G1SYN |
| Gene groups (HGNC) | PDZ domain containing; Syntrophin family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSN8](https://www.uniprot.org/uniprotkb/Q9NSN8) (Gamma-1-syntrophin):

> Adapter protein that binds to and probably organizes the subcellular localization of a variety of proteins. May link various receptors to the actin cytoskeleton and the dystrophin glycoprotein complex (By similarity). May participate in regulating the subcellular location of diacylglycerol kinase-zeta to ensure that diacylglycerol is rapidly inactivated following receptor activation.

**Summary**, from NCBI Gene [54212](https://www.ncbi.nlm.nih.gov/gene/54212):

> The protein encoded by this gene is a member of the syntrophin family. Syntrophins are cytoplasmic peripheral membrane proteins that typically contain 2 pleckstrin homology (PH) domains, a PDZ domain that bisects the first PH domain, and a C-terminal domain that mediates dystrophin binding. This family member plays a role in mediating gamma-enolase trafficking to the plasma membrane and in enhancing its neurotrophic activity. Mutations in this gene are associated with idiopathic scoliosis. …

**Accessions** — [HGNC:13740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13740) · Entrez [54212](https://www.ncbi.nlm.nih.gov/gene/54212) · UniProt [Q9NSN8](https://www.uniprot.org/uniprotkb/Q9NSN8) · Ensembl [ENSG00000147481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147481)

## Data

Gene col 7190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7190); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7190]; `tensor/DDL_lfc|DDL_z.npy` [7190]; `embed/gene_vectors.npy` [7190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7190 or target_col == 7190). Every well: [[SNTG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNTG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
