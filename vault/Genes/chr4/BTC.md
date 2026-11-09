---
symbol: "BTC"
type: "gene"
col: 10530
ensembl_id: "ENSG00000174808"
name: "betacellulin"
location: "4q13.3"
module: 32
arm: "+"
pooled_cpm: 3.75
n_lines_expressing: 30
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 29
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# BTC

*betacellulin* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.63× (z +11.2, q 2e-26, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +7.8, q 1e-12, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.393× (z -6.9, q 3e-09, down in 22 of 27 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PATL2]] (+0.70, fdr 1e-05), [[ANXA2R-AS1]] (+0.67, fdr 7e-05), [[RARRES1]] (+0.67, fdr 2e-05); moves opposite to [[GNAI2]] (-0.61, fdr 7e-04), [[PHKA2]] (-0.59, fdr 1e-04), [[SLC27A1]] (-0.57, fdr 8e-04, ⚠ one half only (not replicated)), [[KIAA1328]] (-0.55, fdr 3e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 29 go from it, the strongest it → [[DTX3L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.63×** | +11.2 | 2e-26 | 12/14 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.64×** | +10.8 | 1e-24 | 5/5 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.71×** | +8.9 | 2e-16 | 7/9 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +7.8 | 1e-12 | 11/24 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.99×** | +7.1 | 1e-10 | 21/27 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +4.9 | 1e-04 | 8/22 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +4.7 | 2e-04 | 7/22 (A-427, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.3 | 0.001 | 5/19 (NCI-H2347, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +4.1 | 0.003 | 5/15 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.72×** | +3.9 | 0.005 | 10/26 (A-427, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.012 | 11/24 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +3.5 | 0.024 | 8/25 (LoVo, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.5 | 0.024 | 5/17 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.024 | 9/27 (A-427, NCI-H460, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.62×** | +3.2 | 0.046 | 6/21 (A-427, A498, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.86×** | +3.2 | 0.046 | 3/15 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.062 | 8/27 (RKO, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +3.1 | 0.062 | 9/25 (LoVo, A-427, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.062 | 10/27 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.083 | 9/27 (A-427, A498, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.085 | 3/25 (LS 180, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10530.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.393×** | -6.9 | 3e-09 | 22/27 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.454×** | -5.8 | 2e-06 | 21/26 (BT-474, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.566×** | -4.2 | 0.005 | 14/27 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.577×** | -4.1 | 0.007 | 17/27 (LoVo, A-427, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -3.9 | 0.013 | 11/27 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 23.8 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +8.6) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.154× (z -10.7) |
| [[LoVo (line)]] | wt | 9.34 | 0 | 4 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0697× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 6.35 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.53× (z +9.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 8.27 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0432× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 4.51 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0492× (z -9.0) |
| [[SW48 (line)]] | wt | 13.0 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.0388× (z -9.7) |
| [[A-172 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.541 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.756 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.807 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.796 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATL2]] | +0.70 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ANXA2R-AS1]] | +0.67 | +0.54 / +0.38 | both halves | 7e-05 |  |
| [[RARRES1]] | +0.67 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SCAMP1-AS1]] | +0.66 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[NRIR]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PARP14]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PHF11]] | +0.64 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[TAFA2]] | +0.64 | +0.59 / +0.29 | both halves | 3e-04 |  |
| [[ARAP2]] | +0.64 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[NINJ2]] | +0.64 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[PSMB8]] | +0.64 | +0.58 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DTX3L]] | +0.64 | +0.57 / +0.63 | both halves | 9e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.61 | -0.56 / -0.21 | both halves | 7e-04 | pathway: ESR-mediated signaling |
| [[PHKA2]] | -0.59 | -0.53 / -0.32 | both halves | 1e-04 |  |
| [[SLC27A1]] | -0.57 | -0.53 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NBPF3]] | -0.55 | -0.53 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[KIAA1328]] | -0.55 | -0.47 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BTC's level | compounds that target TOP2A: 4 of 5 raise it (Amsacrine, Doxorubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[POU5F1B]] | B | POU5F1B activity raises BTC's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.12× lower at baseline in the lines without POU5F1B | 0.040 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises BTC's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HERC6]] | B | HERC6 activity raises BTC's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.35× lower at baseline in the lines without HERC6 | 0.051 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises BTC's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 1.90× lower at baseline in the lines without PARP9 | 0.068 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers BTC's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[LCN2]] | C | LCN2 activity raises BTC's level | lines that do not express LCN2 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without LCN2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4; co-absent with the target |
| [[LAMP3]] | C | LAMP3 activity raises BTC's level | lines that do not express LAMP3 (18) vs lines expressing it (32) | 2.28× lower at baseline in the lines without LAMP3 | 0.051 | ⚠ within organs, on part of the lines; also absent: OCLN, ENTPD2, LSR; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 28, C 1. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DTX3L]] | B | BTC activity raises DTX3L's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.35× lower at baseline in the lines without BTC | 0.007 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[PARP9]] | B | BTC activity raises PARP9's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without BTC | 0.007 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[PARP14]] | B | BTC activity raises PARP14's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.43× lower at baseline in the lines without BTC | 0.008 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[HERC6]] | B | BTC activity raises HERC6's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without BTC | 0.008 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[RNF213]] | B | BTC activity raises RNF213's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.44× lower at baseline in the lines without BTC | 0.011 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[RSAD2]] | B | BTC activity raises RSAD2's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.60× lower at baseline in the lines without BTC | 0.021 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[TAPBPL]] | B | BTC activity raises TAPBPL's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without BTC | 0.024 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[TRANK1]] | B | BTC activity raises TRANK1's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without BTC | 0.025 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[POU5F1B]] | B | BTC activity raises POU5F1B's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.84× lower at baseline in the lines without BTC | 0.026 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[NRIR]] | B | BTC activity raises NRIR's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without BTC | 0.028 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[ADAR]] | B | BTC activity raises ADAR's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.26× lower at baseline in the lines without BTC | 0.038 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |
| [[IFI35]] | B | BTC activity raises IFI35's level | lines that do not express BTC (20) vs lines expressing it (30) | 1.20× lower at baseline in the lines without BTC | 0.039 | ⚠ within organs, on part of the lines; also absent: CHMP4C, SLC27A2, ENSG00000288656; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.5, 56.0); signed map (61.4, 34.2). **Vector** length 60.5, 13.4% of its response variance represented; |z| ≥ 3 in 682 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *IFIT antiviral response* (reactome, mean cos +0.52 to 9); *Viral strategies to evade IFIT action* (reactome, mean cos +0.55 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.2 | -6.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | betacellulin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:74,744,759-74,794,523 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EGF ligand family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 44 pathways, smallest: Inhibition of Signaling by Overexpressed EGFR; Signaling by Overexpressed Wild-Type EGFR in Cancer; EGFR interacts with phospholipase C-gamma |
| Matched by | ensembl_id |

**Function**, from UniProt [P35070](https://www.uniprot.org/uniprotkb/P35070) (Probetacellulin):

> Growth factor that binds to EGFR, ERBB4 and other EGF receptor family members. Potent mitogen for retinal pigment epithelial cells and vascular smooth muscle cells.

**Summary**, from NCBI Gene [685](https://www.ncbi.nlm.nih.gov/gene/685):

> This gene encodes a member of the epidermal growth factor (EGF) family of proteins. Alternative splicing results in multiple transcript variants, at least one of which encodes a preproprotein that is proteolytically processed to generate the secreted growth factor. A secreted form and a membrane-anchored form of this protein bind to multiple different EGF receptors. This protein promotes pancreatic cell proliferation and insulin secretion, as well as retinal vascular permeability. Mutations in …

**Accessions** — [HGNC:1121](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1121) · Entrez [685](https://www.ncbi.nlm.nih.gov/gene/685) · UniProt [P35070](https://www.uniprot.org/uniprotkb/P35070) · Ensembl [ENSG00000174808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174808)

## Data

Gene col 10530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10530); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10530]; `tensor/DDL_lfc|DDL_z.npy` [10530]; `embed/gene_vectors.npy` [10530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10530 or target_col == 10530). Every well: [[BTC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
