---
symbol: "ARHGEF25"
type: "gene"
col: 14249
ensembl_id: "ENSG00000240771"
name: "Rho guanine nucleotide exchange factor 25"
location: "12q13.3"
module: 128
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 35
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 13
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# ARHGEF25

*Rho guanine nucleotide exchange factor 25* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 2.46× (z +10.5, q 6e-23, up in 21 of 28 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.53× (z +3.5, q 0.045, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -9.5, q 1e-18, down in 21 of 23 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.378× (z -7.9, q 6e-13, down in 19 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEPTIN5]] (+0.65, fdr 1e-05), [[SLC4A3]] (+0.65, fdr 7e-06), [[RNF212]] (+0.62, fdr 1e-05); moves opposite to [[SPG11]] (-0.46, fdr 4e-05), [[DYNC2I1]] (-0.41, fdr 2e-04), [[PHF2P2]] (-0.41, fdr 6e-04).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[B4GALNT1]] → it (grade C ⚠); 13 go from it, the strongest it → [[SMO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14249.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.46×** | +10.5 | 6e-23 | 21/28 (A-427, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +5.6 | 7e-06 | 0/3 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +3.9 | 0.015 | 5/12 (A-427, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.54×** | +3.6 | 0.045 | 6/25 (SW 900, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +3.5 | 0.045 | 8/25 (NCI-H1573, J82, …) | all doses, flat | cell-cycle shift (explains ~15% here); position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.055 | 3/27 (hTERT-HPNE, J82, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.3 | 0.066 | 4/11 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.097 | 4/30 (SW480, H4, …) | two highest doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 10 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14249.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.438×** | -9.5 | 1e-18 | 21/23 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.378×** | -7.9 | 6e-13 | 19/22 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.384×** | -7.5 | 1e-11 | 14/27 (SW480, hTERT-HPNE, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.426×** | -7.0 | 5e-10 | 18/29 (LOX-IMVI, C-33 A, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -6.4 | 2e-08 | 16/29 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.485×** | -5.9 | 4e-07 | 15/30 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **0.519×** | -5.3 | 8e-06 | 14/21 (SW480, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.523×** | -5.3 | 9e-06 | 14/30 (SW480, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.535×** | -5.1 | 2e-05 | 13/29 (C-33 A, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -4.7 | 2e-04 | 11/23 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.566×** | -4.6 | 2e-04 | 13/31 (PANC-1, NCI-H1792, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.637×** | -3.6 | 0.012 | 10/29 (HS-578T, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -3.3 | 0.038 | 8/27 (NCI-H460, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.489×** | -3.0 | 0.095 | 6/24 (NCI-H460, A498, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14249. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 6.84 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0531× (z -12.1) |
| [[PANC-1 (line)]] | alt | 2.80 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0858× (z -10.3) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.133× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0751× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 1.85 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -9.1) |
| [[SW480 (line)]] | alt | 3.07 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0662× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change |
| [[A-172 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.575 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.177 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.775 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.183 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.186 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.234 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14249), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN5]] | +0.65 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SLC4A3]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RNF212]] | +0.62 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CHST10]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ADGRB1]] | +0.56 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[PCDHB2]] | +0.56 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[C3orf18]] | +0.55 | +0.61 / +0.38 | both halves | 6e-05 |  |
| [[JPH3]] | +0.54 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[BOLA3-DT]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[DTX3]] | +0.53 | +0.40 / +0.62 | both halves | 5e-05 | ⚠ same locus (0.4 kb, same strand: neighbours can correlate without regulation) |
| [[PGGHG]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[LZTR1]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[BVES-AS1]] | +0.52 | +0.54 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG11]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[DYNC2I1]] | -0.41 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[PHF2P2]] | -0.41 | -0.22 / -0.36 | both halves | 6e-04 |  |
| [[FAM72A]] | -0.41 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[DLEU2]] | -0.41 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[FAM72D]] | -0.41 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B4GALNT1]] | C | B4GALNT1 activity raises ARHGEF25's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without B4GALNT1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[VASH1]] | C | VASH1 activity raises ARHGEF25's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without VASH1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[CHST10]] | C | CHST10 activity raises ARHGEF25's level | lines that do not express CHST10 (12) vs lines expressing it (38) | 2.78× lower at baseline in the lines without CHST10 | 0.062 | ⚠ within organs, on part of the lines; also absent: SNRPN, DNAAF9, ENSG00000268163; co-absent with the target; its own permutation p |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 6, C 7. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMO]] | B | ARHGEF25 activity raises SMO's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without ARHGEF25 | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[CHST14]] | B | ARHGEF25 activity raises CHST14's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.57× lower at baseline in the lines without ARHGEF25 | 0.058 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[SCN8A]] | B | ARHGEF25 activity raises SCN8A's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.14× lower at baseline in the lines without ARHGEF25 | 0.075 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[BOLA3-DT]] | B | ARHGEF25 activity raises BOLA3-DT's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.84× lower at baseline in the lines without ARHGEF25 | 0.076 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[DOK1]] | B | ARHGEF25 activity raises DOK1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.11× lower at baseline in the lines without ARHGEF25 | 0.079 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[ZFP69]] | B | ARHGEF25 activity raises ZFP69's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.53× lower at baseline in the lines without ARHGEF25 | 0.094 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[B4GALNT1]] | C | ARHGEF25 activity raises B4GALNT1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.76× lower at baseline in the lines without ARHGEF25 | 0.002 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[VASH1]] | C | ARHGEF25 activity raises VASH1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.73× lower at baseline in the lines without ARHGEF25 | 0.006 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[CHST10]] | C | ARHGEF25 activity raises CHST10's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.76× lower at baseline in the lines without ARHGEF25 | 0.012 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[PCOLCE2]] | C | ARHGEF25 activity raises PCOLCE2's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without ARHGEF25 | 0.058 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[LRRN2]] | C | ARHGEF25 activity raises LRRN2's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without ARHGEF25 | 0.079 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[PDZD4]] | C | ARHGEF25 activity raises PDZD4's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.05× lower at baseline in the lines without ARHGEF25 | 0.086 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.5, 41.1); signed map (23.2, 26.8). **Vector** length 43.8, 6.94% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +2.1 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -2.0 | -9.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.0 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.9 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.7 | -7.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.0 | -3.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,610,180-57,617,245 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GEFT, p63RhoGEF |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Reactome | 11 pathways, smallest: RHOB GTPase cycle; RHOC GTPase cycle; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VW2](https://www.uniprot.org/uniprotkb/Q86VW2) (Rho guanine nucleotide exchange factor 25):

> May play a role in actin cytoskeleton reorganization in different tissues since its activation induces formation of actin stress fibers. It works as a guanine nucleotide exchange factor for Rho family of small GTPases. Links specifically G alpha q/11-coupled receptors to RHOA activation. May be an important regulator of processes involved in axon and dendrite formation. In neurons seems to be an exchange factor primarily for RAC1. Involved in skeletal myogenesis (By similarity).

**Summary**, from NCBI Gene [115557](https://www.ncbi.nlm.nih.gov/gene/115557):

> Rho GTPases alternate between an inactive GDP-bound state and an active GTP-bound state, and GEFs facilitate GDP/GTP exchange. This gene encodes a guanine nucleotide exchange factor (GEF) which interacts with Rho GTPases involved in contraction of vascular smooth muscles, regulation of responses to angiotensin II and lens cell differentiation. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:30275](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30275) · Entrez [115557](https://www.ncbi.nlm.nih.gov/gene/115557) · UniProt [Q86VW2](https://www.uniprot.org/uniprotkb/Q86VW2) · Ensembl [ENSG00000240771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240771)

## Data

Gene col 14249: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14249); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14249, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14249]; `tensor/DDL_lfc|DDL_z.npy` [14249]; `embed/gene_vectors.npy` [14249]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14249 or target_col == 14249). Every well: [[ARHGEF25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
