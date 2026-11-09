---
symbol: "SYP"
type: "gene"
col: 2201
ensembl_id: "ENSG00000102003"
name: "synaptophysin"
location: "Xp11.23"
module: 161
arm: "+"
pooled_cpm: 8.06
n_lines_expressing: 46
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/161"]
generated_by: "tahoemap"
---

# SYP

*synaptophysin* — Xp11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.03× (z +19.1, q 0e+00, up in 38 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.158×, SW1417 0.482×; ⚠ cell-cycle shift, explains ~13% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.373×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0536×; ⚠ transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGT7]] (+0.69, fdr 1e-05), [[ASMTL]] (+0.68, fdr 2e-05), [[DOCK6]] (+0.66, fdr 3e-05); moves opposite to [[TOR1A]] (-0.65, fdr 3e-05), [[NNT]] (-0.63, fdr 4e-05), [[METTL4]] (-0.63, fdr 3e-05).
> It is in [[Module 161]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CCDC144NL-AS1]] → it (grade B ⚠); 6 go from it, the strongest it → [[NRARP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2201.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.03×** | +19.1 | 0e+00 | 38/43 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.18×** | +18.1 | 0e+00 | 39/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.95×** | +17.8 | 0e+00 | 40/42 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.14×** | +14.8 | 0e+00 | 38/41 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +10.9 | 2e-25 | 8/9 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.18×** | +10.6 | 3e-24 | 32/42 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.18×** | +10.1 | 5e-22 | 25/37 (SW480, NCI-H23, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +9.9 | 3e-21 | 15/22 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +8.2 | 1e-14 | 21/33 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +7.9 | 2e-13 | 25/39 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +7.8 | 4e-13 | 9/13 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +6.0 | 1e-07 | 18/36 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.94×** | +5.8 | 2e-07 | 19/40 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.5 | 1e-06 | 12/24 (RPMI-7951, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +5.5 | 1e-06 | 22/34 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.89×** | +5.1 | 1e-05 | 22/39 (MIA PaCa-2, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +5.0 | 2e-05 | 21/42 (A-427, NCI-H23, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.004 | 5/41 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.008 | 13/40 (RPMI-7951, J82, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.016 | 11/41 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.021 | 4/37 (C-33 A, A-172, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.68×** | +3.3 | 0.023 | 3/31 (SW480, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2201.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (C-33 A 0.158×, SW1417 0.482×; ⚠ cell-cycle shift, explains ~13% of this change); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.373×; ⚠ cell-cycle shift, explains ~0% of this change); [[OTS514 (drug)]] 0.05 µM in 1 line (NCI-H2347 0.0536×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.700× | -3.0 | 0.96 | 7/43 (HT-29, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2201. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 19.3 | 9 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 6.19× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 3.60 | 6 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 26.2× (z +11.9) ⚠ toxic; cell-cycle shift, explains ~27% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 7.14× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +11.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 9.68× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.8× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 3.56 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.19× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 68.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.18× (z +9.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-427 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.373× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -13.5) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1573 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.66× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 13.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +12.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 1 (1 ⚠) | — | [[OTS514 (drug)]] 0.05 µM 0.0536× (z -8.7) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 7.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.88× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 31.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2201), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGT7]] | +0.69 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[ASMTL]] | +0.68 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[DOCK6]] | +0.66 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[CCDC112]] | +0.66 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[RTN2]] | +0.64 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PIGH]] | +0.64 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TNNT1]] | +0.64 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[SLC17A7]] | +0.63 | +0.43 / +0.60 | both halves | 3e-05 | STRING 880 |
| [[RING1]] | +0.63 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[PLIN3]] | +0.63 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[GRHL1]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SPATA2L]] | +0.62 | +0.57 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOR1A]] | -0.65 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[NNT]] | -0.63 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[METTL4]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.61 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CTPS2]] | -0.61 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[SNX5]] | -0.60 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[XNDC1N]] | -0.60 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | -0.60 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[FARS2]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[CRPPA]] | -0.58 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[PSME3IP1]] | -0.58 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[NUP205]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC144NL-AS1]] | B | CCDC144NL-AS1 activity raises SYP's level | lines that do not express CCDC144NL-AS1 (33) vs lines expressing it (17) | 1.70× lower at baseline in the lines without CCDC144NL-AS1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000264660, LINC01518, ENSG00000287861; maybe low, not absent |
| [[NOVA2]] | B | NOVA2 activity raises SYP's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without NOVA2 | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[SCG3]] | B | SCG3 activity raises SYP's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without SCG3 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[SRRM3]] | B | SRRM3 activity raises SYP's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.97× lower at baseline in the lines without SRRM3 | 0.045 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[LINC02327]] | B | LINC02327 activity raises SYP's level | lines that do not express LINC02327 (41) vs lines expressing it (9) | 2.00× lower at baseline in the lines without LINC02327 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000258028, LINC02566, ENSG00000289605 |
| [[LINC00408]] | B | LINC00408 activity raises SYP's level | lines that do not express LINC00408 (38) vs lines expressing it (12) | 1.59× lower at baseline in the lines without LINC00408 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000287861, ANKRD20A9P, PHF2P2 |
| [[DHRS2]] | B | DHRS2 activity raises SYP's level | lines that do not express DHRS2 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without DHRS2 | 0.096 | ⚠ within organs, on part of the lines; also absent: MAN1C1 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRARP]] | C | SYP activity raises NRARP's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.76× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[CFD]] | C | SYP activity raises CFD's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[CCDC112]] | C | SYP activity raises CCDC112's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[CAMSAP3]] | C | SYP activity raises CAMSAP3's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[FCHO1]] | C | SYP activity raises FCHO1's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.31× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |
| [[PIGW]] | C | SYP activity raises PIGW's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.25× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 161]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.715). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (9.1, 0.5); signed map (-23.3, 23.1). **Vector** length 68.3, 12.3% of its response variance represented; |z| ≥ 3 in 901 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +14.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.0 | +18.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.5 | +19.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.2 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | synaptophysin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.23 — chrX:49,187,815-49,200,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MRX96 |
| Gene groups (HGNC) | Synaptophysins; MARVEL domain containing |
| Reactome | 3 pathways, smallest: Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound; Sensory Perception |
| Matched by | ensembl_id |

**Function**, from UniProt [P08247](https://www.uniprot.org/uniprotkb/P08247) (Synaptophysin):

> Possibly involved in structural functions as organizing other membrane components or in targeting the vesicles to the plasma membrane. Involved in the regulation of short-term and long-term synaptic plasticity (By similarity).

**Summary**, from NCBI Gene [6855](https://www.ncbi.nlm.nih.gov/gene/6855):

> This gene encodes an integral membrane protein of small synaptic vesicles in brain and endocrine cells. The protein also binds cholesterol and is thought to direct targeting of vesicle-associated membrane protein 2 (synaptobrevin) to intracellular compartments. Mutations in this gene are associated with an X-linked form of cognitive disability. [provided by RefSeq, Jul 2017]

**Accessions** — [HGNC:11506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11506) · Entrez [6855](https://www.ncbi.nlm.nih.gov/gene/6855) · UniProt [P08247](https://www.uniprot.org/uniprotkb/P08247) · Ensembl [ENSG00000102003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102003)

## Data

Gene col 2201: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2201); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2201, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2201]; `tensor/DDL_lfc|DDL_z.npy` [2201]; `embed/gene_vectors.npy` [2201]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2201 or target_col == 2201). Every well: [[SYP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
