---
symbol: "OVOL1"
type: "gene"
col: 10300
ensembl_id: "ENSG00000172818"
name: "ovo like transcriptional repressor 1"
location: "11q13.1"
module: 4
arm: "-"
pooled_cpm: 4.29
n_lines_expressing: 17
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 48
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# OVOL1

*ovo like transcriptional repressor 1* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.45× (z +18.6, q 0e+00, up in 14 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.580× (z -3.9, q 0.059, down in 2 of 15 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.1000×, NCI-H2347 0.198×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0781×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNK1]] (+0.64, fdr 1e-05), [[PDLIM2]] (+0.59, fdr 1e-05), [[EPOR]] (+0.57, fdr 9e-06); moves opposite to [[OPA1]] (-0.57, fdr 3e-05), [[CHCHD3]] (-0.57, fdr 2e-05), [[MRPL42]] (-0.53, fdr 4e-05).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RNF220]] → it (grade B ⚠); 48 go from it, the strongest it → [[TNK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10300.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.45×** | +18.6 | 0e+00 | 14/15 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.95×** | +13.7 | 4e-40 | 12/15 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.50×** | +10.2 | 4e-22 | 1/4 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +8.5 | 2e-15 | 2/11 (NCI-H1573, SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +7.5 | 7e-12 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.0 | 2e-10 | 8/14 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.68×** | +6.9 | 3e-10 | 10/15 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.23×** | +5.6 | 1e-06 | 4/13 (BT-474, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.17×** | +5.2 | 1e-05 | 5/13 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.71×** | +4.9 | 5e-05 | 0/12 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.7 | 2e-04 | 1/14 (CFPAC-1) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.97×** | +4.6 | 2e-04 | 11/15 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.4 | 5e-04 | 4/13 (LoVo, SW1417, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.84×** | +4.3 | 7e-04 | 10/15 (BT-474, LoVo, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.31×** | +4.1 | 0.001 | 2/12 (KATO III, HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.0 | 0.002 | 2/14 (Panc 03.27, SW1417) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.25×** | +4.0 | 0.002 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.79×** | +3.8 | 0.005 | 4/13 (SW1417, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.005 | 1/15 (LS 180) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.032 | 4/14 (SW1417, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +3.2 | 0.037 | 5/14 (LS 180, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.56×** | +3.1 | 0.050 | 3/15 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.064 | 4/14 (LS 180, CFPAC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.53×** | +3.0 | 0.064 | 11/15 (LS 180, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10300.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.1000×, NCI-H2347 0.198×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0781×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.580×** | -3.9 | 0.059 | 2/15 (NCI-H1573, SW48) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.643× | -3.0 | 0.54 | 1/15 (COLO 205) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10300. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 19.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.98× (z +10.2) | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 21.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0781× (z -14.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 7.90 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +9.2) | — |
| [[KATO III (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +10.8) | — |
| [[LS 180 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -13.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.80× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +10.0) | — |
| [[A-172 (line)]] | wt | 0.297 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.262 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.230 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.345 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.327 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.302 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.406 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.250 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.240 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.362 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.574 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.286 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.90 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.428 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10300), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNK1]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PDLIM2]] | +0.59 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[EPOR]] | +0.57 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[BOLA1]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[ARL14]] | +0.53 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[TOB2]] | +0.52 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CITED2]] | +0.52 | +0.40 / +0.53 | both halves | 5e-05 |  |
| [[MSX2]] | +0.52 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[DLK2]] | +0.51 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MAD2L1BP]] | +0.50 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[SERTAD1]] | +0.50 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ERF]] | +0.50 | +0.46 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OPA1]] | -0.57 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[CHCHD3]] | -0.57 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[VPS50]] | -0.51 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NOL10]] | -0.51 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[UBAC2]] | -0.51 | -0.36 / -0.51 | both halves | 9e-05 |  |
| [[COA1]] | -0.50 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[HERC2]] | -0.50 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[ERI3]] | -0.48 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[MRPS27]] | -0.47 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[USP14]] | -0.47 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[MGMT]] | -0.46 | -0.38 / -0.40 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF220]] | B | RNF220 activity lowers OVOL1's level | lines that do not express RNF220 (9) vs lines expressing it (41) | 2.56× higher at baseline in the lines without RNF220 | 0.050 | ⚠ within organs, on part of the lines; also absent: GNAZ, ENSG00000287400, CTXN1; maybe low, not absent |
| [[RND1]] | B | RND1 activity raises OVOL1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 2.47× lower at baseline in the lines without RND1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[RNF223]] | C | RNF223 activity raises OVOL1's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 5.00× lower at baseline in the lines without RNF223 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2; co-absent with the target |
| [[ARL14]] | C | ARL14 activity raises OVOL1's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 2.71× lower at baseline in the lines without ARL14 | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent; co-absent with the target |
| [[HCP5]] | C | HCP5 activity raises OVOL1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without HCP5 | 0.0995 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 45, C 3. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNK1]] | B | OVOL1 activity raises TNK1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without OVOL1 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TRPV3]] | B | OVOL1 activity raises TRPV3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.95× lower at baseline in the lines without OVOL1 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[GCH1]] | B | OVOL1 activity weakens GCH1's drug response | lines that do not express OVOL1 (31) vs lines expressing it (15) | the lines without OVOL1 respond 1.11× as strongly (z diff -0.86); strongest at Tucidinostat 5 µM: 2.48x vs 1.46x (z diff -3.5) | 0.006 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; target measured in part of the lines; artifact flags |
| [[RND1]] | B | OVOL1 activity raises RND1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without OVOL1 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[ERI3]] | B | OVOL1 activity lowers ERI3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.49× higher at baseline in the lines without OVOL1 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CHCHD3]] | B | OVOL1 activity lowers CHCHD3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.23× higher at baseline in the lines without OVOL1 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| cells under [[Apalutamide (drug)]] 0.5 µM | B | OVOL1, [[TMPRSS4]] activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.29× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| cells under [[Mifepristone (drug)]] 0.5 µM | B | OVOL1, [[TMPRSS4]] activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | OVOL1, [[TMPRSS4]] activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | OVOL1, [[TMPRSS4]] activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[RNF220]] | B | OVOL1 activity lowers RNF220's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.15× higher at baseline in the lines without OVOL1 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[NUP155]] | B | OVOL1 activity lowers NUP155's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.42× higher at baseline in the lines without OVOL1 | 0.028 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (28.8, -34.6); signed map (-0.6, 12.4). **Vector** length 40.3, 10.9% of its response variance represented; |z| ≥ 3 in 270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +13.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | +1.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.6 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +4.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | +0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ovo like transcriptional repressor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,787,063-65,797,214 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HOVO1 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SNAG transcriptional repressors |
| Matched by | ensembl_id |

**Function**, from UniProt [O14753](https://www.uniprot.org/uniprotkb/O14753) (Putative transcription factor Ovo-like 1):

> Putative transcription factor. Involved in hair formation and spermatogenesis. May function in the differentiation and/or maintenance of the urogenital system (By similarity).

**Summary**, from NCBI Gene [5017](https://www.ncbi.nlm.nih.gov/gene/5017):

> This gene encodes a putative zinc finger containing transcription factor that is highly similar to homologous protein in Drosophila and mouse. Based on known functions in these species, this protein is likely involved in hair formation and spermatogenesis in human as well. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:8525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8525) · Entrez [5017](https://www.ncbi.nlm.nih.gov/gene/5017) · UniProt [O14753](https://www.uniprot.org/uniprotkb/O14753) · Ensembl [ENSG00000172818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172818)

## Data

Gene col 10300: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10300); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10300, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10300]; `tensor/DDL_lfc|DDL_z.npy` [10300]; `embed/gene_vectors.npy` [10300]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10300 or target_col == 10300). Every well: [[OVOL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OVOL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
