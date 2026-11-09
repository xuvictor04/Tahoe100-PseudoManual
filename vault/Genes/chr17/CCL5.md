---
symbol: "CCL5"
type: "gene"
col: 15685
ensembl_id: "ENSG00000271503"
name: "C-C motif chemokine ligand 5"
location: "17q12"
module: 14
arm: "+"
pooled_cpm: 28.58
n_lines_expressing: 28
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CCL5

*C-C motif chemokine ligand 5* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.90× (z +20.9, q 0e+00, up in 22 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.489× (z -5.1, q 2e-04, down in 14 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-F]] (+0.74, fdr 7e-06), [[IFIH1]] (+0.73, fdr 7e-06), [[SLC2A6]] (+0.72, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NEURL3]] → it (grade B ⚠); 11 go from it, the strongest it → cells under [[Naproxen (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15685.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.90×** | +20.9 | 0e+00 | 22/26 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **7.28×** | +13.6 | 8e-40 | 21/25 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.00×** | +11.5 | 3e-28 | 19/25 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.96×** | +9.8 | 1e-20 | 21/25 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +6.8 | 1e-09 | 9/22 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +6.5 | 6e-09 | 15/26 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.25×** | +5.8 | 6e-07 | 16/25 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +4.4 | 7e-04 | 6/18 (J82, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.65×** | +3.6 | 0.022 | 9/25 (NCI-H460, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.027 | 7/25 (A549, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.035 | 5/26 (A549, H4, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.63×** | +3.4 | 0.035 | 6/25 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.56×** | +3.2 | 0.062 | 10/25 (NCI-H460, A498, …) | inconsistent across doses | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15685.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.489×** | -5.1 | 2e-04 | 14/25 (A498, HS-578T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.631×** | -4.6 | 0.001 | 16/26 (HS-578T, A549, …) | top dose only | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.544×** | -4.3 | 0.003 | 11/25 (A498, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.549×** | -4.3 | 0.003 | 14/25 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.558×** | -4.2 | 0.004 | 13/25 (J82, A498, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.685×** | -3.8 | 0.012 | 10/26 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.586×** | -3.8 | 0.012 | 10/25 (A498, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.631×** | -3.3 | 0.074 | 11/25 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.67 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15685. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 84.8 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.78× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0780× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 138 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 16.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +16.0) | — |
| [[J82 (line)]] | alt | 76.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.7× (z +23.7) | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.6× (z +17.2) | — |
| [[PANC-1 (line)]] | alt | 10.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 24.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +15.7) | — |
| [[SW 900 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +13.0) | — |
| [[A498 (line)]] | wt | 64.1 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 8.49× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 51.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.202× (z -8.9) ⚠ cell-cycle shift, explains ~58% of this change |
| [[HT-29 (line)]] | alt | 14.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 70.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 9.56 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0675× (z -8.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[NCI-H2030 (line)]] | alt | 134 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +9.2) | — |
| [[A-427 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 74.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.39 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15685), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-F]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 | STRING 437 |
| [[IFIH1]] | +0.73 | +0.67 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 765 |
| [[SLC2A6]] | +0.72 | +0.68 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CXCL10]] | +0.72 | +0.61 / +0.76 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 999 |
| [[GBP4]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 429 |
| [[TNFAIP2]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP5]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 | STRING 516 |
| [[HLA-B]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 496 |
| [[PSMB9]] | +0.70 | +0.66 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT; STRING 449 |
| [[NINJ1]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GCA]] | +0.70 | +0.70 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[PSME2]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 6, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL3]] | B | NEURL3 activity raises CCL5's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 4.04× lower at baseline in the lines without NEURL3 | 0.014 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[OASL]] | B | OASL activity raises CCL5's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.87× lower at baseline in the lines without OASL | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[CXCL3]] | B | CXCL3 activity raises CCL5's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.28× lower at baseline in the lines without CXCL3 | 0.045 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[IFIT2]] | B | IFIT2 activity raises CCL5's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 4.09× lower at baseline in the lines without IFIT2 | 0.051 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[TOP2A]] | B | TOP2A activity lowers CCL5's level | compounds that target TOP2A: 3 of 5 raise it (Amsacrine, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises CCL5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCL3]] | C | CCL3 activity raises CCL5's level | lines that do not express CCL3 (37) vs lines expressing it (13) | 5.27× lower at baseline in the lines without CCL3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1; co-absent with the target |
| [[CXCL10]] | C | CXCL10 activity raises CCL5's level | lines that do not express CXCL10 (23) vs lines expressing it (27) | 3.73× lower at baseline in the lines without CXCL10 | 0.022 | ⚠ within organs, on part of the lines; also absent: PTGFR, ESRRG, LYPD1; maybe low, not absent; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises CCL5's level | lines that do not express IL7R (30) vs lines expressing it (20) | 4.55× lower at baseline in the lines without IL7R | 0.044 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Naproxen (drug)]] 5 µM | B | CCL5 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.82× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[TRAF1]] | B | CCL5 activity raises TRAF1's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 3.03× lower at baseline in the lines without CCL5 | 0.056 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[NFIX]] | B | CCL5 activity raises NFIX's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without CCL5 | 0.057 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| cells under [[Lidocaine (hydrochloride) (drug)]] 0.05 µM | B | CCL5 activity lowers the cells' numbers under Lidocaine (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 1.37× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| cells under [[Irinotecan (hydrochloride) (drug)]] 5 µM | B | CCL5 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[OASL]] | B | CCL5 activity raises OASL's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 2.67× lower at baseline in the lines without CCL5 | 0.083 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| cells under [[Procainamide (hydrochloride) (drug)]] 5 µM | B | CCL5 activity raises the cells' numbers under Procainamide (hydrochloride) 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.84× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| cells under [[Rucaparib (phosphate) (drug)]] 5 µM | B | CCL5 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.79× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| cells under [[Salicylic acid (drug)]] 5 µM | B | CCL5 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 1.17× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[CXCL10]] | C | CCL5 activity raises CXCL10's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without CCL5 | 0.059 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1; co-absent with the target |
| [[HMGN2P46]] | C | CCL5 activity raises HMGN2P46's level | lines that do not express CCL5 (22) vs lines expressing it (28) | 3.74× lower at baseline in the lines without CCL5 | 0.078 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.0, 2.9); signed map (44.0, 9.9). **Vector** length 72.1, 20.1% of its response variance represented; |z| ≥ 3 in 523 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NF-kB* (control, mean cos +0.50 to 12); *IL6 JAK STAT3 signaling* (hallmark, mean cos +0.52 to 11); *TNFR2 non-canonical NF-kB pathway* (reactome, mean cos +0.51 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +20.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +11.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.8 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -2.9 | -4.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -4.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | C-C motif chemokine ligand 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,871,491-35,880,793 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RANTES, SISd, TCP228, MGC17164; previously D17S136E, SCYA5 |
| Gene groups (HGNC) | Chemokine ligands |
| Hallmark sets | ALLOGRAFT_REJECTION, INFLAMMATORY_RESPONSE, COMPLEMENT, INTERFERON_GAMMA_RESPONSE, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 10 pathways, smallest: Chemokine receptors bind chemokines; Interleukin-10 signaling; Peptide ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P13501](https://www.uniprot.org/uniprotkb/P13501) (C-C motif chemokine 5):

> Chemoattractant for blood monocytes, memory T-helper cells and eosinophils. Causes the release of histamine from basophils and activates eosinophils. May activate several chemokine receptors including CCR1, CCR3, CCR4 and CCR5. One of the major HIV-suppressive factors produced by CD8+ T-cells. Recombinant RANTES protein induces a dose-dependent inhibition of different strains of HIV-1, HIV-2, and simian immunodeficiency virus (SIV). The processed form RANTES(3-68) acts as a natural chemotaxis …

**Summary**, from NCBI Gene [6352](https://www.ncbi.nlm.nih.gov/gene/6352):

> This gene is one of several chemokine genes clustered on the q-arm of chromosome 17. Chemokines form a superfamily of secreted proteins involved in immunoregulatory and inflammatory processes. The superfamily is divided into four subfamilies based on the arrangement of the N-terminal cysteine residues of the mature peptide. This chemokine, a member of the CC subfamily, functions as a chemoattractant for blood monocytes, memory T helper cells and eosinophils. It causes the release of histamine …

**Accessions** — [HGNC:10632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10632) · Entrez [6352](https://www.ncbi.nlm.nih.gov/gene/6352) · UniProt [P13501](https://www.uniprot.org/uniprotkb/P13501) · Ensembl [ENSG00000271503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000271503)

## Data

Gene col 15685: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15685); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15685, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15685]; `tensor/DDL_lfc|DDL_z.npy` [15685]; `embed/gene_vectors.npy` [15685]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15685 or target_col == 15685). Every well: [[CCL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
