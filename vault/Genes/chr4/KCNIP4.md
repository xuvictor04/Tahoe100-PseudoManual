---
symbol: "KCNIP4"
type: "gene"
col: 11730
ensembl_id: "ENSG00000185774"
name: "potassium voltage-gated channel interacting protein 4"
location: "4p15.31-p15.2"
module: 75
arm: "+"
pooled_cpm: 14.17
n_lines_expressing: 44
n_dd_up: 28
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 10
direction_downstream: 8
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# KCNIP4

*potassium voltage-gated channel interacting protein 4* — 4p15.31-p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.79× (z +21.3, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.05 µM: 0.766× (z -3.9, q 0.054, down in 11 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00536]] (+0.64, fdr 1e-05), [[LINC01033]] (+0.61, fdr 1e-05), [[SLC35F1]] (+0.61, fdr 1e-05); moves opposite to [[TTLL5]] (-0.50, fdr 6e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[LINC01579]] → it (grade B ⚠); 8 go from it, the strongest it → [[GRIP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.79×** | +21.3 | 0e+00 | 39/41 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +20.0 | 0e+00 | 28/39 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +15.2 | 0e+00 | 14/29 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.46×** | +13.2 | 1e-37 | 30/40 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +12.5 | 8e-34 | 7/15 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.22×** | +11.7 | 2e-29 | 24/38 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +11.6 | 2e-29 | 25/41 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.05×** | +10.5 | 4e-24 | 24/39 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +10.3 | 5e-23 | 7/19 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +7.8 | 5e-13 | 15/36 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.2 | 2e-11 | 13/41 (HOP62, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.59×** | +6.5 | 3e-09 | 17/39 (SW480, SW1417, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +5.4 | 3e-06 | 10/36 (NCI-H460, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.0 | 2e-05 | 10/35 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 3e-04 | 9/34 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +4.3 | 6e-04 | 6/37 (A498, RKO, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 6/40 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.003 | 15/42 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.007 | 14/41 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.766×** | -3.9 | 0.054 | 11/41 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.060 | 10/36 (HT-29, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.5 | 0.083 | 6/42 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.793×** | -3.4 | 0.090 | 10/40 (SNU-423, H4, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.795×** | -3.4 | 0.090 | 13/42 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.807× | -3.1 | 0.16 | 10/41 (KATO III, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.812× | -3.1 | 0.18 | 11/40 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.865× | -3.0 | 0.19 | 9/41 (SNU-423, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 95.7 | 1 | 14 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.46× (z +10.5) | [[Clobetasol propionate (drug)]] 0.5 µM 0.106× (z -13.4) |
| [[C32 (line)]] | wt | 8.84 | 9 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 78.6× (z +14.7) | [[Oxaprozin (drug)]] 0.05 µM 0.0618× (z -9.4) |
| [[SW480 (line)]] | alt | 35.8 | 7 (1 ⚠) | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.11× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -10.0) |
| [[HOP62 (line)]] | alt | 11.3 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 9.67× (z +16.1) | — |
| [[KATO III (line)]] | alt | 65.1 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0290× (z -13.8) |
| [[SK-MEL-2 (line)]] | alt | 111 | 4 (1 ⚠) | 1 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +11.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 15.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.81× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 7.25 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.79× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 17.6 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 22.8× (z +11.5) | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0507× (z -10.1) |
| [[HS-578T (line)]] | alt | 18.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.52× (z +12.8) | — |
| [[J82 (line)]] | alt | 3.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.83× (z +10.3) | — |
| [[A498 (line)]] | wt | 9.18 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.12× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 199 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 6.96 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 18.1× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 8.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.04× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +11.9) | — |
| [[NCI-H2030 (line)]] | alt | 6.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.19× (z +10.3) | — |
| [[NCI-H460 (line)]] | wt | 4.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 13.3× (z +9.7) | — |
| [[SW1417 (line)]] | alt | 14.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.01× (z +10.5) | — |
| [[A-172 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00536]] | +0.64 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[LINC01033]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SLC35F1]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[MIR4300HG]] | +0.61 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[GRM8]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 | same gene group |
| [[THSD7B]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[LINC01933]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LRRC4C]] | +0.60 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[LINC02511]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[LDB2]] | +0.59 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[LINC01828]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.58 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTLL5]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01579]] | B | LINC01579 activity raises KCNIP4's level | lines that do not express LINC01579 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without LINC01579 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, CNTNAP2, CACNA1C; maybe low, not absent |
| [[LINC00871]] | B | LINC00871 activity raises KCNIP4's level | lines that do not express LINC00871 (12) vs lines expressing it (38) | 2.22× lower at baseline in the lines without LINC00871 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FRMPD4]] | B | FRMPD4 activity raises KCNIP4's level | lines that do not express FRMPD4 (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without FRMPD4 | 0.017 | ⚠ within organs, on part of the lines; also absent: COL4A1, BICC1, NTF3 |
| [[ITGA1]] | B | ITGA1 activity raises KCNIP4's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without ITGA1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[TOP2A]] | B | TOP2A activity lowers KCNIP4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EGFEM1P]] | B | EGFEM1P activity raises KCNIP4's level | lines that do not express EGFEM1P (20) vs lines expressing it (30) | 1.56× lower at baseline in the lines without EGFEM1P | 0.042 | ⚠ within organs, on part of the lines; also absent: MMP16, ENSG00000253553, RNF150; maybe low, not absent |
| [[FYB1]] | B | FYB1 activity raises KCNIP4's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 1.50× lower at baseline in the lines without FYB1 | 0.044 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[ARL14EPL]] | B | ARL14EPL activity raises KCNIP4's level | lines that do not express ARL14EPL (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without ARL14EPL | 0.056 | ⚠ within organs, on part of the lines; also absent: MAMLD1, ENSG00000243797, ENSG00000253496; maybe low, not absent |
| [[ATXN1]] | B | ATXN1 activity raises KCNIP4's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 2.24× lower at baseline in the lines without ATXN1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[ATP6V0D2]] | B | ATP6V0D2 activity raises KCNIP4's level | lines that do not express ATP6V0D2 (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without ATP6V0D2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D, ARID1A; also absent: GBP5, NALCN, IGFBP7; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP2]] | B | KCNIP4 activity lowers GRIP2's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.18× higher at baseline in the lines without KCNIP4 | 0.008 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[ACVR1C]] | B | KCNIP4 activity raises ACVR1C's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.74× lower at baseline in the lines without KCNIP4 | 0.022 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[SLIT2]] | B | KCNIP4 activity raises SLIT2's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 4.24× lower at baseline in the lines without KCNIP4 | 0.040 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[DELEC1]] | B | KCNIP4 activity raises DELEC1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 2.30× lower at baseline in the lines without KCNIP4 | 0.047 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[ITGA1]] | B | KCNIP4 activity raises ITGA1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 4.04× lower at baseline in the lines without KCNIP4 | 0.076 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[TRD-AS1]] | B | KCNIP4 activity raises TRD-AS1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without KCNIP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | B | KCNIP4 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express KCNIP4 (6) vs lines expressing it (42) | the lines without KCNIP4: 0.85× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |
| [[FER1L6]] | B | KCNIP4 activity raises FER1L6's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without KCNIP4 | 0.096 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.2, 27.7); signed map (34.7, 20.0). **Vector** length 80.6, 14.3% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.0 | +21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +13.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +15.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.9 | +12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.3 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.2 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.6 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel interacting protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.31-p15.2 — chr4:20,728,606-21,948,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CALP, KCHIP4, MGC44947 |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; EF-hand domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Phase 1 - inactivation of fast Na+ channels; Cardiac conduction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PIL6](https://www.uniprot.org/uniprotkb/Q6PIL6) (Kv channel-interacting protein 4):

> Regulatory subunit of Kv4/D (Shal)-type voltage-gated rapidly inactivating A-type potassium channels. Modulates KCND2 channel density, inactivation kinetics and rate of recovery from inactivation in a calcium-dependent and isoform-specific manner. Modulates KCND3/Kv4.3 currents. Isoform 4 does not increase KCND2 expression at the cell membrane. Isoform 4 retains KCND3 in the endoplasmic reticulum and negatively regulates its expression at the cell membrane.

**Summary**, from NCBI Gene [80333](https://www.ncbi.nlm.nih.gov/gene/80333):

> This gene encodes a member of the family of voltage-gated potassium (Kv) channel-interacting proteins (KCNIPs), which belong to the recoverin branch of the EF-hand superfamily. Members of the KCNIP family are small calcium binding proteins. They all have EF-hand-like domains, and differ from each other in the N-terminus. They are integral subunit components of native Kv4 channel complexes. They may regulate A-type currents, and hence neuronal excitability, in response to changes in …

**Accessions** — [HGNC:30083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30083) · Entrez [80333](https://www.ncbi.nlm.nih.gov/gene/80333) · UniProt [Q6PIL6](https://www.uniprot.org/uniprotkb/Q6PIL6) · Ensembl [ENSG00000185774](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185774)

## Data

Gene col 11730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11730); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11730]; `tensor/DDL_lfc|DDL_z.npy` [11730]; `embed/gene_vectors.npy` [11730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11730 or target_col == 11730). Every well: [[KCNIP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNIP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
