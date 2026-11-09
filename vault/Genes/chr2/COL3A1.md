---
symbol: "COL3A1"
type: "gene"
col: 9667
ensembl_id: "ENSG00000168542"
name: "collagen type III alpha 1 chain"
location: "2q32.2"
module: 66
arm: "+"
pooled_cpm: 37.64
n_lines_expressing: 15
n_dd_up: 19
n_dd_down: 14
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 35
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL3A1

*collagen type III alpha 1 chain* — 2q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.99× (z +17.8, q 0e+00, up in 9 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.5, q 7e-12, up in 5 of 13 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.557× (z -5.8, q 3e-06, down in 8 of 12 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POSTN]] (+0.77, fdr 7e-06), [[SPARC]] (+0.77, fdr 7e-06), [[COL1A1]] (+0.75, fdr 7e-06); moves opposite to [[ZC3H8]] (-0.45, fdr 5e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 35 go from it, the strongest it → [[PRRT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.99×** | +17.8 | 0e+00 | 9/12 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.37×** | +17.7 | 0e+00 | 5/9 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.67×** | +11.9 | 1e-30 | 6/9 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.5 | 7e-12 | 5/13 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.43×** | +6.4 | 2e-08 | 5/9 (A-172, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +5.9 | 3e-07 | 3/13 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +4.7 | 2e-04 | 8/13 (hTERT-HPNE, HS-578T, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 2e-04 | 10/13 (hTERT-HPNE, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +4.5 | 4e-04 | 9/13 (hTERT-HPNE, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.003 | 8/12 (hTERT-HPNE, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.005 | 2/11 (J82, A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.005 | 3/13 (A-172, J82, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.48×** | +3.9 | 0.005 | 3/13 (NCI-H661, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.46×** | +3.8 | 0.007 | 0/13 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.017 | 3/13 (NCI-H460, J82, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.030 | 1/12 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.048 | 0/13 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.557×** | -5.8 | 3e-06 | 8/12 (CHP-212, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.574×** | -5.5 | 8e-06 | 10/12 (H4, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.564×** | -5.5 | 8e-06 | 6/12 (CHP-212, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.680×** | -3.9 | 0.015 | 7/13 (J82, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.682×** | -3.8 | 0.015 | 6/13 (hTERT-HPNE, CHP-212, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.698×** | -3.6 | 0.032 | 0/12 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.683×** | -3.5 | 0.035 | 0/13 | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.714×** | -3.4 | 0.053 | 9/13 (J82, CHP-212, …) | all doses, flat |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **0.716×** | -3.3 | 0.053 | 2/13 (A-427, RPMI-7951) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.719×** | -3.3 | 0.056 | 7/13 (hTERT-HPNE, J82, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.636×** | -3.2 | 0.067 | 2/13 (hTERT-HPNE, J82) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.727×** | -3.2 | 0.068 | 0/13 | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.802×** | -3.1 | 0.078 | 6/13 (hTERT-HPNE, A-172, …) | top dose only |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | **0.735×** | -3.1 | 0.084 | 1/13 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 611 | 5 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +11.1) | [[Verteporfin (drug)]] 5 µM 0.287× (z -10.5) |
| [[J82 (line)]] | alt | 128 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 7.23× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.159× (z -12.5) |
| [[CHP-212 (line)]] | wt | 597 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 10.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 37.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0234× (z -16.4) |
| [[A-427 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -9.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[hTERT-HPNE (line)]] | wt | 246 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 43.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.4) |
| [[A498 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.75 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 318 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 785 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POSTN]] | +0.77 | +0.70 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_ANGIOGENESIS; STRING 976 |
| [[SPARC]] | +0.77 | +0.77 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 911 |
| [[COL1A1]] | +0.75 | +0.66 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[COL1A2]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[COL5A2]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ANGIOGENESIS; STRING 998; ⚠ same locus (19.2 kb: neighbours can correlate without regulation) |
| [[MMP2]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 799 |
| [[NID2]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 562 |
| [[COL4A1]] | +0.66 | +0.69 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 856 |
| [[OLFML2A]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[TGFBI]] | +0.64 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 531 |
| [[NREP]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[CHRDL1]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[FBN1]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 970 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H8]] | -0.45 | -0.39 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers COL3A1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[THY1]] | C | THY1 activity raises COL3A1's level | lines that do not express THY1 (38) vs lines expressing it (12) | 20.95× lower at baseline in the lines without THY1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises COL3A1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 9.41× lower at baseline in the lines without COL1A2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[COL11A1]] | C | COL11A1 activity raises COL3A1's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 12.15× lower at baseline in the lines without COL11A1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises COL3A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 7.98× lower at baseline in the lines without SPARC | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[FBN1]] | C | FBN1 activity raises COL3A1's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 4.97× lower at baseline in the lines without FBN1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL3A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 11.24× lower at baseline in the lines without PDGFRB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises COL3A1's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 6.01× lower at baseline in the lines without COL5A2 | 0.037 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises COL3A1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 9.00× lower at baseline in the lines without PCDH18 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises COL3A1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 5.95× lower at baseline in the lines without COL1A1 | 0.052 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[POSTN]] | C | POSTN activity raises COL3A1's level | lines that do not express POSTN (38) vs lines expressing it (12) | 8.52× lower at baseline in the lines without POSTN | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: APBB1IP, SLC25A24P1, THY1; co-absent with the target |
| [[LDOC1]] | C | LDOC1 activity raises COL3A1's level | lines that do not express LDOC1 (21) vs lines expressing it (29) | 4.52× lower at baseline in the lines without LDOC1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SPANXA2-OT1, S1PR3, SNAP91; co-absent with the target; its own permutation p |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 9, C 26. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRT2]] | B | COL3A1 activity raises PRRT2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.32× lower at baseline in the lines without COL3A1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[NREP]] | B | COL3A1 activity raises NREP's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.77× lower at baseline in the lines without COL3A1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[CNPY4]] | B | COL3A1 activity raises CNPY4's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.94× lower at baseline in the lines without COL3A1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[OLFML2A]] | B | COL3A1 activity raises OLFML2A's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.69× lower at baseline in the lines without COL3A1 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[FKBP7]] | B | COL3A1 activity raises FKBP7's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.03× lower at baseline in the lines without COL3A1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[LAMB2]] | B | COL3A1 activity raises LAMB2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.64× lower at baseline in the lines without COL3A1 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[MYL9]] | B | COL3A1 activity raises MYL9's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 2.15× lower at baseline in the lines without COL3A1 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[SMPD1]] | B | COL3A1 activity raises SMPD1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without COL3A1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[LAMP1]] | B | COL3A1 activity raises LAMP1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.39× lower at baseline in the lines without COL3A1 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677 |
| [[COL5A2]] | C | COL3A1 activity raises COL5A2's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 12.02× lower at baseline in the lines without COL3A1 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[CHRDL1]] | C | COL3A1 activity raises CHRDL1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 1.95× lower at baseline in the lines without COL3A1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[KCNE4]] | C | COL3A1 activity raises KCNE4's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 4.66× lower at baseline in the lines without COL3A1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.1, 22.3); signed map (25.6, 42.4). **Vector** length 40.8, 10.8% of its response variance represented; |z| ≥ 3 in 369 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Crosslinking of collagen fibrils* (reactome, mean cos +0.65 to 5); *Anchoring fibril formation* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +17.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.6 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.0 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | collagen type III alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2 — chr2:188,974,373-189,012,746 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously EDS4A |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Fibrillar collagens |
| Hallmark sets | ANGIOGENESIS, UV_RESPONSE_DN, MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 31 pathways, smallest: Scavenging by Class A Receptors; Fibronectin matrix formation; Developmental Lineage of Pancreatic Ductal Cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P02461](https://www.uniprot.org/uniprotkb/P02461) (Collagen alpha-1(III) chain):

> Collagen type III occurs in most soft connective tissues along with type I collagen. Involved in regulation of cortical development. Is the major ligand of ADGRG1 in the developing brain and binding to ADGRG1 inhibits neuronal migration and activates the RhoA pathway by coupling ADGRG1 to GNA13 and possibly GNA12.

**Summary**, from NCBI Gene [1281](https://www.ncbi.nlm.nih.gov/gene/1281):

> This gene encodes the pro-alpha1 chains of type III collagen, a fibrillar collagen that is found in extensible connective tissues such as skin, lung, uterus, intestine and the vascular system, frequently in association with type I collagen. Mutations in this gene are associated with Ehlers-Danlos syndrome type IV, and with aortic and arterial aneurysms. [provided by R. Dalgleish, Feb 2008]

**Accessions** — [HGNC:2201](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2201) · Entrez [1281](https://www.ncbi.nlm.nih.gov/gene/1281) · UniProt [P02461](https://www.uniprot.org/uniprotkb/P02461) · Ensembl [ENSG00000168542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168542)

## Data

Gene col 9667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9667); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9667]; `tensor/DDL_lfc|DDL_z.npy` [9667]; `embed/gene_vectors.npy` [9667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9667 or target_col == 9667). Every well: [[COL3A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL3A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
