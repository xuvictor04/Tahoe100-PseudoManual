---
symbol: "CCNYL2-1"
type: "gene"
col: 16475
ensembl_id: "ENSG00000290445"
name: ""
location: ""
module: 16
arm: "+"
pooled_cpm: 2.15
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CCNYL2-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.09× (z +11.4, q 3e-27, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.92× (z +6.7, q 3e-09, up in 4 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (RPMI-7951 0.0483×; ⚠ toxic; unreliable plate only); [[Omeprazole (drug)]] 0.5 µM in 1 line (CHP-212 0.0572×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNYL2]] (+0.83, fdr 7e-06, ⚠ same locus), [[ZNF677]] (+0.65, fdr 8e-06), [[ZSCAN23]] (+0.65, fdr 3e-05), [[ECHDC3]] (+0.60, fdr 4e-05); moves opposite to [[FEN1]] (-0.42, fdr 1e-04), [[MESD]] (-0.41, fdr 3e-04), [[CCNE2]] (-0.40, fdr 1e-04).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LINC00839]] → it (grade C ⚠); 12 go from it, the strongest it → [[DYNC2H1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16475.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.09×** | +11.4 | 3e-27 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.86×** | +9.1 | 3e-17 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +7.7 | 2e-12 | 1/8 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.97×** | +7.2 | 1e-10 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +6.7 | 3e-09 | 4/15 (A498, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.35×** | +6.2 | 5e-08 | 1/7 (A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +5.6 | 2e-06 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.57×** | +4.9 | 7e-05 | 1/9 (SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +4.8 | 1e-04 | 1/11 (A-172) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.58×** | +4.6 | 2e-04 | 2/11 (SK-MEL-2, A498) | all doses, stronger at high dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.89×** | +4.6 | 2e-04 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.5 | 3e-04 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.84×** | +4.4 | 5e-04 | 1/9 (CHP-212) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +4.2 | 1e-03 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.77×** | +4.1 | 0.001 | 1/11 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 4/11 (CHP-212, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +3.7 | 0.006 | 1/10 (J82) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.67×** | +3.4 | 0.017 | 1/10 (A498) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.64×** | +3.3 | 0.023 | 0/10 | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.51×** | +2.9 | 0.079 | 1/12 (SK-MEL-2) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.49×** | +2.9 | 0.089 | 3/13 (A-172, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Nimesulide (drug)]] 5 µM in 1 line (RPMI-7951 0.0483×; ⚠ toxic; unreliable plate only); [[Omeprazole (drug)]] 0.5 µM in 1 line (CHP-212 0.0572×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.650× | -3.2 | 0.82 | 6/14 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0572× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0483× (z -11.8) ⚠ toxic; unreliable plate only |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.179 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.398 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.174 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.185 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.197 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.190 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.554 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.170 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.152 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.165 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.198 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.161 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.624 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.306 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.227 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.173 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNYL2]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF677]] | +0.65 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[ZSCAN23]] | +0.65 | +0.65 / +0.46 | both halves | 3e-05 |  |
| [[ECHDC3]] | +0.60 | +0.43 / +0.64 | both halves | 4e-05 |  |
| [[SYT9]] | +0.56 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[FRG1JP]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[LHX6]] | +0.52 | +0.39 / +0.41 | both halves | 5e-05 |  |
| [[TSPYL5]] | +0.50 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[POTEF]] | +0.49 | +0.38 / +0.31 | both halves | 2e-04 |  |
| [[C2orf74]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZNF208]] | +0.49 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[KCTD16]] | +0.48 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ZFP69]] | +0.48 | +0.46 / +0.29 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEN1]] | -0.42 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[MESD]] | -0.41 | -0.28 / -0.34 | both halves | 3e-04 |  |
| [[CCNE2]] | -0.40 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[CFAP44]] | -0.40 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[CENPO]] | -0.40 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[CLSPN]] | -0.39 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[RFX3]] | -0.39 | -0.27 / -0.29 | both halves | 3e-04 |  |
| [[LIN52]] | -0.38 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[FAM111B]] | -0.37 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[NASP]] | -0.37 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[DPY19L1P1]] | -0.37 | -0.21 / -0.34 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00839]] | C | LINC00839 activity raises CCNYL2-1's level | lines that do not express LINC00839 (24) vs lines expressing it (26) | 3.06× lower at baseline in the lines without LINC00839 | 0.008 | ⚠ within organs, on part of the lines; also absent: PRR16, CCNYL2, PCDH10; co-absent with the target |
| [[KIAA0408]] | C | KIAA0408 activity raises CCNYL2-1's level | lines that do not express KIAA0408 (22) vs lines expressing it (28) | 2.23× lower at baseline in the lines without KIAA0408 | 0.034 | ⚠ within organs, on part of the lines; also absent: SOGA3, ENSG00000255330, RFTN1; co-absent with the target |
| [[COX7B2]] | C | COX7B2 activity raises CCNYL2-1's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.06× lower at baseline in the lines without COX7B2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[ZNF677]] | C | ZNF677 activity raises CCNYL2-1's level | lines that do not express ZNF677 (39) vs lines expressing it (11) | 2.85× lower at baseline in the lines without ZNF677 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL11A1, COL3A1, GCG; co-absent with the target |
| [[CARD18]] | C | CARD18 activity raises CCNYL2-1's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 1.21× lower at baseline in the lines without CARD18 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[LINC01518]] | C | LINC01518 activity raises CCNYL2-1's level | lines that do not express LINC01518 (36) vs lines expressing it (14) | 2.20× lower at baseline in the lines without LINC01518 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000285822, CCDC144NL-AS1, PHF2P2; co-absent with the target |
| [[SOGA3]] | C | SOGA3 activity raises CCNYL2-1's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without SOGA3 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1; co-absent with the target |
| [[ANK2]] | C | ANK2 activity raises CCNYL2-1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without ANK2 | 0.068 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 2, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | [[CCNYL2]], CCNYL2-1 activity raises DYNC2H1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 2.55× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent genes |
| [[ZDHHC4]] | B | CCNYL2-1 activity raises ZDHHC4's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 1.20× lower at baseline in the lines without CCNYL2-1 | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1 |
| [[LINC00839]] | C | CCNYL2-1 activity raises LINC00839's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 7.84× lower at baseline in the lines without CCNYL2-1 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[BVES-AS1]] | C | [[CCNYL2]], CCNYL2-1 activity raises BVES-AS1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.86× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[KCTD16]] | C | [[CCNYL2]], CCNYL2-1 activity raises KCTD16's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.27× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[ZNF677]] | C | [[CCNYL2]], CCNYL2-1 activity raises ZNF677's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 3.08× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[CARD18]] | C | [[CCNYL2]], CCNYL2-1 activity raises CARD18's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.88× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[SOGA3]] | C | [[CCNYL2]], CCNYL2-1 activity raises SOGA3's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.35× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[LINC01518]] | C | CCNYL2-1 activity raises LINC01518's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without CCNYL2-1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[KIAA0408]] | C | [[CCNYL2]], CCNYL2-1 activity raises KIAA0408's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 4.47× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[ANK2]] | C | CCNYL2-1 activity raises ANK2's level | lines that do not express CCNYL2-1 (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without CCNYL2-1 | 0.077 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[TSPYL5]] | C | [[CCNYL2]], CCNYL2-1 activity raises TSPYL5's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.77× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.228). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-35.4, 23.3); signed map (-5.5, -33.2). **Vector** length 22.9, 3.87% of its response variance represented; |z| ≥ 3 in 315 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +7.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.8 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.7 | +1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.7 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.6 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.5 | -1.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -1.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.5 | -1.1 |

## What is on record

> [!warning] No registry record
> CCNYL2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16475); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16475]; `tensor/DDL_lfc|DDL_z.npy` [16475]; `embed/gene_vectors.npy` [16475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16475 or target_col == 16475). Every well: [[CCNYL2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNYL2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
