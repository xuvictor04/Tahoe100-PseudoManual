---
symbol: "NID2"
type: "gene"
col: 1501
ensembl_id: "ENSG00000087303"
name: "nidogen 2"
location: "14q22.1"
module: 66
arm: "+"
pooled_cpm: 10.22
n_lines_expressing: 18
n_dd_up: 23
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 27
direction_downstream: 26
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# NID2

*nidogen 2* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.85× (z +14.1, q 4e-42, up in 10 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +11.1, q 3e-26, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.563× (z -6.0, q 1e-06, down in 11 of 15 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPARC]] (+0.74, fdr 7e-06), [[MMP2]] (+0.70, fdr 7e-06), [[COL1A2]] (+0.69, fdr 7e-06); moves opposite to [[IKBKB]] (-0.49, fdr 6e-05), [[MTHFS]] (-0.47, fdr 1e-04), [[ZC3H12C]] (-0.47, fdr 9e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[IGFBP6]] → it (grade B ⚠); 26 go from it, the strongest it → [[PAPSS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.85×** | +14.1 | 4e-42 | 10/14 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +13.0 | 2e-36 | 7/10 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +11.1 | 3e-26 | 7/14 (HS-578T, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.98×** | +10.5 | 1e-23 | 9/12 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +8.5 | 3e-15 | 10/15 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +5.7 | 9e-07 | 2/13 (Panc 03.27, A549) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 1e-06 | 9/15 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 7e-05 | 7/14 (Panc 03.27, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.5 | 5e-04 | 5/14 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.3 | 0.001 | 4/15 (SNU-423, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.2 | 0.001 | 2/16 (Panc 03.27, A498) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +4.2 | 0.002 | 10/15 (HOP62, A549, …) | rises with dose | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.1 | 0.002 | 2/10 (SNU-423, NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.8 | 0.006 | 4/14 (A549, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.8 | 0.006 | 2/13 (NCI-H460, HOP62) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.011 | 7/14 (NCI-H460, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.018 | 2/14 (A549, HOP62) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.039 | 1/14 (H4) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.088 | 3/15 (hTERT-HPNE, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.563×** | -6.0 | 1e-06 | 11/15 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.606×** | -5.0 | 2e-04 | 12/15 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Futibatinib (drug)]] 0.05 µM |  | **0.666×** | -4.0 | 0.009 | 2/15 (HEC-1-A, LoVo) | inconsistent across doses | position effect removed |
| [[Adenosine (drug)]] 0.5 µM |  | **0.681×** | -4.0 | 0.009 | 0/15 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -3.8 | 0.015 | 11/14 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.047 | 0/15 | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.719×** | -3.4 | 0.050 | 7/15 (HOP62, LoVo, …) | top dose only |  |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.717×** | -3.4 | 0.050 | 0/15 | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.736×** | -3.2 | 0.089 | 9/14 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | 0.735× | -3.1 | 0.12 | 1/15 (RPMI-7951) | all doses, flat | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.745× | -3.1 | 0.12 | 0/15 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.731× | -3.0 | 0.12 | 1/15 (CHP-212) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 174 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0927× (z -20.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0472× (z -18.7) |
| [[SNU-423 (line)]] | alt | 57.9 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -15.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -15.2) |
| [[RPMI-7951 (line)]] | alt | 40.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -16.2) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -14.2) |
| [[H4 (line)]] | wt | 21.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0811× (z -10.9) |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.779 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.754 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.939 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPARC]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 445 |
| [[MMP2]] | +0.70 | +0.64 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[COL1A2]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 536 |
| [[PDGFRB]] | +0.68 | +0.58 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 421 |
| [[COL3A1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 562 |
| [[DKK3]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TGFBI]] | +0.66 | +0.57 / +0.73 | both halves | 9e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FBN1]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 465 |
| [[COL1A1]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 643 |
| [[OLFML2A]] | +0.60 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[GLIS1]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ARHGEF6]] | +0.59 | +0.44 / +0.69 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKBKB]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[MTHFS]] | -0.47 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ZC3H12C]] | -0.47 | -0.48 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 1, C 26. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGFBP6]] | B | IGFBP6 activity raises NID2's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without IGFBP6 | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[PDGFRB]] | C | PDGFRB activity raises NID2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.82× lower at baseline in the lines without PDGFRB | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises NID2's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.69× lower at baseline in the lines without C5orf46 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[CA12]] | C | CA12 activity raises NID2's level | lines that do not express CA12 (29) vs lines expressing it (21) | 2.84× lower at baseline in the lines without CA12 | 0.003 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1; co-absent with the target |
| [[COL4A1]] | C | COL4A1 activity raises NID2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 3.60× lower at baseline in the lines without COL4A1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[CHSY3]] | C | CHSY3 activity raises NID2's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 3.24× lower at baseline in the lines without CHSY3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises NID2's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 2.75× lower at baseline in the lines without PDE3A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises NID2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.69× lower at baseline in the lines without FBN1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises NID2's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 2.76× lower at baseline in the lines without SEMA5A | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[SIRLNT]] | C | SIRLNT activity raises NID2's level | lines that do not express SIRLNT (32) vs lines expressing it (18) | 3.73× lower at baseline in the lines without SIRLNT | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises NID2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 3.17× lower at baseline in the lines without ITGA4 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises NID2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.65× lower at baseline in the lines without COL3A1 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 6, C 20. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS2]] | B | NID2 activity raises PAPSS2's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without NID2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[PAPSS2]] | B | NID2 activity strengthens PAPSS2's drug response | lines that do not express NID2 (20) vs lines expressing it (13) | the lines without NID2 respond 0.72× as strongly (z diff +1.62); strongest at Digitoxin 5 µM: 0.43x vs 0.32x (z diff +2.9) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; target measured in part of the lines; artifact flags |
| [[ZC3H12C]] | B | NID2 activity raises ZC3H12C's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without NID2 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[ARHGEF6]] | B | NID2 activity raises ARHGEF6's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.84× lower at baseline in the lines without NID2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[OLFML2A]] | B | NID2 activity raises OLFML2A's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.42× lower at baseline in the lines without NID2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[P2RX7]] | B | NID2 activity raises P2RX7's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.22× lower at baseline in the lines without NID2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1 |
| [[CA12]] | C | NID2 activity raises CA12's level | lines that do not express NID2 (32) vs lines expressing it (18) | 8.51× lower at baseline in the lines without NID2 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[COL4A2]] | C | NID2 activity raises COL4A2's level | lines that do not express NID2 (32) vs lines expressing it (18) | 9.41× lower at baseline in the lines without NID2 | 1e-03 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[COL4A1]] | C | NID2 activity raises COL4A1's level | lines that do not express NID2 (32) vs lines expressing it (18) | 9.25× lower at baseline in the lines without NID2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[TGFBI]] | C | NID2 activity raises TGFBI's level | lines that do not express NID2 (32) vs lines expressing it (18) | 6.26× lower at baseline in the lines without NID2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[PDGFRB]] | C | NID2 activity raises PDGFRB's level | lines that do not express NID2 (32) vs lines expressing it (18) | 5.12× lower at baseline in the lines without NID2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |
| [[SIRLNT]] | C | NID2 activity raises SIRLNT's level | lines that do not express NID2 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without NID2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, LINC01411, COL4A1; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.9, 21.8); signed map (25.7, 43.0). **Vector** length 48.7, 14.4% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Integrin cell surface interactions* (reactome, mean cos +0.52 to 10); *ECM proteoglycans* (reactome, mean cos +0.52 to 9); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +10.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +11.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nidogen 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:52,004,809-52,069,059 (-) |
| Ensembl biotype | protein_coding |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 2 pathways, smallest: Laminin interactions; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14112](https://www.uniprot.org/uniprotkb/Q14112) (Nidogen-2):

> Cell adhesion glycoprotein which is widely distributed in basement membranes. Binds to collagens I and IV, to perlecan and to laminin 1. Does not bind fibulins. It probably has a role in cell-extracellular matrix interactions.

**Summary**, from NCBI Gene [22795](https://www.ncbi.nlm.nih.gov/gene/22795):

> This gene encodes a member of the nidogen family of basement membrane proteins. This protein is a cell-adhesion protein that binds collagens I and IV and laminin and may be involved in maintaining the structure of the basement membrane.[provided by RefSeq, Jun 2010]

**Accessions** — [HGNC:13389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13389) · Entrez [22795](https://www.ncbi.nlm.nih.gov/gene/22795) · UniProt [Q14112](https://www.uniprot.org/uniprotkb/Q14112) · Ensembl [ENSG00000087303](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087303)

## Data

Gene col 1501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1501); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1501]; `tensor/DDL_lfc|DDL_z.npy` [1501]; `embed/gene_vectors.npy` [1501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1501 or target_col == 1501). Every well: [[NID2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NID2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
