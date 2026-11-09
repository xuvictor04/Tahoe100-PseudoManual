---
symbol: "TRIM16L"
type: "gene"
col: 2949
ensembl_id: "ENSG00000108448"
name: "tripartite motif containing 16 like (pseudogene)"
location: "17p11.2"
module: 117
arm: "+"
pooled_cpm: 4.72
n_lines_expressing: 42
n_dd_up: 33
n_dd_down: 9
n_dd_up_clean: 25
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# TRIM16L

*tripartite motif containing 16 like (pseudogene)* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.76× (z +9.8, q 4e-20, up in 16 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.386× (z -9.2, q 2e-17, down in 25 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM16L-1]] (+0.81, fdr 7e-06, ⚠ same locus), [[NMRAL2P-1]] (+0.77, fdr 7e-06), [[ABCC2]] (+0.74, fdr 7e-06), [[TRIM16]] (+0.72, fdr 7e-06); moves opposite to [[RASA2]] (-0.57, fdr 1e-05), [[SNX25]] (-0.56, fdr 2e-05), [[MTMR14]] (-0.53, fdr 2e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 4 go from it, the strongest it → [[PRECSIT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.76×** | +9.8 | 4e-20 | 16/27 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.33×** | +8.2 | 6e-14 | 20/34 (LS 180, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +7.6 | 5e-12 | 11/28 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.1 | 2e-07 | 6/17 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.76×** | +5.5 | 4e-06 | 11/34 (HOP62, C32, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +5.5 | 4e-06 | 2/5 (J82, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.73×** | +5.3 | 7e-06 | 8/36 (J82, NCI-H1573, …) | rises with dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.72×** | +5.3 | 1e-05 | 12/38 (HT-29, SHP-77, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.73×** | +5.1 | 2e-05 | 12/33 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.68×** | +5.1 | 2e-05 | 16/37 (A549, J82, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +4.9 | 4e-05 | 10/37 (NCI-H1573, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.64×** | +4.6 | 2e-04 | 13/30 (NCI-H1573, J82, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.6 | 2e-04 | 1/9 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.62×** | +4.6 | 2e-04 | 7/36 (HT-29, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +4.5 | 2e-04 | 9/34 (A-172, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.38×** | +4.5 | 3e-04 | 11/38 (LoVo, NCI-H1573, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +4.4 | 4e-04 | 12/36 (HOP62, SNU-423, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.002 | 4/38 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.010 | 5/34 (NCI-H1573, A549, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2949.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -9.2 | 2e-17 | 25/38 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.548×** | -8.2 | 5e-14 | 17/27 (SHP-77, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -7.3 | 5e-11 | 23/36 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.545×** | -5.9 | 6e-07 | 18/38 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -5.5 | 4e-06 | 17/37 (SHP-77, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.618×** | -4.7 | 3e-04 | 13/35 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.627×** | -4.5 | 5e-04 | 16/24 (LoVo, J82, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.685×** | -3.7 | 0.018 | 9/36 (PANC-1, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.693×** | -3.6 | 0.024 | 6/38 (SW 900, LOX-IMVI, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 9.34 | 0 | 3 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0501× (z -12.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 25.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.2) |
| [[A498 (line)]] | wt | 17.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -8.6) |
| [[HOP62 (line)]] | alt | 2.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.44× (z +9.3) | — |
| [[LoVo (line)]] | wt | 6.03 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0872× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SW480 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.975 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.841 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM16L-1]] | +0.81 | +0.82 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NMRAL2P-1]] | +0.77 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ABCC2]] | +0.74 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRIM16]] | +0.72 | +0.71 / +0.76 | both halves | 7e-06 | STRING 740 |
| [[ALOX12P2-1]] | +0.71 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NMRAL2P]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[ME1]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CYP4F11]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[CAPS2]] | +0.67 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[ZSCAN31]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[FBXW10B]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 |  |
| [[LRP1B]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[EGF]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASA2]] | -0.57 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SNX25]] | -0.56 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MTMR14]] | -0.53 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[UHRF2]] | -0.52 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[KIAA1958]] | -0.51 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[STC1]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[PIGF]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.50 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MOSPD3]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[MARF1]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[TMEM158]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers TRIM16L's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds |
| [[ALOX12P2-1]] | B | ALOX12P2-1 activity raises TRIM16L's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without ALOX12P2-1 | 0.043 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent |
| [[MGST1]] | B | MGST1 activity raises TRIM16L's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without MGST1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[HDAC6]] | B | HDAC6 activity raises TRIM16L's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRECSIT]] | B | TRIM16L activity raises PRECSIT's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without TRIM16L | 0.013 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[TRIM16L-1]] | B | TRIM16L activity raises TRIM16L-1's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 2.40× lower at baseline in the lines without TRIM16L | 0.023 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[GSEC]] | B | TRIM16L activity raises GSEC's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.35× lower at baseline in the lines without TRIM16L | 0.064 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |
| [[TRIM16]] | B | TRIM16L activity raises TRIM16's level | lines that do not express TRIM16L (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without TRIM16L | 0.070 | ⚠ within organs, on part of the lines; also absent: DSCC1, FOXP4-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.856). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.7, 48.4); signed map (50.6, -9.7). **Vector** length 66.9, 12.7% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.58 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.58 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.58 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +7.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.7 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.4 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -7.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.0 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.1 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.0 | -5.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | +0.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 16 like (pseudogene) |
| Locus type | pseudogene |
| Location | 17p11.2 — chr17:18,722,237-18,735,460 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | TRIM70 |
| Matched by | ensembl_id |

UniProt [Q309B1](https://www.uniprot.org/uniprotkb/Q309B1) carries no function annotation.

**Summary**, from NCBI Gene [147166](https://www.ncbi.nlm.nih.gov/gene/147166):

> Predicted to be located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:32670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32670) · Entrez [147166](https://www.ncbi.nlm.nih.gov/gene/147166) · UniProt [Q309B1](https://www.uniprot.org/uniprotkb/Q309B1) · Ensembl [ENSG00000108448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108448)

## Data

Gene col 2949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2949); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2949]; `tensor/DDL_lfc|DDL_z.npy` [2949]; `embed/gene_vectors.npy` [2949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2949 or target_col == 2949). Every well: [[TRIM16L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM16L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
