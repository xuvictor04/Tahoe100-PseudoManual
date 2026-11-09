---
symbol: "ITIH5"
type: "gene"
col: 4420
ensembl_id: "ENSG00000123243"
name: "inter-alpha-trypsin inhibitor heavy chain 5"
location: "10p14"
module: 8
arm: "+"
pooled_cpm: 9.55
n_lines_expressing: 13
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 17
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ITIH5

*inter-alpha-trypsin inhibitor heavy chain 5* — 10p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +13.6, q 2e-39, up in 2 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 21 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0919×, A498 0.404×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HepG2/C3A 0.148×, A498 0.245×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.0224×); [[Harringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.0898×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTGS2]] (+0.54, fdr 6e-05), [[ITIH2]] (+0.52, fdr 8e-04, ⚠ one half only (not replicated); same locus), [[ATP10A]] (+0.50, fdr 3e-05), [[IL6]] (+0.49, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[GDNF]] → it (grade C ⚠); 17 go from it, the strongest it → [[DIRC3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +13.6 | 2e-39 | 2/11 (SK-MEL-2, A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +12.4 | 5e-33 | 2/11 (SW1417, A498) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.24×** | +10.6 | 4e-24 | 7/11 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +10.5 | 9e-24 | 1/11 (SK-MEL-2) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.24×** | +10.1 | 4e-22 | 1/8 (A498) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +8.8 | 9e-17 | 2/8 (A498, C32) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.17×** | +7.2 | 4e-11 | 0/11 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.3 | 9e-06 | 3/11 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +4.9 | 6e-05 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.92×** | +4.4 | 7e-04 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.003 | 4/11 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.004 | 1/11 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.8 | 0.006 | 2/11 (SW1417, C32) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +3.7 | 0.009 | 1/11 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.014 | 1/7 (C32) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.029 | 2/11 (A549, RPMI-7951) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.029 | 2/11 (C32, HOP62) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.063 | 1/11 (SW1417) | top dose only | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.075 | 1/11 (SK-MEL-2) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.075 | 2/11 (SK-MEL-2, HOP62) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +2.9 | 0.093 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4420.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 21 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HepG2/C3A 0.0919×, A498 0.404×); [[Ixazomib citrate (drug)]] 5 µM in 2 lines (HepG2/C3A 0.148×, A498 0.245×; ⚠ cell-cycle shift, explains ~30% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×; ⚠ cell-cycle shift, explains ~0% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.0224×); [[Harringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.0898×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.671× | -3.7 | 0.10 | 0/11 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.688× | -3.5 | 0.13 | 5/11 (SNU-423, A498, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.512× | -3.3 | 0.18 | 2/11 (C32, SNU-423) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.709× | -3.2 | 0.18 | 4/11 (A498, HepG2/C3A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 23.6 | 0 | 13 (2 ⚠) | — | [[Cobimetinib (drug)]] 0.5 µM 0.0224× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -20.6) |
| [[A498 (line)]] | wt | 135 | 0 | 4 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -10.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.404× (z -9.1) |
| [[A549 (line)]] | wt | 18.1 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0739× (z -8.8) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 5.95 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0438× (z -9.7) |
| [[A-172 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.784 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.772 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.773 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.919 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.986 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.14 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTGS2]] | +0.54 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[ITIH2]] | +0.52 | +0.52 / +0.20 | ⚠ one half (not replicated) | 8e-04 | ⚠ same locus (36.3 kb: neighbours can correlate without regulation) |
| [[ATP10A]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[IL6]] | +0.49 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[CXCL8]] | +0.48 | +0.29 / +0.47 | both halves | 2e-04 |  |
| [[IGFBP3]] | +0.48 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[IGFBP1]] | +0.48 | +0.55 / +0.32 | both halves | 1e-04 |  |
| [[CCL3]] | +0.48 | +0.25 / +0.38 | both halves | 4e-04 |  |
| [[C15orf48]] | +0.48 | +0.32 / +0.50 | both halves | 1e-04 |  |
| [[IGFN1]] | +0.48 | +0.25 / +0.46 | both halves | 4e-04 |  |
| [[SLC4A4]] | +0.47 | +0.32 / +0.48 | both halves | 2e-04 |  |
| [[TIMD4]] | +0.47 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[PREX2]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GDNF]] | C | GDNF activity raises ITIH5's level | lines that do not express GDNF (38) vs lines expressing it (12) | 3.42× lower at baseline in the lines without GDNF | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[TDRD9]] | C | TDRD9 activity raises ITIH5's level | lines that do not express TDRD9 (37) vs lines expressing it (13) | 4.22× lower at baseline in the lines without TDRD9 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GDNF, ITIH5, DCT; co-absent with the target |
| [[NCKAP5]] | C | NCKAP5 activity raises ITIH5's level | lines that do not express NCKAP5 (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without NCKAP5 | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, LYPD1, SALL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 5, C 12. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIRC3]] | B | ITIH5 activity raises DIRC3's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 4.31× lower at baseline in the lines without ITIH5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[CD82]] | B | ITIH5 activity raises CD82's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.47× lower at baseline in the lines without ITIH5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[GSDME]] | B | ITIH5 activity raises GSDME's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.04× lower at baseline in the lines without ITIH5 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[RTN4RL2]] | B | ITIH5 activity raises RTN4RL2's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without ITIH5 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[ITPR1]] | B | ITIH5 activity raises ITPR1's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.20× lower at baseline in the lines without ITIH5 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426 |
| [[KIRREL3]] | C | ITIH5 activity raises KIRREL3's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 5.89× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[TNS1]] | C | ITIH5 activity raises TNS1's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 7.32× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[GDNF]] | C | ITIH5 activity raises GDNF's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 6.89× lower at baseline in the lines without ITIH5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[FRMD4A]] | C | ITIH5 activity raises FRMD4A's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 5.39× lower at baseline in the lines without ITIH5 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[C10orf90]] | C | ITIH5 activity raises C10orf90's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.80× lower at baseline in the lines without ITIH5 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[CD5L]] | C | ITIH5 activity raises CD5L's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.16× lower at baseline in the lines without ITIH5 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[SERPINE2]] | C | ITIH5 activity raises SERPINE2's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.67× lower at baseline in the lines without ITIH5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.193). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.0, 44.8); signed map (52.9, 27.4). **Vector** length 40.1, 12.0% of its response variance represented; |z| ≥ 3 in 314 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +10.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.4 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | inter-alpha-trypsin inhibitor heavy chain 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p14 — chr10:7,559,270-7,666,998 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10848 |
| Gene groups (HGNC) | Inter-alpha-trypsin inhibitor heavy chains |
| Hallmark sets | IL2_STAT5_SIGNALING, ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UX2](https://www.uniprot.org/uniprotkb/Q86UX2) (Inter-alpha-trypsin inhibitor heavy chain H5):

> May act as a tumor suppressor.

**Summary**, from NCBI Gene [80760](https://www.ncbi.nlm.nih.gov/gene/80760):

> This gene encodes a heavy chain component of one of the inter-alpha-trypsin inhibitor (ITI) family members. ITI proteins are involved in extracellular matrix stabilization and in the prevention of tumor metastasis. They are also structurally related plasma serine protease inhibitors and are composed of a light chain and varying numbers of heavy chains. This family member is thought to function as a tumor suppressor in breast and thyroid cancers. Alternative splicing results in multiple …

**Accessions** — [HGNC:21449](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21449) · Entrez [80760](https://www.ncbi.nlm.nih.gov/gene/80760) · UniProt [Q86UX2](https://www.uniprot.org/uniprotkb/Q86UX2) · Ensembl [ENSG00000123243](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123243)

## Data

Gene col 4420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4420); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4420]; `tensor/DDL_lfc|DDL_z.npy` [4420]; `embed/gene_vectors.npy` [4420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4420 or target_col == 4420). Every well: [[ITIH5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITIH5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
