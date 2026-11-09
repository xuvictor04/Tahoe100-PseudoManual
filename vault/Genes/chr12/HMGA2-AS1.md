---
symbol: "HMGA2-AS1"
type: "gene"
col: 12377
ensembl_id: "ENSG00000197301"
name: "HMGA2 antisense RNA 1"
location: "12q14.3"
module: 147
arm: "+"
pooled_cpm: 7.71
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 14
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# HMGA2-AS1

*HMGA2 antisense RNA 1* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.37× (z +9.8, q 4e-20, up in 6 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Betamethasone dipropionate (drug)]] 0.5 µM: 1.34× (z +3.4, q 0.068, up in 11 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 4.10×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.854× (z -6.5, q 5e-08, down in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.584× (z -6.3, q 1e-07, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HMGA2]] (+0.76, fdr 7e-06, ⚠ same locus), [[RPSAP52]] (+0.66, fdr 7e-06), [[CLMP]] (+0.64, fdr 7e-06), [[MAP4K4]] (+0.62, fdr 1e-05); moves opposite to [[GPRC5B]] (-0.55, fdr 1e-05), [[HINT3]] (-0.49, fdr 2e-05), [[TRIM34]] (-0.48, fdr 5e-05).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[RPSAP52]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12377.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HS-578T 4.10×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.37×** | +9.8 | 4e-20 | 6/15 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.7 | 1e-19 | 25/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +7.4 | 2e-11 | 10/22 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.9 | 0.014 | 14/41 (A-172, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.068 | 11/46 (AsPC-1, A498, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.11 | 11/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -6.5 | 5e-08 | 20/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -6.3 | 1e-07 | 26/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.665×** | -4.8 | 2e-04 | 22/46 (NCI-H2030, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.662×** | -4.8 | 2e-04 | 17/47 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.671×** | -4.4 | 0.001 | 14/47 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.706×** | -4.1 | 0.003 | 22/47 (H4, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.700×** | -4.1 | 0.003 | 16/48 (HOP62, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.713×** | -3.8 | 0.008 | 16/45 (C32, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.731×** | -3.7 | 0.013 | 15/48 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.775×** | -3.4 | 0.032 | 10/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -3.4 | 0.034 | 12/48 (RPMI-7951, H4, …) | all doses, flat | position effect removed |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.742×** | -3.3 | 0.054 | 10/45 (C32, CFPAC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.806×** | -3.1 | 0.091 | 13/48 (HOP62, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 3 (1 ⚠) | — | [[Roxadustat (drug)]] 0.05 µM 0.0608× (z -12.4) |
| [[HOP62 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.602× (z -10.4) ⚠ position not correctable · without an alert: [[Belinostat (drug)]] 5 µM 0.219× (z -8.6) |
| [[A549 (line)]] | wt | 7.08 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0558× (z -12.5) |
| [[HS-578T (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.516× (z -10.8) ⚠ position not correctable |
| [[NCI-H2030 (line)]] | alt | 6.45 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.129× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 7.13 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0989× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0458× (z -9.4) |
| [[A-172 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGA2]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RPSAP52]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[CLMP]] | +0.64 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[MAP4K4]] | +0.62 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[RFX8]] | +0.62 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[COL23A1]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[C2orf92]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[DNMBP-AS1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | same gene group |
| [[TOP1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PLCG1-AS1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 | same gene group |
| [[LINC02454]] | +0.58 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[MRC2]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRC5B]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[HINT3]] | -0.49 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TRIM34]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[FYCO1]] | -0.47 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TLR3]] | -0.47 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[FRK]] | -0.45 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[PIK3C2B]] | -0.45 | -0.42 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPSAP52]] | B | RPSAP52 activity raises HMGA2-AS1's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without RPSAP52 | 0.001 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[MSRB3]] | B | MSRB3 activity raises HMGA2-AS1's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without MSRB3 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[MAP2K1]] | B | MAP2K1 activity raises HMGA2-AS1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[LINC02454]] | B | LINC02454 activity raises HMGA2-AS1's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without LINC02454 | 0.036 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[TSHZ3]] | B | TSHZ3 activity raises HMGA2-AS1's level | lines that do not express TSHZ3 (25) vs lines expressing it (25) | 1.43× lower at baseline in the lines without TSHZ3 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B |
| [[PDGFRA]] | B | PDGFRA activity raises HMGA2-AS1's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 1.42× lower at baseline in the lines without PDGFRA | 0.042 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1 |
| [[RPSAP52]] | B | RPSAP52 activity strengthens HMGA2-AS1's drug response | lines that do not express RPSAP52 (20) vs lines expressing it (28) | the lines without RPSAP52 respond 0.69× as strongly (z diff +0.85); strongest at Panobinostat 5 µM: 0.75x vs 0.45x (z diff +2.3) | 0.047 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[AKAP12]] | B | AKAP12 activity raises HMGA2-AS1's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without AKAP12 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[ADAMTS18]] | B | ADAMTS18 activity raises HMGA2-AS1's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without ADAMTS18 | 0.056 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent |
| [[ERRFI1-DT]] | B | ERRFI1-DT activity lowers HMGA2-AS1's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.26× higher at baseline in the lines without ERRFI1-DT | 0.059 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HMGA2-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises HMGA2-AS1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.668). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.5, 9.0); signed map (12.1, 46.9). **Vector** length 64.4, 9.20% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.5 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.6 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | HMGA2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q14.3 — chr12:65,851,340-65,882,167 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RP11-366L20.2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53973) · Entrez [100129940](https://www.ncbi.nlm.nih.gov/gene/100129940) · Ensembl [ENSG00000197301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197301)

## Data

Gene col 12377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12377); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12377]; `tensor/DDL_lfc|DDL_z.npy` [12377]; `embed/gene_vectors.npy` [12377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12377 or target_col == 12377). Every well: [[HMGA2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGA2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
