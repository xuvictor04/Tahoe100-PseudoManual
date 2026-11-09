---
symbol: "IDO1"
type: "gene"
col: 5186
ensembl_id: "ENSG00000131203"
name: "indoleamine 2,3-dioxygenase 1"
location: "8p11.21"
module: 70
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 22
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 31
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# IDO1

*indoleamine 2,3-dioxygenase 1* — 8p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.82× (z +10.4, q 1e-22, up in 8 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.0472×, NCI-H1792 0.148×, NCI-H2347 0.0890×); [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0151×, NCI-H1792 0.0274×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0435×, NCI-H1792 0.0544×; ⚠ cell-cycle shift, explains ~59% of this change); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.0689×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP4]] (+0.80, fdr 7e-06), [[APOL3]] (+0.77, fdr 7e-06), [[CFB]] (+0.77, fdr 7e-06); moves opposite to [[ERGIC1]] (-0.58, fdr 3e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 31 go from it, the strongest it → [[CTSS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +10.4 | 1e-22 | 8/13 (CFPAC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.15×** | +9.6 | 2e-19 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.93×** | +7.5 | 9e-12 | 1/6 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.37×** | +7.5 | 9e-12 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.50×** | +5.0 | 5e-05 | 11/16 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +4.9 | 8e-05 | 1/7 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.49×** | +4.8 | 1e-04 | 10/10 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.36×** | +4.7 | 2e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.6 | 2e-04 | 8/18 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.95×** | +4.3 | 8e-04 | 13/18 (CFPAC-1, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.67×** | +3.8 | 0.006 | 2/5 (HS-578T, NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.61×** | +3.8 | 0.008 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.93×** | +3.6 | 0.014 | 8/17 (CFPAC-1, HS-578T, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.6 | 0.014 | 0/10 | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +3.4 | 0.021 | 1/8 (HS-578T) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +3.4 | 0.021 | 2/17 (HOP62, J82) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +3.3 | 0.028 | 4/13 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.031 | 1/17 (HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +3.2 | 0.038 | 1/10 (NCI-H1792) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.048 | 8/18 (CFPAC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.21×** | +3.1 | 0.048 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +3.0 | 0.057 | 9/18 (CFPAC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.49×** | +3.0 | 0.062 | 5/17 (CFPAC-1, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (HS-578T 0.0472×, NCI-H1792 0.148×, NCI-H2347 0.0890×); [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0151×, NCI-H1792 0.0274×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HS-578T 0.0435×, NCI-H1792 0.0544×; ⚠ cell-cycle shift, explains ~59% of this change); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM in 1 line (HS-578T 0.0689×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.539× | -3.5 | 0.28 | 11/16 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.555× | -3.3 | 0.28 | 8/17 (H4, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 32.5 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0472× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0274× (z -11.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.148× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0890× (z -8.5) |
| [[A-172 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.182 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.714 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.600 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.799 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.552 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.233 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.280 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.235 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.234 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP4]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 633 |
| [[APOL3]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CFB]] | +0.77 | +0.65 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[EPSTI1]] | +0.72 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CTSS]] | +0.72 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[GBP1]] | +0.71 | +0.59 / +0.73 | both halves | 7e-06 | STRING 661 |
| [[SAMD9L]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[APOL1]] | +0.71 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TMEM140]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[PSMB10]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[TRANK1]] | +0.69 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 8, C 13. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IDO1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TRIM22]] | B | TRIM22 activity raises IDO1's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without TRIM22 | 0.034 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFITM1]] | B | IFITM1 activity raises IDO1's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without IFITM1 | 0.039 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[TLR3]] | B | TLR3 activity raises IDO1's level | lines that do not express TLR3 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without TLR3 | 0.071 | ⚠ within organs, on part of the lines; also absent: LGALS3, GBP4, RAB27B; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises IDO1's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.75× lower at baseline in the lines without EPSTI1 | 0.072 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CASP10]] | B | CASP10 activity raises IDO1's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without CASP10 | 0.087 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[PLAAT4]] | B | PLAAT4 activity raises IDO1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without PLAAT4 | 0.093 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[BST2]] | B | BST2 activity raises IDO1's level | lines that do not express BST2 (18) vs lines expressing it (32) | 1.82× lower at baseline in the lines without BST2 | 0.099 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[CD74]] | C | CD74 activity raises IDO1's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.47× lower at baseline in the lines without CD74 | 0.013 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises IDO1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.72× lower at baseline in the lines without TNFAIP6 | 0.020 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[FYB1]] | C | FYB1 activity raises IDO1's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.24× lower at baseline in the lines without FYB1 | 0.021 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450; co-absent with the target |
| [[APOL1]] | C | APOL1 activity raises IDO1's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without APOL1 | 0.028 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 17, C 14. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | IDO1 activity raises CTSS's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.53× lower at baseline in the lines without IDO1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[TRIM22]] | B | IDO1 activity raises TRIM22's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 3.70× lower at baseline in the lines without IDO1 | 0.013 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[GBP1]] | B | IDO1 activity raises GBP1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 3.64× lower at baseline in the lines without IDO1 | 0.019 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[IFITM1]] | B | IDO1 activity raises IFITM1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without IDO1 | 0.021 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[GBP2]] | B | IDO1 activity raises GBP2's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 3.27× lower at baseline in the lines without IDO1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[FBXO39]] | B | IDO1 activity raises FBXO39's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without IDO1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[MX2]] | B | IDO1 activity raises MX2's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.42× lower at baseline in the lines without IDO1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[B2M]] | B | IDO1 activity raises B2M's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without IDO1 | 0.046 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[SAMD9L]] | B | IDO1 activity raises SAMD9L's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without IDO1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[XAF1]] | B | IDO1 activity raises XAF1's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without IDO1 | 0.054 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[PLAAT4]] | B | IDO1 activity raises PLAAT4's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without IDO1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[TNFSF10]] | B | IDO1 activity raises TNFSF10's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without IDO1 | 0.063 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 51.2); signed map (60.7, 29.3). **Vector** length 51.1, 14.8% of its response variance represented; |z| ≥ 3 in 501 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.55 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.61 to 14); *Interferon gamma signaling* (reactome, mean cos +0.62 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.2 | +3.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.9 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | indoleamine 2,3-dioxygenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.21 — chr8:39,902,275-39,928,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously IDO, INDO |
| Gene groups (HGNC) | Indoleamine 2,3-dioxygenase family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P14902](https://www.uniprot.org/uniprotkb/P14902) (Indoleamine 2,3-dioxygenase 1):

> Catalyzes the first and rate limiting step of the catabolism of the essential amino acid tryptophan along the kynurenine pathway. Involved in the peripheral immune tolerance, contributing to maintain homeostasis by preventing autoimmunity or immunopathology that would result from uncontrolled and overreacting immune responses. Tryptophan shortage inhibits T lymphocytes division and accumulation of tryptophan catabolites induces T-cell apoptosis and differentiation of regulatory T-cells. Acts as …

**Summary**, from NCBI Gene [3620](https://www.ncbi.nlm.nih.gov/gene/3620):

> This gene encodes indoleamine 2,3-dioxygenase (IDO) - a heme enzyme that catalyzes the first and rate-limiting step in tryptophan catabolism to N-formyl-kynurenine. This enzyme acts on multiple tryptophan substrates including D-tryptophan, L-tryptophan, 5-hydroxy-tryptophan, tryptamine, and serotonin. This enzyme is thought to play a role in a variety of pathophysiological processes such as antimicrobial and antitumor defense, neuropathology, immunoregulation, and antioxidant activity. Through …

**Accessions** — [HGNC:6059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6059) · Entrez [3620](https://www.ncbi.nlm.nih.gov/gene/3620) · UniProt [P14902](https://www.uniprot.org/uniprotkb/P14902) · Ensembl [ENSG00000131203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131203)

## Data

Gene col 5186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5186); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5186]; `tensor/DDL_lfc|DDL_z.npy` [5186]; `embed/gene_vectors.npy` [5186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5186 or target_col == 5186). Every well: [[IDO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IDO1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
