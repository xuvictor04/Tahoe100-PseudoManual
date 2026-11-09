---
symbol: "NOVA1"
type: "gene"
col: 6353
ensembl_id: "ENSG00000139910"
name: "NOVA alternative splicing regulator 1"
location: "14q12"
module: 19
arm: "+"
pooled_cpm: 24.77
n_lines_expressing: 23
n_dd_up: 19
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 10
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# NOVA1

*NOVA alternative splicing regulator 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.61× (z +9.7, q 2e-19, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.641× (z -6.4, q 7e-08, down in 14 of 21 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.05 µM: 0.722× (z -4.7, q 4e-04, down in 11 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYP1B1]] (+0.67, fdr 7e-06), [[RMDN2-AS1]] (+0.66, fdr 7e-06), [[TRPA1]] (+0.64, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 10 go from it, the strongest it → [[NTN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +9.7 | 2e-19 | 9/21 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +7.5 | 2e-11 | 2/21 (NCI-H2347, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +7.4 | 3e-11 | 12/21 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +7.0 | 5e-10 | 16/21 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.6 | 2e-06 | 1/20 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +5.0 | 5e-05 | 7/21 (BT-474, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 5e-05 | 8/21 (SW 900, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 0.001 | 8/21 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.003 | 2/21 (HOP62, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.003 | 11/21 (SW 900, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.006 | 9/21 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.006 | 14/21 (NCI-H460, A-427, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.010 | 11/21 (SW 900, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.30×** | +3.5 | 0.019 | 2/20 (NCI-H2347, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.021 | 9/21 (NCI-H1792, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.036 | 6/21 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.090 | 4/21 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.090 | 0/21 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.24×** | +2.9 | 0.098 | 0/21 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6353.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.641×** | -6.4 | 7e-08 | 14/21 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.719×** | -4.8 | 4e-04 | 12/21 (SHP-77, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.722×** | -4.7 | 4e-04 | 11/21 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.724×** | -4.7 | 4e-04 | 14/21 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.737×** | -4.2 | 0.003 | 8/21 (NCI-H460, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -4.1 | 0.004 | 6/21 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.762×** | -3.9 | 0.007 | 11/21 (NCI-H23, SW 1271, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.6 | 0.019 | 12/21 (HT-29, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.028 | 14/21 (SW 900, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.786×** | -3.5 | 0.028 | 2/21 (SHP-77, HT-29) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.031 | 9/21 (SW 900, NCI-H23, …) | rises with dose |  |
| [[MK-8353 (drug)]] 0.5 µM |  | **0.728×** | -3.3 | 0.049 | 0/21 | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 78.2 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -9.0) |
| [[A-427 (line)]] | wt | 48.2 | 0 | 5 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 48.4 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.381× (z -8.7) |
| [[SW 900 (line)]] | alt | 119 | 0 | 4 (4 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.231× (z -11.6) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 311 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -10.3) |
| [[HOP62 (line)]] | alt | 33.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +9.2) | [[Lonafarnib (drug)]] 5 µM 0.101× (z -9.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 51.6 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.26× (z +9.9) | — |
| [[NCI-H1792 (line)]] | alt | 88.3 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.295× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 11.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.12× (z +9.9) | — |
| [[SW 1271 (line)]] | alt | 54.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0607× (z -9.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0742× (z -8.5) |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 1 | — | [[Tubulin inhibitor 6 (drug)]] 0.5 µM 0.272× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +11.1) | — |
| [[A-172 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.76 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYP1B1]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RMDN2-AS1]] | +0.66 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TRPA1]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[CYP1B1-AS1]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[IGSF1]] | +0.63 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[CDH8]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[KYNU]] | +0.61 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EDIL3-DT]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PDE7B]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LINC02015]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[EBF1]] | +0.61 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers NOVA1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[MEIS1]] | B | MEIS1 activity raises NOVA1's level | lines that do not express MEIS1 (11) vs lines expressing it (39) | 3.28× lower at baseline in the lines without MEIS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC01798, DYNC1I1, CAMK4 |
| [[LINC02015]] | C | LINC02015 activity raises NOVA1's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 4.30× lower at baseline in the lines without LINC02015 | 0.031 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |
| [[KCTD8]] | C | KCTD8 activity raises NOVA1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 5.66× lower at baseline in the lines without KCTD8 | 0.032 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |
| [[ST8SIA6-AS1]] | C | ST8SIA6-AS1 activity raises NOVA1's level | lines that do not express ST8SIA6-AS1 (40) vs lines expressing it (10) | 4.67× lower at baseline in the lines without ST8SIA6-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: CALCA, MUC6, LINC02267; co-absent with the target |
| [[KCNJ6]] | C | KCNJ6 activity raises NOVA1's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 4.41× lower at baseline in the lines without KCNJ6 | 0.049 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent; co-absent with the target |
| [[EPHA6]] | C | EPHA6 activity raises NOVA1's level | lines that do not express EPHA6 (29) vs lines expressing it (21) | 5.95× lower at baseline in the lines without EPHA6 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLITRK4, NOVA1, KCTD8; co-absent with the target |
| [[RORB]] | C | RORB activity raises NOVA1's level | lines that do not express RORB (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without RORB | 0.073 | ⚠ within organs, on part of the lines; also absent: JAM2, NEGR1, PTPRN; maybe low, not absent; co-absent with the target |
| [[SERPINB4]] | C | SERPINB4 activity raises NOVA1's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without SERPINB4 | 0.098 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 2, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | NOVA1 activity raises NTN4's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 3.40× lower at baseline in the lines without NOVA1 | 0.015 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13 |
| [[RMDN2-AS1]] | B | NOVA1 activity raises RMDN2-AS1's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.03× lower at baseline in the lines without NOVA1 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13 |
| [[EPHA6]] | C | NOVA1 activity raises EPHA6's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 4.39× lower at baseline in the lines without NOVA1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[SLITRK6]] | C | NOVA1 activity raises SLITRK6's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.36× lower at baseline in the lines without NOVA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[CXXC4]] | C | NOVA1 activity raises CXXC4's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without NOVA1 | 0.058 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[PALMD]] | C | NOVA1 activity raises PALMD's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.02× lower at baseline in the lines without NOVA1 | 0.064 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[CYP1B1]] | C | NOVA1 activity raises CYP1B1's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 4.13× lower at baseline in the lines without NOVA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[MARCHF1]] | C | NOVA1 activity raises MARCHF1's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without NOVA1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[PCDH17]] | C | NOVA1 activity raises PCDH17's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without NOVA1 | 0.094 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |
| [[KCTD8]] | C | NOVA1 activity raises KCTD8's level | lines that do not express NOVA1 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without NOVA1 | 0.095 | ⚠ within organs, on part of the lines; also absent: EPHA6, ZYG11A, GALNT13; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, 23.5); signed map (48.1, 24.7). **Vector** length 73.3, 22.8% of its response variance represented; |z| ≥ 3 in 601 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +2.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.4 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | -1.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -2.9 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.8 | -6.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.5 | -4.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | NOVA alternative splicing regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:26,443,090-26,598,033 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NOVA-1 |
| Gene groups (HGNC) | NOVA alternative splicing regulator family |
| Matched by | ensembl_id |

**Function**, from UniProt [P51513](https://www.uniprot.org/uniprotkb/P51513) (RNA-binding protein Nova-1):

> RNA-binding protein which regulates alternative splicing of pre-mRNAs in the brain and spinal cord in a sequence-specific manner (By similarity). Binds to 5'-YCAY-3' repeats, with a minimum of 2 to 3 repeats necessary for high-affinity binding. Mediates both exon inclusion and exclusion, depending upon the position of its binding site within the pre-mRNA. Binding to 5'-YCAY-3' clusters results in a local and asymmetric action to regulate spliceosome assembly. Binding to an exonic 5'-YCAY-3' …

**Summary**, from NCBI Gene [4857](https://www.ncbi.nlm.nih.gov/gene/4857):

> This gene encodes a neuron-specific RNA-binding protein, a member of the Nova family of paraneoplastic disease antigens, that is recognized and inhibited by paraneoplastic antibodies. These antibodies are found in the sera of patients with paraneoplastic opsoclonus-ataxia, breast cancer, and small cell lung cancer. Alternatively spliced transcripts encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7886) · Entrez [4857](https://www.ncbi.nlm.nih.gov/gene/4857) · UniProt [P51513](https://www.uniprot.org/uniprotkb/P51513) · Ensembl [ENSG00000139910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139910)

## Data

Gene col 6353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6353); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6353]; `tensor/DDL_lfc|DDL_z.npy` [6353]; `embed/gene_vectors.npy` [6353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6353 or target_col == 6353). Every well: [[NOVA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOVA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
