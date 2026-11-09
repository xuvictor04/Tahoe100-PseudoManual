---
symbol: "LMO2"
type: "gene"
col: 5690
ensembl_id: "ENSG00000135363"
name: "LIM domain only 2"
location: "11p13"
module: 32
arm: "+"
pooled_cpm: 2.57
n_lines_expressing: 26
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 29
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LMO2

*LIM domain only 2* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.57× (z +16.7, q 0e+00, up in 10 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.434× (z -5.8, q 5e-06, down in 16 of 22 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOBEC3G]] (+0.63, fdr 7e-06), [[MX2]] (+0.59, fdr 3e-05), [[BST2]] (+0.58, fdr 4e-05).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MX2]] → it (grade B ⚠); 29 go from it, the strongest it → [[TRIM22]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5690.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.57×** | +16.7 | 0e+00 | 10/14 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.81×** | +8.9 | 2e-16 | 1/3 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +6.7 | 4e-09 | 2/6 (SW480, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.39×** | +5.6 | 4e-06 | 1/4 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +4.2 | 0.003 | 1/13 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +4.2 | 0.003 | 0/5 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.38×** | +4.0 | 0.005 | 2/10 (Hs 766T, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.0 | 0.005 | 3/17 (J82, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.0 | 0.005 | 0/10 | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.9 | 0.005 | 1/7 (LoVo) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.27×** | +3.8 | 0.007 | 3/8 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.17×** | +3.6 | 0.016 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.71×** | +3.5 | 0.017 | 3/11 (SW480, A-172, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.061 | 4/18 (Hs 766T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.62×** | +3.2 | 0.061 | 2/16 (SW1417, A-172) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.096 | 4/21 (HEC-1-A, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5690.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.434×** | -5.8 | 5e-06 | 16/22 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.482×** | -5.0 | 1e-04 | 14/21 (Panc 03.27, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.545×** | -4.2 | 0.005 | 13/19 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5690. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 33.9 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -15.9) |
| [[HS-578T (line)]] | alt | 9.64 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.0179× (z -16.7) |
| [[SW480 (line)]] | alt | 5.43 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -12.2) |
| [[Hs 766T (line)]] | wt | 16.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.115× (z -11.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.144× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 3.55 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0421× (z -9.1) |
| [[A-427 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.714 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.313 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.784 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.304 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.581 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.726 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.595 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.687 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.244 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5690), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOBEC3G]] | +0.63 | +0.59 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[MX2]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[BST2]] | +0.58 | +0.41 / +0.68 | both halves | 4e-05 |  |
| [[TEK]] | +0.58 | +0.58 / +0.47 | both halves | 2e-05 | **novel candidate** |
| [[RSAD2]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[IFI27]] | +0.57 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[TDRD7]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[OASL]] | +0.55 | +0.34 / +0.67 | both halves | 1e-04 |  |
| [[TNFSF10]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ISG15]] | +0.53 | +0.29 / +0.65 | both halves | 2e-04 |  |
| [[IFIT3]] | +0.53 | +0.36 / +0.61 | both halves | 1e-04 |  |
| [[XAF1]] | +0.53 | +0.37 / +0.55 | both halves | 8e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX2]] | B | MX2 activity raises LMO2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.74× lower at baseline in the lines without MX2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[MDGA1]] | B | MDGA1 activity raises LMO2's level | lines that do not express MDGA1 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without MDGA1 | 0.079 | ⚠ within organs, on part of the lines; also absent: TCF7L1, ZNF470, FBXL2 |
| [[ADAMTS14]] | C | ADAMTS14 activity raises LMO2's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 1.98× lower at baseline in the lines without ADAMTS14 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises LMO2's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without GBP5 | 0.069 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 27, C 2. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM22]] | B | LMO2 activity strengthens TRIM22's drug response | lines that do not express LMO2 (11) vs lines expressing it (19) | the lines without LMO2 respond 0.62× as strongly (z diff +2.33); strongest at Tofacitinib 0.5 µM: 0.48x vs 0.19x (z diff +3.8) | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent; target measured in part of the lines |
| [[UBE2L6]] | B | LMO2 activity strengthens UBE2L6's drug response | lines that do not express LMO2 (22) vs lines expressing it (20) | the lines without LMO2 respond 0.50× as strongly (z diff +2.24); strongest at Panobinostat 5 µM: 0.58x vs 0.30x (z diff +4.4) | 0.006 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IFIT3]] | B | LMO2 activity raises IFIT3's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.64× lower at baseline in the lines without LMO2 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[TRIM22]] | B | LMO2 activity raises TRIM22's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 3.47× lower at baseline in the lines without LMO2 | 0.007 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[IFIT1]] | B | LMO2 activity raises IFIT1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without LMO2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[IFIT2]] | B | LMO2 activity raises IFIT2's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.74× lower at baseline in the lines without LMO2 | 0.017 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[PSMB9]] | B | LMO2 activity raises PSMB9's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without LMO2 | 0.019 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[ZNFX1]] | B | LMO2 activity raises ZNFX1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.51× lower at baseline in the lines without LMO2 | 0.022 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[SAMHD1]] | B | LMO2 activity raises SAMHD1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.86× lower at baseline in the lines without LMO2 | 0.032 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[IFIH1]] | B | LMO2 activity raises IFIH1's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without LMO2 | 0.038 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[TDRD7]] | B | LMO2 activity raises TDRD7's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 1.61× lower at baseline in the lines without LMO2 | 0.044 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |
| [[RSAD2]] | B | LMO2 activity raises RSAD2's level | lines that do not express LMO2 (24) vs lines expressing it (26) | 2.49× lower at baseline in the lines without LMO2 | 0.045 | ⚠ within organs, on part of the lines; also absent: TNFSF10, SAA1, SAA4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.515). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.9, 52.1); signed map (67.0, 29.5). **Vector** length 41.2, 8.27% of its response variance represented; |z| ≥ 3 in 535 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.3 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.5 | -4.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.4 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.2 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain only 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:33,858,576-33,892,076 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TTG2, RHOM2, RBTN2; previously RBTNL1 |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | PANCREAS_BETA_CELLS, HEME_METABOLISM |
| Reactome | 2 pathways, smallest: RUNX1 regulates transcription of genes involved in differentiation of HSCs; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P25791](https://www.uniprot.org/uniprotkb/P25791) (Rhombotin-2):

> Acts with TAL1/SCL to regulate red blood cell development. Also acts with LDB1 to maintain erythroid precursors in an immature state.

**Summary**, from NCBI Gene [4005](https://www.ncbi.nlm.nih.gov/gene/4005):

> LMO2 encodes a cysteine-rich, two LIM-domain protein that is required for yolk sac erythropoiesis. The LMO2 protein has a central and crucial role in hematopoietic development and is highly conserved. The LMO2 transcription start site is located approximately 25 kb downstream from the 11p13 T-cell translocation cluster (11p13 ttc), where a number T-cell acute lymphoblastic leukemia-specific translocations occur. Alternative splicing results in multiple transcript variants encoding different …

**Accessions** — [HGNC:6642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6642) · Entrez [4005](https://www.ncbi.nlm.nih.gov/gene/4005) · UniProt [P25791](https://www.uniprot.org/uniprotkb/P25791) · Ensembl [ENSG00000135363](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135363)

## Data

Gene col 5690: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5690); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5690, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5690]; `tensor/DDL_lfc|DDL_z.npy` [5690]; `embed/gene_vectors.npy` [5690]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5690 or target_col == 5690). Every well: [[LMO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
