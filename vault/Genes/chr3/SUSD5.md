---
symbol: "SUSD5"
type: "gene"
col: 10420
ensembl_id: "ENSG00000173705"
name: "sushi domain containing 5"
location: "3p22.3"
module: 66
arm: "+"
pooled_cpm: 4.17
n_lines_expressing: 27
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# SUSD5

*sushi domain containing 5* — 3p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.86× (z +15.8, q 0e+00, up in 12 of 14 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +10.7, q 1e-24, up in 5 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.142×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALNT1]] (+0.63, fdr 1e-05), [[ANGPT1]] (+0.61, fdr 1e-05), [[MATN3]] (+0.60, fdr 9e-05); moves opposite to [[CIB1]] (-0.54, fdr 1e-04), [[CIAO2B]] (-0.51, fdr 2e-04), [[GSDMB]] (-0.48, fdr 1e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BEND6]] → it (grade C ⚠); 5 go from it, the strongest it → [[PDIA3P1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10420.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.86×** | +15.8 | 0e+00 | 12/14 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.65×** | +14.7 | 0e+00 | 7/9 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.58×** | +11.8 | 1e-29 | 6/10 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.7 | 1e-24 | 5/17 (NCI-H2347, HS-578T, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +7.8 | 6e-13 | 17/24 (J82, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +7.1 | 8e-11 | 6/21 (NCI-H2030, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +6.3 | 3e-08 | 7/23 (A-427, NCI-H1573, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +5.1 | 2e-05 | 4/13 (A-427, SNU-423, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.60×** | +5.0 | 4e-05 | 4/21 (NCI-H2030, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +5.0 | 4e-05 | 4/23 (SNU-423, A-172, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +4.5 | 3e-04 | 4/21 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 6/22 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 3e-04 | 0/22 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.3 | 7e-04 | 3/17 (SW 900, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.79×** | +4.1 | 0.001 | 1/8 (A-427) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.45×** | +3.5 | 0.016 | 1/23 (C-33 A) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.016 | 2/15 (Panc 03.27, RPMI-7951) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.023 | 7/22 (HOP62, NCI-H460, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +3.3 | 0.024 | 0/12 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.049 | 3/22 (A-427, C-33 A, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.049 | 5/23 (A-172, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10420.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (J82 0.0909×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SW 900 0.142×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -4.0 | 0.039 | 3/24 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.710× | -3.5 | 0.15 | 6/23 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | 0.708× | -3.4 | 0.15 | 4/23 (A-427, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10420. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 8.36 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.40× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.68× (z +22.1) | — |
| [[J82 (line)]] | alt | 9.27 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0909× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 2.19 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -9.4) |
| [[A-172 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.930 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.873 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.543 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.708 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.574 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.433 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.612 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.558 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10420), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALNT1]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ANGPT1]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MATN3]] | +0.60 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[ZNF300]] | +0.59 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[CHRDL1]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[POSTN]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[MTMR2]] | +0.57 | +0.38 / +0.39 | both halves | 7e-05 |  |
| [[ITGA4]] | +0.57 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[PDIA3P1]] | +0.56 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[LINC00842]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[LINC01116]] | +0.54 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[MYL9]] | +0.53 | +0.31 / +0.63 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIB1]] | -0.54 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[CIAO2B]] | -0.51 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[GSDMB]] | -0.48 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ETHE1]] | -0.48 | -0.51 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MPG]] | -0.47 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[PHLDB3]] | -0.47 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[BACE2]] | -0.47 | -0.50 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND6]] | C | BEND6 activity raises SUSD5's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 2.75× lower at baseline in the lines without BEND6 | 0.0998 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDIA3P1]] | B | SUSD5 activity raises PDIA3P1's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 1.22× lower at baseline in the lines without SUSD5 | 0.054 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9 |
| [[ACP2]] | B | SUSD5 activity raises ACP2's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 1.07× lower at baseline in the lines without SUSD5 | 0.084 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9 |
| [[MYLK]] | B | SUSD5 activity raises MYLK's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 3.35× lower at baseline in the lines without SUSD5 | 0.094 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9 |
| [[EMB]] | C | SUSD5 activity raises EMB's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 5.29× lower at baseline in the lines without SUSD5 | 0.025 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9; co-absent with the target |
| [[EFEMP1]] | C | SUSD5 activity raises EFEMP1's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 3.98× lower at baseline in the lines without SUSD5 | 0.062 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (57.8, 22.1); signed map (43.1, 21.4). **Vector** length 38.4, 6.54% of its response variance represented; |z| ≥ 3 in 470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +15.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.8 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.7 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.7 | -4.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -0.7 | -0.7 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | sushi domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.3 — chr3:33,150,043-33,218,810 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0527 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

UniProt [O60279](https://www.uniprot.org/uniprotkb/O60279) carries no function annotation.

**Summary**, from NCBI Gene [26032](https://www.ncbi.nlm.nih.gov/gene/26032):

> Predicted to enable hyaluronic acid binding activity. Predicted to be involved in Notch signaling pathway. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29061) · Entrez [26032](https://www.ncbi.nlm.nih.gov/gene/26032) · UniProt [O60279](https://www.uniprot.org/uniprotkb/O60279) · Ensembl [ENSG00000173705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173705)

## Data

Gene col 10420: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10420); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10420, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10420]; `tensor/DDL_lfc|DDL_z.npy` [10420]; `embed/gene_vectors.npy` [10420]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10420 or target_col == 10420). Every well: [[SUSD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUSD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
