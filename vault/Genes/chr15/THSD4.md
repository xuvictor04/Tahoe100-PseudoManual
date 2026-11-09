---
symbol: "THSD4"
type: "gene"
col: 11939
ensembl_id: "ENSG00000187720"
name: "thrombospondin type 1 domain containing 4"
location: "15q23"
module: 193
arm: "+"
pooled_cpm: 324.05
n_lines_expressing: 32
n_dd_up: 5
n_dd_down: 60
n_dd_up_clean: 4
n_dd_down_clean: 52
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# THSD4

*thrombospondin type 1 domain containing 4* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[BAY1125976 (drug)]] 5 µM: 2.09× (z +5.0, q 4e-04, up in 24 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 60 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.521× (z -11.8, q 2e-29, down in 24 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2E3]] (+0.86, fdr 7e-06, ⚠ read-through risk), [[BMP6]] (+0.71, fdr 7e-06), [[ASAP2]] (+0.70, fdr 7e-06), [[SPRY4-AS1]] (+0.69, fdr 7e-06); moves opposite to [[CCL28]] (-0.51, fdr 4e-05), [[ABHD4]] (-0.50, fdr 3e-05), [[CDKN2A]] (-0.50, fdr 3e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CDCP1]] → it (grade B ⚠); 7 go from it, the strongest it → [[ACER3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **2.09×** | +5.0 | 4e-04 | 24/30 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.6 | 0.001 | 20/30 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.017 | 19/30 (SW1417, RPMI-7951, …) | top dose only |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +3.4 | 0.081 | 18/30 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.088 | 12/30 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | 1.40× | +3.1 | 0.17 | 19/30 (CFPAC-1, PANC-1, …) | two highest doses | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 1.27× | +3.0 | 0.17 | 16/31 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.26× | +3.0 | 0.17 | 16/30 (NCI-H1792, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 60 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.521×** | -11.8 | 2e-29 | 24/30 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.531×** | -10.3 | 3e-22 | 25/30 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.447×** | -9.9 | 6e-21 | 27/30 (NCI-H1573, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.504×** | -9.8 | 2e-20 | 25/31 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.521×** | -9.7 | 3e-20 | 26/32 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -9.4 | 7e-19 | 27/30 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -9.0 | 2e-17 | 26/30 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.501×** | -8.9 | 5e-17 | 30/30 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.491×** | -8.8 | 1e-16 | 28/30 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.564×** | -8.7 | 1e-16 | 26/30 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.511×** | -8.6 | 4e-16 | 26/30 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.460×** | -8.5 | 1e-15 | 27/31 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.494×** | -8.3 | 3e-15 | 27/30 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.634×** | -8.2 | 7e-15 | 25/31 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.515×** | -8.2 | 1e-14 | 26/30 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.537×** | -8.0 | 5e-14 | 26/30 (LoVo, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 266 | 0 | 31 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -29.8) |
| [[LoVo (line)]] | wt | 1,149 | 0 | 26 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -23.5) |
| [[NCI-H23 (line)]] | alt | 1,020 | 0 | 26 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -26.2) |
| [[PANC-1 (line)]] | alt | 682 | 0 | 25 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -19.8) |
| [[MIA PaCa-2 (line)]] | alt | 280 | 0 | 22 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.298× (z -30.6) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 5 µM 0.167× (z -14.8) |
| [[A549 (line)]] | wt | 1,161 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -25.2) |
| [[HEC-1-A (line)]] | alt | 181 | 0 | 17 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -18.3) |
| [[NCI-H1573 (line)]] | alt | 1,198 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0478× (z -29.3) |
| [[AsPC-1 (line)]] | alt | 474 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.4) |
| [[AN3 CA (line)]] | alt | 703 | 0 | 13 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -14.6) |
| [[J82 (line)]] | alt | 202 | 0 | 12 (3 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.244× (z -12.6) |
| [[LS 180 (line)]] | wt | 203 | 0 | 10 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 1,463 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -22.2) |
| [[A-427 (line)]] | wt | 171 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -22.2) |
| [[CHP-212 (line)]] | wt | 658 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0727× (z -15.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -11.8) |
| [[A-172 (line)]] | wt | 125 | 0 | 6 | — | [[Trametinib (drug)]] 5 µM 0.294× (z -11.5) |
| [[SW48 (line)]] | wt | 153 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.1) |
| [[KATO III (line)]] | alt | 86.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -14.4) |
| [[Hs 766T (line)]] | wt | 253 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.226× (z -11.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.5) |
| [[SW1417 (line)]] | alt | 172 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 213 | 0 | 2 | — | [[Binimetinib (drug)]] 0.5 µM 0.380× (z -9.4) |
| [[BT-474 (line)]] | alt | 920 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.238× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 95.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.650× (z -12.0) ⚠ position not correctable |
| [[Panc 03.27 (line)]] | alt | 254 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -8.5) |
| [[A498 (line)]] | wt | 38.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 43.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 39.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 31.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 79.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 57.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 33.7 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 69.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 67.5 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 47.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 63.9 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.3 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.4 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.3 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 36.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2E3]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | ⚠ **readthrough risk**: NR2E3 lies 9.3 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[BMP6]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SPRY4-AS1]] | +0.69 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[SHANK2]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[BCAR3]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[CDH4]] | +0.68 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ELK3]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[NT5E]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[SLC35F3]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[LINC00941]] | +0.62 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[HMGA2]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL28]] | -0.51 | -0.48 / -0.40 | both halves | 4e-05 |  |
| [[ABHD4]] | -0.50 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[CDKN2A]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[BTN3A3]] | -0.50 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GBP2]] | -0.49 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | CDCP1 activity raises THSD4's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.82× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[ANTXR2]] | B | ANTXR2 activity raises THSD4's level | lines that do not express ANTXR2 (10) vs lines expressing it (40) | 3.33× lower at baseline in the lines without ANTXR2 | 0.039 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[DKK1]] | B | DKK1 activity raises THSD4's level | lines that do not express DKK1 (20) vs lines expressing it (30) | 3.46× lower at baseline in the lines without DKK1 | 0.051 | ⚠ within organs, on part of the lines; also absent: CACNG4, PALM, CRIP1 |
| [[PRKG1-AS1]] | B | PRKG1-AS1 activity raises THSD4's level | lines that do not express PRKG1-AS1 (15) vs lines expressing it (35) | 3.54× lower at baseline in the lines without PRKG1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: HERC5, RAB31, GALC |
| [[MAP2K1]] | B | MAP2K1 activity raises THSD4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.4% of all compounds | 0.062 | ⚠ off-target possible; 4 compounds |
| [[IL18R1]] | B | IL18R1 activity raises THSD4's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without IL18R1 | 0.067 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[IL1RL1]] | B | IL1RL1 activity raises THSD4's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 2.82× lower at baseline in the lines without IL1RL1 | 0.099 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1 |
| [[NR2E3]] | C | NR2E3 activity raises THSD4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 6.39× lower at baseline in the lines without NR2E3 | 5e-05 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |
| [[SLC35F3]] | C | SLC35F3 activity raises THSD4's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 3.36× lower at baseline in the lines without SLC35F3 | 0.025 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACER3]] | B | THSD4 activity raises ACER3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without THSD4 | 0.034 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[MAML3]] | B | THSD4 activity raises MAML3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.74× lower at baseline in the lines without THSD4 | 0.069 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[ITGA6]] | B | THSD4 activity raises ITGA6's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without THSD4 | 0.088 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[PAQR5]] | B | THSD4 activity raises PAQR5's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 2.16× lower at baseline in the lines without THSD4 | 0.089 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[SRGAP1]] | B | THSD4 activity raises SRGAP1's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without THSD4 | 0.0998 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1 |
| [[NR2E3]] | C | THSD4 activity raises NR2E3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 3.23× lower at baseline in the lines without THSD4 | 0.003 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1; co-absent with the target |
| [[SLC35F3]] | C | THSD4 activity raises SLC35F3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 3.02× lower at baseline in the lines without THSD4 | 0.099 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.848). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.8, 8.0); signed map (8.4, 44.3). **Vector** length 140, 51.0% of its response variance represented; |z| ≥ 3 in 1,635 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belumosudil (drug)]] 5 µM |  | +5.0 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | -11.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.4 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.7 | +1.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -8.6 | -9.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.3 | -8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.2 | -10.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.8 | -8.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -7.3 | -9.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -7.2 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin type 1 domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:71,096,952-71,783,383 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FVSY9334, PRO34005, FLJ13710, ADAMTSL6 |
| Gene groups (HGNC) | ADAMTS like |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMP0](https://www.uniprot.org/uniprotkb/Q6ZMP0) (Thrombospondin type-1 domain-containing protein 4):

> Promotes FBN1 matrix assembly. Attenuates TGFB signaling, possibly by accelerating the sequestration of large latent complexes of TGFB or active TGFB by FBN1 microfibril assembly, thereby negatively regulating the expression of TGFB regulatory targets, such as POSTN.

**Summary**, from NCBI Gene [79875](https://www.ncbi.nlm.nih.gov/gene/79875):

> Predicted to enable hydrolase activity. Predicted to be an extracellular matrix structural constituent. Involved in microfibril assembly. Located in microfibril. Implicated in asthma and thoracic aortic aneurysm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25835) · Entrez [79875](https://www.ncbi.nlm.nih.gov/gene/79875) · UniProt [Q6ZMP0](https://www.uniprot.org/uniprotkb/Q6ZMP0) · Ensembl [ENSG00000187720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187720)

## Data

Gene col 11939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11939); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11939]; `tensor/DDL_lfc|DDL_z.npy` [11939]; `embed/gene_vectors.npy` [11939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11939 or target_col == 11939). Every well: [[THSD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THSD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
