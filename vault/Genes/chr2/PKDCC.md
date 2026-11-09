---
symbol: "PKDCC"
type: "gene"
col: 8592
ensembl_id: "ENSG00000162878"
name: "protein kinase domain containing, cytoplasmic"
location: "2p21"
module: 44
arm: "+"
pooled_cpm: 3.68
n_lines_expressing: 30
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# PKDCC

*protein kinase domain containing, cytoplasmic* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.76× (z +9.9, q 2e-20, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.60× (z +5.1, q 3e-05, up in 2 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.595× (z -4.0, q 0.029, down in 13 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.0450×, KATO III 0.125×, AN3 CA 0.132×; ⚠ cell-cycle shift, explains ~69% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0654×, A498 0.167×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.130×, AN3 CA 0.135×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.144×); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.125×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HT-29 0.120×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLAAT3]] (+0.64, fdr 7e-06), [[SLC11A2]] (+0.63, fdr 1e-05), [[PIK3C2B]] (+0.62, fdr 1e-05); moves opposite to [[BZW1]] (-0.57, fdr 3e-05), [[LINC00941]] (-0.52, fdr 2e-05), [[PITRM1]] (-0.51, fdr 4e-05).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MUC13]] → it (grade B ⚠); 3 go from it, the strongest it → [[MANSC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +9.9 | 2e-20 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.31×** | +6.5 | 2e-08 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +5.9 | 8e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.11×** | +5.8 | 9e-07 | 3/12 (LoVo, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.60×** | +5.1 | 3e-05 | 2/14 (NCI-H2030, AsPC-1) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.7 | 2e-04 | 5/10 (A549, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.6 | 3e-04 | 1/8 (LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +4.6 | 4e-04 | 5/20 (A-427, HT-29, …) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.93×** | +3.7 | 0.015 | 1/7 (NCI-H2030) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.60×** | +3.6 | 0.015 | 5/21 (LS 180, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.018 | 5/18 (A-427, A498, …) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.54×** | +3.3 | 0.039 | 1/16 (HT-29) | top dose only |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.074 | 5/14 (LS 180, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.16×** | +3.1 | 0.074 | 1/9 (AsPC-1) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.1 | 0.078 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +3.0 | 0.084 | 2/11 (SW1417, LoVo) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.72×** | +3.0 | 0.084 | 1/12 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (HT-29 0.0450×, KATO III 0.125×, AN3 CA 0.132×; ⚠ cell-cycle shift, explains ~69% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (AN3 CA 0.0654×, A498 0.167×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.130×, AN3 CA 0.135×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.144×); [[Panobinostat (drug)]] 5 µM in 1 line (A549 0.125×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HT-29 0.120×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.595×** | -4.0 | 0.029 | 13/25 (A549, AN3 CA, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -3.6 | 0.092 | 8/24 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 79.3 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.3) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.7) |
| [[HT-29 (line)]] | alt | 5.69 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0450× (z -18.2) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.120× (z -8.5) |
| [[A498 (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.130× (z -10.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 17.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.124× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.125× (z -9.3) |
| [[KATO III (line)]] | alt | 19.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -16.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[A-172 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.512 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.787 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.665 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.424 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.819 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.738 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.876 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.929 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.454 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLAAT3]] | +0.64 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SLC11A2]] | +0.63 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PPFIBP2]] | +0.59 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[ELF3]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PLEKHG6]] | +0.58 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[TRIM31]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CDX2]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[NPNT]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MAP3K8]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[EFNA1]] | +0.55 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[MGAM2]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BZW1]] | -0.57 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[LINC00941]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PITRM1]] | -0.51 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[MACF1]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[IQGAP1]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[KPNA4]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SLC30A9]] | -0.49 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[SEPTIN10]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[CD59]] | -0.48 | -0.34 / -0.51 | both halves | 1e-04 |  |
| [[TPM3]] | -0.48 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[CAPRIN2]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[NOP14-AS1]] | -0.47 | -0.40 / -0.49 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MUC13]] | B | MUC13 activity raises PKDCC's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 2.25× lower at baseline in the lines without MUC13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[TRIM31]] | B | TRIM31 activity raises PKDCC's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 1.96× lower at baseline in the lines without TRIM31 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1 |
| [[TOX3]] | B | TOX3 activity raises PKDCC's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.36× lower at baseline in the lines without TOX3 | 0.0999 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MANSC1]] | B | PKDCC activity strengthens MANSC1's drug response | lines that do not express PKDCC (15) vs lines expressing it (17) | the lines without PKDCC respond 0.62× as strongly (z diff +1.51); strongest at Homoharringtonine 5 µM: 0.47x vs 0.29x (z diff +3.4) | 0.081 | ⚠ within organs, on part of the lines; also absent: CHD5, CCDC144NL-AS1, LINC02864; target measured in part of the lines; artifact flags |
| [[CAMK2N1]] | B | PKDCC activity strengthens CAMK2N1's drug response | lines that do not express PKDCC (19) vs lines expressing it (21) | the lines without PKDCC respond 0.87× as strongly (z diff +0.91); strongest at Panobinostat 0.5 µM: 0.61x vs 0.30x (z diff +3.8) | 0.089 | ⚠ within organs, on part of the lines; also absent: CHD5, CCDC144NL-AS1, LINC02864; target measured in part of the lines; artifact flags |
| [[RSBN1L]] | B | PKDCC activity raises RSBN1L's level | lines that do not express PKDCC (20) vs lines expressing it (30) | 1.19× lower at baseline in the lines without PKDCC | 0.096 | ⚠ within organs, on part of the lines; also absent: CHD5, CCDC144NL-AS1, LINC02864 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (32.1, 47.0); signed map (50.2, 2.6). **Vector** length 34.3, 5.10% of its response variance represented; |z| ≥ 3 in 566 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.50 to 4); *Aspirin ADME* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.2 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.0 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -0.9 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase domain containing, cytoplasmic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:42,048,021-42,058,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SgK493, Vlk |
| Gene groups (HGNC) | Divergent protein kinase domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q504Y2](https://www.uniprot.org/uniprotkb/Q504Y2) (Extracellular tyrosine-protein kinase PKDCC):

> Secreted tyrosine-protein kinase that mediates phosphorylation of extracellular proteins and endogenous proteins in the secretory pathway, which is essential for patterning at organogenesis stages. Mediates phosphorylation of MMP1, MMP13, MMP14, MMP19 and ERP29. Probably plays a role in platelets: rapidly and quantitatively secreted from platelets in response to stimulation of platelet degranulation. May also have serine/threonine protein kinase activity. Required for longitudinal bone growth …

**Summary**, from NCBI Gene [91461](https://www.ncbi.nlm.nih.gov/gene/91461):

> Enables non-membrane spanning protein tyrosine kinase activity. Involved in peptidyl-tyrosine phosphorylation and skeletal system development. Located in extracellular region. Implicated in intrinsic asthma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25123) · Entrez [91461](https://www.ncbi.nlm.nih.gov/gene/91461) · UniProt [Q504Y2](https://www.uniprot.org/uniprotkb/Q504Y2) · Ensembl [ENSG00000162878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162878)

## Data

Gene col 8592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8592); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8592]; `tensor/DDL_lfc|DDL_z.npy` [8592]; `embed/gene_vectors.npy` [8592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8592 or target_col == 8592). Every well: [[PKDCC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKDCC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
