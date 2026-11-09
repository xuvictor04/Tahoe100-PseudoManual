---
symbol: "COL7A1"
type: "gene"
col: 3535
ensembl_id: "ENSG00000114270"
name: "collagen type VII alpha 1 chain"
location: "3p21.31"
module: 13
arm: "+"
pooled_cpm: 60.53
n_lines_expressing: 26
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 26
direction_downstream: 46
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# COL7A1

*collagen type VII alpha 1 chain* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.73× (z +16.1, q 0e+00, up in 19 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.711× (z -3.9, q 0.054, down in 16 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H1792 0.135×, RPMI-7951 0.213×, HOP62 0.284×, HS-578T 0.244×, …; ⚠ cell-cycle shift, explains ~7% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HOP62 0.150×, H4 0.235×); [[Panobinostat (drug)]] 5 µM in 1 line (HOP62 0.221×; ⚠ cell-cycle shift, would explain all of this change); [[Retinoic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0688×); [[Belinostat (drug)]] 5 µM in 1 line (HOP62 0.256×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APCDD1L-DT]] (+0.70, fdr 7e-06), [[COL5A3]] (+0.66, fdr 7e-06), [[PHLDB1]] (+0.65, fdr 7e-06); moves opposite to [[ZFYVE9]] (-0.49, fdr 3e-05), [[SEC24B]] (-0.48, fdr 8e-05), [[PSMG2]] (-0.47, fdr 4e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 26 arrows point to it, the strongest [[COL5A3]] → it (grade B ⚠); 46 go from it, the strongest it → [[SYNJ2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3535.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.73×** | +16.1 | 0e+00 | 19/24 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.7 | 5e-12 | 9/23 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +6.5 | 2e-08 | 11/21 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.2 | 7e-08 | 11/21 (NCI-H460, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +5.9 | 3e-07 | 17/24 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 13/24 (Panc 03.27, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 1e-04 | 11/24 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +3.7 | 0.015 | 15/24 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3535.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 8 lines (NCI-H1792 0.135×, RPMI-7951 0.213×, HOP62 0.284×, HS-578T 0.244×, …; ⚠ cell-cycle shift, explains ~7% of this change); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HOP62 0.150×, H4 0.235×); [[Panobinostat (drug)]] 5 µM in 1 line (HOP62 0.221×; ⚠ cell-cycle shift, would explain all of this change); [[Retinoic acid (drug)]] 0.5 µM in 1 line (CHP-212 0.0688×); [[Belinostat (drug)]] 5 µM in 1 line (HOP62 0.256×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.054 | 16/24 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.748× | -3.3 | 0.24 | 13/24 (CHP-212, NCI-H460, …) | two highest doses | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | 0.745× | -3.2 | 0.25 | 6/24 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.761× | -3.1 | 0.25 | 3/24 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.768× | -3.0 | 0.28 | 19/24 (HOP62, H4, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3535. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 381 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +9.0) | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -12.7) |
| [[A549 (line)]] | wt | 102 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +16.8) | — |
| [[SW1417 (line)]] | alt | 19.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +18.5) | — |
| [[H4 (line)]] | wt | 97.6 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -10.0) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.235× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 131 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +12.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -8.8) ⚠ cell-cycle shift, explains ~7% of this change |
| [[J82 (line)]] | alt | 183 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.46× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H1792 (line)]] | alt | 180 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -17.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[Panc 03.27 (line)]] | alt | 21.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.54× (z +16.6) | — |
| [[PANC-1 (line)]] | alt | 26.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +20.1) | — |
| [[A-172 (line)]] | wt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.2) | — |
| [[A498 (line)]] | wt | 96.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +11.4) | — |
| [[CHP-212 (line)]] | wt | 28.7 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0688× (z -9.3) |
| [[Hs 766T (line)]] | wt | 49.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -8.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HS-578T (line)]] | alt | 322 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -11.9) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H460 (line)]] | wt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 396 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -15.0) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A-427 (line)]] | wt | 8.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.96 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 11.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.1 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 13.5 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.72 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.99 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3535), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APCDD1L-DT]] | +0.70 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[COL5A3]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 542 |
| [[PHLDB1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 | same gene group |
| [[APCDD1L]] | +0.62 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[CSF1R]] | +0.61 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[SHISAL1]] | +0.60 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[BMP1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 589 |
| [[SYNGAP1]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 | same gene group |
| [[VCAN]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[GRIN2A]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[COL5A1]] | +0.58 | +0.55 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 607 |
| [[SYNPO]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE9]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SEC24B]] | -0.48 | -0.37 / -0.41 | both halves | 8e-05 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 754 |
| [[PSMG2]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[INTS9]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[EBPL]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 3, C 23. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL5A3]] | B | COL5A3 activity raises COL7A1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.47× lower at baseline in the lines without COL5A3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[VSTM4]] | B | VSTM4 activity raises COL7A1's level | lines that do not express VSTM4 (31) vs lines expressing it (19) | 3.61× lower at baseline in the lines without VSTM4 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01411, KIRREL3, CCL2 |
| [[FBN1]] | B | FBN1 activity raises COL7A1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 3.20× lower at baseline in the lines without FBN1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[ADAMTS12]] | C | ADAMTS12 activity raises COL7A1's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 6.48× lower at baseline in the lines without ADAMTS12 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises COL7A1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 5.90× lower at baseline in the lines without COL5A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises COL7A1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 4.33× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises COL7A1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 5.82× lower at baseline in the lines without ITGA11 | 0.007 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[HTR1F]] | C | HTR1F activity raises COL7A1's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 3.75× lower at baseline in the lines without HTR1F | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises COL7A1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 3.85× lower at baseline in the lines without COL15A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises COL7A1's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without SHISAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[GNG2]] | C | GNG2 activity raises COL7A1's level | lines that do not express GNG2 (22) vs lines expressing it (28) | 3.37× lower at baseline in the lines without GNG2 | 0.021 | ⚠ within organs, on part of the lines; also absent: SNAI2, LBH, PLAT; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises COL7A1's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 4.27× lower at baseline in the lines without PTHLH | 0.023 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 19, C 27. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ2]] | B | COL7A1 activity raises SYNJ2's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.40× lower at baseline in the lines without COL7A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[PRSS23]] | B | COL7A1 activity raises PRSS23's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.07× lower at baseline in the lines without COL7A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[SYNJ2]] | B | COL7A1 activity strengthens SYNJ2's drug response | lines that do not express COL7A1 (21) vs lines expressing it (24) | the lines without COL7A1 respond 0.46× as strongly (z diff +2.80); strongest at Idarubicin (hydrochloride) 5 µM: 0.80x vs 0.46x (z diff +4.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC22A4]] | B | COL7A1 activity raises SLC22A4's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without COL7A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[SEPTIN9]] | B | COL7A1 activity raises SEPTIN9's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without COL7A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[CD82]] | B | COL7A1 activity raises CD82's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without COL7A1 | 0.027 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[CD44]] | B | COL7A1 activity raises CD44's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.91× lower at baseline in the lines without COL7A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[ARHGAP23]] | B | COL7A1 activity raises ARHGAP23's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without COL7A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[COL5A3]] | B | COL7A1 activity raises COL5A3's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without COL7A1 | 0.046 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[FAM20C]] | B | COL7A1 activity raises FAM20C's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 3.90× lower at baseline in the lines without COL7A1 | 0.047 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[LINC01500]] | B | COL7A1 activity raises LINC01500's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without COL7A1 | 0.052 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[TGFB1]] | B | COL7A1 activity raises TGFB1's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.56× lower at baseline in the lines without COL7A1 | 0.053 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.0, 14.2); signed map (21.2, 44.6). **Vector** length 88.4, 31.2% of its response variance represented; |z| ≥ 3 in 633 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ECM proteoglycans* (reactome, mean cos +0.51 to 8); *NCAM1 interactions* (reactome, mean cos +0.50 to 6); *Signaling by PDGF* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.6 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +7.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.4 | +1.4 |
| fall | [[Triamcinolone (drug)]] 0.5 µM |  | -2.5 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.3 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type VII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:48,564,073-48,595,329 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EBDCT, EBD1, EBR1 |
| Gene groups (HGNC) | Collagens; Fibronectin type III domain containing; MicroRNA protein coding host genes |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 18 pathways, smallest: Anchoring fibril formation; Fibronectin matrix formation; Cargo concentration in the ER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02388](https://www.uniprot.org/uniprotkb/Q02388) (Collagen alpha-1(VII) chain):

> Stratified squamous epithelial basement membrane protein that forms anchoring fibrils which may contribute to epithelial basement membrane organization and adherence by interacting with extracellular matrix (ECM) proteins such as type IV collagen.

**Summary**, from NCBI Gene [1294](https://www.ncbi.nlm.nih.gov/gene/1294):

> This gene encodes the alpha chain of type VII collagen. The type VII collagen fibril, composed of three identical alpha collagen chains, is restricted to the basement zone beneath stratified squamous epithelia. It functions as an anchoring fibril between the external epithelia and the underlying stroma. Mutations in this gene are associated with all forms of dystrophic epidermolysis bullosa. In the absence of mutations, however, an acquired form of this disease can result from an autoimmune …

**Accessions** — [HGNC:2214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2214) · Entrez [1294](https://www.ncbi.nlm.nih.gov/gene/1294) · UniProt [Q02388](https://www.uniprot.org/uniprotkb/Q02388) · Ensembl [ENSG00000114270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114270)

## Data

Gene col 3535: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3535); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3535, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3535]; `tensor/DDL_lfc|DDL_z.npy` [3535]; `embed/gene_vectors.npy` [3535]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3535 or target_col == 3535). Every well: [[COL7A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL7A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
