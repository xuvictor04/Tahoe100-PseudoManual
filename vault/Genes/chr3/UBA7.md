---
symbol: "UBA7"
type: "gene"
col: 11253
ensembl_id: "ENSG00000182179"
name: "ubiquitin like modifier activating enzyme 7"
location: "3p21.31"
module: 32
arm: "+"
pooled_cpm: 4.29
n_lines_expressing: 41
n_dd_up: 10
n_dd_down: 38
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 48
direction_downstream: 55
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# UBA7

*ubiquitin like modifier activating enzyme 7* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.72× (z +4.2, q 0.007, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Binimetinib (drug)]] 5 µM: 1.65× (z +4.1, q 0.007, up in 11 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 0.337× (z -8.9, q 4e-16, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A3]] (+0.83, fdr 7e-06), [[TRIM22]] (+0.79, fdr 7e-06), [[PARP10]] (+0.78, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 48 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 55 go from it, the strongest it → [[TNFRSF14]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11253.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +4.2 | 0.007 | 2/8 (A-172, RPMI-7951) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +4.1 | 0.007 | 11/39 (AsPC-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.007 | 14/32 (LoVo, Hs 766T, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **1.41×** | +3.9 | 0.016 | 7/36 (AsPC-1, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.055 | 8/39 (AsPC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.055 | 6/35 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.55×** | +3.4 | 0.056 | 5/34 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.056 | 7/38 (SNU-423, A498, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.75×** | +3.2 | 0.078 | 5/30 (AsPC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.084 | 6/35 (AsPC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11253.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **0.337×** | -8.9 | 4e-16 | 25/36 (RPMI-7951, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.383×** | -7.8 | 1e-12 | 22/29 (RPMI-7951, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.514×** | -7.7 | 3e-12 | 25/30 (SNU-423, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.425×** | -7.0 | 4e-10 | 23/36 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.426×** | -7.0 | 4e-10 | 25/37 (H4, Hs 766T, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.425×** | -6.7 | 2e-09 | 21/33 (A-172, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.428×** | -6.5 | 5e-09 | 21/34 (HT-29, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.476×** | -6.1 | 1e-07 | 18/35 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -5.5 | 2e-06 | 21/34 (MIA PaCa-2, LoVo, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.504×** | -5.4 | 4e-06 | 17/25 (RPMI-7951, A-172, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.526×** | -5.2 | 8e-06 | 18/34 (PANC-1, H4, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.529×** | -5.2 | 9e-06 | 16/36 (AsPC-1, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.540×** | -5.0 | 2e-05 | 16/31 (NCI-H2347, LoVo, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.657×** | -4.9 | 5e-05 | 16/35 (A-172, RPMI-7951, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.564×** | -4.7 | 1e-04 | 18/34 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.373×** | -4.2 | 9e-04 | 14/33 (LoVo, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.603×** | -4.1 | 0.001 | 17/36 (RPMI-7951, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.701×** | -4.1 | 0.001 | 14/36 (Panc 03.27, J82, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.388×** | -4.0 | 0.002 | 15/32 (LoVo, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -3.9 | 0.002 | 17/36 (NCI-H2347, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.726×** | -3.7 | 0.005 | 16/36 (NCI-H2347, NCI-H1573, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11253. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 13.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.132× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.111× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0492× (z -12.2) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0558× (z -12.8) |
| [[LoVo (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.190× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[MIA PaCa-2 (line)]] | alt | 3.97 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0298× (z -9.5) |
| [[SNU-423 (line)]] | alt | 7.65 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A-427 (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.583 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.888 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11253), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A3]] | +0.83 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[TRIM22]] | +0.79 | +0.77 / +0.80 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 407 |
| [[PARP10]] | +0.78 | +0.72 / +0.81 | both halves | 7e-06 | STRING 478 |
| [[EPSTI1]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI44L]] | +0.74 | +0.72 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[XAF1]] | +0.74 | +0.71 / +0.76 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 492 |
| [[TNFSF10]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[OAS2]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 430 |
| [[APOL1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[IFI44]] | +0.72 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 411 |
| [[TRANK1]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SAMD9L]] | +0.71 | +0.63 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 42, C 6. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises UBA7's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.36× lower at baseline in the lines without PLAAT4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[CD5L]] | B | CD5L activity raises UBA7's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without CD5L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises UBA7's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.35× lower at baseline in the lines without EPSTI1 | 0.002 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[GBP4]] | B | GBP4 activity raises UBA7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.44× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFITM1]] | B | IFITM1 activity raises UBA7's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without IFITM1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[SAMD9L]] | B | SAMD9L activity raises UBA7's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.42× lower at baseline in the lines without SAMD9L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[APOL1]] | B | APOL1 activity raises UBA7's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without APOL1 | 0.005 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[RSAD2]] | B | RSAD2 activity raises UBA7's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without RSAD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[MX1]] | B | MX1 activity raises UBA7's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.75× lower at baseline in the lines without MX1 | 0.009 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[STING1]] | B | STING1 activity raises UBA7's level | lines that do not express STING1 (17) vs lines expressing it (33) | 2.07× lower at baseline in the lines without STING1 | 0.010 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[IFI44]] | B | IFI44 activity raises UBA7's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.08× lower at baseline in the lines without IFI44 | 0.013 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP1]] | B | GBP1 activity raises UBA7's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without GBP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |

### Downstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 50, C 5. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF14]] | B | UBA7 activity raises TNFRSF14's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without UBA7 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[IFITM1]] | B | UBA7 activity raises IFITM1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 7.01× lower at baseline in the lines without UBA7 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[PARP14]] | B | UBA7 activity raises PARP14's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without UBA7 | 0.006 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[PLSCR1]] | B | UBA7 activity raises PLSCR1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 3.33× lower at baseline in the lines without UBA7 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[SAMD9L]] | B | UBA7 activity raises SAMD9L's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.38× lower at baseline in the lines without UBA7 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[MX2]] | B | UBA7 activity raises MX2's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.51× lower at baseline in the lines without UBA7 | 0.009 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[GBP4]] | B | UBA7 activity raises GBP4's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 4.36× lower at baseline in the lines without UBA7 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[CFB]] | B | UBA7 activity raises CFB's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 5.67× lower at baseline in the lines without UBA7 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[IFI27]] | B | UBA7 activity raises IFI27's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 4.75× lower at baseline in the lines without UBA7 | 0.013 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[PARP10]] | B | UBA7 activity raises PARP10's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.16× lower at baseline in the lines without UBA7 | 0.013 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[DDX60]] | B | UBA7 activity raises DDX60's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.90× lower at baseline in the lines without UBA7 | 0.014 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[TRANK1]] | B | UBA7 activity raises TRANK1's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without UBA7 | 0.016 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.5, 52.5); signed map (63.6, 30.4). **Vector** length 75.5, 16.5% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.60 to 60); *interferon* (control, mean cos +0.65 to 23); *Interferon alpha/beta signaling* (reactome, mean cos +0.63 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.9 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.9 | -8.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.6 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin like modifier activating enzyme 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,805,209-49,813,953 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D8, UBE2, UBA1B; previously UBE1L |
| Gene groups (HGNC) | Ubiquitin like modifier activating enzymes; MicroRNA protein coding host genes |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 18 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Termination of translesion DNA synthesis; Negative regulators of DDX58/IFIH1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P41226](https://www.uniprot.org/uniprotkb/P41226) (Ubiquitin-like modifier-activating enzyme 7):

> E1-activating enzyme that catalyzes the covalent conjugation of the ubiquitin-like protein product of ISG15 to additional interferon stimulated proteins (ISGs) as well as other cellular proteins such as P53 in a process termed protein ISGylation. Plays an essential role in antiviral immunity together with ISG15 by restricting the replication of many viruses including rabies virus, influenza virus, sindbis virus, rotavirus or human cytomegalovirus. For example, ISG15 modification of influenza A …

**Summary**, from NCBI Gene [7318](https://www.ncbi.nlm.nih.gov/gene/7318):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E1 ubiquitin-activating enzyme family. The encoded enzyme is a retinoid target that triggers promyelocytic leukemia (PML)/retinoic acid receptor …

**Accessions** — [HGNC:12471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12471) · Entrez [7318](https://www.ncbi.nlm.nih.gov/gene/7318) · UniProt [P41226](https://www.uniprot.org/uniprotkb/P41226) · Ensembl [ENSG00000182179](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182179)

## Data

Gene col 11253: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11253); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11253, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11253]; `tensor/DDL_lfc|DDL_z.npy` [11253]; `embed/gene_vectors.npy` [11253]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11253 or target_col == 11253). Every well: [[UBA7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBA7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
