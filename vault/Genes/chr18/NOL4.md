---
symbol: "NOL4"
type: "gene"
col: 2168
ensembl_id: "ENSG00000101746"
name: "nucleolar protein 4"
location: "18q12.1"
module: 108
arm: "+"
pooled_cpm: 6.41
n_lines_expressing: 20
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 8
direction_downstream: 10
tags: ["gene", "module/108"]
generated_by: "tahoemap"
---

# NOL4

*nucleolar protein 4* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.36× (z +19.1, q 0e+00, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.631× (z -5.1, q 2e-04, down in 14 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM167A]] (+0.65, fdr 1e-05), [[TRIM9]] (+0.64, fdr 7e-06), [[NTNG1]] (+0.62, fdr 1e-05).
> It is in [[Module 108]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GABRA2]] → it (grade C ⚠); 10 go from it, the strongest it → [[SFMBT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.36×** | +19.1 | 0e+00 | 6/14 (BT-474, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.08×** | +17.7 | 0e+00 | 14/17 (PANC-1, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +15.9 | 0e+00 | 9/15 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.75×** | +11.3 | 3e-27 | 15/16 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.8 | 3e-25 | 1/6 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.47×** | +10.1 | 7e-22 | 13/16 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.8 | 1e-20 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +9.4 | 3e-19 | 12/16 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +9.4 | 4e-19 | 12/16 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +7.4 | 1e-11 | 13/17 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +5.8 | 4e-07 | 0/11 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +5.3 | 6e-06 | 10/16 (SHP-77, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.2 | 1e-05 | 3/15 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +5.1 | 2e-05 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +4.7 | 9e-05 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.13×** | +4.4 | 4e-04 | 8/16 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +4.2 | 8e-04 | 2/13 (BT-474, PANC-1) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.002 | 6/15 (BT-474, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.012 | 4/16 (LOX-IMVI, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.037 | 5/16 (LOX-IMVI, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.631×** | -5.1 | 2e-04 | 14/17 (LOX-IMVI, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.651×** | -4.8 | 5e-04 | 13/16 (LOX-IMVI, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.668×** | -4.5 | 0.001 | 9/16 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.718×** | -3.7 | 0.033 | 5/16 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.724×** | -3.6 | 0.037 | 11/16 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.753× | -3.2 | 0.15 | 3/16 (HOP62, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 35.3 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0186× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0804× (z -13.8) |
| [[PANC-1 (line)]] | alt | 7.09 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 7.27× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 6.41 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 12.3× (z +9.3) | — |
| [[J82 (line)]] | alt | 6.68 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.48× (z +12.9) | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0479× (z -10.0) |
| [[SHP-77 (line)]] | alt | 167 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 3.00 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.00× (z +8.5) | — |
| [[A-427 (line)]] | wt | 3.43 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.75× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 6.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 48.0× (z +15.8) | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0308× (z -11.1) |
| [[HOP62 (line)]] | alt | 8.84 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.141× (z -9.8) |
| [[A-172 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.12 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM167A]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[TRIM9]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NTNG1]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[ASXL3]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ADGRB3]] | +0.60 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[TCF4]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[NDNF]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[KCNH7]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[OCA2]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[NETO1]] | +0.59 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[CACNA1A]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[SLC8A1]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRA2]] | C | GABRA2 activity raises NOL4's level | lines that do not express GABRA2 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without GABRA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: LINC02253, ASXL3, ENSG00000257883; maybe low, not absent; co-absent with the target |
| [[ASXL3]] | C | ASXL3 activity raises NOL4's level | lines that do not express ASXL3 (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without ASXL3 | 0.011 | ⚠ within organs, on part of the lines; also absent: VIPR2, NOL4, KCNH5; maybe low, not absent; co-absent with the target |
| [[DSCAM]] | C | DSCAM activity raises NOL4's level | lines that do not express DSCAM (37) vs lines expressing it (13) | 2.95× lower at baseline in the lines without DSCAM | 0.020 | ⚠ within organs, on part of the lines; also absent: CGA, RIT2, LINC01456; maybe low, not absent; co-absent with the target |
| [[LINC02899]] | C | LINC02899 activity raises NOL4's level | lines that do not express LINC02899 (40) vs lines expressing it (10) | 2.71× lower at baseline in the lines without LINC02899 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02999, MUC6, SIM1; co-absent with the target |
| [[CELF4]] | C | CELF4 activity raises NOL4's level | lines that do not express CELF4 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without CELF4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CHST8, ASXL3, SULT4A1; maybe low, not absent; co-absent with the target |
| [[NTNG1]] | C | NTNG1 activity raises NOL4's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without NTNG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[NETO1]] | C | NETO1 activity raises NOL4's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.30× lower at baseline in the lines without NETO1 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[SYT9]] | C | SYT9 activity raises NOL4's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without SYT9 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFMBT2]] | B | NOL4 activity raises SFMBT2's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.26× lower at baseline in the lines without NOL4 | 0.060 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent |
| [[DIRC3-AS1]] | B | NOL4 activity raises DIRC3-AS1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without NOL4 | 0.069 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent |
| [[FGF14]] | C | NOL4 activity raises FGF14's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.98× lower at baseline in the lines without NOL4 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[GABRA2]] | C | NOL4 activity raises GABRA2's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without NOL4 | 0.010 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[DTNA]] | C | NOL4 activity raises DTNA's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 6.06× lower at baseline in the lines without NOL4 | 0.025 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[EYA1]] | C | NOL4 activity raises EYA1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 4.14× lower at baseline in the lines without NOL4 | 0.027 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[SYT9]] | C | NOL4 activity raises SYT9's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without NOL4 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[DSCAM]] | C | NOL4 activity raises DSCAM's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without NOL4 | 0.050 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[NETO1]] | C | NOL4 activity raises NETO1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without NOL4 | 0.079 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |
| [[NTNG1]] | C | NOL4 activity raises NTNG1's level | lines that do not express NOL4 (30) vs lines expressing it (20) | 3.08× lower at baseline in the lines without NOL4 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCTD8, ASXL3, DSCAM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 108]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.558). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 22.5); signed map (35.3, 42.8). **Vector** length 51.3, 14.3% of its response variance represented; |z| ≥ 3 in 471 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +9.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.9 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:33,851,100-34,224,952 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOLP, HRIHFB2255, CT125 |
| Matched by | ensembl_id |

UniProt [O94818](https://www.uniprot.org/uniprotkb/O94818) carries no function annotation.

**Summary**, from NCBI Gene [8715](https://www.ncbi.nlm.nih.gov/gene/8715):

> Predicted to enable RNA binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7870) · Entrez [8715](https://www.ncbi.nlm.nih.gov/gene/8715) · UniProt [O94818](https://www.uniprot.org/uniprotkb/O94818) · Ensembl [ENSG00000101746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101746)

## Data

Gene col 2168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2168); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2168]; `tensor/DDL_lfc|DDL_z.npy` [2168]; `embed/gene_vectors.npy` [2168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2168 or target_col == 2168). Every well: [[NOL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
