---
symbol: "PSG1"
type: "gene"
col: 13823
ensembl_id: "ENSG00000231924"
name: "pregnancy specific beta-1-glycoprotein 1"
location: "19q13.2"
module: 27
arm: "+"
pooled_cpm: 4.14
n_lines_expressing: 5
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 41
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PSG1

*pregnancy specific beta-1-glycoprotein 1* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.22× (z +10.7, q 8e-24, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +4.3, q 0.001, up in 1 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VWA2]] (+0.65, fdr 1e-05), [[APCDD1]] (+0.65, fdr 2e-05), [[ST18]] (+0.65, fdr 4e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[KRT5]] → it (grade C ⚠); 41 go from it, the strongest it → [[ADAMTS19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13823.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.22×** | +10.7 | 8e-24 | 2/2 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.45×** | +10.0 | 3e-21 | 2/3 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.03×** | +9.0 | 4e-17 | 2/2 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.02×** | +5.5 | 5e-06 | 0/3 | top dose only | cell-cycle shift (explains ~1% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.84×** | +4.8 | 2e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.43×** | +4.4 | 1e-03 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.3 | 0.001 | 1/3 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.41×** | +4.2 | 0.002 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.2 | 0.002 | 1/3 (J82) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +4.1 | 0.003 | 1/3 (SNU-423) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.0 | 0.004 | 0/3 | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.41×** | +3.9 | 0.005 | 1/2 (SNU-423) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.04×** | +3.5 | 0.017 | 0/3 | inconsistent across doses | low cells (technical?); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **2.58×** | +3.4 | 0.031 | 2/3 (SW480, SNU-423) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.3 | 0.033 | 1/3 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.033 | 1/3 (SNU-423) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +3.3 | 0.033 | 0/3 | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.92×** | +3.2 | 0.037 | 1/3 (SNU-423) | top dose only |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.84×** | +3.0 | 0.073 | 0/3 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.073 | 3/3 (SNU-423, J82, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.33×** | +3.0 | 0.073 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13823.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.523× | -3.0 | 0.54 | 0/3 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13823. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 84.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.16× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.228 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.269 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.274 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.288 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.267 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.290 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.403 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.270 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.331 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.223 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.264 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.785 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13823), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VWA2]] | +0.65 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[APCDD1]] | +0.65 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ST18]] | +0.65 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[SHISA9]] | +0.64 | +0.69 / +0.36 | both halves | 1e-04 | **novel candidate** |
| [[FGF19]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[JAKMIP2-AS1]] | +0.61 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[F10]] | +0.60 | +0.58 / +0.39 | both halves | 6e-05 |  |
| [[COLGALT2]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[ANO4]] | +0.57 | +0.65 / +0.24 | both halves | 4e-04 | **novel candidate** |
| [[CDK15]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 | **novel candidate** |
| [[SLCO6A1]] | +0.56 | +0.47 / +0.36 | both halves | 1e-04 |  |
| [[SLC30A10]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 0, C 14. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT5]] | C | KRT5 activity raises PSG1's level | lines that do not express KRT5 (46) vs lines expressing it (4) | 1.47× lower at baseline in the lines without KRT5 | 0.001 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: APOB, BMP10, TBXT; co-absent with the target |
| [[JAKMIP2-AS1]] | C | JAKMIP2-AS1 activity raises PSG1's level | lines that do not express JAKMIP2-AS1 (38) vs lines expressing it (12) | 1.07× lower at baseline in the lines without JAKMIP2-AS1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[SLC25A24P1]] | C | SLC25A24P1 activity raises PSG1's level | lines that do not express SLC25A24P1 (40) vs lines expressing it (10) | 1.71× lower at baseline in the lines without SLC25A24P1 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC01425, ENSG00000275016, MAGEB2; co-absent with the target |
| [[PCSK1]] | C | PCSK1 activity raises PSG1's level | lines that do not express PCSK1 (40) vs lines expressing it (10) | 1.08× lower at baseline in the lines without PCSK1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, CALCA, GSG1L2; co-absent with the target |
| [[LINC00491]] | C | LINC00491 activity raises PSG1's level | lines that do not express LINC00491 (33) vs lines expressing it (17) | 1.89× lower at baseline in the lines without LINC00491 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APCDD1L, LINC01905, ADGRG7; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity lowers PSG1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 1.03× higher at baseline in the lines without CSMD3 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[GABRG2]] | C | GABRG2 activity lowers PSG1's level | lines that do not express GABRG2 (36) vs lines expressing it (14) | 1.02× higher at baseline in the lines without GABRG2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000287211, PCSK1, BAGE2; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity lowers PSG1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.12× higher at baseline in the lines without FKBP9P1-1 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[TGFBI]] | C | TGFBI activity raises PSG1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without TGFBI | 0.074 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949; co-absent with the target |
| [[FGF20]] | C | FGF20 activity raises PSG1's level | lines that do not express FGF20 (41) vs lines expressing it (9) | 1.08× lower at baseline in the lines without FGF20 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, HEPHL1, GCG; co-absent with the target |
| [[FGF19]] | C | FGF19 activity raises PSG1's level | lines that do not express FGF19 (42) vs lines expressing it (8) | 1.07× lower at baseline in the lines without FGF19 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, SFTPA2, KRT5; co-absent with the target |
| [[FGD5]] | C | FGD5 activity lowers PSG1's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 1.04× higher at baseline in the lines without FGD5 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5; co-absent with the target |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 7, C 34. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS19]] | B | PSG1 activity raises ADAMTS19's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.15× lower at baseline in the lines without PSG1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[DKK2]] | B | PSG1 activity raises DKK2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.01× lower at baseline in the lines without PSG1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[LINC02254]] | B | PSG1 activity raises LINC02254's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 1.91× lower at baseline in the lines without PSG1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[LINC03042]] | B | PSG1 activity raises LINC03042's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.21× lower at baseline in the lines without PSG1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[LINC02842]] | B | PSG1 activity raises LINC02842's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 1.83× lower at baseline in the lines without PSG1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[LINC02466]] | B | PSG1 activity raises LINC02466's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.60× lower at baseline in the lines without PSG1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[FKBP9P1]] | B | PSG1 activity raises FKBP9P1's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 1.41× lower at baseline in the lines without PSG1 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB |
| [[JAKMIP2-AS1]] | C | PSG1 activity raises JAKMIP2-AS1's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 4.33× lower at baseline in the lines without PSG1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[KRT5]] | C | PSG1 activity raises KRT5's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.32× lower at baseline in the lines without PSG1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[SHISA9]] | C | PSG1 activity raises SHISA9's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 4.22× lower at baseline in the lines without PSG1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[FGF19]] | C | PSG1 activity raises FGF19's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 3.07× lower at baseline in the lines without PSG1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |
| [[VWA2]] | C | PSG1 activity raises VWA2's level | lines that do not express PSG1 (45) vs lines expressing it (5) | 2.45× lower at baseline in the lines without PSG1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, KRT5, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.1, 42.8); signed map (63.6, 16.5). **Vector** length 16.3, 7.59% of its response variance represented; |z| ≥ 3 in 83 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.6 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +0.8 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.4 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.4 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.4 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | +0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.4 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.4 | +0.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.4 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | pregnancy specific beta-1-glycoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:42,866,464-42,879,822 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSGGA, CD66f, PBG1; previously PSBG1 |
| Gene groups (HGNC) | CD molecules; V-set domain containing; Pregnancy specific glycoproteins |
| Reactome | 2 pathways, smallest: Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

UniProt [P11464](https://www.uniprot.org/uniprotkb/P11464) carries no function annotation.

**Summary**, from NCBI Gene [5669](https://www.ncbi.nlm.nih.gov/gene/5669):

> The human placenta is a multihormonal endocrine organ that produces hormones, enzymes, and other molecules that support fetal survival and development. Pregnancy-specific beta-1-glycoprotein (PSBG, PSG) is a major product of the syncytiotrophoblast, reaching concentrations of 100 to 290 mg/l at term in the serum of pregnant women (Horne et al., 1976 [PubMed 971765]). PSG is a member of the immunoglobulin (Ig) superfamily (Watanabe and Chou, 1988 [PubMed 3257488]; Streydio et al., 1988 [PubMed …

**Accessions** — [HGNC:9514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9514) · Entrez [5669](https://www.ncbi.nlm.nih.gov/gene/5669) · UniProt [P11464](https://www.uniprot.org/uniprotkb/P11464) · Ensembl [ENSG00000231924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231924)

## Data

Gene col 13823: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13823); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13823, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13823]; `tensor/DDL_lfc|DDL_z.npy` [13823]; `embed/gene_vectors.npy` [13823]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13823 or target_col == 13823). Every well: [[PSG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
