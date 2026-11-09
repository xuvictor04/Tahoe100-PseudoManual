---
symbol: "FMN2"
type: "gene"
col: 7919
ensembl_id: "ENSG00000155816"
name: "formin 2"
location: "1q43"
module: 9
arm: "+"
pooled_cpm: 14.25
n_lines_expressing: 24
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 17
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 25
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# FMN2

*formin 2* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.61× (z +18.6, q 0e+00, up in 15 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0647×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.176×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH18]] (+0.75, fdr 7e-06), [[DMD]] (+0.72, fdr 7e-06), [[PIEZO2]] (+0.68, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TRPC4]] → it (grade C ⚠); 25 go from it, the strongest it → cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.61×** | +18.6 | 0e+00 | 15/20 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +18.1 | 0e+00 | 7/18 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +17.0 | 0e+00 | 7/14 (H4, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +16.8 | 0e+00 | 9/21 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +13.5 | 2e-39 | 20/22 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +11.3 | 8e-28 | 6/15 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.13×** | +10.3 | 4e-23 | 13/20 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.03×** | +9.7 | 2e-20 | 14/21 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.99×** | +9.4 | 2e-19 | 16/21 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +7.9 | 2e-13 | 11/21 (SK-MEL-2, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +7.3 | 2e-11 | 15/21 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +6.6 | 2e-09 | 16/21 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +6.3 | 2e-08 | 14/21 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +5.2 | 9e-06 | 7/20 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.9 | 4e-05 | 3/21 (hTERT-HPNE, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +4.7 | 1e-04 | 14/22 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 1e-04 | 10/21 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.90×** | +4.6 | 1e-04 | 11/21 (SNU-423, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.4 | 3e-04 | 8/21 (SNU-423, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.31×** | +3.7 | 0.005 | 7/20 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0647×; ⚠ cell-cycle shift, explains ~52% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.122×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H23 0.123×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A-427 0.176×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.7 | 0.15 | 2/22 (NCI-H1792, BT-474) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.841× | -3.3 | 0.25 | 6/22 (SW 1088, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.50 | 8 | 0 | [[Tucidinostat (drug)]] 5 µM 10.9× (z +18.0) | — |
| [[A498 (line)]] | wt | 4.79 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +19.5) | — |
| [[HOP62 (line)]] | alt | 11.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.15× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 18.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -10.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 146 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.09× (z +18.0) | — |
| [[hTERT-HPNE (line)]] | wt | 70.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +19.2) | — |
| [[RPMI-7951 (line)]] | alt | 39.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +20.7) | — |
| [[SK-MEL-2 (line)]] | alt | 7.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 64.2× (z +20.3) | — |
| [[A-427 (line)]] | wt | 15.3 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.53× (z +9.0) | [[Ixazomib citrate (drug)]] 0.5 µM 0.176× (z -8.7) |
| [[H4 (line)]] | wt | 20.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +11.3) | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0647× (z -11.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[J82 (line)]] | alt | 4.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.1× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 70.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.35× (z +21.6) | — |
| [[HS-578T (line)]] | alt | 5.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +13.8) | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +9.7) | — |
| [[A549 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH18]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[DMD]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PIEZO2]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[RGS7]] | +0.67 | +0.65 / +0.68 | both halves | 7e-06 | same gene group; STRING 449 |
| [[TMPRSS15]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[FSTL5]] | +0.64 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[MSR1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[KCNH1]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[EPHA5]] | +0.64 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[NEGR1]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SNTG2]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[PCSK2]] | +0.62 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPC4]] | C | TRPC4 activity raises FMN2's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.76× lower at baseline in the lines without TRPC4 | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[FAM133A]] | C | FAM133A activity raises FMN2's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without FAM133A | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises FMN2's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.97× lower at baseline in the lines without LINC01885 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises FMN2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 2.81× lower at baseline in the lines without MGAT4C | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[LINC02506]] | C | LINC02506 activity raises FMN2's level | lines that do not express LINC02506 (40) vs lines expressing it (10) | 3.83× lower at baseline in the lines without LINC02506 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OVAAL, LINC01610, ENSG00000241168; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises FMN2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.22× lower at baseline in the lines without SLC6A17 | 0.051 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[ERC2]] | C | ERC2 activity raises FMN2's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 2.86× lower at baseline in the lines without ERC2 | 0.062 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent; co-absent with the target |
| [[ERBB4]] | C | ERBB4 activity raises FMN2's level | lines that do not express ERBB4 (33) vs lines expressing it (17) | 2.81× lower at baseline in the lines without ERBB4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, NETO1, CDH10; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises FMN2's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 3.38× lower at baseline in the lines without SCN3A | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[FSTL5]] | C | FSTL5 activity raises FMN2's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 3.18× lower at baseline in the lines without FSTL5 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2; co-absent with the target |
| [[SNTG2]] | C | SNTG2 activity raises FMN2's level | lines that do not express SNTG2 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without SNTG2 | 0.080 | ⚠ within organs, on part of the lines; also absent: TENM4, CRMP1, ENSG00000240086; maybe low, not absent; co-absent with the target |
| [[PCDH10]] | C | PCDH10 activity raises FMN2's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 3.84× lower at baseline in the lines without PCDH10 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 9, C 16. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | FMN2 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 1.25× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[LINC01117]] | B | FMN2 activity raises LINC01117's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.68× lower at baseline in the lines without FMN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[OFCC1]] | B | FMN2 activity raises OFCC1's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without FMN2 | 0.068 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| cells under [[(S)-Crizotinib (drug)]] 0.5 µM | B | FMN2 activity raises the cells' numbers under (S)-Crizotinib 0.5 µM (protects the cells) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 0.85× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[TMEFF2]] | B | FMN2 activity raises TMEFF2's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 1.85× lower at baseline in the lines without FMN2 | 0.077 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[ADAMTSL1]] | B | FMN2 activity raises ADAMTSL1's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without FMN2 | 0.084 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| cells under [[Omeprazole (drug)]] 5 µM | B | FMN2 activity raises the cells' numbers under Omeprazole 5 µM (protects the cells) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 0.90× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| cells under [[Peretinoin (drug)]] 5 µM | B | FMN2 activity lowers the cells' numbers under Peretinoin 5 µM (makes them more sensitive) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | FMN2 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 1.16× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[TRPC4]] | C | FMN2 activity raises TRPC4's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.75× lower at baseline in the lines without FMN2 | 0.004 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[EPHA5]] | C | FMN2 activity raises EPHA5's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.35× lower at baseline in the lines without FMN2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[SNAP25]] | C | FMN2 activity raises SNAP25's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 5.45× lower at baseline in the lines without FMN2 | 0.018 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 29.6); signed map (39.0, 31.0). **Vector** length 63.8, 17.0% of its response variance represented; |z| ≥ 3 in 580 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +18.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +17.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +18.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +13.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +1.3 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.1 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.9 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | formin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:240,014,348-240,475,187 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Formins; DEP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ56](https://www.uniprot.org/uniprotkb/Q9NZ56) (Formin-2):

> Actin-binding protein that is involved in actin cytoskeleton assembly and reorganization. Acts as an actin nucleation factor and promotes assembly of actin filaments together with SPIRE1 and SPIRE2. Involved in intracellular vesicle transport along actin fibers, providing a novel link between actin cytoskeleton dynamics and intracellular transport (By similarity). Required for asymmetric spindle positioning, asymmetric oocyte division and polar body extrusion during female germ cell meiosis (By …

**Summary**, from NCBI Gene [56776](https://www.ncbi.nlm.nih.gov/gene/56776):

> This gene is a member of the formin homology protein family. The encoded protein is thought to have essential roles in organization of the actin cytoskeleton and in cell polarity. This protein mediates the formation of an actin mesh that positions the spindle during oogenesis and also regulates the formation of actin filaments in the nucleus. This protein also forms a perinuclear actin/focal-adhesion system that regulates the shape and position of the nucleus during cell migration. Mutations in …

**Accessions** — [HGNC:14074](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14074) · Entrez [56776](https://www.ncbi.nlm.nih.gov/gene/56776) · UniProt [Q9NZ56](https://www.uniprot.org/uniprotkb/Q9NZ56) · Ensembl [ENSG00000155816](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155816)

## Data

Gene col 7919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7919); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7919]; `tensor/DDL_lfc|DDL_z.npy` [7919]; `embed/gene_vectors.npy` [7919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7919 or target_col == 7919). Every well: [[FMN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
