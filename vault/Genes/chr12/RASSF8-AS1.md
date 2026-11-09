---
symbol: "RASSF8-AS1"
type: "gene"
col: 14470
ensembl_id: "ENSG00000246695"
name: "RASSF8 antisense RNA 1"
location: "12p12.1"
module: 80
arm: "+"
pooled_cpm: 16.23
n_lines_expressing: 36
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# RASSF8-AS1

*RASSF8 antisense RNA 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.90× (z +20.8, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.545× (z -8.3, q 6e-14, down in 21 of 34 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DENND5B-AS1]] (+0.71, fdr 7e-06), [[TMLHE-AS1]] (+0.61, fdr 8e-05), [[LPXN]] (+0.60, fdr 3e-05); moves opposite to [[LRRC42]] (-0.57, fdr 8e-05), [[ELP1]] (-0.57, fdr 1e-04), [[IFT172]] (-0.53, fdr 2e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[LRRC8C-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14470.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.90×** | +20.8 | 0e+00 | 31/32 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +9.3 | 6e-18 | 22/31 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +7.7 | 2e-12 | 16/33 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +6.6 | 5e-09 | 20/33 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.5 | 1e-08 | 15/26 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +5.8 | 5e-07 | 12/22 (C32, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +5.8 | 5e-07 | 16/34 (SW480, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.8 | 5e-07 | 7/17 (LOX-IMVI, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.6 | 1e-06 | 18/34 (SW480, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.6 | 1e-06 | 15/33 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.28×** | +4.8 | 7e-05 | 13/34 (SK-MEL-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 5e-04 | 13/33 (SW480, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.036 | 9/33 (CHP-212, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belzutifan (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.037 | 9/29 (MIA PaCa-2, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.044 | 3/34 (NCI-H23, A-427, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.053 | 7/32 (J82, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14470.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.545×** | -8.3 | 6e-14 | 21/34 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.369×** | -7.1 | 2e-10 | 17/31 (MIA PaCa-2, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -7.1 | 2e-10 | 21/33 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.866× | -6.6 | 5e-09 | 10/34 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.680×** | -5.3 | 2e-05 | 17/34 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -4.6 | 4e-04 | 15/32 (NCI-H460, RPMI-7951, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -4.3 | 0.002 | 14/27 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.758×** | -3.8 | 0.011 | 12/33 (NCI-H460, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | 0.794× | -3.1 | 0.11 | 16/31 (PANC-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.795× | -3.1 | 0.11 | 9/34 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14470. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.4 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.206× (z -15.7) |
| [[PANC-1 (line)]] | alt | 33.2 | 2 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -12.9) |
| [[SW480 (line)]] | alt | 14.6 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +18.8) | — |
| [[NCI-H23 (line)]] | alt | 40.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.255× (z -9.9) ⚠ toxic |
| [[A-427 (line)]] | wt | 26.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +8.7) | [[Orlistat (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 10.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +15.2) | — |
| [[A549 (line)]] | wt | 6.43 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.514× (z -18.6) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 9.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +11.4) | — |
| [[J82 (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +11.5) | — |
| [[LoVo (line)]] | wt | 4.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.1× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 8.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +10.5) | — |
| [[AN3 CA (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.44 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14470), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND5B-AS1]] | +0.71 | +0.69 / +0.59 | both halves | 7e-06 | same gene group |
| [[TMLHE-AS1]] | +0.61 | +0.63 / +0.37 | both halves | 8e-05 | same gene group |
| [[LPXN]] | +0.60 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[BASP1-AS1]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 | same gene group |
| [[PPEF1]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[WAKMAR2]] | +0.59 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[CDK6-AS1]] | +0.58 | +0.55 / +0.38 | both halves | 7e-05 | same gene group |
| [[EDARADD]] | +0.58 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[FRMD6-AS2]] | +0.58 | +0.61 / +0.37 | both halves | 9e-05 | same gene group |
| [[LINC01829]] | +0.58 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[MIR1915HG]] | +0.57 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[BHLHE40-AS1]] | +0.57 | +0.54 / +0.34 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC42]] | -0.57 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[ELP1]] | -0.57 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[IFT172]] | -0.53 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[OXNAD1]] | -0.53 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[ILVBL]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[IMPDH1]] | -0.49 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[PIK3R2]] | -0.49 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[POT1]] | -0.49 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[SKIC3]] | -0.48 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[CEP192]] | -0.48 | -0.42 / -0.28 | both halves | 3e-04 |  |
| [[TBCD]] | -0.48 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[GTPBP3]] | -0.47 | -0.37 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 7, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises RASSF8-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without CYP1B1-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises RASSF8-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.34× lower at baseline in the lines without MIR1915HG | 0.067 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[BASP1-AS1]] | B | BASP1-AS1 activity raises RASSF8-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.99× lower at baseline in the lines without BASP1-AS1 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[LINC01010]] | B | LINC01010 activity raises RASSF8-AS1's level | lines that do not express LINC01010 (29) vs lines expressing it (21) | 3.14× lower at baseline in the lines without LINC01010 | 0.094 | ⚠ within organs, on part of the lines; also absent: TRIML2, PHACTR1, LINC01776 |
| [[HDAC6]] | B | HDAC6 activity raises RASSF8-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CFAP58]] | B | CFAP58 activity raises RASSF8-AS1's level | lines that do not express CFAP58 (6) vs lines expressing it (44) | 2.39× lower at baseline in the lines without CFAP58 | 0.097 | ⚠ within organs, on part of the lines; also absent: MINDY4, ENSG00000286162, MPP4; maybe low, not absent |
| [[RASSF8]] | C | RASSF8 activity raises RASSF8-AS1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 5.48× lower at baseline in the lines without RASSF8 | 1e-05 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1; co-absent with the target |
| [[NTNG2]] | C | NTNG2 activity raises RASSF8-AS1's level | lines that do not express NTNG2 (19) vs lines expressing it (31) | 3.37× lower at baseline in the lines without NTNG2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FSD1, ANTXR1, RASSF8; co-absent with the target |
| [[LINC01829]] | C | LINC01829 activity raises RASSF8-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 3.66× lower at baseline in the lines without LINC01829 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8C-DT]] | B | RASSF8-AS1 activity raises LRRC8C-DT's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without RASSF8-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[C1QTNF6]] | B | RASSF8-AS1 activity strengthens C1QTNF6's drug response | lines that do not express RASSF8-AS1 (14) vs lines expressing it (34) | the lines without RASSF8-AS1 respond 0.65× as strongly (z diff +1.63); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.33x (z diff +2.8) | 0.030 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; target measured in part of the lines; artifact flags |
| [[CYP1B1-AS1]] | B | RASSF8-AS1 activity raises CYP1B1-AS1's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without RASSF8-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[PPM1L]] | B | RASSF8-AS1 activity raises PPM1L's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.09× lower at baseline in the lines without RASSF8-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | B | RASSF8-AS1 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express RASSF8-AS1 (14) vs lines expressing it (34) | the lines without RASSF8-AS1: 1.28× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[C1QTNF6]] | B | RASSF8-AS1 activity raises C1QTNF6's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.52× lower at baseline in the lines without RASSF8-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[PHLDA2]] | B | RASSF8-AS1 activity lowers PHLDA2's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 2.18× higher at baseline in the lines without RASSF8-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[RXYLT1]] | B | RASSF8-AS1 activity raises RXYLT1's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without RASSF8-AS1 | 0.091 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[PBLD]] | B | RASSF8-AS1 activity raises PBLD's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.24× lower at baseline in the lines without RASSF8-AS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[RASSF8]] | C | RASSF8-AS1 activity raises RASSF8's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 5.98× lower at baseline in the lines without RASSF8-AS1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; co-absent with the target |
| [[NTNG2]] | C | RASSF8-AS1 activity raises NTNG2's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 2.84× lower at baseline in the lines without RASSF8-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804; co-absent with the target |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.1, 12.2); signed map (28.1, 0.9). **Vector** length 78.5, 17.6% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +20.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +9.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +5.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +0.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -7.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RASSF8 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p12.1 — chr12:25,936,683-25,959,765 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48637) · Entrez [100506451](https://www.ncbi.nlm.nih.gov/gene/100506451) · Ensembl [ENSG00000246695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246695)

## Data

Gene col 14470: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14470); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14470, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14470]; `tensor/DDL_lfc|DDL_z.npy` [14470]; `embed/gene_vectors.npy` [14470]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14470 or target_col == 14470). Every well: [[RASSF8-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASSF8-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
