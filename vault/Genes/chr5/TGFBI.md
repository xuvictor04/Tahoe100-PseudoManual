---
symbol: "TGFBI"
type: "gene"
col: 4212
ensembl_id: "ENSG00000120708"
name: "transforming growth factor beta induced"
location: "5q31.1"
module: 66
arm: "+"
pooled_cpm: 189.7
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 25
direction_downstream: 21
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# TGFBI

*transforming growth factor beta induced* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.74× (z +15.2, q 0e+00, up in 19 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +3.9, q 0.016, up in 6 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.379× (z -20.7, q 0e+00, down in 22 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NID2]] (+0.66, fdr 9e-06), [[COL3A1]] (+0.64, fdr 1e-05), [[MMP2]] (+0.64, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[PRSS23]] → it (grade B ⚠); 21 go from it, the strongest it → [[CD109]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.74×** | +15.2 | 0e+00 | 19/24 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +15.0 | 0e+00 | 18/22 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +11.7 | 2e-29 | 16/22 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.016 | 6/25 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.7 | 0.026 | 5/23 (NCI-H1792, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.039 | 9/24 (CFPAC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.082 | 16/23 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.379×** | -20.7 | 0e+00 | 22/23 (RPMI-7951, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.361×** | -15.4 | 0e+00 | 23/23 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.502×** | -10.4 | 4e-23 | 21/23 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.518×** | -9.9 | 4e-21 | 23/23 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.520×** | -9.9 | 5e-21 | 20/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.523×** | -9.4 | 4e-19 | 19/23 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.682×** | -5.8 | 6e-07 | 17/23 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.701×** | -5.4 | 5e-06 | 20/23 (HepG2/C3A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.703×** | -5.3 | 7e-06 | 16/23 (H4, J82, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.716×** | -5.1 | 2e-05 | 15/23 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.734×** | -4.7 | 1e-04 | 13/23 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.741×** | -4.5 | 3e-04 | 18/23 (J82, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -4.1 | 0.002 | 0/25 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.003 | 15/23 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.758×** | -3.9 | 0.004 | 2/23 (SW480, SW1417) | inconsistent across doses |  |
| [[Pimozide (drug)]] 5 µM |  | **0.795×** | -3.5 | 0.019 | 0/23 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 240 | 3 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Cobimetinib (drug)]] 0.5 µM 2.50× (z +9.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.200× (z -15.9) |
| [[SW480 (line)]] | alt | 59.9 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -16.0) |
| [[HS-578T (line)]] | alt | 1,328 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -27.6) |
| [[NCI-H460 (line)]] | wt | 526 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -15.9) |
| [[HOP62 (line)]] | alt | 564 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -26.7) |
| [[J82 (line)]] | alt | 129 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -19.1) |
| [[A498 (line)]] | wt | 343 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 185 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -15.5) |
| [[H4 (line)]] | wt | 1,063 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -33.0) |
| [[HepG2_C3A (line)]] | wt | 328 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 618 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0603× (z -35.2) |
| [[SW1417 (line)]] | alt | 201 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -16.2) |
| [[PANC-1 (line)]] | alt | 168 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 120 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +10.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 115 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -21.9) |
| [[NCI-H2347 (line)]] | alt | 130 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -17.2) |
| [[Panc 03.27 (line)]] | alt | 86.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -11.0) |
| [[SNU-423 (line)]] | alt | 530 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.0) |
| [[SW 1088 (line)]] | alt | 2,700 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -17.5) |
| [[SW 900 (line)]] | alt | 121 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.8) |
| [[hTERT-HPNE (line)]] | wt | 843 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -15.6) |
| [[LOX-IMVI (line)]] | wt | 76.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.146× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 51.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +10.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 29.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 42.4 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 45.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 32.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 29.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 26.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 20.4 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NID2]] | +0.66 | +0.57 / +0.73 | both halves | 9e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL3A1]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 531 |
| [[MMP2]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 621 |
| [[EFEMP1]] | +0.63 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[POSTN]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 643 |
| [[PDGFRB]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL5A2]] | +0.61 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 417 |
| [[COL4A1]] | +0.60 | +0.49 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 691 |
| [[CDK15]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SPARC]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 609 |
| [[ANTXR1]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ITGA4]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 5, C 20. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | PRSS23 activity raises TGFBI's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without PRSS23 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[CD109]] | B | CD109 activity raises TGFBI's level | lines that do not express CD109 (15) vs lines expressing it (35) | 4.58× lower at baseline in the lines without CD109 | 0.051 | ⚠ within organs, on part of the lines; also absent: KMO, PID1, EVA1A-AS |
| [[FBN1]] | B | FBN1 activity raises TGFBI's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.91× lower at baseline in the lines without FBN1 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[MXRA8]] | B | MXRA8 activity raises TGFBI's level | lines that do not express MXRA8 (33) vs lines expressing it (17) | 3.02× lower at baseline in the lines without MXRA8 | 0.064 | ⚠ within organs, on part of the lines; also absent: CARMN, MEG8, MEG3 |
| [[MYOF]] | B | MYOF activity raises TGFBI's level | lines that do not express MYOF (6) vs lines expressing it (44) | 3.25× lower at baseline in the lines without MYOF | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |
| [[NID2]] | C | NID2 activity raises TGFBI's level | lines that do not express NID2 (32) vs lines expressing it (18) | 6.26× lower at baseline in the lines without NID2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises TGFBI's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 7.36× lower at baseline in the lines without IGFBP7 | 0.003 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises TGFBI's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.90× lower at baseline in the lines without PDGFRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[CA12]] | C | CA12 activity raises TGFBI's level | lines that do not express CA12 (29) vs lines expressing it (21) | 4.23× lower at baseline in the lines without CA12 | 0.004 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[SMIM10]] | C | SMIM10 activity raises TGFBI's level | lines that do not express SMIM10 (24) vs lines expressing it (26) | 5.08× lower at baseline in the lines without SMIM10 | 0.005 | ⚠ within organs, on part of the lines; also absent: SNAI2, MCAM, ZNF365; co-absent with the target |
| [[CARMN]] | C | CARMN activity raises TGFBI's level | lines that do not express CARMN (40) vs lines expressing it (10) | 8.48× lower at baseline in the lines without CARMN | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, TMPRSS15, DCN; co-absent with the target |
| [[SLC8A1]] | C | SLC8A1 activity raises TGFBI's level | lines that do not express SLC8A1 (26) vs lines expressing it (24) | 4.86× lower at baseline in the lines without SLC8A1 | 0.013 | ⚠ within organs, on part of the lines; also absent: DPY19L2, MAGI2, MAGI2-AS3; co-absent with the target |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 7, C 14. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD109]] | B | TGFBI activity raises CD109's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.75× lower at baseline in the lines without TGFBI | 0.011 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[PTPN14]] | B | TGFBI activity raises PTPN14's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 1.61× lower at baseline in the lines without TGFBI | 0.049 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[PRSS23]] | B | TGFBI activity raises PRSS23's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.54× lower at baseline in the lines without TGFBI | 0.054 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[COL6A1]] | B | TGFBI activity raises COL6A1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.24× lower at baseline in the lines without TGFBI | 0.057 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| cells under [[Arbutin (drug)]] 5 µM | B | TGFBI activity raises the cells' numbers under Arbutin 5 µM (protects the cells) | lines that do not express TGFBI (25) vs lines expressing it (23) | the lines without TGFBI: 0.81× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[THBS1]] | B | TGFBI activity raises THBS1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without TGFBI | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[ARHGEF6]] | B | TGFBI activity raises ARHGEF6's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without TGFBI | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[BICC1]] | C | TGFBI activity raises BICC1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 4.12× lower at baseline in the lines without TGFBI | 0.013 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[SMIM10]] | C | TGFBI activity raises SMIM10's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.21× lower at baseline in the lines without TGFBI | 0.016 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[EDIL3]] | C | TGFBI activity raises EDIL3's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 4.69× lower at baseline in the lines without TGFBI | 0.016 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[CDK15]] | C | TGFBI activity raises CDK15's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 2.09× lower at baseline in the lines without TGFBI | 0.026 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[EFEMP1]] | C | TGFBI activity raises EFEMP1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.63× lower at baseline in the lines without TGFBI | 0.035 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.4, 22.3); signed map (25.5, 42.2). **Vector** length 90.9, 30.1% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.54 to 16); *Integrin cell surface interactions* (reactome, mean cos +0.55 to 10); *ECM proteoglycans* (reactome, mean cos +0.54 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.7 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.1 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -5.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -9.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | transforming growth factor beta induced |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:136,028,988-136,063,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BIGH3, CDB1, CDGG1; previously CSD3, LCD1, CSD1, CSD2 |
| Hallmark sets | APICAL_JUNCTION, GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 1 pathways, smallest: Amyloid fiber formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15582](https://www.uniprot.org/uniprotkb/Q15582) (Transforming growth factor-beta-induced protein ig-h3):

> Plays a role in cell adhesion. May play a role in cell-collagen interactions (By similarity).

**Summary**, from NCBI Gene [7045](https://www.ncbi.nlm.nih.gov/gene/7045):

> This gene encodes an RGD-containing protein that binds to type I, II and IV collagens. The RGD motif is found in many extracellular matrix proteins modulating cell adhesion and serves as a ligand recognition sequence for several integrins. This protein plays a role in cell-collagen interactions and may be involved in endochondrial bone formation in cartilage. The protein is induced by transforming growth factor-beta and acts to inhibit cell adhesion. Mutations in this gene are associated with …

**Accessions** — [HGNC:11771](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11771) · Entrez [7045](https://www.ncbi.nlm.nih.gov/gene/7045) · UniProt [Q15582](https://www.uniprot.org/uniprotkb/Q15582) · Ensembl [ENSG00000120708](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120708)

## Data

Gene col 4212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4212); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4212]; `tensor/DDL_lfc|DDL_z.npy` [4212]; `embed/gene_vectors.npy` [4212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4212 or target_col == 4212). Every well: [[TGFBI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TGFBI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
