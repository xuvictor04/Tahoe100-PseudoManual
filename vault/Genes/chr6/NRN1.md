---
symbol: "NRN1"
type: "gene"
col: 4570
ensembl_id: "ENSG00000124785"
name: "neuritin 1"
location: "6p25.1"
module: 103
arm: "+"
pooled_cpm: 27.18
n_lines_expressing: 23
n_dd_up: 5
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 6
direction_downstream: 26
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# NRN1

*neuritin 1* — 6p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.22× (z +5.8, q 3e-06, up in 17 of 21 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.41×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.317× (z -14.9, q 0e+00, down in 21 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA3]] (+0.68, fdr 7e-06), [[LINC03047]] (+0.67, fdr 7e-06), [[HOXA13]] (+0.67, fdr 7e-06); moves opposite to [[REEP3]] (-0.46, fdr 1e-04), [[NUTM2A-AS1]] (-0.46, fdr 9e-05), [[LPP]] (-0.46, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LRP2]] → it (grade B ⚠); 26 go from it, the strongest it → [[SMAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4570.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (HOP62 1.41×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +5.8 | 3e-06 | 17/21 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +5.2 | 6e-05 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +3.9 | 0.019 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.7 | 0.035 | 0/17 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.48×** | +3.6 | 0.036 | 7/21 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4570.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.317×** | -14.9 | 0e+00 | 21/21 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.331×** | -9.8 | 5e-20 | 21/21 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.350×** | -9.6 | 1e-19 | 20/21 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.419×** | -8.0 | 2e-13 | 21/21 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -6.8 | 1e-09 | 21/21 (C32, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -6.2 | 5e-08 | 19/21 (SW 900, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.509×** | -6.0 | 2e-07 | 19/20 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.536×** | -5.7 | 7e-07 | 19/21 (C32, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.578×** | -5.0 | 3e-05 | 13/20 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -4.4 | 6e-04 | 19/21 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.660×** | -3.7 | 0.013 | 16/19 (SW 900, NCI-H460, …) | rises with dose | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.665×** | -3.5 | 0.024 | 3/21 (SW 1088, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.694×** | -3.4 | 0.034 | 13/21 (NCI-H1792, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.776×** | -3.3 | 0.040 | 13/21 (J82, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.712×** | -3.1 | 0.066 | 16/21 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -3.1 | 0.067 | 16/21 (SW 900, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4570. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 69.6 | 0 | 14 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0426× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0718× (z -18.8) |
| [[C32 (line)]] | wt | 93.1 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -25.5) |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0301× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -16.6) |
| [[LoVo (line)]] | wt | 174 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0597× (z -29.2) |
| [[NCI-H460 (line)]] | wt | 23.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -19.1) |
| [[LS 180 (line)]] | wt | 155 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -14.3) |
| [[SNU-423 (line)]] | alt | 161 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -25.6) |
| [[SW480 (line)]] | alt | 17.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -19.1) |
| [[HOP62 (line)]] | alt | 41.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0908× (z -24.1) |
| [[NCI-H1792 (line)]] | alt | 16.9 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.0337× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 37.8 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0808× (z -20.5) |
| [[SHP-77 (line)]] | alt | 50.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.7) |
| [[COLO 205 (line)]] | alt | 16.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.9) |
| [[H4 (line)]] | wt | 61.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -14.6) |
| [[RKO (line)]] | wt | 17.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0421× (z -14.7) |
| [[A-172 (line)]] | wt | 24.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.6) |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.8) |
| [[J82 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.8) |
| [[SW 1088 (line)]] | alt | 78.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0600× (z -8.5) |
| [[SW48 (line)]] | wt | 9.75 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -9.3) |
| [[A-427 (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.17 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.61 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4570), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA3]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC03047]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[HOXA13]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[GPR155]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM45A]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CA9]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[MLLT3]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[DPYSL4]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PPFIA4]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SPICE1]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[RAB20]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REEP3]] | -0.46 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[NUTM2A-AS1]] | -0.46 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[LPP]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[SGPL1]] | -0.45 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP2]] | B | LRP2 activity raises NRN1's level | lines that do not express LRP2 (22) vs lines expressing it (28) | 3.11× lower at baseline in the lines without LRP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: KCNJ6, COL15A1, AIM2; maybe low, not absent |
| [[RAB20]] | B | RAB20 activity raises NRN1's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without RAB20 | 0.034 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[APLN]] | B | APLN activity raises NRN1's level | lines that do not express APLN (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without APLN | 0.055 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[BNIP3]] | B | BNIP3 activity raises NRN1's level | lines that do not express BNIP3 (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without BNIP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SPART, PRKD1, SPART-AS1 |
| [[PTPRD]] | C | PTPRD activity raises NRN1's level | lines that do not express PTPRD (25) vs lines expressing it (25) | 2.55× lower at baseline in the lines without PTPRD | 0.025 | ⚠ within organs, on part of the lines; also absent: FAP, FGF14, TDRP; co-absent with the target |
| [[TNFRSF19]] | C | TNFRSF19 activity raises NRN1's level | lines that do not express TNFRSF19 (21) vs lines expressing it (29) | 2.98× lower at baseline in the lines without TNFRSF19 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000248837, PCDH9, LOXL3; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 24, C 2. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAP2]] | B | NRN1 activity raises SMAP2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without NRN1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[ZNF395]] | B | NRN1 activity raises ZNF395's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.55× lower at baseline in the lines without NRN1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[DPCD]] | B | NRN1 activity raises DPCD's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.22× lower at baseline in the lines without NRN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[PPFIA4]] | B | NRN1 activity raises PPFIA4's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.79× lower at baseline in the lines without NRN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[TCAF2]] | B | NRN1 activity raises TCAF2's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.84× lower at baseline in the lines without NRN1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[SLC35E1]] | B | NRN1 activity raises SLC35E1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.12× lower at baseline in the lines without NRN1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[APLN]] | B | NRN1 activity raises APLN's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without NRN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[SETBP1]] | B | NRN1 activity raises SETBP1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.09× lower at baseline in the lines without NRN1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[PIAS2]] | B | NRN1 activity strengthens PIAS2's drug response | lines that do not express NRN1 (27) vs lines expressing it (22) | the lines without NRN1 respond 0.78× as strongly (z diff +1.28); strongest at Panobinostat 5 µM: 0.79x vs 0.57x (z diff +3.7) | 0.041 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137; target measured in part of the lines; artifact flags |
| [[TMEM45A]] | B | NRN1 activity raises TMEM45A's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without NRN1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[SPICE1]] | B | NRN1 activity raises SPICE1's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.35× lower at baseline in the lines without NRN1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |
| [[PFKFB4]] | B | NRN1 activity raises PFKFB4's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without NRN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.3, -14.2); signed map (-32.1, 28.7). **Vector** length 75.6, 25.1% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | +2.6 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -0.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.9 | -6.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.5 | -9.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.4 | -6.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | neuritin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.1 — chr6:5,997,999-6,007,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NRN |
| Reactome | 1 pathways, smallest: Post-translational modification: synthesis of GPI-anchored proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPD7](https://www.uniprot.org/uniprotkb/Q9NPD7) (Neuritin):

> Promotes neurite outgrowth and especially branching of neuritic processes in primary hippocampal and cortical cells.

**Summary**, from NCBI Gene [51299](https://www.ncbi.nlm.nih.gov/gene/51299):

> This gene encodes a member of the neuritin family, and is expressed in postmitotic-differentiating neurons of the developmental nervous system and neuronal structures associated with plasticity in the adult. The expression of this gene can be induced by neural activity and neurotrophins. The encoded protein contains a consensus cleavage signal found in glycosylphoshatidylinositol (GPI)-anchored proteins. The encoded protein promotes neurite outgrowth and arborization, suggesting its role in …

**Accessions** — [HGNC:17972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17972) · Entrez [51299](https://www.ncbi.nlm.nih.gov/gene/51299) · UniProt [Q9NPD7](https://www.uniprot.org/uniprotkb/Q9NPD7) · Ensembl [ENSG00000124785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124785)

## Data

Gene col 4570: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4570); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4570, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4570]; `tensor/DDL_lfc|DDL_z.npy` [4570]; `embed/gene_vectors.npy` [4570]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4570 or target_col == 4570). Every well: [[NRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
