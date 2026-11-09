---
symbol: "MGAT5B"
type: "gene"
col: 9555
ensembl_id: "ENSG00000167889"
name: "alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B"
location: "17q25.2"
module: 195
arm: "+"
pooled_cpm: 10.13
n_lines_expressing: 35
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 9
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# MGAT5B

*alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B* — 17q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +4.6, q 0.002, up in 14 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.702× (z -4.6, q 0.002, down in 11 of 23 measured lines) ⚠ transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.718× (z -4.3, q 0.005, down in 11 of 30 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLI2]] (+0.57, fdr 1e-05), [[MTCL1]] (+0.53, fdr 2e-05), [[MEGF11]] (+0.52, fdr 9e-05); moves opposite to [[RABGAP1]] (-0.48, fdr 5e-05), [[FNDC3A]] (-0.46, fdr 3e-05), [[GALK2]] (-0.44, fdr 1e-04).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[GALNT14]] → it (grade B ⚠); 9 go from it, the strongest it → [[FIBCD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9555.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.6 | 0.002 | 14/33 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 0.002 | 13/30 (NCI-H2347, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.4 | 0.002 | 8/31 (C32, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.009 | 10/29 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.009 | 9/32 (SW480, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.4 | 0.074 | 8/21 (A-427, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.0 | 0.18 | 7/32 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.28× | +3.0 | 0.18 | 10/30 (C32, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9555.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.702×** | -4.6 | 0.002 | 11/23 (NCI-H460, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.718×** | -4.3 | 0.005 | 11/30 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.727×** | -4.1 | 0.006 | 15/32 (HOP62, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.016 | 9/32 (H4, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.588×** | -3.6 | 0.033 | 9/30 (LOX-IMVI, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.751×** | -3.6 | 0.033 | 10/14 (SW480, J82, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.763×** | -3.5 | 0.037 | 13/32 (LOX-IMVI, HOP62, …) | two highest doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.621×** | -3.2 | 0.082 | 7/27 (SK-MEL-2, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.801×** | -3.2 | 0.082 | 10/31 (SW480, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.780× | -3.1 | 0.11 | 12/29 (A-427, SK-MEL-2, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.785× | -3.0 | 0.13 | 10/27 (HOP62, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9555. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 13.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.183× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 40.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -13.2) ⚠ cell-cycle shift, explains ~16% of this change |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0740× (z -8.6) |
| [[J82 (line)]] | alt | 9.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.23 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RPMI-7951 (line)]] | alt | 8.51 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0945× (z -8.5) |
| [[SHP-77 (line)]] | alt | 9.12 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0647× (z -10.4) |
| [[SW480 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.937 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.791 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9555), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLI2]] | +0.57 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MTCL1]] | +0.53 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[MEGF11]] | +0.52 | +0.37 / +0.50 | both halves | 9e-05 |  |
| [[C2CD2]] | +0.51 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[EVC]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FAM167A]] | +0.51 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[TTC7B]] | +0.50 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[CPA6]] | +0.49 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[STK32B]] | +0.49 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[MICAL3]] | +0.49 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[TRAF3]] | +0.49 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[TMSB15B]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGAP1]] | -0.48 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[FNDC3A]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[GALK2]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[KIAA0319L]] | -0.43 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[TBCK]] | -0.43 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[ATF6]] | -0.42 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[PKN2]] | -0.42 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[JAK1]] | -0.41 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[SENP2]] | -0.41 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[MBD5]] | -0.41 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[DYNC2I1]] | -0.41 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[UMAD1]] | -0.41 | -0.32 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT14]] | B | GALNT14 activity lowers MGAT5B's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.41× higher at baseline in the lines without GALNT14 | 0.055 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[NTM]] | B | NTM activity raises MGAT5B's level | lines that do not express NTM (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without NTM | 0.092 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000222032, CDH13, THY1 |
| [[ELFN1]] | C | ELFN1 activity raises MGAT5B's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 3.13× lower at baseline in the lines without ELFN1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; co-absent with the target |
| [[SORCS2]] | C | SORCS2 activity raises MGAT5B's level | lines that do not express SORCS2 (22) vs lines expressing it (28) | 3.31× lower at baseline in the lines without SORCS2 | 0.023 | ⚠ within organs, on part of the lines; also absent: ELFN1, CECR2, NTRK3; maybe low, not absent; co-absent with the target |
| [[FAM124A]] | C | FAM124A activity raises MGAT5B's level | lines that do not express FAM124A (14) vs lines expressing it (36) | 3.72× lower at baseline in the lines without FAM124A | 0.044 | ⚠ within organs, on part of the lines; also absent: RAB6B, TCF7L1, EML1; co-absent with the target |
| [[PHF21B]] | C | PHF21B activity raises MGAT5B's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 2.70× lower at baseline in the lines without PHF21B | 0.051 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[GBX2-AS1]] | C | GBX2-AS1 activity raises MGAT5B's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 3.32× lower at baseline in the lines without GBX2-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B; co-absent with the target |
| [[SPEG]] | C | SPEG activity raises MGAT5B's level | lines that do not express SPEG (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without SPEG | 0.065 | ⚠ within organs, on part of the lines; also absent: APBA2, FBXO17, GJC1; co-absent with the target |
| [[ADAMTS18]] | C | ADAMTS18 activity raises MGAT5B's level | lines that do not express ADAMTS18 (23) vs lines expressing it (27) | 2.93× lower at baseline in the lines without ADAMTS18 | 0.075 | ⚠ within organs, on part of the lines; also absent: TSHZ3, TWIST2, INSYN2B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FIBCD1]] | B | MGAT5B activity raises FIBCD1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without MGAT5B | 0.005 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[TMSB15B]] | B | MGAT5B activity raises TMSB15B's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.12× lower at baseline in the lines without MGAT5B | 0.013 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[MTCL1]] | B | MGAT5B activity raises MTCL1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without MGAT5B | 0.040 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL |
| [[GBX2-AS1]] | C | MGAT5B activity raises GBX2-AS1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.72× lower at baseline in the lines without MGAT5B | 0.006 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[SORCS2]] | C | MGAT5B activity raises SORCS2's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.77× lower at baseline in the lines without MGAT5B | 0.017 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[TCF7L1]] | C | MGAT5B activity raises TCF7L1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 4.88× lower at baseline in the lines without MGAT5B | 0.031 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[SPEG]] | C | MGAT5B activity raises SPEG's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 3.20× lower at baseline in the lines without MGAT5B | 0.060 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[TUB]] | C | MGAT5B activity raises TUB's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 2.95× lower at baseline in the lines without MGAT5B | 0.066 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |
| [[EML1]] | C | MGAT5B activity raises EML1's level | lines that do not express MGAT5B (15) vs lines expressing it (35) | 4.41× lower at baseline in the lines without MGAT5B | 0.070 | ⚠ within organs, on part of the lines; also absent: SDK2, PYGO1, EVL; co-absent with the target |

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (54.2, 10.4); signed map (-0.4, 54.8). **Vector** length 58.1, 10.6% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +2.2 | -3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.6 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.1 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.2 — chr17:76,868,404-76,950,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GnT-IX, FLJ25132, GnT-VB |
| Gene groups (HGNC) | Mannosyl-glycoprotein N-acetylglucosaminyltransferases |
| Reactome | 3 pathways, smallest: DAG1 core M2 glycosylations; DAG1 glycosylations; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3V5L5](https://www.uniprot.org/uniprotkb/Q3V5L5) (Alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase B):

> Glycosyltransferase that acts on alpha-linked mannose of N-glycans and O-mannosyl glycans. Catalyzes the transfer of N-acetylglucosamine (GlcNAc) to the beta 1-6 linkage of the mannose residue of GlcNAc-beta1,2-Man-alpha on both the alpha1,3- and alpha1,6-linked mannose arms in the core structure of N-glycan. Also acts on the GlcNAc-beta1,2-Man-alpha1-Ser/Thr moiety, forming a 2,6-branched structure in brain O-mannosyl glycan. Plays an active role in modulating integrin and laminin-dependent …

**Summary**, from NCBI Gene [146664](https://www.ncbi.nlm.nih.gov/gene/146664):

> Enables alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase activity and manganese ion binding activity. Involved in protein O-linked glycosylation. Predicted to be located in Golgi membrane. Predicted to be active in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24140) · Entrez [146664](https://www.ncbi.nlm.nih.gov/gene/146664) · UniProt [Q3V5L5](https://www.uniprot.org/uniprotkb/Q3V5L5) · Ensembl [ENSG00000167889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167889)

## Data

Gene col 9555: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9555); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9555, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9555]; `tensor/DDL_lfc|DDL_z.npy` [9555]; `embed/gene_vectors.npy` [9555]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9555 or target_col == 9555). Every well: [[MGAT5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGAT5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
