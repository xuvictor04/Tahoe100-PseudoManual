---
symbol: "NR2E3"
type: "gene"
col: 15917
ensembl_id: "ENSG00000278570"
name: "nuclear receptor subfamily 2 group E member 3"
location: "15q23"
module: 193
arm: "+"
pooled_cpm: 6.97
n_lines_expressing: 27
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 5
direction_downstream: 11
tags: ["gene", "module/193"]
generated_by: "tahoemap"
---

# NR2E3

*nuclear receptor subfamily 2 group E member 3* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.98× (z +6.1, q 8e-07, up in 1 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.97× (z +5.9, q 1e-06, up in 3 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.296× (z -11.2, q 2e-26, down in 24 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4]] (+0.86, fdr 7e-06, ⚠ read-through risk), [[BMP6]] (+0.74, fdr 7e-06), [[DOCK4]] (+0.64, fdr 7e-06), [[SLC35F3]] (+0.63, fdr 7e-06); moves opposite to [[NR0B1]] (-0.61, fdr 1e-05), [[CPLX2]] (-0.50, fdr 5e-05), [[CDKN2A]] (-0.47, fdr 5e-05).
> It is in [[Module 193]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[IL18R1]] → it (grade B ⚠); 11 go from it, the strongest it → [[ACER3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15917.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.1 | 8e-07 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +5.9 | 1e-06 | 3/24 (LS 180, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.65×** | +4.5 | 0.002 | 13/25 (SNU-423, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.3 | 0.002 | 2/17 (CFPAC-1, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.3 | 0.002 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.004 | 8/25 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.004 | 5/25 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.058 | 2/21 (AsPC-1, HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.058 | 0/24 | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.058 | 6/23 (J82, NCI-H23, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.39× | +3.1 | 0.11 | 6/25 (SNU-423, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 1 with an alert ⚠; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15917.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.296×** | -11.2 | 2e-26 | 24/25 (NCI-H1573, LoVo, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.422×** | -7.9 | 6e-13 | 19/25 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.493×** | -7.7 | 2e-12 | 18/25 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.417×** | -7.6 | 6e-12 | 20/25 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -7.1 | 1e-10 | 21/25 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.446×** | -6.9 | 6e-10 | 15/25 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.517×** | -6.5 | 8e-09 | 18/25 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -6.2 | 4e-08 | 16/24 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.611×** | -5.7 | 8e-07 | 16/25 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.548×** | -5.3 | 6e-06 | 15/21 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.566×** | -5.2 | 9e-06 | 13/24 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -5.2 | 9e-06 | 15/23 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.591×** | -4.8 | 6e-05 | 14/25 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.600×** | -4.7 | 1e-04 | 12/24 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.698×** | -4.7 | 1e-04 | 14/25 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15917. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 23.4 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -20.7) |
| [[NCI-H460 (line)]] | wt | 10.2 | 0 | 19 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0262× (z -19.5) ⚠ toxic; cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.108× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 29.3 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0711× (z -23.1) |
| [[NCI-H1573 (line)]] | alt | 42.0 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0489× (z -22.7) |
| [[NCI-H2030 (line)]] | alt | 50.7 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0860× (z -18.3) |
| [[A549 (line)]] | wt | 17.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0607× (z -20.3) |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0831× (z -11.0) |
| [[Hs 766T (line)]] | wt | 5.68 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.0671× (z -8.8) |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 5 µM 0.0483× (z -9.4) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.367× (z -9.7) ⚠ position not correctable |
| [[PANC-1 (line)]] | alt | 4.38 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.790 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.752 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.702 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15917), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4]] | +0.86 | +0.84 / +0.85 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 9.3 kb 3′ of THSD4 on the same strand (can correlate by spillover, not regulation) |
| [[BMP6]] | +0.74 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[DOCK4]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[SLC35F3]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[CDH4]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SHANK2]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[ST6GAL2]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PITPNC1]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.57 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NT5E]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NTSR1]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR0B1]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 | pathway: Nuclear Receptor transcription pathway |
| [[CPLX2]] | -0.50 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[CDKN2A]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[PRRT2]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL18R1]] | B | IL18R1 activity raises NR2E3's level | lines that do not express IL18R1 (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without IL18R1 | 0.049 | ⚠ within organs, on part of the lines; also absent: JCAD |
| [[MAP2K1]] | B | MAP2K1 activity raises NR2E3's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[THSD4]] | C | THSD4 activity raises NR2E3's level | lines that do not express THSD4 (18) vs lines expressing it (32) | 3.23× lower at baseline in the lines without THSD4 | 0.003 | ⚠ within organs, on part of the lines; also absent: NR2E3, EDN1, CLDN1; co-absent with the target |
| [[SLC35F3]] | C | SLC35F3 activity raises NR2E3's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 2.62× lower at baseline in the lines without SLC35F3 | 0.045 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3; co-absent with the target |
| [[EPGN]] | C | EPGN activity raises NR2E3's level | lines that do not express EPGN (41) vs lines expressing it (9) | 3.03× lower at baseline in the lines without EPGN | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, TBXT, ENSG00000289418; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACER3]] | B | NR2E3 activity raises ACER3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without NR2E3 | 0.007 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[BMP6]] | B | NR2E3 activity raises BMP6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.50× lower at baseline in the lines without NR2E3 | 0.056 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[COL4A3]] | B | NR2E3 activity raises COL4A3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without NR2E3 | 0.060 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[DUSP6]] | B | NR2E3 activity lowers DUSP6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.51× higher at baseline in the lines without NR2E3 | 0.060 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[CACNG6]] | B | NR2E3 activity raises CACNG6's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.60× lower at baseline in the lines without NR2E3 | 0.074 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[COL4A4]] | B | NR2E3 activity raises COL4A4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 1.89× lower at baseline in the lines without NR2E3 | 0.078 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[PPP2R2C]] | B | NR2E3 activity raises PPP2R2C's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.09× lower at baseline in the lines without NR2E3 | 0.081 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L |
| [[THSD4]] | C | NR2E3 activity raises THSD4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 6.39× lower at baseline in the lines without NR2E3 | 5e-05 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |
| [[SLC35F3]] | C | NR2E3 activity raises SLC35F3's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 4.23× lower at baseline in the lines without NR2E3 | 0.008 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |
| [[ARHGEF4]] | C | NR2E3 activity raises ARHGEF4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without NR2E3 | 0.016 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |
| [[CDCP1]] | C | NR2E3 activity raises CDCP1's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 3.07× lower at baseline in the lines without NR2E3 | 0.069 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |

## Where it sits

- **Module**: [[Module 193]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.9, 8.8); signed map (8.7, 44.0). **Vector** length 87.4, 24.7% of its response variance represented; |z| ≥ 3 in 844 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +4.5 |
|  | [[vincristine (drug)]] 5 µM |  | +1.2 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.7 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -6.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -5.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.7 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 2 group E member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:71,792,638-71,818,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PNR, rd7, RP37 |
| Gene groups (HGNC) | Nuclear receptor subfamily 2 group E |
| Reactome | 1 pathways, smallest: Nuclear Receptor transcription pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5X4](https://www.uniprot.org/uniprotkb/Q9Y5X4) (Photoreceptor-specific nuclear receptor):

> Orphan nuclear receptor of retinal photoreceptor cells. Transcriptional factor that is an activator of rod development and repressor of cone development. Binds the promoter region of a number of rod- and cone-specific genes, including rhodopsin, M- and S-opsin and rod-specific phosphodiesterase beta subunit. Enhances rhodopsin expression. Represses M- and S-cone opsin expression.

**Summary**, from NCBI Gene [10002](https://www.ncbi.nlm.nih.gov/gene/10002):

> This protein is part of a large family of nuclear receptor transcription factors involved in signaling pathways. Nuclear receptors have been shown to regulate pathways involved in embryonic development, as well as in maintenance of proper cell function in adults. Members of this family are characterized by discrete domains that function in DNA and ligand binding. This gene encodes a retinal nuclear receptor that is a ligand-dependent transcription factor. Defects in this gene are a cause of …

**Accessions** — [HGNC:7974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7974) · Entrez [10002](https://www.ncbi.nlm.nih.gov/gene/10002) · UniProt [Q9Y5X4](https://www.uniprot.org/uniprotkb/Q9Y5X4) · Ensembl [ENSG00000278570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000278570)

## Data

Gene col 15917: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15917); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15917, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15917]; `tensor/DDL_lfc|DDL_z.npy` [15917]; `embed/gene_vectors.npy` [15917]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15917 or target_col == 15917). Every well: [[NR2E3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2E3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
