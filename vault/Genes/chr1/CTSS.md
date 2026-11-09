---
symbol: "CTSS"
type: "gene"
col: 8639
ensembl_id: "ENSG00000163131"
name: "cathepsin S"
location: "1q21.3"
module: 70
arm: "+"
pooled_cpm: 28.9
n_lines_expressing: 35
n_dd_up: 15
n_dd_down: 27
n_dd_up_clean: 10
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 53
direction_downstream: 72
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CTSS

*cathepsin S* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.09× (z +9.4, q 2e-18, up in 20 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +9.3, q 4e-18, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.386× (z -12.1, q 7e-31, down in 26 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP4]] (+0.77, fdr 7e-06), [[GBP3]] (+0.76, fdr 7e-06), [[GBP1]] (+0.75, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[MMP7]] → it (grade B ⚠); 72 go from it, the strongest it → [[B2M]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +9.4 | 2e-18 | 20/29 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +9.3 | 4e-18 | 19/30 (HOP62, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +6.4 | 4e-08 | 12/26 (J82, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +6.1 | 2e-07 | 12/25 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +5.9 | 5e-07 | 23/33 (SNU-423, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 8e-06 | 20/31 (A498, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.5 | 5e-04 | 18/33 (HOP62, AsPC-1, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.002 | 14/32 (A549, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +4.0 | 0.003 | 12/32 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.003 | 17/28 (A549, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.009 | 13/32 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 13/33 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.040 | 13/33 (SW1417, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.059 | 15/30 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.077 | 15/32 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.386×** | -12.1 | 7e-31 | 26/33 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -11.3 | 6e-27 | 27/33 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.421×** | -11.0 | 7e-26 | 26/33 (SNU-423, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.479×** | -9.3 | 1e-18 | 25/29 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.487×** | -9.1 | 8e-18 | 26/33 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.675×** | -5.0 | 6e-05 | 25/33 (A-172, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.485×** | -4.8 | 1e-04 | 22/32 (SNU-423, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.688×** | -4.7 | 2e-04 | 15/33 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.497×** | -4.6 | 2e-04 | 20/30 (A-172, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.697×** | -4.6 | 3e-04 | 15/32 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -4.5 | 4e-04 | 18/33 (COLO 205, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.707×** | -4.4 | 6e-04 | 18/33 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.789×** | -4.2 | 0.001 | 15/33 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.717×** | -4.2 | 0.001 | 20/32 (AsPC-1, LoVo, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.719×** | -4.2 | 0.001 | 14/32 (NCI-H2347, A549, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 134 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -20.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.110× (z -16.4) |
| [[A-172 (line)]] | wt | 38.8 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.101× (z -16.5) |
| [[A549 (line)]] | wt | 61.9 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -13.8) |
| [[AsPC-1 (line)]] | alt | 41.2 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -11.0) |
| [[SNU-423 (line)]] | alt | 80.9 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.0878× (z -19.6) |
| [[NCI-H2347 (line)]] | alt | 198 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.323× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 5 | — | [[Belinostat (drug)]] 0.5 µM 0.166× (z -12.3) |
| [[HOP62 (line)]] | alt | 22.4 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +12.3) | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.161× (z -10.3) |
| [[SW 900 (line)]] | alt | 53.8 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 60.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -11.4) |
| [[A498 (line)]] | wt | 57.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.308× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 31.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.131× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 42.4 | 0 | 2 | — | [[Saquinavir (drug)]] 0.5 µM 0.232× (z -10.1) |
| [[LoVo (line)]] | wt | 16.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.198× (z -10.3) |
| [[SW1417 (line)]] | alt | 18.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -10.9) |
| [[HT-29 (line)]] | alt | 20.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.223× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 12.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.106× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0770× (z -11.8) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 76.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0503× (z -8.7) |
| [[A-427 (line)]] | wt | 4.79 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.78 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP4]] | +0.77 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[GBP3]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[GBP1]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PARP14]] | +0.74 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation |
| [[EPSTI1]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[PSMB10]] | +0.72 | +0.75 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[IDO1]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PSMB8]] | +0.71 | +0.61 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP; STRING 445 |
| [[FBXO39]] | +0.71 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[B2M]] | +0.71 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_ALLOGRAFT_REJECTION; STRING 690 |
| [[TAP1]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_ALLOGRAFT_REJECTION |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 46, C 7. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP7]] | B | MMP7 activity raises CTSS's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 4.01× lower at baseline in the lines without MMP7 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP |
| [[CD74]] | B | CD74 activity raises CTSS's level | lines that do not express CD74 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without CD74 | 0.003 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[GBP4]] | B | GBP4 activity raises CTSS's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 3.05× lower at baseline in the lines without GBP4 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[KMO]] | B | KMO activity raises CTSS's level | lines that do not express KMO (18) vs lines expressing it (32) | 3.11× lower at baseline in the lines without KMO | 0.005 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[CD5L]] | B | CD5L activity raises CTSS's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[OASL]] | B | OASL activity raises CTSS's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.37× lower at baseline in the lines without OASL | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises CTSS's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without EPSTI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CASP10]] | B | CASP10 activity raises CTSS's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.59× lower at baseline in the lines without CASP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[IDO1]] | B | IDO1 activity raises CTSS's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without IDO1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[IFI16]] | B | IFI16 activity raises CTSS's level | lines that do not express IFI16 (18) vs lines expressing it (32) | 2.72× lower at baseline in the lines without IFI16 | 0.014 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IFI44]] | B | IFI44 activity raises CTSS's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without IFI44 | 0.014 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CXCL3]] | B | CXCL3 activity raises CTSS's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.91× lower at baseline in the lines without CXCL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |

### Downstream of this gene

*72 arrows, 72 of them with an alert ⚠; grade A 0, B 66, C 6. Shown: the 12 strongest; 60 more arrows (60 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B2M]] | B | CTSS activity raises B2M's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.27× lower at baseline in the lines without CTSS | 5e-04 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IRF1]] | B | CTSS activity raises IRF1's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without CTSS | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP4]] | B | CTSS activity raises GBP4's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.56× lower at baseline in the lines without CTSS | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFI44]] | B | CTSS activity raises IFI44's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.26× lower at baseline in the lines without CTSS | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[SAMD9]] | B | CTSS activity raises SAMD9's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.13× lower at baseline in the lines without CTSS | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HLA-E]] | B | CTSS activity raises HLA-E's level | lines that do not express CTSS (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without CTSS | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HLA-F]] | B | CTSS activity raises HLA-F's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without CTSS | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[OASL]] | B | CTSS activity raises OASL's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without CTSS | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFI44L]] | B | CTSS activity raises IFI44L's level | lines that do not express CTSS (15) vs lines expressing it (35) | 4.19× lower at baseline in the lines without CTSS | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[CFB]] | B | CTSS activity raises CFB's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.68× lower at baseline in the lines without CTSS | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[HMGN2P46]] | B | CTSS activity raises HMGN2P46's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.61× lower at baseline in the lines without CTSS | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[KYNU]] | B | CTSS activity raises KYNU's level | lines that do not express CTSS (15) vs lines expressing it (35) | 4.83× lower at baseline in the lines without CTSS | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.1, 51.3); signed map (62.1, 28.8). **Vector** length 111, 31.0% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.57 to 25); *interferon alpha response* (hallmark, mean cos +0.55 to 19); *Interferon gamma signaling* (reactome, mean cos +0.64 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.7 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.0 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +6.2 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | +4.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -9.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.8 | -4.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.7 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -3.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,730,079-150,765,957 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cathepsins; Elastases |
| Hallmark sets | ALLOGRAFT_REJECTION, COMPLEMENT, KRAS_SIGNALING_UP |
| Reactome | 27 pathways, smallest: Trafficking and processing of endosomal TLR; Endosomal/Vacuolar pathway; SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25774](https://www.uniprot.org/uniprotkb/P25774) (Cathepsin S):

> Thiol protease. Key protease responsible for the removal of the invariant chain from MHC class II molecules and MHC class II antigen presentation. The bond-specificity of this proteinase is in part similar to the specificities of cathepsin L. Elicits itch by mediating cleavage and activation of MRGPRX1 (By similarity).

**Summary**, from NCBI Gene [1520](https://www.ncbi.nlm.nih.gov/gene/1520):

> The preproprotein encoded by this gene, a member of the peptidase C1 family, is a lysosomal cysteine proteinase that participates in the degradation of antigenic proteins to peptides for presentation on MHC class II molecules. The mature protein cleaves the invariant chain of MHC class II molecules in endolysosomal compartments and enables the formation of antigen-MHC class II complexes and the proper display of extracellular antigenic peptides by MHC-II. The mature protein also functions as an …

**Accessions** — [HGNC:2545](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2545) · Entrez [1520](https://www.ncbi.nlm.nih.gov/gene/1520) · UniProt [P25774](https://www.uniprot.org/uniprotkb/P25774) · Ensembl [ENSG00000163131](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163131)

## Data

Gene col 8639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8639); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8639]; `tensor/DDL_lfc|DDL_z.npy` [8639]; `embed/gene_vectors.npy` [8639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8639 or target_col == 8639). Every well: [[CTSS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
