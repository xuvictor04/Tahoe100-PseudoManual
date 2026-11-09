---
symbol: "C2CD4A"
type: "gene"
col: 12610
ensembl_id: "ENSG00000198535"
name: "C2 calcium dependent domain containing 4A"
location: "15q22.2"
module: 155
arm: "+"
pooled_cpm: 2.05
n_lines_expressing: 12
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 39
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# C2CD4A

*C2 calcium dependent domain containing 4A* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.71× (z +11.4, q 4e-27, up in 4 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Pravastatin (sodium) (drug)]] 5 µM: 0.453× (z -4.0, q 0.042, down in 0 of 8 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[S100A8]] (+0.72, fdr 7e-06), [[SERPINB4]] (+0.71, fdr 7e-06), [[S100A9]] (+0.70, fdr 7e-06).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CEACAM5]] → it (grade C ⚠); 39 go from it, the strongest it → [[SRMS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.71×** | +11.4 | 4e-27 | 4/7 (LoVo, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.44×** | +9.2 | 7e-18 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.61×** | +7.9 | 5e-13 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +7.7 | 2e-12 | 3/7 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.19×** | +6.9 | 8e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.71×** | +4.9 | 7e-05 | 1/4 (BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.52×** | +4.6 | 4e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.08×** | +3.8 | 0.011 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.83×** | +3.8 | 0.011 | 4/6 (BT-474, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.5 | 0.022 | 1/8 (CFPAC-1) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.97×** | +3.5 | 0.024 | 0/6 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.4 | 0.034 | 1/6 (LS 180) | top dose only | cell-cycle shift (explains ~10% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.51×** | +3.3 | 0.034 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +3.3 | 0.034 | 0/6 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +3.3 | 0.034 | 0/6 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.88×** | +3.3 | 0.040 | 0/6 | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.29×** | +3.0 | 0.082 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.50×** | +2.9 | 0.096 | 0/8 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.453×** | -4.0 | 0.042 | 0/8 | rises with dose | plate-row cell shift |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.499×** | -3.6 | 0.073 | 1/8 (LS 180) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.518×** | -3.4 | 0.073 | 1/9 (KATO III) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.518×** | -3.4 | 0.073 | 0/8 | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.837× | -3.4 | 0.073 | 4/9 (LoVo, HT-29, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 5 µM |  | 0.329× | -3.0 | 0.20 | 2/8 (NCI-H1573, BT-474) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Decitabine (drug)]] 5 µM |  | 0.547× | -3.0 | 0.20 | 0/6 | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 14.9 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0189× (z -12.4) |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0861× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 35.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.0) |
| [[A-172 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.716 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.649 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.520 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.189 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.267 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.288 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.249 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.259 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.515 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.266 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[S100A8]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB4]] | +0.71 | +0.71 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[S100A9]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[UBE2QL1]] | +0.70 | +0.73 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB3]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC01440]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[ADAM28]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[CES1]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[FGB]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[SPTSSB]] | +0.60 | +0.52 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[TCIM]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LINC01456]] | +0.58 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEACAM5]] | C | CEACAM5 activity raises C2CD4A's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 3.30× lower at baseline in the lines without CEACAM5 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881; co-absent with the target |
| [[LINC01456]] | C | LINC01456 activity raises C2CD4A's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.90× lower at baseline in the lines without LINC01456 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises C2CD4A's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 2.29× lower at baseline in the lines without TMEM45B | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[SMIM31]] | C | SMIM31 activity raises C2CD4A's level | lines that do not express SMIM31 (34) vs lines expressing it (16) | 2.47× lower at baseline in the lines without SMIM31 | 0.008 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises C2CD4A's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 1.89× lower at baseline in the lines without TSPAN1 | 0.034 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[SERPINB3]] | C | SERPINB3 activity raises C2CD4A's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.73× lower at baseline in the lines without SERPINB3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[MMP13]] | C | MMP13 activity raises C2CD4A's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.91× lower at baseline in the lines without MMP13 | 0.081 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4; co-absent with the target |
| [[LRATD1]] | C | LRATD1 activity raises C2CD4A's level | lines that do not express LRATD1 (30) vs lines expressing it (20) | 1.83× lower at baseline in the lines without LRATD1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000259560, NETO1, ENSG00000235495; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 8, C 31. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRMS]] | B | C2CD4A activity raises SRMS's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without C2CD4A | 0.005 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[FRY]] | B | C2CD4A activity raises FRY's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without C2CD4A | 0.015 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[LHFPL5]] | B | C2CD4A activity raises LHFPL5's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.47× lower at baseline in the lines without C2CD4A | 0.032 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[SAMD5]] | B | C2CD4A activity raises SAMD5's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 3.39× lower at baseline in the lines without C2CD4A | 0.038 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[LURAP1]] | B | C2CD4A activity raises LURAP1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.64× lower at baseline in the lines without C2CD4A | 0.052 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[LINC01285]] | B | C2CD4A activity raises LINC01285's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.03× lower at baseline in the lines without C2CD4A | 0.055 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[CEMIP]] | B | C2CD4A activity raises CEMIP's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 4.28× lower at baseline in the lines without C2CD4A | 0.083 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[NELL1]] | B | C2CD4A activity raises NELL1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without C2CD4A | 0.086 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[TMEM45B]] | C | C2CD4A activity raises TMEM45B's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 11.33× lower at baseline in the lines without C2CD4A | 7e-04 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[TSPAN1]] | C | C2CD4A activity raises TSPAN1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 4.21× lower at baseline in the lines without C2CD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[CEACAM5]] | C | C2CD4A activity raises CEACAM5's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 8.98× lower at baseline in the lines without C2CD4A | 0.004 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[LINC01456]] | C | C2CD4A activity raises LINC01456's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 3.20× lower at baseline in the lines without C2CD4A | 0.007 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.1, 48.2); signed map (54.6, 23.6). **Vector** length 37.5, 16.2% of its response variance represented; |z| ≥ 3 in 206 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.64 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.64 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | C2 calcium dependent domain containing 4A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:62,066,977-62,070,917 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NLF1; previously FAM148A |
| Gene groups (HGNC) | C2 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCU7](https://www.uniprot.org/uniprotkb/Q8NCU7) (C2 calcium-dependent domain-containing protein 4A):

> May be involved in inflammatory process. May regulate cell architecture and adhesion.

**Summary**, from NCBI Gene [145741](https://www.ncbi.nlm.nih.gov/gene/145741):

> Involved in positive regulation of acute inflammatory response; regulation of cell adhesion; and regulation of vascular permeability involved in acute inflammatory response. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33627) · Entrez [145741](https://www.ncbi.nlm.nih.gov/gene/145741) · UniProt [Q8NCU7](https://www.uniprot.org/uniprotkb/Q8NCU7) · Ensembl [ENSG00000198535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198535)

## Data

Gene col 12610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12610); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12610]; `tensor/DDL_lfc|DDL_z.npy` [12610]; `embed/gene_vectors.npy` [12610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12610 or target_col == 12610). Every well: [[C2CD4A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C2CD4A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
