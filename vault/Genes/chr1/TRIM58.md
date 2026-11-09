---
symbol: "TRIM58"
type: "gene"
col: 8569
ensembl_id: "ENSG00000162722"
name: "tripartite motif containing 58"
location: "1q44"
module: 66
arm: "+"
pooled_cpm: 2.98
n_lines_expressing: 19
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TRIM58

*tripartite motif containing 58* — 1q44

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.37× (z +15.5, q 0e+00, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.74× (z +6.3, q 2e-08, up in 16 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.266×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCAM]] (+0.57, fdr 6e-05), [[KRT80]] (+0.57, fdr 4e-05), [[TMEM52B]] (+0.55, fdr 1e-05); moves opposite to [[PMS2P4-1]] (-0.53, fdr 2e-05), [[TMEM134]] (-0.50, fdr 1e-04), [[SENP5]] (-0.50, fdr 2e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RBM24]] → it (grade C ⚠); 9 go from it, the strongest it → [[NPHP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.37×** | +15.5 | 0e+00 | 3/5 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.49×** | +13.8 | 1e-40 | 8/8 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.15×** | +9.2 | 1e-17 | 6/6 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +6.7 | 2e-09 | 4/16 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.30×** | +6.7 | 2e-09 | 2/11 (HOP62, SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +6.6 | 4e-09 | 8/13 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +6.5 | 5e-09 | 9/14 (SNU-423, J82, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.74×** | +6.3 | 2e-08 | 16/17 (SW1417, LS 180, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.68×** | +5.7 | 9e-07 | 1/10 (LoVo) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +5.6 | 1e-06 | 4/17 (HOP62, NCI-H23, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +5.4 | 4e-06 | 2/17 (J82, hTERT-HPNE) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.51×** | +4.7 | 1e-04 | 9/17 (hTERT-HPNE, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.48×** | +4.4 | 4e-04 | 5/17 (NCI-H23, J82, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.01×** | +4.0 | 0.002 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.64×** | +4.0 | 0.003 | 12/16 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +3.8 | 0.006 | 8/15 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.008 | 7/17 (HOP62, SNU-423, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.5 | 0.013 | 1/16 (NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.52×** | +3.4 | 0.020 | 8/16 (SNU-423, HOP62, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.026 | 1/17 (HCT15) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.50×** | +3.3 | 0.026 | 2/14 (HS-578T, SNU-423) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.75×** | +3.2 | 0.029 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.031 | 7/17 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.72×** | +3.1 | 0.040 | 5/16 (HS-578T, HOP62, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.051 | 11/17 (hTERT-HPNE, J82, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.266×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 11.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.1× (z +11.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 17.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.13× (z +8.7) | — |
| [[NCI-H23 (line)]] | alt | 6.64 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +12.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW1417 (line)]] | alt | 10.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -9.8) |
| [[A-172 (line)]] | wt | 0.301 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.337 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.253 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.227 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.256 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.350 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCAM]] | +0.57 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[KRT80]] | +0.57 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[TMEM52B]] | +0.55 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[EPHA5]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[INA]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[SCN9A]] | +0.54 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[FMN2]] | +0.54 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[OLR1]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[RBM24]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[COL12A1]] | +0.52 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CDH2]] | +0.51 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[TMEM47]] | +0.51 | +0.39 / +0.55 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TMEM134]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SENP5]] | -0.50 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[GLE1]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[DZANK1]] | -0.50 | -0.29 / -0.50 | both halves | 2e-04 |  |
| [[KIAA0319L]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NPHP3]] | -0.48 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[USP20]] | -0.47 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[KIAA0753]] | -0.46 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[WDR37]] | -0.46 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[FBH1]] | -0.45 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[RECQL5]] | -0.44 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM24]] | C | RBM24 activity raises TRIM58's level | lines that do not express RBM24 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without RBM24 | 0.026 | ⚠ within organs, on part of the lines; also absent: SRGN, P3H2, FMN2; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises TRIM58's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.12× lower at baseline in the lines without ANGPT1 | 0.045 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[FMN2]] | C | FMN2 activity raises TRIM58's level | lines that do not express FMN2 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without FMN2 | 0.047 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent; co-absent with the target |
| [[RGS7]] | C | RGS7 activity raises TRIM58's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without RGS7 | 0.054 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent; co-absent with the target |
| [[TMEM52B]] | C | TMEM52B activity raises TRIM58's level | lines that do not express TMEM52B (39) vs lines expressing it (11) | 2.03× lower at baseline in the lines without TMEM52B | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: OLR1, HOXD11, ENSG00000230258; co-absent with the target |
| [[OLR1]] | C | OLR1 activity raises TRIM58's level | lines that do not express OLR1 (40) vs lines expressing it (10) | 2.03× lower at baseline in the lines without OLR1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM52B, ENSG00000230258, PSG9; co-absent with the target |
| [[KCNT2]] | C | KCNT2 activity raises TRIM58's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 1.41× lower at baseline in the lines without KCNT2 | 0.076 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPHP3]] | B | TRIM58 activity raises NPHP3's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.35× lower at baseline in the lines without TRIM58 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[SCN8A]] | B | TRIM58 activity raises SCN8A's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without TRIM58 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[CAV2]] | B | TRIM58 activity raises CAV2's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.36× lower at baseline in the lines without TRIM58 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[RECQL5]] | B | TRIM58 activity raises RECQL5's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.18× lower at baseline in the lines without TRIM58 | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[COL12A1]] | B | TRIM58 activity raises COL12A1's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.29× lower at baseline in the lines without TRIM58 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20 |
| [[TMPRSS15]] | C | TRIM58 activity raises TMPRSS15's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without TRIM58 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |
| [[OLR1]] | C | TRIM58 activity raises OLR1's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.62× lower at baseline in the lines without TRIM58 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |
| [[PSG4]] | C | TRIM58 activity raises PSG4's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without TRIM58 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |
| [[TMEM52B]] | C | TRIM58 activity raises TMEM52B's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without TRIM58 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.2, 25.2); signed map (44.4, 18.1). **Vector** length 40.0, 9.71% of its response variance represented; |z| ≥ 3 in 344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +13.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +1.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +3.1 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q44 — chr1:247,857,187-247,880,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BIA2 |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG06](https://www.uniprot.org/uniprotkb/Q8NG06) (E3 ubiquitin-protein ligase TRIM58):

> E3 ubiquitin ligase induced during late erythropoiesis. Directly binds and ubiquitinates the intermediate chain of the microtubule motor dynein (DYNC1LI1/DYNC1LI2), stimulating the degradation of the dynein holoprotein complex. May participate in the erythroblast enucleation process through regulation of nuclear polarization.

**Summary**, from NCBI Gene [25893](https://www.ncbi.nlm.nih.gov/gene/25893):

> Predicted to enable ubiquitin protein ligase activity. Predicted to be involved in innate immune response and regulation of gene expression. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24150](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24150) · Entrez [25893](https://www.ncbi.nlm.nih.gov/gene/25893) · UniProt [Q8NG06](https://www.uniprot.org/uniprotkb/Q8NG06) · Ensembl [ENSG00000162722](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162722)

## Data

Gene col 8569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8569); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8569]; `tensor/DDL_lfc|DDL_z.npy` [8569]; `embed/gene_vectors.npy` [8569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8569 or target_col == 8569). Every well: [[TRIM58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
