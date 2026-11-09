---
symbol: "MEX3A"
type: "gene"
col: 14893
ensembl_id: "ENSG00000254726"
name: "mex-3 RNA binding family member A"
location: "1q22"
module: 5
arm: "+"
pooled_cpm: 12.22
n_lines_expressing: 44
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 15
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MEX3A

*mex-3 RNA binding family member A* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +9.8, q 3e-20, up in 14 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +9.8, q 3e-20, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.497× (z -6.3, q 2e-07, down in 26 of 40 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP16]] (+0.55, fdr 3e-05), [[DHX33]] (+0.54, fdr 4e-05), [[MRTO4]] (+0.54, fdr 4e-05); moves opposite to [[SERINC3]] (-0.45, fdr 5e-05), [[SAR1B]] (-0.45, fdr 3e-04), [[PRKACA]] (-0.41, fdr 0.001, ⚠ one half only (not replicated)), [[PITHD1]] (-0.41, fdr 5e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PDE3B]] → it (grade B ⚠); 15 go from it, the strongest it → [[RNF8]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14893.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +9.8 | 3e-20 | 14/22 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +9.8 | 3e-20 | 29/38 (HT-29, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.48×** | +8.1 | 8e-14 | 23/32 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.84×** | +7.7 | 2e-12 | 28/40 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +6.8 | 1e-09 | 23/34 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **2.07×** | +6.5 | 7e-09 | 32/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.03×** | +6.3 | 2e-08 | 33/40 (A-172, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.99×** | +5.7 | 9e-07 | 15/27 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.84×** | +5.4 | 3e-06 | 26/38 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.63×** | +4.3 | 8e-04 | 25/39 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +4.0 | 0.003 | 23/40 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.34×** | +3.7 | 0.010 | 14/41 (HS-578T, BT-474, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +3.6 | 0.013 | 15/34 (HT-29, BT-474, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[EX229 (drug)]] 5 µM |  | **2.15×** | +3.6 | 0.014 | 15/36 (MIA PaCa-2, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **2.11×** | +3.5 | 0.019 | 14/38 (C32, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.1 | 0.058 | 17/40 (SNU-423, H4, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14893.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.497×** | -6.3 | 2e-07 | 26/40 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.622×** | -6.0 | 5e-07 | 25/38 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.552×** | -5.3 | 2e-05 | 23/40 (NCI-H23, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.642×** | -4.0 | 0.010 | 16/40 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -3.5 | 0.044 | 19/37 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -3.3 | 0.089 | 13/39 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.089 | 13/40 (SW48, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Cytarabine (drug)]] 5 µM |  | 0.704× | -3.0 | 0.16 | 12/39 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.714× | -3.0 | 0.16 | 9/42 (C-33 A, A-172, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14893. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 29.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 9.72 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -13.4) |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.6) |
| [[A-172 (line)]] | wt | 39.8 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.61× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 27.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.9) |
| [[CHP-212 (line)]] | wt | 95.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.9) |
| [[HT-29 (line)]] | alt | 7.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0555× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 6.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +8.5) | — |
| [[RKO (line)]] | wt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.0) |
| [[SHP-77 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.351× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW480 (line)]] | alt | 31.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.0) |
| [[A-427 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14893), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP16]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[DHX33]] | +0.54 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[MRTO4]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[MRM1]] | +0.53 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[ALDH1B1]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[BCCIP]] | +0.51 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[POLR1G]] | +0.51 | +0.34 / +0.64 | both halves | 1e-04 |  |
| [[NOP2]] | +0.50 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[BEND3]] | +0.50 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[WDR12]] | +0.50 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[LINC01357]] | +0.49 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[DHX37]] | +0.49 | +0.38 / +0.48 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC3]] | -0.45 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[SAR1B]] | -0.45 | -0.28 / -0.49 | both halves | 3e-04 |  |
| [[PRKACA]] | -0.41 | -0.15 / -0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[PITHD1]] | -0.41 | -0.23 / -0.44 | both halves | 5e-04 |  |
| [[CHP1]] | -0.40 | -0.05 / -0.51 | ⚠ one half (not replicated) | 0.005 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3B]] | B | PDE3B activity raises MEX3A's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 2.08× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[CGAS]] | B | CGAS activity lowers MEX3A's level | lines that do not express CGAS (17) vs lines expressing it (33) | 2.22× higher at baseline in the lines without CGAS | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[PHF21B]] | B | PHF21B activity raises MEX3A's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without PHF21B | 0.091 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF8]] | B | MEX3A activity raises RNF8's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without MEX3A | 0.008 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[PRKACA]] | B | MEX3A activity raises PRKACA's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without MEX3A | 0.026 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[NAT10]] | B | MEX3A activity raises NAT10's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without MEX3A | 0.037 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[PITHD1]] | B | MEX3A activity raises PITHD1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.27× lower at baseline in the lines without MEX3A | 0.042 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[POLR1C]] | B | MEX3A activity raises POLR1C's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.23× lower at baseline in the lines without MEX3A | 0.048 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[DNAAF2]] | B | MEX3A activity raises DNAAF2's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without MEX3A | 0.057 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[BOLA3-DT]] | B | MEX3A activity raises BOLA3-DT's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without MEX3A | 0.065 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[SLC9B2]] | B | MEX3A activity raises SLC9B2's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without MEX3A | 0.083 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[NACC1]] | B | MEX3A activity raises NACC1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.52× lower at baseline in the lines without MEX3A | 0.089 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[MDN1]] | B | MEX3A activity raises MDN1's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without MEX3A | 0.090 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[CCDC86]] | B | MEX3A activity raises CCDC86's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without MEX3A | 0.092 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[UBE3D]] | B | MEX3A activity raises UBE3D's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.33× lower at baseline in the lines without MEX3A | 0.095 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.3, -38.3); signed map (-3.4, -49.7). **Vector** length 70.9, 15.3% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.7 | +7.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +5.5 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.5 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.7 | +6.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +6.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | mex-3 RNA binding family member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,072,013-156,082,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF162; previously RKHD4 |
| Gene groups (HGNC) | Ring finger proteins; Mex-3 RNA binding family |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L020](https://www.uniprot.org/uniprotkb/A1L020) (RNA-binding protein MEX3A):

> RNA binding protein, may be involved in post-transcriptional regulatory mechanisms.

**Summary**, from NCBI Gene [92312](https://www.ncbi.nlm.nih.gov/gene/92312):

> Enables RNA binding activity. Located in P-body and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33482](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33482) · Entrez [92312](https://www.ncbi.nlm.nih.gov/gene/92312) · UniProt [A1L020](https://www.uniprot.org/uniprotkb/A1L020) · Ensembl [ENSG00000254726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254726)

## Data

Gene col 14893: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14893); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14893, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14893]; `tensor/DDL_lfc|DDL_z.npy` [14893]; `embed/gene_vectors.npy` [14893]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14893 or target_col == 14893). Every well: [[MEX3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MEX3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
