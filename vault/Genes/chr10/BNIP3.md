---
symbol: "BNIP3"
type: "gene"
col: 10692
ensembl_id: "ENSG00000176171"
name: "BCL2 interacting protein 3"
location: "10q26.3"
module: 99
arm: "+"
pooled_cpm: 164.89
n_lines_expressing: 39
n_dd_up: 8
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# BNIP3

*BCL2 interacting protein 3* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.05 µM: 1.65× (z +6.5, q 3e-08, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.364× (z -17.1, q 0e+00, down in 36 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.79, fdr 7e-06), [[HILPDA]] (+0.70, fdr 7e-06), [[GYS1]] (+0.68, fdr 7e-06).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); 3 go from it, the strongest it → [[DIPK2A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.65×** | +6.5 | 3e-08 | 31/37 (H4, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.52×** | +5.4 | 2e-05 | 21/37 (NCI-H1792, NCI-H460, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 2e-04 | 27/37 (HOP62, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.34×** | +3.8 | 0.020 | 21/37 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.030 | 20/37 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.074 | 26/37 (SHP-77, SNU-423, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.076 | 24/37 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.076 | 21/37 (SHP-77, LoVo, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.57× | +3.0 | 0.16 | 18/37 (SHP-77, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10692.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.364×** | -17.1 | 0e+00 | 36/37 (LOX-IMVI, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.413×** | -11.0 | 2e-25 | 35/36 (SNU-423, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.526×** | -8.0 | 3e-13 | 27/37 (C-33 A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.541×** | -7.9 | 3e-13 | 24/37 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.594×** | -6.2 | 6e-08 | 26/35 (SNU-1, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -5.5 | 4e-06 | 24/35 (C-33 A, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.644×** | -5.4 | 4e-06 | 27/36 (SW 900, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.731×** | -5.3 | 9e-06 | 23/38 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.7 | 1e-04 | 1/39 (SW 1271) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.506×** | -4.5 | 4e-04 | 32/38 (HepG2/C3A, AN3 CA, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Gallic acid (drug)]] 0.05 µM |  | **0.784×** | -3.1 | 0.093 | 21/37 (HS-578T, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.785×** | -3.1 | 0.093 | 19/37 (C32, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.791× | -3.0 | 0.12 | 18/37 (SW 900, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 310 | 1 | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.36× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -27.6) |
| [[H4 (line)]] | wt | 263 | 5 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.16× (z +13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.43× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 307 | 4 (4 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +13.9) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -11.4) |
| [[SNU-1 (line)]] | wt | 392 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -17.8) |
| [[AN3 CA (line)]] | alt | 501 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -21.4) |
| [[C32 (line)]] | wt | 324 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -17.0) |
| [[HOP62 (line)]] | alt | 219 | 4 (3 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +13.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.78× (z +10.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.403× (z -8.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.517× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 118 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -14.8) |
| [[SW 900 (line)]] | alt | 319 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -14.0) |
| [[C-33 A (line)]] | alt | 331 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -22.8) |
| [[CFPAC-1 (line)]] | alt | 440 | 0 | 4 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.383× (z -11.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 253 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +14.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.54× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.379× (z -9.2) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 307 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.8) |
| [[SNU-423 (line)]] | alt | 482 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -20.1) |
| [[A-427 (line)]] | wt | 173 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -12.3) |
| [[CHP-212 (line)]] | wt | 231 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.7) |
| [[HepG2_C3A (line)]] | wt | 400 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.0) |
| [[LS 180 (line)]] | wt | 179 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -15.8) |
| [[SK-MEL-2 (line)]] | alt | 115 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -15.2) |
| [[A498 (line)]] | wt | 49.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 79.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 209 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.356× (z -10.4) |
| [[HS-578T (line)]] | alt | 197 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.8) |
| [[hTERT-HPNE (line)]] | wt | 220 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.65× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 172 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.92× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.6) |
| [[A-172 (line)]] | wt | 136 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -10.8) |
| [[J82 (line)]] | alt | 196 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -10.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.445× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 150 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.2) |
| [[NCI-H2347 (line)]] | alt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 297 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.8) |
| [[PANC-1 (line)]] | alt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.6) |
| [[SW 1271 (line)]] | alt | 131 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0344× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.79 | +0.76 / +0.77 | both halves | 7e-06 | STRING 495 |
| [[HILPDA]] | +0.70 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[GYS1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[USP28]] | +0.67 | +0.57 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[YEATS2]] | +0.67 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[C4orf3]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CRYBG3]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[P4HA1]] | +0.65 | +0.64 / +0.59 | both halves | 7e-06 | STRING 466 |
| [[FUT11]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[EGLN1]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 | STRING 673 |
| [[GBE1]] | +0.65 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[LDHA]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 | STRING 642 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises BNIP3's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 3.28× lower at baseline in the lines without PLOD2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[PPP1R3C]] | B | PPP1R3C activity raises BNIP3's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without PPP1R3C | 0.069 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[STC2]] | C | STC2 activity raises BNIP3's level | lines that do not express STC2 (13) vs lines expressing it (37) | 5.48× lower at baseline in the lines without STC2 | 0.074 | ⚠ within organs, on part of the lines; also absent: CHST10, PEG10, ZNF606; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DIPK2A]] | B | BNIP3 activity raises DIPK2A's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without BNIP3 | 0.058 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1 |
| [[NRN1]] | B | BNIP3 activity raises NRN1's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without BNIP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1 |
| [[STC2]] | C | BNIP3 activity raises STC2's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 5.04× lower at baseline in the lines without BNIP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.695). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -16.6); signed map (-37.3, 25.7). **Vector** length 128, 43.4% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.53 to 17); *mTORC1 signaling* (hallmark, mean cos +0.51 to 15); *Glycolysis* (reactome, mean cos +0.53 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.4 | +2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -1.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +4.5 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +3.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -8.2 | -11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -17.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.4 | -5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -2.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:131,967,684-131,981,967 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Nip3, HABON |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12983](https://www.uniprot.org/uniprotkb/Q12983) (BCL2/adenovirus E1B 19 kDa protein-interacting protein 3):

> Apoptosis-inducing protein that can overcome BCL2 suppression. May play a role in repartitioning calcium between the two major intracellular calcium stores in association with BCL2. Involved in mitochondrial quality control via its interaction with SPATA18/MIEAP: in response to mitochondrial damage, participates in mitochondrial protein catabolic process (also named MALM) leading to the degradation of damaged proteins inside mitochondria. The physical interaction of SPATA18/MIEAP, BNIP3 and …

**Summary**, from NCBI Gene [664](https://www.ncbi.nlm.nih.gov/gene/664):

> This gene is encodes a mitochondrial protein that contains a BH3 domain and acts as a pro-apoptotic factor. The encoded protein interacts with anti-apoptotic proteins, including the E1B 19 kDa protein and Bcl2. This gene is silenced in tumors by DNA methylation. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:1084](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1084) · Entrez [664](https://www.ncbi.nlm.nih.gov/gene/664) · UniProt [Q12983](https://www.uniprot.org/uniprotkb/Q12983) · Ensembl [ENSG00000176171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176171)

## Data

Gene col 10692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10692); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10692]; `tensor/DDL_lfc|DDL_z.npy` [10692]; `embed/gene_vectors.npy` [10692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10692 or target_col == 10692). Every well: [[BNIP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNIP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
