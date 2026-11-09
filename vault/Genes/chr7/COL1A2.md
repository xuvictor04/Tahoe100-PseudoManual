---
symbol: "COL1A2"
type: "gene"
col: 8991
ensembl_id: "ENSG00000164692"
name: "collagen type I alpha 2 chain"
location: "7q21.3"
module: 66
arm: "+"
pooled_cpm: 87.98
n_lines_expressing: 13
n_dd_up: 8
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 37
direction_downstream: 39
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL1A2

*collagen type I alpha 2 chain* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.25× (z +13.9, q 3e-41, up in 7 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +6.7, q 3e-09, up in 4 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.499× (z -7.5, q 4e-11, down in 11 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPARC]] (+0.80, fdr 7e-06), [[COL1A1]] (+0.75, fdr 7e-06), [[COL3A1]] (+0.74, fdr 7e-06); moves opposite to [[ARHGEF5]] (-0.47, fdr 3e-04), [[GSTO2]] (-0.45, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 37 arrows point to it, the strongest [[RPH3AL]] → it (grade B ⚠); 39 go from it, the strongest it → [[TET1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8991.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.25×** | +13.9 | 3e-41 | 7/12 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.50×** | +12.4 | 4e-33 | 6/10 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +6.7 | 3e-09 | 4/12 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +6.7 | 4e-09 | 4/10 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.09×** | +4.5 | 9e-04 | 4/7 (SNU-423, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +4.3 | 0.002 | 3/13 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.72×** | +3.8 | 0.013 | 8/11 (MIA PaCa-2, AN3 CA, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.040 | 6/10 (MIA PaCa-2, A-172, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8991.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.499×** | -7.5 | 4e-11 | 11/11 (AN3 CA, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.410×** | -6.8 | 3e-09 | 10/11 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.504×** | -5.2 | 3e-05 | 11/11 (C32, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.521×** | -5.0 | 9e-05 | 9/11 (C32, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.537×** | -4.7 | 2e-04 | 1/10 (MIA PaCa-2) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.556×** | -4.3 | 0.002 | 10/11 (AN3 CA, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.586×** | -4.1 | 0.004 | 9/11 (SNU-423, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.593×** | -3.7 | 0.016 | 0/11 | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.626×** | -3.6 | 0.022 | 3/10 (J82, AN3 CA, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.667× | -3.1 | 0.11 | 8/11 (hTERT-HPNE, MIA PaCa-2, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.753× | -3.1 | 0.11 | 9/11 (hTERT-HPNE, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8991. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 589 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0644× (z -23.0) |
| [[A-172 (line)]] | wt | 454 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -15.0) |
| [[C32 (line)]] | wt | 174 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -21.3) |
| [[RPMI-7951 (line)]] | alt | 1,317 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -15.5) |
| [[SNU-423 (line)]] | alt | 300 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -13.0) |
| [[NCI-H661 (line)]] | alt | 536 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -14.7) |
| [[SW 1088 (line)]] | alt | 642 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.1) |
| [[HS-578T (line)]] | alt | 1,312 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 910 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -8.5) |
| [[J82 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.02× (z +11.9) ⚠ position not correctable | — |
| [[A-427 (line)]] | wt | 4.40 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.62 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.34 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.21 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.45 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 87.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.24 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 6.47 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.33 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 8.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.32 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8991), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPARC]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 959 |
| [[COL1A1]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[COL3A1]] | +0.74 | +0.75 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[FBN1]] | +0.72 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 965 |
| [[PDGFRB]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 629 |
| [[NID2]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 536 |
| [[AEBP1]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 | STRING 578 |
| [[DKK3]] | +0.68 | +0.69 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LOXL3]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures |
| [[SDC2]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[IGFBP5]] | +0.65 | +0.57 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_UV_RESPONSE_DN; STRING 494 |
| [[TIMP3]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 662 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF5]] | -0.47 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[GSTO2]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 1, C 36. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPH3AL]] | B | RPH3AL activity lowers COL1A2's level | lines that do not express RPH3AL (10) vs lines expressing it (40) | 10.30× higher at baseline in the lines without RPH3AL | 0.030 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, PATJ; maybe low, not absent |
| [[FBN1]] | C | FBN1 activity raises COL1A2's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 8.54× lower at baseline in the lines without FBN1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises COL1A2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 7.88× lower at baseline in the lines without PRRX1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises COL1A2's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 7.83× lower at baseline in the lines without COL1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[THY1]] | C | THY1 activity raises COL1A2's level | lines that do not express THY1 (38) vs lines expressing it (12) | 12.22× lower at baseline in the lines without THY1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises COL1A2's level | lines that do not express SPARC (34) vs lines expressing it (16) | 10.56× lower at baseline in the lines without SPARC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[LOXL3]] | C | LOXL3 activity raises COL1A2's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 5.87× lower at baseline in the lines without LOXL3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent; co-absent with the target |
| [[IHO1]] | C | IHO1 activity raises COL1A2's level | lines that do not express IHO1 (36) vs lines expressing it (14) | 6.07× lower at baseline in the lines without IHO1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DCT, TYR, ENSG00000253474; maybe low, not absent; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises COL1A2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 12.72× lower at baseline in the lines without PDGFRB | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises COL1A2's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 13.13× lower at baseline in the lines without AEBP1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises COL1A2's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 9.29× lower at baseline in the lines without COL5A2 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[DIRAS3]] | C | DIRAS3 activity raises COL1A2's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 11.22× lower at baseline in the lines without DIRAS3 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 8, C 31. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TET1]] | B | COL1A2 activity raises TET1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 3.53× lower at baseline in the lines without COL1A2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[CNPY4]] | B | COL1A2 activity raises CNPY4's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 1.83× lower at baseline in the lines without COL1A2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[SMPD1]] | B | COL1A2 activity raises SMPD1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without COL1A2 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[RPH3AL]] | B | COL1A2 activity lowers RPH3AL's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.72× higher at baseline in the lines without COL1A2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[EML1]] | B | COL1A2 activity raises EML1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 3.40× lower at baseline in the lines without COL1A2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[PLOD1]] | B | COL1A2 activity raises PLOD1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without COL1A2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[BSG]] | B | COL1A2 activity raises BSG's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 1.46× lower at baseline in the lines without COL1A2 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[P3H3]] | B | COL1A2 activity raises P3H3's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 2.09× lower at baseline in the lines without COL1A2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5 |
| [[COL5A2]] | C | COL1A2 activity raises COL5A2's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 8.74× lower at baseline in the lines without COL1A2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[COL3A1]] | C | COL1A2 activity raises COL3A1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 9.41× lower at baseline in the lines without COL1A2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[PRRX1]] | C | COL1A2 activity raises PRRX1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 5.83× lower at baseline in the lines without COL1A2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[FBN1]] | C | COL1A2 activity raises FBN1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 7.90× lower at baseline in the lines without COL1A2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.6, 21.9); signed map (25.9, 42.6). **Vector** length 55.1, 20.9% of its response variance represented; |z| ≥ 3 in 413 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NCAM1 interactions* (reactome, mean cos +0.52 to 5); *NCAM signaling for neurite out-growth* (reactome, mean cos +0.52 to 5); *Signaling by PDGF* (reactome, mean cos +0.55 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +12.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | collagen type I alpha 2 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q21.3 — chr7:94,394,895-94,431,227 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously OI4 |
| Gene groups (HGNC) | Fibrillar collagens |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 46 pathways, smallest: Defective VWF cleavage by ADAMTS13 variant; Defects of platelet adhesion to exposed collagen; Enhanced cleavage of VWF variant by ADAMTS13 |
| Matched by | ensembl_id |

**Function**, from UniProt [P08123](https://www.uniprot.org/uniprotkb/P08123) (Collagen alpha-2(I) chain):

> Type I collagen is a member of group I collagen (fibrillar forming collagen).

**Summary**, from NCBI Gene [1278](https://www.ncbi.nlm.nih.gov/gene/1278):

> This gene encodes the pro-alpha2 chain of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIB, recessive Ehlers-Danlos syndrome Classical type, idiopathic osteoporosis, and atypical Marfan syndrome. Symptoms associated with mutations …

**Accessions** — [HGNC:2198](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2198) · Entrez [1278](https://www.ncbi.nlm.nih.gov/gene/1278) · UniProt [P08123](https://www.uniprot.org/uniprotkb/P08123) · Ensembl [ENSG00000164692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164692)

## Data

Gene col 8991: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8991); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8991, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8991]; `tensor/DDL_lfc|DDL_z.npy` [8991]; `embed/gene_vectors.npy` [8991]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8991 or target_col == 8991). Every well: [[COL1A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL1A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
