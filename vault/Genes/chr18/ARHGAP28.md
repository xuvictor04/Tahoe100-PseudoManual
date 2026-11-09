---
symbol: "ARHGAP28"
type: "gene"
col: 1541
ensembl_id: "ENSG00000088756"
name: "Rho GTPase activating protein 28"
location: "18p11.31"
module: 152
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 28
n_dd_up: 29
n_dd_down: 15
n_dd_up_clean: 21
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/152"]
generated_by: "tahoemap"
---

# ARHGAP28

*Rho GTPase activating protein 28* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.83× (z +16.3, q 0e+00, up in 22 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.414× (z -9.8, q 5e-20, down in 18 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA3]] (+0.69, fdr 7e-06), [[NREP]] (+0.67, fdr 7e-06), [[KCTD16]] (+0.67, fdr 7e-06).
> It is in [[Module 152]], a single-armed module (Retinoid metabolism and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → [[P2RX7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.83×** | +16.3 | 0e+00 | 22/24 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +9.7 | 7e-20 | 15/24 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.38×** | +9.3 | 3e-18 | 2/9 (A-427, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.14×** | +8.4 | 4e-15 | 21/24 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +7.6 | 3e-12 | 1/15 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.98×** | +7.6 | 3e-12 | 16/22 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +7.2 | 4e-11 | 13/23 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +6.5 | 6e-09 | 10/23 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +6.1 | 7e-08 | 13/22 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.0 | 1e-07 | 1/14 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 13/25 (HOP62, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +4.7 | 1e-04 | 14/23 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 4e-04 | 9/24 (HOP62, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.08×** | +4.2 | 9e-04 | 10/24 (SW480, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 9e-04 | 14/23 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 7/23 (A-172, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 13/25 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.004 | 10/25 (HOP62, HS-578T, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1541.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.414×** | -9.8 | 5e-20 | 18/24 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -7.3 | 6e-11 | 20/23 (NCI-H1792, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.559×** | -6.5 | 2e-08 | 19/21 (NCI-H1792, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.573×** | -6.2 | 7e-08 | 14/23 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.595×** | -5.8 | 8e-07 | 11/25 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.664×** | -4.6 | 5e-04 | 13/24 (CHP-212, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -4.1 | 0.003 | 15/24 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.707×** | -3.9 | 0.007 | 6/23 (SK-MEL-2, AN3 CA, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.031 | 13/23 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.722×** | -3.4 | 0.032 | 14/23 (NCI-H460, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.041 | 14/24 (C32, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.744×** | -3.3 | 0.043 | 17/23 (KATO III, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.747×** | -3.3 | 0.048 | 6/23 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.753×** | -3.2 | 0.059 | 12/24 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -3.0 | 0.094 | 9/23 (NCI-H460, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 23.1 | 1 (1 ⚠) | 7 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.57× (z +8.6) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.0774× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.104× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 8 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.151× (z -12.5) |
| [[H4 (line)]] | wt | 23.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -11.4) |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0801× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 6.48 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0996× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.108× (z -10.2) |
| [[SW480 (line)]] | alt | 2.06 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 11.7× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0565× (z -10.2) |
| [[A-172 (line)]] | wt | 13.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.92× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0683× (z -12.9) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 10.0 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0667× (z -8.7) |
| [[HOP62 (line)]] | alt | 7.50 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0982× (z -9.5) |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0446× (z -14.6) |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0713× (z -10.6) |
| [[A498 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.753 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.653 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.707 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.747 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.605 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.892 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.588 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.650 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.748 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA3]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[NREP]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[KCTD16]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[NCAM2]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC01266]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ATRNL1]] | +0.63 | +0.58 / +0.65 | both halves | 8e-06 | **novel candidate** |
| [[PPP2R2B]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[MIR3171HG]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[ZMAT4]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PTPRD]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SYT11]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[CDH18]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ARHGAP28's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[HMCN1]] | C | HMCN1 activity raises ARHGAP28's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.99× lower at baseline in the lines without HMCN1 | 0.078 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises ARHGAP28's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.29× lower at baseline in the lines without ANGPT1 | 0.089 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[GRIK2]] | C | GRIK2 activity raises ARHGAP28's level | lines that do not express GRIK2 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without GRIK2 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR9-3HG, PCDH10, PLEKHG4B; co-absent with the target |
| [[SNCA]] | C | SNCA activity raises ARHGAP28's level | lines that do not express SNCA (29) vs lines expressing it (21) | 2.76× lower at baseline in the lines without SNCA | 0.097 | ⚠ within organs, on part of the lines; also absent: SLC6A15, CNKSR2, CDH10; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P2RX7]] | B | ARHGAP28 activity raises P2RX7's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 2.56× lower at baseline in the lines without ARHGAP28 | 0.030 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1 |
| [[TNFRSF19]] | B | ARHGAP28 activity raises TNFRSF19's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 2.46× lower at baseline in the lines without ARHGAP28 | 0.087 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1 |
| [[NREP]] | C | ARHGAP28 activity raises NREP's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 3.68× lower at baseline in the lines without ARHGAP28 | 0.020 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1; co-absent with the target |
| [[GRIK2]] | C | ARHGAP28 activity raises GRIK2's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 3.20× lower at baseline in the lines without ARHGAP28 | 0.022 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1; co-absent with the target |
| [[KCTD16]] | C | ARHGAP28 activity raises KCTD16's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 3.68× lower at baseline in the lines without ARHGAP28 | 0.065 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1; co-absent with the target |
| [[EPHA3]] | C | ARHGAP28 activity raises EPHA3's level | lines that do not express ARHGAP28 (22) vs lines expressing it (28) | 3.27× lower at baseline in the lines without ARHGAP28 | 0.088 | ⚠ within organs, on part of the lines; also absent: RORB, ENSG00000256417, TMTC1; co-absent with the target |

## Where it sits

- **Module**: [[Module 152]] — Retinoid metabolism and transport; 29 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.9, 30.5); signed map (36.2, 34.4). **Vector** length 61.5, 14.9% of its response variance represented; |z| ≥ 3 in 731 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.1 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -2.7 | -6.2 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.1 |
|  | [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.3 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:6,729,716-6,915,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1314, FLJ10312 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2N2](https://www.uniprot.org/uniprotkb/Q9P2N2) (Rho GTPase-activating protein 28):

> GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state.

**Summary**, from NCBI Gene [79822](https://www.ncbi.nlm.nih.gov/gene/79822):

> Predicted to enable GTPase activator activity. Predicted to be involved in negative regulation of stress fiber assembly; regulation of actin filament polymerization; and regulation of small GTPase mediated signal transduction. Predicted to be located in cytosol. Predicted to be active in cytoplasm. Implicated in allergic disease. Biomarker of meningioma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25509) · Entrez [79822](https://www.ncbi.nlm.nih.gov/gene/79822) · UniProt [Q9P2N2](https://www.uniprot.org/uniprotkb/Q9P2N2) · Ensembl [ENSG00000088756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088756)

## Data

Gene col 1541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1541); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1541]; `tensor/DDL_lfc|DDL_z.npy` [1541]; `embed/gene_vectors.npy` [1541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1541 or target_col == 1541). Every well: [[ARHGAP28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
