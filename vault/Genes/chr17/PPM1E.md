---
symbol: "PPM1E"
type: "gene"
col: 10574
ensembl_id: "ENSG00000175175"
name: "protein phosphatase, Mg2+/Mn2+ dependent 1E"
location: "17q24.2"
module: 61
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 34
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 36
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PPM1E

*protein phosphatase, Mg2+/Mn2+ dependent 1E* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.00× (z +31.9, q 0e+00, up in 25 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.139×, SHP-77 0.281×, A-427 0.194×, PANC-1 0.330×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.296×, SHP-77 0.348×, C-33 A 0.366×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (PANC-1 0.145×, A-427 0.0682×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.342×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (A549 0.0923×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEFF2]] (+0.58, fdr 7e-06), [[SH3GL2]] (+0.54, fdr 4e-05), [[INPP1]] (+0.53, fdr 2e-04); moves opposite to [[DZANK1]] (-0.45, fdr 5e-04), [[NELFE]] (-0.41, fdr 3e-04), [[LRRC47]] (-0.38, fdr 6e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[GNAO1]] → it (grade B ⚠); 4 go from it, the strongest it → [[UGT1A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.00×** | +31.9 | 0e+00 | 25/31 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **5.53×** | +24.0 | 0e+00 | 30/31 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.78×** | +20.3 | 0e+00 | 29/31 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.15×** | +20.0 | 0e+00 | 28/31 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.63×** | +18.1 | 0e+00 | 29/31 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +16.9 | 0e+00 | 23/30 (HCT15, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.01×** | +15.4 | 0e+00 | 28/31 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.76×** | +14.2 | 6e-44 | 26/31 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.42×** | +12.4 | 1e-33 | 10/23 (CFPAC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +12.3 | 4e-33 | 17/29 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.38×** | +12.1 | 4e-32 | 21/31 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.36×** | +10.8 | 2e-25 | 24/31 (NCI-H460, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.05×** | +9.7 | 1e-20 | 6/15 (CFPAC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.00×** | +9.7 | 1e-20 | 20/29 (J82, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +9.5 | 6e-20 | 16/30 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +9.4 | 2e-19 | 21/32 (A498, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +8.6 | 2e-16 | 14/30 (NCI-H460, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10574.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (C-33 A 0.139×, SHP-77 0.281×, A-427 0.194×, PANC-1 0.330×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (PANC-1 0.296×, SHP-77 0.348×, C-33 A 0.366×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[TAK-901 (drug)]] 5 µM in 2 lines (PANC-1 0.145×, A-427 0.0682×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.342×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (A549 0.0923×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.847× | -3.3 | 0.50 | 6/31 (HCT15, A498, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.1 | 0.50 | 5/32 (HCT15, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.24 | 9 | 0 | [[Panobinostat (drug)]] 5 µM 26.5× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 7.58 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 24.0× (z +14.5) | — |
| [[PANC-1 (line)]] | alt | 59.9 | 1 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.342× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 8 | 0 | [[Panobinostat (drug)]] 5 µM 25.1× (z +14.6) | — |
| [[A549 (line)]] | wt | 6.13 | 6 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +12.3) | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0923× (z -8.6) |
| [[J82 (line)]] | alt | 19.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +13.6) | — |
| [[A-172 (line)]] | wt | 9.47 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 13.9× (z +11.8) | — |
| [[BT-474 (line)]] | alt | 21.7 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 8.61× (z +13.8) | — |
| [[C-33 A (line)]] | alt | 101 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 27.9 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.08× (z +10.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0482× (z -19.3) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 7.10 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +17.5) | — |
| [[CFPAC-1 (line)]] | alt | 5.09 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 25.1× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 3.89 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 23.1× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 35.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 4.65 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.83 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 8.03× (z +10.3) | — |
| [[CHP-212 (line)]] | wt | 38.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 26.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.03× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[C32 (line)]] | wt | 4.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +12.0) | — |
| [[HCT15 (line)]] | alt | 6.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.41× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEFF2]] | +0.58 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[SH3GL2]] | +0.54 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[INPP1]] | +0.53 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[ZNF536]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[GPM6A]] | +0.50 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[KCNG3]] | +0.50 | +0.50 / +0.57 | both halves | 1e-05 | pathway: Neuronal System |
| [[SNTG2]] | +0.49 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[WDR17]] | +0.49 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[ELOVL4]] | +0.48 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[CLGN]] | +0.48 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[RGS7]] | +0.48 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PTPRO]] | +0.47 | +0.40 / +0.56 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZANK1]] | -0.45 | -0.24 / -0.39 | both halves | 5e-04 |  |
| [[NELFE]] | -0.41 | -0.29 / -0.44 | both halves | 3e-04 |  |
| [[LRRC47]] | -0.38 | -0.22 / -0.39 | both halves | 6e-04 |  |
| [[B4GALT7]] | -0.38 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAO1]] | B | GNAO1 activity raises PPM1E's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.37× lower at baseline in the lines without GNAO1 | 0.042 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |
| [[TOP2A]] | B | TOP2A activity lowers PPM1E's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MED12L]] | C | MED12L activity raises PPM1E's level | lines that do not express MED12L (18) vs lines expressing it (32) | 3.08× lower at baseline in the lines without MED12L | 0.048 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[KCNG3]] | C | KCNG3 activity raises PPM1E's level | lines that do not express KCNG3 (20) vs lines expressing it (30) | 2.46× lower at baseline in the lines without KCNG3 | 0.063 | ⚠ within organs, on part of the lines; also absent: ELOVL2, LHX2, MAPK8IP2; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT1A1]] | B | PPM1E activity lowers UGT1A1's level | lines that do not express PPM1E (16) vs lines expressing it (34) | 3.03× higher at baseline in the lines without PPM1E | 0.031 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| [[LINC01133]] | B | PPM1E activity lowers LINC01133's level | lines that do not express PPM1E (16) vs lines expressing it (34) | 3.14× higher at baseline in the lines without PPM1E | 0.039 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| [[TLL1]] | B | PPM1E activity lowers TLL1's level | lines that do not express PPM1E (16) vs lines expressing it (34) | 1.08× higher at baseline in the lines without PPM1E | 0.067 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| cells under [[Panobinostat (drug)]] 0.5 µM | B | PPM1E activity raises the cells' numbers under Panobinostat 0.5 µM (protects the cells) | lines that do not express PPM1E (16) vs lines expressing it (32) | the lines without PPM1E: 0.88× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.8, 32.5); signed map (33.0, 24.6). **Vector** length 66.6, 13.3% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +20.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +5.0 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +4.6 | +12.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +8.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +9.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +3.6 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.0 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase, Mg2+/Mn2+ dependent 1E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:58,755,854-58,985,179 (+) |
| Ensembl biotype | protein_coding |
| Also known as | POPX1, KIAA1072, PP2CH, CaMKP-N |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Reactome | 5 pathways, smallest: Negative regulation of NMDA receptor-mediated neuronal transmission; Activation of NMDA receptors and postsynaptic events; Neurotransmitter receptors and postsynaptic signal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WY54](https://www.uniprot.org/uniprotkb/Q8WY54) (Protein phosphatase 1E):

> Protein phosphatase that inactivates multifunctional CaM kinases such as CAMK4 and CAMK2 (By similarity). Dephosphorylates and inactivates PAK. May play a role in the inhibition of actin fiber stress breakdown and in morphological changes driven by TNK2/CDC42. Dephosphorylates PRKAA2 (By similarity).

**Summary**, from NCBI Gene [22843](https://www.ncbi.nlm.nih.gov/gene/22843):

> This gene encodes a member of the PPM family of serine/threonine-protein phosphatases. The encoded protein is localized to the nucleus and dephosphorylates and inactivates multiple substrates including serine/threonine-protein kinase PAK 1, 5'-AMP-activated protein kinase (AMPK) and the multifunctional calcium/calmodulin-dependent protein kinases. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:19322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19322) · Entrez [22843](https://www.ncbi.nlm.nih.gov/gene/22843) · UniProt [Q8WY54](https://www.uniprot.org/uniprotkb/Q8WY54) · Ensembl [ENSG00000175175](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175175)

## Data

Gene col 10574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10574); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10574]; `tensor/DDL_lfc|DDL_z.npy` [10574]; `embed/gene_vectors.npy` [10574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10574 or target_col == 10574). Every well: [[PPM1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPM1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
