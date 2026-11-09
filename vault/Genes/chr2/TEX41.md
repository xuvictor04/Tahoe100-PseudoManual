---
symbol: "TEX41"
type: "gene"
col: 13546
ensembl_id: "ENSG00000226674"
name: "testis expressed 41"
location: "2q22.3"
module: 121
arm: "+"
pooled_cpm: 40.37
n_lines_expressing: 21
n_dd_up: 24
n_dd_down: 13
n_dd_up_clean: 21
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 27
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# TEX41

*testis expressed 41* — 2q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.20× (z +12.9, q 1e-35, up in 4 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.455× (z -9.2, q 3e-17, down in 18 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP24]] (+0.73, fdr 7e-06), [[BICC1]] (+0.68, fdr 7e-06), [[CNTN6]] (+0.66, fdr 7e-06).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CXCL10]] → it (grade B ⚠); 27 go from it, the strongest it → [[PLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13546.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +12.9 | 1e-35 | 4/19 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +10.5 | 1e-23 | 10/19 (HOP62, NCI-H1792, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +9.9 | 7e-21 | 0/17 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +6.8 | 2e-09 | 7/19 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.4 | 2e-08 | 2/17 (A549, NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.70×** | +6.2 | 6e-08 | 11/18 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +6.0 | 2e-07 | 5/19 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +5.4 | 6e-06 | 0/19 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +5.3 | 7e-06 | 4/19 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.2 | 1e-05 | 12/19 (C32, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +4.9 | 5e-05 | 6/19 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.001 | 4/19 (HOP62, A549, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.001 | 12/18 (C32, A498, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.0 | 0.002 | 9/19 (C32, NCI-H1792, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.004 | 14/18 (C32, HOP62, …) | rises with dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.004 | 6/18 (SNU-423, RPMI-7951, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.014 | 9/19 (C32, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13546.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.455×** | -9.2 | 3e-17 | 18/18 (J82, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.579×** | -6.4 | 5e-08 | 18/19 (J82, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.654×** | -4.8 | 4e-04 | 15/19 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.670×** | -4.7 | 4e-04 | 17/18 (A498, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.683×** | -4.4 | 1e-03 | 18/19 (J82, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.700×** | -4.2 | 0.003 | 9/18 (SW 900, NCI-H1792, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.714×** | -3.9 | 0.007 | 13/18 (J82, A498, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.722×** | -3.8 | 0.009 | 12/19 (SW 900, J82, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.795×** | -3.8 | 0.009 | 14/19 (SW 900, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.724×** | -3.8 | 0.009 | 6/18 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.015 | 16/18 (A498, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.740×** | -3.5 | 0.021 | 13/18 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.744×** | -3.3 | 0.039 | 0/19 | rises with dose | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13546. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 503 | 0 | 18 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0342× (z -20.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0483× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 374 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.271× (z -13.1) |
| [[A498 (line)]] | wt | 53.5 | 0 | 8 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.129× (z -11.9) |
| [[C32 (line)]] | wt | 144 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.92× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.200× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW 900 (line)]] | alt | 37.9 | 0 | 7 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0957× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 27.5 | 3 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.93× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.196× (z -10.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.198× (z -10.5) |
| [[SHP-77 (line)]] | alt | 162 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0492× (z -23.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 89.7 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0877× (z -11.9) |
| [[HOP62 (line)]] | alt | 13.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +12.1) | — |
| [[NCI-H661 (line)]] | alt | 1,397 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.197× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 9.20 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.18 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.79 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13546), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP24]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[BICC1]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CNTN6]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[EBF1]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.63 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[ARHGAP15]] | +0.61 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MSC-AS1]] | +0.61 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[TRPC4]] | +0.61 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[HECW2]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CASC15]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 | same gene group |
| [[TRPA1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PEX5L]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL10]] | B | CXCL10 activity raises TEX41's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 3.33× lower at baseline in the lines without CXCL10 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers TEX41's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[BAALC]] | C | BAALC activity raises TEX41's level | lines that do not express BAALC (32) vs lines expressing it (18) | 4.27× lower at baseline in the lines without BAALC | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[TMEM178B]] | C | TMEM178B activity raises TEX41's level | lines that do not express TMEM178B (22) vs lines expressing it (28) | 4.82× lower at baseline in the lines without TMEM178B | 0.014 | ⚠ within organs, on part of the lines; also absent: NTRK3, SPOCK1, POU3F2; co-absent with the target |
| [[CNTN6]] | C | CNTN6 activity raises TEX41's level | lines that do not express CNTN6 (38) vs lines expressing it (12) | 4.75× lower at baseline in the lines without CNTN6 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000234426, LINC02476, SPARC; maybe low, not absent; co-absent with the target |
| [[GLIS1]] | C | GLIS1 activity raises TEX41's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 4.81× lower at baseline in the lines without GLIS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[CDH6]] | C | CDH6 activity raises TEX41's level | lines that do not express CDH6 (33) vs lines expressing it (17) | 2.57× lower at baseline in the lines without CDH6 | 0.077 | ⚠ within organs, on part of the lines; also absent: TOX, LUM, BAALC; co-absent with the target |
| [[LINC03041]] | C | LINC03041 activity raises TEX41's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 4.87× lower at baseline in the lines without LINC03041 | 0.082 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent; co-absent with the target |
| [[COL11A1]] | C | COL11A1 activity raises TEX41's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 3.18× lower at baseline in the lines without COL11A1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 9, C 18. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | TEX41 activity raises PLD1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.57× lower at baseline in the lines without TEX41 | 0.025 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[FAM13C]] | B | TEX41 activity raises FAM13C's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without TEX41 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[PDZRN3]] | B | TEX41 activity raises PDZRN3's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.03× lower at baseline in the lines without TEX41 | 0.031 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[CPQ]] | B | TEX41 activity raises CPQ's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without TEX41 | 0.032 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[NREP]] | B | TEX41 activity raises NREP's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.68× lower at baseline in the lines without TEX41 | 0.035 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | TEX41 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express TEX41 (29) vs lines expressing it (19) | the lines without TEX41: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[IPCEF1]] | B | TEX41 activity raises IPCEF1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without TEX41 | 0.077 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[ARHGAP24]] | B | TEX41 activity raises ARHGAP24's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.75× lower at baseline in the lines without TEX41 | 0.084 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| cells under [[Macitentan (drug)]] 5 µM | B | TEX41 activity lowers the cells' numbers under Macitentan 5 µM (makes them more sensitive) | lines that do not express TEX41 (29) vs lines expressing it (19) | the lines without TEX41: 1.22× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[BAALC]] | C | TEX41 activity raises BAALC's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 2.93× lower at baseline in the lines without TEX41 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[GLIS1]] | C | TEX41 activity raises GLIS1's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 3.43× lower at baseline in the lines without TEX41 | 0.011 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |
| [[ZEB2]] | C | TEX41 activity raises ZEB2's level | lines that do not express TEX41 (29) vs lines expressing it (21) | 8.30× lower at baseline in the lines without TEX41 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.7, 24.6); signed map (42.6, 26.8). **Vector** length 84.9, 29.4% of its response variance represented; |z| ≥ 3 in 629 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -9.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.6 | -4.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -1.0 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 41 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q22.3 — chr2:144,666,312-145,262,988 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZp686O1327, LINC00953 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48667](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48667) · Entrez [401014](https://www.ncbi.nlm.nih.gov/gene/401014) · Ensembl [ENSG00000226674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226674)

## Data

Gene col 13546: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13546); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13546, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13546]; `tensor/DDL_lfc|DDL_z.npy` [13546]; `embed/gene_vectors.npy` [13546]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13546 or target_col == 13546). Every well: [[TEX41 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX41.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
