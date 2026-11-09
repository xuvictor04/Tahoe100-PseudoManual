---
symbol: "DNAH11"
type: "gene"
col: 2682
ensembl_id: "ENSG00000105877"
name: "dynein axonemal heavy chain 11"
location: "7p15.3"
module: 121
arm: "+"
pooled_cpm: 30.31
n_lines_expressing: 27
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 8
direction_downstream: 20
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# DNAH11

*dynein axonemal heavy chain 11* — 7p15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.30× (z +17.1, q 0e+00, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.671× (z -5.8, q 3e-06, down in 16 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 0.113×, HOP62 0.226×, J82 0.239×, NCI-H23 0.259×, …); [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (NCI-H23 0.110×, NCI-H460 0.194×, J82 0.182×, PANC-1 0.213×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Ixazomib citrate (drug)]] 5 µM in 3 lines (CFPAC-1 0.211×, PANC-1 0.269×, NCI-H460 0.296×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.226×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAT4]] (+0.66, fdr 7e-06), [[FLRT2]] (+0.64, fdr 3e-05), [[CPED1]] (+0.62, fdr 1e-05); moves opposite to [[TMEM50B]] (-0.45, fdr 4e-05), [[SERAC1]] (-0.44, fdr 1e-04), [[ANAPC5]] (-0.44, fdr 8e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[LINC01029]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +17.1 | 0e+00 | 11/24 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +11.8 | 7e-30 | 6/19 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.73×** | +8.0 | 3e-13 | 8/24 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +6.8 | 1e-09 | 10/25 (A-172, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +6.0 | 2e-07 | 6/22 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.9 | 4e-07 | 7/25 (A549, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +5.1 | 2e-05 | 7/24 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.1 | 3e-05 | 4/25 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.9 | 5e-05 | 13/25 (A-172, HS-578T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.6 | 2e-04 | 11/25 (BT-474, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +4.3 | 9e-04 | 11/25 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 9/25 (J82, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 6/25 (A-172, HS-578T, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.1 | 0.074 | 5/25 (NCI-H2347, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2682.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 6 lines (CFPAC-1 0.113×, HOP62 0.226×, J82 0.239×, NCI-H23 0.259×, …); [[Niclosamide (olamine) (drug)]] 5 µM in 4 lines (NCI-H23 0.110×, NCI-H460 0.194×, J82 0.182×, PANC-1 0.213×; ⚠ toxic; cell-cycle shift, explains ~39% of this change); [[Ixazomib citrate (drug)]] 5 µM in 3 lines (CFPAC-1 0.211×, PANC-1 0.269×, NCI-H460 0.296×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.226×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.671×** | -5.8 | 3e-06 | 16/25 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.769×** | -3.8 | 0.034 | 17/25 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.789×** | -3.5 | 0.088 | 15/25 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.088 | 10/25 (LOX-IMVI, H4, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.799× | -3.3 | 0.12 | 10/25 (PANC-1, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 175 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -20.3) |
| [[NCI-H23 (line)]] | alt | 77.7 | 0 | 6 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.259× (z -13.2) |
| [[PANC-1 (line)]] | alt | 29.1 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.367× (z -10.0) |
| [[H4 (line)]] | wt | 122 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.238× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 92.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.296× (z -8.8) |
| [[J82 (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.3) |
| [[HS-578T (line)]] | alt | 26.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.63× (z +16.8) | — |
| [[A-172 (line)]] | wt | 17.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 50.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -13.9) |
| [[hTERT-HPNE (line)]] | wt | 27.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 68.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.217× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 60.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1573 (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.175× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -9.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW 1088 (line)]] | alt | 269 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -8.8) |
| [[A-427 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.92 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.71 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.10 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.86 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.39 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.00 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.14 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.45 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAT4]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FLRT2]] | +0.64 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[CPED1]] | +0.62 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LINC02057]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ZFHX4]] | +0.57 | +0.56 / +0.46 | both halves | 2e-05 |  |
| [[ZNF804A]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HECW2]] | +0.55 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[BASP1-AS1]] | +0.55 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[ADAMTS9-AS2]] | +0.55 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[THSD7A]] | +0.53 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[AOX1]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50B]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.44 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[ANAPC5]] | -0.44 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[MCUR1]] ⚠ | -0.43 | -0.41 / -0.38 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP7B]] | -0.42 | -0.35 / -0.27 | both halves | 3e-04 |  |
| [[DHTKD1]] | -0.42 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[CCZ1]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[E4F1]] | -0.41 | -0.33 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNAH11's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[STEAP1B-AS1]] | C | STEAP1B-AS1 activity raises DNAH11's level | lines that do not express STEAP1B-AS1 (30) vs lines expressing it (20) | 4.57× lower at baseline in the lines without STEAP1B-AS1 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, IL6, EFEMP1; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises DNAH11's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.51× lower at baseline in the lines without ODAD2 | 0.032 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[MAGI2]] | C | MAGI2 activity raises DNAH11's level | lines that do not express MAGI2 (30) vs lines expressing it (20) | 3.61× lower at baseline in the lines without MAGI2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGI2-AS3, MMP2, PHACTR1; co-absent with the target |
| [[PDGFC]] | C | PDGFC activity raises DNAH11's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 3.92× lower at baseline in the lines without PDGFC | 0.042 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11; co-absent with the target |
| [[DPY19L2]] | C | DPY19L2 activity raises DNAH11's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 4.27× lower at baseline in the lines without DPY19L2 | 0.051 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises DNAH11's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 3.48× lower at baseline in the lines without ABCC9 | 0.059 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises DNAH11's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 3.46× lower at baseline in the lines without MAGI2-AS3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01029]] | B | DNAH11 activity lowers LINC01029's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.01× higher at baseline in the lines without DNAH11 | 0.007 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[CFAP58]] | B | DNAH11 activity raises CFAP58's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.51× lower at baseline in the lines without DNAH11 | 0.023 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[NR2F2-AS1]] | B | DNAH11 activity raises NR2F2-AS1's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.82× lower at baseline in the lines without DNAH11 | 0.031 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[APH1B]] | B | DNAH11 activity raises APH1B's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.26× lower at baseline in the lines without DNAH11 | 0.033 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[ABL2]] | B | DNAH11 activity raises ABL2's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 1.79× lower at baseline in the lines without DNAH11 | 0.040 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| cells under [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.20× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[RNF217]] | B | DNAH11 activity raises RNF217's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.52× lower at baseline in the lines without DNAH11 | 0.076 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| cells under [[Imiquimod (hydrochloride) (drug)]] 0.05 µM | B | DNAH11 activity lowers the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.21× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.15× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| cells under [[Vortioxetine (drug)]] 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.20× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[PLAGL1]] | B | DNAH11 activity raises PLAGL1's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without DNAH11 | 0.086 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| cells under [[Digitoxin (drug)]] 0.05 µM | B | DNAH11 activity lowers the cells' numbers under Digitoxin 0.05 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.46× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 25.5); signed map (41.9, 27.2). **Vector** length 74.0, 19.8% of its response variance represented; |z| ≥ 3 in 668 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +17.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.3 — chr7:21,543,039-21,901,839 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Dnahc11, DPL11, CILD7, DNAHC11, DNAHBL, DNHBL |
| Gene groups (HGNC) | Dyneins, axonemal outer arm complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DT5](https://www.uniprot.org/uniprotkb/Q96DT5) (Dynein axonemal heavy chain 11):

> Force generating protein required for cilia beating in respiratory epithelia (By similarity). Produces force towards the minus ends of microtubules (By similarity). Key component of dynein, a family of motor proteins essential for movement along microtubules (By similarity). Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP (By similarity). Required for structural and functional integrity of cilia (By similarity).

**Summary**, from NCBI Gene [8701](https://www.ncbi.nlm.nih.gov/gene/8701):

> This gene encodes a ciliary outer dynein arm protein and is a member of the dynein heavy chain family. It is a microtubule-dependent motor ATPase and has been reported to be involved in the movement of respiratory cilia. Mutations in this gene have been implicated in causing Kartagener Syndrome (a combination of situs inversus totalis and Primary Ciliary Dyskinesia (PCD), also called Immotile Cilia Syndrome 1 (ICS1)) and male sterility. [provided by RefSeq, Mar 2013]

**Accessions** — [HGNC:2942](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2942) · Entrez [8701](https://www.ncbi.nlm.nih.gov/gene/8701) · UniProt [Q96DT5](https://www.uniprot.org/uniprotkb/Q96DT5) · Ensembl [ENSG00000105877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105877)

## Data

Gene col 2682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2682); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2682]; `tensor/DDL_lfc|DDL_z.npy` [2682]; `embed/gene_vectors.npy` [2682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2682 or target_col == 2682). Every well: [[DNAH11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
