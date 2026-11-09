---
symbol: "LDOC1"
type: "gene"
col: 11256
ensembl_id: "ENSG00000182195"
name: "LDOC1 regulator of NFKB signaling"
location: "Xq27.1"
module: 42
arm: "+"
pooled_cpm: 7.17
n_lines_expressing: 29
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 13
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# LDOC1

*LDOC1 regulator of NFKB signaling* — Xq27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.56× (z +11.4, q 3e-27, up in 12 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.47× (z +4.9, q 1e-04, up in 13 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.304× (z -21.2, q 0e+00, down in 22 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[F2R]] (+0.59, fdr 2e-05), [[LINC00632]] (+0.57, fdr 1e-05), [[FKBP7]] (+0.56, fdr 2e-05); moves opposite to [[TNIP2]] (-0.46, fdr 3e-05), [[DHX58]] (-0.44, fdr 5e-05), [[LIME1]] (-0.44, fdr 7e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPANXA2-OT1]] → it (grade C ⚠); 13 go from it, the strongest it → [[HTRA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11256.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +11.4 | 3e-27 | 12/13 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +9.3 | 4e-18 | 12/18 (NCI-H2030, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +7.2 | 9e-11 | 11/15 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +4.9 | 1e-04 | 13/27 (HEC-1-A, A498, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.015 | 11/26 (NCI-H2347, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.068 | 3/25 (A498, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.17 | 4/22 (NCI-H23, NCI-H1573, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11256.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.304×** | -21.2 | 0e+00 | 22/24 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.413×** | -11.1 | 2e-26 | 20/24 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.494×** | -8.5 | 3e-15 | 20/24 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.528×** | -8.0 | 1e-13 | 15/24 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -5.7 | 2e-06 | 14/25 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -5.6 | 2e-06 | 11/27 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.639×** | -5.3 | 9e-06 | 15/25 (J82, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -5.2 | 2e-05 | 14/25 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.670×** | -5.0 | 3e-05 | 10/25 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.704×** | -4.4 | 6e-04 | 9/25 (HEC-1-A, hTERT-HPNE, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.006 | 7/25 (NCI-H1573, SW 1271, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.750×** | -3.5 | 0.023 | 10/23 (NCI-H460, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.759×** | -3.5 | 0.023 | 10/26 (HEC-1-A, HS-578T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.780× | -3.0 | 0.11 | 6/24 (NCI-H2030, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11256. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -17.1) |
| [[NCI-H2030 (line)]] | alt | 29.2 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -19.5) |
| [[HEC-1-A (line)]] | alt | 16.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.18× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.1) |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.5) |
| [[J82 (line)]] | alt | 8.39 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0443× (z -14.9) |
| [[A-172 (line)]] | wt | 8.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.2) |
| [[A549 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.6) |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.6) |
| [[HS-578T (line)]] | alt | 9.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 5.70 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0647× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -16.2) |
| [[SNU-423 (line)]] | alt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0811× (z -18.4) |
| [[A-427 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.746 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.689 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.802 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.598 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.700 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.815 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.650 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11256), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F2R]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[LINC00632]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[FKBP7]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[GGCX]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[EHD3]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[DKK3]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[HTRA1]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SPARC]] | +0.53 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[PCDHGC3]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SLITRK4]] | +0.52 | +0.55 / +0.36 | both halves | 1e-04 |  |
| [[P3H1]] | +0.52 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[NOMO2]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNIP2]] | -0.46 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[DHX58]] | -0.44 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[LIME1]] | -0.44 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[BCL2L13]] | -0.44 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ETS2]] | -0.43 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[NINJ1]] | -0.43 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[PNLIPRP3]] | -0.43 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[CEBPD]] | -0.42 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[FDX2]] | -0.42 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[EIF4EBP3]] | -0.42 | -0.45 / -0.32 | both halves | 1e-04 |  |
| [[PRDM16]] | -0.42 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[TRIM47]] | -0.42 | -0.35 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPANXA2-OT1]] | C | SPANXA2-OT1 activity raises LDOC1's level | lines that do not express SPANXA2-OT1 (22) vs lines expressing it (28) | 6.67× lower at baseline in the lines without SPANXA2-OT1 | 1e-04 | ⚠ within organs, on part of the lines; also absent: LDOC1, S1PR3, SH3GL3; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 5, C 8. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTRA1]] | B | LDOC1 activity raises HTRA1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 2.36× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; its own permutation p |
| [[P3H1]] | B | LDOC1 activity raises P3H1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 1.73× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; its own permutation p |
| [[FKBP7]] | B | LDOC1 activity raises FKBP7's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; its own permutation p |
| [[SPARC]] | B | LDOC1 activity raises SPARC's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 3.81× lower at baseline in the lines without LDOC1 | 0.071 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91 |
| [[FKBP1A]] | B | LDOC1 activity raises FKBP1A's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 1.16× lower at baseline in the lines without LDOC1 | 0.087 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91 |
| [[SPANXA2-OT1]] | C | LDOC1 activity raises SPANXA2-OT1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 7.02× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[COL3A1]] | C | LDOC1 activity raises COL3A1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.52× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[DKK3]] | C | LDOC1 activity raises DKK3's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 3.50× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[EHD3]] | C | LDOC1 activity raises EHD3's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 2.76× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[FSTL1]] | C | LDOC1 activity raises FSTL1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.05× lower at baseline in the lines without LDOC1 | 0.070 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target |
| [[FHL1]] | C | LDOC1 activity raises FHL1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.09× lower at baseline in the lines without LDOC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |
| [[COL4A6]] | C | LDOC1 activity raises COL4A6's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without LDOC1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (60.4, 18.5); signed map (22.8, 41.1). **Vector** length 49.5, 10.1% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +4.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -21.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.6 | -11.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -5.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | LDOC1 regulator of NFKB signaling |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq27.1 — chrX:141,111,605-141,177,129 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Mar7, Mart7, SIRH7, RTL7; previously BCUR1 |
| Gene groups (HGNC) | Retrotransposon Gag like family |
| Matched by | ensembl_id |

**Function**, from UniProt [O95751](https://www.uniprot.org/uniprotkb/O95751) (Protein LDOC1):

> May have an important role in the development and/or progression of some cancers.

**Summary**, from NCBI Gene [23641](https://www.ncbi.nlm.nih.gov/gene/23641):

> The protein encoded by this gene contains a leucine zipper-like motif and a proline-rich region that shares marked similarity with an SH3-binding domain. The protein localizes to the nucleus and is down-regulated in some cancer cell lines. It is thought to regulate the transcriptional response mediated by the nuclear factor kappa B (NF-kappaB). The gene has been proposed as a tumor suppressor gene whose protein product may have an important role in the development and/or progression of some …

**Accessions** — [HGNC:6548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6548) · Entrez [23641](https://www.ncbi.nlm.nih.gov/gene/23641) · UniProt [O95751](https://www.uniprot.org/uniprotkb/O95751) · Ensembl [ENSG00000182195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182195)

## Data

Gene col 11256: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11256); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11256, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11256]; `tensor/DDL_lfc|DDL_z.npy` [11256]; `embed/gene_vectors.npy` [11256]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11256 or target_col == 11256). Every well: [[LDOC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LDOC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
