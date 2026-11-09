---
symbol: "CSMD2"
type: "gene"
col: 4306
ensembl_id: "ENSG00000121904"
name: "CUB and Sushi multiple domains 2"
location: "1p35.1"
module: 13
arm: "+"
pooled_cpm: 9.18
n_lines_expressing: 18
n_dd_up: 25
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 19
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CSMD2

*CUB and Sushi multiple domains 2* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.55× (z +26.5, q 0e+00, up in 9 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.627× (z -5.1, q 2e-04, down in 9 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMNAT2]] (+0.71, fdr 7e-06), [[PTHLH]] (+0.66, fdr 7e-06), [[IQCJ-SCHIP1]] (+0.65, fdr 1e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 19 go from it, the strongest it → [[NMNAT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4306.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.55×** | +26.5 | 0e+00 | 9/15 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.85×** | +14.2 | 4e-43 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +13.3 | 6e-38 | 11/16 (A-427, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.27×** | +12.9 | 4e-36 | 2/10 (HS-578T, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +9.3 | 1e-18 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +8.7 | 4e-16 | 5/16 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +8.5 | 1e-15 | 1/13 (BT-474) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +7.9 | 2e-13 | 11/16 (HOP62, NCI-H23, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +7.4 | 7e-12 | 7/14 (SW480, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +6.7 | 1e-09 | 10/16 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.2 | 8e-06 | 0/11 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.1 | 2e-05 | 4/15 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.8 | 8e-05 | 12/16 (A-427, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 3e-04 | 1/16 (HS-578T) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.001 | 8/15 (NCI-H23, BT-474, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Hydroxyurea (drug)]] 0.05 µM |  | **1.43×** | +3.6 | 0.010 | 2/12 (H4, RPMI-7951) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.85×** | +3.5 | 0.014 | 2/9 (A-172, SW480) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.014 | 6/16 (A-172, RPMI-7951, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.025 | 3/14 (BT-474, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4306.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.627×** | -5.1 | 2e-04 | 9/16 (RPMI-7951, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.661×** | -4.5 | 0.002 | 5/16 (Hs 766T, HOP62, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.706×** | -3.6 | 0.050 | 5/16 (A-172, SNU-423, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.752×** | -3.5 | 0.053 | 5/16 (HOP62, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.726×** | -3.5 | 0.053 | 8/16 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.730×** | -3.4 | 0.055 | 7/16 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.715×** | -3.4 | 0.057 | 3/16 (Hs 766T, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4306. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.8 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.214× (z -11.0) ⚠ cell-cycle shift, explains ~66% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -8.5) |
| [[Hs 766T (line)]] | wt | 186 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 91.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.121× (z -10.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 6.85 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.67× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.203× (z -9.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.502× (z -10.3) ⚠ position not correctable |
| [[NCI-H23 (line)]] | alt | 4.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.60× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.293× (z -8.9) ⚠ cell-cycle shift, explains ~66% of this change |
| [[SW 900 (line)]] | alt | 3.90 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.05 µM 0.0453× (z -8.6) |
| [[SW480 (line)]] | alt | 3.60 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.43× (z +9.6) | — |
| [[A498 (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4306), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMNAT2]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[PTHLH]] | +0.66 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[IQCJ-SCHIP1]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[PODXL]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[IL11]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[SAMD3]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.63 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[VAT1L]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[NES]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.63 | +0.43 / +0.66 | both halves | 3e-05 |  |
| [[LRRC8C]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[RBFOX1]] | +0.63 | +0.56 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 2, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CSMD2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises CSMD2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LINC02813]] | C | LINC02813 activity raises CSMD2's level | lines that do not express LINC02813 (26) vs lines expressing it (24) | 2.70× lower at baseline in the lines without LINC02813 | 0.038 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, ENSG00000260517, CUBN; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises CSMD2's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without COL5A1 | 0.041 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[TENM4]] | C | TENM4 activity raises CSMD2's level | lines that do not express TENM4 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without TENM4 | 0.042 | ⚠ within organs, on part of the lines; also absent: APCDD1L-DT, LINC02930, PXDN; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises CSMD2's level | lines that do not express HHIP (33) vs lines expressing it (17) | 2.86× lower at baseline in the lines without HHIP | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |
| [[SIGLEC15]] | C | SIGLEC15 activity raises CSMD2's level | lines that do not express SIGLEC15 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without SIGLEC15 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC01615, ZNF257, NLRP1; co-absent with the target |
| [[APCDD1L-DT]] | C | APCDD1L-DT activity raises CSMD2's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without APCDD1L-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent; co-absent with the target |
| [[ZNF385D]] | C | ZNF385D activity raises CSMD2's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 2.45× lower at baseline in the lines without ZNF385D | 0.091 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 7, C 12. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMNAT2]] | B | CSMD2 activity raises NMNAT2's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.50× lower at baseline in the lines without CSMD2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[CNIH3]] | B | CSMD2 activity raises CNIH3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without CSMD2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[RAC2]] | B | CSMD2 activity raises RAC2's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without CSMD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[MANCR]] | B | CSMD2 activity raises MANCR's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.67× lower at baseline in the lines without CSMD2 | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[KCNN3]] | B | CSMD2 activity raises KCNN3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without CSMD2 | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[RASA3]] | B | CSMD2 activity raises RASA3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 1.43× lower at baseline in the lines without CSMD2 | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[PDE4DIPP2]] | B | CSMD2 activity raises PDE4DIPP2's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.08× lower at baseline in the lines without CSMD2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent |
| [[VAT1L]] | C | CSMD2 activity raises VAT1L's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 2.98× lower at baseline in the lines without CSMD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[DKK3]] | C | CSMD2 activity raises DKK3's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 3.76× lower at baseline in the lines without CSMD2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[COL5A1]] | C | CSMD2 activity raises COL5A1's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 4.87× lower at baseline in the lines without CSMD2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[LINC02813]] | C | CSMD2 activity raises LINC02813's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 1.92× lower at baseline in the lines without CSMD2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |
| [[RFX8]] | C | CSMD2 activity raises RFX8's level | lines that do not express CSMD2 (32) vs lines expressing it (18) | 3.72× lower at baseline in the lines without CSMD2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ZNF667, ZNF667-AS1, SOX11; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.7, 11.7); signed map (17.8, 49.0). **Vector** length 49.8, 12.7% of its response variance represented; |z| ≥ 3 in 518 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +26.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.2 | +3.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -1.7 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CUB and Sushi multiple domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,513,998-34,165,842 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1884 |
| Gene groups (HGNC) | Sushi domain containing; Complement system regulators and receptors |
| Matched by | ensembl_id |

UniProt [Q7Z408](https://www.uniprot.org/uniprotkb/Q7Z408) carries no function annotation.

**Summary**, from NCBI Gene [114784](https://www.ncbi.nlm.nih.gov/gene/114784):

> The protein encoded by this gene is thought to be involved in the control of complement cascade of the immune system. Defects in this gene have been associated with schizophrenia. This gene may act as a tumor suppressor for colorectal cancer. [provided by RefSeq, Jan 2020]

**Accessions** — [HGNC:19290](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19290) · Entrez [114784](https://www.ncbi.nlm.nih.gov/gene/114784) · UniProt [Q7Z408](https://www.uniprot.org/uniprotkb/Q7Z408) · Ensembl [ENSG00000121904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121904)

## Data

Gene col 4306: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4306); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4306, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4306]; `tensor/DDL_lfc|DDL_z.npy` [4306]; `embed/gene_vectors.npy` [4306]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4306 or target_col == 4306). Every well: [[CSMD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSMD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
