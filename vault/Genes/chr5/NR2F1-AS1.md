---
symbol: "NR2F1-AS1"
type: "gene"
col: 14119
ensembl_id: "ENSG00000237187"
name: "NR2F1 regulatory antisense RNA 1"
location: "5q15"
module: 202
arm: "+"
pooled_cpm: 79.74
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/202"]
generated_by: "tahoemap"
---

# NR2F1-AS1

*NR2F1 regulatory antisense RNA 1* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +7.7, q 9e-12, up in 20 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.388× (z -12.0, q 1e-30, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA2D1]] (+0.65, fdr 1e-05), [[RIMS2]] (+0.62, fdr 1e-05), [[TCF12]] (+0.61, fdr 1e-05); moves opposite to [[PRUNE1]] (-0.62, fdr 1e-05), [[SLC35A1]] (-0.60, fdr 1e-05), [[LCMT1]] (-0.58, fdr 3e-05).
> It is in [[Module 202]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NR2F1]] → it (grade C ⚠); 4 go from it, the strongest it → [[LZIC]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.7 | 9e-12 | 20/40 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.1 | 4e-10 | 22/40 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +5.2 | 4e-05 | 23/40 (SK-MEL-2, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.388×** | -12.0 | 1e-30 | 34/40 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.408×** | -11.4 | 1e-27 | 37/40 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.410×** | -11.3 | 2e-27 | 33/40 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.638×** | -5.7 | 1e-06 | 23/40 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.640×** | -5.7 | 1e-06 | 27/39 (A-172, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.685×** | -4.8 | 1e-04 | 21/40 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.677×** | -4.8 | 1e-04 | 25/39 (NCI-H2030, A-427, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.031 | 22/40 (A-427, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.778×** | -3.2 | 0.083 | 19/40 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.782×** | -3.1 | 0.088 | 18/40 (A-427, J82, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.783×** | -3.1 | 0.088 | 20/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | 0.779× | -3.1 | 0.10 | 19/39 (Hs 766T, J82, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 561 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.106× (z -24.5) |
| [[C-33 A (line)]] | alt | 439 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0759× (z -24.0) |
| [[MIA PaCa-2 (line)]] | alt | 264 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0941× (z -17.0) |
| [[LS 180 (line)]] | wt | 62.2 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.310× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 33.4 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +18.5) | — |
| [[HS-578T (line)]] | alt | 120 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.202× (z -11.7) |
| [[J82 (line)]] | alt | 135 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.163× (z -12.9) |
| [[SHP-77 (line)]] | alt | 115 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -15.3) |
| [[A-172 (line)]] | wt | 126 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -11.6) |
| [[C32 (line)]] | wt | 90.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.355× (z -9.7) |
| [[Hs 766T (line)]] | wt | 56.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -9.6) |
| [[LoVo (line)]] | wt | 37.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.17× (z +22.4) | — |
| [[NCI-H1792 (line)]] | alt | 91.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 76.5 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -15.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 71.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +24.2) | — |
| [[SK-MEL-2 (line)]] | alt | 42.8 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 18.0× (z +19.9) | — |
| [[A498 (line)]] | wt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +14.3) | — |
| [[CFPAC-1 (line)]] | alt | 53.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.45× (z +21.1) | — |
| [[RPMI-7951 (line)]] | alt | 70.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 111 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +14.4) | — |
| [[SW480 (line)]] | alt | 27.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.9) | [[Panobinostat (drug)]] 5 µM 0.325× (z -9.1) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0978× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[AsPC-1 (line)]] | alt | 52.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.266× (z -9.6) |
| [[HOP62 (line)]] | alt | 56.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 32.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.394× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 66.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -14.5) |
| [[NCI-H596 (line)]] | alt | 72.5 | 1 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 11.8× (z +9.7) | — |
| [[NCI-H661 (line)]] | alt | 245 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.146× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 45.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -8.8) |
| [[PANC-1 (line)]] | alt | 87.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 137 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.355× (z -8.5) |
| [[SW48 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.101× (z -8.9) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A549 (line)]] | wt | 19.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.77 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.32 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 54.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D1]] | +0.65 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[RIMS2]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TCF12]] | +0.61 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TASOR]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[IPO9-AS1]] | +0.60 | +0.61 / +0.34 | both halves | 1e-04 | same gene group |
| [[SALL1]] | +0.59 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DLGAP4-AS1]] | +0.59 | +0.57 / +0.32 | both halves | 2e-04 | same gene group |
| [[E2F3]] | +0.58 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[TENM3-AS1]] | +0.58 | +0.50 / +0.43 | both halves | 3e-05 | same gene group |
| [[ZNF804A]] | +0.58 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LINC01776]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ITPR2-AS1]] | +0.57 | +0.52 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRUNE1]] | -0.62 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[SLC35A1]] | -0.60 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[LCMT1]] | -0.58 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[STX7]] | -0.58 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[NPRL2]] | -0.57 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NBPF3]] | -0.56 | -0.43 / -0.40 | both halves | 4e-05 |  |
| [[EDEM2]] | -0.55 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[HSDL1]] | -0.55 | -0.39 / -0.43 | both halves | 6e-05 |  |
| [[MFSD9]] | -0.55 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PCTP]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GMCL1]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[SDHAP1]] | -0.54 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F1]] | C | NR2F1 activity raises NR2F1-AS1's level | lines that do not express NR2F1 (8) vs lines expressing it (42) | 4.79× lower at baseline in the lines without NR2F1 | 0.031 | ⚠ within organs, on part of the lines; also absent: NR2F1-AS1, PCDH15; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LZIC]] | B | NR2F1-AS1 activity raises LZIC's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.16× lower at baseline in the lines without NR2F1-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |
| [[PCTP]] | B | NR2F1-AS1 activity lowers PCTP's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.57× higher at baseline in the lines without NR2F1-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |
| [[NRIP1]] | B | NR2F1-AS1 activity lowers NRIP1's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 1.64× higher at baseline in the lines without NR2F1-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15 |
| [[NR2F1]] | C | NR2F1-AS1 activity raises NR2F1's level | lines that do not express NR2F1-AS1 (8) vs lines expressing it (42) | 4.01× lower at baseline in the lines without NR2F1-AS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: TGFB1, NR2F1, PCDH15; co-absent with the target |

## Where it sits

- **Module**: [[Module 202]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.2, 7.6); signed map (27.0, 8.7). **Vector** length 111, 29.9% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | -0.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.3 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.1 | -12.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.5 | -11.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.1 | -11.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | NR2F1 regulatory antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q15 — chr5:93,360,779-93,585,649 (-) |
| Ensembl biotype | lncRNA |
| Also known as | NAS1, FLJ42709 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48622) · Entrez [441094](https://www.ncbi.nlm.nih.gov/gene/441094) · Ensembl [ENSG00000237187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237187)

## Data

Gene col 14119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14119); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14119]; `tensor/DDL_lfc|DDL_z.npy` [14119]; `embed/gene_vectors.npy` [14119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14119 or target_col == 14119). Every well: [[NR2F1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR2F1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
