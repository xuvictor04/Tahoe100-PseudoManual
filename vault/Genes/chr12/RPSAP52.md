---
symbol: "RPSAP52"
type: "gene"
col: 14286
ensembl_id: "ENSG00000241749"
name: "ribosomal protein SA pseudogene 52"
location: "12q14.3"
module: 147
arm: "+"
pooled_cpm: 30.06
n_lines_expressing: 30
n_dd_up: 20
n_dd_down: 50
n_dd_up_clean: 17
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 35
direction_downstream: 23
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# RPSAP52

*ribosomal protein SA pseudogene 52* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.81× (z +9.5, q 1e-18, up in 7 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.207× (z -17.8, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02454]] (+0.79, fdr 7e-06), [[ARHGAP22]] (+0.76, fdr 7e-06), [[MIR100HG]] (+0.75, fdr 7e-06).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[NAV3]] → it (grade B ⚠); 23 go from it, the strongest it → [[HMGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +9.5 | 1e-18 | 7/26 (HT-29, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +6.3 | 1e-07 | 17/28 (SNU-423, Panc 03.27, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.69×** | +6.0 | 4e-07 | 20/28 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.0 | 4e-07 | 13/26 (SW48, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.44×** | +5.9 | 5e-07 | 18/28 (C32, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +5.6 | 2e-06 | 12/27 (C32, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 1e-05 | 13/28 (PANC-1, C32, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.54×** | +4.9 | 5e-05 | 15/27 (RPMI-7951, C32, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.53×** | +4.8 | 9e-05 | 12/25 (RPMI-7951, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.7 | 2e-04 | 3/18 (C32, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.48×** | +4.5 | 3e-04 | 11/26 (HS-578T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.55×** | +4.4 | 6e-04 | 16/27 (RPMI-7951, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.001 | 14/28 (SW48, C32, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.009 | 12/27 (C32, RPMI-7951, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.019 | 15/28 (HOP62, SW 900, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.019 | 4/28 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.019 | 8/25 (SW 900, C32, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.36×** | +3.2 | 0.038 | 6/25 (NCI-H23, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 3 with an alert ⚠; shown: the 15 strongest. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.207×** | -17.8 | 0e+00 | 26/28 (RKO, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.239×** | -16.1 | 0e+00 | 26/28 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.278×** | -14.4 | 6e-45 | 25/28 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.359×** | -11.6 | 6e-29 | 24/28 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.383×** | -9.4 | 5e-19 | 21/25 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.532×** | -8.7 | 2e-16 | 23/28 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.472×** | -8.5 | 2e-15 | 22/28 (HS-578T, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.474×** | -8.4 | 3e-15 | 22/28 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.500×** | -8.0 | 6e-14 | 21/28 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.461×** | -7.6 | 2e-12 | 19/27 (HS-578T, RKO, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.565×** | -7.5 | 2e-12 | 20/28 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.541×** | -6.9 | 2e-10 | 19/28 (HEC-1-A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.581×** | -6.1 | 5e-08 | 18/27 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.592×** | -5.9 | 1e-07 | 19/28 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.555×** | -5.8 | 3e-07 | 19/27 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 193 | 0 | 20 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0931× (z -16.3) |
| [[HS-578T (line)]] | alt | 176 | 0 | 19 (5 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0126× (z -21.1) |
| [[RKO (line)]] | wt | 235 | 0 | 19 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0586× (z -22.7) |
| [[NCI-H1792 (line)]] | alt | 90.5 | 0 | 15 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.380× (z -18.5) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.0448× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 47.8 | 0 | 14 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0369× (z -17.5) |
| [[Hs 766T (line)]] | wt | 52.0 | 0 | 13 | — | [[Panobinostat (drug)]] 5 µM 0.0509× (z -14.0) |
| [[SW48 (line)]] | wt | 155 | 3 (1 ⚠) | 7 | [[Homoharringtonine (drug)]] 0.5 µM 8.38× (z +10.9) | [[Cobimetinib (drug)]] 5 µM 0.109× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0267× (z -17.8) |
| [[RPMI-7951 (line)]] | alt | 59.7 | 1 (1 ⚠) | 6 (1 ⚠) | [[Daptomycin (drug)]] 5 µM 5.15× (z +8.6) ⚠ unreliable plate only | [[Panobinostat (drug)]] 0.5 µM 0.0524× (z -15.4) |
| [[CFPAC-1 (line)]] | alt | 22.7 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.123× (z -10.4) |
| [[LOX-IMVI (line)]] | wt | 37.0 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0368× (z -17.9) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -10.8) |
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -11.7) |
| [[HT-29 (line)]] | alt | 7.67 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 6.18× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0946× (z -9.0) |
| [[J82 (line)]] | alt | 9.12 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0605× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 16.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -10.0) |
| [[C32 (line)]] | wt | 18.1 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.0502× (z -9.5) |
| [[H4 (line)]] | wt | 17.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0587× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.573× (z -8.8) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 9.42 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0438× (z -11.9) |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0885× (z -11.2) |
| [[SW 900 (line)]] | alt | 48.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -10.0) |
| [[A-172 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.42 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02454]] | +0.79 | +0.82 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[ARHGAP22]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[MIR100HG]] | +0.75 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NT5E]] | +0.72 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[RDUR]] | +0.69 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.69 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[ELK3]] | +0.67 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.67 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[EVA1A]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 19, C 16. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NAV3]] | B | NAV3 activity raises RPSAP52's level | lines that do not express NAV3 (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without NAV3 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises RPSAP52's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without PDCD1LG2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[BCL2A1]] | B | BCL2A1 activity raises RPSAP52's level | lines that do not express BCL2A1 (26) vs lines expressing it (24) | 2.92× lower at baseline in the lines without BCL2A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: BASP1-AS1, TMEM156, CSGALNACT1 |
| [[HMGA2]] | B | HMGA2 activity raises RPSAP52's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 4.34× lower at baseline in the lines without HMGA2 | 0.029 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[STC1]] | B | STC1 activity raises RPSAP52's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without STC1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[PTPRE]] | B | PTPRE activity raises RPSAP52's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without PTPRE | 0.041 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[RAI14]] | B | RAI14 activity raises RPSAP52's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 3.12× lower at baseline in the lines without RAI14 | 0.043 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[RFX8]] | B | RFX8 activity raises RPSAP52's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 3.56× lower at baseline in the lines without RFX8 | 0.043 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[GDNF]] | B | GDNF activity raises RPSAP52's level | lines that do not express GDNF (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without GDNF | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9 |
| [[MIR100HG]] | B | MIR100HG activity raises RPSAP52's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.83× lower at baseline in the lines without MIR100HG | 0.051 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[HTR7]] | B | HTR7 activity raises RPSAP52's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.11× lower at baseline in the lines without HTR7 | 0.051 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[MAP2K1]] | B | MAP2K1 activity raises RPSAP52's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 9.2% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 17, C 6. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | RPSAP52 activity raises HMGA2's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 5.43× lower at baseline in the lines without RPSAP52 | 1e-04 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[HMGA2-AS1]] | B | RPSAP52 activity raises HMGA2-AS1's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without RPSAP52 | 0.001 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[RASA3]] | B | RPSAP52 activity raises RASA3's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.72× lower at baseline in the lines without RPSAP52 | 0.010 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[C13orf46]] | B | RPSAP52 activity raises C13orf46's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.19× lower at baseline in the lines without RPSAP52 | 0.013 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[C11orf91]] | B | RPSAP52 activity raises C11orf91's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.05× lower at baseline in the lines without RPSAP52 | 0.015 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[MIR31HG]] | B | RPSAP52 activity raises MIR31HG's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without RPSAP52 | 0.025 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[HTR7]] | B | RPSAP52 activity raises HTR7's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without RPSAP52 | 0.035 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[PDE4DIPP2]] | B | RPSAP52 activity raises PDE4DIPP2's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.13× lower at baseline in the lines without RPSAP52 | 0.036 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[FMNL3]] | B | RPSAP52 activity raises FMNL3's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without RPSAP52 | 0.042 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[HMGA2-AS1]] | B | RPSAP52 activity strengthens HMGA2-AS1's drug response | lines that do not express RPSAP52 (20) vs lines expressing it (28) | the lines without RPSAP52 respond 0.69× as strongly (z diff +0.85); strongest at Panobinostat 5 µM: 0.75x vs 0.45x (z diff +2.3) | 0.047 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[LAMA4]] | B | RPSAP52 activity raises LAMA4's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 3.88× lower at baseline in the lines without RPSAP52 | 0.050 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[RFX8]] | B | RPSAP52 activity raises RFX8's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 3.19× lower at baseline in the lines without RPSAP52 | 0.066 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.798). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.8, 9.2); signed map (12.7, 47.4). **Vector** length 117, 32.9% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.5 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +5.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +4.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -6.0 | -11.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.8 | -8.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.3 | -8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -8.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.2 | -7.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.8 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein SA pseudogene 52 |
| Locus type | pseudogene |
| Location | 12q14.3 — chr12:65,758,121-65,758,998 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:35752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35752) · Entrez [204010](https://www.ncbi.nlm.nih.gov/gene/204010) · Ensembl [ENSG00000241749](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241749)

## Data

Gene col 14286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14286); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14286]; `tensor/DDL_lfc|DDL_z.npy` [14286]; `embed/gene_vectors.npy` [14286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14286 or target_col == 14286). Every well: [[RPSAP52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPSAP52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
