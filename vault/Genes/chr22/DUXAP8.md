---
symbol: "DUXAP8"
type: "gene"
col: 13038
ensembl_id: "ENSG00000206195"
name: "double homeobox A pseudogene 8"
location: "22q11.1"
module: 33
arm: "+"
pooled_cpm: 12.01
n_lines_expressing: 43
n_dd_up: 1
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 17
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# DUXAP8

*double homeobox A pseudogene 8* — 22q11.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.45× (z +4.3, q 0.010, up in 12 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.643× (z -7.4, q 8e-11, down in 25 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.313×, LOX-IMVI 0.256×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0565×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0722×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUXAP9]] (+0.88, fdr 7e-06), [[WDR36]] (+0.60, fdr 1e-05), [[NBEAP2]] (+0.58, fdr 2e-05); moves opposite to [[ING2]] (-0.61, fdr 1e-05), [[ZMYM5]] (-0.58, fdr 2e-05), [[IRX5]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DUXAP10]] → it (grade C ⚠); 17 go from it, the strongest it → [[SFXN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.010 | 12/40 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.37× | +3.5 | 0.15 | 14/40 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.22× | +3.3 | 0.22 | 11/41 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13038.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.313×, LOX-IMVI 0.256×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.127×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 5 µM in 1 line (HepG2/C3A 0.0565×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0722×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -7.4 | 8e-11 | 25/39 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.657×** | -7.0 | 5e-10 | 25/39 (PANC-1, MIA PaCa-2, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.522×** | -6.6 | 6e-09 | 22/40 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -3.7 | 0.029 | 15/39 (HCT15, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.827× | -3.2 | 0.15 | 14/40 (CHP-212, H4, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0565× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Pioglitazone (drug)]] 0.5 µM 0.0654× (z -11.6) |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 2 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0722× (z -10.7) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -9.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.105× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 25.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 6.33 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.110× (z -9.1) |
| [[PANC-1 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -11.3) ⚠ cell-cycle shift, explains ~69% of this change |
| [[RKO (line)]] | wt | 44.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.5) |
| [[SW480 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP9]] | +0.88 | +0.84 / +0.89 | both halves | 7e-06 | same gene group |
| [[WDR36]] | +0.60 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[NBEAP2]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MRPL42]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CCT2]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[KAT2A]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[METTL3]] | +0.56 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RPE]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CLNS1A]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PFKM]] | +0.56 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[RPSA]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ADAT2]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING2]] | -0.61 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[ZMYM5]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[IRX5]] | -0.56 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[KLHL22]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NUMB]] | -0.54 | -0.36 / -0.53 | both halves | 9e-05 |  |
| [[FAM193A]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SHOC2]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[UBN1]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[DLEU2]] | -0.51 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[RBX1]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[MTHFR]] | -0.49 | -0.46 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP10]] | C | DUXAP10 activity raises DUXAP8's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 4.91× lower at baseline in the lines without DUXAP10 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9; co-absent with the target |
| [[DUXAP9]] | C | DUXAP9 activity raises DUXAP8's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 4.67× lower at baseline in the lines without DUXAP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent; co-absent with the target |
| [[EID2]] | C | EID2 activity raises DUXAP8's level | lines that do not express EID2 (3) vs lines expressing it (47) | 5.00× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent; its own permutation p |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFXN4]] | B | DUXAP8 activity raises SFXN4's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.91× lower at baseline in the lines without DUXAP8 | 0.009 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[CARNMT1]] | B | DUXAP8 activity raises CARNMT1's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without DUXAP8 | 0.011 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[DTD2]] | B | DUXAP8 activity raises DTD2's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.83× lower at baseline in the lines without DUXAP8 | 0.014 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[ADAT2]] | B | DUXAP8 activity raises ADAT2's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without DUXAP8 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[METTL3]] | B | DUXAP8 activity raises METTL3's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.36× lower at baseline in the lines without DUXAP8 | 0.047 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[EBPL]] | B | DUXAP8 activity raises EBPL's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.46× lower at baseline in the lines without DUXAP8 | 0.048 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[HEATR1]] | B | DUXAP8 activity raises HEATR1's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.53× lower at baseline in the lines without DUXAP8 | 0.067 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[SHOC2]] | B | DUXAP8 activity strengthens SHOC2's drug response | lines that do not express DUXAP8 (7) vs lines expressing it (42) | the lines without DUXAP8 respond 0.89× as strongly (z diff +1.27); strongest at Panobinostat 5 µM: 1.07x vs 1.38x (z diff +3.5) | 0.068 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2; target measured in part of the lines; artifact flags |
| [[RPE]] | B | DUXAP8 activity raises RPE's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without DUXAP8 | 0.069 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[LRPPRC]] | B | DUXAP8 activity raises LRPPRC's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.50× lower at baseline in the lines without DUXAP8 | 0.080 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[ZC3HAV1L]] | B | DUXAP8 activity raises ZC3HAV1L's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.38× lower at baseline in the lines without DUXAP8 | 0.082 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |
| [[NKRF]] | B | DUXAP8 activity raises NKRF's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without DUXAP8 | 0.083 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.1, -29.6); signed map (-17.1, -47.5). **Vector** length 60.1, 10.2% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -0.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.6 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | -0.4 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | +0.9 | +2.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.4 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | -3.1 | -7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.0 | -7.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -0.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | double homeobox A pseudogene 8 |
| Locus type | pseudogene |
| Location | 22q11.1 — chr22:15,784,959-15,829,984 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes |
| Matched by | symbol |

**Summary**, from NCBI Gene [503637](https://www.ncbi.nlm.nih.gov/gene/503637):

> Homeobox genes encode DNA-binding proteins, many of which are thought to be involved in early embryonic development. Homeobox genes encode a DNA-binding domain of 60 to 63 amino acids referred to as the homeodomain. This pseudogene is a member of the DUXA homeobox gene family. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:32187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32187) · Entrez [503637](https://www.ncbi.nlm.nih.gov/gene/503637) · Ensembl [ENSG00000206195](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000206195)

## Data

Gene col 13038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13038); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13038]; `tensor/DDL_lfc|DDL_z.npy` [13038]; `embed/gene_vectors.npy` [13038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13038 or target_col == 13038). Every well: [[DUXAP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUXAP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
