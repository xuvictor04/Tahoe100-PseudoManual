---
symbol: "HSPA2"
type: "gene"
col: 4768
ensembl_id: "ENSG00000126803"
name: "heat shock protein family A (Hsp70) member 2"
location: "14q23.3"
module: 93
arm: "+"
pooled_cpm: 5.62
n_lines_expressing: 38
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/093"]
generated_by: "tahoemap"
---

# HSPA2

*heat shock protein family A (Hsp70) member 2* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.88× (z +16.3, q 0e+00, up in 30 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0434×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.164×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0858×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TENT5C]] (+0.62, fdr 1e-05), [[LGMN]] (+0.60, fdr 2e-05), [[FAM222A]] (+0.60, fdr 1e-05); moves opposite to [[AAGAB]] (-0.49, fdr 3e-05), [[TRMT61B]] (-0.48, fdr 1e-04), [[RMDN3]] (-0.46, fdr 4e-04).
> It is in [[Module 093]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SOX9]] → it (grade B ⚠); 2 go from it, the strongest it → [[FSCN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.88×** | +16.3 | 0e+00 | 30/34 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.20×** | +15.2 | 0e+00 | 30/34 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.57×** | +11.8 | 8e-30 | 26/34 (SW480, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +10.7 | 1e-24 | 19/32 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +10.7 | 1e-24 | 20/29 (SW480, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +9.7 | 3e-20 | 21/30 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.77×** | +9.0 | 2e-17 | 5/10 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.44×** | +8.2 | 2e-14 | 22/29 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +7.3 | 1e-11 | 16/34 (SW480, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +6.7 | 1e-09 | 16/22 (SW480, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **2.03×** | +6.5 | 4e-09 | 9/21 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.02×** | +6.2 | 2e-08 | 20/32 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.81×** | +5.4 | 3e-06 | 22/33 (SW480, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.75×** | +5.1 | 1e-05 | 12/35 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.69×** | +4.8 | 5e-05 | 14/34 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.1 | 0.046 | 6/24 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.05 µM |  | **1.44×** | +3.1 | 0.049 | 5/29 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.56×** | +2.9 | 0.089 | 1/27 (PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.089 | 4/29 (SW 900, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4768.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Triamcinolone (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0434×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.164×); [[Harringtonine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0858×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 0.714× | -3.1 | 0.66 | 6/20 (A498, AsPC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Econazole (drug)]] 0.5 µM |  | 0.721× | -3.0 | 0.66 | 3/34 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 7.60 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +13.6) | — |
| [[A-427 (line)]] | wt | 16.4 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 8.15× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.2) |
| [[Hs 766T (line)]] | wt | 6.15 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 12.7× (z +9.1) | [[Rapamycin (drug)]] 0.5 µM 0.0886× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 7.87 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.9× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 5.47 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.35× (z +10.1) | — |
| [[A498 (line)]] | wt | 5.23 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.18× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 30.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.59× (z +9.6) | — |
| [[A549 (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 2.29 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0635× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0434× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 5.58 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0858× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 12.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.24× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 4.83 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.14× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 5.59 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 18.2× (z +9.4) | — |
| [[SNU-423 (line)]] | alt | 3.87 | 0 | 1 | — | [[Lopinavir (drug)]] 5 µM 0.0648× (z -8.6) |
| [[A-172 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.988 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.924 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TENT5C]] | +0.62 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[LGMN]] | +0.60 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[FAM222A]] | +0.60 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[GSTM3]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_SPERMATOGENESIS |
| [[HAP1]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[SNAI1]] | +0.59 | +0.40 / +0.68 | both halves | 5e-05 |  |
| [[MYLIP]] | +0.56 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[PPP1R36]] | +0.56 | +0.66 / +0.59 | both halves | 7e-06 | ⚠ same locus (3.7 kb, same strand: neighbours can correlate without regulation) |
| [[CRISPLD2]] | +0.55 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[TNFSF9]] | +0.55 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[ATP1B1]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[VASN]] | +0.54 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[MIR9-1HG]] | +0.54 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAGAB]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[TRMT61B]] | -0.48 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[RMDN3]] | -0.46 | -0.26 / -0.57 | both halves | 4e-04 |  |
| [[EIF2B1]] | -0.46 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[MRPS35]] | -0.44 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[TIMM23B]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[MRRF]] | -0.44 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[SCO1]] | -0.43 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZNF343]] | -0.42 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[PEX26]] | -0.42 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[MAPKAPK5]] | -0.42 | -0.19 / -0.56 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NUP42]] | -0.42 | -0.22 / -0.43 | both halves | 6e-04 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 447 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX9]] | B | SOX9 activity lowers HSPA2's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.74× higher at baseline in the lines without SOX9 | 0.049 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[TOP2A]] | B | TOP2A activity lowers HSPA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYT11]] | B | SYT11 activity raises HSPA2's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without SYT11 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1 |
| [[CA8]] | B | CA8 activity raises HSPA2's level | lines that do not express CA8 (27) vs lines expressing it (23) | 1.72× lower at baseline in the lines without CA8 | 0.096 | ⚠ within organs, on part of the lines; also absent: STK32B, NKAIN3, CNKSR2 |
| [[SYNM]] | C | SYNM activity raises HSPA2's level | lines that do not express SYNM (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without SYNM | 0.069 | ⚠ within organs, on part of the lines; also absent: AKR1B1, GAMT, FHL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSCN1]] | B | HSPA2 activity raises FSCN1's level | lines that do not express HSPA2 (12) vs lines expressing it (38) | 3.37× lower at baseline in the lines without HSPA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SGCE, MICU3, TUSC3; maybe low, not absent; its own permutation p |
| [[KCNK5]] | B | HSPA2 activity lowers KCNK5's level | lines that do not express HSPA2 (12) vs lines expressing it (38) | 4.05× higher at baseline in the lines without HSPA2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SGCE, MICU3, TUSC3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 093]] — TNF-alpha signaling via NF-kB; 49 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, -27.7); signed map (1.6, 18.2). **Vector** length 55.7, 9.61% of its response variance represented; |z| ≥ 3 in 784 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +11.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +8.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +10.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family A (Hsp70) member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.3 — chr14:64,535,905-64,546,173 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Heat shock 70kDa proteins |
| Hallmark sets | SPERMATOGENESIS, UV_RESPONSE_UP |
| Reactome | 15 pathways, smallest: Attenuation phase; HSF1-dependent transactivation; Meiotic synapsis |
| Matched by | ensembl_id |

**Function**, from UniProt [P54652](https://www.uniprot.org/uniprotkb/P54652) (Heat shock-related 70 kDa protein 2):

> Molecular chaperone implicated in a wide variety of cellular processes, including protection of the proteome from stress, folding and transport of newly synthesized polypeptides, activation of proteolysis of misfolded proteins and the formation and dissociation of protein complexes. Plays a pivotal role in the protein quality control system, ensuring the correct folding of proteins, the re-folding of misfolded proteins and controlling the targeting of proteins for subsequent degradation. This …

**Summary**, from NCBI Gene [3306](https://www.ncbi.nlm.nih.gov/gene/3306):

> Enables enzyme binding activity and unfolded protein binding activity. Involved in negative regulation of inclusion body assembly and protein refolding. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5235) · Entrez [3306](https://www.ncbi.nlm.nih.gov/gene/3306) · UniProt [P54652](https://www.uniprot.org/uniprotkb/P54652) · Ensembl [ENSG00000126803](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126803)

## Data

Gene col 4768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4768); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4768]; `tensor/DDL_lfc|DDL_z.npy` [4768]; `embed/gene_vectors.npy` [4768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4768 or target_col == 4768). Every well: [[HSPA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
