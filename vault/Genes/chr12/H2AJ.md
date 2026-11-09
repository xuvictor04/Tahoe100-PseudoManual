---
symbol: "H2AJ"
type: "gene"
col: 14471
ensembl_id: "ENSG00000246705"
name: "H2A.J histone"
location: "12p12.3"
module: 68
arm: "+"
pooled_cpm: 11.42
n_lines_expressing: 39
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 7
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# H2AJ

*H2A.J histone* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.01× (z +13.9, q 3e-41, up in 33 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-A]] (+0.67, fdr 1e-05), [[HHLA3]] (+0.66, fdr 7e-06), [[POLR1H]] (+0.63, fdr 7e-06); moves opposite to [[FBXW2]] (-0.62, fdr 1e-05), [[OPA1]] (-0.61, fdr 9e-06), [[HERC2P3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[THOC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +13.9 | 3e-41 | 33/34 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **3.78×** | +13.3 | 5e-38 | 31/35 (LOX-IMVI, C32, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **4.06×** | +9.5 | 3e-19 | 34/36 (A-427, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.48×** | +8.8 | 1e-16 | 28/30 (PANC-1, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.58×** | +6.4 | 1e-08 | 18/21 (LS 180, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.40×** | +6.2 | 5e-08 | 25/35 (SW1417, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +6.2 | 6e-08 | 26/37 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +6.1 | 6e-08 | 27/32 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +5.9 | 3e-07 | 29/35 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.23×** | +5.7 | 8e-07 | 25/37 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.36×** | +5.6 | 1e-06 | 15/24 (NCI-H1573, SW480, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +5.5 | 2e-06 | 28/33 (MIA PaCa-2, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | **2.14×** | +5.4 | 3e-06 | 23/29 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.95×** | +4.7 | 1e-04 | 24/34 (SW1417, PANC-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.93×** | +4.7 | 1e-04 | 24/36 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.008 | 16/37 (HOP62, Hs 766T, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.5 | 0.013 | 17/37 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.080 | 14/36 (MIA PaCa-2, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.616× | -3.2 | 0.35 | 17/36 (NCI-H1573, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.635× | -3.2 | 0.35 | 18/37 (LS 180, NCI-H1573, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.629× | -3.1 | 0.35 | 16/37 (LS 180, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.79 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +10.4) | — |
| [[A498 (line)]] | wt | 9.46 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +11.0) | — |
| [[A549 (line)]] | wt | 22.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 5.74 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.45× (z +10.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 14.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.26× (z +11.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +8.7) | — |
| [[KATO III (line)]] | alt | 47.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +10.7) | — |
| [[LoVo (line)]] | wt | 14.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 9.29 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.10× (z +12.8) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 17.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +11.4) | — |
| [[PANC-1 (line)]] | alt | 7.57 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.90× (z +13.3) | — |
| [[SW480 (line)]] | alt | 12.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.30× (z +12.2) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +9.7) | — |
| [[A-427 (line)]] | wt | 29.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.92× (z +8.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C32 (line)]] | wt | 9.06 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +12.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[CFPAC-1 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.38× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.87× (z +8.7) | — |
| [[J82 (line)]] | alt | 8.72 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +9.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +10.2) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SW 900 (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 32.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +11.5) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A-172 (line)]] | wt | 0.935 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.998 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.908 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-A]] | +0.67 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[HHLA3]] | +0.66 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[POLR1H]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 | pathway: B-WICH complex positively regulates rRNA expression; STRING 492 |
| [[SMDT1]] | +0.62 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[B2M]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[UNK]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TBCC]] | +0.59 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.59 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[EMC9]] | +0.59 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[STAP2]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[RSF1]] | +0.59 | +0.54 / +0.54 | both halves | 1e-05 | pathway: Chromosome Maintenance |
| [[PNRC1]] | +0.58 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.62 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[OPA1]] | -0.61 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[HERC2P3]] | -0.60 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.59 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[HERC2]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[CCT3]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[HSPD1]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[CHCHD6]] | -0.58 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[DCAF13]] | -0.58 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.57 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CACYBP]] | -0.57 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TCOF1]] | -0.57 | -0.54 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers H2AJ's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THOC5]] | B | H2AJ activity lowers THOC5's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.42× higher at baseline in the lines without H2AJ | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[CDKN1B]] | B | H2AJ activity raises CDKN1B's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without H2AJ | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[PPM1F]] | B | H2AJ activity lowers PPM1F's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.37× higher at baseline in the lines without H2AJ | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[MSX2]] | B | H2AJ activity raises MSX2's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without H2AJ | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[CCT3]] | B | H2AJ activity lowers CCT3's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.33× higher at baseline in the lines without H2AJ | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[UNC79]] | B | H2AJ activity lowers UNC79's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.99× higher at baseline in the lines without H2AJ | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |
| [[HERC2P3]] | B | H2AJ activity lowers HERC2P3's level | lines that do not express H2AJ (11) vs lines expressing it (39) | 1.50× higher at baseline in the lines without H2AJ | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321 |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-2.3, -28.1); signed map (13.3, -7.5). **Vector** length 70.5, 19.1% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +6.4 | +13.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +13.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.0 | +9.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.1 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.0 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -3.4 | -3.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | -3.1 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -2.8 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | +1.3 |

## What is on record

|  |  |
|---|---|
| Name | H2A.J histone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:14,774,405-14,778,002 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10903, MGC921; previously H2AFJ |
| Gene groups (HGNC) | H2A histones |
| Hallmark sets | P53_PATHWAY |
| Reactome | 108 pathways, smallest: ChAHP complex assembly; DNA methylation; RNA Polymerase I Promoter Opening |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTM1](https://www.uniprot.org/uniprotkb/Q9BTM1) (Histone H2A.J):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.

**Summary**, from NCBI Gene [55766](https://www.ncbi.nlm.nih.gov/gene/55766):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene is located on chromosome 12 and …

**Accessions** — [HGNC:14456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14456) · Entrez [55766](https://www.ncbi.nlm.nih.gov/gene/55766) · UniProt [Q9BTM1](https://www.uniprot.org/uniprotkb/Q9BTM1) · Ensembl [ENSG00000246705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000246705)

## Data

Gene col 14471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14471); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14471]; `tensor/DDL_lfc|DDL_z.npy` [14471]; `embed/gene_vectors.npy` [14471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14471 or target_col == 14471). Every well: [[H2AJ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AJ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
